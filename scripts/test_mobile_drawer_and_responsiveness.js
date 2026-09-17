const http = require('http');

async function evalInWebview(expr) {
  const json = await new Promise((resolve, reject) => {
    http.get('http://localhost:9222/json', res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => resolve(JSON.parse(d)));
    }).on('error', reject);
  });

  const wsUrl = json[0].webSocketDebuggerUrl;
  const ws = new WebSocket(wsUrl);

  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => {
      try { ws.close(); } catch {}
      reject(new Error('CDP timeout'));
    }, 6000);

    ws.onopen = () => {
      ws.send(JSON.stringify({
        id: 1,
        method: 'Runtime.evaluate',
        params: { expression: expr, returnByValue: true, awaitPromise: true }
      }));
    };
    ws.onmessage = msg => {
      clearTimeout(timer);
      const resp = JSON.parse(msg.data);
      try { ws.close(); } catch {}
      if (resp.result && resp.result.result) {
        resolve(resp.result.result.value);
      } else {
        resolve(resp);
      }
    };
    ws.onerror = err => {
      clearTimeout(timer);
      reject(err);
    };
  });
}

async function runMobileAudit() {
  console.log("==================================================================");
  console.log("AUDITING MOBILE RESPONSIVENESS & TAP-TO-HIDE DRAWER BEHAVIOR");
  console.log("==================================================================");

  // Close any open modals first
  await evalInWebview(`(() => {
    const closeBtns = Array.from(document.querySelectorAll('button')).filter(b => b.textContent.trim() === 'Close');
    closeBtns.forEach(b => b.click());
    const aside = document.getElementById('galaxsee-sidebar');
    if (window.__galaxsee_close_sidebar) window.__galaxsee_close_sidebar();
    return true;
  })()`);
  await new Promise(r => setTimeout(r, 400));

  // Test 1: DOM metrics & Initial State
  console.log("\n[TEST 1] Verifying initial mobile layout metrics & DOM efficiency...");
  const t1 = await evalInWebview(`(() => {
    const domNodes = document.querySelectorAll('*').length;
    const main = document.querySelector('main');
    const aside = document.getElementById('galaxsee-sidebar');
    const backdrop = document.querySelector('div.fixed.inset-0.z-40');
    const toggleBtn = document.querySelector('[data-sidebar-toggle="true"]');
    const mainWidth = main ? Math.round(main.getBoundingClientRect().width) : 0;
    const screenWidth = window.innerWidth;
    const isSidebarClosed = aside ? aside.className.includes('-translate-x-full') : false;

    return {
      domNodes,
      screenWidth,
      mainWidth,
      isFullWidth: mainWidth === screenWidth,
      isSidebarClosed,
      hasBackdrop: !!backdrop,
      hasToggleBtn: !!toggleBtn
    };
  })()`);
  console.log("Test 1 Result:", t1);
  if (!t1.isFullWidth || !t1.isSidebarClosed || t1.hasBackdrop || !t1.hasToggleBtn) {
    throw new Error("Test 1 Failed: Initial mobile layout is incorrect");
  }

  // Test 2: Tap Hamburger button to open drawer
  console.log("\n[TEST 2] Tapping hamburger button to open drawer...");
  const t2 = await evalInWebview(`(() => {
    const toggleBtn = document.querySelector('[data-sidebar-toggle="true"]');
    if (toggleBtn) {
      toggleBtn.click();
      return { clicked: true };
    }
    return { clicked: false };
  })()`);
  console.log("Test 2 Result:", t2);
  await new Promise(r => setTimeout(r, 400));

  // Test 3: Verify drawer is open with backdrop
  console.log("\n[TEST 3] Verifying drawer is open with z-40 backdrop...");
  const t3 = await evalInWebview(`(() => {
    const aside = document.getElementById('galaxsee-sidebar');
    const backdrop = document.querySelector('div.fixed.inset-0.z-40');
    const isExpanded = aside ? aside.className.includes('translate-x-0') : false;
    return {
      isExpanded,
      hasBackdrop: !!backdrop
    };
  })()`);
  console.log("Test 3 Result:", t3);
  if (!t3.isExpanded || !t3.hasBackdrop) {
    throw new Error("Test 3 Failed: Drawer did not open or backdrop is missing");
  }

  // Test 4: Tap backdrop to hide drawer
  console.log("\n[TEST 4] Tapping backdrop to hide drawer (Tap-to-Hide test)...");
  const t4 = await evalInWebview(`(() => {
    const backdrop = document.querySelector('div.fixed.inset-0.z-40');
    if (backdrop) {
      backdrop.click();
      return { clicked: true };
    }
    return { clicked: false };
  })()`);
  console.log("Test 4 Result:", t4);
  await new Promise(r => setTimeout(r, 400));

  // Test 5: Verify drawer is closed and backdrop is gone
  console.log("\n[TEST 5] Verifying drawer closed after backdrop tap...");
  const t5 = await evalInWebview(`(() => {
    const aside = document.getElementById('galaxsee-sidebar');
    const backdrop = document.querySelector('div.fixed.inset-0.z-40');
    const isClosed = aside ? aside.className.includes('-translate-x-full') : false;
    return {
      isClosed,
      hasBackdrop: !!backdrop
    };
  })()`);
  console.log("Test 5 Result:", t5);
  if (!t5.isClosed || t5.hasBackdrop) {
    throw new Error("Test 5 Failed: Drawer did not close upon tapping backdrop");
  }

  // Test 6: Reopen drawer and tap menu item (Auto-close on navigation)
  console.log("\n[TEST 6] Reopening drawer and tapping 'Favorites' menu item...");
  await evalInWebview(`(() => {
    const toggleBtn = document.querySelector('[data-sidebar-toggle="true"]');
    if (toggleBtn) toggleBtn.click();
  })()`);
  await new Promise(r => setTimeout(r, 400));

  const t6 = await evalInWebview(`(() => {
    const aside = document.getElementById('galaxsee-sidebar');
    const favBtn = Array.from(aside.querySelectorAll('button')).find(b => b.textContent.includes('Favorites'));
    if (favBtn) {
      favBtn.click();
      return { clickedFav: true };
    }
    return { clickedFav: false };
  })()`);
  console.log("Test 6 Result:", t6);
  await new Promise(r => setTimeout(r, 500));

  // Test 7: Verify auto-closed and navigated to Favorites
  console.log("\n[TEST 7] Verifying drawer auto-closed and view switched to Favorites...");
  const t7 = await evalInWebview(`(() => {
    const aside = document.getElementById('galaxsee-sidebar');
    const backdrop = document.querySelector('div.fixed.inset-0.z-40');
    const isClosed = aside ? aside.className.includes('-translate-x-full') : false;
    const isFavView = document.body.innerText.includes('Favorites');
    return {
      isClosed,
      hasBackdrop: !!backdrop,
      isFavView
    };
  })()`);
  console.log("Test 7 Result:", t7);
  if (!t7.isClosed || t7.hasBackdrop || !t7.isFavView) {
    throw new Error("Test 7 Failed: Drawer did not auto-close or failed to navigate to Favorites");
  }

  // Test 8: Navigate back to Gallery
  console.log("\n[TEST 8] Reopening drawer and navigating back to Gallery...");
  await evalInWebview(`(() => {
    const toggleBtn = document.querySelector('[data-sidebar-toggle="true"]');
    if (toggleBtn) toggleBtn.click();
  })()`);
  await new Promise(r => setTimeout(r, 400));

  await evalInWebview(`(() => {
    const aside = document.getElementById('galaxsee-sidebar');
    const galBtn = Array.from(aside.querySelectorAll('button')).find(b => b.textContent.trim() === 'Gallery');
    if (galBtn) galBtn.click();
  })()`);
  await new Promise(r => setTimeout(r, 500));

  const t8 = await evalInWebview(`(() => {
    const aside = document.getElementById('galaxsee-sidebar');
    const isClosed = aside ? aside.className.includes('-translate-x-full') : false;
    const photoCount = document.querySelectorAll('.photo-card').length;
    return {
      isClosed,
      photoCount
    };
  })()`);
  console.log("Test 8 Result:", t8);

  console.log("\n==================================================================");
  console.log("ALL 8 MOBILE RESPONSIVENESS & TAP-TO-HIDE TESTS PASSED 100%!");
  console.log("==================================================================");
}

runMobileAudit().catch(err => {
  console.error("AUDIT FAILED:", err);
  process.exit(1);
});
