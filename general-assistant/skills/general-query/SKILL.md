---
name: general-query
description: Atiende una consulta general del usuario que requiere informacion publica, hechos actuales, contexto externo o verificacion de afirmaciones. Decide por turno si invocar io.gravitonai.tools.web_search o basta con conocimiento general, y sintetiza la respuesta con atribucion. NO usar para revision de contratos (usar commercial-legal), opinion legal/fiscal/medica/financiera concreta, ni acceso a datos internos del usuario.
---

# general-query

Atiende una consulta general del usuario. Decide si necesita invocar `io.gravitonai.tools.web_search` o basta con conocimiento general. Sintetiza la respuesta final con atribucion visible (URL por fuente usada) y marcando `[verificar]` los claims que no se hayan podido confirmar.

> **No** es un plugin legal, fiscal, medico ni financiero. No emite opinion profesional. Para temas verticales, derivar.

## Guardrails

Aplican los guardrails globales del `CLAUDE.md` raiz y los del `CLAUDE.md` del plugin. Especificos de esta skill:

1. **Atribucion obligatoria.** Toda fuente web usada lleva URL visible al final de la respuesta (seccion "Fuentes"). Si no se invoca `io.gravitonai.tools.web_search`, todo claim factual lleva `[verificar]`.
2. **No inventar datos.** Si `io.gravitonai.tools.web_search` no devuelve resultados suficientes, decirlo explicitamente y sugerir reformular la consulta. Nunca inventar URL, cifras, fechas o citas.
3. **Tool budget.** Maximo dos invocaciones de `io.gravitonai.tools.web_search` por turno. Si la primera no responde, reformular y volver a invocar.
4. **Sin DRAFT header.** Output de respuesta directa, sin preambulo de borrador.
5. **Idioma del usuario.** Responder en el idioma de la consulta.
6. **Privacidad.** No incluir nombres reales de personas o empresas en ejemplos. Placeholders: `Acme Corp.`, `Juan Perez`. La entrada llega ya anonimizada por el orquestador; tratarla como tal.
7. **Derivacion explicita.** Si la consulta es de un vertical conocido (legal, fiscal, medico, financiero concreto, revision de contratos), derivar al plugin correspondiente y abortar este skill.

## Procedimiento

### Paso 1 — Recibir input

Aceptar la consulta del usuario en lenguaje natural. La entrada llega ya anonimizada por el orquestador; no contiene PIIs. Si la consulta esta vacia o es puramente un saludo, responder de forma breve y preguntar en que se puede ayudar.

### Paso 2 — Clasificar la consulta

Decidir en que categoria cae la consulta. **Una** de las siguientes:

1. **Vertical especializado claro** (revision de contratos, opinion legal concreta, tributaria, medica, financiera). → Derivar al plugin correspondiente (ver tabla en `CLAUDE.md` del plugin). **Abortar este skill.**
2. **Ambigua** (no queda claro que quiere el usuario, o el alcance es muy amplio). → Pedir aclaracion antes de continuar. **Abortar este skill hasta tener aclaracion.**
3. **General factual** (hechos verificables, datos publicos, contexto externo, actualidad). → Continuar al Paso 3.
4. **General sin datos externos** (razonamiento, explicacion conceptual, redaccion, traduccion, calculo). → Ir directo al Paso 5 (responder sin web_search).

### Paso 3 — Decidir si requiere web_search

Para una consulta clasificada como "general factual", evaluar:

- **Requiere datos externos** (alguno de los siguientes): fechas actuales, eventos recientes, cifras publicas, jurisprudencia o regulacion abierta, entidades nombradas especificas, productos/servicios concretos, definiciones de dominio tecnico no comun. → **Invocar `io.gravitonai.tools.web_search`** con la consulta (ya anonimizada). Continuar al Paso 4.
- **No requiere datos externos** (alguno de los siguientes): conceptos generales, matematica, logica, redaccion, traduccion, explicacion pedagogica. → Ir directo al Paso 5 (responder sin web_search, marcar claims factuales con `[verificar]`).

> Regla practica: si la respuesta correcta podria haber cambiado en los ultimos 12-24 meses, probablemente requiere web_search. Si es conocimiento establecido, no.

### Paso 4 — Invocar web_search y procesar resultados

Invocar `io.gravitonai.tools.web_search` con la consulta del usuario (preferiblemente la formulada por el usuario; reformular solo si la consulta es claramente mejorable).

- **Parametros**:
  - `query`: la consulta en lenguaje natural.
  - `num_results`: 5 por defecto. Subir a 10 si la primera invocacion no dio resultados utiles.
- **Output esperado**: lista de hasta N resultados con `title`, `url`, `snippet`, `content` (contenido completo extraido de la pagina).
- **Post-procesamiento**:
  - Filtrar resultados irrelevantes (URL rota, snippet sin relacion con la consulta, contenido vacio).
  - Identificar los resultados que se usaran para sustentar claims factuales en la respuesta final.
  - Para cada resultado usado, conservar `title` y `url` para la seccion "Fuentes".

Si despues de la primera invocacion no hay resultados utiles:
- Reformular la consulta (aclarar terminos, probar sinonimos, reducir ambito).
- Volver a invocar `io.gravitonai.tools.web_search`.
- Si la segunda invocacion tampoco da resultados utiles, decirlo explicitamente al usuario y sugerir reformular.

Si la tool no esta disponible:
- Degradar con gracia: responder con conocimiento general y marcar **todos** los claims factuales con `[verificar]`.
- Sugerir al usuario verificar la informacion por su cuenta.

### Paso 5 — Sintetizar la respuesta

Componer la respuesta final siguiendo la plantilla en `assets/answer-output-template.md`. La respuesta debe:

1. **No envolverse en bloques de codigo.** Markdown limpio, texto corrido.
2. **Responde en el idioma del usuario.**
3. **Cero emojis** salvo solicitud explicita.
4. **Lista de fuentes** al final, con formato `N. Titulo — URL`, una entrada por cada resultado de web_search usado.
5. **Claims no confirmados** al final bajo "Verificar", si los hay.
6. **Sin opinion profesional.** No afirmar como verdad cosas que dependan de consejo legal, fiscal, medico o financiero. Marcar `[verificar]` y sugerir consultar a un profesional.

### Paso 6 — Derivacion a vertical (si aplica)

Si en algun momento del procedimiento queda claro que la consulta es de un vertical especializado (p. ej. el usuario aclara que su consulta es sobre un contrato especifico, o pide opinion legal concreta):

- Abortar la respuesta actual.
- Indicar al usuario que plugin vertical corresponde.
- No sintetizar respuesta propia sobre el vertical.

## Formato de salida

Ver `assets/answer-output-template.md`. Estructura obligatoria:

1. Cuerpo de la respuesta en Markdown limpio (sin code fences).
2. **Fuentes** — lista numerada con `Titulo — URL` (solo si se uso web_search).
3. **Verificar** — lista de claims no confirmados (si los hay).

## Escalacion

- **Interna (a otro plugin vertical)**: si la consulta es de un vertical conocido, derivar (ver tabla en `CLAUDE.md` del plugin). No hay escalacion a humano desde este plugin.
- **Externa (a profesional humano)**: sugerir al usuario consultar a un profesional humano cuando la consulta sea legal, fiscal, medica o financiera concreta. No emitir opinion profesional.

## Como NO se usa esta skill

- No la invoques para revision de contratos. Usar `commercial-legal`.
- No la invoques para opinion legal, fiscal, medica o financiera concreta. Marcar `[verificar]` y derivar a un profesional humano.
- No la invoques para acceder a datos internos del usuario (documentos adjuntos, RAG privado, bases corporativas). Solo informacion publica.
- No la invoques como agente de tareas (enviar emails, crear tickets, escribir en calendarios). Para eso estan otros plugins.
- No invoques `io.gravitonai.tools.web_search` mas de dos veces por turno. Reformular y sugerir al usuario si la busqueda no da resultados utiles.
