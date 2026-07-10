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

## Procedimiento

Este procedimiento se conduce como una entrevista: se presenta una seccion, se espera la respuesta del usuario, y solo entonces se pasa a la siguiente. Nunca se listan dos secciones a la vez ni se vuelca el formulario completo de golpe. La verificacion normativa, la validacion de condiciones y la generacion del contrato son acciones internas que se disparan en los puntos indicados — no son preguntas adicionales al usuario.

### Entrevista (una seccion por turno)

**Seccion 1 — Clasificacion** (primera pregunta, antes de cualquier otra cosa)

Determina la plantilla, el titulo de la LAU aplicable, el plazo minimo y la fianza minima. Empieza con un filtro de alcance (Pregunta 0) antes de las tres preguntas de clasificacion.

**Consistencia obligatoria:** el arbol de decision (Pregunta 0, 1, 2 y 3, con su redaccion exacta y su orden) es fijo y no cambia de una conversacion a otra. Usar textualmente la redaccion de estas cuatro preguntas tal como aparece aqui abajo, sin parafrasear, sin generar una redaccion alternativa, sin anadir preguntas nuevas ni reordenarlas. Si en algun momento se detecta que se esta a punto de formular estas preguntas de otra manera, releer esta seccion y usar el texto literal.

**Pregunta 0 — Finalidad del uso (filtro de alcance, se pregunta primero):**

"¿El arrendamiento es para residencia habitual y permanente o para una actividad de negocio estable, o es de temporada (vacacional, de verano, por trabajo temporal) o una vivienda turistica gestionada como alojamiento?"

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
       con las Secciones 2-5 ni generar ningun borrador.
```

Solo si la respuesta es "habitual / permanente", continuar con las tres preguntas de clasificacion, **una por turno, esperando la respuesta antes de pasar a la siguiente**:

**Pregunta 1 — Tipo de inmueble:**
"¿El contrato es para vivienda habitual o para un local de negocio / uso distinto de vivienda?"

| Respuesta | Efecto |
|---|---|
| Vivienda habitual | `tipo_inmueble = VIVIENDA` · Titulo II LAU · plantilla `contrato-arrendamiento-vivienda.md` · fianza minima 1 mensualidad |
| Local de negocio | `tipo_inmueble = LOCAL` · Titulo III LAU · plantilla `contrato-arrendamiento-local.md` · fianza minima 2 mensualidades |

**Pregunta 2 — Naturaleza del arrendador** (se pregunta tras recibir la respuesta a la Pregunta 1):
"¿El arrendador es persona fisica o persona juridica (empresa, sociedad)?"

| Respuesta | Efecto |
|---|---|
| Persona fisica | `naturaleza_arrendador = FISICA` · duracion minima 5 anos (Art. 9.1 LAU) |
| Persona juridica | `naturaleza_arrendador = JURIDICA` · duracion minima 7 anos (Art. 9.1 LAU) |

**Pregunta 3 — Naturaleza del arrendatario** (se pregunta tras recibir la respuesta a la Pregunta 2):
"¿Y el arrendatario, es persona fisica o persona juridica?"

| Respuesta | Efecto |
|---|---|
| Persona fisica | `naturaleza_arrendatario = FISICA` |
| Persona juridica | `naturaleza_arrendatario = JURIDICA` |

**Alcance de la Seccion 1 — solo estas cuatro preguntas (0-3), una por turno:**
- Cada pregunta (0, 1, 2, 3) va en su propio mensaje. Nunca combinar dos o mas preguntas de esta lista en el mismo turno, ni presentar el arbol completo de una vez: se avanza pregunta a pregunta, tomando cada decision antes de pasar a la siguiente.
- No preguntar por jurisdiccion, pais, ciudad o provincia como parte de la clasificacion: esta skill aplica exclusivamente a Espana y a la LAU (Ley 29/1994), segun el `CLAUDE.md` del plugin `derecho-civil`. Si el usuario indica que el inmueble esta fuera de Espana, esta skill no aplica; indicarlo y no continuar con el procedimiento.
- No preguntar por el regimen registral del bien (titularidad inscrita, cargas, hipotecas, propiedad horizontal, embargos): esta skill genera el contrato de arrendamiento, no realiza due diligence de titularidad. No forma parte de la clasificacion ni de ningun otro paso de este procedimiento.
- No sustituir ni ampliar estas cuatro preguntas por otras. Si el usuario aporta datos adicionales por su cuenta, se pueden anotar como clausula adicional (Seccion 5), pero no se preguntan de forma proactiva aqui.
- Si el usuario responde varias preguntas a la vez de forma espontanea (por ejemplo, en su primer mensaje), aceptarlas e integrarlas igualmente; solo preguntar por las que sigan sin respuesta.

Esperar las cuatro respuestas antes de continuar: sin ellas no hay plantilla ni marco legal que aplicar, asi que no se genera ningun borrador ni se avanza a la Seccion 2 hasta tenerlas completas. No es un bloqueo formal con mensaje de error — es, simplemente, el orden natural de la entrevista, pregunta a pregunta.

En cuanto el usuario responda, ejecutar la Verificacion normativa (mas abajo) antes de continuar con la Seccion 2.

**Seccion 2 — Ubicacion**

"¿En que comunidad autonoma y municipio esta el inmueble? ¿Sabes si el municipio esta declarado zona de mercado residencial tensionado? (si / no / no lo se)"

Si responde "no lo se": invocar `web_search("zona mercado residencial tensionado [municipio] [comunidad autonoma]")` y comunicar el resultado.

Si la comunidad autonoma tiene normativa propia relevante (Cataluna, Pais Vasco, Navarra, Madrid zona tensionada, etc.), ejecutar la Consulta de normativa autonomica (mas abajo) antes de continuar con la Seccion 3.

**Seccion 3 — Partes**

"Datos del arrendador: nombre completo o razon social, NIF/CIF, y domicilio a efectos de notificaciones. Datos del arrendatario: nombre completo o razon social, NIF/CIF, y domicilio actual."

**Seccion 4 — Inmueble**

"Direccion completa del inmueble (calle, numero, piso, puerta, codigo postal, municipio). Referencia catastral, si se dispone de ella. Descripcion: superficie util aproximada y numero de habitaciones (vivienda), o descripcion del local (uso distinto). ¿Incluye elementos accesorios como plaza de garaje, trastero o mobiliario?"

**Seccion 5 — Condiciones economicas**

"Renta mensual pactada, en euros. Duracion del contrato en anos, o 'minimo legal'. Fianza: numero de mensualidades, o 'segun ley'. Actualizacion de renta: indice pactado, o 'segun ley' (IGC con tope IPC). ¿Algun gasto a cargo del arrendatario (comunidad, IBI, suministros)? ¿Alguna clausula adicional que quieras incluir?"

**Como conducir la entrevista:**
- Una seccion por mensaje, en el orden 2→5. Esperar la respuesta antes de pasar a la siguiente seccion. Dentro de una misma seccion (2 a 5) sí se pueden agrupar varias preguntas en el mismo mensaje — son datos del mismo tema (ubicacion, partes, inmueble, condiciones economicas). Esto es distinto de la Seccion 1 (arbol de decision), donde cada pregunta va sola, sin excepcion (ver Seccion 1).
- Mostrar el titulo de la seccion como encabezado del mensaje al usuario (p. ej. "**Seccion 2 — Ubicacion**") antes de la pregunta correspondiente, para que pueda seguir el progreso de la entrevista.
- Si el usuario aporta espontaneamente datos de varias secciones a la vez (por ejemplo, en su primer mensaje), aceptarlos e integrarlos igualmente; solo preguntar por las secciones que sigan incompletas.
- Desde que se resuelve la Seccion 1, generar y actualizar el borrador del contrato de forma progresiva (ver "Generacion del contrato") conforme llegan las respuestas de las Secciones 2-5, en vez de esperar a tenerlas todas.

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

### Generacion del contrato (progresiva, en paralelo a la entrevista)

Seleccionar la plantilla segun `tipo_inmueble` (Seccion 1):
- Vivienda: `assets/contrato-arrendamiento-vivienda.md`
- Local de negocio: `assets/contrato-arrendamiento-local.md`

Primera invocacion, en cuanto se resuelva la Seccion 1 (y, si ya se dispone, la Seccion 2 o 3):
```
draft_markdown(
  template_id: "contrato-arrendamiento-vivienda" | "contrato-arrendamiento-local",
  variables: {
    tipo_inmueble, naturaleza_arrendador, naturaleza_arrendatario (Seccion 1),
    datos disponibles de las Secciones 2-5
  }
)
```

Rellenar todos los campos `[DATO]` con los datos reales disponibles en ese momento. Los campos accesorios que el usuario no haya proporcionado quedan como `[DATO — PENDIENTE DE COMPLETAR]` (esto no aplica a `tipo_inmueble`, `naturaleza_arrendador` ni `naturaleza_arrendatario`: ver Seccion 1, que debe estar resuelta antes de esta primera invocacion).

Invocaciones siguientes: cada vez que el usuario responda una nueva seccion de la entrevista, actualizar (Edit) el mismo documento sustituyendo los `[DATO — PENDIENTE DE COMPLETAR]` correspondientes, en vez de regenerarlo desde cero. La Revision final solo se ejecuta como cierre, cuando ya no queden secciones pendientes.

### Revision final antes de entregar

Verificar que el contrato generado:
- Tiene el header DRAFT.
- Incluye la fecha de la Verificacion normativa.
- Tiene todas las clausulas obligatorias segun el tipo de inmueble.
- No contiene clausulas nulas.
- Todos los importes son coherentes (renta, fianza, actualizacion).
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
