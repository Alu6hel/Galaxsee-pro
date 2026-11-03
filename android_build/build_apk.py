import os
import sys
import shutil
import subprocess
import zipfile

DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(DIR)

ANDROID_SDK = os.environ.get("ANDROID_HOME", r"C:\Users\Alu\AppData\Local\Android\Sdk")
SDK_JAR = os.path.join(ANDROID_SDK, "platforms", "android-36", "android.jar")
BUILD_TOOLS_DIR = os.path.join(ANDROID_SDK, "build-tools", "36.0.0")

AAPT2 = os.path.join(BUILD_TOOLS_DIR, "aapt2.exe")
D8 = os.path.join(BUILD_TOOLS_DIR, "d8.bat")
ZIPALIGN = os.path.join(BUILD_TOOLS_DIR, "zipalign.exe")
APKSIGNER = os.path.join(BUILD_TOOLS_DIR, "apksigner.bat")

os.chdir(DIR)

# Clean
for folder in ["gen", "bin"]:
    if os.path.exists(folder):
        shutil.rmtree(folder)
for f in ["compiled_res.zip", "base_unaligned.apk", "galaxsee_pro_aligned.apk"]:
    if os.path.exists(f):
        os.remove(f)

os.makedirs("gen", exist_ok=True)
os.makedirs("bin/classes", exist_ok=True)

# Sync web assets from web_app_dist
print("Syncing web assets from web_app_dist to android_build/assets...")
web_dist = os.path.join(ROOT_DIR, "web_app_dist")
assets_dir = os.path.join(DIR, "assets")
for item in os.listdir(web_dist):
    src_item = os.path.join(web_dist, item)
    dst_item = os.path.join(assets_dir, item)
    if os.path.isdir(src_item):
        if os.path.exists(dst_item):
            shutil.rmtree(dst_item)
        shutil.copytree(src_item, dst_item)
    else:
        shutil.copy2(src_item, dst_item)

# 1. Compile resources
print("[1/6] Compiling resources with AAPT2...")
subprocess.run([AAPT2, "compile", "--dir", "res", "-o", "compiled_res.zip"], check=True)

# 2. Link APK
print("[2/6] Linking APK with AAPT2...")
subprocess.run([
    AAPT2, "link",
    "-I", SDK_JAR,
    "--manifest", "AndroidManifest.xml",
    "-A", "assets",
    "compiled_res.zip",
    "--java", "gen",
    "--auto-add-overlay",
    "-o", "base_unaligned.apk"
], check=True)

# 3. Compile Java source
print("[3/6] Compiling Java source...")
java_files = [os.path.join("gen", "com", "galaxsee", "app", "R.java")]
src_dir = os.path.join("src", "com", "galaxsee", "app")
for f in os.listdir(src_dir):
    if f.endswith(".java"):
        java_files.append(os.path.join(src_dir, f))

subprocess.run(["javac", "-source", "11", "-target", "11", "-cp", SDK_JAR, "-d", "bin/classes"] + java_files, check=True)

# 4. Generate classes.dex
print("[4/6] Generating classes.dex with D8...")
class_files = []
for root, dirs, files in os.walk("bin/classes"):
    for f in files:
        if f.endswith(".class"):
            class_files.append(os.path.join(root, f))

subprocess.run([D8] + class_files + ["--lib", SDK_JAR, "--output", "bin"], check=True, shell=True)

print("Adding classes.dex into base_unaligned.apk...")
with zipfile.ZipFile("base_unaligned.apk", "a") as z:
    z.write(os.path.join("bin", "classes.dex"), "classes.dex")

# 5. Zipalign
print("[5/6] Zipalign...")
subprocess.run([ZIPALIGN, "-p", "4", "base_unaligned.apk", "galaxsee_pro_aligned.apk"], check=True)

# 6. Sign APK
print("[6/6] Signing APK...")
keystore = "debug.keystore"
if not os.path.exists(keystore):
    subprocess.run([
        "keytool", "-genkey", "-v", "-keystore", keystore,
        "-storepass", "android", "-alias", "androiddebugkey",
        "-keypass", "android", "-keyalg", "RSA", "-keysize", "2048",
        "-validity", "10000", "-dname", "CN=Android Debug,O=Android,C=US"
    ], check=True)

out_apk = os.path.join(ROOT_DIR, "galaxsee_pro.apk")
subprocess.run([
    APKSIGNER, "sign",
    "--ks", keystore,
    "--ks-pass", "pass:android",
    "--out", out_apk,
    "galaxsee_pro_aligned.apk"
], check=True, shell=True)

print(f"\nSUCCESS! Production APK generated at: {out_apk}")
