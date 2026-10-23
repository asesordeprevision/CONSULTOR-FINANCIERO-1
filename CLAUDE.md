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
- Flujo de cierre: tras el apartado, Gayosso envía al cliente un correo ("Asegura hoy la paz del mañana") con botón "Ver mi cotización"; el cliente la revisa y FIRMA ELECTRÓNICAMENTE (válido por contrato, cláusula de contratación por medios electrónicos). Acompañar ese correo con un WhatsApp puente que le indique qué hacer.
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
