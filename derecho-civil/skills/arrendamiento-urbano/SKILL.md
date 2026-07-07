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

1. Verificar siempre la LAU en el BOE antes de redactar. Sin verificacion, no proceder. Si se detecta una version de la LAU posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 1). No usar una version desactualizada.
2. Nunca incluir clausulas que perjudiquen al arrendatario en los derechos reconocidos por el Titulo II LAU (son nulas de pleno derecho — Art. 6).
3. Si el municipio es zona de mercado residencial tensionado, aplicar obligatoriamente las limitaciones de renta de los Art. 17.6 y 17.7 LAU y advertir al usuario.
4. Si el arrendador es persona juridica, la duracion minima es 7 anos (no 5). Nunca reducirla.
5. Nunca omitir la clausula de fianza. El importe minimo es imperativo (Art. 36 LAU).
6. Los gastos de gestion inmobiliaria y formalizacion del contrato son siempre a cargo del arrendador (Art. 20.1 LAU). No pueden pactarse a cargo del arrendatario.
7. Marcar todos los campos a rellenar con `[DATO]` en mayusculas. Nunca inventar datos.
8. Si el usuario pide clausulas que contradigan normas imperativas, rechazar y explicar el motivo.

## Procedimiento

### Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, antes de cualquier otra accion)

La skill se actualiza a si misma en cada lanzamiento: comprueba la LAU en la fuente oficial y, si detecta una version posterior, reescribe sus propias references antes de redactar. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la version registrada localmente.** Las references indican la ultima modificacion conocida (25/05/2023, Ley 12/2023). Anotar esa fecha como referencia de comparacion.

**1.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003&p=20230525&tn=1",
  format: "text"
)
```
Extraer: fecha de ultima modificacion del texto consolidado; articulos modificados respecto a la version registrada; version verificada para el encabezado del contrato.

**1.3 — Comparar.** Contrastar la fecha/redaccion oficial con la registrada en las references.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la fecha oficial es posterior o cambia la redaccion de articulos aplicados, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/lau-vivienda-plazos-renta-fianza.md`, `references/lau-derechos-obligaciones-partes.md` y/o `references/lau-arrendamiento-local-negocio.md` con la redaccion vigente.
- Actualizar la nota de "ultima modificacion conocida" en el encabezado de esas references con la nueva fecha.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente de la LAU (fecha y articulos).

No redactar el contrato hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si read_document falla (error HTTP, timeout):
```
web_search("Ley 29/1994 Arrendamientos Urbanos texto consolidado BOE ultima modificacion")
```
Si ambos fallan: usar references como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LAU en el BOE. El contrato se genera con la version de referencia (25/05/2023). Verificar manualmente antes de firmar."

### Paso 2 — Recogida de datos (una pregunta por bloque si el usuario no los ha proporcionado)

Si el usuario no ha proporcionado todos los datos, preguntar en este orden:

**Bloque A — Tipo de contrato:**
"El contrato es para: (1) vivienda habitual, (2) local de negocio / uso distinto de vivienda?"

**Bloque B — Naturaleza de las partes:**
"El arrendador es persona fisica o persona juridica (empresa, sociedad)?"
"El arrendatario es persona fisica o persona juridica?"

**Bloque C — Ubicacion:**
"Comunidad autonoma y municipio donde se ubica el inmueble?"
"El municipio esta declarado zona de mercado residencial tensionado? (si / no / no lo se)"

Si responde "no lo se": invocar `web_search("zona mercado residencial tensionado [municipio] [comunidad autonoma]")` y comunicar el resultado.

**Bloque D — Datos de las partes:**
- Arrendador: nombre completo o razon social, NIF/CIF, domicilio a efectos de notificaciones.
- Arrendatario: nombre completo o razon social, NIF/CIF, domicilio actual.

**Bloque E — Datos del inmueble:**
- Direccion completa (calle, numero, piso, puerta, codigo postal, municipio).
- Referencia catastral (si se dispone).
- Descripcion: superficie util aproximada, numero de habitaciones (vivienda) o descripcion del local.
- Elementos accesorios incluidos: plaza de garaje, trastero, mobiliario (si aplica).

**Bloque F — Condiciones economicas:**
- Renta mensual pactada en euros.
- Duracion del contrato (anos) o "minimo legal".
- Fianza: numero de mensualidades o "segun ley".
- Actualizacion de renta: indice pactado o "segun ley" (IGC con tope IPC).
- Gastos a cargo del arrendatario (comunidad, IBI, suministros): si/no y cuales.

### Paso 3 — Validacion de condiciones

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

### Paso 4 — Consulta de normativa autonomica (si aplica)

Si el usuario menciona una comunidad autonoma con normativa propia relevante (Cataluna, Pais Vasco, Navarra, Madrid zona tensionada, etc.):

```
web_search("deposito fianza arrendamiento [comunidad autonoma] organismo competente 2024")
```

Incluir en el contrato la clausula de deposito de fianza ante el organismo autonomico correspondiente.

### Paso 5 — Generacion del contrato

Seleccionar la plantilla segun tipo de inmueble:
- Vivienda: `assets/contrato-arrendamiento-vivienda.md`
- Local de negocio: `assets/contrato-arrendamiento-local.md`

Invocar:
```
draft_markdown(
  template_id: "contrato-arrendamiento-vivienda" | "contrato-arrendamiento-local",
  variables: {
    todos los datos recogidos en los bloques A-F
  }
)
```

Rellenar todos los campos `[DATO]` con los datos reales. Los campos que el usuario no haya proporcionado quedan como `[DATO — PENDIENTE DE COMPLETAR]`.

### Paso 6 — Revision final antes de entregar

Verificar que el contrato generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Tiene todas las clausulas obligatorias segun el tipo de inmueble.
- No contiene clausulas nulas.
- Todos los importes son coherentes (renta, fianza, actualizacion).
- Los plazos son conformes a la LAU.

### Paso 7 — Entrega y advertencias finales

Entregar el contrato y anadir al final:

```
Advertencias:
1. Este contrato es un DRAFT generado automaticamente. Debe ser revisado por un abogado colegiado antes de su firma.
2. Version de la LAU verificada: [fecha extraida en Paso 1].
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
