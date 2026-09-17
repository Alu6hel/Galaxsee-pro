# 📖 Galaxsee Pro — User Manual, Feature Specification & Developer Operations Guide

---

## 1. Executive Overview & Architecture

**Galaxsee Pro** is an ultra-fast, local-first photo, video, and audio management studio engineered for 120Hz/60Hz multi-touch gesture responsiveness, deep-zoom pyramidal rendering, on-device non-destructive editing, hardware-accelerated privacy vault, and seamless multi-format transcoding.

### Core Architecture Pillars:
- **100% Local-First & Private**: Zero external telemetry, zero tracking scripts, and zero cloud lock-in. All operations run directly on your device hardware.
- **Hardware-Accelerated Physics**: 120Hz smooth pan, pinch-to-zoom, and momentum scrolling leveraging CSS hardware transforms, WebGL, and multi-threaded Web Workers.
- **Deterministic Algorithmic Engines**: Image analysis, silhouette detection, color quantization, and vectorization run mathematically without relying on unpredictable cloud AI models.

---

## 2. Interactive Navigation, Shortcuts & Gestures

### Touch Gestures (Mobile & Touchscreens):
- **Pinch-to-Grid Scale**: Seamlessly scale the gallery grid continuously from 1 column (hero detail view) up to 14 columns (dense contact sheet) using two-finger pinch/spread gestures.
- **Deep Zoom & Pan**: Pinch to zoom up to 3200% into any high-resolution image with sub-pixel bicubic interpolation. Drag with one finger to pan across gigapixel details.
- **Inertial Momentum**: Flick up or down with edge bounce physics for rapid browsing through tens of thousands of media items.
- **Long-Press Context Menu**: Long-press any thumbnail to open the quick-action menu (Inspect EXIF, Edit, Convert to SVG, Add to Vault, Favorite).

### Keyboard Shortcuts (Desktop & Chromebook):

| Shortcut | Context | Action |
|---|---|---|
| `1` – `6` | Gallery View | Set grid column density (1 = 1 col, 2 = 2 col ... 6 = 8+ col) |
| `Space` | Gallery View | Quick-look photo preview |
| `Enter` / Double Click | Gallery / Grid | Open photo in full-screen detail inspector |
| `Esc` | Viewer / Modal | Close modal, inspector, or exit full-screen |
| `Arrow Left` / `Arrow Right` | Viewer | Navigate to previous / next photo |
| `E` | Viewer / Selection | Open **Pro Non-Destructive Editing Studio** |
| `I` | Viewer / Selection | Toggle **EXIF & Histogram Inspector** |
| `C` | Multiple Selected | Launch **Multi-Photo Compare Studio** |
| `Ctrl + A` | Gallery | Select all photos in current view |
| `Ctrl + H` | Gallery | Toggle visibility of hidden items |
| `Delete` / `Backspace` | Selection | Move selected photos to Recycle Bin |

---

## 3. High-Quality Algorithmic SVG Vector Converter Studio

The **SVG Vector Converter Studio** (`Kv` & `Xv`) transforms raster photography and graphics into scalable, resolution-independent SVG XML graphics using deterministic computational geometry.

### 🔬 Pure Algorithmic Determinism (No Cloud AI)
- **Zero Hallucinations**: Unlike generative AI models that fabricate non-existent imagery, Galaxsee Pro extracts real mathematical boundaries directly from pixel luminance and chrominance.
- **100% Vector Geometry**: Generates standard W3C compliant `<svg xmlns="http://www.w3.org/2000/svg">` XML code containing crisp `<path>` and `<g>` vectors.

### 📁 Universal Format Support & Scale Handling
- **Supported Formats**: PNG, JPEG, WebP, AVIF, HEIC/HEIF, BMP, GIF, and standard image formats.
- **Scale-Invariant Multi-Scale Downsampling Grid**:
  - Automatically downsamples massive sensor files (e.g. 48MP, 108M, 8K captures) to an optimal analysis resolution without sacrificing contour sharpness or crashing the device browser canvas.
  - Three user-selectable detail grids:
    * **Standard Analysis Grid (640px)**: Fast, lightweight, compact SVG file size.
    * **High Fidelity Grid (1080px)**: Balanced curve smoothness and detail for web and graphic assets.
    * **Ultra Detail Grid (1440px)**: Maximum polygon contour fidelity for precision print, engraving, and CNC fabrication.

### 🎨 Three Vectorization Modes

```
+-----------------------------------------------------------------------------------+
|                            GALAXSEE VECTOR STUDIO                                 |
+-----------------------------------------------------------------------------------+
|  [ Pure Vector ]          |  [ Monochrome Silhouette ]   |  [ High-Fidelity Hybrid ] |
|  Quantized multi-color    |  Single compound vector      |  Base raster photo        |
|  contours & SVG paths.    |  path (#000000) for cutting  |  with sharp vector        |
|  8, 16, 32, 64 colors.    |  plotters, logos, stamps.    |  contours overlay.        |
+-----------------------------------------------------------------------------------+
```

1. **Mode 1: Pure Vector**:
   - Performs color quantization into 8, 16, 32, or 64 clusters using weighted Euclidean distance in RGB color space.
   - Extracts connected-component bounding runs and generates smooth SVG polygon paths for each color group.
   - Outputs 100% scalable vector artwork with no raster dependencies.
2. **Mode 2: Monochrome Silhouette**:
   - Analyzes pixel luminance against a contrast-optimized threshold.
   - Emits a unified compound `<path fill="#000000">` representing the subject contours.
   - Ideal for laser cutters, vinyl plotters (Cricut/Silhouette), stencil cutting, stamp making, and icon design.
3. **Mode 3: High-Fidelity Hybrid**:
   - Embeds a color-optimized base raster photograph inside `<image xlink:href="...">`.
   - Overlays high-contrast vector contour line-art paths (`<path stroke="#10b981" ...>`) directly on top.
   - Delivers stunning artistic mixed-media styling while preserving photorealistic highlights and skin tones.

### 🚀 How to Use the Vector Converter
1. **From Gallery View**: Right-click or long-press any photo thumbnail and choose **"Convert to SVG Vector"**.
2. **From Viewer Toolbar**: While inspecting a photo, tap the **Export / Convert** icon in the top toolbar and select **"SVG Vector Studio"**.
3. **From Bulk Transcoder**: Select multiple photos, tap **Export**, and select the **"SVG Vector"** format tile.
4. **Tune Parameters**:
   - Select your desired **Vector Mode** (Pure Vector, Silhouette, or Hybrid).
   - Adjust the **Color Palette** (8, 16, 32, or 64 colors).
   - Choose the **Analysis Detail Grid** (Standard 640px, High 1080px, Ultra 1440px).
5. **Convert & Export**:
   - Tap **"Vectorize to SVG"**.
   - Upon completion, tap **"Download All"** or **"Save to Device"**.
   - On Android, the SVG file is automatically written to `/sdcard/Download/Galaxsee/` and registered with the Android Media Scanner so it immediately appears in your files and external design apps.

---

## 4. Pro Studio Feature Suite

### 🔬 Cull Studio (Light Table & Eye Focus)
- Designed for wedding, sports, and portrait photographers sorting through large shoot sessions.
- **One-Tap Flagging**: Rapidly tag photos with Keep (`P`), Reject (`X`), or 1–5 Star ratings.
- **Eye Focus Zoom**: Automatically centers and magnifies human eyes/faces to check critical sharpness before keeping.
- **XMP Sidecar Export**: Export non-destructive rating flags directly to Adobe Lightroom / Capture One compatible `.xmp` sidecar files.

### 🎨 Non-Destructive Editing Studio
- **Exposure & Contrast**: Precise 32-bit floating-point tone mapping.
- **8-Channel HSL Wheels**: Independent control over Hue, Saturation, and Luminance for Red, Orange, Yellow, Green, Aqua, Blue, Purple, and Magenta.
- **Parametric Tone Curve**: Fine-tune shadows, darks, lights, and highlights across global RGB and individual color channels.

### 🔒 Zero-Knowledge Encrypted Private Vault
- Secure sensitive images inside a hardware-isolated AES-256 encrypted vault.
- Protected by PIN authentication or biometric fingerprint / face unlock.
- Vaulted media is encrypted on disk and completely hidden from Android Gallery and third-party file explorers.

---

## 5. Universal In-App Update System

Both **Galaxsee Pro** and **Galaxsee Standard** include an integrated, zero-dependency in-app update engine connecting directly to official releases.

### Checking for Updates:
1. Open Galaxsee and tap the **Settings** icon (gear in the sidebar or top bar).
2. Scroll to the **Application Updates & Version** card.
3. Tap **"Check for Updates"**.
4. The app contacts the official release endpoint. If a newer build is available:
   - The **Update Modal** opens displaying the new release version and title.
   - Comprehensive **Release Notes & Changelog** are displayed.
   - Exact download package size (in MB) is verified.
5. Tap **"Download & Install Update"**:
   - The app streams the `.apk` package to secure cache storage while displaying a real-time download progress bar and percentage.
   - Once verified, the Android `PackageInstaller` is invoked via `GalaxseeFileProvider` to seamlessly install the update without needing to uninstall the app or lose settings.

---

## 6. Developer Blueprint: How to Update Created Apps (Now & Future)

> [!IMPORTANT]
> This section is the complete operational playbook answering: *"for both gallery apps and future apps when a user needs update how can i update their app?"*

### Architecture Overview
An application can be updated through four distinct distribution paths depending on your deployment model:

```
                               +----------------------------------------+
                               |     APPLICATION UPDATE STRATEGIES      |
                               +----------------------------------------+
                                                   |
         +--------------------+--------------------+--------------------+--------------------+
         |                    |                    |                    |                    |
         v                    v                    v                    v                    v
  [ Strategy 1 ]       [ Strategy 2 ]       [ Strategy 3 ]       [ Strategy 4 ]       [ Strategy 5 ]
  GitHub Releases      Over-The-Air (OTA)   Google Play Store    Self-Hosted Server   Desktop Auto-Update
  Direct APK Install   Web Assets Sync      Internal / Track     Custom API / S3      (Electron Updater)
  (Active Built-in)    (Zero Reinstall)     (Automated Store)    (Enterprise/Local)   (Windows .exe)
```

---

### 🛠️ Strategy 1: Active Production Workflow (GitHub Releases Direct APK)

This is the fully implemented system currently running in both **Galaxsee Pro** and **Galaxsee Standard**.

#### Step 1: Bump Application Version
1. Open `android_build/AndroidManifest.xml`:
   ```xml
   <!-- Increment versionCode by 1, and update versionName -->
   <manifest xmlns:android="http://schemas.android.com/apk/res/android"
       package="com.galaxsee.app"
       android:versionCode="2"
       android:versionName="1.1.0">
   ```
2. Open `android_build/src/com/galaxsee/app/MainActivity.java`:
   - Verify the fallback current version matches `"1.1.0"`.
3. In `web_app_dist/assets/index-*.js`, update the version badge string:
   - Change `"v1.0.0"` to `"v1.1.0"`.

#### Step 2: Compile & Sign the Release APK
Run the zero-dependency build script from the repository root:
```bash
# For Galaxsee Pro:
cd /home/davidalujones/.gemini/antigravity/scratch/Galaxsee/android_build
./build_apk.sh

# For Galaxsee Standard:
cd /home/davidalujones/.gemini/antigravity/scratch/Galaxsee_standard/android_build
./build_apk.sh
```
*The script compiles Java sources with `javac`, converts bytecode with `d8`, aligns with `zipalign`, and cryptographically signs with `apksigner`.*

#### Step 3: Publish the GitHub Release
Tag the git commit and publish the APK asset using the GitHub CLI (`gh`) or GitHub web interface:

```bash
# Using GitHub CLI:
cd /home/davidalujones/.gemini/antigravity/scratch/Galaxsee
git tag v1.1.0
git push origin v1.1.0

gh release create v1.1.0 galaxsee_pro.apk \
  --title "Galaxsee Pro v1.1.0 — High-Quality SVG Vector Engine & Performance Boost" \
  --notes "### What's New in v1.1.0:
- Pure Algorithmic SVG Vector Converter Studio (no AI dependencies)
- Pure Vector, Monochrome Silhouette, and High-Fidelity Hybrid modes
- Color quantization controls (8, 16, 32, 64 colors)
- Direct Android Downloads folder saving via MediaScanner bridge
- Universal in-app updater with real-time download progress bar"
```

#### Step 4: User Experience
1. Existing users tap **"Check for Updates"** in Galaxsee Settings.
2. The app queries `https://api.github.com/repos/Alu6hel/Galaxsee-pro/releases/latest`.
3. The app detects `v1.1.0` > `v1.0.0`, displays the release notes and 17MB package size.
4. User taps **"Download & Install Update"**. The APK downloads and prompts installation directly on screen.

---

### ⚡ Strategy 2: Over-The-Air (OTA) Instant Web Bundle Updates (Future Apps)

For apps built on a WebView architecture (like Galaxsee), you can update the user interface, algorithms, and features **instantly without requiring the user to download an APK or reinstall anything**.

#### Architecture Blueprint:
1. **Dynamic Asset Loading**:
   Instead of loading `file:///android_asset/assets/index.html`, the app checks for updated web bundles stored in `context.getFilesDir() / "www"`:
   ```java
   File localWebDir = new File(getFilesDir(), "www");
   if (new File(localWebDir, "index.html").exists()) {
       webView.loadUrl("file://" + localWebDir.getAbsolutePath() + "/index.html");
   } else {
       webView.loadUrl("file:///android_asset/assets/index.html");
   }
   ```
2. **OTA Update Checker**:
   On app startup, a lightweight background thread queries a manifest file (`https://yourserver.com/ota-manifest.json`):
   ```json
   {
     "bundleVersion": "2026.09.20",
     "bundleUrl": "https://yourserver.com/bundles/bundle-20260920.zip",
     "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
   }
   ```
3. **Hot Unpack**:
   If `bundleVersion` is newer than the stored local version:
   - Download `bundle.zip`.
   - Unzip into `context.getFilesDir() / "www_new"`.
   - Rename `www_new` to `www`.
   - On the next app launch (or with a gentle "Restart to Apply Update" toast), the new version loads immediately!

---

### 🏪 Strategy 3: Google Play Store & Android App Bundles (AAB)

When distributing through the Google Play Store:

1. **Build an Android App Bundle (.aab)**:
   ```bash
   # Build proto resources with aapt2
   aapt2 compile --dir res -o compiled_res.zip
   aapt2 link --proto-format -o base.apk -I android.jar --manifest AndroidManifest.xml compiled_res.zip
   # Pack into .aab with bundletool
   bundletool build-bundle --modules=base.zip --output=galaxsee_pro.aab
   ```
2. **Sign with Release Keystore**:
   ```bash
   jarsigner -keystore my-release-key.jks -storepass YOUR_PASSWORD galaxsee_pro.aab my-key-alias
   ```
3. **Upload to Google Play Console**:
   - Push to **Internal Testing**, **Closed Testing**, or **Production** tracks.
   - Users receive background updates automatically via Google Play Services.
4. **Google Play In-App Updates API**:
   - Integrate `com.google.android.play:app-update` for flexible or immediate in-app update modals managed by Google Play.

---

### 🌐 Strategy 4: Self-Hosted Update Server (Custom REST API)

If you prefer not to rely on GitHub Releases, you can host your own microservice on Cloudflare Workers, AWS S3, or VPS:

#### 1. Manifest Endpoint (`https://api.yourdomain.com/v1/update`):
```json
{
  "appId": "com.galaxsee.app",
  "versionCode": 2,
  "versionName": "1.1.0",
  "minSupportedVersion": "1.0.0",
  "mandatory": false,
  "downloadUrl": "https://cdn.yourdomain.com/apks/galaxsee_pro_v1.1.0.apk",
  "size": 5615232,
  "sha256": "4b97a4...",
  "changelog": [
    "Algorithmic SVG Vector Converter Studio",
    "Enhanced 120Hz gesture physics",
    "Security patches"
  ]
}
```

#### 2. Update Checker Implementation:
Modify `MainActivity.java` `apiUrl` to point to `https://api.yourdomain.com/v1/update`. The rest of the download, notification, and `GalaxseeFileProvider` installation logic remains completely unchanged!

---

### 💻 Strategy 5: Desktop Auto-Update (Windows / macOS / Linux)

For the Windows desktop package (`Galaxsee Pro Photo Gallery Setup 1.0.0.exe`):
- **Electron-Updater**: Uses Squirrel.Windows or NSIS differential updates.
- When you publish a GitHub release with `latest.yml` and `Galaxsee Pro Setup 1.1.0.exe`, the desktop app automatically detects the update, downloads the diff block in the background, and prompts: *"Update Ready: Restart to apply."*

---

## 7. Operational Troubleshooting & Developer Reference

### Common Scenarios & Fixes:

| Issue | Root Cause | Solution |
|---|---|---|
| Update check returns `HTTP 404` | GitHub repository has no published release tag yet. | Run `gh release create v1.0.0 ...` to publish the first official release. |
| Installation blocked on Android | Android requires permission to install apps from within the gallery. | Ensure `android.permission.REQUEST_INSTALL_PACKAGES` is in `AndroidManifest.xml`. If prompted, toggle "Allow from this source" in Android Settings. |
| `FileUriExposedException` | Using `file://` URI directly in Android 7.0+. | Use `GalaxseeFileProvider.getUriForFile()` with `FLAG_GRANT_READ_URI_PERMISSION` (already implemented in `MainActivity.java`). |
| SVG conversion fails on massive 100MP photos | Out-of-memory on mobile WebView canvas. | The built-in multi-scale grid automatically downsamples to 640px/1080px/1440px. Ensure your device has at least 200MB free RAM. |

---

*Authored by the Alumungandr Engineering Team for Galaxsee Pro.*
