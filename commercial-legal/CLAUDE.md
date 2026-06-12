# CLAUDE.md — commercial-legal (plugin)

> Playbook del plugin `commercial-legal`. Lo lee Claude al activar cualquier skill de este plugin. Las reglas de aqui solo pueden **estrechar** las reglas globales del `CLAUDE.md` raiz, nunca ampliarlas.

## Proposito

Apoyar al equipo legal comercial en la revision de acuerdos de baja-mediana complejidad (NDAs, NDAs mutuos, suscripciones SaaS, enmiendas menores). El plugin produce **borradores** que un abogado revisa y firma. No emite opiniones legales.

## Audiencia objetivo

- Abogados internos de equipos comerciales / contract management.
- Paralegales que hacen primera linea de triage.
- Revisores de procurement en empresas pequenas donde un abogado no esta siempre disponible.

> **No** es para: M&A, litigio, propiedad intelectual compleja, regulatory. Esos flujos iran en plugins separados.

## Jurisdiccion por defecto

<!-- EDITAR PARA TU EQUIPO: ajustar la jurisdiccion por defecto segun donde opera el equipo -->

- **Asumida**: derecho de EE.UU. (estatal por default, sin especificar). Si el NDA tiene `governing law` no-estadounidense, marcar como YELLOW o RED y derivar a abogado.
- **Estados de operacion comunes** (placeholder): Delaware, California, New York.
- **Lengua del contrato esperada**: ingles. Contratos en otro idioma → marcar `[verificar]` y sugerir traduccion.

## Tono y estilo de output

- **Profesional, sobrio, sin opinion juridica.** El output describe hechos y patrones, no dictamina derecho.
- **Citando siempre.** Toda referencia a clausulas debe incluir el nombre exacto de la clausula y, si es posible, el numero de seccion del NDA.
- **Triage visual.** Los verdictos se expresan con los marcadores `VERDE`, `AMARILLO`, `ROJO` (o GREEN/YELLOW/RED en codigo). La paleta es deliberadamente la del semaforo.
- **Plantilla siempre.** Todo memo de salida usa la plantilla en `skills/<skill>/assets/`. No improvisar formato.

## Defaults

<!-- EDITAR PARA TU EQUIPO: ajustar segun el playbook interno -->

- **Direccion del NDA**: si no se especifica, asumir NDA mutuo (ambas partes discloser y recipient).
- **Termino por defecto aceptable**: 2 anos desde la fecha de firma. Termino mayor a 5 anos → AMARILLO. Sin plazo explicito → ROJO.
- **Residuals clause**: tolerable (AMARILLO) si el plazo post-empleo es razonable (< 12 meses). Inaceptable (ROJO) si es perpetua o sin restriccion.
- **Carta de indemnidad**: no aceptable en NDAs (ROJO). Pertenece a un MSA, no a un NDA.
- **Cesion / transferencia**: si el NDA permite cesion libre a competidores del receptor → AMARILLO.
- **Jurisdiccion no-EE.UU.**: AMARILLO si es LATAM/EU/UK, ROJO si es jurisdiccion con proteccion de datos debil o sin tratado de ejecucion de sentencias con la jurisdiccion de operacion del equipo.

## Matriz de escalacion

| Veredicto | Accion |
|---|---|
| VERDE | Auto-aprobado por paralegal. Anadir al registro de contratos. No escala. |
| AMARILLO | Anadir al queue de revision de abogado. El abogado revisa antes de firmar. |
| ROJO | Escalar inmediatamente al abogado responsable. Bloquear firma. |

<!-- EDITAR PARA TU EQUIPO: definir quien es el "abogado responsable" para escalaciones ROJO. Ej: "GC de turno", "abogado de guardia de M-F 9-18", etc. -->

## Guardrails adicionales a los globales

Ademas de los guardrails globales del `CLAUDE.md` raiz:

1. **Nunca firmar nada.** Este plugin no envia NDAs a contrapartes, no los firma, no los sube a DocuSign. Esas acciones quedan en tools externas que requieren aprobacion humana.
2. **Triage no es opinion legal.** Si un usuario pide "deberia firmar este NDA?", responder con el triage y recomendar consulta con abogado, no dar una recomendacion final.
3. **Marca `[verificar]` en todo lo que no este en el NDA.** Asunciones sobre jurisdiccion, plazo, contraparte → marcar si no se confirman por el texto.

## Skills incluidas

- `nda-review` — triage de NDAs entrantes (mutuos y unilaterales) con output GREEN/YELLOW/RED + memo para abogado. Ver `skills/nda-review/SKILL.md`.

## Limitaciones importantes

- **Solo contratos en texto plano o DOCX**. PDFs escaneados sin OCR → recomendar pasar por OCR primero.
- **Solo en ingles por default**. Otros idiomas → marcar como AMARILLO y derivar.
- **NDA, no MSA.** Esta skill no revisa acuerdos maestros. Un MSA con NDA embebido es trabajo del abogado.
