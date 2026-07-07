---
name: alta-autonomo
description: >
  Prepara el alta de trabajador autonomo en Espana: (1) el alta censal en la AEAT mediante el modelo
  036 (declaracion censal en el censo de empresarios, profesionales y retenedores, con epigrafe IAE y
  eleccion de regimen de IVA e IRPF) y (2) el alta en el RETA de la Seguridad Social por el sistema de
  cotizacion segun rendimientos netos previstos, conforme a la Ley 20/2007 del Estatuto del Trabajo
  Autonomo y al RD-ley 13/2022, en su version consolidada vigente verificada en el BOE. Genera hojas de
  datos para los formularios oficiales, la cuota estimada del tramo, el checklist de documentos y las
  sedes y plazos de presentacion. NO usar para altas de sociedades, autonomos societarios o colaboradores
  sin revision, ni para el calculo definitivo de la cuota ni para presentar los tramites de forma automatica.
when_to_use: |
  - El usuario va a darse de alta como autonomo (trabajador por cuenta propia) por primera vez o de nuevo.
  - El usuario necesita preparar el modelo 036 (alta censal en Hacienda) y el alta en el RETA.
  - El usuario quiere saber que epigrafe IAE, regimen de IVA/IRPF y tramo de cuota le corresponden.
  - El usuario pregunta por la tarifa plana, los plazos de alta o la documentacion necesaria.
inputs:
  - datos_interesado: nombre y apellidos, NIF, domicilio fiscal, telefono y correo de contacto
  - actividad: descripcion de la actividad economica que va a ejercer
  - epigrafe_iae: epigrafe del IAE si lo conoce (empresarial o profesional)
  - fecha_inicio: fecha prevista de inicio de la actividad
  - rendimientos_previstos: rendimientos netos mensuales previstos en euros (para el tramo de cotizacion)
  - regimen_iva: regimen de IVA aplicable (general / recargo de equivalencia / exento) si lo conoce
  - regimen_irpf: metodo de estimacion de IRPF (directa simplificada / directa normal / objetiva-modulos)
  - tarifa_plana: si cumple los requisitos de la cuota reducida de inicio de actividad (si / no / desconocido)
  - domicilio_actividad: lugar donde ejerce la actividad, si difiere del domicilio fiscal
outputs:
  - hoja_datos_alta_censal: hoja de datos para el modelo 036 con epigrafe IAE y regimenes, DRAFT
  - hoja_datos_alta_reta: hoja de datos para el alta en RETA con tramo y cuota estimada, DRAFT
  - checklist_documentos: relacion de documentos, sedes y plazos de cada tramite
references:
  - references/censo-036-037-aeat.md
  - references/reta-cotizacion-ingresos-reales.md
  - references/fuentes-y-plazos.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/hoja-datos-alta-censal-036.md
  - assets/hoja-datos-alta-reta.md
---

# Preparar el Alta de Trabajador Autonomo (Censal AEAT + RETA)

> DRAFT — para revision por un gestor o asesor colegiado antes de su presentacion. No constituye asesoramiento fiscal ni laboral.

## Guardrails

1. Verificar siempre en el BOE y en las sedes de la AEAT y la Seguridad Social la normativa, el modelo censal y las cuotas vigentes antes de preparar el tramite. Sin verificacion, no proceder.
2. Si se detecta una version posterior de la Ley 20/2007, del RD-ley 13/2022, del modelo censal o de la tabla de tramos del RETA respecto a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 1). No usar datos desactualizados.
3. Las cuotas y bases del RETA son ORIENTATIVAS: marcar siempre los importes como estimados y advertir de la regularizacion anual por rendimientos reales. Nunca presentar la cuota como definitiva.
4. Recoger el epigrafe IAE, el regimen de IVA y el metodo de IRPF antes de rellenar la hoja de datos. Si el usuario no los conoce, orientar segun la actividad, pero no fijarlos por el sin confirmacion.
5. Respetar el orden y los plazos: el alta censal (036) se presenta ANTES del inicio de la actividad; el alta en el RETA puede solicitarse hasta 60 dias naturales antes del inicio y surte efecto desde la fecha de inicio.
6. Nunca inventar NIF, epigrafes, importes de cuota ni fechas. Los campos sin dato quedan marcados como pendientes.
7. Advertir de la tarifa plana (cuota reducida de inicio de actividad) y de sus requisitos; no darla por aplicable sin confirmar que el usuario los cumple.
8. Indicar siempre el organismo, la sede de presentacion (Import@ss y Sede AEAT) y el medio de identificacion (Cl@ve o certificado digital).

## Procedimiento

### Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, antes de cualquier otra accion)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de preparar el tramite. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la version registrada localmente.** Abrir `references/fuentes-y-plazos.md` y anotar la "Version registrada" de la Ley 20/2007, del RD-ley 13/2022, del modelo censal 036 y del ejercicio de las cuotas del RETA.

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
Y verificar los tramos, cuotas y tarifa plana del ejercicio en curso, y el modelo censal vigente, con:
```
web_search("tabla tramos cuotas RETA autonomos rendimientos netos ejercicio en curso Seguridad Social base minima")
web_search("modelo 036 037 declaracion censal AEAT alta autonomo vigente")
web_search("tarifa plana autonomos cuota reducida inicio actividad requisitos ejercicio en curso")
```

**1.3 — Comparar.** Contrastar la version oficial y las cuotas vigentes con las registradas localmente y con el texto de las references.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o los importes han cambiado, usar las herramientas de escritura (Write/Edit) para:
- Actualizar `references/censo-036-037-aeat.md` si el modelo censal o los regimenes han cambiado (por ejemplo, la supresion del modelo 037 y su integracion en el 036).
- Actualizar `references/reta-cotizacion-ingresos-reales.md` con la tabla de tramos, cuotas y tarifa plana del ejercicio en curso, manteniendo los importes marcados como `[verificar]`.
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-y-plazos.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma, importes y fecha).

No preparar ninguna hoja de datos hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_document` falla (error HTTP, timeout):
```
web_search("Ley 20/2007 Estatuto del Trabajo Autonomo texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente en el BOE ni las cuotas del RETA. La hoja de datos se genera con la version de referencia. Verificar los importes y el modelo manualmente antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no prepara nada hasta recoger estos datos:

**Bloque A — Datos del interesado:**
- Nombre y apellidos, NIF, domicilio fiscal.
- Telefono y correo de contacto a efectos de notificaciones.

**Bloque B — Actividad y epigrafe IAE:**
- Descripcion de la actividad que va a ejercer.
- Epigrafe del IAE, si lo conoce. Si no, orientar segun la actividad (seccion empresarial o profesional) para que el usuario lo confirme.
- Lugar donde ejerce la actividad, si difiere del domicilio fiscal.

**Bloque C — Fecha de inicio:**
"En que fecha prevista va a iniciar la actividad? De ella dependen los plazos del alta censal y del RETA."

**Bloque D — Rendimientos previstos y cuota:**
"Que rendimientos netos mensuales previstos tendra la actividad? Sirven para situarle en el tramo de cotizacion del RETA y estimar la cuota."

**Bloque E — Regimen de IVA e IRPF:**
- Regimen de IVA (general, recargo de equivalencia, exento) segun la actividad.
- Metodo de estimacion del IRPF (estimacion directa simplificada, directa normal o estimacion objetiva por modulos).

**Bloque F — Tarifa plana:**
"Es su primer alta como autonomo, o han pasado al menos dos anos (tres si ya disfruto antes de la bonificacion) desde su ultima alta en el RETA, y no tiene deudas con Hacienda ni con la Seguridad Social? De ello depende que pueda acogerse a la tarifa plana (cuota reducida de inicio)."

### Paso 3 — Validacion previa

Antes de preparar las hojas de datos, validar:

a) **Modelo censal aplicable:** determinar si procede el modelo 036 (universal) o si el usuario debe usar la version simplificada para personas fisicas. Consultar `references/censo-036-037-aeat.md`.

b) **Epigrafe IAE:** confirmar que el epigrafe corresponde a la actividad (empresarial o profesional). Advertir de que puede darse de alta en mas de un epigrafe si ejerce varias actividades.

c) **Tramo de cotizacion:** situar los rendimientos netos previstos en el tramo correspondiente de la tabla vigente y anotar la cuota estimada. Advertir de que el importe es orientativo y se regulariza anualmente.

d) **Tarifa plana:** si el usuario cumple los requisitos, aplicar la cuota reducida y anotar su duracion y condiciones de prorroga. Si no, o si hay duda, no aplicarla y advertir.

e) **Plazos:** confirmar que el alta censal se presenta antes del inicio de la actividad y que el alta en el RETA se solicita en plazo (hasta 60 dias naturales antes del inicio; efectos desde la fecha de inicio).

### Paso 4 — Generacion de las hojas de datos

Generar las dos hojas de datos:
```
draft_markdown(
  template_id: "hoja-datos-alta-censal-036",
  variables: { datos del Bloque A, actividad y epigrafe del Bloque B, fecha del Bloque C, regimenes del Bloque E }
)
draft_markdown(
  template_id: "hoja-datos-alta-reta",
  variables: { datos del Bloque A, fecha del Bloque C, rendimientos y tramo del Bloque D, tarifa plana del Bloque F }
)
```

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado quedan como campo pendiente de completar. Aplicar el estilo de `references/estilo-redaccion-escritos.md`: hoja de datos clara, con los campos ordenados como en el formulario oficial, y checklist accionable.

### Paso 5 — Revision final y advertencias

Verificar que cada hoja de datos generada:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Identifica correctamente al interesado, la actividad y el epigrafe IAE.
- Indica el organismo, la sede de presentacion y el plazo aplicable.
- Marca la cuota del RETA como estimada y advierte de la regularizacion anual.

Entregar las hojas de datos y anadir al final:
```
Advertencias:
1. Estas hojas de datos son un DRAFT generado automaticamente. Deben ser revisadas por un gestor o asesor antes de presentar los tramites.
2. Normativa verificada: [fecha extraida en Paso 1].
3. El alta censal (modelo 036) se presenta en la Sede Electronica de la AEAT ANTES del inicio de la actividad.
4. El alta en el RETA se solicita en Import@ss (Seguridad Social) hasta 60 dias naturales antes del inicio; surte efecto desde la fecha de inicio real.
5. La cuota del RETA indicada es ORIENTATIVA (segun rendimientos previstos) y se regulariza al ano siguiente segun los rendimientos reales comunicados por la AEAT.
6. La tarifa plana requiere cumplir los requisitos vigentes; se solicita marcando la bonificacion en el alta del RETA.
```

## Como NO se usa esta skill

- No usar para el alta de sociedades (SL, SA), que requieren modelo 036 completo, alta en el Registro Mercantil y regimen distinto.
- No usar sin revision para autonomos societarios (administradores/socios) ni autonomos colaboradores: la cotizacion y las bonificaciones difieren.
- No usar para calcular con caracter definitivo la cuota, el IRPF ni el IVA: los importes son orientativos.
- No usar para presentar los tramites de forma automatica: la skill genera el DRAFT y guia la presentacion.
- No usar para bajas, modificaciones censales complejas ni recursos frente a la AEAT o la TGSS: derivar.

## Escalacion

| Situacion | Accion |
|---|---|
| Alta de sociedad, autonomo societario o colaborador | Advertir que excede el alcance y derivar a gestor colegiado |
| Actividad con regimenes especiales de IVA o alta en el ROI/VIES | Verificar con web_search y advertir; puede requerir modelo 036 completo |
| Deudas con la AEAT o la TGSS que impiden la tarifa plana | Advertir de la perdida de la bonificacion y derivar |
| Duda sobre el epigrafe IAE o el metodo de IRPF aplicable | Orientar segun la actividad y recomendar confirmacion profesional |
| Sancion, requerimiento o recurso administrativo asociado | Escalar via escalate_to_attorney |
