# Cotización formal imprimible (carta vertical) Capillas Marianas, 2 servicios por categoría. python3 gen.py
import os,datetime
D=os.path.dirname(os.path.abspath(__file__))
def m(x,c=False): return f"${x:,.2f}" if c else f"${x:,.0f}"
MESES=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
hoy=datetime.datetime.now(datetime.UTC).replace(tzinfo=None)-datetime.timedelta(hours=6); fecha=f"{hoy.day} de {MESES[hoy.month-1]} de {hoy.year}"
CAT={
"premier":dict(nom="PREMIER PRO",clave="826890",lista=164600.02,ml=4575.88,cont=98760.00,t36=(121145.62,3367.85),t48=(127729.62,2656.78),
 fotos=["../marianas_fachada.jpg","../ataudes/celesti.jpg","../ataudes/pacis.jpg"],pies=["Capillas Marianas","Ataúd Celesti","Urna Pacis"],
 por="La categoría más completa de Gayosso y la única <b>Multiplaza</b>: su servicio es válido en las 24 agencias Gayosso de 13 estados.",
 inc=["<b>Sala de velación Premier</b> 24 h para 60 personas (salas Premier y Magna, 5º piso; Lourdes y Fátima, 4º piso)","Ataúd de lujo de metal o madera cat. Premier (Celesti / Eternus)","Si elige cremación: ataúd de lujo de presentación y <b>urna de lujo</b> de madera (Pacis)","<b>Multiplaza:</b> válido en cualquier agencia Gayosso del país","1 copia del acta de defunción"],
 up=("¿Quiere proteger a una persona más?","Con la <b>Promoción 2 + 1</b> el tercer servicio Premier Pro le sale de obsequio: <b>48 × $3,321.14</b> con tarjeta de crédito (solo <b>$664.36 más al mes</b>) o <b>$131,686.58 de contado</b>."),conf=True),
"universal":dict(nom="UNIVERSAL PRO",clave="826885",lista=124600.02,ml=3463.88,cont=74760.01,t36=(91705.61,2549.42),t48=(96689.62,2011.14),
 fotos=["../marianas_fachada.jpg","../ataudes/legatum.jpg","../ataudes/aural.jpg"],pies=["Capillas Marianas","Ataúd Legatum","Urna Aural"],
 por="El punto de equilibrio de Gayosso: ataúd de metal o madera y un servicio completo, con una inversión muy por debajo de Premier.",
 inc=["Sala de velación Estándar 24 h para 40 personas","Ataúd de metal o madera cat. Universal (Legatum / Stella)","Si elige cremación: ataúd de presentación y <b>urna de madera</b> (Aural)","Servicio en la agencia Gayosso de su plaza"],
 up=("¿Quiere proteger a una persona más?","Con la <b>Promoción 2 + 1</b> el tercer servicio Universal Pro le sale de obsequio: <b>48 × $2,514.06</b> con tarjeta de crédito o <b>$99,685 de contado</b>."),conf=False),
"esencial":dict(nom="ESENCIAL PRO",clave="826882",lista=96600.00,ml=2685.48,cont=61824.00,t36=(71097.60,1976.51),t48=(74961.60,1559.20),
 fotos=["../marianas_fachada.jpg","../ataudes/iter_pax.jpg","../ataudes/oblatio.jpg"],pies=["Capillas Marianas","Ataúd Iter Pax","Urna Oblatio"],
 por="Un servicio funerario completo y digno, con el respaldo de Gayosso, a la inversión más accesible.",
 inc=["Sala de velación Estándar 24 h para 20 personas","Ataúd metálico cat. Esencial (Iter Pax)","Si elige cremación: ataúd de presentación y <b>urna de madera</b> (Oblatio)","Servicio en la agencia Gayosso de su plaza"],
 up=("¿Busca también el lugar de descanso?","En la nueva <b>Marianas Nogalar</b>: 2 Esencial Pro + <b>nicho para 2 urnas de regalo</b> desde <b>48 × $1,816.24</b> con tarjeta de crédito o <b>$72,016 de contado</b>."),conf=True)}
COM=["Asesoría en trámites","Traslados en el área conurbada (a la funeraria y al destino final)","Embalsamamiento y arreglo estético","Cafetería básica","<b>Ambivalente:</b> al momento se elige inhumación o cremación","100% transferible: usted designa a quién se le da cada servicio"]
CSS="""@page{size:letter;margin:0}*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Helvetica Neue',Arial,sans-serif;color:#1d2b24;background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{width:8.5in;height:11in;padding:.38in .45in .3in;display:flex;flex-direction:column}
.hd{display:flex;align-items:center;gap:14px;border-bottom:3px solid #b8954a;padding-bottom:8px}
.hd img{height:50px}.hd .t{flex:1}.hd h1{font-size:13px;letter-spacing:2.5px;color:#7a5f22;font-weight:700}
.hd h2{font-size:21px;color:#0f4a36;margin-top:1px}.hd .r{text-align:right;font-size:10.5px;color:#5b6b63;line-height:1.5}
.to{display:flex;justify-content:space-between;align-items:flex-end;margin:10px 0 6px;font-size:11.5px}
.to .ln{flex:1;border-bottom:1px solid #9aa8a0;margin:0 10px 3px;height:16px}
.intro{font-size:11px;line-height:1.5;color:#33433b;margin-bottom:8px}
.band{background:#0f4a36;color:#fff;border-radius:8px;padding:9px 14px;display:flex;justify-content:space-between;align-items:center}
.band b{font-size:17px;letter-spacing:.5px}.band span{font-size:11px;color:#e8d9b0}
.why{font-size:11px;color:#33433b;margin:7px 0;line-height:1.45;border-left:3px solid #b8954a;padding-left:9px}
.cols{display:grid;grid-template-columns:1.25fr 1fr;gap:12px}
ul{list-style:none;font-size:10.3px;line-height:1.38}li{padding-left:13px;position:relative;margin-bottom:2px}
li:before{content:"✔";position:absolute;left:0;color:#2e7d32;font-size:9.5px}
h3{font-size:11px;color:#0f4a36;text-transform:uppercase;letter-spacing:.5px;margin:4px 0 4px}
.ph{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:6px;margin-top:4px}
.ph div{text-align:center;font-size:8.5px;color:#5b6b63}.ph img{width:100%;height:96px;object-fit:contain;background:#fff!important;border-radius:6px;border:1px solid #e3e8e5;background:#f6f6f2}
.lst{background:#f7f3ea;border:1px solid #d9c89f;border-radius:8px;padding:8px 11px;font-size:11px;margin-bottom:6px}
.lst .a{display:flex;justify-content:space-between}.lst s{color:#8a8a8a}
table{width:100%;border-collapse:collapse;font-size:11px;margin-top:6px}
th{background:#0f4a36;color:#fff;padding:6px;text-align:left;font-size:9.8px;text-transform:uppercase;letter-spacing:.3px}
td{padding:7px 6px;border-bottom:1px solid #e3e8e5}td.r,th.r{text-align:right}
tr.st td{background:#fbf6e8}tr.st td:first-child{border-left:4px solid #b8954a}
.tg{display:inline-block;font-size:8.5px;font-weight:700;color:#fff;background:#b8954a;border-radius:9px;padding:1px 7px;margin-left:5px;vertical-align:1px}
.tg.g{background:#2e7d32}.mo{font-weight:700;color:#0f4a36;font-size:12.5px}.sv{color:#2e7d32;font-weight:700}.sm{font-size:9.3px;color:#6b7a72}
.gift{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-top:8px}
.bx{border:1px solid #d9c89f;border-radius:8px;padding:7px 10px;font-size:10px;line-height:1.42;background:#fdfaf3}
.bx h4{font-size:10.8px;color:#0f4a36;margin-bottom:2px}.bx.up{background:#eef5f0;border-color:#9cc5ab}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:7px;margin-top:8px}
.steps div{font-size:9.6px;line-height:1.38;background:#f3f6f4;border-radius:7px;padding:6px 8px}
.steps b{display:block;color:#0f4a36;font-size:10.3px}
.vig{margin-top:7px;background:#fdecea;color:#9c1c14;border-radius:7px;padding:6px 10px;font-size:11px;font-weight:700;text-align:center}
.nt{flex:1;margin-top:8px;min-height:30px;border:1px dashed #c9d2cd;border-radius:7px;padding:5px 10px;font-size:9.5px;color:#6b7a72;background:repeating-linear-gradient(transparent 0 21px,#e3e8e5 21px 22px)}
.ft{margin-top:8px;border-top:1px solid #e3e8e5;padding-top:6px;display:flex;justify-content:space-between;gap:12px;font-size:8.3px;color:#6b7a72;line-height:1.38}
.sig{text-align:right;font-size:10px;color:#1d2b24;white-space:nowrap}.sig b{font-size:11.5px;color:#0f4a36}"""
def page(k):
  c=CAT[k];L=c['lista'];r=lambda t:(L-t,(L-t)/L*100)
  a36,p36=r(c['t36'][0]);a48,p48=r(c['t48'][0]);ac,pc=r(c['cont'])
  dia=lambda mm:int(mm/30/2)+1
  rows=f"""<tr class="st"><td><b>Tarjeta de crédito · 48 meses</b><span class="tg">MÁS ACCESIBLE</span><div class="sm">Sin enganche · sin intereses</div></td><td class="r mo">{m(c['t48'][1],1)}</td><td class="r">{m(c['t48'][0],1)}</td><td class="r sv">{m(a48)} <span class="sm">({p48:.1f}%)</span></td><td class="r sm">menos de ${dia(c['t48'][1])}<br>diarios c/u</td></tr>
<tr><td><b>Tarjeta de crédito · 36 meses</b><div class="sm">Sin enganche · sin intereses</div></td><td class="r mo">{m(c['t36'][1],1)}</td><td class="r">{m(c['t36'][0],1)}</td><td class="r sv">{m(a36)} <span class="sm">({p36:.1f}%)</span></td><td class="r sm">${c['ml']-c['t36'][1]:,.0f} menos<br>que la de lista</td></tr>
<tr class="st"><td><b>Contado</b><span class="tg g">MAYOR AHORRO</span><div class="sm">Una sola exhibición</div></td><td class="r">—</td><td class="r mo">{m(c['cont'],1)}</td><td class="r sv">{m(ac)} <span class="sm">({pc:.1f}%)</span></td><td class="r sm">{m(c['cont']/2)}<br>por servicio</td></tr>"""
  ph="".join(f"<div><img src=\"{f}\" style=\"{'object-fit:cover' if i==0 else ''}\">{p}</div>" for i,(f,p) in enumerate(zip(c["fotos"],c["pies"])))
  return f"""<div class="pg"><div class="hd"><img src="../logo.jpg"><div class="t"><h1>PROPUESTA DE PREVISIÓN FAMILIAR</h1><h2>Capillas Marianas · Monterrey</h2></div><div class="r">San Pedro Garza García, N.L.<br><b>{fecha}</b></div></div>
<div class="to"><span>Para:</span><span class="ln"></span><span>Tel.:</span><span class="ln" style="flex:.55"></span></div>
<p class="intro">Es un gusto saludarle. Conforme a lo que platicamos, le comparto la propuesta para dejar protegidos a <b>dos integrantes de su familia</b>, con el detalle de lo que incluye, su inversión y las formas de pago disponibles.</p>
<div class="band"><b>2 SERVICIOS · PREVISIÓN GAYOSSO {c['nom']}</b><span>Clave {c['clave']} · Capillas Marianas</span></div>
<p class="why">{c['por']}</p>
<div class="cols"><div><h3>Cada servicio incluye</h3><ul>{''.join(f'<li>{i}</li>' for i in c['inc']+COM)}</ul></div>
<div><div class="ph">{ph.split('</div>',1)[1] if False else ph}</div>
<div class="lst" style="margin-top:7px"><div class="a"><span>Precio de lista (2 servicios)</span><s>{m(L,1)}</s></div><div class="a sm"><span>36 mensualidades de lista</span><s>{m(c['ml'],1)}</s></div></div></div></div>
<h3 style="margin-top:6px">Su inversión con promoción · formas de pago</h3>
<table><tr><th>Forma de pago</th><th class="r">Mensualidad</th><th class="r">Precio total</th><th class="r">Ahorro vs. lista</th><th class="r">Equivale a</th></tr>{rows}</table>
<div class="gift"><div class="bx"><h4>🎁 Certificado Vacacional Royal Holiday</h4>Con tarjeta de crédito: 4 días / 3 noches todo incluido para 2 adultos y 2 menores (tarifa regular $24,995; cuota de reservación desde $3,999; aplican requisitos). Sujeto a disponibilidad.</div>
<div class="bx up"><h4>{c['up'][0]}</h4>{c['up'][1]}</div></div>
<div class="gift" style="grid-template-columns:1fr 1fr 1fr;gap:7px;margin-top:7px"><div class="bx">🔒 <b>Precio congelado</b> y sin intereses pagando a tiempo.</div><div class="bx">↩️ <b>5 días hábiles</b> después de firmar para cancelar con devolución.</div><div class="bx">💵 ¿Prefiere contado pero no hoy? Aparte con su 1ª mensualidad y liquide en <b>55 días</b>.</div></div>
<div class="steps"><div><b>1 · Aparte su folio</b>Solo correo electrónico e INE. No implica pago ni compromiso hoy.</div><div><b>2 · Revise su correo</b>De ABRAHAM CUTIPA QUENAYA, asunto “Asegura hoy la paz del mañana” (revise Spam).</div><div><b>3 · Firme desde su celular</b>Botón “Ver mi cotización” y firma electrónica en menos de 5 minutos.</div></div>
<div class="vig">⏰ Promoción vigente hasta el 30 de noviembre de 2026 · después aplica precio de lista</div>
<div class="nt"><b>Notas del asesor:</b></div>
<div class="ft"><span>Precios en pesos, sujetos a confirmación en el sistema de Gayosso al generar su folio. No incluye: derechos de inhumación o cremación, trámites y pago de actas, oficios religiosos, flores, traslados foráneos, maniobras de nicho ni embalsamamiento clínico. Si elige cremación, Gayosso informa si el ataúd aplica o hay diferencia de precio. Capillas Marianas: Av. Lázaro Cárdenas 1005 Pte., Col. Loma Larga, San Pedro Garza García, N.L. · Valide mi registro como asesor oficial: gayossocatrinas.com/951848-2</span>
<span class="sig"><b>Abraham Cutipa</b><br>Asesor Certificado de Previsión Familiar<br>WhatsApp 81 1627 6206</span></div></div>"""
for k in CAT:
  n=f"cotizacion_2{k}_marianas"+("" if CAT[k]['conf'] else "_POR_CONFIRMAR")
  open(f"{D}/{n}.html","w").write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{n}</title><style>{CSS}</style></head><body>{page(k)}</body></html>')
  print(n)
