# Genera 3 hojas imprimibles (carta vertical) de listas de precios de propiedad Gayosso Monterrey.
import os
D=os.path.dirname(os.path.abspath(__file__))
def m(x): return f"${x:,.0f}"
AGOT={'821965','821967','821964','821962'}
marianas=[ # zona, clave, desc, cap, lista, rebaja
("Zona Mausoleo","821966","Nicho chico · nivel sup/inf","2 urnas",27625,15),
("Zona Mausoleo","821965","Nicho chico · nivel medio","2 urnas",37295,5),
("Zona Mausoleo","821968","Nicho grande · nivel sup/inf","4 urnas",55250,15),
("Zona Mausoleo","821967","Nicho grande · nivel medio","4 urnas",74590,15),
("Zona Mausoleo","823562","Nicho grande cabecera · sup/inf","4 urnas*",71825,25),
("Zona Mausoleo","823550","Nicho grande cabecera · medio","4 urnas*",96965,25),
("Zona Mausoleo","823571","Nicho familiar cabecera · medio","6 urnas",193935,25),
("Zona Premier","821961","Nicho chico · nivel sup/inf","2 urnas",38680,20),
("Zona Premier","821960","Nicho chico · nivel medio","2 urnas",52215,25),
("Zona Premier","821964","Nicho grande · nivel sup/inf","4 urnas",77355,25),
("Zona Premier","821962","Nicho grande · nivel medio","4 urnas",104430,30),
("Zona Premier","824278","Nicho grande cabecera · sup/inf","4 urnas*",100560,30),
("Zona Premier","824277","Nicho grande cabecera · medio","4 urnas*",135755,25),
("Zona Capilla","823357","Nicho chico · nivel sup/inf","2 urnas",55250,25),
("Zona Capilla","823356","Nicho chico · nivel medio","2 urnas",74590,25),
("Zona Capilla","823358","Nicho grande · nivel sup/inf","4 urnas",110505,30),
("Zona Capilla","823359","Nicho grande · nivel medio","4 urnas",149180,30),
("Zona Capilla","823884","Nicho grande cabecera · sup/inf","4 urnas*",143655,25),
]
nogalar=[]
for z,base in [("Zona Mausoleo · piso 5",[("827302","Nicho chico · superior","2 urnas",32000,30),("827303","Nicho chico · medio","2 urnas",43205,30),("827304","Nicho chico · inferior","2 urnas",37600,30),
 ("827305","Nicho grande · superior","4 urnas",64000,30),("827306","Nicho grande · medio","4 urnas",86405,30),("827307","Nicho grande · inferior","4 urnas",75205,30),
 ("827311","Nicho grande cabecera · superior","4 urnas*",83200,40),("827312","Nicho grande cabecera · medio","4 urnas*",112320,40),("827313","Nicho grande cabecera · inferior","4 urnas*",97760,40),
 ("827308","Nicho familiar cabecera · superior","6 urnas*",166395,40),("827309","Nicho familiar cabecera · medio","6 urnas*",224650,30),("827310","Nicho familiar cabecera · inferior","6 urnas*",195520,40)]),
 ("Zona Premier · piso 5",[("827314","Nicho chico · superior","2 urnas",44800,40),("827315","Nicho chico · medio","2 urnas",60485,30),("827316","Nicho chico · inferior","2 urnas",52640,40),
 ("827317","Nicho grande · superior","4 urnas",89600,40),("827318","Nicho grande · medio","4 urnas",120970,40),("827319","Nicho grande · inferior","4 urnas",105285,40),
 ("827323","Nicho grande cabecera · superior","4 urnas*",116480,40),("827324","Nicho grande cabecera · medio","4 urnas*",157250,40),("827325","Nicho grande cabecera · inferior","4 urnas*",136865,40),
 ("827320","Nicho familiar cabecera · superior","6 urnas*",232955,40),("827321","Nicho familiar cabecera · medio","6 urnas*",314510,40),("827322","Nicho familiar cabecera · inferior","6 urnas*",273730,40)])]:
  nogalar+=[(z,)+r for r in base]
jardines=[
("Nichos y urnas","824763","Paq. ecológico Ciprés Italiano","1 urna",47385,0),
("Nichos y urnas","826493","Nicho chico preferencial · superior","2 urnas*",53725,25),
("Nichos y urnas","826495","Nicho chico preferencial · inferior","2 urnas*",66125,25),
("Nichos y urnas","826494","Nicho chico preferencial · medio","2 urnas*",78525,25),
("Nichos y urnas","826618","Sendero memorial Premier · inferior","4 urnas",87460,35),
("Nichos y urnas","826617","Sendero memorial Premier · medio","4 urnas",109140,35),
("Nichos y urnas","826616","Sendero memorial Premier · superior","4 urnas",130820,35),
("Gavetas (inhumación)","826490","Gaveta mural preferencial · superior","1 gaveta",84685,30),
("Gavetas (inhumación)","826492","Gaveta mural preferencial · inferior","1 gaveta",97230,40),
("Gavetas (inhumación)","826491","Gaveta mural preferencial · medio","1 gaveta",109780,35),
("Producto mayor","824751","Paq. jardín privado 4G 4OS","4 gav. + 4 os.",350300,5),
("Producto mayor","824991","Paq. capilla clásica sobre piso 6G 6O","6 gav. + 6 os.",838340,0),
("Producto mayor","825064","Paq. capilla Premier sobre piso 6G 6O","6 gav. + 6 os.",898220,0),
("Producto mayor","824992","Paq. capilla clásica bajo piso 6G 6O","6 gav. + 6 os.",1013480,0),
]
CSS="""@page{size:letter;margin:0}*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Helvetica Neue',Arial,sans-serif;color:#1d2b24;background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{width:8.5in;height:11in;padding:.42in .45in .35in;display:flex;flex-direction:column}
.hd{display:flex;align-items:center;gap:14px;border-bottom:3px solid #b8954a;padding-bottom:10px}
.hd img{height:54px}.hd .t{flex:1}.hd h1{font-size:21px;color:#0f4a36;letter-spacing:.3px}
.hd p{font-size:11px;color:#5b6b63;margin-top:2px}.hd .tag{text-align:right;font-size:10px;color:#5b6b63;line-height:1.45}
.hd .tag b{display:block;font-size:12px;color:#0f4a36}
.dir{font-size:10px;color:#5b6b63;margin:7px 0 8px}
table{width:100%;border-collapse:collapse;font-size:10.6px}
th{background:#0f4a36;color:#fff;font-weight:600;padding:5px 6px;text-align:left;font-size:9.8px;text-transform:uppercase;letter-spacing:.3px}
th.r,td.r{text-align:right}td{padding:var(--pd,4.3px) 6px;border-bottom:1px solid #e3e8e5}
tr.z td{background:#f3ede0;color:#7a5f22;font-weight:700;font-size:10.4px;padding:5px 6px;border-bottom:1px solid #d9c89f}
tr:nth-child(even):not(.z) td{background:#fafbfa}
td.k{font-family:Menlo,Consolas,monospace;color:#5b6b63;font-size:10px}td.c{color:#0f4a36;font-weight:600}
td.p{font-weight:700}td.d{color:#9a7a30;font-weight:600}td.f{font-weight:700;color:#0f4a36}
tr.ag td{color:#a0a6a3;text-decoration:line-through}tr.ag td.st{text-decoration:none;color:#b3261e;font-weight:700}
td.st{font-size:9px;color:#2e7d32;font-weight:700}
.box{margin-top:auto;display:grid;grid-template-columns:1fr 1fr;gap:10px;padding-top:10px}
.b{border:1px solid #d9c89f;border-radius:6px;padding:8px 10px;font-size:9.6px;line-height:1.45;background:#fdfaf3}
.b h3{font-size:10.4px;color:#0f4a36;margin-bottom:3px}
.ft{margin-top:8px;border-top:1px solid #e3e8e5;padding-top:6px;font-size:8.8px;color:#6b7a72;display:flex;justify-content:space-between;gap:12px}
.note{font-size:9.5px;color:#5b6b63;margin-top:6px;line-height:1.4}"""
def page(title,sub,sede,dirs,rows,boxes,notes,pad=4.3):
  h=[f'<div class="pg" style="--pd:{pad}px"><div class="hd"><img src="../logo.jpg"><div class="t"><h1>{title}</h1><p>{sub}</p></div><div class="tag"><b>{sede}</b>Lista de precios de propiedad<br>Vigencia: noviembre 2026</div></div><div class="dir">📍 {dirs}</div>',
     '<table><tr><th>Clave</th><th>Producto</th><th>Capacidad</th><th class="r">Precio lista</th><th class="r">Rebaja en paquete**</th><th class="r">Contado solo*</th><th class="r">Estatus</th></tr>']
  last=None
  for z,k,d,c,p,r in rows:
    if z!=last: h.append(f'<tr class="z"><td colspan="7">{z}</td></tr>');last=z
    ag=k in AGOT
    h.append(f'<tr class="{"ag" if ag else ""}"><td class="k">{k}</td><td>{d}</td><td class="c">{c}</td><td class="r p">{m(p)}</td><td class="r d">{r}%</td><td class="r f">{m(p*0.80)}</td><td class="r st">{"AGOTADO" if ag else "Disponible"}</td></tr>')
  h.append('</table>'+''.join(f'<p class="note">{n}</p>' for n in notes))
  h.append('<div class="box">'+''.join(f'<div class="b"><h3>{a}</h3>{b}</div>' for a,b in boxes)+'</div>')
  h.append('<div class="ft"><span>*Contado solo = lista × 0.80 (P001, producto sin servicios; confirmado en nichos Nogalar, jardín privado y gaveta mural). **La rebaja comercial aplica en paquetes con servicios (p. ej. 2 Esencial + nicho = lista × 0.70 × factor de pago). Precio final, mensualidades y promociones: SIEMPRE del Cotizador. Uso a perpetuidad; inventario sujeto a disponibilidad.</span><span style="white-space:nowrap"><b>Abraham Cutipa</b> · Asesor de Previsión<br>WhatsApp 81 1627 6206</span></div></div>')
  return ''.join(h)
mant_n=("Cuotas anuales (hoja oficial Monterrey)","Nicho chico / individual: <b>$1,150</b> mantenimiento + <b>$900</b> conservación<br>Nicho grande / familiar: <b>$1,700</b> + <b>$900</b> conservación<br>Se cobran a partir de los 6 meses o al primer uso.")
noinc=("No incluido en el precio","No incluye: apertura y cierre del nicho (depósito de cenizas), grabado de placa, derechos y trámites. Depósito: acta, orden y certificado de cremación, INE, número de contrato; documentos escaneados a coordeservicios_mty@gayosso.com.")
P=[("lista_nichos_marianas",page("Nichos · Mausoleo Capillas Marianas","Centro GG34 · Oficina MC26","CAPILLAS MARIANAS","Av. Lázaro Cárdenas 1005 Pte., Col. Loma Larga, San Pedro Garza García, N.L., C.P. 64710",marianas,
  [("Capacidad y niveles","Chico = 2 urnas · Grande = 4 urnas · Familiar = 6 urnas.<br>Niveles por filas: superior (A–C), medio (D–F), inferior (G–H). El nivel medio (a la altura de la vista) es el más solicitado.<br>Medidas aprox.: chico 27×25×40 cm; grande 56×25×40 cm."),mant_n],
  ["<b>AGOTADOS</b> (confirmado 11-nov): 821965, 821967, 821964, 821962. Alternativa nivel medio 4 urnas: cabecera mausoleo 823550 o Nogalar grande medio 827306. Contado de Marianas: referencia, sin captura del Cotizador. *Capacidad de nichos de cabecera por confirmar en oficina. "+noinc[1]],pad=8.2)),
 ("lista_nichos_nogalar",page("Nichos · Mausoleo Marianas Nogalar","Centro MNM1 · Oficina MIN1 · piso 5","MARIANAS NOGALAR","Av. Nogalar Sur 420 A, San Nicolás de los Garza, C.P. 66484, N.L. · Apertura diciembre 2026 · Visitas con cita: lunes 9:00–14:00",nogalar,
  [("Preventa Nogalar","Paquetes integrales nicho + servicios con descuento adicional (2 o 3 servicios: 30%; 4 servicios: 35%).<br>Ejemplo confirmado: 2 Esencial Pro + nicho chico superior, contado $72,016 o 48 × $1,816.24 TDC: el nicho sale de regalo."),mant_n],
  ["Contado confirmado con Cotizador: 827302, 827303, 827304 y 827305; el resto es referencia. *Capacidad de nichos de cabecera (grande 4 / familiar 6) por confirmar en oficina. En Nogalar el nivel inferior es intermedio en precio; el superior es el más accesible. "+noinc[1]])),
 ("lista_jardines_descanso",page("Cementerio Jardines del Descanso","Centro GG12 · Oficina CJ04","JARDINES DEL DESCANSO","Calle de la Meza 7650, Col. La Estanzuela, Monterrey, N.L., C.P. 64988 · Tel. (81) 8317 8505",jardines,
  [("Medidas (catálogo Gayosso)","Jardín privado: 2.24 × 2.94 m, 7.65 m², 4 gavetas + 4 osarios bajo piso; se usa con 100% pagado.<br>Gaveta mural: 0.90 × 2.50 × 0.80 m, tapa de mármol, 1 gaveta.<br>Capillas: 6 gavetas + 6 osarios, loseta y cancel. Ciprés: 30×40×35 cm, 1 urna.<br>Sendero memorial: forrado de mármol, 4 urnas."),
   ("Cuotas anuales (hoja oficial Monterrey)","Gaveta mural / Ciprés: <b>$1,700</b> + <b>$750</b> conservación<br>Sendero memorial: <b>$1,700</b><br>Jardines: <b>$2,800</b> + <b>$1,050</b> conservación<br>Capillas: <b>$3,500</b> + <b>$1,050</b> conservación<br>Nichos: $1,150 / $1,700 + $900")],
  ["Contado de Ciprés, sendero, nicho preferencial y capillas: referencia, sin captura del Cotizador. Rebaja de sendero y gaveta mural incluye 5% adicional \"150 años\". *Capacidad del nicho chico preferencial por confirmar. Para 4 personas conviene el jardín privado (contado $280,240 = $70,060 por lugar) sobre 4 gavetas murales. Incluye servicio de inhumación en jardín privado y gaveta mural. No incluye: derechos ante autoridad, apertura/cierre, grabado de lápida, mantenimiento."],pad=10.5))]
for n,body in P:
  open(f"{D}/{n}.html","w").write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{n}</title><style>{CSS}</style></head><body>{body}</body></html>')
open(f"{D}/listas_precios_propiedad.html","w").write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Listas de precios</title><style>{CSS}</style></head><body>'+''.join(b for _,b in P)+'</body></html>')
