import sys
STY={
 'verde':dict(bg='linear-gradient(160deg,#0b2e19 0%,#14472a 60%,#0b2e19 100%)',fg='#fff',acc='#d9b55e',sub='#cfe0d3',card='rgba(255,255,255,.06)',line='#d9b55e',pill='#25a244'),
 'negro':dict(bg='linear-gradient(160deg,#0d0d0d 0%,#1d1d1d 60%,#0d0d0d 100%)',fg='#fff',acc='#d4af5a',sub='#cfcfcf',card='rgba(255,255,255,.05)',line='#d4af5a',pill='#25a244'),
 'marfil':dict(bg='linear-gradient(160deg,#fbf8f1 0%,#f3eee2 100%)',fg='#14331f',acc='#a8822f',sub='#4b5b50',card='#fff',line='#a8822f',pill='#1f7a3a'),
}
def card(st,kick,title,sub,img,imgbg,save,mes,cont,lista,vig,extra=""):
  s=STY[st]
  return f'''<!doctype html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1080px;font-family:"DejaVu Sans",Arial,sans-serif;background:{s['bg']};color:{s['fg']};overflow:hidden}}
.w{{position:absolute;inset:26px;border:2px solid {s['line']};border-radius:22px;padding:30px 40px;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:center}}
.lg{{background:#fff;border-radius:10px;padding:5px 9px}}.lg img{{height:52px;display:block}}
.kick{{font-size:16px;letter-spacing:5px;color:{s['acc']};font-weight:bold;text-align:right}}
h1{{font-family:"DejaVu Serif",serif;font-size:50px;line-height:1.05;margin-top:22px}}
.sub{{font-size:21px;color:{s['sub']};margin-top:8px}}
.mid{{display:flex;gap:26px;margin-top:24px;flex:1}}
.ph{{position:relative;width:430px;border-radius:16px;background:{imgbg};display:flex;align-items:center;justify-content:center;overflow:hidden;border:1px solid {s['line']}}}
.chip{{position:absolute;left:12px;right:12px;bottom:12px;background:#fff;border-radius:12px;padding:8px;display:flex;align-items:center;gap:10px;color:#14331f;font-size:14px;font-weight:bold}}.chip img{{height:58px;max-width:55%}}
.feat{{list-style:none;font-size:16px;line-height:1.55;color:{s['sub']}}}.feat li:before{{content:'✔ ';color:{s['acc']};font-weight:bold}}
.ph img{{max-width:100%;max-height:100%}}.ph img.cov{{width:100%;height:100%;object-fit:cover}}
.info{{flex:1;display:flex;flex-direction:column;gap:12px}}
.save{{background:{s['acc']};color:#1a1406;border-radius:14px;text-align:center;padding:12px}}
.save b{{display:block;font-size:56px;line-height:1}}.save span{{font-size:16px;font-weight:bold;letter-spacing:2px}}
.box{{background:{s['card']};border:1px solid {s['line']};border-radius:14px;padding:12px 16px}}
.box .l{{font-size:14px;color:{s['sub']}}}.box .v{{font-size:34px;font-weight:bold}}.box .v small{{font-size:17px}}
.lista{{font-size:17px;color:{s['sub']}}}.lista s{{color:{s['sub']}}}
.bot{{display:flex;justify-content:space-between;align-items:center;margin-top:20px;border-top:1px solid {s['line']};padding-top:14px}}
.vig{{font-size:16px;color:{s['acc']};font-weight:bold}}.vig small{{display:block;color:{s['sub']};font-weight:normal;font-size:13px;margin-top:2px}}
.wa{{background:{s['pill']};color:#fff;font-weight:bold;font-size:20px;padding:10px 20px;border-radius:30px}}
{extra}
</style></head><body><div class="w">
<div class="top"><div class="lg"><img src="../logo.jpg"></div><div class="kick">{kick}</div></div>
<h1>{title}</h1><div class="sub">{sub}</div>
<div class="mid"><div class="ph">{img}</div><div class="info">
{save}{mes}{cont}<div class="lista">{lista}</div></div></div>
<div class="bot"><div class="vig">{vig}</div><div class="wa">WhatsApp 81 1627 6206</div></div>
</div></body></html>'''

def offer(st,kick,title,sub,img,imgbg,pct,mes,mesl,cont,contpct,lista,feat='',vig='⏰ Vigente al 30 de noviembre<small>Precio congelado · sin intereses · certificado vacacional con TDC</small>'):
  return card(st,kick,title,sub,img,imgbg,
   f'<div class="save"><span>AHORRE HASTA</span><b>{pct}</b></div>',
   f'<div class="box"><div class="l">{mesl}</div><div class="v">${mes}<small>/mes</small></div></div>',
   f'<div class="box"><div class="l">De contado · ahorre {contpct}</div><div class="v">${cont}</div></div>',
   f'Precio de lista <s>${lista}</s><ul class="feat" style="margin-top:10px">{feat}</ul>',vig)

P=dict(kick='PROMOCIÓN 2 + 1',title='Premier Pro<br>3 servicios por 2',sub='El tercer servicio sin costo · válido en 24 agencias del país',
  img='<img class="cov" src="../fotos_nogalar/lobby.jpg"><div class="chip"><img src="../ataudes/celesti.jpg">Ataúd de lujo · Sala Premier 60 personas</div>',imgbg='#000',feat='<li>Sala Premier y ataúd de lujo</li><li>Inhumación o cremación</li><li>Copia del acta de defunción</li>',pct='47%',mes='3,321',mesl='Desde · T. crédito 48 meses',cont='131,687',contpct='47%',lista='246,900')
for st in STY:
  open(f'muestra_{st}.html','w').write(offer(st,**P))
if len(sys.argv)>1:
  st=sys.argv[1]
  open('01_categorias.html','w').write(card(st,'PRECIOS DE LISTA','Elija su<br>categoría','Ambivalentes: inhumación o cremación, a elegir al momento',
   '<img class="cov" src="../fotos_nogalar/sala_velacion.jpg"><div class="chip"><img src="../ataudes/iter_pax.jpg" style="height:34px"><img src="../ataudes/legatum.jpg" style="height:34px"><img src="../ataudes/celesti.jpg" style="height:34px"></div>','#000',
   '','<div class="box"><div class="l">Esencial Pro · sala 20 personas</div><div class="v">$48,300</div></div><div class="box"><div class="l">Universal Pro · sala 40 personas</div><div class="v">$62,300</div></div><div class="box" style="border-width:2px"><div class="l">Premier Pro · sala 60 · Multiplaza</div><div class="v">$82,300</div></div>',
   '','Pregunte por la promoción del mes<ul class="feat" style="margin-top:14px;font-size:17px"><li>Traslados y asesoría en trámites</li><li>Embalsamado y arreglo estético</li><li>Cafetería básica</li><li>Urna si elige cremación</li><li>100% transferible</li></ul>','💳 Mensualidades sin intereses<small>Precio congelado · 100% transferible · PROFECO</small>'))
  open('02_premier_2mas1.html','w').write(offer(st,**P))
  open('03_universal_2mas1.html','w').write(offer(st,'PROMOCIÓN 2 + 1','Universal Pro<br>3 servicios por 2','El tercer servicio sin costo · ataúd de metal o madera',
   '<img class="cov" src="../fotos_nogalar/lobby2.jpg"><div class="chip"><img src="../ataudes/legatum.jpg">Metal o madera · sala 40 personas</div>','#000','47%','2,514','Desde · T. crédito 48 meses','99,685','47%','186,900',feat='<li>Ataúd de metal o madera</li><li>Inhumación o cremación</li><li>Embalsamado y cafetería</li>'))
  open('04_esencial2_nicho.html','w').write(offer(st,'NICHO DE REGALO','2 Esencial Pro<br>+ nicho de regalo','Servicio para 2 personas + nicho para 2 urnas · Marianas Nogalar',
   '<img class="cov" src="../nogalar_nichos1.jpg">','#000','44%','1,816','Desde · T. crédito 48 meses','72,016','44%','128,600',feat='<li>Velación y cremación o inhumación</li><li>Nicho a perpetuidad</li><li>Nueva casa funeraria · San Nicolás</li>'))
  open('05_jardin_privado.html','w').write(offer(st,'PROPIEDAD A PERPETUIDAD','Jardín privado<br>para 4','4 gavetas y 4 osarios · Jardines del Descanso',
   '<img class="cov" src="../jardin_privado_foto.jpg">','#000','20%','6,789','Enganche 20% + 35 mensualidades','280,240','20%','350,300',feat='<li>Terreno a perpetuidad</li><li>4 gavetas y 4 osarios bajo piso</li><li>Para toda la familia</li>',
   vig='🌳 2.24 × 2.94 m · 7.65 m²<small>Incluye construcción y servicio de inhumación</small>'))
