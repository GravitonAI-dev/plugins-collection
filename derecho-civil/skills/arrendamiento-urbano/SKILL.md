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
10. **Generación diferida del documento hasta el cierre completo de la entrevista.** El documento final no debe generarse, ni se debe invocar la herramienta `draft_markdown` ni crear/modificar archivo alguno en el disco, hasta que las Secciones 1 a 10 hayan sido consultadas individualmente y el usuario haya dado su confirmación explícita para proceder a la redacción. Hasta ese momento, ninguna acción de escritura sobre el entregable puede ejecutarse, ni siquiera con datos genéricos ni con marcadores `[DATO — PENDIENTE DE COMPLETAR]`. Esta regla prevalece sobre la lógica de "generación progresiva" o "mail-merge desde la Sección 1" descrita en otros apartados del propio SKILL.md.

## Procedimiento

Este procedimiento se conduce como una entrevista: se presenta una seccion, se espera la respuesta del usuario, y solo entonces se pasa a la siguiente. Nunca se listan dos secciones a la vez ni se vuelca el formulario completo de golpe. La verificacion normativa, la validacion de condiciones y la generacion del contrato son acciones internas que se disparan en los puntos indicados — no son preguntas adicionales al usuario.

### Estado interno y regla de parada (evaluar ANTES de cada respuesta)

Antes de emitir cualquier respuesta, el LLM debe evaluar internamente:

1. ¿En qué paso de la entrevista me encuentro? (Pre-entrevista; Sección 1 con Preguntas 0-3; Sección 2; ...; Sección 10; Cierre de entrevista; Generación; Realimentación).
2. ¿He recibido respuesta del usuario a la pregunta de la sección/paso actual?
3. ¿He obtenido confirmación explícita del usuario para avanzar al siguiente paso?

Reglas duras:
- Determina en qué sección de la entrevista te encuentras. Formula únicamente la pregunta correspondiente a esa sección y detén la generación inmediatamente. Prohibido avanzar a la siguiente sección sin recibir la respuesta del usuario.
- Si la pregunta ha sido respondida pero no he recibido confirmación explícita para avanzar, mostrar la vista previa del cambio aplicado a la cláusula correspondiente y preguntar "¿Confirmamos esta cláusula y avanzamos a la siguiente?". Detenerse hasta recibir OK.
- Si he recibido respuesta y confirmación, marcar la sección como completada en la Tabla de progreso, actualizar la sección actual a la siguiente y formular la siguiente pregunta.
- Solo después de que la Sección 10 haya sido confirmada, preguntar al usuario si procede a la redacción final. Hasta que el usuario dé su OK explícito a esa pregunta final, no se carga ningún asset, no se invoca `draft_markdown`, no se crea ni se modifica ningún archivo en el disco.

### Tabla de progreso

El LLM mantiene esta tabla de progreso actualizada en cada turno (la muestra al inicio de su respuesta o al pedir cada nueva sección) para que el usuario vea dónde está:

| # | Sección | Descripción | Estado |
|---|---------|-------------|--------|
| 0 | Finalidad del uso | Filtro de alcance (Pregunta 0) | Pendiente |
| 1 | Tipo de inmueble | Pregunta 1 | Pendiente |
| 2 | Naturaleza del arrendador | Pregunta 2 | Pendiente |
| 3 | Naturaleza del arrendatario | Pregunta 3 | Pendiente |
| 4 | Ubicación y zona tensionada | Sección 2 | Pendiente |
| 5 | Datos de las partes | Sección 3 | Pendiente |
| 6 | Cláusulas PRIMERA y SEGUNDA (Objeto/Destino) | Sección 4 | Pendiente |
| 7 | Cláusula TERCERA (Duración) | Sección 5 | Pendiente |
| 8 | Cláusula CUARTA (Renta) | Sección 6 | Pendiente |
| 9 | Cláusula QUINTA (Actualización) | Sección 7 | Pendiente |
| 10 | Cláusula SEXTA (Fianza) | Sección 8 | Pendiente |
| 11 | Cláusula SÉPTIMA (Gastos y suministros) | Sección 9 | Pendiente |
| 12 | Pactos opcionales y cláusulas adicionales | Sección 10 | Pendiente |
| 13 | Cierre de entrevista | OK de redacción | Pendiente |
| 14 | Redacción y entrega | Generación del documento | Pendiente |
| 15 | Realimentación | Bucle post-entrega | Pendiente |

Estados posibles: `Pendiente`, `En curso`, `Confirmada`, `Omitida (modo rápido)`.

**Resumen operativo en 5 pasos (en este orden, sin saltarse ninguno):**
1. **Recorrer la entrevista** (Secciones 1-10, que cubren las filas 0-12 de la Tabla de progreso) — una sección por turno, con confirmación explícita del usuario entre cada paso. Ningún archivo se crea ni se modifica en el disco durante este recorrido.
2. **Confirmación final de cierre de entrevista** (fila 13 de la Tabla) — tras la Sección 10, preguntar al usuario "¿Procedemos a la redacción del contrato?" y esperar OK explícito. Sin ese OK, no avanzar.
3. **Buscar y cargar el asset** — solo tras el OK del paso 2. Leer (Read) el archivo de plantilla correspondiente al `tipo_inmueble` ya resuelto (`assets/contrato-arrendamiento-vivienda.md` para VIVIENDA, `assets/contrato-arrendamiento-local.md` para LOCAL). Nunca redactar el contrato de memoria: hay que tener el texto literal delante para poder copiarlo.
4. **Generar el documento** (fila 14 de la Tabla) — sustituir los `{{variable}}` del asset por los datos confirmados en las Secciones 1-10 y crear el archivo del contrato en el disco (Write). Es una sola operación al cierre, no progresiva.
5. **Bucle de realimentación** (fila 15 de la Tabla) — tras la entrega, abrir el menú de ajustes (ver "Bucle de realimentación post-entrega").

### Entrevista (una seccion por turno)

**Seccion 1 — Clasificacion** (primera pregunta, antes de cualquier otra cosa)

Determina la plantilla, el titulo de la LAU aplicable, el plazo minimo y la fianza minima. Empieza con un filtro de alcance (Pregunta 0) antes de las tres preguntas de clasificacion.

**Consistencia obligatoria:** el arbol de decision (Pregunta 0, 1, 2 y 3, con su redaccion exacta y su orden) es fijo y no cambia de una conversacion a otra. Usar textualmente la redaccion de estas cuatro preguntas tal como aparece aqui abajo, sin parafrasear, sin generar una redaccion alternativa, sin anadir preguntas nuevas ni reordenarlas. Si en algun momento se detecta que se esta a punto de formular estas preguntas de otra manera, releer esta seccion y usar el texto literal.

**Nota de implementacion (ConfidentialAI):** este `SKILL.md` es la especificacion de referencia y la unica fuente de verdad del arbol de decision. El backend de produccion de ConfidentialAI (repo `GravitonAI-dev/GPT`) no lee este archivo directamente hoy: tiene su propio sistema de "user intents" (`descriptions.json`, `system_roles.json`, `system_directives.json`, `chains_of_thought.json`) que no conoce esta skill. Para que el arbol de decision de esta seccion (Pregunta 0-3) llegue realmente al modelo en produccion, quien integre esta skill en ese backend debe copiar el texto literal de las Pregunta 0-3 (tal cual aparece aqui abajo, sin parafrasear) dentro de las instrucciones de esa intencion. Mientras esa integracion no exista, este documento sirve como especificacion para cualquier orquestador (Claude Code, Claude Agent SDK, u otro) que sí cargue y seleccione esta skill directamente.

**Pregunta 0 — Finalidad del uso (filtro de alcance, se pregunta primero):**

TEXTO EXACTO A USAR (copiar literalmente, sin modificar ni una palabra):
"¿El arrendamiento es para residencia habitual y permanente o para una actividad de negocio estable, o es de temporada (vacacional, de verano, por trabajo temporal) o una vivienda turistica gestionada como alojamiento?"

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
"¿El contrato es para vivienda habitual o para un local de negocio / uso distinto de vivienda?"

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
- NO se genera ni se modifica ningun archivo en disco durante la entrevista. La generacion del documento ocurre una sola vez, al cierre de la entrevista (Sección 10 confirmada y OK explicito de "procedemos a la redaccion"); ver Guardrail 10 y "Generacion del contrato".

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

### Generacion del contrato (unica, al cierre de la entrevista)

La generacion del documento ocurre UNA SOLA VEZ, al cierre de la entrevista, tras la confirmacion explicita del usuario. Durante la entrevista (Secciones 1-10) NO se escribe ni se modifica ningun archivo en el disco; las "vistas previas" que el LLM muestra al usuario son texto plano en el chat, no escrituras reales (ver Guardrail 10 y "Como conducir la entrevista").

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

**Cuando generar el documento:** solo cuando se den las DOS condiciones siguientes:
1. La Seccion 10 ha sido confirmada por el usuario.
2. El usuario ha dado su OK explicito a la pregunta final de cierre "¿Procedemos a la redaccion del contrato?".

Hasta que ambas se cumplan, ninguna operacion de escritura sobre el entregable se ejecuta.

**Pasos de la generacion unica (fila 14 de la Tabla de progreso):**
1. Invocar `Read(assets/contrato-arrendamiento-vivienda.md)` o `Read(assets/contrato-arrendamiento-local.md)`, segun `tipo_inmueble`. Este paso es obligatorio y no puede omitirse: sin el contenido real del archivo delante, no hay texto literal que sustituir.
2. Sustituir en memoria (mentalmente) todos los `{{variable}}` del asset por los datos confirmados en las Secciones 1-10, bloque por bloque, conservando el texto fijo de las clausulas.
3. Crear el archivo del contrato en el disco con `Write`, usando `snake_case` como nomenclatura (ej. `contrato_arrendamiento_vivienda_calle_mayor_123.md`) y conservando el header DRAFT y la fecha de verificacion LAU.
4. Confirmar en el chat la creacion del archivo y mostrar las advertencias finales (ver "Entrega y advertencias finales").

**Manejo de campos sin confirmar al cierre de la entrevista.** Si al llegar al cierre de la entrevista algun dato de relleno sigue sin ser confirmado por el usuario, el LLM debe:
- Si el dato tiene un default legal claro (duracion minima, fianza minima, indice IGC, gastos a cargo del arrendador): aplicar el default del `CLAUDE.md` del plugin y registrarlo en el chat.
- Si el dato NO tiene default (nombres de las partes, direccion del inmueble, importe de la renta): preguntar al usuario UNA vez si quiere proporcionar ese dato antes de la redaccion o prefiere que el campo quede como `[DATO — PENDIENTE DE COMPLETAR]`. Si el usuario prefiere este formato, el contrato se genera con esos campos pendientes y se anade una advertencia explicita en la entrega.

**No hay invocaciones progresivas de `draft_markdown` durante la entrevista.** La regla anterior de "actualizar el borrador con cada seccion" y la coletilla final sobre "datos de relleno que nunca bloquean la entrega" quedan sin efecto (ver Guardrail 10). Solo hay una invocacion, al cierre, tras la doble confirmacion indicada arriba.

### Revision final antes de entregar

Se ejecuta cuando el usuario pide el documento o da por terminada la entrevista, tenga o no todas las Secciones 2-10 completas — no es necesario que esten todas respondidas. Verificar que el contrato generado:
- Tiene el header DRAFT.
- Incluye la fecha de la Verificacion normativa.
- Tiene todas las clausulas obligatorias segun el tipo de inmueble.
- No contiene clausulas nulas.
- Todos los importes son coherentes entre si (renta, fianza, actualizacion) — los que esten disponibles; los pendientes quedan como `[DATO — PENDIENTE DE COMPLETAR]`.
- Los plazos son conformes a la LAU.

### Entrega y advertencias finales

Entregar el contrato y anadir al final:

```
Advertencias:
1. Este contrato es un DRAFT generado automaticamente. Debe ser revisado por un abogado colegiado antes de su firma.
2. Version de la LAU verificada: [fecha extraida en la Verificacion normativa].
3. Si el inmueble se ubica en zona de mercado residencial tensionado, verificar la aplicacion de los limites de renta antes de firmar.
4. El deposito de fianza ante el organismo autonomico competente es obligatorio. Consultar el procedimiento en [comunidad autonoma].
5. Se recomienda la inscripcion del contrato en el Registro de la Propiedad para mayor seguridad juridica (Art. 37 LAU).
```

## Bucle de realimentación post-entrega

Tras la entrega del contrato (fila 14 de la Tabla de progreso confirmada), el LLM NO da por terminada la conversacion. Entra en el paso 5 del Resumen operativo (fila 15 de la Tabla): un bucle de realimentacion en el que ofrece al usuario un menu explicito de ajustes y permanece a la espera hasta que el usuario cierre la conversacion o indique que el contrato esta conforme.

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
