#!/usr/bin/env python3
import sys
import os
import subprocess

def patch_bundle(file_path):
    print(f"\n=======================================================")
    print(f"PATCHING: {file_path}")
    print(f"=======================================================")
    
    if not os.path.exists(file_path):
        print(f"Warning: File {file_path} does not exist, skipping.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    orig_len = len(code)

    # 1. Header Brand Logo Unification in U1
    # Replace ALU company logo with Galaxsee cosmic logo
    target_logo_def = 'I=D?"./light alu logo.svg":"./dark alu company logo.svg"'
    repl_logo_def = 'I="./icon-512.svg"'
    if target_logo_def in code:
        code = code.replace(target_logo_def, repl_logo_def, 1)
        print("[1a] Patched header brand logo definition to ./icon-512.svg")
    else:
        print("[1a] Note: target_logo_def not found or already patched")

    # 1b. Header Brand Logo Image Tag & Container Fill
    target_logo_container = 'justify-center p-0.5 overflow-hidden \,children:a.jsx("img",{src:I,alt:"Galaxsee Logo",onError:E=>{E.currentTarget.src="./app_icon_512.png"},className:"w-full h-full object-contain"})'
    repl_logo_container = 'justify-center overflow-hidden bg-transparent\,children:a.jsx("img",{src:I,alt:"Galaxsee Logo",onError:E=>{E.currentTarget.src="./app_icon_512.png"},className:"w-full h-full object-cover rounded-[6px]"})'
    if target_logo_container in code:
        code = code.replace(target_logo_container, repl_logo_container, 1)
        print("[1b] Patched header brand logo container and image tag to fill space edge-to-edge")
    else:
        target_logo_img = 'a.jsx("img",{src:I,alt:"Alu Logo",onError:E=>{E.currentTarget.src=D?"./light alu logo.png":"./dark alu company logo.png"},className:"w-full h-full object-contain"})'
        repl_logo_img = 'a.jsx("img",{src:I,alt:"Galaxsee Logo",onError:E=>{E.currentTarget.src="./app_icon_512.png"},className:"w-full h-full object-cover rounded-[6px]"})'
        if target_logo_img in code:
            code = code.replace(target_logo_img, repl_logo_img, 1)
            print("[1b] Patched header brand logo image tag to fill space edge-to-edge")
        else:
            print("[1b] Note: target_logo_img not found or already patched")

    # 2. Photo Viewer (cv) Active Photo Tracking & Back Button Accessibility
    target_cv_effect = 'M.useEffect(()=>{I(1),P({x:0,y:0}),H(0)},[d.id]);'
    repl_cv_effect = 'M.useEffect(()=>{I(1),P({x:0,y:0}),H(0);if(typeof window<"u"){window.__galaxsee_last_viewed_photo_id=d.id;}},[d.id]);'
    if target_cv_effect in code:
        code = code.replace(target_cv_effect, repl_cv_effect, 1)
        print("[2a] Patched cv active photo tracking on d.id change")
    else:
        print("[2a] Note: target_cv_effect not found or already patched")

    target_cv_back = 'a.jsxs("button",{onClick:()=>{we.playKeypad(),h()},className:`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-colors'
    repl_cv_back = 'a.jsxs("button",{title:"Back to Grid","aria-label":"Back to Grid",onClick:()=>{we.playKeypad(),h()},className:`galaxsee-back-btn flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-colors'
    if target_cv_back in code:
        code = code.replace(target_cv_back, repl_cv_back, 1)
        print("[2b] Patched cv Back button with accessibility title, aria-label, and galaxsee-back-btn class")
    else:
        print("[2b] Note: target_cv_back not found or already patched")

    # 3. Photo Grid (ov) Scroll Container onScroll Tracker
    target_ov_scroller = 'return a.jsxs("div",{ref:R,onMouseDown:J,'
    repl_ov_scroller = 'return a.jsxs("div",{ref:R,onScroll:$e=>{if(typeof window<"u"&&!window.__galaxsee_is_restoring_scroll){if($e.currentTarget.scrollTop>0)window.__galaxsee_last_grid_scroll=$e.currentTarget.scrollTop;}},onMouseDown:J,'
    if target_ov_scroller in code:
        code = code.replace(target_ov_scroller, repl_ov_scroller, 1)
        print("[3] Added onScroll position tracker to ov ref:R container")
    else:
        print("[3] Note: target_ov_scroller not found or already patched")

    # 4. Photo Card Click & Double Click in ov
    target_ov_click = 'onClick:$e=>{v||$e.shiftKey||$e.metaKey||$e.ctrlKey?($e.stopPropagation(),we.playKeypad(),_(Re.id,$e.shiftKey)):m(Re)},onDoubleClick:$e=>{$e.stopPropagation();m(Re)}'
    repl_ov_click = 'onClick:$e=>{if(v||$e.shiftKey||$e.metaKey||$e.ctrlKey){$e.stopPropagation();we.playKeypad();_(Re.id,$e.shiftKey);}else{if(typeof window<"u"){window.__galaxsee_last_viewed_photo_id=Re.id;if(R.current&&R.current.scrollTop>0)window.__galaxsee_last_grid_scroll=R.current.scrollTop;window.__galaxsee_is_restoring_scroll=true;}m(Re);}},onDoubleClick:$e=>{$e.stopPropagation();if(typeof window<"u"){window.__galaxsee_last_viewed_photo_id=Re.id;if(R.current&&R.current.scrollTop>0)window.__galaxsee_last_grid_scroll=R.current.scrollTop;window.__galaxsee_is_restoring_scroll=true;}m(Re);}'
    if target_ov_click in code:
        code = code.replace(target_ov_click, repl_ov_click, 1)
        print("[4] Attached last viewed photo and scroll capture to ov card onClick & onDoubleClick")
    else:
        print("[4] Note: target_ov_click not found or already patched")

    # 5. Dynamic Batch Expansion & Multi-Pass Scroll Restoration in ov
    target_ov_batch = 'nt=M.useRef(new Map),[renderLimit,setRenderLimit]=M.useState(60);M.useEffect(()=>{setRenderLimit(60);},[d,ue,B]);'
    repl_ov_batch = (
        'nt=M.useRef(new Map),'
        '[renderLimit,setRenderLimit]=M.useState(()=>{'
        'if(typeof window<"u"&&window.__galaxsee_last_viewed_photo_id&&Ue){'
        'const pIdx=Ue.findIndex(p=>p.id===window.__galaxsee_last_viewed_photo_id);'
        'if(pIdx>=60)return Math.min(100000,pIdx+40);'
        '}return 60;});'
        'M.useEffect(()=>{'
        'if(typeof window<"u"&&window.__galaxsee_is_restoring_scroll)return;'
        'setRenderLimit(60);'
        '},[d,ue,B]);'
        'M.useLayoutEffect(()=>{'
        'const targetScroll=typeof window<"u"?window.__galaxsee_last_grid_scroll:null;'
        'const targetId=typeof window<"u"?window.__galaxsee_last_viewed_photo_id:null;'
        'if(!targetScroll&&!targetId)return;'
        'window.__galaxsee_is_restoring_scroll=true;'
        'if(targetId&&Ue){'
        'const pIdx=Ue.findIndex(p=>p.id===targetId);'
        'if(pIdx>=0){setRenderLimit(prev=>Math.max(prev,pIdx+40));}'
        '}'
        'const doRestore=()=>{'
        'const scroller=R.current;'
        'if(!scroller)return false;'
        'let handled=false;'
        'if(targetId&&nt.current&&nt.current.has(targetId)){'
        'const el=nt.current.get(targetId);'
        'if(el){'
        'const sr=scroller.getBoundingClientRect();'
        'const er=el.getBoundingClientRect();'
        'if(er.top<sr.top||er.bottom>sr.bottom){'
        'const diff=(er.top-sr.top)-(sr.height/2-er.height/2);'
        'scroller.scrollTop+=diff;'
        '}'
        'handled=true;'
        '}'
        '}'
        'if(!handled&&typeof targetScroll==="number"&&targetScroll>0){'
        'scroller.scrollTop=targetScroll;'
        'handled=true;'
        '}'
        'return handled;'
        '};'
        'doRestore();'
        'const af=requestAnimationFrame(()=>{'
        'doRestore();'
        'const t1=setTimeout(()=>{'
        'doRestore();'
        'window.__galaxsee_is_restoring_scroll=false;'
        '},120);'
        'return()=>clearTimeout(t1);'
        '});'
        'return()=>{'
        'cancelAnimationFrame(af);'
        'window.__galaxsee_is_restoring_scroll=false;'
        '};'
        '},[]);'
    )
    if target_ov_batch in code:
        code = code.replace(target_ov_batch, repl_ov_batch, 1)
        print("[5] Replaced ov batching and implemented dynamic expansion & multi-pass useLayoutEffect scroll restoration")
    else:
        print("[5] Note: target_ov_batch not found or already patched")

    # 6. Storage Folders View (Qv) Persistence & Photo Click Memory
    target_qv_state = 'const x=g==="light"||g==="light_galaxsee"||g==="blue_sky",[T,N]=M.useState(null),'
    repl_qv_state = (
        'const x=g==="light"||g==="light_galaxsee"||g==="blue_sky",'
        '[T,_N_raw]=M.useState(()=>{try{return window.__galaxsee_active_folder||null}catch{return null}}),'
        'N=M.useCallback(val=>{_N_raw(val);if(typeof window<"u")window.__galaxsee_active_folder=val;},[]),'
    )
    if target_qv_state in code:
        code = code.replace(target_qv_state, repl_qv_state, 1)
        print("[6a] Wrapped Qv folder state [T,N] with window.__galaxsee_active_folder persistence")
    else:
        print("[6a] Note: target_qv_state not found or already patched")

    target_qv_photo_click = 'onClick: () => u(V),'
    repl_qv_photo_click = 'onClick: () => { if(typeof window<"u"){window.__galaxsee_last_viewed_photo_id=V.id;window.__galaxsee_active_folder=T;} u(V); },'
    if target_qv_photo_click in code:
        code = code.replace(target_qv_photo_click, repl_qv_photo_click, 1)
        print("[6b] Linked Qv photo card click to active photo ID & folder memory")
    else:
        print("[6b] Note: target_qv_photo_click not found or already patched")

    # 7. Precise Search Engine Upgrade (Fast Keyword, Tag, Number & Date matching)
    target_my = 'function my(d,u,h=.5){var _,x,T,N,A;if(!d||!d.trim()||u.length===0)return[];const m=d.trim().toLowerCase(),g=m.split(/[\\s,._-]+/).filter(Boolean),w=uy(m),y=[],k=g.filter(D=>Um[D]);for(let D=0;D<u.length;D++){const I=u[D],U=Xu(I);let P=fy(w,U),ae;const H=(I.title||"").toLowerCase(),E=(_=I.tags)==null?void 0:_.some(K=>m.includes(K.toLowerCase())),Z=((T=(x=I.location)==null?void 0:x.city)==null?void 0:T.toLowerCase().includes(m))||((A=(N=I.location)==null?void 0:N.country)==null?void 0:A.toLowerCase().includes(m));if((H.includes(m)||E||Z)&&(P=Math.min(1,P+.25),ae="Keyword & Tag Match"),k.length>0&&I.colorPalette&&I.colorPalette.length>0)for(const K of k){const X=Um[K];X&&I.colorPalette.some(me=>{const De=ry(me);return De?cy(De,X)<90:!1})&&(P=Math.min(1,P+.15),ae=ae?`${ae} + Dominant ${K}`:`Dominant Color (${K})`)}P>=h&&y.push({photo:I,score:P,matchReason:ae||`Semantic Match (${Math.round(P*100)}%)`})}return y.sort((D,I)=>I.score-D.score),y}'
    repl_my = '''function my(d,u,h=.5){if(!d||!d.trim()||!u||u.length===0)return[];const raw=d.trim().toLowerCase(),terms=raw.split(/[\\s,._-]+/).filter(Boolean);if(terms.length===0)return[];const out=[];for(let i=0;i<u.length;i++){const it=u[i];if(!it)continue;const title=(it.title||"").toLowerCase(),desc=(it.description||"").toLowerCase(),path=(it.filePath||it.localPath||"").toLowerCase(),folder=(it.folder||"").toLowerCase(),cat=(it.category||"").toLowerCase(),ft=(it.fileType||"").toLowerCase();let yr="",mo="",mosh="",dy="";if(it.date){try{const dt=new Date(it.date);if(!isNaN(dt.getTime())){yr=String(dt.getFullYear()),mo=dt.toLocaleString("en-US",{month:"long"}).toLowerCase(),mosh=dt.toLocaleString("en-US",{month:"short"}).toLowerCase(),dy=String(dt.getDate())}}catch{}}const city=(it.location&&it.location.city?it.location.city:"").toLowerCase(),country=(it.location&&it.location.country?it.location.country:"").toLowerCase(),locName=(it.location&&it.location.name?it.location.name:"").toLowerCase(),make=(it.exif&&it.exif.cameraMake?it.exif.cameraMake:"").toLowerCase(),model=(it.exif&&it.exif.cameraModel?it.exif.cameraModel:"").toLowerCase(),iso=it.exif&&it.exif.iso!=null?String(it.exif.iso):"",tags=Array.isArray(it.tags)?it.tags.map(t=>String(t).toLowerCase()):[],ppl=Array.isArray(it.people)?it.people.map(p=>String(p).toLowerCase()):[];let colorMatch=!1,colorName="";if(it.colorPalette&&it.colorPalette.length>0&&typeof Um<"u")for(const t of terms){const rgb=Um[t];if(rgb&&typeof ry==="function"&&typeof cy==="function"&&it.colorPalette.some(c=>{const cRgb=ry(c);return cRgb?cy(cRgb,rgb)<90:!1})){colorMatch=!0,colorName=t;break}}let full=!1,score=0,reason="";if(title===raw)score+=2000,reason="Exact Title",full=!0;else if(title.startsWith(raw))score+=1200,reason="Title Starts With",full=!0;else if(title.includes(raw))score+=800,reason="Title Match",full=!0;else if(desc.includes(raw)||path.includes(raw))score+=600,reason="Filename Match",full=!0;else if(tags.some(t=>t===raw||t.includes(raw)))score+=500,reason="Tag Match",full=!0;else if(ppl.some(p=>p===raw||p.includes(raw)))score+=500,reason="Person Match",full=!0;let allTerms=!0;for(const t of terms){let tScore=0;if(title===t)tScore+=1000;else if(title.startsWith(t))tScore+=600;else if(title.includes(t))tScore+=400;else if(desc.includes(t)||path.includes(t))tScore+=300;else if(tags.some(tg=>tg.includes(t)))tScore+=250;else if(ppl.some(p=>p.includes(t)))tScore+=250;else if(folder.includes(t)||cat.includes(t))tScore+=180;else if(ft.includes(t)||t.length>=3&&("."+t).includes(ft.replace("image/",".")))tScore+=150;else if(yr&&(t===yr||t.length>=4&&yr.includes(t))||mo&&mo.startsWith(t)||mosh&&mosh===t||dy&&dy===t)tScore+=140;else if(city.includes(t)||country.includes(t)||locName.includes(t))tScore+=120;else if(make.includes(t)||model.includes(t)||iso&&iso===t)tScore+=100;else if(colorMatch&&colorName===t)tScore+=200;if(tScore>0)score+=tScore;else{allTerms=!1;break}}if(full||allTerms&&score>0)out.push({photo:it,score:Math.min(1,.5+score/3000),rawScore:score,matchReason:reason||(colorMatch?`Dominant Color (${colorName})`:"Keyword Match")})}return out.sort((a,b)=>b.rawScore-a.rawScore),out}'''
    if target_my in code:
        code = code.replace(target_my, repl_my, 1)
        print("[7] Upgraded search engine with precise keyword, number, tag, and date matching")
    else:
        print("[7] Note: target_my not found or already patched")

    # Write patched file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)

    new_len = len(code)
    print(f"Finished patching: {orig_len} -> {new_len} ({new_len - orig_len:+d} bytes)")

    # Verify node syntax
    res = subprocess.run(["node", "-c", file_path], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FATAL: Syntax validation failed for {file_path}:")
        print(res.stderr)
        sys.exit(1)
    else:
        print(f"VERIFICATION SUCCESS: 0 syntax errors in {file_path}!")

if __name__ == "__main__":
    targets = [
        "/home/davidalujones/.gemini/antigravity/scratch/Galaxsee/web_app_dist/assets/index-DpfNch1h.js",
        "/home/davidalujones/.gemini/antigravity/scratch/Galaxsee/android_build/assets/assets/index-DpfNch1h.js",
        "/home/davidalujones/.gemini/antigravity/scratch/Galaxsee_standard/web_app_dist/assets/index-DpfNch1h.js",
        "/home/davidalujones/.gemini/antigravity/scratch/Galaxsee_standard/android_build/assets/assets/index-DpfNch1h.js",
    ]
    if len(sys.argv) > 1:
        targets = sys.argv[1:]

    for t in targets:
        patch_bundle(t)
    print("\nALL TARGETS PATCHED AND VERIFIED CLEANLY!")
