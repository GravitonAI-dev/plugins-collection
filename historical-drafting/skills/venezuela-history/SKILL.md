---
name: venezuela-history
description: Investigación especializada en historia de Venezuela con borradores de resúmenes y análisis verificables, citas trazables y separación entre hecho documentado e interpretación. NO usar para historia de otros países, eventos contemporáneos (< 50 años), biografía de personas vivas, ni para emitir verdades historiográficas definitivas.
---

# venezuela-history

Investigacion especializada en historia de Venezuela. Produce borradores de resumenes y analisis verificables, con citas trazables y separacion explicita entre hecho documentado e interpretacion. Todo output es un borrador para revision humana; no sustituye validacion academica ni revision por pares.

## Guardrails

Aplican los guardrails globales del `CLAUDE.md` raiz y los del `CLAUDE.md` del plugin. Especificos de esta skill:

1. **Sin header DRAFT legal.** Esta skill no toca temas legales / regulatorios / fiscales / de privacidad, por lo que el header canonico `DRAFT — para revision por un abogado` no aplica.
2. **Marcador `[verificar]` obligatorio** en toda afirmacion sin fuente trazable. Sin fuente no se afirma como hecho.
3. **Separacion hecho / interpretacion.** El output distingue visualmente entre hechos documentados y analisis o interpretacion. Nunca se presenta interpretacion como hecho.
4. **Sin anacronismos.** No se aplican categorias o instituciones modernas a un evento historico si no existian en su epoca. Si la proyeccion retroactiva es util, debe declararse explicitamente como interpretacion.
5. **Sin datos inventados.** No se inventan fechas, cifras, nombres, ni citas. Si un dato es incierto, se marca `[verificar]` o se excluye del borrador.
6. **Idioma por defecto**: espanol. Si la consulta es en otro idioma, mantener el idioma del usuario y buscar fuentes en ese idioma cuando sea posible.
7. **Borrador, no publicacion.** El output es para revision humana. No se presenta como verdad historiografica definitiva.

## Procedimiento

### Paso 1 — Recibir input

Aceptar uno o varios de los siguientes inputs del usuario:

- **Tema o evento historico de Venezuela** (obligatorio). Ej: "la guerra federal", "el golpe de estado de 1948", "la industria petrolera bajo Perez Jimenez".
- **Epoca o periodo** (opcional). Si el usuario lo acota, respetarlo. Si no, inferirlo del evento.
- **Tipo de output** (opcional): `resumen`, `analisis`, `cronologia`, `ficha-biografica`. Default: el agente elige el mas adecuado al evento.
- **Fuentes aportadas** (opcional): URLs, paths locales o citas que el usuario ya tiene y quiere que se usen como base.
- **Nivel de profundidad** (opcional): `breve`, `estandar`, `detallado`. Default: `estandar`.

Si el input obligatorio esta vacio o es ambiguo, pedir aclaracion antes de continuar. No inventar contenido.

### Paso 2 — Validar el alcance

Antes de investigar, confirmar que la consulta entra en el alcance de la skill:

- Es historia de Venezuela (no de otro pais).
- No es un evento contemporaneo estricto (ultimos 50 anios), salvo que el usuario marque explicitamente `nivel=detallado` y justifique la inclusion.
- No es biografia de una persona viva.
- No es una consulta factual actual (ej: "quien es el presidente actual de Venezuela"); eso va a `general-assistant`.

Si la consulta cae fuera del alcance:

- Abortar el flujo de la skill.
- Derivar al plugin adecuado (`general-assistant` en la mayoria de los casos) con un mensaje claro: `Esa consulta no entra en el alcance de la skill venezuela-history. Para <razon>, el plugin adecuado es <plugin>. Si lo que querias era investigar <evento>, podemos reformular la consulta.`

Si la ambiguedad es alta pero no evidente fuera de alcance, marcar `[verificar: alcance]` y pedir aclaracion al usuario antes de continuar.

### Paso 3 — Identificar el evento y sus hechos clave

Descomponer el tema en hechos clave a investigar. Para el alcance acordado:

- Lista tentativa de afirmaciones factuales a verificar.
- Epoca, actores principales, ubicacion geografica.
- Si la informacion disponible es insuficiente para descomponer, marcar `[verificar: alcance]` y pedir aclaracion al usuario.

Consultar las references disponibles para evitar anacronismos y para identificar periodizacion comun:

- `references/venezuela-glossary.md` para terminos historicos, politicos e institucionales.
- `references/venezuela-timeline.md` para situar el evento en la cronologia nacional.
- `references/primary-sources-index.md` para localizar archivos y repositorios.
- `references/reference-historians.md` para identificar historiadores y obras clave por epoca.

### Paso 4 — Recolectar fuentes

- **Fuentes del usuario**: si el usuario las aporto, leerlas con `io.gravitonai.tools.read_document`.
- **Complemento con busqueda**: usar `io.gravitonai.tools.web_search` para localizar fuentes primarias y secundarias adicionales.
- **Jerarquia** (de mayor a menor confianza, ver `CLAUDE.md` del plugin):
  1. Fuentes primarias (documentos de epoca, archivos, periodicos contemporaneos).
  2. Fuentes secundarias academicas con revision por pares.
  3. Fuentes secundarias divulgativas o enciclopedicas.
  4. Otras fuentes web. Marcar como `[verificar: fuente]` salvo evidencia clara de procedencia.

Si `web_search` o `read_document` no estan disponibles (todas las tools son opcionales), la skill degrada con mas marcadores `[verificar]` y un borrador mas conservador.

### Paso 5 — Triangular hechos

Para cada afirmacion factual de la lista tentativa:

- Buscar al menos dos fuentes coincidentes, o una fuente primaria.
- Si se logra, asignar veredicto VERDE.
- Si solo hay una fuente secundaria o fuentes con diferencias menores, asignar AMARILLO y documentar la fuente unica o las discrepancias.
- Si no hay fuente trazable o las fuentes son contradictorias, asignar ROJO y no presentar la afirmacion como hecho.

### Paso 6 — Clasificar cada bloque

Asignar el veredicto por bloque (VERDE / AMARILLO / ROJO) segun la matriz del `CLAUDE.md` del plugin.

| Veredicto | Significado |
|---|---|
| VERDE | Hecho documentado por una fuente primaria o dos o mas fuentes secundarias coincidentes. |
| AMARILLO | Hecho apoyado por una sola fuente secundaria, o fuentes secundarias con diferencias menores. |
| ROJO | Hecho sin fuente trazable, fuentes contradictorias, o afirmacion fuera del alcance del evento. |

### Paso 7 — Separar analisis de hechos

Si el `tipo de output` incluye `analisis` (o si el agente lo juzga util dado el evento):

- Redactar la seccion de analisis / interpretacion como una seccion visualmente separada de los hechos documentados.
- Declarar explicitamente que el contenido de esa seccion es interpretacion del autor, no hecho.
- Toda conclusion interpretativa debe estar anclada en los hechos documentados en secciones anteriores.

### Paso 8 — Componer cronologia (si aplica)

Si el evento lo amerita (multiples hechos con fechas, secuencia temporal relevante), redactar una cronologia:

- Solo hechos VERDE o AMARILLO.
- Cada item con fecha (o rango si es incierto), descripcion corta y fuente.
- Items sin fecha exacta → marcar `[verificar: fecha]`.

### Paso 9 — Componer el output final

Estructura obligatoria del output (no hay asset formal; esta estructura es fija en el `SKILL.md`):

1. **Metadata**: plugin, version, skill, fecha del borrador, tema, epoca.
2. **Hechos documentados**: afirmaciones con fuente trazable y veredicto por bloque.
3. **Analisis / interpretacion** (si aplica): seccion separada, declarada como interpretacion.
4. **Cronologia** (si aplica): secuencia temporal con fuentes.
5. **Lista de fuentes**: agrupadas por jerarquia (primarias, secundarias academicas, divulgativas, otras).
6. **Issues y marcadores `[verificar]`**: afirmaciones sin fuente o con fuente debil, marcadas para revision humana.
7. **Recomendacion de escalacion**: si hay bloques en ROJO, indicar el flujo al investigador responsable.

### Paso 10 — Listar issues y escalacion

Recopilar todos los marcadores `[verificar]` del output en una seccion visible al final:

- Bloque o afirmacion afectada.
- Tipo de verificacion faltante (fuente, fecha, cifra, alcance).
- Sugerencia de donde encontrar la verificacion (ej: "Archivo General de la Nacion", "Diario de debates de la fecha X").

Si hay bloques en ROJO, emitir recomendacion explicita de escalacion al **investigador responsable** (ver `CLAUDE.md` del plugin). No invocar `io.gravitonai.tools.escalate_to_attorney` (es una tool legal; esta skill no es legal).

### Paso 11 — Entregar el borrador

Devolver el borrador al usuario con:

- Advertencia explicita de que es borrador para revision humana, no verdad historiografica definitiva.
- Lista visible de issues y marcadores `[verificar]`.
- Recomendacion de escalacion si hay bloques en ROJO.

No enviar el borrador a ningun destino externo. No publicar. No archivar. La publicacion y el archivo son responsabilidad humana.

## Formato de salida

Estructura fija (no hay plantilla en `assets/` por convencion explicita del usuario):

1. Metadata
2. Hechos documentados (con veredicto por bloque)
3. Analisis / interpretacion (separado, si aplica)
4. Cronologia (si aplica)
5. Lista de fuentes (jerarquizada)
6. Issues y marcadores `[verificar]`
7. Recomendacion de escalacion (si hay ROJO)

Cada bloque factual lleva: afirmacion, fuente (autor / obra / anio / URL o localizador), veredicto.

## Escalacion

- **A humano (investigador responsable)**: si hay bloques en ROJO. Marcar `[verificar]` en el bloque y emitir recomendacion de escalacion en la seccion final del output. Gate humano obligatorio: el investigador decide si el bloque se publica, se reformula o se descarta.
- **A otro plugin**: si la consulta cae fuera del alcance (Paso 2), derivar a `general-assistant` con mensaje claro.
- **No aplica `io.gravitonai.tools.escalate_to_attorney`**: esa tool es para escalacion legal. Aqui la escalacion es a humano, sin tool automatica.

## Como NO se usa esta skill

- **No la invoques para historia de otros paises.** Aunque el periodo o el tema tenga lazos con Venezuela (ej: "la independencia de Colombia"), esta skill solo cubre el caso venezolano. Derivar a `general-assistant`.
- **No la invoques para eventos contemporaneos (< 50 anios)** salvo que el usuario justifique la inclusion. Para eventos muy recientes, usar fuentes de actualidad via `general-assistant`.
- **No la invoques para biografia de personas vivas.** Para perfiles de personas vivas, usar `general-assistant`.
- **No la invoques para emitir verdades historiograficas definitivas.** El output es borrador para revision humana, no publicacion academica.
- **No la invoques para preguntas factuales actuales** (ej: "quien es el presidente de Venezuela ahora"). Eso es trabajo de `general-assistant`.