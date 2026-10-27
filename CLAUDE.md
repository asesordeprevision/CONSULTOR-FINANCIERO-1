# Consultor Financiero — memoria de campañas Meta Ads

Cuenta publicitaria principal: `789501147519125` (negocio "Abraham Cutipa - Asesor Financiero", MXN).
La cuenta `1779143873445450` ("Consultor Financiero" / Previsión Familiar) aún no está habilitada para Ads MCP.
Mercado: previsión funeraria / previsión familiar en Nuevo León (Monterrey y área metropolitana).

## Reglas de segmentación para TODA campaña nueva (o al editar una existente)

Origen: 2026-10-06 llegaron conversaciones de WhatsApp con números extranjeros aunque el 100% de la entrega fue en MX.

- Tipos de ubicación: solo `home` y `frequently_in`. **Nunca** `recent` (atrae viajeros, transportistas y gente de paso por Monterrey).
- Ubicaciones (placements) manuales, sin Audience Network:
  - publisher_platforms: facebook, instagram, whatsapp
  - facebook_positions: feed, story, facebook_reels, marketplace, profile_feed, instream_video (sin `search` ni `notification`)
  - instagram_positions: stream, story, reels, explore_home, profile_feed
  - whatsapp_positions: status
- Advantage+ audience puede quedar activo, pero con expansión geográfica apagada (`individual_setting.geo = 0`).
- Edad para previsión: 25–65.
- Mantener exclusión de la audiencia "Retargeting Nogalar - Interaccion Pagina 365d" (`120255465505980768`) en campañas de captación en frío. OJO: esa audiencia son los que interactuaron con la página de previsión (`826648143857806`); excluirla solo tiene sentido si existe una campaña de retargeting que SÍ la incluya.
- Audiencias calientes disponibles: "Público Unificado - Engagers Página Gayosso (365d)" (`120255894808770768`), "AUD_NL_FanPageUnificada_365d" (`120256036448630768`), "Video Engagement - Reel Creditos Pensionados" (`120255905930770768`). Excluir siempre "[DB][Lista de Clientes]" (`120256226767570768`).
- El lookalike de la lista de clientes (`120256297242750768`) está creado sobre US, no MX: no usarlo; recrear en MX.

## Aprendizajes de rendimiento (previsión, 90 días al 2026-10-16)

- Mejor creativo histórico: "WhatsApp - Fin de Año 2026" (creative `29021759714084558`), $16.35 por conversación.
- Por ubicación: Historias de Facebook ~$11, Marketplace ~$17, Feed de Facebook ~$35, Reels de Facebook $43–139, Instagram casi sin conversiones. Priorizar Feed + Historias + Marketplace de FB; Reels e Instagram solo con creativo vertical propio.
- Por edad: 65+ es el segmento más barato (~$17); mujeres 35–54 el más caro ($53–59). Hombres más baratos que mujeres en todas las edades.
- La tasa clic→conversación de ~17–20% es la base histórica de la cuenta, no una falla nueva.
- Oportunidad cruzada: leads de créditos para pensionados/jubilados son prospectos naturales de previsión.

## Preferencias del cliente

- NO mencionar "Día de Muertos" en textos, títulos ni descripciones de anuncios.

## Propuestas de cierre por WhatsApp (formato estándar aprobado 2026-10-20)

Cuando el cliente comparta cotizaciones del "Cotizador GG" y pida una propuesta/presentación, usar SIEMPRE este formato (nivel ejecutivo).

Reglas de cálculo y contenido:
- El usuario manda dos capturas: la de promoción y la de PRECIO DE LISTA (normalmente condición `M036`, 36 M ENG. DIFERIDO). Todo ahorro se calcula contra el precio de lista, no contra el tachado del cotizador. Si los plazos difieren (p. ej. lista 36 vs promo 48), etiquetar cada mensualidad con su plazo y advertir al usuario que el tachado del sistema no coincide con la lista.
- Condición `D0xx` = pago con tarjeta de crédito, SIN enganche: solo se carga la primera mensualidad al formalizar.
- Condición `DD36` = 36 meses domiciliado a tarjeta de DÉBITO. `P001` = contado en una sola exhibición. Ya NO existe talonario. El enganche (15/20%) SÍ existe pero es OPCIONAL: no se requiere; solo se usa si el cliente decide ponerlo (baja la mensualidad). Presentar siempre "sin enganche requerido".
- Esencial Pro: débito máximo 36 meses; tarjeta de crédito hasta 48 meses.
- Además del texto, se puede entregar una imagen de propuesta (1080x1350) con logo Grupo Gayosso, opciones de pago en tarjetas, obsequio, vigencia, apartado y datos de Abraham (WhatsApp 81 1627 6206), con nota al pie de costos no incluidos. Es propuesta del asesor, NUNCA una imitación de captura del Cotizador.
- Flujo de cierre: tras el apartado, Gayosso envía al cliente un correo ("Asegura hoy la paz del mañana") con botón "Ver mi cotización"; el cliente la revisa y FIRMA ELECTRÓNICAMENTE (válido por contrato, cláusula de contratación por medios electrónicos). El WhatsApp puente es opcional (el usuario prefiere no usarlo por ahora); los datos del correo van en el paso 2 de la imagen de propuesta. El correo llega firmado por "ABRAHAM CUTIPA QUENAYA" desde asesor129381@asesoresgg.com (tutea al cliente, no trae WhatsApp ni fecha límite): en la imagen se indica remitente y asunto para que lo encuentre y no lo confunda con spam.
- Apartado: solo correo electrónico activo + INE → se genera folio de contratación que respeta precio y regalo hasta la fecha límite. "No implica pago ni compromiso hoy."
- Obsequio: Certificado Vacacional con valor de $24,999 POR CONTRATO (2 contratos = 2 certificados = $49,998).
- Promoción 2+1 con más de 3 servicios: se hacen contratos separados de 3 servicios cada uno; mostrar mensualidad por contrato y pago mensual total.
- Fecha límite actual de la promoción: 31 de octubre de 2026 (actualizar si cambia).
- Incluir: ahorro $ y %, mensualidad de lista vs promoción, equivalente diario, precio congelado, beneficio total (ahorro + $24,999).
- Categorías Gayosso: PREMIER PRO, UNIVERSAL PRO y ESENCIAL PRO. Las tres son AMBIVALENTES = el usuario elige al momento entre paquete de INHUMACIÓN o de CREMACIÓN. Solo PREMIER PRO es MULTIPLAZA (se redime en cualquier agencia Gayosso del país sin costo adicional); Universal y Esencial son LOCALES (cambiar de agencia cuesta ~20% del precio de contado del paquete en la nueva agencia).
- OJO: "Ambivalente" NO significa "lo usa quien lo necesite primero" (error en propuestas anteriores al 2026-10-23).
- No inventar coberturas, intereses ni datos que no estén en la cotización; al final listar al usuario los puntos a confirmar.
- Nunca mencionar "Día de Muertos". Formato WhatsApp (*negritas* con un asterisco, ~tachado~), dentro de bloque de código para copiar. Nombre del cliente como *[NOMBRE]* si no se da. Trato de "usted".
- Nunca pedir datos de tarjeta por WhatsApp.

Plantilla:

```
Estimado(a) *[NOMBRE]*, buen día.

Le saluda Abraham Cutipa, Asesor Certificado de Previsión Familiar de *Grupo Gayosso*. Conforme a lo que platicamos, le comparto la propuesta que mejor se ajusta a lo que busca: *[NECESIDAD DEL CLIENTE]*.

━━━━━━━━━━━━━━━
*PROPUESTA: [PRODUCTO]*
━━━━━━━━━━━━━━━

*¿Por qué [PRODUCTO]?*
[1–2 líneas de por qué encaja con la necesidad]

*Incluye:*
▪️ [concepto 1 de la cotización]
▪️ Paquete *Ambivalente*: al momento se elige inhumación o cremación
▪️ (Solo Premier Pro) Paquete *Multiplaza*: válido en cualquier agencia Gayosso del país
▪️ [...]

━━━━━━━━━━━━━━━
*INVERSIÓN*
━━━━━━━━━━━━━━━

Precio de lista: ~$[LISTA]~
*Precio con promoción: $[PROMO]*
✅ *Ahorro: $[AHORRO] ([%]%)*

*Plan de pagos: [N] mensualidades fijas con tarjeta de crédito, sin enganche*
Mensualidad de lista: ~$[MENS_LISTA]~
*Mensualidad con promoción: $[MENS_PROMO]*
✅ *$[DIF] menos cada mes[, en el mismo plazo]*

Equivale a *$[DIARIO] pesos diarios* para que su familia no tenga que tomar decisiones ni desembolsar en el momento más difícil.

🔒 *Precio congelado durante los [N] meses*, protegido de cualquier aumento futuro.

━━━━━━━━━━━━━━━
*BENEFICIO ADICIONAL*
━━━━━━━━━━━━━━━

🎁 *Certificado Vacacional de obsequio con valor de $24,999*

*Beneficio total a su favor:*
Ahorro vs. precio de lista: $[AHORRO]
Certificado vacacional: $24,999.00
*Total: $[AHORRO + 24,999]*

━━━━━━━━━━━━━━━
*VIGENCIA Y SIGUIENTE PASO*
━━━━━━━━━━━━━━━

⏰ Esta promoción tiene vigencia *únicamente hasta el [FECHA LÍMITE]*. Después aplica precio de lista.

Para reservarla a su nombre solo requiero:
1. *Correo electrónico* activo
2. *INE*

Con ello genero su *folio de contratación*, que le garantiza este precio y el certificado vacacional hasta el [FECHA LÍMITE]. *No implica pago ni compromiso hoy.*

Al formalizar, únicamente se carga la *primera mensualidad de $[MENS_PROMO]*.

¿Le parece bien si le genero su folio hoy mismo? Quedo a sus órdenes para cualquier duda. 🕊️

*Abraham Cutipa*
Asesor Certificado de Previsión Familiar
Grupo Gayosso · Monterrey
```

Variantes: con varias opciones (p. ej. mensualidades vs contado) usar bloques "OPCIÓN 1 / OPCIÓN 2" dentro de INVERSIÓN y cerrar con "¿Cuál opción le acomoda mejor?". Con paquete "2 + 1 de obsequio", agregar la línea "Paga menos de lo que cuestan solo [X] a precio de lista: [Y] le sale de obsequio".

## Propuesta vigente OCTUBRE 2026: Premier Pro 2+1 (válida solo hasta el 31-oct-2026)

Aprobada 2026-10-23. Precios de octubre: en NOVIEMBRE no reutilizar estas cifras; pedir al usuario capturas nuevas (promo + lista M036) y recalcular. Usar esta estructura como modelo para cualquier paquete 2+1.

Cifras (3 servicios Premier Pro, 1 contrato):
- Precio de lista M036: $246,900.03 ($82,300.01 por servicio; 2 a lista = $164,600.02). Mensualidad de lista 36 m: $6,863.82. (El tachado del cotizador dice $239,493.03: no usarlo.)
- Promoción: $159,670.00 → ahorro $87,230.03 (35.3%). Beneficio total con certificado: $112,229.03.
- Opción 1, débito DD36: $4,438.83/mes ($2,424.99 menos que la de lista, mismo plazo; < $50 diarios por persona). Cotizador: enganche Pr $4,438.83 + 35 mensualidades (suma $159,797.88, $127.88 sobre el total: no poner "total a pagar" en esa opción).
- Opción 2, tarjeta de crédito 48 m: $3,321.14/mes (de cotización TDC previa; confirmar con D048). "Menos de la mitad" de la mensualidad de lista; < $37 diarios por persona. Es la "MÁS ACCESIBLE".
- Incluye por servicio: Sala Premier, ataúd de lujo metal o madera cat. Premier, embalsamado y arreglo estético, cafetería básica, copia de acta de defunción, Ambivalente, Multiplaza.

Imagen (1080x1350, mismo diseño que la de Esencial Pro): encabezado logo + "PROPUESTA PERSONALIZADA"; banda verde "3 Servicios · Previsión Gayosso PREMIER PRO / Promoción 2 + 1 · el tercer servicio le sale de obsequio"; lista "Cada servicio incluye" + recuadro precio de lista tachado y precio con promoción; tres tarjetas: "1 · DÉBITO 36 MESES", "2 · T. CRÉDITO 48 MESES" (dorada, insignia "★ MÁS ACCESIBLE ★") y "PROMOCIÓN 2 + 1" ("3 por menos que 2", 2 a lista tachado vs. lo que paga por los 3); banda dorada del certificado de $24,999 (precio congelado · sin intereses si paga a tiempo · 5 días hábiles para cancelar); vigencia en rojo; 3 pasos (correo e INE → correo "Asegura hoy la paz del mañana" de ABRAHAM CUTIPA QUENAYA, clic en Ver mi cotización, revisar Spam → firma electrónica en < 5 min); pie con nombre y botón WhatsApp 81 1627 6206; letra pequeña de costos no incluidos.

Texto WhatsApp: plantilla estándar con estas variaciones: subtítulo "*Promoción 2 + 1*"; "¿Por qué Premier Pro?" = categoría más completa y única Multiplaza; en INVERSIÓN, línea 2+1 ("Paga menos de lo que cuestan solo 2 a precio de lista (~$164,600.02~): *el tercer servicio le sale de obsequio.*"), luego "OPCIÓN 1 · Débito a 36 meses" y "OPCIÓN 2 · Tarjeta de crédito a 48 meses ⭐ _la más accesible_"; "no se requiere enganche" en ambas; precio congelado + sin intereses; en el siguiente paso, mencionar el correo de ABRAHAM CUTIPA QUENAYA y la firma electrónica; cierre "¿Cuál opción le acomoda mejor?". Enviar primero la imagen y luego el texto.

## Propuesta vigente OCTUBRE 2026: Universal Pro 2+1 (válida solo hasta el 31-oct-2026)

Aprobada 2026-10-24. Mismas reglas que la de Premier Pro 2+1: en NOVIEMBRE no reutilizar cifras; pedir capturas nuevas (DD36, D048 y lista M036) y recalcular.

Cifras (3 servicios Universal Pro, 1 contrato; capturas del cotizador con fecha de precio 23/10/2026):
- Precio de lista M036: $186,900.03 ($62,300.01 por servicio; 2 a lista = $124,600.02). Mensualidad de lista 36 m: $5,195.82. (Tachado del cotizador $181,293.03: no usarlo.)
- Promoción (33.33% en cotizador): $120,868.06 → ahorro vs. lista $66,031.97 (35.3%). Beneficio total con certificado: $91,030.97.
- Opción 1, débito DD36: $3,360.13/mes ($1,835.69 menos que la de lista, mismo plazo; < $38 diarios por persona). Suma 36 pagos $120,964.68 (+$96.62).
- Opción 2, tarjeta de crédito D048: $2,514.06/mes ("menos de la mitad"; < $28 diarios por persona), "MÁS ACCESIBLE". Suma 48 pagos $120,674.88 (−$193.18). Por las diferencias, no poner "total a pagar" en las opciones.
- Incluye por servicio: Sala Estándar, ataúd metal o madera cat. Universal, embalsamado y arreglo estético, cafetería básica, Ambivalente. Multiplaza NO: en imagen y texto decir "Servicio en agencia Gayosso de su plaza" (no "local"); si preguntan, cambio de agencia ~20% del contado.

Imagen: mismo diseño que Premier 2+1, con banda "3 Servicios · Gayosso UNIVERSAL PRO" (título corto para que no se parta en dos líneas), tarjetas "1 · DÉBITO 36 MESES", "2 · T. CRÉDITO 48 MESES" (dorada, MÁS ACCESIBLE) y "PROMOCIÓN 2 + 1" ("3 por menos que 2"); diarios como "Menos de $X diarios c/u".

Texto WhatsApp: igual que Premier 2+1, cambiando "¿Por qué Universal Pro?" = punto de equilibrio de Gayosso: ataúd de metal o madera y servicio completo, con inversión muy por debajo de Premier; necesidad: "dejar protegidos a tres integrantes de su familia con un servicio completo, a una mensualidad cómoda"; en ambas opciones mostrar mensualidad de lista (36 meses) tachada.

## Propuesta vigente OCTUBRE 2026: Esencial Pro 1 servicio, enfoque VELACIÓN + CREMACIÓN (válida solo hasta el 31-oct-2026)

Aprobada 2026-10-27. En NOVIEMBRE no reutilizar cifras; pedir capturas nuevas (M036, P001, DD36, D036) y recalcular. Usar para clientes que buscan velación y cremación. Plazo máximo 36 meses (débito o crédito) o contado.

Cifras (1 servicio):
- Precio de lista M036: $48,300.00 (36 mensualidades de $1,342.74).
- Opción 1, contado P001: $30,912.00 → ahorro $17,388 (36%). Estrella "★ MAYOR AHORRO ★". DERIVADO de la cotización de 2 servicios (÷2): validar con captura P001 de 1 servicio.
- Opción 2, débito DD36: $1,041.97/mes ($300.77 menos que la de lista; < $35 diarios) → total $37,480.80, ahorro $10,819.20 (22.4%). DERIVADO (÷2): validar con captura DD36.
- Opción 3, tarjeta de crédito D036: $1,111.79/mes ($230.95 menos; < $38 diarios) → total $39,992.40, ahorro $8,307.60 (17.2%). De cotización real de 1 servicio.
- Beneficio total: contado $42,387.00; débito $35,818.20; crédito $33,306.60.
- Incluye: velación en Sala Estándar, ataúd metálico cat. Esencial, embalsamado y arreglo estético, cafetería básica, Ambivalente (al momento se elige cremación o inhumación), agencia Gayosso de su plaza, atención 24/7. NO poner urna (no viene en la cotización) hasta que el usuario confirme que el paquete de cremación la incluye.
- Argumento clave: "si el servicio termina en cremación, no tiene sentido invertir en un ataúd de lujo; Esencial Pro le da lo que necesita, sin pagar de más".
- Letra pequeña extra: "Si se elige cremación, Gayosso informa si el ataúd aplica o hay diferencia de precio" (cláusula del contrato).

Imagen: diseño base; banda "1 Servicio · Gayosso ESENCIAL PRO / Velación y cremación · un servicio digno, al precio justo"; "Su servicio incluye:" + recuadro lista tachado con "36 mensualidades de $1,342.74"; tres tarjetas: "1 · CONTADO" (dorada, MAYOR AHORRO), "2 · DÉBITO 36 MESES", "3 · T. CRÉDITO 36 MESES"; banda del certificado, vigencia, 3 pasos y pie.

Texto WhatsApp: plantilla estándar con título "*PROPUESTA: PREVISIÓN GAYOSSO ESENCIAL PRO* / *Velación + Cremación*"; necesidad "velación y cremación, con un servicio digno y al precio justo"; OPCIÓN 1 contado ⭐ _mayor ahorro_, OPCIÓN 2 débito y OPCIÓN 3 crédito, ambas con mensualidad de lista tachada y "menos cada mes, en el mismo plazo"; beneficio total en tres líneas; cierre "¿Cuál opción le acomoda mejor?". Si se confirma que débito es más barato que crédito: "con débito ahorra $70 más al mes".

## Propuesta vigente OCTUBRE 2026: Nicho para 2 urnas, Mausoleo Nogalar (válida solo hasta el 31-oct-2026)

Aprobada 2026-10-24. En NOVIEMBRE no reutilizar cifras; pedir capturas nuevas (M036, P001, D036) y recalcular. Usar como modelo para cualquier propuesta de nicho.

Cifras (producto 827302 "PAQ. NICHO CHICO ZONA MAUS PISO 5 NIV. SUP", Ambivalente NO, Multiplaza NO):
- Precio de lista M036: $32,000.00 (36 mensualidades de $889.60).
- Opción 1, contado P001: $25,600.00 → ahorro $6,400 (20%). Es la estrella ("★ MAYOR AHORRO ★"), al revés que en servicios: a meses el descuento es débil.
- Opción 2, tarjeta de crédito D036: $818.43/mes (36 pagos, enganche opcional; < $28 diarios) → total $29,440, ahorro $2,560 (8%). Suma 36 pagos $29,463.48 (+$23.48): no poner "total a pagar".
- Beneficio total: contado $31,399 (6,400 + 24,999); 36 meses $27,559. Gancho: el certificado de $24,999 "¡vale casi lo mismo que su nicho!".
- Incluye: construcción de nicho chico en mausoleo, espacio con capacidad para 2 urnas (dato del usuario, no viene en la cotización: confirmar), piso 5 nivel superior, ceremonia de depósito de cenizas, Mausoleo Nogalar. No mencionar Ambivalente ni Multiplaza.
- No incluido (cláusula Quinta): cuota de mantenimiento anual, apertura/cierre del nicho, grabado de placa, derechos y trámites. Va en letra pequeña de la imagen y en una nota en cursiva del texto ("se cubren por separado; con gusto le detallo los montos"). Si es nicho/capilla privada: 100% pagado para usarlo.

Imagen: mismo diseño base; banda "Nicho para 2 urnas · Mausoleo Nogalar / Un espacio propio y digno para el descanso de su familia"; "Su nicho incluye:" + recuadro de lista tachado con "36 mensualidades de $889.60"; DOS tarjetas grandes: "1 · CONTADO" (dorada, MAYOR AHORRO) y "2 · T. CRÉDITO 36 MESES"; banda dorada del certificado con "¡Vale casi lo mismo que su nicho!"; mismos 3 pasos, vigencia y pie.

Texto WhatsApp: plantilla estándar; necesidad "asegurar un lugar propio y digno para el descanso de su familia"; título "*PROPUESTA: NICHO PARA 2 URNAS* / *Mausoleo Nogalar*"; "¿Por qué un nicho en Mausoleo Nogalar?" = espacio propio, cuidado y permanente donde reunirse y recordar, sin buscar ni pagar un lugar en el momento más difícil; OPCIÓN 1 contado ⭐ _mayor ahorro_, OPCIÓN 2 TDC 36 con mensualidad de lista tachada; beneficio total en dos líneas (contado / 36 meses); nota de costos no incluidos antes del cierre "¿Cuál opción le acomoda mejor?".

## Respuesta a leads que SOLICITAN INFORMACIÓN (Meta → WhatsApp), aprobado 2026-10-24

Para prospectos que llegan del anuncio y piden informes NO usar el texto largo de cierre: van 3 mensajes cortos. La imagen de propuesta se envía con el Mensaje 1 como pie. Las cifras son las de octubre 2026 (vigentes al 31-oct); en noviembre se actualizan con capturas nuevas.

Mensaje 1 (pie de la imagen), estructura:
```
¡Hola! Muchas gracias por su interés. Le saluda Abraham Cutipa, Asesor Certificado de Previsión Familiar de *Grupo Gayosso* en Monterrey. 🕊️

Le comparto el detalle de la *[PROMOCIÓN] en Previsión Gayosso [CATEGORÍA]*: protege a *[N] integrantes de su familia* [y paga menos de lo que cuestan solo 2 a precio de lista. *El tercer servicio le sale de obsequio.*]

✅ *Ahorro de $[AHORRO]* contra precio de lista
💳 Desde *$[MENS_TDC48] al mes* por los [N] servicios (tarjeta de crédito, 48 meses) o *$[MENS_DD36]* (débito, 36 meses)
🚫 *Sin enganche requerido*
🔒 *Precio congelado* y sin intereses pagando a tiempo
🎁 *Certificado Vacacional de obsequio* con valor de $24,999
[línea diferenciadora de la categoría]

⏰ Vigente *solo hasta el 31 de octubre*.

Para orientarle mejor: *¿a quiénes le gustaría proteger?* (por ejemplo usted, su pareja, sus papás)
```

Variantes del Mensaje 1:
- Premier Pro 2+1: ahorro $87,230; $3,321.14 TDC 48 / $4,438.83 débito 36; línea "📍 *Multiplaza:* válido en cualquier agencia Gayosso del país".
- Universal Pro 2+1: ahorro $66,031 (redondeado); $2,514.06 TDC 48 / $3,360.13 débito 36; línea "⚱️ Ataúd de *metal o madera* y paquete *Ambivalente*: al momento se elige inhumación o cremación". NO mencionar Multiplaza (no la tiene).
- Esencial Pro 2 servicios (sin 2+1): "*Promoción de octubre*", "protege a *2 integrantes de su familia* con un servicio funerario completo y el respaldo de Gayosso, por menos de lo que imagina"; $1,559.20 TDC 48 / $2,083.93 débito 36 (siempre "por los 2 servicios"); línea extra "💵 De contado: *$61,824*, con *ahorro de $34,776 (36%)* contra precio de lista"; línea "⚱️ *Ambivalente:* al momento se elige inhumación o cremación"; ejemplo de pregunta "(por ejemplo usted y su pareja, o sus papás)".

Mensaje 2 (cuando responde con interés):
```
Excelente. Para apartarle la promoción a su nombre solo necesito:

1. *Correo electrónico* activo
2. *INE*

Con eso genero su *folio de contratación*, que le respeta el precio y el certificado vacacional hasta el 31 de octubre. *No implica pago ni compromiso hoy.*

Le llegará un correo de *ABRAHAM CUTIPA QUENAYA* con el asunto *"Asegura hoy la paz del mañana"*. Ahí revisa su cotización y firma desde su celular en menos de 5 minutos. Al formalizar solo se carga la *primera mensualidad*.

¿Me comparte su correo para generar su folio hoy mismo?
```

Mensaje 3 (sin respuesta en 24 h):
```
Buen día, solo para confirmar que recibió la información de [la Promoción 2 + 1 en CATEGORÍA / Previsión Esencial Pro]. Le recuerdo que vence el *31 de octubre* y después aplica precio de lista. ¿Tiene alguna duda que le pueda resolver? 🕊️
```

Uso de la pregunta "¿a quiénes le gustaría proteger?" (calificación): 1–2 personas → Esencial Pro o servicio individual; 3 → paquete 2+1; 6 o más → 2 contratos 2+1. Escalamientos: Esencial con 3 personas → Universal 2+1 (~$955/mes más a 48 m, un servicio más y mejor categoría); Universal que pregunta por otras ciudades → Premier 2+1 (~$807/mes más a 48 m, Multiplaza y Sala Premier). Nunca pedir datos de tarjeta en estos mensajes.

## Comparativo PREMIER vs UNIVERSAL (cliente que vio Premier y pide Universal), aprobado 2026-10-28

Cuando el cliente ya recibió Premier Pro 2+1 y pide ver Universal: NO presentar Universal como propuesta nueva desde cero; presentarla comparada con Premier para que la decisión sea "cuál de las dos" y no "compro o no". Cifras de octubre 2026 (en noviembre actualizar).

Mensaje 1 (pie de la imagen de Universal Pro 2+1):
```
Con gusto, *[NOMBRE]*. Le comparto la propuesta en *Previsión Gayosso Universal Pro*, con la misma *Promoción 2 + 1*: protege a *3 integrantes de su familia* y *el tercer servicio le sale de obsequio*. 🕊️

✅ *Ahorro de $66,031* contra precio de lista
💳 *$2,514.06 al mes* por los 3 servicios (tarjeta de crédito, 48 meses)
💳 *$3,360.13 al mes* por los 3 servicios (débito, 36 meses)
👨‍👩‍👧 *Menos de $28 diarios por persona*
🚫 Sin enganche requerido
🔒 Precio congelado y sin intereses pagando a tiempo
🎁 *Certificado Vacacional de $24,999* de obsequio
```

Mensaje 2 (comparación, justo después):
```
Para que pueda decidir con toda claridad, así se comparan las dos opciones:

*✅ LO QUE SE MANTIENE IGUAL*
▪️ 3 servicios, el tercero de obsequio
▪️ Embalsamado, arreglo estético y cafetería
▪️ *Ambivalente:* al momento se elige inhumación o cremación
▪️ Certificado Vacacional de $24,999
▪️ Precio congelado, sin enganche y atención 24/7

*🔄 LO QUE CAMBIA*
▪️ *Sala:* Premier ➝ Estándar
▪️ *Ataúd:* de lujo categoría Premier ➝ metal o madera categoría Universal
▪️ *Cobertura:* Premier es válido en *cualquier agencia Gayosso del país*; Universal, en la agencia de su plaza

*💰 LA DIFERENCIA*
Premier Pro: $3,321.14 al mes
Universal Pro: $2,514.06 al mes
➡️ *$807 menos al mes con Universal*

Si su familia vive en Monterrey y no le preocupa el traslado a otra ciudad, *Universal Pro le da un servicio completo y digno pagando menos*. Si alguno vive o viaja fuera, *Premier le da esa tranquilidad*.

⏰ Ambas terminan el *sábado 31 de octubre*.

*¿Con cuál de las dos se siente más tranquilo(a)?*
```

Mensaje de cierre (cuando elige cualquiera): pedir correo electrónico + foto de INE (frente y reverso), folio de contratación sin pago ni compromiso, correo de ABRAHAM CUTIPA QUENAYA "Asegura hoy la paz del mañana" para firmar desde el celular; "¿Me los comparte para dejarlo listo?".

Criterio de decisión que se le da al cliente: familia en Monterrey → Universal; alguien vive o viaja fuera → Premier (Multiplaza). Si pregunta "¿cuál me recomienda?": responder con su propio dato ("Si toda su familia está aquí, Universal: servicio completo y ahorra más de $9,600 al año. Si alguien está fuera, Premier."). Dejarle elegir con criterio reduce cancelaciones en los 5 días hábiles. Para el caso inverso (vio Universal y pregunta por más), usar la misma estructura invirtiendo el sentido: "$807 más al mes" por Sala Premier, ataúd de lujo y Multiplaza.

## Contrato Gayosso (Contrato de prestación de servicios funerarios a futuro, PROFECO 3692-2022) — argumentos verificados

Usar en presentaciones solo lo que está aquí (fuente: contrato de adhesión, págs. 3–8):
- *Sin intereses*: el monto total ya contempla todo; no hay gasto, interés ni cargo adicional si paga a tiempo. (Atraso: interés moratorio 3% mensual; >90 días puede rescindirse.)
- *Precio congelado*: los montos no pueden modificarse sin consentimiento escrito del cliente.
- *Garantía de cancelación*: 5 días hábiles tras la firma para cancelar con devolución íntegra. Después aplica pena convencional de 48% de lo pagado.
- *Beneficio por fallecimiento del titular (quita)*: si el titular fallece antes de terminar de pagar, Gayosso condona el saldo de UN servicio para el propio titular, si: va al corriente, pagó ≥25% del contrato, pasaron ≥90 días desde la firma y tenía 18–60 años al firmar. Una sola vez, intransferible.
- *Titular sustituto*, beneficiarios y usuarios designables y modificables en cualquier momento.
- *Cesión*: puede ceder el contrato a otra persona pagando 10% del precio vigente.
- *Pagos anticipados* sin penalización.
- *Servicio 24/7, 365 días*, tel. 800-716-1616. Si la agencia no tiene disponibilidad, se presta en otra agencia de igual o superior categoría sin costo.
- *% mínimo pagado para usar un servicio antes de liquidar*: servicio individual 100%; dúplex 50% / 100%; triplex/cuádruplex/paquetes integrales 50% / 75% / 100% (1er/2do/3er uso); capillas y jardines privados 100%. El saldo restante se liquida al usarlo. Mencionarlo con honestidad si preguntan.
- *NO incluido* (cláusula Quinta): derechos de inhumación ante autoridad, apertura/cierre de fosas y nichos, grabado de lápida, cuota de mantenimiento anual (fosas/nichos), gestión de actas de defunción y derechos gubernamentales.
- Cremación: si se elige cremar, Gayosso informa si el ataúd sirve para cremación o si hay ataúdes especiales; puede haber diferencia de precio.
- Pago domiciliado a tarjeta de crédito o pagaré como garantía de mensualidades.
- No guardar en este repo (es público) nombres, firmas ni datos de clientes que aparezcan en contratos.

## Operación

- Editar un conjunto o campaña activa por MCP lo pausa automáticamente: reactivar campaña y conjunto después de cada edición.
- Tras cambiar segmentación, no volver a tocar el conjunto en 5–7 días (fase de aprendizaje).
- Números extranjeros de spam (+234, +92, +91, +62, etc.): no responder, bloquear y reportar en WhatsApp.

## Historial

- 2026-10-07 00:15 UTC: corregida la segmentación del conjunto "Previsión Familiar - Cierre WhatsApp - SEP 2026" (`120255806431370768`); campaña `120255806054890768` con fin programado 2026-10-08 00:15 UTC (18:15 hora de Monterrey del 7-oct).
- 2026-10-16: creadas en pausa la campaña FRÍA `120257101274550768` ($200/día, conjunto `120257101281740768`, anuncio `120257101286310768`) y la CALIENTE `120257101274740768` ($60/día, conjunto `120257101283010768`, anuncios `120257101286860768` y `120257101287530768`). Solo ubicaciones de Facebook: Estados de WhatsApp exige incluir Historias de Instagram. Al publicarlas hay que pausar Tranquilidad `120257021195410768`.
- 2026-10-16: nuevos creativos. FRÍA: anuncio "Vaquita Padre Regio" `120257101817340768` (creative `1410500244484937`) compite con Fin de Año. CALIENTE: anuncio "Promo 2+1" `120257101836590768` (creative `1410506920708085`; el anterior `120257101819650768` quedó archivado); la campaña CALIENTE termina 2026-11-01 05:59 UTC (fin de la promo del 31-oct). En la caliente NO activar los anuncios con imágenes repetidas (`120257101286860768`, `120257101287530768`). Imágenes subidas desde Business Suite dan "Image Not Found" por API; deben subirse desde el Administrador de anuncios.
- 2026-10-16: PUBLICADAS. FRÍA activa ($200/día) con Fin de Año + Vaquita; CALIENTE activa ($60/día) solo con Promo 2+1 (termina sola el 31-oct 23:59 Monterrey). Tranquilidad `120257021195410768` en pausa. Pendiente: después del 31-oct, la caliente necesita un creativo nuevo sin promoción. Revisar resultados a los 3–4 días (~20-oct).
- 2026-10-20 (revisión lunes): el 17-oct Meta puso los 3 anuncios en "Update Required" (issue code 2446955); entrega detenida ~17–19 oct hasta reactivarse el 19-oct 11:10. Cuenta en "In grace period" desde el 19-oct 20:15 (pago pendiente). Resultados 16–20 oct: Fin de Año $61.93 / 3 conv ($20.64); Vaquita $393.24 / 10 conv ($39.32); Promo 2+1 caliente $162.67 / 3 conv ($54.22), frecuencia 2.2 con alcance 456. Casi todo el gasto fue a Feed.
