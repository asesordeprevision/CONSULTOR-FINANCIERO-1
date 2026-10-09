# Consultor Financiero — memoria de campañas Meta Ads

Cuenta publicitaria principal: `789501147519125` (negocio "Abraham Cutipa - Asesor Financiero", MXN).
La cuenta `1779143873445450` ("Consultor Financiero" / Previsión Familiar) aún no está habilitada para Ads MCP.
Mercado: previsión funeraria / previsión familiar en Nuevo León (Monterrey y área metropolitana).

La misma cuenta `789501147519125` también corre la línea de negocio **Créditos** (créditos de nómina para pensionados, jubilados y trabajadores del sector público). Este chat/proyecto está enfocado solo en Créditos, no en Gayosso/Previsión Familiar — tratar ambas líneas como independientes al aplicar las reglas de segmentación de abajo.

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
- Mantener exclusión de la audiencia "Retargeting Nogalar - Interaccion Pagina 365d" (`120255465505980768`) en campañas de captación en frío.

## Operación

- Editar un conjunto o campaña activa por MCP lo pausa automáticamente: reactivar campaña y conjunto después de cada edición.
- Tras cambiar segmentación, no volver a tocar el conjunto en 5–7 días (fase de aprendizaje).
- Números extranjeros de spam (+234, +92, +91, +62, etc.): no responder, bloquear y reportar en WhatsApp.

## SaleAds IA (herramienta externa)

SaleAds IA crea/edita campañas de forma independiente en esta misma cuenta, fuera de este chat. Riesgo conocido: al crear conjuntos con `destination_type = WHATSAPP`, genera los creativos con CTA "Instagram Message" por default en vez de "WhatsApp Message" — esto bloquea la entrega con el error "Invalid Call To Action: Invalid Call To Action type is used with Click To WhatsApp ad".

- Fix técnico: un creativo de video con CTA `WHATSAPP_MESSAGE` necesita `call_to_action.value.app_destination = "WHATSAPP"` explícito (vía `object_story_spec` inline en `ads_create_ad`). Sin ese `value.app_destination`, Meta intenta enrutarlo como Messenger y choca con `optimization_goal: CONVERSATIONS` + `destination_type: WHATSAPP`, devolviendo el error "Replies optimization only with Messenger". El CTA con `app_destination` tampoco acepta `link_url` ("Too many parameters in Call To Action").
- El creativo roto es inmutable: hay que crear creativo + anuncio nuevos y archivar (no pausar — Meta revalida el CTA inválido incluso para confirmar PAUSED) los anuncios viejos.
- SaleAds IA también duplica conjuntos idénticos (mismo targeting, mismos creativos, mismo minuto de creación) bajo una sola campaña, causando fragmentación — revisar y archivar duplicados.
- Mientras una campaña de SaleAds IA esté en fase de aprendizaje (5–7 días tras una corrección), pausar esa estrategia específica en el dashboard de SaleAds IA (botón "Pausar estrategia"), no desconectar la integración.

## Historial

- 2026-10-07 00:15 UTC: corregida la segmentación del conjunto "Previsión Familiar - Cierre WhatsApp - SEP 2026" (`120255806431370768`); campaña `120255806054890768` con fin programado 2026-10-08 00:15 UTC (18:15 hora de Monterrey del 7-oct).
- 2026-10-09: campañas "Créditos especializados para pensionados y activos - e05d" (`120256976525130768`, $25 MXN/día) y "Asesoría financiera para trabajadores del estado - ba49" (`120256976523740768`, $41.66 MXN/día), generadas por SaleAds IA, llegaron con CTA "Instagram Message" en los 5 videos de e05d pese a destino WhatsApp (bloqueaba entrega). Corregido: 5 creativos/anuncios nuevos con CTA `WHATSAPP_MESSAGE` + `app_destination` correcto (ver sección SaleAds IA); 5 anuncios viejos archivados; conjunto "ba49 - AdSet 2" (duplicado exacto de AdSet 1) archivado por fragmentación. Campaña ba49 (imágenes) ya tenía el CTA correcto, no requirió cambios. Ambas estrategias pausadas en el dashboard de SaleAds IA para respetar la fase de aprendizaje — no tocar hasta ~2026-10-16.
