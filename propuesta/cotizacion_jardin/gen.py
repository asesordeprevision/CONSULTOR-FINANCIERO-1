# Cotización formal imprimible JARDÍN PRIVADO (Jardines del Descanso, CJ04): solo y con 1 Premier Pro. python3 gen.py
import os,re,datetime
D=os.path.dirname(os.path.abspath(__file__))
CSS=re.search(r'CSS="""(.*?)"""',open(f"{D}/../cotizacion_marianas/gen.py").read(),re.S).group(1)
CSS+=""".nt{flex:1;margin-top:8px;min-height:30px;border:1px dashed #c9d2cd;border-radius:7px;padding:5px 10px;font-size:9.5px;color:#6b7a72;background:repeating-linear-gradient(transparent 0 21px,#e3e8e5 21px 22px)}
.ft{margin-top:8px}.big img{width:100%;height:150px;object-fit:cover;border-radius:8px}.big div{font-size:8.5px;color:#5b6b63;text-align:center}
td .sub{font-size:9.6px;color:#33433b}"""
def m(x,c=True): return f"${x:,.2f}" if c else f"${x:,.0f}"
MESES=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
hoy=datetime.datetime.now(datetime.UTC).replace(tzinfo=None)-datetime.timedelta(hours=6); fecha=f"{hoy.day} de {MESES[hoy.month-1]} de {hoy.year}"
# --- Cifras (actualizar con capturas del Cotizador) ---
J=dict(lista=350300.01,ml=9738.34,cont=280240.01,d012=(297755.01,44663.25,11,23016.46),d020=(297755.01,59551.00,35,6788.81),d048=(339791.01,7067.65))
P=dict(lista=82300.01,ml=2287.94,cont=52672.00,d048=(71847.91,1494.44),d036=(68144.41,1894.41))
INC_J=["<b>Terreno a perpetuidad</b> con capacidad para <b>4 gavetas y 4 osarios</b> bajo piso","Construcción de concreto armado, delimitada con barda perimetral (lote 2 × 3 m)","<b>4 servicios de inhumación</b> incluidos, con preparación del lote","Toldo de protección, sillería y alfombra tipo césped","Descensor automático, jefe ceremonial con atril, amplificador y micrófono","Ceremonia de inhumación","<b>Título de Derecho de Uso a Perpetuidad</b> al liquidar, con plano de ubicación"]
INC_P=["<b>Sala de velación Premier</b> 24 h para 60 personas en Capillas Marianas","Ataúd de lujo de metal o madera cat. Premier, o urna de lujo si elige cremación","<b>Multiplaza:</b> válido en las 24 agencias Gayosso del país","Traslados, embalsamamiento, arreglo estético, cafetería básica y asesoría en trámites","<b>Ambivalente</b> (inhumación o cremación) y copia del acta de defunción"]
def head(t,sub,lugar):
  return f"""<div class="hd"><img src="../logo.jpg"><div class="t"><h1>PROPUESTA DE PROPIEDAD A PERPETUIDAD</h1><h2>{t}</h2></div><div class="r">{lugar}<br><b>{fecha}</b></div></div>
<div class="to"><span>Para:</span><span class="ln"></span><span>Tel.:</span><span class="ln" style="flex:.55"></span></div>
<p class="intro">Es un gusto saludarle. Conforme a lo que platicamos, le comparto la propuesta {sub}, con el detalle de lo que incluye, su inversión y las formas de pago disponibles.</p>"""
STEPS="""<div class="steps"><div><b>1 · Aparte su folio</b>Solo correo electrónico e INE. No implica pago ni compromiso hoy.</div><div><b>2 · Revise su correo</b>De ABRAHAM CUTIPA QUENAYA, asunto “Asegura hoy la paz del mañana” (revise Spam).</div><div><b>3 · Firme desde su celular</b>Botón “Ver mi cotización” y firma electrónica en menos de 5 minutos.</div></div>
<div class="vig">⏰ Precios vigentes hasta el 30 de noviembre de 2026 · inventario sujeto a disponibilidad</div><div class="nt"><b>Notas del asesor:</b></div>"""
def foot(extra):
  return f"""<div class="ft"><span>Precios en pesos, sujetos a confirmación en el sistema de Gayosso al generar su folio. El jardín privado se usa con el 100% pagado y genera cuota anual de mantenimiento ($2,800) y conservación ($1,050) a partir de los 6 meses o del primer uso. No incluye: derechos de inhumación ante autoridad, grabado de lápida, gestión de actas ni permisos. {extra}Cementerio Jardines del Descanso: Calle de la Meza 7650, Col. La Estanzuela, Monterrey, N.L. · Tel. (81) 8317 8505 · abierto todos los días. Valide mi registro como asesor oficial: gayossocatrinas.com/951848-2</span>
<span class="sig"><b>Abraham Cutipa</b><br>Asesor Certificado de Previsión Familiar<br>WhatsApp 81 1627 6206</span></div>"""
def ah(lista,t): return f'{m(lista-t,False)} <span class="sm">({(lista-t)/lista*100:.0f}%)</span>'
def jardin():
  L=J['lista'];c12,e12,n12,m12=J['d012'];c20,e20,n20,m20=J['d020'];c48,m48=J['d048']
  rows=f"""<tr class="st"><td><b>Contado</b><span class="tg g">MAYOR AHORRO</span><div class="sm">Una sola exhibición · {m(J['cont']/4,False)} por lugar</div></td><td class="r">—</td><td class="r mo">{m(J['cont'])}</td><td class="r sv">{ah(L,J['cont'])}</td></tr>
<tr><td><b>12 meses con enganche 15%</b><div class="sm">Domiciliado</div></td><td class="r"><span class="sub">Enganche {m(e12)}</span><br><span class="mo">{n12} × {m(m12)}</span></td><td class="r">{m(c12)}</td><td class="r sv">{ah(L,c12)}</td></tr>
<tr class="st"><td><b>35 meses con enganche 20%</b><span class="tg">RECOMENDADO</span><div class="sm">Mismo ahorro que 12 meses, mensualidad menor</div></td><td class="r"><span class="sub">Enganche {m(e20)}</span><br><span class="mo">{n20} × {m(m20)}</span></td><td class="r">{m(c20)}</td><td class="r sv">{ah(L,c20)}</td></tr>
<tr><td><b>Tarjeta de crédito · 48 meses</b><div class="sm">Sin enganche · sin intereses</div></td><td class="r mo">48 × {m(m48)}</td><td class="r">{m(c48)}</td><td class="r sv">{ah(L,c48)}</td></tr>"""
  return f"""<div class="pg">{head("Jardín Privado · Jardines del Descanso","de un <b>lugar propio y permanente</b> donde su familia podrá reunirse y descansar unida","Monterrey, N.L.")}
<div class="band"><b>JARDÍN PRIVADO · 4 GAVETAS + 4 OSARIOS</b><span>Clave 824751 · Cementerio Jardines del Descanso</span></div>
<p class="why">Un espacio a perpetuidad con <b>4 gavetas y 4 osarios</b> para que la familia descanse unida, con jardín propio y barda perimetral: su familia no tendrá que buscar ni pagar un lugar en el momento más difícil.</p>
<div class="cols"><div><h3>Incluye</h3><ul>{''.join(f'<li>{i}</li>' for i in INC_J)}</ul></div>
<div><div class="big"><img src="../jardin_privado_ficha_foto.jpg"><div>Jardín privado · imagen representativa</div></div>
<div class="lst" style="margin-top:7px"><div class="a"><span>Precio de lista</span><s>{m(L)}</s></div><div class="a sm"><span>36 mensualidades de lista</span><s>{m(J['ml'])}</s></div><div class="a sm"><span>Por lugar (4 gavetas)</span><s>{m(L/4,False)}</s></div></div></div></div>
<h3 style="margin-top:6px">Su inversión · formas de pago</h3>
<table><tr><th>Forma de pago</th><th class="r">Pagos</th><th class="r">Precio</th><th class="r">Ahorro vs. lista</th></tr>{rows}</table>
<div class="gift"><div class="bx"><h4>🔒 Su propiedad, protegida</h4>Precio congelado y sin intereses pagando a tiempo. Pagos anticipados sin penalización. 5 días hábiles después de firmar para cancelar con devolución. Hasta 2 beneficiarios y titular sustituto.</div>
<div class="bx up"><h4>¿Y el servicio funerario?</h4>Complete su plan con <b>Previsión Gayosso Premier Pro</b>: desde <b>48 × $1,494.44</b> con tarjeta de crédito o <b>$52,672 de contado</b>. Velación en Capillas Marianas y, con el jardín, todo queda resuelto.</div></div>
{STEPS}{foot("")}</div>"""
def combo():
  LJ,LP=J['lista'],P['lista'];L=LJ+LP;c20,e20,n20,m20=J['d020'];c48,m48=J['d048'];p48,pm48=P['d048']
  r1=J['cont']+P['cont'];r2=c20+p48;r3=c48+p48
  rows=f"""<tr class="st"><td><b>Contado ambos</b><span class="tg g">MAYOR AHORRO</span><div class="sm">Jardín {m(J['cont'])} + Premier {m(P['cont'])}</div></td><td class="r">—</td><td class="r mo">{m(r1)}</td><td class="r sv">{ah(L,r1)}</td></tr>
<tr class="st"><td><b>Jardín con enganche 20% + Premier a 48 meses</b><span class="tg">RECOMENDADO</span><div class="sm">Enganche del jardín {m(e20)} · después solo Premier del mes 36 al 48 ({m(pm48)})</div></td><td class="r"><span class="sub">Meses 1–35</span><br><span class="mo">{m(m20+pm48)}</span></td><td class="r">{m(r2)}</td><td class="r sv">{ah(L,r2)}</td></tr>
<tr><td><b>Ambos con tarjeta de crédito · 48 meses</b><div class="sm">Sin enganche · jardín {m(m48)} + Premier {m(pm48)}</div></td><td class="r mo">48 × {m(m48+pm48)}</td><td class="r">{m(r3)}</td><td class="r sv">{ah(L,r3)}</td></tr>"""
  return f"""<div class="pg">{head("1 Premier Pro + Jardín Privado","para dejar resuelto <b>todo en un solo plan</b>: el servicio funerario más completo de Gayosso y el lugar de descanso de su familia","Monterrey, N.L.")}
<div class="band"><b>PREMIER PRO + JARDÍN PRIVADO 4 GAVETAS 4 OSARIOS</b><span>Claves 826890 + 824751</span></div>
<p class="why">Servicio, velación y lugar de descanso resueltos de una vez: la familia solo hace una llamada al <b>*247</b> y Gayosso se encarga del resto.</p>
<div class="cols"><div><h3>Previsión Premier Pro (1 servicio)</h3><ul>{''.join(f'<li>{i}</li>' for i in INC_P)}</ul>
<h3 style="margin-top:5px">Jardín privado</h3><ul>{''.join(f'<li>{i}</li>' for i in [INC_J[0],INC_J[2],INC_J[3]+"; descensor, jefe ceremonial y ceremonia",INC_J[6]])}</ul></div>
<div><div class="big"><img src="../jardin_privado_ficha_foto.jpg" style="height:128px"><div>Jardín privado · imagen representativa</div></div>
<div class="lst" style="margin-top:7px"><div class="a"><span>Premier Pro, lista</span><s>{m(LP)}</s></div><div class="a"><span>Jardín privado, lista</span><s>{m(LJ)}</s></div><div class="a"><span><b>Total de lista</b></span><s><b>{m(L)}</b></s></div><div class="a sm"><span>36 mensualidades de lista</span><s>{m(J['ml']+P['ml'])}</s></div></div></div></div>
<h3 style="margin-top:6px">Su inversión · formas de pago</h3>
<table><tr><th>Forma de pago</th><th class="r">Mensualidad</th><th class="r">Precio</th><th class="r">Ahorro vs. lista</th></tr>{rows}</table>
<div class="gift"><div class="bx"><h4>🎁 Certificado Vacacional Royal Holiday</h4>Con el contrato Premier pagado con tarjeta de crédito: 4 días / 3 noches todo incluido (tarifa regular $24,995; cuota de reservación desde $3,999; aplican requisitos).</div>
<div class="bx up"><h4>¿Más familia por proteger?</h4>Con la <b>Promoción 2 + 1</b> lleva 3 servicios Premier Pro: <b>48 × $3,321.14</b> o <b>$131,686.58 de contado</b>. El jardín tiene 4 gavetas para la familia.</div></div>
{STEPS}{foot("Son dos contratos: Premier (Capillas Marianas) y jardín (Jardines del Descanso). ")}</div>"""
for n,f in [("cotizacion_jardin_privado",jardin),("cotizacion_premier_jardin_privado",combo)]:
  open(f"{D}/{n}.html","w").write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{n}</title><style>{CSS}</style></head><body>{f()}</body></html>');print(n)
