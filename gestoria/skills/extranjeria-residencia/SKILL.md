---
name: extranjeria-residencia
description: >
  Prepara el tramite administrativo de solicitud del Numero de Identidad de Extranjero (NIE) o de
  autorizacion de residencia (residencia temporal no lucrativa, residencia por arraigo, reagrupacion
  familiar u otra) ante la Oficina de Extranjeria, conforme a la Ley Organica 4/2000 (LOEX) y al
  Reglamento de Extranjeria (RD 1155/2024, en vigor desde el 20/05/2025) verificados en el BOE.
  Genera la hoja de datos para el formulario EX correspondiente, el escrito de solicitud o alegaciones
  cuando procede, el checklist de documentos y el pago de la tasa (modelo 790), e indica el organismo,
  la sede de presentacion, la cita previa y los plazos. La resolucion es discrecional de la
  Administracion. NO usar para solicitar el visado ante el consulado, ni para la nacionalidad espanola,
  el asilo o la proteccion internacional, ni para recurrir una denegacion previa.
when_to_use: |
  - El usuario (extranjero o su representante) quiere obtener el NIE por interes economico, profesional o social.
  - El usuario quiere solicitar una autorizacion de residencia: no lucrativa, por arraigo o por reagrupacion familiar.
  - El usuario pide preparar el formulario EX, el checklist de documentos y la tasa de un tramite de extranjeria.
inputs:
  - tipo_tramite: nie / residencia no lucrativa / residencia por arraigo / reagrupacion familiar / otra
  - tipo_arraigo: solo si es arraigo. social / sociolaboral / socioformativo / familiar / segunda oportunidad
  - datos_extranjero: nombre y apellidos, nacionalidad, numero de pasaporte, fecha de nacimiento
  - nie_previo: si el extranjero ya tiene NIE asignado (si / no)
  - motivo: motivo del NIE o de la residencia
  - domicilio_espana: domicilio en Espana a efectos de notificaciones, si lo hay
  - datos_apoyo: medios economicos, seguro medico, tiempo de permanencia, familiar reagrupante, contrato u oferta de trabajo, etc.
  - representante: si actua un representante (gestor, abogado, familiar) y sus datos
  - lugar_presentacion: en Espana (Oficina de Extranjeria) o desde el extranjero (consulado)
outputs:
  - hoja_datos_ex: hoja de datos para el formulario EX, checklist de documentos, organismo y tasa, en markdown, DRAFT
  - escrito_solicitud: opcional, escrito de solicitud o alegaciones de residencia en markdown, DRAFT
references:
  - references/loex-y-reglamento.md
  - references/formularios-ex-y-tasas.md
  - references/documentacion-por-tramite.md
  - references/fuentes-y-plazos.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/hoja-datos-solicitud-ex.md
  - assets/escrito-solicitud-residencia.md
---

# Preparar Solicitud de NIE o Autorizacion de Residencia (Extranjeria)

> DRAFT — para revision por un gestor colegiado o profesional antes de su presentacion. No constituye asesoramiento juridico ni garantiza la concesion del tramite.

## Guardrails

1. Verificar siempre la LOEX y el Reglamento de Extranjeria en el BOE antes de preparar el tramite. Sin verificacion, no proceder (ver Paso 1).
2. El Reglamento vigente es el RD 1155/2024 (en vigor 20/05/2025), que derogo el RD 557/2011. Si en el BOE se detecta una version posterior o una modificacion, actualizar los archivos del plugin antes de preparar el tramite. Nunca usar la version derogada.
3. Verificar el formulario EX aplicable y la tasa (modelo 790) vigentes en la sede del organismo. Los importes de tasa cambian por orden ministerial: marcar el importe como aproximado y remitir al modelo oficial para el pago.
4. La resolucion de una autorizacion de residencia es DISCRECIONAL de la Administracion. Nunca afirmar que el tramite se concedera. Advertir siempre de que el silencio administrativo y la denegacion son posibles.
5. Nunca inventar datos personales, numero de pasaporte, NIE, importes de tasa ni numeros de formulario. Marcar todo campo pendiente con el patron del asset.
6. No preparar el visado: para la residencia solicitada desde el extranjero, el visado se pide en el consulado y queda fuera de esta skill; indicarlo y derivar.
7. Aplicar la posicion conservadora: ante la duda sobre el tipo de tramite, el formulario o la documentacion, marcar `[verificar]` y recomendar confirmar en la Oficina de Extranjeria o con un profesional.
8. Indicar siempre el organismo competente, la sede de presentacion, la necesidad de cita previa y los plazos aplicables.

## Procedimiento

### Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, antes de cualquier otra accion)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de preparar el tramite. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la version registrada localmente.** Abrir `references/fuentes-y-plazos.md` y anotar la version registrada de la LOEX, del Reglamento (RD 1155/2024) y de los formularios EX y la tasa.

**1.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-2000-544",
  format: "text"
)
```
Extraer la fecha del texto consolidado vigente de la LOEX. Consultar tambien el Reglamento:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099",
  format: "text"
)
```
Y comprobar el catalogo de formularios EX y la tasa en la sede del organismo:
```
read_document(
  path: "https://www.inclusion.gob.es/web/migraciones/modelos-generales",
  format: "text"
)
```

**1.3 — Comparar.** Contrastar la version oficial (LOEX, Reglamento, formularios, tasa) con la registrada localmente y con el texto de las references.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto ha cambiado, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/loex-y-reglamento.md`, `references/formularios-ex-y-tasas.md` y/o `references/documentacion-por-tramite.md`.
- Actualizar la tabla de version registrada y las fechas en `references/fuentes-y-plazos.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma, formulario o tasa, y fecha).

No preparar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_document` falla (error HTTP, timeout):
```
web_search("Reglamento de Extranjeria RD 1155/2024 formularios EX tasa 790 BOE texto vigente")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la normativa de extranjeria en el BOE. El tramite se prepara con la version de referencia. Verificar manualmente el formulario y la tasa antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no prepara nada hasta recoger estos datos:

**Bloque A — Tipo de tramite:**
"Que tramite desea preparar? (1) NIE (Numero de Identidad de Extranjero) por interes economico, profesional o social; (2) autorizacion de residencia temporal no lucrativa; (3) autorizacion de residencia por arraigo; (4) reagrupacion familiar; (5) otra."

Si elige arraigo, preguntar el tipo: social, sociolaboral, socioformativo, familiar o segunda oportunidad (ver `references/loex-y-reglamento.md`).

**Bloque B — Datos del extranjero:**
- Nombre y apellidos, nacionalidad, numero de pasaporte y fecha de caducidad, fecha de nacimiento.
- Si ya tiene NIE asignado (si / no) y, en su caso, cual.

**Bloque C — Motivo:**
- Motivo del NIE (operacion economica, actividad profesional, herencia, apertura de cuenta, etc.) o de la residencia.

**Bloque D — Domicilio y presentacion:**
- Domicilio en Espana a efectos de notificaciones, si lo hay.
- Si el tramite se presenta en Espana (Oficina de Extranjeria) o desde el extranjero (consulado). Si es desde el extranjero, advertir de que el visado se solicita en el consulado y queda fuera de esta skill.

**Bloque E — Datos de apoyo (segun el tramite):**
- Residencia no lucrativa: medios economicos suficientes (referencia IPREM), seguro medico, ausencia de antecedentes.
- Arraigo: tiempo de permanencia en Espana, vinculos, informe de integracion o de arraigo, oferta o contrato de trabajo si aplica.
- Reagrupacion familiar: datos del familiar reagrupante (residente legal), vinculo, vivienda y medios.

**Bloque F — Representante:**
"Actua un representante (gestor, abogado, familiar) en nombre del interesado? Si es asi, indique sus datos y la forma de representacion."

### Paso 3 — Validacion del tramite

Antes de preparar los documentos, validar con `references/documentacion-por-tramite.md`:

a) **Tipo de tramite y formulario EX.** Confirmar el formulario EX aplicable (ver `references/formularios-ex-y-tasas.md`): EX-15 para el NIE, EX-01 para residencia no lucrativa, EX-10 para arraigo (circunstancias excepcionales), EX-11 para reagrupacion familiar. Si hay duda, marcar `[verificar]`.

b) **Documentacion del motivo.** Confirmar que el usuario dispone de la documentacion clave del tramite (pasaporte en vigor, justificante de la tasa 790, y la documentacion del motivo: medios economicos, seguro medico, antecedentes, informe de arraigo, etc.). Si falta un documento imprescindible, indicarlo y no darlo por presentado.

c) **Competencia y lugar de presentacion.** Identificar la Oficina de Extranjeria de la provincia del domicilio, o el consulado si se solicita desde el extranjero. Advertir de la necesidad de cita previa.

d) **Tasa.** Identificar el codigo de la tasa (modelo 790): codigo 012 para la expedicion de documentos de extranjeros (NIE/TIE) y codigo 052 para la tramitacion de autorizaciones de residencia. Marcar el importe como aproximado y remitir al modelo oficial.

e) **Discrecionalidad y plazos.** Recordar que la resolucion es discrecional, informar del plazo de resolucion y del sentido del silencio administrativo aplicable al tramite (ver `references/fuentes-y-plazos.md`).

### Paso 4 — Generacion de los documentos

Generar siempre la hoja de datos y el checklist:
```
draft_markdown(
  template_id: "hoja-datos-solicitud-ex",
  variables: {
    todos los datos recogidos en los bloques A-F,
    formulario_ex, codigo_tasa, importe_tasa_aprox, organismo, sede, plazo
  }
)
```

Si el tramite es una autorizacion de residencia (no lucrativa, arraigo, reagrupacion) y el usuario pide tambien un escrito de solicitud o alegaciones, generar ademas:
```
draft_markdown(
  template_id: "escrito-solicitud-residencia",
  variables: { datos del interesado, representante, tipo de residencia, motivo y fundamentos }
)
```

Para un NIE simple no suele hacer falta escrito de alegaciones: basta la hoja de datos del EX-15 y el checklist.

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado quedan con el marcador del asset. Aplicar el estilo de `references/estilo-redaccion-escritos.md`: lenguaje administrativo claro, estructura EXPONE / SOLICITA, una idea por parrafo, sin formulas grandilocuentes.

### Paso 5 — Revision final y advertencias

Verificar que cada documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Identifica el formulario EX, el organismo, la sede, la cita previa, la tasa (codigo y importe aproximado) y el plazo.
- Relaciona el checklist completo de documentos del tramite.
- Advierte de que la resolucion es discrecional de la Administracion.

Entregar los documentos y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un gestor o profesional antes de su presentacion.
2. Version de la normativa verificada (LOEX y RD 1155/2024): [fecha extraida en Paso 1].
3. Debe presentarse el formulario EX oficial firmado junto con la documentacion del checklist y el justificante del pago de la tasa (modelo 790).
4. La resolucion de la autorizacion de residencia es discrecional de la Administracion; puede ser denegada o resolverse por silencio.
5. Para tramites solicitados desde el extranjero, el visado se solicita en el consulado y no forma parte de esta skill.
6. Verificar el importe de la tasa en el modelo oficial antes de pagar, y pedir cita previa en la Oficina de Extranjeria o consulado.
```

## Como NO se usa esta skill

- No usar para solicitar el visado ante el consulado (tramite consular, fuera de alcance).
- No usar para la nacionalidad espanola (por residencia, opcion o carta de naturaleza).
- No usar para asilo, proteccion internacional ni apatridia.
- No usar para recurrir una denegacion previa ni para un procedimiento sancionador o de expulsion: derivar a un profesional.
- No usar para tramitar la tarjeta de residencia de familiar de ciudadano de la Union (regimen comunitario) sin advertir de que sigue un procedimiento distinto.
- No usar si el usuario pide una valoracion juridica sobre sus posibilidades de exito: la resolucion es discrecional; derivar a un abogado o profesional especialista.

## Escalacion

| Situacion | Accion |
|---|---|
| Denegacion previa, recurso administrativo o contencioso | Advertir que excede el alcance y derivar a un abogado especialista en extranjeria |
| Procedimiento sancionador, expulsion o devolucion en curso | Escalar a abogado; no preparar el tramite de residencia sin asistencia |
| Tramite consular o visado desde el extranjero | Indicar que corresponde al consulado y derivar |
| Regimen comunitario (familiar de ciudadano UE) o proteccion internacional | Advertir de la diferencia de procedimiento y derivar |
| Antecedentes penales o dudas sobre requisitos del arraigo | Verificar con web_search y advertir; ante duda, derivar |
| Especialidad autonomica en el informe de arraigo o integracion | Verificar con web_search y advertir |
