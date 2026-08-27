---
name: alta-baja-autonomo
description: >
  Prepara el alta Y la baja de trabajador autonomo en Espana: (1) el alta o la baja censal en la AEAT
  mediante el modelo 036 (declaracion censal en el censo de empresarios, profesionales y retenedores;
  en el alta con epigrafe IAE y eleccion de regimen de IVA e IRPF; en la baja con la fecha efectiva de
  cese y sus efectos en IVA e IRPF) y (2) el alta o la baja en el RETA de la Seguridad Social (en el alta,
  eleccion de base segun rendimientos netos previstos; en la baja, comunicacion del cese y sus efectos en
  la cuota), conforme a la Ley 20/2007 del Estatuto del Trabajo Autonomo y al RD-ley 13/2022, en su version
  consolidada vigente verificada en el BOE. Genera hojas de datos para los formularios oficiales, la cuota
  estimada del tramo, el checklist de documentos y las sedes y plazos de presentacion. NO usar para altas
  ni bajas de sociedades, autonomos societarios o colaboradores sin revision, ni para el calculo definitivo
  de la cuota ni para presentar los tramites de forma automatica.
when_to_use: |
  - El usuario va a darse de alta como autonomo (trabajador por cuenta propia) por primera vez o de nuevo.
  - El usuario va a cesar su actividad y darse de baja como autonomo (baja censal 036 y baja en el RETA).
  - El usuario necesita preparar el modelo 036 (alta o baja censal en Hacienda) y el alta o la baja en el RETA.
  - El usuario quiere saber que epigrafe IAE, regimen de IVA/IRPF y tramo de cuota le corresponden.
  - El usuario pregunta por la tarifa plana, los plazos de alta o de baja, los efectos del cese en la cuota o la documentacion necesaria.
inputs:
  - tipo_operacion: tipo de tramite (alta / baja)
  - datos_interesado: nombre y apellidos, NIF, domicilio fiscal, telefono y correo de contacto
  - actividad: descripcion de la actividad economica (alta: que va a ejercer; baja: que cesa)
  - epigrafe_iae: epigrafe del IAE si lo conoce (empresarial o profesional)
  - fecha_inicio: fecha prevista de inicio de la actividad (solo para el alta)
  - fecha_cese: fecha de cese de la actividad (solo para la baja)
  - rendimientos_previstos: rendimientos netos mensuales previstos en euros (alta: para el tramo de cotizacion)
  - regimen_iva: regimen de IVA aplicable (general / recargo de equivalencia / exento) si lo conoce
  - regimen_irpf: metodo de estimacion de IRPF (directa simplificada / directa normal / objetiva-modulos)
  - tarifa_plana: si cumple los requisitos de la cuota reducida de inicio de actividad (si / no / desconocido)
  - domicilio_actividad: lugar donde ejerce la actividad, si difiere del domicilio fiscal
  - obligaciones_pendientes: declaraciones o cuotas del periodo aun no presentadas (baja: para el aviso de cierre fiscal)
outputs:
  - hoja_datos_alta_censal: hoja de datos para el alta en el modelo 036 con epigrafe IAE y regimenes, DRAFT
  - hoja_datos_alta_reta: hoja de datos para el alta en RETA con tramo y cuota estimada, DRAFT
  - hoja_datos_baja_censal: hoja de datos para la baja en el modelo 036 con fecha de cese y efectos en IVA/IRPF, DRAFT
  - hoja_datos_baja_reta: hoja de datos para la baja en el RETA con fecha de cese y efectos en la cuota, DRAFT
  - checklist_documentos: relacion de documentos, sedes y plazos de cada tramite
references:
  - references/censo-036-037-aeat.md
  - references/reta-cotizacion-ingresos-reales.md
  - references/fuentes-y-plazos.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/hoja-datos-alta-censal-036.md
  - assets/hoja-datos-alta-reta.md
  - assets/hoja-datos-baja-censal-036.md
  - assets/hoja-datos-baja-reta.md
---

# Preparar el Alta o la Baja de Trabajador Autonomo (Censal AEAT + RETA)

> DRAFT — para revision por un gestor o asesor colegiado antes de su presentacion. No constituye asesoramiento fiscal ni laboral.

## Guardrails

1. Verificar siempre en el BOE y en las sedes de la AEAT y la Seguridad Social la normativa, el modelo censal, las cuotas y los plazos vigentes antes de preparar el tramite. Sin verificacion, no proceder.
2. Si se detecta una version posterior de la Ley 20/2007, del RD-ley 13/2022, del modelo censal, de la tabla de tramos del RETA o de los plazos de alta/baja respecto a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 1). No usar datos desactualizados.
3. Las cuotas y bases del RETA son ORIENTATIVAS: marcar siempre los importes como estimados y advertir de la regularizacion anual por rendimientos reales. Nunca presentar la cuota como definitiva.
4. Determinar SIEMPRE al inicio si el tramite es un ALTA o una BAJA (Paso 2, Bloque 0). No mezclar los dos flujos: cada uno tiene datos, plazos y assets distintos.
5. En el ALTA: recoger el epigrafe IAE, el regimen de IVA y el metodo de IRPF antes de rellenar la hoja de datos. Si el usuario no los conoce, orientar segun la actividad, pero no fijarlos por el sin confirmacion.
6. En el ALTA: respetar el orden y los plazos: el alta censal (036) se presenta ANTES del inicio de la actividad; el alta en el RETA puede solicitarse hasta 60 dias naturales antes del inicio y surte efecto desde la fecha de inicio.
7. En la BAJA: respetar los plazos de cese. La baja en el RETA se comunica en los 3 dias naturales siguientes al cese; la baja censal (036) en el plazo de 1 mes desde el cese. Advertir de los efectos en la cuota y de las obligaciones fiscales pendientes.
8. Nunca inventar NIF, epigrafes, importes de cuota ni fechas. Los campos sin dato quedan marcados como pendientes.
9. Advertir de la tarifa plana (cuota reducida de inicio de actividad) y de sus requisitos; no darla por aplicable sin confirmar que el usuario los cumple. No aplica a la baja.
10. Indicar siempre el organismo, la sede de presentacion (Import@ss y Sede AEAT) y el medio de identificacion (Cl@ve o certificado digital).

## Procedimiento

### Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, antes de cualquier otra accion)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de preparar el tramite. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la version registrada localmente.** Abrir `references/fuentes-y-plazos.md` y anotar la "Version registrada" de la Ley 20/2007, del RD-ley 13/2022, del modelo censal 036 y del ejercicio de las cuotas del RETA, y los plazos de alta y de baja.

**1.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409",
  format: "text"
)
```
Extraer la redaccion vigente de la Ley 20/2007 (Estatuto del Trabajo Autonomo), en especial los arts. 30 a 38 bis (cotizacion). Consultar tambien el RD-ley 13/2022:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482",
  format: "text"
)
```
Y verificar los tramos, cuotas y tarifa plana del ejercicio en curso, el modelo censal vigente y los plazos de alta y de baja, con:
```
web_search("tabla tramos cuotas RETA autonomos rendimientos netos ejercicio en curso Seguridad Social base minima")
web_search("modelo 036 037 declaracion censal AEAT alta baja autonomo vigente casilla 150 152")
web_search("tarifa plana autonomos cuota reducida inicio actividad requisitos ejercicio en curso")
web_search("baja autonomo RETA plazo 3 dias naturales cese efectos cuota mes completo Import@ss")
```

**1.3 — Comparar.** Contrastar la version oficial, las cuotas y los plazos vigentes con los registrados localmente y con el texto de las references.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o los importes o plazos han cambiado, usar las herramientas de escritura (Write/Edit) para:
- Actualizar `references/censo-036-037-aeat.md` si el modelo censal, los regimenes o el procedimiento de baja censal han cambiado (por ejemplo, la supresion del modelo 037 y su integracion en el 036, o las casillas de baja).
- Actualizar `references/reta-cotizacion-ingresos-reales.md` con la tabla de tramos, cuotas, tarifa plana y reglas de efectos de la baja del ejercicio en curso, manteniendo los importes marcados como `[verificar]`.
- Actualizar la tabla "Version registrada", los plazos de alta y de baja y las fechas en `references/fuentes-y-plazos.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma, importes, plazos y fecha).

No preparar ninguna hoja de datos hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_document` falla (error HTTP, timeout):
```
web_search("Ley 20/2007 Estatuto del Trabajo Autonomo texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente en el BOE ni las cuotas y plazos del RETA. La hoja de datos se genera con la version de referencia. Verificar los importes, el modelo y los plazos manualmente antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no prepara nada hasta recoger estos datos.

**Bloque 0 — Tipo de operacion (SIEMPRE el primero):**
"Desea preparar (1) el ALTA como autonomo (inicio de actividad) o (2) la BAJA como autonomo (cese de actividad)?"

Segun la respuesta, seguir la rama A (alta) o la rama B (baja).

#### Rama A — ALTA

**Bloque A1 — Datos del interesado:**
- Nombre y apellidos, NIF, domicilio fiscal.
- Telefono y correo de contacto a efectos de notificaciones.

**Bloque A2 — Actividad y epigrafe IAE:**
- Descripcion de la actividad que va a ejercer.
- Epigrafe del IAE, si lo conoce. Si no, orientar segun la actividad (seccion empresarial o profesional) para que el usuario lo confirme.
- Lugar donde ejerce la actividad, si difiere del domicilio fiscal.

**Bloque A3 — Fecha de inicio:**
"En que fecha prevista va a iniciar la actividad? De ella dependen los plazos del alta censal y del RETA."

**Bloque A4 — Rendimientos previstos y cuota:**
"Que rendimientos netos mensuales previstos tendra la actividad? Sirven para situarle en el tramo de cotizacion del RETA y estimar la cuota."

**Bloque A5 — Regimen de IVA e IRPF:**
- Regimen de IVA (general, recargo de equivalencia, exento) segun la actividad.
- Metodo de estimacion del IRPF (estimacion directa simplificada, directa normal o estimacion objetiva por modulos).

**Bloque A6 — Tarifa plana:**
"Es su primer alta como autonomo, o han pasado al menos dos anos (tres si ya disfruto antes de la bonificacion) desde su ultima alta en el RETA, y no tiene deudas con Hacienda ni con la Seguridad Social? De ello depende que pueda acogerse a la tarifa plana (cuota reducida de inicio)."

#### Rama B — BAJA

**Bloque B1 — Datos del interesado:**
- Nombre y apellidos, NIF, domicilio fiscal.
- Telefono y correo de contacto a efectos de notificaciones.

**Bloque B2 — Actividad que cesa:**
- Descripcion de la actividad y epigrafe(s) IAE en que estaba dado de alta.
- Si cesa TODAS sus actividades o solo alguna (baja parcial en un epigrafe frente a baja total como autonomo).

**Bloque B3 — Fecha de cese:**
"En que fecha ha cesado o va a cesar la actividad? De ella dependen los plazos de la baja censal (1 mes) y de la baja en el RETA (3 dias naturales) y los efectos en la cuota."

**Bloque B4 — Regimen fiscal de origen:**
- Regimen de IVA en que tributaba (general, recargo de equivalencia, exento, simplificado).
- Metodo de estimacion del IRPF (directa simplificada, directa normal, objetiva por modulos).
- Sirven para determinar las ultimas declaraciones a presentar tras el cese.

**Bloque B5 — Obligaciones pendientes:**
"Tiene alguna declaracion o cuota del periodo aun sin presentar (ultimo IVA modelo 303, resumen anual 390, pago fraccionado de IRPF 130/131, retenciones 111/115, resumen 190/180) o alguna deuda con la AEAT o la TGSS? Sirve para el aviso de cierre fiscal."

### Paso 3 — Validacion previa

Antes de preparar las hojas de datos, validar segun la rama.

#### Rama A — ALTA

a) **Modelo censal aplicable:** determinar si procede el modelo 036 (universal) o su version simplificada para personas fisicas. Consultar `references/censo-036-037-aeat.md`.

b) **Epigrafe IAE:** confirmar que el epigrafe corresponde a la actividad (empresarial o profesional). Advertir de que puede darse de alta en mas de un epigrafe si ejerce varias actividades.

c) **Tramo de cotizacion:** situar los rendimientos netos previstos en el tramo correspondiente de la tabla vigente y anotar la cuota estimada. Advertir de que el importe es orientativo y se regulariza anualmente.

d) **Tarifa plana:** si el usuario cumple los requisitos, aplicar la cuota reducida y anotar su duracion y condiciones de prorroga. Si no, o si hay duda, no aplicarla y advertir.

e) **Plazos:** confirmar que el alta censal se presenta antes del inicio de la actividad y que el alta en el RETA se solicita en plazo (hasta 60 dias naturales antes del inicio; efectos desde la fecha de inicio).

#### Rama B — BAJA

a) **Alcance del cese:** confirmar si es una baja total como autonomo (afecta a censo y RETA) o una modificacion censal (baja de un epigrafe manteniendo actividad). Si es solo modificacion, no procede la baja en el RETA: advertir y ajustar.

b) **Modelo censal de baja:** el cese se comunica en el modelo 036 marcando la causa de baja (casilla 150) y la fecha efectiva del cese (casilla 152). Consultar `references/censo-036-037-aeat.md`.

c) **Plazos de baja:** confirmar que la baja en el RETA se comunica en los 3 dias naturales siguientes al cese y la baja censal (036) en el plazo de 1 mes desde el cese. Advertir si el plazo ya ha vencido o esta a punto de vencer.

d) **Efectos en la cuota del RETA:** desde el sistema de cotizacion por rendimientos reales, las tres primeras bajas de cada ano natural surten efecto desde el dia del cese (se cotiza solo por los dias trabajados); a partir de la cuarta baja del mismo ano, se cotiza el mes completo. Si la baja se comunica fuera de plazo, surte efecto la fecha de presentacion y se generan cuotas hasta entonces. Marcar como `[verificar]` y advertir.

e) **Obligaciones fiscales pendientes:** identificar las ultimas declaraciones a presentar tras el cese (ultimo modelo 303 y resumen anual 390 de IVA; ultimo pago fraccionado 130/131 y declaracion anual de IRPF; resumen 190/180 de retenciones si procedia). Advertir de que la baja censal no exime de presentarlas ni de saldar deudas pendientes.

### Paso 4 — Generacion de las hojas de datos

**Rama A — ALTA.** Generar las dos hojas de datos del alta:
```
draft_markdown(
  template_id: "hoja-datos-alta-censal-036",
  variables: { datos del Bloque A1, actividad y epigrafe del Bloque A2, fecha del Bloque A3, regimenes del Bloque A5 }
)
draft_markdown(
  template_id: "hoja-datos-alta-reta",
  variables: { datos del Bloque A1, fecha del Bloque A3, rendimientos y tramo del Bloque A4, tarifa plana del Bloque A6 }
)
```

**Rama B — BAJA.** Generar las dos hojas de datos de la baja:
```
draft_markdown(
  template_id: "hoja-datos-baja-censal-036",
  variables: { datos del Bloque B1, actividad y epigrafe del Bloque B2, fecha de cese del Bloque B3, regimenes de origen del Bloque B4, obligaciones del Bloque B5 }
)
draft_markdown(
  template_id: "hoja-datos-baja-reta",
  variables: { datos del Bloque B1, fecha de cese del Bloque B3, efectos en la cuota del Paso 3 }
)
```

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado quedan como campo pendiente de completar. Aplicar el estilo de `references/estilo-redaccion-escritos.md`: hoja de datos clara, con los campos ordenados como en el formulario oficial, y checklist accionable.

### Paso 5 — Revision final y advertencias

Verificar que cada hoja de datos generada:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Identifica correctamente al interesado, la actividad y el epigrafe IAE.
- Indica el organismo, la sede de presentacion y el plazo aplicable.
- En el alta, marca la cuota del RETA como estimada y advierte de la regularizacion anual; en la baja, advierte de los efectos en la cuota y de las obligaciones pendientes.

Entregar las hojas de datos y anadir al final el bloque de advertencias segun la rama.

**Rama A — ALTA:**
```
Advertencias:
1. Estas hojas de datos son un DRAFT generado automaticamente. Deben ser revisadas por un gestor o asesor antes de presentar los tramites.
2. Normativa verificada: [fecha extraida en Paso 1].
3. El alta censal (modelo 036) se presenta en la Sede Electronica de la AEAT ANTES del inicio de la actividad.
4. El alta en el RETA se solicita en Import@ss (Seguridad Social) hasta 60 dias naturales antes del inicio; surte efecto desde la fecha de inicio real.
5. La cuota del RETA indicada es ORIENTATIVA (segun rendimientos previstos) y se regulariza al ano siguiente segun los rendimientos reales comunicados por la AEAT.
6. La tarifa plana requiere cumplir los requisitos vigentes; se solicita marcando la bonificacion en el alta del RETA.
```

**Rama B — BAJA:**
```
Advertencias:
1. Estas hojas de datos son un DRAFT generado automaticamente. Deben ser revisadas por un gestor o asesor antes de presentar los tramites.
2. Normativa verificada: [fecha extraida en Paso 1].
3. La baja en el RETA se comunica en Import@ss (Seguridad Social) en los 3 dias naturales siguientes al cese de la actividad.
4. La baja censal (modelo 036, casilla 150) se presenta en la Sede Electronica de la AEAT en el plazo de 1 mes desde el cese; la fecha efectiva de baja se consigna en la casilla 152.
5. Efectos en la cuota: las tres primeras bajas del ano natural surten efecto desde el dia del cese (cotizacion por dias); a partir de la cuarta, se cotiza el mes completo. Fuera de plazo, la baja surte efecto la fecha de presentacion.
6. La baja NO exime de presentar las ultimas declaraciones del periodo (IVA modelo 303 y resumen 390; IRPF pago fraccionado 130/131 y declaracion anual; retenciones 111/115 y resumen 190/180 si procedian) ni de saldar deudas pendientes con la AEAT o la TGSS.
```

## Como NO se usa esta skill

- No usar para el alta ni la baja de sociedades (SL, SA), que requieren modelo 036 completo, tramites registrales y regimen distinto.
- No usar sin revision para autonomos societarios (administradores/socios) ni autonomos colaboradores: la cotizacion y las bonificaciones difieren.
- No usar para calcular con caracter definitivo la cuota, el IRPF ni el IVA: los importes son orientativos.
- No usar para presentar los tramites de forma automatica: la skill genera el DRAFT y guia la presentacion.
- No usar para modificaciones censales complejas, recursos frente a la AEAT o la TGSS ni para la prestacion por cese de actividad (paro del autonomo): derivar.

## Escalacion

| Situacion | Accion |
|---|---|
| Alta o baja de sociedad, autonomo societario o colaborador | Advertir que excede el alcance y derivar a gestor colegiado |
| Actividad con regimenes especiales de IVA o alta en el ROI/VIES | Verificar con web_search y advertir; puede requerir modelo 036 completo |
| Deudas con la AEAT o la TGSS que impiden la tarifa plana o complican la baja | Advertir y derivar |
| Duda sobre el epigrafe IAE o el metodo de IRPF aplicable | Orientar segun la actividad y recomendar confirmacion profesional |
| Baja ligada a la solicitud de la prestacion por cese de actividad | Advertir que la prestacion excede el alcance de la skill y derivar |
| Sancion, requerimiento o recurso administrativo asociado | Advertir y derivar a gestor colegiado o abogado |
