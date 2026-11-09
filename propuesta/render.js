const { chromium } = require('playwright');
// uso: node render.js <html absoluto> <png> [ancho] [alto]
(async()=>{const w=+process.argv[4]||1080,h=+process.argv[5]||1350;const b=await chromium.launch();const p=await b.newPage({viewport:{width:w,height:h}});
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(500);await p.screenshot({path:process.argv[3]});await b.close();})();
