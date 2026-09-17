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
    }, 4000);

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

const expr = process.argv.slice(2).join(' ') || '1+1';
evalInWebview(expr)
  .then(val => {
    console.log(typeof val === 'object' ? JSON.stringify(val, null, 2) : val);
    process.exit(0);
  })
  .catch(err => {
    console.error(err.message || err);
    process.exit(1);
  });

