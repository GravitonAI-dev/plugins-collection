---
name: arrendamiento-urbano
description: >
  Genera un contrato de arrendamiento urbano completo (vivienda habitual o local de negocio)
  entre arrendador y arrendatario, aplicando la Ley 29/1994 de Arrendamientos Urbanos (LAU)
  en su version consolidada vigente verificada en el BOE. Adapta las clausulas segun la
  naturaleza de las partes (persona fisica o juridica) y la ubicacion del inmueble.
  NO usar para arrendamientos de finca rustica, viviendas turisticas, contratos de temporada,
  viviendas militares, ni viviendas de porteros o guardas.
when_to_use: |
  - El usuario quiere redactar un contrato de alquiler de vivienda o local.
  - El usuario proporciona datos de arrendador, arrendatario e inmueble.
  - El usuario pide que el contrato cumpla con la LAU.
inputs:
  - tipo_inmueble: vivienda habitual o local de negocio / uso distinto de vivienda
  - naturaleza_arrendador: persona fisica o persona juridica
  - naturaleza_arrendatario: persona fisica o persona juridica
  - datos_arrendador: nombre o razon social, NIF o CIF, domicilio
  - datos_arrendatario: nombre o razon social, NIF o CIF, domicilio
  - datos_inmueble: direccion completa, referencia catastral, descripcion, comunidad autonoma, municipio
  - renta_mensual: importe en euros
  - duracion: anos pactados o "minimo legal"
  - fianza: mensualidades o "segun ley"
  - fecha_inicio: fecha de inicio del contrato
  - clausulas_adicionales: opcionales, a peticion del usuario
outputs:
  - contrato_arrendamiento: contrato completo en markdown, DRAFT, con todas las clausulas LAU
references:
  - references/lau-vivienda-plazos-renta-fianza.md
  - references/lau-derechos-obligaciones-partes.md
  - references/lau-arrendamiento-local-negocio.md
assets:
  - assets/contrato-arrendamiento-vivienda.md
  - assets/contrato-arrendamiento-local.md
---

# Generar Contrato de Arrendamiento

> DRAFT — para revision por un abogado antes de su firma. No constituye asesoramiento juridico.

## Guardrails

1. Verificar siempre la LAU en el BOE antes de redactar. Sin verificacion, no proceder. Si se detecta una version de la LAU posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver "Verificacion normativa"). No usar una version desactualizada.
2. Nunca incluir clausulas que perjudiquen al arrendatario en los derechos reconocidos por el Titulo II LAU (son nulas de pleno derecho — Art. 6).
3. Si el municipio es zona de mercado residencial tensionado, aplicar obligatoriamente las limitaciones de renta de los Art. 17.6 y 17.7 LAU y advertir al usuario.
4. Si el arrendador es persona juridica, la duracion minima es 7 anos (no 5). Nunca reducirla.
5. Nunca omitir la clausula de fianza. El importe minimo es imperativo (Art. 36 LAU).
6. Los gastos de gestion inmobiliaria y formalizacion del contrato son siempre a cargo del arrendador (Art. 20.1 LAU). No pueden pactarse a cargo del arrendatario.
7. Marcar todos los campos a rellenar con `[DATO]` en mayusculas. Nunca inventar datos.
8. Si el usuario pide clausulas que contradigan normas imperativas, rechazar y explicar el motivo.
9. La clasificacion del contrato (`tipo_inmueble`, `naturaleza_arrendador`, `naturaleza_arrendatario`) se resuelve en la Seccion 1 de la entrevista (ver Procedimiento), antes de generar cualquier borrador. No se asume un valor por defecto para estos tres campos ni se dejan como `[DATO — PENDIENTE DE COMPLETAR]`: son la primera pregunta natural de la conversacion, no una validacion con mensaje de error.
10. **Generación del Documento (Fase 2).** Tras recolectar los datos básicos y de clasificación (Secciones 1 a 3 de la Fase 1), el LLM DEBE invocar inmediatamente la herramienta `Write` cargando la plantilla correspondiente en el disco. No postergues la creación hasta el final de la entrevista. El ajuste detallado de cláusulas (Fase 3) se realiza iterando sobre el archivo ya escrito mediante la herramienta `Edit`.

## Procedimiento (Flujo en 3 Fases)

Este procedimiento se conduce como una entrevista dividida en tres grandes fases. Nunca se listan dos secciones a la vez ni se vuelca el formulario completo de golpe. La verificacion normativa, la validacion de condiciones y la generacion del contrato son acciones obligatorias que se disparan en los puntos indicados.

### Estado interno y regla de parada (evaluar ANTES de cada respuesta)

Antes de emitir cualquier respuesta, el LLM debe evaluar internamente:

1. ¿En qué paso y Fase de la entrevista me encuentro? (Fase 1: Clasificación; Fase 2: Creación Documento; Fase 3: Ajuste de Cláusulas; Realimentación).
2. ¿He recibido respuesta del usuario a la pregunta de la sección/paso actual?
3. ¿He invocado las herramientas (`Write`/`Edit`) si corresponde a la Fase actual?

Reglas duras:
- Formula únicamente la pregunta correspondiente a esa sección y detén la generación inmediatamente. Prohibido avanzar a la siguiente pregunta sin recibir la respuesta del usuario.
- En la Fase 3, tras acordar una cláusula, **DEBES invocar `Edit` para persistirla en disco antes de pasar a la siguiente cláusula.**

### Tabla de progreso

El LLM mantiene esta tabla de progreso actualizada en cada turno (la muestra al inicio de su respuesta o al pedir cada nueva sección) para que el usuario vea dónde está:

| # | Fase / Sección | Descripción | Estado |
|---|----------------|-------------|--------|
| 0 | F1 - Finalidad | Filtro de alcance (Pregunta 0) | Pendiente |
| 1 | F1 - Inmueble | Pregunta 1 | Pendiente |
| 2 | F1 - Arrendador | Pregunta 2 | Pendiente |
| 3 | F1 - Arrendatario| Pregunta 3 | Pendiente |
| 4 | F1 - Ubicación | Sección 2 (Datos iniciales) | Pendiente |
| 5 | F1 - Partes | Sección 3 (Datos iniciales) | Pendiente |
| 6 | F2 - Creación | Volcado de plantilla en disco (`Write`) | Pendiente |
| 7 | F3 - Cláusula 1 y 2 | Sección 4 (Objeto/Destino) | Pendiente |
| 8 | F3 - Cláusula 3 | Sección 5 (Duración) | Pendiente |
| 9 | F3 - Cláusula 4 | Sección 6 (Renta) | Pendiente |
| 10 | F3 - Cláusula 5 | Sección 7 (Actualización) | Pendiente |
| 11 | F3 - Cláusula 6 | Sección 8 (Fianza) | Pendiente |
| 12 | F3 - Cláusula 7 | Sección 9 (Gastos y suministros) | Pendiente |
| 13 | F3 - Adicionales | Sección 10 (Pactos opcionales) | Pendiente |
| 14 | Realimentación | Bucle post-entrega | Pendiente |

Estados posibles: `Pendiente`, `En curso`, `Confirmada`, `Omitida (modo rápido)`.

**Resumen operativo en 3 Fases:**
1. **Fase 1: Recorrer la entrevista inicial (Secciones 1 a 3):** Hacer UNA pregunta por turno, con confirmación explícita del usuario entre cada paso. Aquí determinamos las partes, la ubicación y el tipo de plantilla a usar.
2. **Fase 2: Creación del documento base:** Inmediatamente tras recolectar los datos de las Secciones 1 a 3, buscar y cargar el asset correspondiente (VIVIENDA o LOCAL), e invocar `Write` para crear el archivo en el disco reemplazando las variables básicas ya recopiladas.
3. **Fase 3: Ajuste por Secciones (Secciones 4 a 10):** Se recorren las cláusulas del documento ya existente en disco. Por cada cláusula, se pregunta al usuario los detalles técnicos, y con su confirmación se invoca `Edit` sobre el archivo en disco para persistir la cláusula.
4. **Bucle de realimentación:** Tras terminar la Fase 3, se abre el menú de ajustes generales.

### Entrevista (una seccion por turno)

**Seccion 1 — Clasificacion** (primera pregunta, antes de cualquier otra cosa)

Determina la plantilla, el titulo de la LAU aplicable, el plazo minimo y la fianza minima. Empieza con un filtro de alcance (Pregunta 0) antes de las tres preguntas de clasificacion.

**Consistencia obligatoria:** el arbol de decision (Pregunta 0, 1, 2 y 3, con su redaccion exacta y su orden) es fijo y no cambia de una conversacion a otra. Usar textualmente la redaccion de estas cuatro preguntas tal como aparece aqui abajo, sin parafrasear, sin generar una redaccion alternativa, sin anadir preguntas nuevas ni reordenarlas. Si en algun momento se detecta que se esta a punto de formular estas preguntas de otra manera, releer esta seccion y usar el texto literal.

**Nota de implementacion (ConfidentialAI):** este `SKILL.md` es la especificacion de referencia y la unica fuente de verdad del arbol de decision. El backend de produccion de ConfidentialAI (repo `GravitonAI-dev/GPT`) no lee este archivo directamente hoy: tiene su propio sistema de "user intents" (`descriptions.json`, `system_roles.json`, `system_directives.json`, `chains_of_thought.json`) que no conoce esta skill. Para que el arbol de decision de esta seccion (Pregunta 0-3) llegue realmente al modelo en produccion, quien integre esta skill en ese backend debe copiar el texto literal de las Pregunta 0-3 (tal cual aparece aqui abajo, sin parafrasear) dentro de las instrucciones de esa intencion. Mientras esa integracion no exista, este documento sirve como especificacion para cualquier orquestador (Claude Code, Claude Agent SDK, u otro) que sí cargue y seleccione esta skill directamente.

**Pregunta 0 — Finalidad del uso (filtro de alcance, se pregunta primero):**

TEXTO EXACTO A USAR (copiar literalmente, sin modificar ni una palabra):
"¿El uso previsto del inmueble es continuado y permanente en el tiempo, o es de temporada (vacacional, de verano, por trabajo temporal) o se trata de una vivienda turistica gestionada como alojamiento?"

Espera la respuesta del usuario. No continues a la Pregunta 1 ni a ninguna otra cosa hasta recibirla.

```
  ├─ Habitual / permanente (vivienda o negocio estable) → continuar con la Pregunta 1
  └─ Temporada / vacacional / turistica                 → FUERA DE ALCANCE de esta skill
       • Temporada (Art. 3.2 LAU): arrendamiento para uso distinto de vivienda por
         temporada (de verano o cualquier otra) — regimen de libertad de pactos,
         sin plazo minimo de 5/7 anos ni el resto de protecciones del Titulo II.
       • Vivienda turistica (Art. 5.e LAU): excluida expresamente de la LAU;
         se rige por la normativa turistica de la comunidad autonoma correspondiente.
       Detener el procedimiento aqui: explicar al usuario que esta skill no cubre
       este tipo de arrendamiento (ver "Como NO se usa esta skill") y no continuar
       con las Secciones 2-10 ni generar ningun borrador.
```

**Regla anti-suposicion:** una respuesta a otra pregunta nunca resuelve la Pregunta 0. Por ejemplo, si el usuario dice "es para vivienda" antes de que se le haya preguntado la Pregunta 0, eso responde (como mucho) a la Pregunta 1 (tipo de inmueble), pero NO dice si es habitual/permanente o de temporada/turistica — no asumir "habitual" a partir de eso. Si la respuesta de un turno no distingue con claridad entre las opciones de la pregunta que se esta resolviendo en ese momento, repetir la misma pregunta (texto literal) pidiendo que se aclare esa distincion especifica, en vez de asumir una opcion.

Solo si la respuesta es "habitual / permanente", continuar con las tres preguntas de clasificacion, **una por turno, esperando la respuesta antes de pasar a la siguiente**:

**Pregunta 1 — Tipo de inmueble:**
TEXTO EXACTO A USAR (copiar literalmente, sin modificar ni una palabra):
"Perfecto. ¿El inmueble que se va a arrendar es una vivienda (cualquier tipo: piso, casa, chalet, apartamento) o un local de negocio / espacio para uso distinto de vivienda?"

Espera la respuesta del usuario. No continues a la Pregunta 2 ni a ninguna otra cosa hasta recibirla.

| Respuesta | Efecto |
|---|---|
| Vivienda habitual | `tipo_inmueble = VIVIENDA` · Titulo II LAU · plantilla `contrato-arrendamiento-vivienda.md` · fianza minima 1 mensualidad |
| Local de negocio | `tipo_inmueble = LOCAL` · Titulo III LAU · plantilla `contrato-arrendamiento-local.md` · fianza minima 2 mensualidades |

**Pregunta 2 — Naturaleza del arrendador** (se pregunta tras recibir la respuesta a la Pregunta 1):
TEXTO EXACTO A USAR (copiar literalmente, sin modificar ni una palabra):
"¿El arrendador es persona fisica o persona juridica (empresa, sociedad)?"

Espera la respuesta del usuario. No continues a la Pregunta 3 ni a ninguna otra cosa hasta recibirla.

| Respuesta | Efecto |
|---|---|
| Persona fisica | `naturaleza_arrendador = FISICA` · duracion minima 5 anos (Art. 9.1 LAU) |
| Persona juridica | `naturaleza_arrendador = JURIDICA` · duracion minima 7 anos (Art. 9.1 LAU) |

**Pregunta 3 — Naturaleza del arrendatario** (se pregunta tras recibir la respuesta a la Pregunta 2):
TEXTO EXACTO A USAR (copiar literalmente, sin modificar ni una palabra):
"¿Y el arrendatario, es persona fisica o persona juridica?"

Espera la respuesta del usuario. No continues a la Seccion 2 ni a generar ningun borrador hasta recibirla.

| Respuesta | Efecto |
|---|---|
| Persona fisica | `naturaleza_arrendatario = FISICA` |
| Persona juridica | `naturaleza_arrendatario = JURIDICA` |

**Alcance de la Seccion 1 — solo estas cuatro preguntas (0-3), una por turno:**
- Cada pregunta (0, 1, 2, 3) va en su propio mensaje. Nunca combinar dos o mas preguntas de esta lista en el mismo turno, ni presentar el arbol completo de una vez: se avanza pregunta a pregunta, tomando cada decision antes de pasar a la siguiente.
- **Nunca mezclar preguntas de la Seccion 1 con datos de relleno del contrato (Secciones 2-10).** Por ejemplo, "Datos de las partes: nombre completo y DNI/NIF/NIE del arrendador, del arrendatario, domicilio de notificacion de cada parte" es contenido de la Seccion 3 (Partes) — un dato de relleno, no de clasificacion — y no debe aparecer en el mismo mensaje que la Pregunta 0, 1, 2 o 3, ni antes de que la Seccion 1 este resuelta por completo. Son dos categorias distintas de pregunta (ver Guardrail 9 y 10) y nunca comparten turno.
- No preguntar por jurisdiccion, pais, ciudad o provincia como parte de la clasificacion: esta skill aplica exclusivamente a Espana y a la LAU (Ley 29/1994), segun el `CLAUDE.md` del plugin `derecho-civil`. Si el usuario indica que el inmueble esta fuera de Espana, esta skill no aplica; indicarlo y no continuar con el procedimiento.
- No preguntar por el regimen registral del bien (titularidad inscrita, cargas, hipotecas, propiedad horizontal, embargos): esta skill genera el contrato de arrendamiento, no realiza due diligence de titularidad. No forma parte de la clasificacion ni de ningun otro paso de este procedimiento.
- No sustituir ni ampliar estas cuatro preguntas por otras. Si el usuario aporta datos adicionales por su cuenta, se pueden anotar como clausula adicional (Seccion 10), pero no se preguntan de forma proactiva aqui.
- Si el usuario responde varias preguntas a la vez de forma espontanea (por ejemplo, en su primer mensaje), aceptarlas e integrarlas igualmente; solo preguntar por las que sigan sin respuesta.

Esperar las cuatro respuestas antes de continuar: sin ellas no hay plantilla ni marco legal que aplicar, asi que no se genera ningun borrador ni se avanza a la Seccion 2 hasta tenerlas completas. No es un bloqueo formal con mensaje de error — es, simplemente, el orden natural de la entrevista, pregunta a pregunta.

**Ejemplo de respuesta CORRECTA para el primer turno** (usuario dice "quiero un contrato de alquiler"):

```
¿El arrendamiento es para residencia habitual y permanente o para una actividad
de negocio estable, o es de temporada (vacacional, de verano, por trabajo
temporal) o una vivienda turistica gestionada como alojamiento?
```

Y ahi termina la respuesta. Nada mas.

**Ejemplo de respuesta INCORRECTA para ese mismo turno** (no hacer esto — patron real observado y prohibido):

```
Antes de ayudarle, necesito que me indique varios puntos:
1. Su posicion en la operacion: ¿arrendador o arrendatario?
2. Naturaleza del inmueble: ¿vivienda, local, oficina, garaje, finca rustica?
3. Jurisdiccion: ¿en que pais/ciudad esta el inmueble?
4. Finalidad: ¿quiere un contrato, una revision, o asesoramiento?
```

Esto esta mal por multiples motivos a la vez: mezcla varias preguntas en un solo
turno, ninguna de las 4 preguntas coincide con el texto literal de la Seccion 1,
pregunta por jurisdiccion (prohibido), y pregunta por cosas fuera del alcance de
esta skill (posicion en la operacion, tipo de servicio). Antes de enviar
cualquier respuesta en la Seccion 1, verificar que contiene EXACTAMENTE una de
las cuatro preguntas (0, 1, 2 o 3) con su texto literal, y nada mas. Si la
respuesta que se esta a punto de enviar contiene mas de una pregunta, o una
pregunta que no aparece textualmente arriba, no enviarla: corregirla primero.

En cuanto el usuario responda, ejecutar la Verificacion normativa (mas abajo) antes de continuar con la Seccion 2.

**Las Secciones 2-10 estan alineadas 1:1 con las clausulas del contrato** (ver "Estructura de clausulas" en "Generacion del contrato"), en el mismo orden en que aparecen en la plantilla. Esto permite ir rellenando el documento clausula por clausula conforme avanza la entrevista, no por bloques tematicos sueltos.

**Seccion 2 — Ubicacion** (contexto previo al encabezado y a REUNIDOS)

"¿En que comunidad autonoma y municipio esta el inmueble? ¿Sabes si el municipio esta declarado zona de mercado residencial tensionado? (si / no / no lo se)"

Si responde "no lo se": invocar `web_search("zona mercado residencial tensionado [municipio] [comunidad autonoma]")` y comunicar el resultado.

Si la comunidad autonoma tiene normativa propia relevante (Cataluna, Pais Vasco, Navarra, Madrid zona tensionada, etc.), ejecutar la Consulta de normativa autonomica (mas abajo) antes de continuar con la Seccion 3.

**Seccion 3 — Partes** (bloque REUNIDOS)

"Datos del arrendador: nombre completo o razon social, NIF/CIF, y domicilio a efectos de notificaciones. Datos del arrendatario: nombre completo o razon social, NIF/CIF, y domicilio actual."

**Seccion 4 — Clausula PRIMERA (Objeto) y SEGUNDA (Destino)**

"Direccion completa del inmueble (calle, numero, piso, puerta, codigo postal, municipio). Referencia catastral, si se dispone de ella. Descripcion: superficie util aproximada y numero de habitaciones (vivienda), o descripcion del local (uso distinto). ¿Incluye elementos accesorios como plaza de garaje, trastero o mobiliario?" Si `tipo_inmueble = LOCAL`, anadir: "¿Que actividad se va a desarrollar en el local?" (rellena la clausula SEGUNDA — Destino y actividad; en vivienda, la Segunda es boilerplate fijo y no necesita pregunta).

**Seccion 5 — Clausula TERCERA (Duracion)**

"Duracion del contrato en anos, o 'minimo legal'. Fecha de inicio del contrato."

**Seccion 6 — Clausula CUARTA (Renta)**

"Renta mensual pactada, en euros. Forma de pago (transferencia, domiciliacion, otro) y cuenta/IBAN del arrendador."

**Seccion 7 — Clausula QUINTA (Actualizacion de la renta)**

"Actualizacion de renta: indice pactado, o 'segun ley' (IGC con tope IPC)."

**Seccion 8 — Clausula SEXTA (Fianza)**

"Fianza: numero de mensualidades, o 'segun ley'. ¿Se pacta alguna garantia adicional (aval bancario, seguro de impago, deposito adicional)?"

**Seccion 9 — Clausula SEPTIMA (Gastos y suministros)**

"¿Algun gasto a cargo del arrendatario (comunidad, IBI, seguro del edificio)? Los suministros individualizados (agua, luz, gas) son siempre a cargo del arrendatario segun la plantilla — confirmar si aplica alguna excepcion."

**Seccion 10 — Pactos opcionales y clausulas adicionales** (Clausula DECIMA, Notificaciones, Fuero, y Clausulas Adicionales)

"¿Se renuncia al derecho de adquisicion preferente (Art. 25 LAU), o se mantiene? ¿Correos electronicos de las partes para notificaciones, si se desea anadirlos ademas del domicilio? ¿Se pacta mediacion o arbitraje antes de la via judicial? ¿Alguna clausula adicional que quieras incluir?"

**Como conducir la entrevista:**
- Una seccion por mensaje, en el orden 2→10. Esperar la respuesta antes de pasar a la siguiente seccion. Dentro de una misma seccion sí se pueden agrupar varias preguntas en el mismo mensaje — son datos de la misma clausula. Esto es distinto de la Seccion 1 (arbol de decision), donde cada pregunta va sola, sin excepcion (ver Seccion 1), y nunca se mezcla con estas (ver "Alcance de la Seccion 1").
- Mostrar el titulo de la seccion como encabezado del mensaje al usuario (p. ej. "**Seccion 4 — Clausula PRIMERA (Objeto)**") antes de la pregunta correspondiente, para que pueda seguir el progreso de la entrevista clausula por clausula. La vista previa de la cláusula rellenada se muestra justo debajo de la pregunta, en texto plano formateado (sin bloques de código), seguida de la pregunta de confirmación "¿Confirmamos esta cláusula y avanzamos a la siguiente?".
- Si el usuario aporta espontaneamente datos de varias secciones a la vez (por ejemplo, en su primer mensaje), aceptarlos e integrarlos igualmente; solo preguntar por las secciones que sigan incompletas. Si el usuario aporta datos de varias secciones ANTES de que se haya resuelto la Sección 1, las Preguntas 0-3 siguen siendo obligatorias una a una (no se mezclan con datos de relleno; ver "Alcance de la Seccion 1").
- NO se genera ni se modifica ningun archivo en disco durante la Fase 1. La generacion del documento base ocurre UNA SOLA VEZ al inicio de la Fase 2, tras recopilar los datos básicos (Secciones 1 a 3). Luego, las modificaciones se aplican en vivo sobre el disco en la Fase 3 mediante `Edit` (ver "Generación del contrato base (Fase 2)").

**Patron completo de un turno de las Secciones 2-10 (ejemplo, Seccion 4):**

> **Seccion 4 — Clausula PRIMERA (Objeto) y SEGUNDA (Destino)**
>
> Direccion completa del inmueble (calle, numero, piso, puerta, codigo postal, municipio). Referencia catastral, si se dispone de ella. Descripcion: superficie util aproximada y numero de habitaciones (vivienda), o descripcion del local (uso distinto). ¿Incluye elementos accesorios como plaza de garaje, trastero o mobiliario?
>
> --- Vista previa aplicada (todavia no se ha escrito en disco) ---
>
> PRIMERA — Objeto del arrendamiento
> La parte arrendadora cede en arrendamiento a la parte arrendataria la vivienda situada en [DIRECCION], con superficie util aproximada de [X] m² y [Y] habitaciones, Referencia Catastral [REF]. Incluye: plaza de garaje nº [X], trastero nº [Y].
>
> SEGUNDA — Destino
> La vivienda se destina a residencia habitual y permanente de la parte arrendataria y su unidad familiar, quedando prohibida cualquier otra utilizacion.
>
> --- Fin de la vista previa ---
>
> ¿Confirmamos esta clausula y avanzamos a la siguiente seccion?

Tras la confirmacion explicita del usuario (por ejemplo, "OK", "confirmado", "perfecto", "adelante"), marcar la seccion como `Confirmada` en la Tabla de progreso, formular la siguiente pregunta (Seccion 5) y detenerse hasta recibir su respuesta.

**Manejo de interrupciones (compatible con la regla global del `CLAUDE.md`):**
- Si el usuario pausa, hace una pregunta lateral, o aporta datos de varias secciones a la vez, registra lo recibido, responde brevemente a su pregunta o dato, y luego retoma la seccion pendiente sin perder el progreso.
- Si el usuario quiere volver a una seccion anterior, retrocede sin perder lo avanzado: actualiza la Tabla de progreso para reflejar que esa seccion vuelve a estar `En curso` y vuelve a preguntarla (o confirma el cambio si solo quiere ajustar un dato).
- Si el usuario dice "saltemos gates", "avanza con defaults" o equivalente, omite las confirmaciones intermedias y solo confirma al cierre de la entrevista ("¿Procedemos a la redaccion?"); ademas, aplica los defaults del `CLAUDE.md` del plugin para los datos que el usuario no haya especificado (duracion minima legal, fianza minima legal, indice IGC, gastos a cargo del arrendador, etc.). Documenta en el chat que se ha activado el modo rapido y marca las secciones afectadas como `Omitida (modo rápido)` en la Tabla de progreso.
- Si el usuario dice "cancela", "olvida lo anterior" o equivalente, descarta el progreso de la entrevista (todas las secciones vuelven a `Pendiente`) y vuelve a la Pregunta 0.

### Verificacion normativa (disparada tras la Seccion 1; accion interna, no es una pregunta al usuario)

La skill se actualiza a si misma en cada lanzamiento: comprueba la LAU en la fuente oficial y, si detecta una version posterior, reescribe sus propias references antes de redactar. Ejecutar SIEMPRE esta secuencia:

a) **Leer la version registrada localmente.** Las references indican la ultima modificacion conocida (25/05/2023, Ley 12/2023). Anotar esa fecha como referencia de comparacion.

b) **Consultar la fuente oficial vigente.** Invocar:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003&p=20230525&tn=1",
  format: "text"
)
```
Extraer: fecha de ultima modificacion del texto consolidado; articulos modificados respecto a la version registrada; version verificada para el encabezado del contrato.

c) **Comparar.** Contrastar la fecha/redaccion oficial con la registrada en las references.

d) **Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la fecha oficial es posterior o cambia la redaccion de articulos aplicados, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/lau-vivienda-plazos-renta-fianza.md`, `references/lau-derechos-obligaciones-partes.md` y/o `references/lau-arrendamiento-local-negocio.md` con la redaccion vigente.
- Actualizar la nota de "ultima modificacion conocida" en el encabezado de esas references con la nueva fecha.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente de la LAU (fecha y articulos).

No redactar el contrato hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

e) **Fallback si la fuente no es accesible.** Si read_document falla (error HTTP, timeout):
```
web_search("Ley 29/1994 Arrendamientos Urbanos texto consolidado BOE ultima modificacion")
```
Si ambos fallan: usar references como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LAU en el BOE. El contrato se genera con la version de referencia (25/05/2023). Verificar manualmente antes de firmar."

### Validacion de condiciones (interna, conforme avanza la entrevista)

a) **Duracion minima:**
   - Arrendador persona fisica: minimo 5 anos (Art. 9.1 LAU). Si el usuario pacta menos, aplicar prorroga obligatoria hasta 5 anos y advertir.
   - Arrendador persona juridica: minimo 7 anos (Art. 9.1 LAU). Si el usuario pacta menos, aplicar prorroga obligatoria hasta 7 anos y advertir.

b) **Fianza minima:**
   - Vivienda: 1 mensualidad (Art. 36.1 LAU).
   - Uso distinto: 2 mensualidades (Art. 36.1 LAU).
   - Si el usuario pacta menos, corregir al minimo legal y advertir.

c) **Zona tensionada:**
   - Si el municipio es zona tensionada: la renta no puede superar la ultima renta del contrato anterior en la misma vivienda (si existe) ni el indice de referencia de precios (Art. 17.6 LAU). Advertir y pedir confirmacion al usuario.

d) **Clausulas adicionales solicitadas:**
   - Verificar que no contradigan normas imperativas del Titulo II (vivienda) o Titulo III (local) LAU.
   - Si alguna es nula, rechazarla, explicar el motivo citando el articulo, y proponer alternativa valida.

### Consulta de normativa autonomica (disparada tras la Seccion 2, si aplica)

Si el usuario menciona una comunidad autonoma con normativa propia relevante (Cataluna, Pais Vasco, Navarra, Madrid zona tensionada, etc.):

```
web_search("deposito fianza arrendamiento [comunidad autonoma] organismo competente 2024")
```

Incluir en el contrato la clausula de deposito de fianza ante el organismo autonomico correspondiente.

### Generación del contrato base (Fase 2)

La generacion del documento ocurre inmediatamente tras confirmar la Sección 3 (Datos de las partes). Durante esta fase (Secciones 1 a 3) NO se escribe ni se modifica ningún archivo. Una vez completadas esas 3 secciones iniciales, se procede a crear el archivo base. 

Seleccionar la plantilla segun `tipo_inmueble` (Seccion 1, ya resuelta al llegar aqui):
- Vivienda: `assets/contrato-arrendamiento-vivienda.md`
- Local de negocio: `assets/contrato-arrendamiento-local.md`

**Estructura de clausulas del contrato (numeracion ordinal femenina: PRIMERA, SEGUNDA, TERCERA...).** Esta es la estructura obligatoria del documento final, tal como esta en las plantillas de `assets/`. Si por cualquier motivo no se tiene acceso al archivo de la plantilla, usar esta lista igualmente — es la fuente de verdad de que clausulas debe tener el contrato y en que orden:

Para `tipo_inmueble = VIVIENDA` (`contrato-arrendamiento-vivienda.md`):
PRIMERA — Objeto del arrendamiento · SEGUNDA — Destino · TERCERA — Duracion · CUARTA — Renta · QUINTA — Actualizacion de la renta · SEXTA — Fianza · SEPTIMA — Gastos y suministros · OCTAVA — Conservacion y obras · NOVENA — Cesion y subarriendo · DECIMA — Derecho de adquisicion preferente · DECIMOPRIMERA — Resolucion del contrato · DECIMOSEGUNDA — Notificaciones · DECIMOTERCERA — Fuero y legislacion aplicable.

Para `tipo_inmueble = LOCAL` (`contrato-arrendamiento-local.md`):
PRIMERA — Objeto del arrendamiento · SEGUNDA — Destino y actividad · TERCERA — Duracion · CUARTA — Renta · QUINTA — Actualizacion de la renta · SEXTA — Fianza · SEPTIMA — Gastos, tributos y suministros · OCTAVA — Obras · NOVENA — Cesion y subarriendo · DECIMA — Derecho de adquisicion preferente · DECIMOPRIMERA — Indemnizacion al arrendatario por extincion del contrato · DECIMOSEGUNDA — Resolucion del contrato · DECIMOTERCERA — Notificaciones · DECIMOCUARTA — Fuero y legislacion aplicable.

Ambas plantillas incluyen ademas, antes de las clausulas: encabezado con DRAFT y fecha de verificacion LAU, y bloque REUNIDOS/EXPONEN con la identificacion de las partes; y despues de las clausulas: CLAUSULAS ADICIONALES, FIRMAS, y (solo vivienda) INVENTARIO DE MOBILIARIO Y ENSERES si aplica. No inventar una estructura de clausulas distinta ni renombrar los encabezados.

**Es una plantilla de sustitucion literal, no un texto para redactar de nuevo cada vez.** El archivo de `assets/` correspondiente (`contrato-arrendamiento-vivienda.md` o `contrato-arrendamiento-local.md`) se usa como un documento de mail-merge: se copia su texto fijo tal cual, caracter por caracter, y unicamente se sustituyen los marcadores `{{variable}}` por los datos reales confirmados en la entrevista. Las frases legales de cada clausula (los parrafos que no son un marcador) nunca se reescriben, resumen, reordenan ni parafrasean — son iguales en todos los contratos generados por esta skill, cambien lo que cambien los datos del cliente. Los bloques marcados como condicionales en la plantilla (p. ej. `<!-- Si zona tensionada: ... -->`, `<!-- Si duracion < minimo legal, insertar: ... -->`) se incluyen o se omiten segun corresponda al caso, pero si se incluyen, su texto tambien se copia literalmente, sin modificarlo. El resultado: dos contratos para el mismo `tipo_inmueble` deben ser identicos salvo en los valores concretos sustituidos.

**Pasos de la generacion del Documento Base:**
1. Invocar `Read(assets/contrato-arrendamiento-vivienda.md)` o `Read(assets/contrato-arrendamiento-local.md)`, segun `tipo_inmueble`. Este paso es obligatorio y no puede omitirse: sin el contenido real del archivo delante, no hay texto literal que sustituir.
2. Sustituir en memoria (mentalmente) todos los `{{variable}}` correspondientes a la Fase 1 (datos básicos) bloque por bloque, conservando el texto fijo de las clausulas. Para las cláusulas que aún no se han abordado (Fase 3), mantenlas temporalmente en blanco o con sus marcadores `[DATO]`.
3. Crear el archivo del contrato en el disco con `Write`, usando `snake_case` como nomenclatura (ej. `contrato_arrendamiento_vivienda_calle_mayor_123.md`) y conservando el header DRAFT y la fecha de verificacion LAU.
4. Confirmar en el chat la creacion del archivo, y avisar que ahora procederas a rellenar los detalles tecnicos (cláusulas, Fase 3).

**Fase 3 (Edición iterativa).** Después de este punto, por cada sección restante, formularás la pregunta al usuario. Tras su confirmación, usarás `Edit` para actualizar específicamente la cláusula correspondiente en el disco, confirmándolo en el chat.

### Revision final tras completar la Fase 3

Se ejecuta cuando el usuario pide el documento o da por terminada la entrevista. Verificar que el contrato generado:
- Tiene el header DRAFT.
- Incluye la fecha de la Verificacion normativa.
- Tiene todas las clausulas obligatorias segun el tipo de inmueble.
- No contiene clausulas nulas.
- Todos los importes son coherentes entre si (renta, fianza, actualizacion) — los que esten disponibles; los pendientes quedan como `[DATO — PENDIENTE DE COMPLETAR]`.
- Los plazos son conformes a la LAU.

### Advertencias finales

Una vez concluido el proceso, añadir en el chat:

```
Advertencias:
1. Este contrato es un DRAFT generado automaticamente. Debe ser revisado por un abogado colegiado antes de su firma.
2. Version de la LAU verificada: [fecha extraida en la Verificacion normativa].
3. Si el inmueble se ubica en zona de mercado residencial tensionado, verificar la aplicacion de los limites de renta antes de firmar.
4. El deposito de fianza ante el organismo autonomico competente es obligatorio. Consultar el procedimiento en [comunidad autonoma].
5. Se recomienda la inscripcion del contrato en el Registro de la Propiedad para mayor seguridad juridica (Art. 37 LAU).
```

## Bucle de realimentación post-entrega

Tras completar la Fase 3, el LLM NO da por terminada la conversacion. Entra en el bucle de realimentacion (fila 14 de la Tabla) en el que ofrece al usuario un menu explicito de ajustes y permanece a la espera hasta que el usuario cierre la conversacion o indique que el contrato esta conforme.

**Mensaje de apertura del bucle** (justo despues de la entrega del contrato en el chat, junto a la confirmacion de `Write`):

---

Contrato entregado en `[nombre_del_archivo.extension]`.

¿Que quieres hacer ahora?

1. Ajustar una clausula existente (indicame cual y que cambio quieres aplicar).
2. Añadir una clausula adicional (indicame el contenido que quieras incorporar).
3. Eliminar una clausula opcional (indicame cual).
4. Corregir un dato de las partes o del inmueble (indicame el dato y el valor correcto).
5. Regenerar el contrato completo desde una seccion concreta (indicame desde cual).
6. Revisar la verificacion normativa de la LAU (volver a comprobar la version vigente en el BOE).
7. Cerrar y dar el contrato por bueno.

---

**Reglas del bucle:**
- El LLM permanece en este estado hasta que el usuario elija la opcion 7 ("Cerrar y dar el contrato por bueno") o abandone la conversacion. Cualquier otra opcion del menu, cualquier pregunta lateral o cualquier dato nuevo aportado por el usuario se trata como una iteracion del bucle.
- Si el usuario elige cualquiera de las opciones 1-6, el LLM aplica el ajuste con el mismo patron gate explicito: recoge los datos o la indicacion correspondiente, muestra la vista previa del cambio en texto plano, pregunta "¿Confirmamos?", y tras la confirmacion aplica la modificacion al archivo en disco con `Edit` y confirma la operacion en el chat.
- Si el ajuste afecta a un dato de clasificacion (Sección 1: tipo de inmueble, naturaleza de las partes, finalidad), el LLM advierte al usuario que eso puede requerir regenerar el documento desde la plantilla correspondiente (VIVIENDA o LOCAL) y le ofrece esa opcion en el menu.
- Si el usuario hace una pregunta lateral o solicita una revision tecnica (por ejemplo, "esta clausula respeta el Art. 17 LAU?"), el LLM responde a la pregunta con su analisis tecnico y, tras responder, vuelve a mostrar el menu del bucle.
- Si el usuario aporta datos nuevos que no estaban en el contrato original, se tratan como ajuste del dato correspondiente (opcion 4 del menu): se les pide confirmacion, se aplica con `Edit` y se confirma en el chat.
- En cada iteracion del bucle, el LLM actualiza la Tabla de progreso añadiendo una linea "Ajuste realizado: [resumen]" como registro visible de las modificaciones aplicadas.
- La regla global de "interrupciones y cambios de direccion" del `CLAUDE.md` aplica tambien dentro de este bucle: el usuario puede mezclar varias solicitudes en un mismo turno y el LLM las procesa todas antes de volver a mostrar el menu.

**Como NO se aplica este bucle:**
- El bucle NO se usa para revisar contratos generados por terceros; esa funcionalidad no entra en el alcance de esta skill (ver "Limitaciones" en el `CLAUDE.md` del plugin).
- El bucle NO se usa para reabrir la entrevista desde cero. Si el usuario quiere rehacer, debe decirlo explicitamente ("empezar de nuevo", "rehacer el contrato", "volver a la pregunta 0"); en ese caso, el LLM reinicia la Tabla de progreso (todas las filas vuelven a `Pendiente`) y vuelve a la Pregunta 0 de la Sección 1.

## Como NO se usa esta skill

- No usar para revisar contratos existentes de terceros.
- No usar para contratos de temporada o viviendas turisticas (filtrado en la Pregunta 0 de la Seccion 1).
- No usar para arrendamientos de finca rustica.
- No usar si el usuario solicita opinion juridica sobre un litigio: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| Litigio activo o previo entre las partes | Escalar via escalate_to_attorney |
| Clausulas que no pueden resolverse con la LAU | Escalar via escalate_to_attorney |
| Arrendatario en situacion de vulnerabilidad acreditada | Advertir y ofrecer escalacion |
| Duda sobre zona tensionada que no resuelve web_search | Advertir y recomendar consulta al ayuntamiento |
| Pregunta 0 revela arrendamiento de temporada o vivienda turistica | Detener el procedimiento, explicar la exclusion (Art. 3.2 o Art. 5.e LAU) y no generar el contrato |
