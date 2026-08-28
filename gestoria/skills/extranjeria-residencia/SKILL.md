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
  - assets/template-hoja-datos-solicitud-ex.md
  - assets/template-escrito-solicitud-residencia.md
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

### Paso 1 — Verificacion normativa

**1.1 — Consultar la version registrada en references.** Consultar el archivo `fuentes-y-plazos.md` directamente desde el bloque `<document kind="references-collection">` de tu system prompt y anotar la version registrada de la LOEX, del Reglamento (RD 1155/2024) y de los formularios EX y la tasa.

**1.2 — Consultar la fuente oficial vigente en vivo.** Invocar:
```
web_search("BOE-A-2000-544 Ley Organica 4/2000 derechos libertades extranjeros Espana texto consolidado")
web_search("BOE-A-2024-24099 Real Decreto 1155/2024 Reglamento Extranjeria texto consolidado")
```
Y comprobar el catalogo de formularios EX y la tasa en la sede del organismo:
```
web_search("modelos generales extranjeria formularios EX tasa 790 codigo 012 052 Ministerio Inclusion")
```

**1.3 — Comparar.** Contrastar la version oficial (LOEX, Reglamento, formularios, tasa) con la registrada en `fuentes-y-plazos.md` y con las referencias del prompt (`loex-y-reglamento.md`, `formularios-ex-y-tasas.md`, `documentacion-por-tramite.md`).

**1.4 — Aplicar cambios normativos.** Si la version oficial es posterior o el texto ha cambiado:
- Aplicar en memoria la normativa, formularios y tasas vigentes para adaptar los documentos.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma, formulario o tasa, y fecha).

**1.5 — Fallback si la busqueda no es accesible.** Si la busqueda web falla: usar las references cargadas en el prompt como respaldo y notificar al usuario:
"No se pudo verificar en vivo la version vigente de la normativa de extranjeria en el BOE. El tramite se prepara con la version de referencia. Verificar manualmente el formulario y la tasa antes de presentar."

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

Tomar las plantillas correspondientes directamente desde el bloque `<document kind="assets-collection">` de tu system prompt:

Generar siempre la hoja de datos y el checklist con la plantilla `template-hoja-datos-solicitud-ex.md` invocando `create_file`:
```
create_file(
  relative_file_path: "hoja_datos_solicitud_ex.md",
  file_content: "... contenido completo adaptado para formulario EX, tasa 790, checklist y datos de bloques A-F ..."
)
```

Si el tramite es una autorizacion de residencia (no lucrativa, arraigo, reagrupacion) y el usuario pide tambien un escrito de solicitud o alegaciones, generar ademas con la plantilla `template-escrito-solicitud-residencia.md`:
```
create_file(
  relative_file_path: "escrito_solicitud_residencia.md",
  file_content: "... contenido completo con datos de interesado, tipo de residencia, motivo y fundamentos ..."
)
```

### Reglas de Adaptación y Cláusulas Condicionales:

1. **Representación:**
   - *Si actúa representante:* Indicar en el encabezamiento: `Actúa en su nombre {{nombre_representante}}, en calidad de {{condicion_representante}} (gestor administrativo / abogado / familiar), cuya representación se acredita mediante {{acreditacion_representacion}}.`
   - *Si actúa por sí mismo:* Consignar la actuación a nombre propio del solicitante.

2. **Modalidad de Residencia y Justificación Material:**
   - *Residencia No Lucrativa:* Exponer y justificar medios económicos suficientes (`{{medios_economicos}}` - % IPREM) y seguro médico privado con cobertura completa en España (`{{seguro_medico}}`).
   - *Residencia Temporal por Arraigo:* Precisar modalidad (`{{tipo_arraigo}}`: social, sociolaboral, socioformativo, familiar o segunda oportunidad), tiempo de permanencia continuada (`{{tiempo_permanencia}}`) y vínculos o contrato/compromiso formativo (`{{datos_arraigo}}`).
   - *Reagrupación Familiar:* Identificar al reagrupante (`{{reagrupante}}`), título de residencia, acreditar parentesco/vínculo legalizado y traducido (`{{vinculo}}`), y disponibilidad de vivienda adecuada y medios económicos suficientes (`{{vivienda_medios}}`).

3. **Checklist Documental Específico según Trámite:**
   - Adaptar la lista de verificación documental de `hoja_datos_solicitud_ex.md` seleccionando los requisitos de `references/documentacion-por-tramite.md` aplicables exclusivamente al trámite (NIE, Arraigo, No Lucrativa, Reagrupación).

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado quedan como `[DATO — PENDIENTE DE COMPLETAR]`. Aplicar las directivas de `estilo-redaccion-escritos.md` (disponible directamente en `<document kind="references-collection">` del prompt): lenguaje administrativo claro, estructura EXPONE / SOLICITA, una idea por parrafo, sin formulas grandilocuentes.

Tras guardar los archivos en disco del workspace, invocar `read_file` exclusivamente sobre las rutas del workspace para verificar la integridad de los documentos escritos.

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
