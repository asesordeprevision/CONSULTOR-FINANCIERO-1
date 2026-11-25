CSS='''*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;font-family:"DejaVu Sans",Arial,sans-serif;overflow:hidden;background:#0f2e17;color:#fff}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.sh{position:absolute;inset:0}
.logo{position:absolute;top:34px;left:40px;background:#fff;border-radius:14px;padding:8px 12px}.logo img{height:70px;display:block}
.tag{position:absolute;top:44px;right:40px;background:#c62828;border:3px solid #e6c66e;border-radius:30px;padding:10px 22px;font-weight:bold;font-size:22px;letter-spacing:1px}
.box{position:absolute;left:40px;right:40px}
h1{font-size:64px;line-height:1.08;font-weight:900;text-shadow:0 3px 14px rgba(0,0,0,.6)}
h1 span{color:#ffd76a}
.sub{font-size:28px;line-height:1.35;margin-top:14px;text-shadow:0 2px 10px rgba(0,0,0,.6)}
.price{display:inline-block;margin-top:22px;background:#fff;color:#1f5f2a;border-radius:18px;padding:14px 26px;border:4px solid #e6c66e}
.price small{display:block;font-size:20px;color:#555;font-weight:bold}
.price b{font-size:56px;font-weight:900}.price b i{font-size:22px;font-style:normal}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.chips div{background:rgba(255,255,255,.14);border:2px solid rgba(255,255,255,.5);border-radius:30px;padding:8px 16px;font-size:21px;font-weight:bold}
.cta{position:absolute;left:40px;right:40px;bottom:40px;background:#25a244;border-radius:40px;text-align:center;font-size:32px;font-weight:bold;padding:20px;box-shadow:0 6px 20px rgba(0,0,0,.4)}
.fine{position:absolute;left:40px;right:40px;bottom:12px;font-size:13px;color:rgba(255,255,255,.75);text-align:center}
.strip{position:absolute;left:40px;right:40px;display:flex;gap:10px}
.strip div{flex:1;height:200px;border-radius:14px;background-size:cover;background-position:center;border:3px solid #e6c66e;position:relative}
.strip span{position:absolute;left:0;right:0;bottom:0;background:rgba(0,0,0,.65);font-size:16px;font-weight:bold;text-align:center;padding:5px}
'''
FINE='Precio de lista $128,600. Desde $1,816.24 al mes = 2 servicios Previsión Gayosso Esencial Pro + nicho para 2 urnas en Mausoleo Nogalar, 48 meses con tarjeta de crédito. Vigencia 30-nov-2026, sujeto a disponibilidad.'
def page(name,body):
    open(name+'.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}<div class="fine">{FINE}</div></body></html>')
L='<div class="logo"><img src="../logo.jpg"></div>'
CTA='<div class="cta">💬 Escríbame por WhatsApp</div>'
# A: evolucion del ganador Fin de Año
page('fria_A_fin_de_ano', f'''<div class="bg" style="background-image:url(../fotos_nogalar/sala_catafalco_frente.jpg)"></div>
<div class="sh" style="background:linear-gradient(180deg,rgba(10,40,20,.25) 0%,rgba(10,40,20,.55) 45%,rgba(8,30,15,.95) 100%)"></div>{L}
<div class="tag">CIERRE 2026</div>
<div class="box" style="top:520px"><h1>2026 está por terminar.<br><span>¿Ya protegió a su familia?</span> ❤️</h1>
<div class="sub">Deje resuelto el servicio y el lugar de descanso, para que nadie decida bajo presión ni pague de más cuando más duele.</div>
<div class="price"><small>2 servicios + nicho de regalo · desde</small><b>$1,816<i>/mes</i></b></div>
<div class="chips"><div>✔ Sin enganche</div><div>✔ Precio congelado</div><div>✔ Grupo Gayosso desde 1875</div></div></div>{CTA}''')
# B: novedad Nogalar
page('fria_B_nueva_nogalar', f'''<div class="bg" style="background-image:url(../fotos_nogalar/fachada_jardineras.jpg);background-position:center 30%"></div>
<div class="sh" style="background:linear-gradient(180deg,rgba(0,0,0,.15) 0%,rgba(8,30,15,.35) 35%,rgba(8,30,15,.96) 62%)"></div>{L}
<div class="tag">PREVENTA</div>
<div class="box" style="top:600px"><h1>Nueva <span>Capillas Marianas Nogalar</span> en San Nicolás</h1>
<div class="sub">Abre en diciembre. Hoy puede asegurar su lugar con precio de preventa.</div></div>
<div class="strip" style="top:900px"><div style="background-image:url(../fotos_nogalar/nichos_madera_cristal.jpg)"><span>Mausoleo · nichos</span></div><div style="background-image:url(../fotos_nogalar/sala_catafalco_pasillo.jpg)"><span>Salas de velación</span></div><div style="background-image:url(../fotos_nogalar/sala_amplia_sillones.jpg)"><span>Áreas para su familia</span></div></div>
<div class="box" style="top:1120px"><div class="chips" style="margin-top:0"><div>🎁 2 servicios + nicho de regalo</div><div>desde $1,816/mes</div><div>⏰ hasta el 30 de nov.</div></div></div>{CTA}''')
# C: pregunta emocional
page('fria_C_pregunta', f'''<div class="bg" style="background-image:url(../fotos_nogalar/nichos_madera_cristal.jpg)"></div>
<div class="sh" style="background:linear-gradient(180deg,rgba(8,30,15,.92) 0%,rgba(8,30,15,.55) 40%,rgba(8,30,15,.95) 78%)"></div>{L}
<div class="box" style="top:170px"><h1 style="font-size:60px">Si mañana usted faltara,<br><span>¿su familia sabría qué hacer?</span></h1>
<div class="sub">Cuando ocurre, todo se decide en horas, con prisa y a precio de urgencia. Usted puede dejarlo resuelto hoy, con calma.</div></div>
<div class="box" style="top:830px"><div class="price"><small>Servicio para 2 personas + nicho de regalo</small><b>desde $1,816<i>/mes</i></b></div>
<div class="chips"><div>✔ Inhumación o cremación</div><div>✔ Sin enganche</div><div>✔ Sin intereses</div></div></div>{CTA}''')
