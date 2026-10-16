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

## Operación

- Editar un conjunto o campaña activa por MCP lo pausa automáticamente: reactivar campaña y conjunto después de cada edición.
- Tras cambiar segmentación, no volver a tocar el conjunto en 5–7 días (fase de aprendizaje).
- Números extranjeros de spam (+234, +92, +91, +62, etc.): no responder, bloquear y reportar en WhatsApp.

## Historial

- 2026-10-07 00:15 UTC: corregida la segmentación del conjunto "Previsión Familiar - Cierre WhatsApp - SEP 2026" (`120255806431370768`); campaña `120255806054890768` con fin programado 2026-10-08 00:15 UTC (18:15 hora de Monterrey del 7-oct).
- 2026-10-16: creadas en pausa la campaña FRÍA `120257101274550768` ($200/día, conjunto `120257101281740768`, anuncio `120257101286310768`) y la CALIENTE `120257101274740768` ($60/día, conjunto `120257101283010768`, anuncios `120257101286860768` y `120257101287530768`). Solo ubicaciones de Facebook: Estados de WhatsApp exige incluir Historias de Instagram. Al publicarlas hay que pausar Tranquilidad `120257021195410768`.
- 2026-10-16: nuevos creativos. FRÍA: anuncio "Vaquita Padre Regio" `120257101817340768` (creative `1410500244484937`) compite con Fin de Año. CALIENTE: anuncio "Día de Muertos Promo 2+1" `120257101819650768` (creative `1468744925130546`); la campaña CALIENTE termina 2026-11-01 05:59 UTC (fin de la promo del 31-oct). En la caliente NO activar los anuncios con imágenes repetidas (`120257101286860768`, `120257101287530768`). Imágenes subidas desde Business Suite dan "Image Not Found" por API; deben subirse desde el Administrador de anuncios.
