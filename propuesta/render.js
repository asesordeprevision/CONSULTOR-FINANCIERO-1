const { chromium } = require('playwright');
// uso: node render.js <html absoluto> <png> [ancho] [alto]
// La fecha del encabezado (".top .d") se actualiza sola al día de hoy en Monterrey.
(async()=>{const w=+process.argv[4]||1080,h=+process.argv[5]||1350;const b=await chromium.launch();const p=await b.newPage({viewport:{width:w,height:h}});
await p.goto('file://'+process.argv[2]);
const hoy=new Date().toLocaleDateString('es-MX',{timeZone:'America/Monterrey',day:'numeric',month:'long',year:'numeric'});
await p.evaluate(hoy=>{document.querySelectorAll('.top .d').forEach(el=>{el.innerHTML=el.innerHTML.replace(/\d{1,2} de [a-záéíóú]+ de \d{4}/i,hoy);});},hoy);
await p.waitForTimeout(500);await p.screenshot({path:process.argv[3]});await b.close();})();
