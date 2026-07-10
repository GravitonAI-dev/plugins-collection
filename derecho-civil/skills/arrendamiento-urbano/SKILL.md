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

1. Verificar siempre la LAU en el BOE antes de redactar. Sin verificacion, no proceder. Si se detecta una version de la LAU posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 2). No usar una version desactualizada.
2. Nunca incluir clausulas que perjudiquen al arrendatario en los derechos reconocidos por el Titulo II LAU (son nulas de pleno derecho — Art. 6).
3. Si el municipio es zona de mercado residencial tensionado, aplicar obligatoriamente las limitaciones de renta de los Art. 17.6 y 17.7 LAU y advertir al usuario.
4. Si el arrendador es persona juridica, la duracion minima es 7 anos (no 5). Nunca reducirla.
5. Nunca omitir la clausula de fianza. El importe minimo es imperativo (Art. 36 LAU).
6. Los gastos de gestion inmobiliaria y formalizacion del contrato son siempre a cargo del arrendador (Art. 20.1 LAU). No pueden pactarse a cargo del arrendatario.
7. Marcar todos los campos a rellenar con `[DATO]` en mayusculas. Nunca inventar datos.
8. Si el usuario pide clausulas que contradigan normas imperativas, rechazar y explicar el motivo.
9. **BLOQUEANTE.** Nunca verificar la LAU, recoger el resto de datos ni redactar nada sin haber resuelto antes el arbol de decision del Paso 1 (`tipo_inmueble`, `naturaleza_arrendador`, `naturaleza_arrendatario`). Es el primer paso del procedimiento, antes incluso de la verificacion normativa. Nunca inferir estas tres respuestas, asumirlas por defecto, ni rellenarlas como `[DATO — PENDIENTE DE COMPLETAR]`.

## Procedimiento

### Paso 1 — Arbol de decision: clasificacion del contrato (OBLIGATORIO, primer paso — antes de verificar la LAU, recoger datos o redactar nada)

Esta es la primera accion del procedimiento, por delante de la verificacion normativa (Paso 2). Su salida determina la plantilla, el titulo de la LAU aplicable, el plazo minimo y la fianza minima. Resolver el arbol completo antes de continuar:

```
Pregunta 1 — Tipo de inmueble
"El contrato es para: (1) vivienda habitual, (2) local de negocio / uso distinto de vivienda?"
  |
  ├─ Vivienda habitual  → tipo_inmueble = VIVIENDA
  |                        Titulo II LAU | plantilla contrato-arrendamiento-vivienda.md | fianza minima 1 mensualidad
  |
  └─ Local de negocio   → tipo_inmueble = LOCAL
                           Titulo III LAU | plantilla contrato-arrendamiento-local.md | fianza minima 2 mensualidades

Pregunta 2 — Naturaleza del arrendador
"El arrendador es persona fisica o persona juridica (empresa, sociedad)?"
  |
  ├─ Persona fisica     → naturaleza_arrendador = FISICA    → duracion minima 5 anos (Art. 9.1 LAU)
  |
  └─ Persona juridica    → naturaleza_arrendador = JURIDICA  → duracion minima 7 anos (Art. 9.1 LAU)

Pregunta 3 — Naturaleza del arrendatario
"El arrendatario es persona fisica o persona juridica?"
  |
  ├─ Persona fisica     → naturaleza_arrendatario = FISICA
  |
  └─ Persona juridica    → naturaleza_arrendatario = JURIDICA
```

**Regla de bloqueo:** si el usuario no ha respondido explicitamente estas tres preguntas, detener el procedimiento aqui mismo. No pasar al Paso 2 (verificacion normativa), no recoger el resto de datos (Paso 3), no redactar nada. Nunca inferir la respuesta ni asumir un valor por defecto (por ejemplo "vivienda" o "persona fisica"), y nunca rellenarlas como `[DATO — PENDIENTE DE COMPLETAR]`: son las unicas respuestas de todo el procedimiento sin ese fallback, porque sin ellas no existe plantilla ni marco legal aplicable que redactar.

**Regla de no-mezcla:** estas tres preguntas se presentan en un mensaje propio, separado de cualquier pregunta del Paso 3. Nunca combinarlas con las preguntas de recogida de datos (nombres, direccion, renta, fianza, etc.) en el mismo mensaje ni en la misma lista: son de naturaleza distinta (clasifican el contrato, no lo rellenan) y deben resolverse por completo antes de que exista ninguna pregunta del Paso 3.

### Paso 2 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, tras resolver el Paso 1)

La skill se actualiza a si misma en cada lanzamiento: comprueba la LAU en la fuente oficial y, si detecta una version posterior, reescribe sus propias references antes de redactar. Ejecutar SIEMPRE esta secuencia:

**2.1 — Leer la version registrada localmente.** Las references indican la ultima modificacion conocida (25/05/2023, Ley 12/2023). Anotar esa fecha como referencia de comparacion.

**2.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003&p=20230525&tn=1",
  format: "text"
)
```
Extraer: fecha de ultima modificacion del texto consolidado; articulos modificados respecto a la version registrada; version verificada para el encabezado del contrato.

**2.3 — Comparar.** Contrastar la fecha/redaccion oficial con la registrada en las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la fecha oficial es posterior o cambia la redaccion de articulos aplicados, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/lau-vivienda-plazos-renta-fianza.md`, `references/lau-derechos-obligaciones-partes.md` y/o `references/lau-arrendamiento-local-negocio.md` con la redaccion vigente.
- Actualizar la nota de "ultima modificacion conocida" en el encabezado de esas references con la nueva fecha.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente de la LAU (fecha y articulos).

No redactar el contrato hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**2.5 — Fallback si la fuente no es accesible.** Si read_document falla (error HTTP, timeout):
```
web_search("Ley 29/1994 Arrendamientos Urbanos texto consolidado BOE ultima modificacion")
```
Si ambos fallan: usar references como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LAU en el BOE. El contrato se genera con la version de referencia (25/05/2023). Verificar manualmente antes de firmar."

### Paso 3 — Recogida de datos (progresiva, un bloque por mensaje, mientras se va editando el documento)

`tipo_inmueble`, `naturaleza_arrendador` y `naturaleza_arrendatario` ya se obtuvieron en el Paso 1 y no se repiten aqui. Estos son datos de relleno del documento, no de clasificacion: se recogen de forma progresiva, nunca todos de golpe en una unica lista.

**Como recoger estos datos:**
- Preguntar un bloque (A, B, C o D) por mensaje, en este orden, y esperar la respuesta antes de pasar al siguiente.
- En cuanto haya datos suficientes del Bloque A y B, generar un primer borrador del contrato (Paso 6) con `[DATO — PENDIENTE DE COMPLETAR]` en los campos de los bloques aun no respondidos, en vez de esperar a tener el bloque D para generar cualquier version del documento.
- Tras cada respuesta del usuario, actualizar (Edit, no reescribir desde cero) el borrador ya generado con los datos nuevos y volver a mostrarlo o confirmarlo antes de pedir el siguiente bloque.
- Si el usuario aporta espontaneamente datos de varios bloques a la vez (por ejemplo, en su primer mensaje), aceptarlos e integrarlos igualmente; solo preguntar por los bloques que sigan incompletos.

Preguntar en este orden:

**Bloque A — Ubicacion:**
"Comunidad autonoma y municipio donde se ubica el inmueble?"
"El municipio esta declarado zona de mercado residencial tensionado? (si / no / no lo se)"

Si responde "no lo se": invocar `web_search("zona mercado residencial tensionado [municipio] [comunidad autonoma]")` y comunicar el resultado.

**Bloque B — Datos de las partes:**
- Arrendador: nombre completo o razon social, NIF/CIF, domicilio a efectos de notificaciones.
- Arrendatario: nombre completo o razon social, NIF/CIF, domicilio actual.

**Bloque C — Datos del inmueble:**
- Direccion completa (calle, numero, piso, puerta, codigo postal, municipio).
- Referencia catastral (si se dispone).
- Descripcion: superficie util aproximada, numero de habitaciones (vivienda) o descripcion del local.
- Elementos accesorios incluidos: plaza de garaje, trastero, mobiliario (si aplica).

**Bloque D — Condiciones economicas:**
- Renta mensual pactada en euros.
- Duracion del contrato (anos) o "minimo legal".
- Fianza: numero de mensualidades o "segun ley".
- Actualizacion de renta: indice pactado o "segun ley" (IGC con tope IPC).
- Gastos a cargo del arrendatario (comunidad, IBI, suministros): si/no y cuales.

### Paso 4 — Validacion de condiciones

Antes de generar el contrato, validar:

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

### Paso 5 — Consulta de normativa autonomica (si aplica)

Si el usuario menciona una comunidad autonoma con normativa propia relevante (Cataluna, Pais Vasco, Navarra, Madrid zona tensionada, etc.):

```
web_search("deposito fianza arrendamiento [comunidad autonoma] organismo competente 2024")
```

Incluir en el contrato la clausula de deposito de fianza ante el organismo autonomico correspondiente.

### Paso 6 — Generacion del contrato (iterativa, en paralelo al Paso 3)

Seleccionar la plantilla segun `tipo_inmueble` (Paso 1):
- Vivienda: `assets/contrato-arrendamiento-vivienda.md`
- Local de negocio: `assets/contrato-arrendamiento-local.md`

Primera invocacion, en cuanto haya datos minimos del Bloque A/B del Paso 3:
```
draft_markdown(
  template_id: "contrato-arrendamiento-vivienda" | "contrato-arrendamiento-local",
  variables: {
    tipo_inmueble, naturaleza_arrendador, naturaleza_arrendatario (Paso 1),
    datos disponibles de los bloques A-D (Paso 3)
  }
)
```

Rellenar todos los campos `[DATO]` con los datos reales disponibles en ese momento. Los campos accesorios que el usuario no haya proporcionado quedan como `[DATO — PENDIENTE DE COMPLETAR]` (esto no aplica a `tipo_inmueble`, `naturaleza_arrendador` ni `naturaleza_arrendatario`: ver Paso 1, que deben estar resueltos antes de esta primera invocacion).

Invocaciones siguientes: cada vez que el usuario responda un nuevo bloque del Paso 3, actualizar (Edit) el mismo documento sustituyendo los `[DATO — PENDIENTE DE COMPLETAR]` correspondientes, en vez de regenerarlo desde cero. El Paso 7 (revision final) solo se ejecuta como cierre, cuando ya no queden bloques pendientes.

### Paso 7 — Revision final antes de entregar

Verificar que el contrato generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 2).
- Tiene todas las clausulas obligatorias segun el tipo de inmueble.
- No contiene clausulas nulas.
- Todos los importes son coherentes (renta, fianza, actualizacion).
- Los plazos son conformes a la LAU.

### Paso 8 — Entrega y advertencias finales

Entregar el contrato y anadir al final:

```
Advertencias:
1. Este contrato es un DRAFT generado automaticamente. Debe ser revisado por un abogado colegiado antes de su firma.
2. Version de la LAU verificada: [fecha extraida en Paso 2].
3. Si el inmueble se ubica en zona de mercado residencial tensionado, verificar la aplicacion de los limites de renta antes de firmar.
4. El deposito de fianza ante el organismo autonomico competente es obligatorio. Consultar el procedimiento en [comunidad autonoma].
5. Se recomienda la inscripcion del contrato en el Registro de la Propiedad para mayor seguridad juridica (Art. 37 LAU).
```

## Como NO se usa esta skill

- No usar para revisar contratos existentes de terceros.
- No usar para contratos de temporada o viviendas turisticas.
- No usar para arrendamientos de finca rustica.
- No usar si el usuario solicita opinion juridica sobre un litigio: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| Litigio activo o previo entre las partes | Escalar via escalate_to_attorney |
| Clausulas que no pueden resolverse con la LAU | Escalar via escalate_to_attorney |
| Arrendatario en situacion de vulnerabilidad acreditada | Advertir y ofrecer escalacion |
| Duda sobre zona tensionada que no resuelve web_search | Advertir y recomendar consulta al ayuntamiento |
