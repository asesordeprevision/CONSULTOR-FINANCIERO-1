# Consultor Financiero — memoria de campañas Meta Ads

Cuenta publicitaria principal: `789501147519125` (negocio "Abraham Cutipa - Asesor Financiero", MXN).
La cuenta `1779143873445450` ("Consultor Financiero" / Previsión Familiar) aún no está habilitada para Ads MCP.
Mercado: previsión funeraria / previsión familiar en Nuevo León (Monterrey y área metropolitana).

## Alcance de este proyecto (regla del usuario 2026-11-10)

Aquí SOLO se trabaja Previsión Gayosso (campaña CALIENTE `120257101274740768` y futuras de previsión/propiedad). Las campañas de créditos IMSS Ley 73 y "Primeras Ventas por WhatsApp con Fotos" (`120257509932420768`) se manejan en otro lado: no reportarlas ni proponer cambios sobre ellas aquí.

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
- VERIFICACIÓN DE SEDE (obligatoria en CADA cotización que comparta el usuario, regla 2026-11-06): cruzar la oficina ("Oficina PR") y las claves de producto con la tabla de claves. NOGALAR = oficinas [FCN1] Fun. Cap. Nogalar / [MIN1] Maus. Nogalar; servicios Esencial 827291, Universal 827292, Premier 827294; nichos 8273xx (Maus. Nogalar). CAPILLAS MARIANAS = oficinas [GCM8] Funeraria Capillas Marianas / [MC26] Mausoleo Capilla Marianas; servicios Esencial 826882, Universal 826885, Premier 826890; nichos 82xxxx de GG34. Según el resultado: poner en imagen y texto la sede y dirección correctas (Nogalar: Av. Nogalar Sur 420 A, San Nicolás de los Garza; Marianas: Av. Lázaro Cárdenas 1005 Pte., Loma Larga, San Pedro); aplicar la oferta Buen Fin de nichos SOLO si es Nogalar; y avisar al usuario al inicio de la respuesta ("Cotización de NOGALAR/CAPILLAS MARIANAS (oficina X, clave Y)"). Si hay claves mezcladas (servicio de una sede y nicho de otra) o la oficina no coincide con la clave, señalarlo antes de armar la propuesta.
- El usuario manda dos capturas: la de promoción y la de PRECIO DE LISTA (normalmente condición `M036`, 36 M ENG. DIFERIDO). Todo ahorro se calcula contra el precio de lista, no contra el tachado del cotizador. Si los plazos difieren (p. ej. lista 36 vs promo 48), etiquetar cada mensualidad con su plazo y advertir al usuario que el tachado del sistema no coincide con la lista.
- Condición `D0xx` = pago con tarjeta de crédito, SIN enganche: solo se carga la primera mensualidad al formalizar.
- Condición `DD36` = 36 meses domiciliado a tarjeta de DÉBITO. `P001` = contado en una sola exhibición. Ya NO existe talonario. El enganche (15/20%) SÍ existe pero es OPCIONAL: no se requiere; solo se usa si el cliente decide ponerlo (baja la mensualidad). Presentar siempre "sin enganche requerido".
- Esencial Pro: débito máximo 36 meses; tarjeta de crédito hasta 48 meses.
- Además del texto, se puede entregar una imagen de propuesta (1080x1350) con logo Grupo Gayosso, opciones de pago en tarjetas, obsequio, vigencia, apartado y datos de Abraham (WhatsApp 81 1627 6206), con nota al pie de costos no incluidos. Es propuesta del asesor, NUNCA una imitación de captura del Cotizador.
- Flujo de cierre: tras el apartado, Gayosso envía al cliente un correo ("Asegura hoy la paz del mañana") con botón "Ver mi cotización"; el cliente la revisa y FIRMA ELECTRÓNICAMENTE (válido por contrato, cláusula de contratación por medios electrónicos). El WhatsApp puente es opcional (el usuario prefiere no usarlo por ahora); los datos del correo van en el paso 2 de la imagen de propuesta. El correo llega firmado por "ABRAHAM CUTIPA QUENAYA" desde asesor129381@asesoresgg.com (tutea al cliente, no trae WhatsApp ni fecha límite): en la imagen se indica remitente y asunto para que lo encuentre y no lo confunda con spam.
- Apartado: solo correo electrónico activo + INE → se genera folio de contratación que respeta precio y regalo hasta la fecha límite. "No implica pago ni compromiso hoy."
- Obsequio: Certificado Vacacional POR CONTRATO (2 contratos = 2 certificados). Validado 2026-11-03 en la liga oficial del convenio (https://que-es.royal-holiday.com/gayosso/): es de *Royal Holiday*, 4 días / 3 noches TODO INCLUIDO, 2 adultos + 2 menores (hasta 6 años), seguro de asistencia de viaje; destinos Cozumel, Puerto Vallarta, Cancún, Acapulco, Ixtapa y Huatulco. *Tarifa regular $24,995* (usar esta cifra, no $24,999). NO es gratis: cuota de reservación desde $3,999 (Park Royal Beach Acapulco, Cancún, Huatulco, Ixtapa) y desde $8,499 (Grand Park Royal Cozumel y Puerto Vallarta). Requisitos: solo titular del contrato Gayosso; pareja/cónyuges de 30 a 60 años con ingreso mensual mancomunado mínimo de $50,000 (si no cumple, cobran tarifa regular); una vez por familia; no aplica a socios Royal Holiday ni a quien ya usó otra promoción RH; ID oficial + tarjeta de crédito al registrarse; reservar dentro de 3 meses y viajar dentro de 6 meses desde la entrega; reservaciones hasta el 31-dic-2026; sin reembolso; reservas al 800 711 1515. Escasez real: "válido para las primeras reservaciones disponibles" / sujeto a disponibilidad. En imágenes y textos mencionar siempre la cuota de reservación "desde $3,999" para no presentarlo como gratis.
- Promoción 2+1 con más de 3 servicios: se hacen contratos separados de 3 servicios cada uno; mostrar mensualidad por contrato y pago mensual total.
- Fecha límite actual de la promoción: *30 de noviembre de 2026* (anuncio oficial Gayosso visto 2026-11-01: "Hasta el 30 de noviembre: 2 servicios + 1 sin costo adicional, además de un certificado"). Las cifras de octubre guardadas abajo se usan solo hasta confirmar con capturas nuevas del Cotizador que no cambiaron; confirmar también que el certificado vacacional sigue siendo de $24,999.
- Incluir: ahorro $ y %, mensualidad de lista vs promoción, equivalente diario, precio congelado, beneficio total (ahorro + $24,999).
- Categorías Gayosso: PREMIER PRO, UNIVERSAL PRO y ESENCIAL PRO. Las tres son AMBIVALENTES = el usuario elige al momento entre paquete de INHUMACIÓN o de CREMACIÓN. Solo PREMIER PRO es MULTIPLAZA (se redime en cualquier agencia Gayosso del país sin costo adicional); Universal y Esencial son LOCALES (cambiar de agencia cuesta ~20% del precio de contado del paquete en la nueva agencia).
- OJO: "Ambivalente" NO significa "lo usa quien lo necesite primero" (error en propuestas anteriores al 2026-10-23).
- No inventar coberturas, intereses ni datos que no estén en la cotización; al final listar al usuario los puntos a confirmar.
- Nunca mencionar "Día de Muertos". Formato WhatsApp (*negritas* con un asterisco, ~tachado~), dentro de bloque de código para copiar. Si NO se conoce el nombre del cliente, NO usar [NOMBRE] ni "Estimado(a)": abrir con "¡Hola, buen día! 🕊️" y cerrar pidiendo el nombre ("¿Me comparte su nombre para generar su folio a su nombre?"); texto listo para enviar sin editar. Trato de "usted".
- Nunca pedir datos de tarjeta por WhatsApp.
- Liga de validación de asesor (página "Identidad Validada" de Grupo Gayosso, con foto, zona Monterrey y correo de reporte asesoresgayosso@gayosso.com): https://gayossocatrinas.com/951848-2/ . Incluirla en TODOS los textos de propuesta, cierre y solicitud de información, antes de la pregunta de cierre: "✅ Puede validar mi registro como asesor oficial aquí: 👉 [liga]". En el mensaje donde se piden correo e INE, repetirla ("Antes de compartirme su INE, puede validar que soy asesor oficial aquí"). La página muestra el nombre como "CUITPA" (error de captura de Gayosso): si el cliente pregunta, es la misma persona.
- Cliente que quiere SOLO servicio funerario (inhumación, sin cremación): presentar "🎁 DE OBSEQUIO: PLAN AMBIVALENTE · 2 EN 1" = contrata inhumación y sin pagar más se lleva la opción de cremación (urna de madera + ataúd de presentación); "2 opciones al precio de 1". Usar "2 en 1", NUNCA "2x1" (sugiere dos servicios). Letra pequeña: si se elige cremación, Gayosso informa si el ataúd aplica o hay diferencia de precio. Modelo aprobado 2026-11-03 con Esencial Pro 1 servicio (lista $48,300; TDC 36 $1,111.79; enganche 15% $5,542.43 + $897.87; enganche 20% $7,389.90 + $842.45; precio con enganche $36,949.50).

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

## Propuesta vigente OCTUBRE 2026: 2 Esencial Pro + Nicho de obsequio (válida solo hasta el 31-oct-2026)

Aprobada 2026-10-28. En NOVIEMBRE no reutilizar cifras; pedir capturas nuevas (M036, D036, D048 del paquete) y recalcular. Promoción del cotizador "2 PREVISION GAYOSSO ESENCIAL PRO + PAQ. NICHO CHICO ZONA MAUS PISO 5 NIV. SUP" (25%). Modelo para cualquier "servicios + nicho de obsequio" (existe también la versión 2 Premier Pro + nicho: lista $196,600.02, promo $143,026.52, TDC 48 $2,974.95/mes, ahorro $53,573.50 (27.2%), nicho gratis + $21,573.50; beneficio total $78,572.50; confirmar precios vigentes).

Cifras (1 cotización; tomada como 1 contrato = 1 certificado, confirmar si Gayosso lo formaliza separado → serían 2 certificados $49,998):
- Precio de lista M036: 2 Esencial $96,600 + nicho $32,000 = $128,600.00; mensualidad de lista 36 m $3,575.08.
- Opción 1, TDC D036: $88,734.00, $2,466.81/mes ($1,108.27 menos, mismo plazo; < $83 diarios por todo) → ahorro $39,866 (31%). Suma 36 pagos $88,805.16 (+$71.16).
- Opción 2, TDC D048: $93,556.50, $1,945.98/mes (< $65 diarios por todo), "MÁS ACCESIBLE" → ahorro $35,043.50 (27.2%). Suma 48 pagos $93,407.04 (−$149.46). No poner "total a pagar"; usar "precio con promoción".
- Gancho: paga menos que solo los 2 Esencial a lista ($96,600) → "el nicho le sale de obsequio" (a 36 m además ahorra $7,866).
- Beneficio total: 36 m $64,865.00; 48 m $60,042.50.
- Incluye: por servicio velación en Sala Estándar, ataúd metálico cat. Esencial, embalsamado y arreglo estético, cafetería, Ambivalente (cremación o inhumación); nicho: construcción y espacio en nicho piso 5 nivel superior, ceremonia de depósito de cenizas. Urna NO (confirmar si el paquete de cremación la incluye).
- Letra pequeña: cremación/ataúd (Gayosso informa si aplica o hay diferencia), no incluye mantenimiento anual, apertura/cierre del nicho, grabado de placa, derechos y trámites.

Imagen: banda "2 Servicios ESENCIAL PRO + Nicho / Servicio y lugar de descanso en un solo plan · ¡el nicho de obsequio!"; dos bloques de incluye (servicio y nicho); recuadro de lista con desglose tachado (2 Esencial / Nicho / total) y "36 mensualidades de $3,575.08"; tarjetas "1 · T. CRÉDITO 36 MESES", "2 · T. CRÉDITO 48 MESES" (dorada, MÁS ACCESIBLE) y "NICHO DE OBSEQUIO" ("Paga menos que solo los 2 servicios", 2 a lista tachado vs. "usted paga por todo desde $88,734", "¡Nicho gratis!"); certificado, vigencia, 3 pasos y pie. Versión Premier: una tarjeta TDC 48 (dorada, "★ TODO EN UN SOLO PLAN ★") + tarjeta NICHO DE OBSEQUIO.

Texto WhatsApp: plantilla estándar; necesidad "dejar resuelto todo para dos integrantes de su familia: la velación, la cremación y el lugar de descanso"; título "*PROPUESTA: 2 PREVISIÓN GAYOSSO ESENCIAL PRO* / *+ NICHO DE OBSEQUIO en Mausoleo Nogalar*"; "¿Por qué esta propuesta?" = resuelve en un solo plan el servicio completo y el lugar donde descansarán las cenizas; INVERSIÓN con desglose de lista (2 servicios, nicho, total, mensualidad de lista), línea de nicho de obsequio, OPCIÓN 1 TDC 36 y OPCIÓN 2 TDC 48 ⭐ _la más accesible_ (precio con promoción, mensualidad, ahorro, diario); beneficio total en dos líneas; nota de costos no incluidos; cierre "¿Cuál opción le acomoda mejor?".

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

## Qué incluye / no incluye (tabla oficial Protección Familiar Gayosso, Agencia A Monterrey) y salas en los formatos

Usar SIEMPRE en imágenes y textos de propuesta (columna lateral "¿Qué incluye? / ¿Qué NO incluye?" aprobada 2026-10-28):
- Las 3 categorías incluyen: asesoría en trámites; traslado a la funeraria y al cementerio/panteón/crematorio (área conurbada); embalsamamiento; arreglo estético básico (aseo, vestido, maquillaje); cafetería básica; ataúd para inhumación; URNA para cremación; ataúd de uso para presentación (velación si elige cremación); Ambivalente; 100% transferible (usuarios designables sin costo; ceder el contrato completo cuesta 10%).
- Premier Pro: ataúd de lujo metal o madera cat. Premier; urna de lujo madera cat. Premier; ataúd de lujo de presentación; *Sala de velación Premier 24 h, 60 personas sentadas*; Multiplaza (agencias del mismo tipo o inferior, no superior); 1 copia del acta de defunción PLUS.
- Universal Pro: ataúd metal o madera cat. Universal; urna de madera cat. Universal; *Sala de velación Estándar 24 h, 40 personas sentadas*. Sin Multiplaza ni acta.
- Esencial Pro: ataúd de metal cat. Esencial; urna de madera (la tabla dice "de lujo cat. Premiere", probable error: poner solo "urna de madera"); *Sala de velación Estándar 24 h, 20 personas sentadas*. Sin Multiplaza ni acta.
- NO incluye (las 3): recuperación en hospitales/instituciones; trámites (certificado médico, CODE); apostillados y embajada; traslados foráneos; embalsamamiento clínico; sacerdote y oficios religiosos; oratorio; esquela y flores; transporte de acompañantes; traslados foráneos a destino final; derechos de inhumación; gestión del acta de defunción; maniobras de nicho y de destape.
- No poner en las imágenes el teléfono 800 de Gayosso ni "atención 24/7" como recuadro (pedido del usuario 2026-10-28).
- Salas en los formatos (Capillas Marianas): en propuestas Premier escribir "Sala Premier 24 h para 60 personas · salas Premier y Magna (5º piso), Lourdes y Fátima (4º piso) en Capillas Marianas". En Universal/Esencial escribir la capacidad (40 / 20 personas) y NO nombrar sala hasta que el usuario confirme cuáles de Mausoleo A, Mausoleo B, Esperanza y Piedad corresponden a cada categoría.

## Direcciones Gayosso Monterrey y cobertura nacional (usar en propuestas cuando se requiera)

- *Capillas Marianas* (agencia GCM8, Agencia A): Av. Lázaro Cárdenas No. 1005 Pte., Col. Loma Larga, San Pedro Garza García, N.L. (la presentación oficial de Gayosso usa C.P. 64710; antes teníamos 66220: usar 64710).
- *Capillas Marianas Nogalar* ("Marianas Nogalar", nueva casa funeraria, APERTURA DICIEMBRE 2026; ya se puede visitar con el asesor). Dirección OFICIAL (presentación Gayosso 2026-11-06): *Av. Nogalar Sur 420 A, San Nicolás de los Garza, C.P. 66484, N.L.* (antes usábamos "#440, entre Futuro Nogalar y Privada San Francisco": corregir a 420 A). Argumento en visitas: conocer las dos instalaciones (Capillas Marianas y la nueva Nogalar).
- *Cementerio Jardines del Descanso* (oficina CJ04): Calle de la Meza No. 7650, Col. La Estanzuela, C.P. 64988, Monterrey, N.L. Tel. (81) 8317 8505, abierto todos los días de 5:00 a 18:00.
- *Oficinas administrativas*: Aramberri No. 1115 Ote., esq. Diego de Montemayor, Col. Centro, Monterrey, N.L. Tel. (81) 8173 5469. L–V 9:00–13:00 y 15:00–18:00; sábados 9:00–13:00.
- *Oficinas telemarketing*: Hidalgo #1911, Col. Obispado, entre Verlaine y Baudelaire.
- *Reportar fallecimiento*: *247 (línea de emergencia funeraria, consejeros 24 h). Documentos para solicitar el servicio: contrato; certificado médico de defunción; identificación oficial vigente del fallecido (INE, pasaporte o cédula); acta de nacimiento; acta de matrimonio. (Usar en mensajes post-venta/bienvenida, no en las imágenes de propuesta.)
- *Cobertura nacional Gayosso*: 13 estados, 24 agencias, 23 cementerios, 17 mausoleos (Baja California, Durango, Coahuila, Nuevo León, Tamaulipas, Aguascalientes, Guanajuato, Guadalajara/Jalisco, Estado de México, Michoacán, Guerrero, CDMX, Morelos). Nuevo León: 2 agencias, 1 cementerio, 1 mausoleo.
- *Premier Pro Multiplaza*: el servicio se redime en las agencias Gayosso de todo México donde hay Gayosso (24 agencias en 13 estados). Argumento: "válido en las 24 agencias Gayosso de 13 estados". Universal y Esencial: solo su plaza.

## Capillas Marianas — salas

- Salas PREMIER PRO (Sala Premier, 60 personas): *Premier* (5º piso), *Magna* (5º piso), *Lourdes* (4º piso), *Fátima* (4º piso).
- Otras salas: *Mausoleo A*, *Mausoleo B*, *Esperanza* y *Piedad* (pendiente confirmar cuáles son Universal, 40 personas, y cuáles Esencial, 20 personas).
- Uso: en citas presenciales y recorridos de cierre nombrar la sala ("le muestro la sala Magna, en el 5º piso, donde estaría su familia"). Para clientes Premier, recorrer 5º/4º piso; no prometer salas Premier a clientes Universal/Esencial.

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

## Argumentos oficiales de gayosso.com (extraídos 2026-11-10; usar en textos e imágenes de confianza)

- *Contigo desde 1875*: 150 años; fundada por Eusebio Gayosso tras perder a su madre, para simplificar trámites y acompañar a las familias. Primera agencia en el Hotel Gillow (CDMX).
- *Más de 2 millones de mexicanos confían en Gayosso*; más de 830 mil familias acompañadas.
- *La única funeraria con servicio integral*: previsión, capillas, mausoleos y cementerios propios.
- Presencia nacional (sitio web): 24 agencias, 23 cementerios y 21 mausoleos (la presentación local decía 17 mausoleos: usar 21).
- Calidad: ISO 9001 y norma UNE de servicios funerarios; NPS certificado por tercero.
- Planes funerarios: "Planifica y ahorra · 100% transferible · Inhumación o cremación · Plan personalizado". Atención inmediata 24/7.
- Agencias: cafetería, florería, capilla ecuménica, crematorio, nichos, estacionamiento, wifi, valet parking, accesibilidad, elevador.
- *Gayosso MED*: telemedicina y segunda opinión médica; descuentos de 5% a 25% en medicamentos y farmacias; 1 servicio de ambulancia al año; cuestionario de salud. (Se regala en la preventa Nogalar, "aplican restricciones".)
- *Gayosso Contigo*: plan de lealtad para clientes, descuentos con +1,500 aliados, app iOS/Android (gayossocontigo.com).
- Otros: servicio internacional (traslados, acta apostillada), Rest In Cloud (obituario digital, mural conmemorativo), Pet Love Story (mascotas), florería en línea, asistencia emocional (guías de duelo).
- Testimonios públicos: "Nunca me esperé el gran servicio que nos ofrecieron" (Familia Ávila); "Empresa muy atenta y con personal muy cálido y humano" (Familia Baltazar).
- Imagen de confianza: propuesta/por_que_gayosso.html (render nocturno de Nogalar).

## Catálogo de propiedades Gayosso 2025 (Drive: CATÁLOGO_PROPIEDADES_25.pdf, leído 2026-11-10)

Todas: uso perpetuo, cuota anual de mantenimiento y/o conservación, inventario varía por plaza, imágenes ilustrativas. Medidas interiores aproximadas:
- Cementerio: *Nicho exterior* 30×60×30 cm, mármol (chico 2 urnas, grande 4, familiar 6). *Lote tipo americano* 0.93×2.30×0.76 m, lápida y florero, 2 o 4 gavetas. *Gaveta mural* 0.90×2.50×0.80 m, tapa de mármol, 1 gaveta (doble: 2, altura 1.60 m; triple: 3; *obispal*: 1, 2.50 m de frente). *Ciprés ecológico* 30×40×35 cm con árbol ciprés, 1 urna. *Sendero memorial* 67×30×30 cm forrado de mármol con jardinera, 4 urnas.
- Producto mayor: *Jardín privado* 7.99 m² (2.24 × 2.94 m), 4 gavetas / 4 osarios BAJO PISO, muros inferiores de block y superiores de tabique rojo, repisón y tapas de concreto. *Jardín familiar* 12.51 m² (3.30 × 3.10 m), 8 gavetas / 8 osarios bajo piso. *Capilla estándar* 11.42 m² (3.34 × 3.42 m), 6 gavetas / 6 osarios sobre o bajo piso, loseta, cancel de aluminio y cristal. *Capilla clásica* 10.96 m² (3.20 × 3.42 m), 6/6, puerta en arco y cúpula. *Capilla premier* igual a clásica + detalles de cantera. *Capilla doble romana* 7.34 m² (2.71 × 2.71 m), 5 gavetas / 4 osarios sobre piso.
- Mausoleo: *Nicho interior* mueble MDF con melamina, cristal claro; individual 1 urna, chico 2, grande 4, familiar 6.
- Escalera de venta del jardín privado: si la familia es de más de 4 → jardín familiar (8); si busca construcción cerrada → capillas (6).

## Contrato Gayosso aplicado a PROPIEDAD (jardín privado, nichos, gavetas, capillas) — leído del contrato PROFECO 3692-2022 el 2026-11-09

Mismo contrato de adhesión que los servicios funerarios. Puntos clave para explicar al cliente de propiedad (sin datos del cliente de la copia revisada):
- *Perpetuidad* (cláusula Tercera): el derecho de uso de fosas, nichos, gavetas y jardines es a perpetuidad conforme a la legislación aplicable. Al liquidar, Gayosso emite *Constancia de Pago Total* y el *Título de Derecho de Uso a Perpetuidad* (cláusula Sexta), con plano de ubicación.
- *Uso*: capillas y jardines privados requieren *100% pagado* para usarse (tabla de la cláusula Octava). El contrato puede usarse a partir de *15 días de la firma*; antes se trata como necesidad inmediata (precios de lista de uso inmediato, abonando lo pagado).
- *Lugar en construcción*: si el lugar aún no está construido, Gayosso debe tenerlo disponible en máximo 180 días naturales; si no, paga pena convencional al cliente.
- *Mantenimiento anual* (Quinta): obligatorio; se cobra a partir de los 6 meses de la adquisición o al primer uso, lo que ocurra primero. Para usar el lugar hay que estar al corriente. Montos en gayosso.com (tabla interna: jardines $2,800 + conservación $1,050, confirmar).
- *Abandono*: lugares sin inhumación, depósito de cenizas ni pago de mantenimiento por 10 años se consideran abandonados y Gayosso puede recuperarlos (con notificación previa y exhumación). Decirlo con honestidad: el mantenimiento al corriente protege la perpetuidad.
- *No incluido / a cargo del cliente*: derechos de inhumación ante autoridad, apertura y cierre (maniobras), grabado de lápida, mantenimiento anual, gestión de actas, derechos de traslado y permisos de inhumación, exhumación, reinhumación o cremación.
- *Beneficiarios*: hasta 2; titular sustituto designable y removible; usuarios designables y modificables por escrito.
- *Cesión*: al corriente, pagando 10% del precio vigente; Gayosso responde en 30 días naturales.
- *Pagos*: anticipados sin penalización; sin intereses pagando a tiempo; mora 3% mensual; >90 días puede rescindirse. Domiciliación a tarjeta de crédito o pagaré como garantía.
- *Cancelación*: 5 días hábiles tras la firma con devolución íntegra (aviso fehaciente por escrito). Después, pena convencional de 48% de lo pagado. Contratos ya usados (incluye Jardines Privados) NO pueden cancelarse: se mantienen hasta su liquidación.
- *Quita por fallecimiento del titular*: aplica solo a UN servicio funerario del titular; NO condona lotes, gavetas, criptas o nichos restantes: no prometerla en propiedad.
- Incumplimiento de Gayosso: devuelve lo pagado + 48%. Controversias: PROFECO. Atención a clientes L–V 9:00–17:00.

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
- 2026-10-29 (revisión): FRÍA `120257101274550768` en pausa (decisión del usuario); CALIENTE subida a $200/día. Acumulado 16–29 oct: CALIENTE Promo 2+1 $1,938.11 / 58 conv ($33.42), frecuencia 1.91, alcance 9,669, CTR 3.44%; últimos 7 días $1,345.86 / 39 conv ($34.51). FRÍA: Fin de Año $215.17 / 8 conv ($26.90, el más barato); Vaquita $872.84 / 15 conv ($58.19, no reactivar). Total cuenta $3,026 / 81 conv ($37.36). La caliente termina sola el 31-oct; para noviembre: creativo nuevo sin promoción y reactivar la fría solo con Fin de Año.
- 2026-10-30 (noche): VENTA CERRADA en Capillas Marianas (Universal Pro 2+1, cliente presencial el último día de la promoción, guion de cita: recorrido por sala + cierre por alternativa 48 m TDC / 36 m débito). Pendiente noviembre: creativo nuevo sin promoción para la caliente, reactivar fría solo con Fin de Año, ubicaciones solo Feed/Historias/Marketplace FB, caliente ~$100/día; confirmar promoción de noviembre de Gayosso y actualizar cifras de todas las propuestas.
- 2026-11-01: CONFIRMADO con Cotizador (fecha precio 01/11/2026, fin vigencia 30/11/2026) que Premier Pro 2+1 conserva las cifras de octubre: lista M036 $246,900.03 ($6,863.82/mes); contado P001 $131,686.58 ($43,895.53 c/u, ahorro $115,213.45, 46.7%); TDC D048 $3,321.14/mes ($159,670, ahorro 35.3%); TDC D036 $4,210.02/mes ($151,439.59, ahorro $95,460.44, 38.7%, $2,653.80 menos que la de lista). Orden de presentación pedido por el usuario: precio de lista → contado → 48 m TDC → 36 m TDC. El usuario de cotización "Juan Carlos" es interno del asesor, NO es cliente: no usarlo en propuestas.
- 2026-11-01: CONFIRMADO Universal Pro 2+1 noviembre (Cotizador 01/11/2026, vigencia 30/11/2026), mismas cifras que octubre: lista M036 $186,900.03 ($5,195.82/mes); TDC D048 $2,514.06/mes ($120,868.06, 35.3%); débito DD36 $3,360.13/mes; NUEVA condición P003 "tres exhibiciones": $99,685.00 en 3 pagos de ~$33,225 (ahorro $87,215, 46.7%; mismo precio que contado P001). Orden: lista → tres exhibiciones/contado → 48 m TDC → 36 m débito.
- 2026-11-04: CONFIRMADO Premier Pro 1 SERVICIO noviembre (Cotizador 03/11/2026, vigencia 30/11/2026, oficina GCM8): lista M036 $82,300.01 ($2,287.94/mes); TDC D048 $1,494.44/mes ($71,847.91, ahorro $10,452.10, 12.7%, 10% en cotizador); TDC D036 $1,894.41/mes ($68,144.41, ahorro $14,155.60, 17.2%); contado P001 $52,672.00 (ahorro $29,628.01, 36%, 20% en cotizador). Orden pedido para 1 servicio: lista → 48 m → 36 m → contado AL FINAL como "mayor ahorro"; nota "enganche opcional de 15% o 20%" sin cifras hasta tener captura; incluir direcciones de Capillas Marianas y Marianas Nogalar.
- 2026-11-06: OFERTA "BUEN FIN" GAYOSSO, EXCLUSIVA MARIANAS NOGALAR (comunicado interno). Paquetes integrales de NICHO Nogalar + servicios: con 2 o 3 servicios el descuento pasa de 25% a 30%; con 4 servicios, de 30% a 35%. Nicho con 1 solo servicio y paquetes integrales de Capillas Marianas: SIN cambio. Ejemplo del comunicado: 2 Universal Pro + nicho grande nivel medio, condición D035: octubre $134,515 → noviembre $125,547 (diferencia real $8,968; el comunicado dice "prácticamente $11,000": confirmar con cotización antes de publicar cifra). REGLA: NO mencionar porcentajes al cliente; hablar de la rebaja en PESOS ("de $5,000 a $15,000 menos que en octubre", según categoría y nicho). Vigencia del Buen Fin: pendiente de confirmar. Se usará para un 2º anuncio en la campaña activa.
- 2026-11-06: CIFRAS Buen Fin Nogalar "2 PREVISION GAYOSSO UNIVERSAL PRO + PAQ. NICHO CHICO ZONA MAUS PISO 5 NIV. MED" (producto nicho 827303), 30% en cotizador: lista M036 $167,805.02 (2 Universal $124,600.02 + nicho $43,205.00; 36 mensualidades de $4,664.98); D035 (35 meses con enganche, aplica TDC o débito; enganche personalizable al alza) enganche $14,976.60 + 35 × $2,426.21, precio $99,843.99 (ahorro $67,961.03, 40.5%; < $81 diarios por todo); contado P001 $93,970.81 (ahorro $73,834.21, 44%). Gancho: 2 Universal a lista $124,600 > lo que paga por todo → "el nicho le sale de obsequio" (contado $30,629 menos; D035 $24,756 menos). Vs. octubre (25% sobre la misma base, SUPUESTO a confirmar): D035 ~$7,131 menos; contado ~$6,712 menos. Orden: lista → 35 meses → contado → explicación del nicho de obsequio al final. CONFIRMADO por el usuario: el nicho chico es para 2 URNAS y la oferta LLEVA certificado vacacional de obsequio (LIMITADOS). Imagen: scratchpad/propuesta/universal2nicho_nogalar.html. Logo recuperado recortando un render previo (el scratchpad se borra al reiniciar el contenedor).
- 2026-11-06: misma oferta 2 Universal + nicho chico 2 urnas Nogalar, SIN ENGANCHE con TDC: D036 $3,004.25/mes × 36 (precio $108,066.43, ahorro $59,738.59, 35.6%; $1,660 menos que la mensualidad de lista; suma 36 pagos $108,153: no poner "total a pagar"); D048 $2,369.94/mes × 48 (precio $113,939.61, ahorro $53,865.41, 32.1%; < $80 diarios). En TODAS las opciones se paga menos que solo los 2 Universal a lista ($124,600) → nicho de obsequio. Formato aprobado: lista → 1 · enganche 15% (D035, mayor ahorro, crédito o débito) → 2 · sin enganche TDC 36 → 3 · sin enganche TDC 48; contado $93,970.81 como línea. Imagen: scratchpad/propuesta/universal2nicho_flex.html.

## Información operativa Gayosso (compartida 2026-11-06, consultar cuando se requiera)

Medios de pago de mensualidades (para clientes ya contratados, post-venta):
- *Oxxo*: pedir "pago de servicios Gayosso" con el número de referencia del contrato (uno por contrato; si no lo tiene, pedirlo en módulos o al 800 701 7830). Solo efectivo, con costo por servicio; conservar comprobante.
- *Liga de pago al celular*: llamar al 800 701 7830, pedir liga de pago, dar número de contrato o nombre del titular y celular; llega un mensaje con liga al banco para pagar con tarjeta de crédito o débito.
- *Caja en agencias Gayosso*: con número de contrato y de cliente (o nombre del titular) y monto; efectivo, crédito o débito.
- *Transferencia*: llamar al 800 701 7830, pedir pago por transferencia; llega una CLABE SPEI de un solo uso con vigencia de 24 h; transferir el monto EXACTO indicado.
- *Portal "Soy Cliente Gayosso"* (gayosso.com > Soy cliente): consultar servicios del contrato, descargar contratos digitales, estado de cuenta, pagar en línea con tarjeta, descargar facturas y actualizar beneficiarios y titular sustituto. Registro con QR del folleto oficial.
- Emergencia funeraria *247; 800 GAYOSSO (800 429 6776); redes @GayossoOnline. (No poner los 800 en imágenes de propuesta; sí en mensajes post-venta/bienvenida.)

Cuotas anuales de mantenimiento (tabla interna; usar para responder "¿cuánto es el mantenimiento?"):
- TABLA "CLUSTER 1" (compartida 2026-11-10, más reciente; confirmar si Monterrey es Cluster 1): gaveta mural / 4 gavetas / Ciprés $1,520; sendero memorial $1,520; jardines $2,530; capillas $3,165. Si se confirma, usar estas cifras en lugar de las de abajo.
- Nicho chico/individual $1,150; nicho grande/familiar $1,700; gaveta mural/4 gavetas/Ciprés $1,700; jardines $2,800; capillas $3,500; sendero memorial $1,700 (aplica en cementerios y mausoleos Gayosso, incl. Monterrey).
- Cuota de conservación: lote gaveta 2G/3G/4G, lote preferencial y gaveta mural $750; capilla, jardín familiar y jardín privado $1,050; nichos $900. (Confirmar con oficina si el nicho paga mantenimiento + conservación o solo una.)

Claves de producto por oficina de ventas:
- Oficinas: [CJ04] Cementerio Jardines del Descanso, [FCN1] Fun. Cap. Nogalar, [GCM8] Funeraria Capillas Marianas, [MC26] Mausoleo Capilla Marianas, [MIN1] Maus. Nogalar.
- Nogalar: Esencial 827291, Universal 827292, Premier 827294. Marianas: Esencial 826882, Universal 826885, Premier 826890.
- Condiciones de pago y descuento base (sin promoción): M036 efectivo 0%; DD36 débito 3%; D036 crédito 8%; D035, D020, D048 crédito 12%; P001 contado 12%. OJO: la tabla marca D035 como T. CRÉDITO; el 2026-11-06 el usuario dijo que la oferta D035 de nicho aplica crédito o débito: confirmar antes de prometer débito en D035.

Listas de precios de NICHOS y paquetes (precio de lista, rebaja comercial vigente noviembre 2026, sin promoción de servicios):
- Maus. Nogalar (MNM1): nicho chico zona maus piso 5 sup 827302 $32,000 (30%); med 827303 $43,205 (30%); inf 827304 $37,600 (30%); nicho grande zona maus piso 5 sup 827305 $64,000, med 827306 $86,405, inf 827307 $75,205 (30%); nicho fam cab zona maus piso 5 sup 827308 $166,395 (40%), med 827309 $224,650 (30%), inf 827310 $195,520 (40%); nicho grande cab z maus piso 5 sup 827311 $83,200, med 827312 $112,320, inf 827313 $97,760 (40%); nicho chico z Premier piso 5 sup 827314 $44,800 (40%), med 827315 $60,485 (30%), inf 827316 $52,640 (40%); nicho grande z Premier piso 5 sup 827317 $89,600, med 827318 $120,970, inf 827319 $105,285 (40%); nicho fam cab z Premier piso 5 sup 827320 $232,955, med 827321 $314,510, inf 827322 $273,730 (40%); nicho grande cab z Prem piso 5 sup 827323 $116,480, med 827324 $157,250, inf 827325 $136,865 (40%).
- Maus. Cap. Marianas (GG34): nicho familiar cabecera mausoleo med 823571 $193,935 (25%); nicho grande cabecera capilla s/i 823884 $143,655 (25%); nicho grande zona capilla niv. medio 823359 $149,180 (30%); nicho grande cabecera Premier med 824277 $135,755 (25%); nicho grande zona capilla sup/inf 823358 $110,505 (30%); nicho grande zona Premier niv. medio 821962 $104,430 (30%); nicho grande cabecera mausoleo med 823550 $96,965 (25%); nicho grande cabecera Premier s/i 824278 $100,560 (30%); nicho chico zona capilla niv. medio 823356 $74,590 (25%); nicho grande zona mausoleo niv. medio 821967 $74,590 (15%); nicho grande zona Premier sup/inf 821964 $77,355 (25%); nicho grande cabecera mausoleo s/i 823562 $71,825 (25%); nicho chico zona capilla sup/inf 823357 $55,250 (25%); nicho chico zona Premier niv. medio 821960 $52,215 (25%); nicho grande zona mausoleo sup/inf 821968 $55,250 (15%); nicho chico zona mausoleo niv. medio 821965 $37,295 (5%); nicho chico zona Premier sup/inf 821961 $38,680 (20%); nicho chico zona mausoleo sup/inf 821966 $27,625 (15%).
- Cementerio Jardines del Descanso (GG12): capilla clásica SP 6G 6O 824991 $838,340 (0%); capilla Premier SP 6G 6O 825064 $898,220 (0%); capilla clásica BP 6G 6O 824992 $1,013,480 (0%); jardín privado 4G 4OS 824751 $350,300 (5%); sendero memorial Premier sup 826616 $130,820, medio 826617 $109,140, inf 826618 $87,460 (35% total: 30% + 5% "150 años"); gaveta mural preferencial med 826491 $109,780 (35%), inf 826492 $97,230 (40%), sup 826490 $84,685 (30%); nicho chico preferencial med 826494 $78,525, inf 826495 $66,125, sup 826493 $53,725 (25%); paq. ecológico Ciprés Italiano 824763 $47,385 (0%).
- Estas rebajas son las de la tabla; el precio final real se toma SIEMPRE del Cotizador (las promociones de paquete pueden sustituirlas).

Plantillas de imagen: guardadas en el repo en `propuesta/` (render.js + logo.jpg + HTML base) porque el scratchpad se borra al reiniciar el contenedor. Render: `node propuesta/render.js <html absoluto> <png>` (Chromium/playwright preinstalado). Desde 2026-11-11 render.js pone sola la fecha del día (hora de Monterrey) en el encabezado ".top .d": siempre volver a renderizar antes de reenviar una imagen.
- 2026-11-06: CIFRAS Buen Fin Nogalar "2 PREVISION GAYOSSO PREMIER PRO + PAQ. NICHO CHICO ZONA MAUS PISO 5 NIV. MED" (oficina MIN1/FCN1, Premier 827294 + nicho 827303, 30%): lista M036 $207,805.02 (2 Premier $164,600.02 + nicho $43,205.00; 36 × $5,776.98); D035 enganche 15% $18,546.60 + 35 × $3,004.55 (precio $123,643.99, ahorro $84,161.03, 40.5%); D036 sin enganche 36 × $3,720.37 (precio $133,826.43, ahorro $73,978.59, 35.6%; $2,056 menos que la de lista); D048 sin enganche 48 × $2,934.87 (precio $141,099.61, ahorro $66,705.41, 32.1%; < $98 diarios); contado P001 $116,370.80 (ahorro $91,434.22, 44%). Nicho de obsequio en todas las opciones (2 Premier a lista $164,600; a 48 m paga $23,500 menos; contado $48,229 menos). Plantilla: propuesta/premier2nicho_flex.html.
- 2026-11-06: CIFRAS Buen Fin Nogalar "2 PREVISION GAYOSSO ESENCIAL PRO + PAQ. NICHO CHICO ZONA MAUS PISO 5 NIV. SUP" (MIN1/FCN1, Esencial 827291 + nicho 827302 NIVEL SUPERIOR, no medio; 30%): lista M036 $128,600 (2 Esencial $96,600 + nicho $32,000; 36 × $3,575.08); D035 enganche 15% $11,477.55 + 35 × $1,859.36 (precio $76,517.00, ahorro $52,083, 40.5%); D036 sin enganche 36 × $2,302.35 (precio $82,818.40, ahorro $45,781.60, 35.6%; $1,272 menos que la de lista); D048 sin enganche 48 × $1,816.24 (precio $87,319.40, ahorro $41,280.60, 32.1%; < $61 diarios); contado P001 $72,016.00 (ahorro $56,584, 44%). Nicho de obsequio en todas las opciones (2 Esencial a lista $96,600; a 48 m $9,281 menos; contado $24,584 menos). Plantilla: propuesta/esencial2nicho_flex.html. Patrón confirmado en las 3 categorías: total = lista × factor de condición (D036 0.92, D048 0.97, D035 0.85, P001 0.80) × 0.70; las MENSUALIDADES no se pueden derivar exactas (ajuste de redondeo del Cotizador): siempre pedir captura.
- 2026-11-06: CIFRAS CAPILLAS MARIANAS (MC26/GCM8, NO Buen Fin, 25% en cotizador) "2 PREVISION GAYOSSO ESENCIAL PRO + PAQ. NICHO CHICO ZONA PREMIER NIV. MEDIO" (Esencial 826882 + nicho 821960, Mausoleo Capillas Marianas): lista M036 $148,814.99 (2 Esencial $96,600 + nicho $52,214.99; 36 × $4,137.06); D035 enganche $14,230.43 + 35 × $2,305.33 (precio $94,869.56, ahorro $53,945.43, 36.2%; < $77 diarios); contado P001 $89,288.99 (ahorro $59,526, 40%). Nicho de obsequio: 2 Esencial a lista $96,600 → contado $7,311 menos; D035 solo $1,730 menos (argumento débil a meses). Nicho chico zona Premier = 2 URNAS (confirmado por el usuario). Plantilla: propuesta/esencial2nicho_marianas.html.
- 2026-11-06: misma oferta Marianas 2 Esencial + nicho zona Premier (2 urnas), SIN ENGANCHE: D036 36 × $2,854.57 (precio $102,682.35, ahorro $46,132.64, 31.0%; $1,282 menos que la de lista); D048 48 × $2,251.87 (precio $108,262.91, ahorro $40,552.08, 27.2%; < $76 diarios). OJO: en D036 y D048 el total SUPERA los 2 Esencial a lista ($96,600) → NO decir "nicho de obsequio" en esas opciones; el obsequio solo aplica con enganche (D035) o contado. Plantilla: propuesta/esencial2nicho_marianas_flex.html. Vs. Nogalar (Buen Fin) el mismo paquete es ~$15–21 mil más barato.
- 2026-11-07: FORMATO DE IMAGEN APROBADO hasta el 18-nov-2026: "C2 Buen Fin" = listón superior rayado rojo con borde dorado "🔥 BUEN FIN GAYOSSO · HASTA EL 18 DE NOVIEMBRE 🔥 / Precios especiales en previsión familiar · certificados vacacionales limitados", banda verde del producto debajo, vigencia "⏰ Precios Buen Fin hasta el 18 de noviembre · certificados limitados" y SIN fecha del Cotizador en letra pequeña. Plantillas en repo: propuesta/buenfin_premier2mas1.html, buenfin_universal2mas1.html, buenfin_esencial1.html (base: bf_C2.html). Aplicar a TODAS las propuestas (incl. paquetes con nicho) hasta el 18-nov. La 2+1 en el Cotizador sigue a 30-nov: si preguntan después del 18, "precio y certificados sujetos a disponibilidad".
- 2026-11-07: PUBLICIDAD OFICIAL GAYOSSO BUEN FIN (anuncio de Facebook compartido por el usuario): "Buen Fin 13 al 17 de noviembre"; "Adquiere 2 servicios funerarios, obtén un 3er servicio sin costo adicional + certificado vacacional"; letra pequeña: vigencia al 30-nov-2026, aplica en Universal y Premier, NO en Esencial, "aplica únicamente con forma de pago de contado y enganche hasta de 24 meses" (OJO: el Cotizador sí aplica el 2+1 en D036/D048 sin enganche; confirmar con oficina antes de que un cliente lo cuestione). Estrategia del usuario: urgencia propia hasta el 18-nov; argumento de cierre = "aparte su folio antes del 18 y se le respeta precio y certificado para firmar con calma" (el cliente no conoce el proceso de folio: explicarlo).
- 2026-11-08: CIFRAS JARDÍN PRIVADO, Cementerio Jardines del Descanso (oficina CJ04, producto 824751 "PAQ. JARDIN PRIVADO 4G 4OS": terreno a perpetuidad jardín privado 2x3, construcción jardín privado 4 gavetas, construcción de osario, servicio de inhumación; Ambivalente NO, Multiplaza NO). Lista M036 $350,300.01 (36 × $9,738.34). Contado P001 $280,240.01 (ahorro $70,060, 20%; $70,060 por lugar vs $87,575 a lista). D012 12 meses domiciliado: enganche 15% $44,663.25 + 11 × $23,016.46 (precio $297,755.01, ahorro $52,545, 15%). D020 35 meses enganche 20%: $59,551.00 + 35 × $6,788.81 (precio $297,755.01, ahorro $52,545). D048 sin enganche 48 × $7,067.65 (precio $339,791.01, ahorro $10,509, 3%; < $59 diarios por lugar). D060 60 × $6,222.03 = $374,821.01 SUPERA la lista (+$24,521): no presentarlo como oferta; solo si el cliente pide la mensualidad más baja, y aclarando que cuesta más. Son los descuentos base por condición (sin promoción extra). Jardín privado se usa al 100% pagado; mantenimiento jardines $2,800/año + conservación $1,050 (confirmar). Certificado vacacional en propiedad: CONFIRMAR con oficina que aplica. Plantilla: propuesta/buenfin_jardin_privado.html.
- 2026-11-09: CONFIRMADO Esencial Pro 2 SERVICIOS noviembre (Cotizador 09/11/2026, vigencia 30/11/2026, oficina GCM8 Capillas Marianas, clave 826882; promoción "2 PREVISION GAYOSSO ESENCIAL PRO + 20% de descuento", NO es 2+1): lista M036 $96,600.00 (36 × $2,685.48); contado P001 $61,824.00 ($30,912 c/u, ahorro $34,776, 36%); TDC D048 48 × $1,559.20 (precio $74,961.60, ahorro $21,638.40, 22.4%; < $26 diarios c/u; suma pagos −$120: no poner total a pagar); TDC D036 36 × $1,976.51 (precio $71,097.60, ahorro $25,502.40, 26.4%; $709 menos que la de lista; < $33 diarios c/u). Beneficio total (+$24,995): contado $59,771; 36 m $50,497; 48 m $46,633. Orden: lista → contado → 48 → 36. Plantilla: propuesta/buenfin_esencial2.html.
- 2026-11-10: CIFRAS GAVETA MURAL PREFERENCIAL NIVEL MEDIO, Jardines del Descanso (CJ04, clave 826491: terreno a perpetuidad gaveta mural 1×2.4 preferencial medio + construcción + servicio de inhumación; catálogo: 0.90×2.50×0.80 m, tapa de mármol, CAPACIDAD 1 GAVETA). Lista M036 $109,780 (36 × $3,051.88); contado P001 $87,824 (ahorro $21,956, 20%); TDC D036 36 × $2,807.73 ($100,997.60, ahorro $8,782.40, 8%; $244 menos al mes); TDC D048 48 × $2,214.92 ($106,486.60, ahorro $3,293.40, 3%; < $74 diarios). Enganche desde 15% disponible (sin captura). OJO: para 4 personas NO conviene (4 gavetas de contado $351,296 > jardín privado $280,240; por lugar $87,824 vs $70,060): presentar como 1 lugar y escalar a jardín privado o lote americano 4 gavetas / sendero memorial 4 urnas. Plantilla: propuesta/buenfin_gaveta_mural.html.
- 2026-11-10: CONFIRMADO Universal Pro 1 SERVICIO (GCM8, clave 826885, promoción "1 PREVISION GAYOSSO UNIVERSAL PRO + 10% de descuento"): lista $62,300.01; TDC D036 36 × $1,434.05 (precio $51,584.41, ahorro $10,715.60, 17.2%; < $48 diarios). Comparativa 1 servicio con TDC: Esencial D036 $1,111.79 · Universal D036 $1,434.05 · Premier D048 $1,494.44 (Premier a 48 m solo ~$60/mes más que Universal a 36 m: argumento para subir a Premier). Beneficio total (+$24,995): Esencial $33,303; Universal $35,711; Premier $35,447. Patrón 1 servicio confirmado en las 3 categorías: total = lista × factor (D036 0.92, D048 0.97, P001 0.80) × 0.90. Plantilla: propuesta/buenfin_3categorias_1servicio.html.
- 2026-11-10: CAMPAÑA OFICIAL GAYOSSO BUEN FIN (6 piezas compartidas por el usuario; "13 al 17 de noviembre", "Anticípate y protege el futuro de tu familia"; letra pequeña: válida al 30-nov-2026, SOLO Universal y Premier, consulta términos). Esquema:
  - 2 servicios + 3er servicio sin costo adicional + certificado vacacional.
  - 1 servicio: 20% por temporada + 20% adicional pagando de contado; o 20% + 15% pagando a 12 meses (enganche mínimo 15%).
  - 2 servicios: 25% por temporada + 20% adicional de contado; o 25% + 15% a 12 meses.
  - Cálculo esperado (descuentos en cascada sobre lista; CONFIRMAR con Cotizador): 1 Premier contado $52,672 (= lista × 0.80 × 0.80, ya confirmado); 1 Universal contado ≈ $39,872; 1 servicio a 12 meses = lista × 0.80 × 0.85 (Premier ≈ $55,964; Universal ≈ $42,364). 2 servicios contado = lista × 0.75 × 0.80 (2 Premier ≈ $98,760; 2 Universal ≈ $74,760); 2 servicios a 12 meses = × 0.75 × 0.85 (2 Premier ≈ $104,933; 2 Universal ≈ $79,433).
  - Lectura comercial: por servicio, el 2+1 de contado (Premier $43,895 c/u) sale MÁS barato que "2 servicios con 25%+20%" ($49,380 c/u): con 2 personas, ofrecer el 2+1 y designar el 3er servicio a otro familiar. Las condiciones a 36/48 meses sin enganche que da el Cotizador NO aparecen en la publicidad oficial (siguen vigentes en sistema: confirmar con oficina).
  - Esencial Pro NO entra en la campaña oficial (su 20% de 2 servicios es promoción de sistema, no Buen Fin).
- 2026-11-10: PIEZAS DE PREVENTA de la gerencia (compartidas por el usuario): (1) "¡Oferta de preventa Capillas San Nicolás! 2 servicios funerarios y llévate sin costo el nicho, mensualidades desde $1,816.24, 48 meses sin intereses" (= 2 Esencial + nicho Nogalar D048, ya confirmado); (2) "3x2 servicios funerarios categoría Premier, desde $3,321.14, 48 meses sin intereses, sin enganche". Ambas: GRATIS seguro médico GAYOSSO MED (aplican restricciones; detalles NO confirmados: preguntar en qué consiste antes de explicarlo), certificado vacacional Royal Holiday, "descuentos adicionales en paquetes con nichos y/o 2 o más servicios", vigencia 16-NOV-2026 sujeto a disponibilidad de folios, "promoción exclusiva por preventa Capillas Nogalar". Anuncio mejorado para Meta: propuesta/anuncio_nicho_nogalar.html (+ nogalar_edificio.jpg recortado de la pieza, baja resolución).
- 2026-11-10: CAMPAÑA CALIENTE `120257101274740768`: presupuesto subido a $400/día (decisión del usuario); conjunto `120257101283010768` con fin programado 2026-11-18 23:59 Monterrey (todo termina el 18; con folio se respeta precio a fin de mes). Nuevo anuncio "CALIENTE - Nicho de regalo Nogalar (fin 18 nov)" `120257540628430768` (creative `2748791848872682`, imagen hash `1d26f52f5f0a99a4cfe66066084ee688`, CTA WhatsApp) junto a "Promo 2+1 (fin 18 nov)" `120257497755090768`. Esta campaña no permite fechas por anuncio: el fin se pone en el conjunto. Subir imágenes a Meta: commitear el PNG al repo (público) y usar la URL raw de GitHub. Pendiente: creativo de cierre de año para después del 18.
- 2026-11-10: Criterio del usuario: el Buen Fin es estrategia comercial de Gayosso; es probable que los precios se mantengan hasta el 30-nov. Plan: el 17-nov cambiar la imagen (evitar saturar al público caliente) por una creatividad con la oferta vigente a fin de mes, sin la fecha del 18; extender el conjunto al 30-nov. Recordatorio programado para el 17-nov 8:52 am Monterrey.
- 2026-11-10 (19:00 Monterrey, revisión): CALIENTE a $400/día, gasto del día $370 / 23 conv ($16.10). Anuncio "Nicho de regalo Nogalar" `120257540628430768` (primer día): $275 / 21 conv ($13.12), CTR 8.06%, frecuencia 1.3 → MEJOR costo histórico de la cuenta (supera Fin de Año $16.35). "Promo 2+1 (fin 18 nov)" `120257497755090768`: ~$991 / 17 conv ($58.32) del 7 al 10-nov; quedó en PAUSA el 10-nov 18:09 (no lo pausó Claude). 1–10 nov campaña: ~$3,124 / 93 conv (~$33.6). Decisión sugerida: no tocar el conjunto (aprendizaje), mantener $400, vigilar frecuencia (>2.5 = saturación) antes del cambio del 17-nov.
- 2026-11-11: CONTRATO ANTIGUO de cliente revisado (sin guardar datos del cliente): "PAQ. SF PREVISION PLATA ELITE" (categorías anteriores de Gayosso; el anexo menciona también una "Categoría TOTAL", la única que incluía trámites y actas). Contenido por servicio: ataúd cat. Plata Elite, cafetería básica PR, servicio funerario SALA ESTÁNDAR, embalsamado PR, arreglo estético, paq. Ambivalente → mismos componentes que el Esencial Pro/Universal Pro actuales (Sala Estándar), NO equivale a Premier Pro (sala Premier, Multiplaza, acta). Equivalencia exacta Esencial vs Universal depende del ataúd: confirmar con Atención a Clientes (81) 8345-7014. Oportunidad con clientes de contratos antiguos: venta de nicho/propiedad (tienen servicio ambivalente pero no lugar de descanso) o escalar a Premier. El anexo antiguo da "Cañón de la Meza No. 7650" y horario 8:00–18:00 para Jardines del Descanso (nosotros teníamos "Calle de la Meza" y 5:00–18:00: confirmar).
- 2026-11-11: certificado vacacional re-verificado en https://que-es.royal-holiday.com/gayosso/ (mismas condiciones guardadas arriba: reservaciones hasta 31-dic-2026; reservar en 3 meses y viajar en 6 meses desde la entrega). La diapositiva interna de Gayosso dice "reservar hasta 01-oct-2026 y viajar hasta 31-ene-2027" y menciona Mazatlán y Los Cabos (sin todo incluido): está DESACTUALIZADA, usar la web. Texto resumen para cliente entregado (sin transporte, solo titular, una vez por familia, parejas 30–60 con ingreso mancomunado ≥ $50,000).
- 2026-11-11: IMÁGENES DE NIVELES DE NICHOS (fotos del usuario): propuesta/niveles_nichos_marianas.html y niveles_nichos_nogalar.html. Marianas: zonas Premier (planta alta), Capilla (planta baja, junto a la capilla ecuménica) y Mausoleo; distribución "nueva etapa" por filas A–H: superior (A–C), medio (D–F), inferior (G–H); medidas interiores aprox. nicho chico 27 × 25 cm × 40 cm de fondo, grande 56 × 25 × 40 cm. Nogalar: Mausoleo piso 5, zonas Mausoleo y Premier, niveles sup/med/inf (medidas no confirmadas). Capacidades que maneja Gayosso: 2 (chico), 4 (grande), 6 (familiar), 8 y 10 urnas (cuáles productos son de 8 y 10: confirmar). Argumento: el nivel MEDIO (altura de la vista) es el más caro; superior el más accesible (en Marianas inferior = superior; en Nogalar inferior es intermedio).
- 2026-11-11: CONFIRMADO NICHO SOLO Nogalar (Cotizador 11/11/2026, vigencia 30/11/2026, oficina MIN1; descuentos base por condición, sin promoción de paquete): SUPERIOR 827302: lista M036 $32,000 (36 × $889.60); D036 36 × $818.43 ($29,440, ahorro $2,560); P001 $25,600 (ahorro $6,400). MEDIO 827303: lista $43,205 (de la tabla, falta captura M036 para la mensualidad); D036 36 × $1,105.01 ($39,748.60, ahorro $3,456.40); P001 $34,564 (ahorro $8,641). Medio vs superior: +$286.58/mes (< $10 diarios) o +$8,964 de contado. Sin opción 48 meses por monto; enganche sí (pedir captura). Certificado vacacional en nicho solo: CONFIRMAR.
