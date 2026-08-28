---
name: alta-baja-seguridad-social
description: >
  Prepara altas y bajas en la Seguridad Social (Regimen General) que corresponden al empleador y al
  trabajador por cuenta ajena en Espana: (1) afiliacion inicial y numero de la Seguridad Social (NUSS)
  con el modelo TA.1; (2) inscripcion de empresa y apertura del Codigo de Cuenta de Cotizacion (CCC),
  y sus variaciones o baja, con el modelo TA.6; (3) alta y baja de trabajadores por cuenta ajena en el
  Regimen General por el empleador via Sistema RED o Import@ss; (4) alta y baja de empleadas de hogar
  (Sistema Especial del Regimen General), conforme al texto refundido de la LGSS (RD-legislativo 8/2015)
  y al Reglamento general de inscripcion, afiliacion, altas y bajas (RD 84/1996), en su version consolidada
  vigente verificada en el BOE. Genera la hoja de datos del modelo TA correspondiente, el checklist de
  documentos, el organismo y la via de presentacion y los plazos. NO usar para el alta de autonomos en el
  RETA (usar la skill alta-baja-autonomo), ni para el calculo definitivo de cuotas, expedientes de
  regularizacion, actas de la Inspeccion de Trabajo o recursos ante la TGSS.
when_to_use: |
  - El empleador va a dar de alta o de baja a un trabajador por cuenta ajena en el Regimen General.
  - Un trabajador necesita su afiliacion inicial y numero de la Seguridad Social (NUSS) por primera vez.
  - Una empresa va a inscribirse y abrir su Codigo de Cuenta de Cotizacion (CCC), o darlo de baja.
  - Un empleador de hogar va a dar de alta o de baja a una empleada de hogar.
  - El usuario pregunta por los plazos del alta previa, de la baja o por la documentacion y la via (RED / Import@ss).
inputs:
  - tipo_operacion: alta / baja
  - sujeto: afiliacion inicial (NUSS) / inscripcion de empresa (CCC) / trabajador Regimen General / empleada de hogar
  - datos_empleador: razon social o nombre, CIF o NIF, domicilio, CCC si ya existe
  - datos_trabajador: nombre y apellidos, NIF, NUSS si lo tiene, grupo de cotizacion
  - fecha_efectos: fecha de inicio de la relacion laboral (alta) o de cese (baja)
  - tipo_contrato: modalidad de contrato y tipo de jornada (para el alta)
  - via_presentacion: Sistema RED (autorizado) / Import@ss (sin autorizacion RED) si lo conoce
outputs:
  - hoja_datos_ta: hoja de datos del modelo TA correspondiente (TA.1, TA.6 o alta-baja de trabajador), DRAFT
  - checklist_documentos: relacion de documentos, organismo, via de presentacion y plazo del tramite
references:
  - references/lgss-y-reglamento-afiliacion.md
  - references/tramites-tgss-modelos-ta.md
  - references/plazos-y-sedes.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/template-hoja-datos-afiliacion-ta1.md
  - assets/template-hoja-datos-alta-baja-trabajador.md
  - assets/template-hoja-datos-inscripcion-empresa-ccc.md
---

# Preparar Altas y Bajas en la Seguridad Social (Regimen General y Empleador)

> DRAFT — para revision por un gestor o asesor laboral colegiado antes de su presentacion. No constituye asesoramiento laboral.

## Guardrails

1. Verificar siempre en el BOE y en la sede de la TGSS la normativa, el modelo TA y los plazos vigentes antes de preparar el tramite. Sin verificacion, no proceder.
2. Si se detecta una version posterior del texto refundido de la LGSS (RD-legislativo 8/2015), del RD 84/1996 o de los modelos TA respecto a la registrada en las references, actualizar los archivos del plugin antes de preparar el tramite (ver Paso 1). No usar datos desactualizados.
3. Preguntar SIEMPRE, antes de preparar nada, el tipo de operacion (alta / baja) y el sujeto (afiliacion inicial, inscripcion de empresa, trabajador del Regimen General o empleada de hogar). De esa combinacion depende el modelo TA y la via.
4. Respetar los plazos: el alta del trabajador es PREVIA al inicio de la actividad (puede solicitarse hasta 60 dias naturales antes); la baja se comunica en los 3 dias naturales siguientes al cese. Para empleadas de hogar la baja se comunica en los 6 dias naturales siguientes (Import@ss admite hacerla en 3). Advertir del alta fuera de plazo.
5. Distinguir la via segun quien presenta: las empresas y los autorizados actuan por el Sistema RED (obligatorio para empresas del Regimen General); un empleador de hogar o un particular sin autorizacion RED usa Import@ss.
6. Esta skill cubre el Regimen General y al empleador. NO cubre el alta en el RETA (autonomos): si el usuario quiere darse de alta como autonomo, derivar a la skill alta-baja-autonomo.
7. Nunca inventar NIF, CIF, NUSS, CCC, grupos de cotizacion, codigos de contrato ni fechas. Los campos sin dato quedan marcados como pendientes.
8. Indicar siempre el organismo (TGSS), la via de presentacion (Sistema RED / Import@ss) y el medio de identificacion (certificado digital, DNI-e o Cl@ve).

## Procedimiento

### Paso 1 — Verificacion normativa

**1.1 — Consultar la version registrada en references.** Consultar el archivo `plazos-y-sedes.md` directamente desde el bloque `<document kind="references-collection">` de tu system prompt y anotar la "Version registrada" del texto refundido de la LGSS, del RD 84/1996 y de los modelos TA, y los plazos registrados.

**1.2 — Consultar la fuente oficial vigente en vivo.** Invocar:
```
web_search("BOE-A-2015-11724 Real Decreto Legislativo 8/2015 LGSS texto refundido afiliacion altas bajas")
web_search("BOE-A-1996-4396 Real Decreto 84/1996 Reglamento General inscripcion empresas afiliacion")
```
Y verificar los modelos TA, la via y los plazos vigentes con:
```
web_search("modelo TA.1 afiliacion numero Seguridad Social TA.6 inscripcion empresa codigo cuenta cotizacion TGSS vigente")
web_search("alta baja trabajador Regimen General Sistema RED Import@ss plazo alta previa baja 3 dias naturales")
web_search("alta baja empleada de hogar Sistema Especial Regimen General Import@ss plazos vigente")
```

**1.3 — Comparar.** Contrastar la version oficial, los modelos y los plazos vigentes con los registrados en `plazos-y-sedes.md` y con las referencias del prompt (`lgss-y-reglamento-afiliacion.md`, `tramites-tgss-modelos-ta.md`).

**1.4 — Aplicar cambios normativos.** Si la version oficial es posterior o los modelos o plazos han cambiado:
- Aplicar en memoria la redaccion y circuitos vigentes para adaptar las hojas de datos.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma, modelo o plazo, y fecha).

**1.5 — Fallback si la busqueda no es accesible.** Si la busqueda web falla: usar las references cargadas en el prompt como respaldo y notificar al usuario:
"No se pudo verificar en vivo la version vigente de la LGSS en el BOE ni los modelos TA. La hoja de datos se genera con la version de referencia. Verificar el modelo y los plazos manualmente antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no prepara nada hasta recoger estos datos:

**Bloque A — Tipo de operacion y sujeto (SIEMPRE primero):**
"Que operacion desea preparar: (1) un alta o (2) una baja? Y a quien afecta: (a) afiliacion inicial y numero de la Seguridad Social de un trabajador, (b) inscripcion de empresa y apertura del Codigo de Cuenta de Cotizacion, (c) alta o baja de un trabajador por cuenta ajena en el Regimen General, o (d) alta o baja de una empleada de hogar?"

De la respuesta depende el modelo TA, la via y las siguientes preguntas. Si el sujeto es un autonomo (RETA), detener y derivar a la skill `alta-baja-autonomo`.

**Bloque B — Datos del empleador (si aplica: inscripcion de empresa, trabajador o empleada de hogar):**
- Razon social o nombre y apellidos, CIF o NIF, domicilio.
- Codigo de Cuenta de Cotizacion (CCC) si ya esta inscrito. Si no lo tiene, primero procede la inscripcion de empresa (modelo TA.6).

**Bloque C — Datos del trabajador (si aplica: afiliacion, trabajador o empleada de hogar):**
- Nombre y apellidos, NIF.
- Numero de la Seguridad Social (NUSS) si ya lo tiene. Si no lo tiene, primero procede la afiliacion inicial (modelo TA.1).
- Grupo de cotizacion segun la categoria profesional.

**Bloque D — Fecha de efectos:**
- En un alta: fecha prevista de inicio de la relacion laboral (el alta debe ser previa).
- En una baja: fecha de cese en el trabajo (el plazo de comunicacion cuenta desde el dia siguiente).

**Bloque E — Tipo de contrato y jornada (solo en altas de trabajador o empleada de hogar):**
- Modalidad de contrato (indefinido, temporal, fijo-discontinuo) y su codigo.
- Tipo de jornada (completa o parcial) y, en su caso, horas.

**Bloque F — Via de presentacion:**
"Presenta como empresa o autorizado del Sistema RED, o como empleador de hogar o particular sin autorizacion RED (via Import@ss)?"

### Paso 3 — Validacion previa

Antes de preparar la hoja de datos, validar:

a) **Orden logico de los tramites.** Un trabajador sin NUSS necesita primero la afiliacion inicial (TA.1). Un empleador sin CCC necesita primero la inscripcion de empresa (TA.6). Solo despues procede el alta del trabajador. Advertir si falta un tramite previo.

b) **Modelo TA aplicable.** Determinar el modelo segun el sujeto: TA.1 (afiliacion / NUSS), TA.6 (inscripcion de empresa / CCC y sus variaciones o baja), alta o baja de trabajador del Regimen General (via RED / Import@ss), y empleada de hogar (Sistema Especial, formulario propio). Consultar `references/tramites-tgss-modelos-ta.md`.

c) **Plazo.** Confirmar que el alta se prepara con caracter previo al inicio (hasta 60 dias naturales antes) y que la baja se comunica en plazo (3 dias naturales para el Regimen General; 6 dias para empleadas de hogar, admitiendo Import@ss 3 dias). Advertir del alta o la baja fuera de plazo y de sus consecuencias.

d) **Via de presentacion.** Confirmar la via: Sistema RED para empresas y autorizados (obligatorio en el Regimen General); Import@ss para el empleador de hogar o el particular sin autorizacion RED.

e) **Grupo de cotizacion y contrato.** En el alta de un trabajador, confirmar el grupo de cotizacion y el codigo de contrato. Si el usuario no los conoce, orientar segun la categoria, pero no fijarlos por el sin confirmacion.

### Paso 4 — Generacion de la hoja de datos

Tomar la plantilla correspondiente directamente desde el bloque `<document kind="assets-collection">` de tu system prompt:
- Afiliacion inicial / NUSS: `template-hoja-datos-afiliacion-ta1.md`
- Inscripcion de empresa / CCC (y variaciones o baja): `template-hoja-datos-inscripcion-empresa-ccc.md`
- Alta o baja de trabajador del Regimen General o de empleada de hogar: `template-hoja-datos-alta-baja-trabajador.md`

Generar la hoja de datos en el workspace invocando `create_file`:
```
create_file(
  relative_file_path: "hoja_datos_seguridad_social.md",
  file_content: "... contenido completo adaptado segun modelo TA y datos recogidos en los bloques A-F ..."
)
```

### Reglas de Adaptación y Cláusulas Condicionales:

1. **Afiliación Previa y NUSS (en TA.1):**
   - *Si el trabajador ya dispone de NUSS (`{{nuss}}`):* Hacer constar que no procede nueva afiliación inicial, sino en su caso variación de datos censales.

2. **Tipo de Operación y Régimen (en Alta/Baja de Trabajador):**
   - *Si la operación es un ALTA:* Indicar los datos contractuales (tipo de contrato, CNO, grupo de cotización, coeficiente de jornada) y recordar el plazo preceptivo previo (hasta 60 días antes del inicio real).
   - *Si el sujeto es empleada de hogar:* Especificar la retribución mensual pactada (`{{retribucion}}`) y número de horas semanales (`{{horas_semanales}}`), determinantes de la base de cotización en el Sistema Especial de Empleados de Hogar.
   - *Si la operación es una BAJA:* Indicar la causa de baja (fin de contrato, despido, baja voluntaria) y el plazo reglamentario: 3 días naturales siguientes al cese para Régimen General, y 6 días naturales para empleadas de hogar.

3. **Operaciones sobre Código de Cuenta de Cotización (en TA.6 / TA.7):**
   - *Inscripción de Empresa / Primer CCC:* Apertura previa al inicio con trabajadores.
   - *Variación de Datos:* Detallar la modificación requerida sobre el CCC (`{{ccc}}`: `{{detalle_variacion}}`).
   - *Baja de CCC:* Solicitar baja del CCC (`{{ccc}}`) con efectos `{{fecha_efectos}}` tras tramitar la baja de la totalidad de la plantilla.

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado quedan como `[DATO — PENDIENTE DE COMPLETAR]`.

Aplicar las directivas de `estilo-redaccion-escritos.md` (disponible directamente en `<document kind="references-collection">` del prompt): hoja de datos clara, con los campos ordenados como en el modelo TA oficial, y checklist accionable.

Tras guardar el archivo en disco del workspace, invocar `read_file` exclusivamente sobre la ruta del workspace para verificar la integridad del documento escrito.

### Paso 5 — Revision final y advertencias

Verificar que la hoja de datos generada:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Identifica correctamente al empleador, al trabajador, el CCC y el NUSS cuando proceda.
- Indica el organismo (TGSS), la via de presentacion (Sistema RED / Import@ss) y el plazo aplicable.
- Resuelve correctamente los bloques condicionales segun alta o baja.

Entregar la hoja de datos y anadir al final:
```
Advertencias:
1. Esta hoja de datos es un DRAFT generado automaticamente. Debe ser revisada por un gestor o asesor laboral antes de presentar el tramite.
2. Normativa verificada: [fecha extraida en Paso 1].
3. El alta del trabajador debe presentarse con caracter PREVIO al inicio de la actividad (hasta 60 dias naturales antes); surte efecto desde la fecha de inicio real.
4. La baja se comunica en los 3 dias naturales siguientes al cese (6 dias naturales para empleadas de hogar; Import@ss admite 3).
5. Las empresas del Regimen General presentan altas, bajas y variaciones por el Sistema RED; el empleador de hogar o el particular sin autorizacion RED, por Import@ss.
6. La afiliacion (TA.1) y la inscripcion de empresa (TA.6) son tramites previos: sin NUSS del trabajador o sin CCC del empleador no puede tramitarse el alta.
```

## Como NO se usa esta skill

- No usar para el alta o la baja de autonomos en el RETA: usar la skill `alta-baja-autonomo`.
- No usar para el calculo definitivo de cuotas, bases o bonificaciones de cotizacion: los importes se verifican aparte.
- No usar para expedientes de regularizacion, reclamaciones de deuda, aplazamientos o devolucion de cuotas ante la TGSS.
- No usar para actas de la Inspeccion de Trabajo, recursos administrativos ni procedimientos sancionadores.
- No usar para presentar los tramites de forma automatica: la skill genera el DRAFT y guia la presentacion.

## Escalacion

| Situacion | Accion |
|---|---|
| Alta o baja de autonomo (RETA) | Derivar a la skill alta-baja-autonomo |
| Alta fuera de plazo o baja con efectos retroactivos con posible recargo | Advertir de las consecuencias y derivar a gestor colegiado |
| Grupo de cotizacion, codigo de contrato o bonificacion dudosos | Orientar segun la categoria y recomendar confirmacion profesional |
| Regularizacion, reclamacion de deuda o aplazamiento con la TGSS | Advertir que excede el alcance y derivar |
| Acta de la Inspeccion de Trabajo, sancion o recurso administrativo | Advertir y derivar a gestor colegiado o abogado laboralista |
