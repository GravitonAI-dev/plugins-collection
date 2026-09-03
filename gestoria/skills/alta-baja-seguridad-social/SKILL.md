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
  vigente verificada en el BOE. Opera bajo el flujo de 5 fases canonicas con clasificacion HITL, consulta de assets,
  creacion zero-vacios en workspace y edicion incremental seccion a seccion. NO usar para el alta de autonomos en el
  RETA (usar la skill alta-baja-autonomo), ni para el calculo definitivo de cuotas, expedientes de
  regularizacion, actas de la Inspeccion de Trabajo o recursos ante la TGSS.
when_to_use: |
  - El empleador va a dar de alta o de baja a un trabajador por cuenta ajena en el Regimen General.
  - Un trabajador necesita su afiliacion inicial y numero de la Seguridad Social (NUSS) por primera vez.
  - Una empresa va a inscribirse y abrir su Codigo de Cuenta de Cotizacion (CCC), o darlo de baja.
  - Un empleador de hogar va a dar de alta o de baja a una empleada de hogar.
  - El usuario pregunta por los plazos del alta previa, de la baja o por la documentacion y la via (RED / Import@ss).
inputs:
  - tipo_operacion: alta / baja (V1)
  - tipo_sujeto_tramite: cuenta_ajena_regimen_general / empleada_hogar / afiliacion_nuss_ta1 / inscripcion_empresa_ccc_ta6 (V2)
  - naturaleza_empleador: persona_fisica / persona_juridica (V3)
  - naturaleza_trabajador: persona_fisica (V4)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
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

# Preparar Altas y Bajas en la Seguridad Social (Régimen General y Empleador)

> DRAFT — para revisión por un gestor administrativo o asesor laboral colegiado antes de su presentación oficial. No constituye asesoramiento laboral definitivo ni representación técnica ante la TGSS.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para preparar la afiliación, inscripción o alta/baja de trabajadores en la Tesorería General de la Seguridad Social (TGSS).

### Vectores de Estado (Uso Estrictamente Interno):
Para garantizar un enrutamiento determinista y el cumplimiento estricto de la normativa de la Seguridad Social, el asistente resuelve y mantiene internamente en memoria los siguientes vectores de estado:
- **V1 (Tipo de Operación):** `alta` | `baja`.
- **V2 (Tipo de Sujeto / Trámite):** `cuenta_ajena_regimen_general` | `empleada_hogar` | `afiliacion_nuss_ta1` | `inscripcion_empresa_ccc_ta6`.
- **V3 (Naturaleza del Empleador):** `persona_fisica` | `persona_juridica`.
- **V4 (Naturaleza del Trabajador):** `persona_fisica`.
- **V5 (Origen Plantilla / Asset):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`, `V4`, `V5`) y los resúmenes de validación con marcas técnicas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

Tu primer objetivo es determinar el sujeto pasivo del trámite y el modelo aplicable.

### 1.1 Escucha Activa Previa
Antes de invocar formularios, evalúa el mensaje inicial del usuario:
- Si el usuario ya indicó de forma inequívoca el trámite concreto (ej. afiliar a un trabajador nuevo que no tiene NUSS, dar de alta un contrato de trabajo, dar de alta a una empleada de hogar o inscribir una empresa), registra los vectores y avanza a la **Fase 2**.
- Si falta determinar la operación principal (`V1`) o el sujeto del trámite (`V2`), invoca de inmediato la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "tipo_operacion",
      "rationale": "Resolver V1 para determinar si se preparan trámites de alta/afiliación o cese/baja.",
      "question": "¿Qué tipo de trámite laboral desea preparar?",
      "options": [
        {"id": "alta", "label": "Alta laboral, afiliación inicial o apertura de cuenta de cotización"},
        {"id": "baja", "label": "Baja de trabajador o cierre de cuenta de cotización"}
      ]
    },
    {
      "id": "tipo_sujeto_tramite",
      "rationale": "Resolver V2 para determinar el formulario oficial de la TGSS y el circuito telemático.",
      "question": "¿A qué sujeto o ámbito corresponde el trámite?",
      "options": [
        {"id": "cuenta_ajena_regimen_general", "label": "Trabajador por cuenta ajena en Régimen General (empresa)"},
        {"id": "empleada_hogar", "label": "Empleado/a de hogar (Sistema Especial del Régimen General)"},
        {"id": "afiliacion_nuss_ta1", "label": "Afiliación inicial y asignación de NUSS del trabajador (Modelo TA.1)"},
        {"id": "inscripcion_empresa_ccc_ta6", "label": "Inscripción de empresa y apertura de CCC (Modelo TA.6)"}
      ]
    }
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V2 = afiliacion_nuss_ta1`:**
  - Hoja de datos propuesta: `assets/template-hoja-datos-afiliacion-ta1.md`. Proceder a la **Fase 2**.
- **Si `V2 = inscripcion_empresa_ccc_ta6`:**
  - Hoja de datos propuesta: `assets/template-hoja-datos-inscripcion-empresa-ccc.md`. Proceder a la **Fase 2**.
- **Si `V2 = cuenta_ajena_regimen_general` o `empleada_hogar`:**
  - Hoja de datos propuesta: `assets/template-hoja-datos-alta-baja-trabajador.md`. Proceder a la **Fase 2**.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `lgss-y-reglamento-afiliacion.md`, `tramites-tgss-modelos-ta.md` y `plazos-y-sedes.md`.
2. Opcionalmente verifica mediante `web_search` el marco de plazos del RD 84/1996 y la LGSS. Aplica cualquier actualización normativa directamente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal y Regla Imperativa de Plazos:**
   - **Alta Laboral Previa (OBLIGATORIO):** Recordar que el alta de un trabajador por cuenta ajena debe solicitarse de forma preceptiva **antes del inicio material de la prestación de servicios** (con hasta 60 días naturales de antelación). El inicio de labores sin alta previa constituye infracción administrativa muy grave (art. 22.2 LISOS).
   - **Baja Laboral:** Debe comunicarse dentro de los **3 días naturales** posteriores al cese de la relación laboral.
   - **Canal Telemático:** Explicar si el trámite se cursará a través del Sistema RED (empresas con autorización) o del portal Import@ss (empleadores de hogar y particulares).
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Presentar la hoja de datos oficial correspondiente (`template-hoja-datos-afiliacion-ta1.md`, `template-hoja-datos-alta-baja-trabajador.md` o `template-hoja-datos-inscripcion-empresa-ccc.md`).
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación de V5 (Origen Plantilla) y Manejo de la Elección
- **Si `V5 = plantilla_sistema`:** Toma el asset oficial seleccionado y avanza a la **Fase 3**.
- **Si `V5 = plantilla_usuario`:** Adopta la minuta del usuario desde `<attached_documents>` o `<user_message>`, valida la observancia de normas laborales imperativas y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en el archivo correspondiente del workspace (ej: `hoja_datos_alta_trabajador.md`, `hoja_datos_afiliacion_ta1.md` o `hoja_datos_inscripcion_ccc.md`).
   - Aplica el principio **Zero-Omission**:
     - Sustituye los datos ya conocidos del triaje.
     - Todos los campos pendientes deben permanecer como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves.
     - PROHIBIDO dejar archivos vacíos o resúmenes coloquiales.
2. **Validación de Disco (`read_file`):**
   - Comprueba la integridad física del documento recién creado en el workspace.
3. **Confirmación en Chat:**
   - Comunica la ruta absoluta del documento en el workspace y enlaza de inmediato la primera sección de la **Fase 4**.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques de datos aplicando el ciclo interactivo:
```
[Pregunta al Usuario] ──> [Vista Previa en texto plano] ──> [¿Confirmamos esta sección?] ──> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Pregunta en Chat:** Solicita los datos específicos del bloque orientando sobre las opciones técnicas (grupos de cotización, convenios o coeficientes de jornada).
2. **Vista Previa (Preview):** Muestra el bloque redactado en texto plano.
3. **Confirmación:** Pregunta literalmente: `¿Confirmamos esta sección?`.
4. **Persistencia en Disco:** Tras el consentimiento, ejecuta `edit_file` con precisión quirúrgica y valida con `read_file`.

### Hoja de Ruta de Secciones — TRABAJADOR POR CUENTA AJENA / EMPLEADA DE HOGAR:

1. **Datos del Empleador o Empresa** *(confirmación agrupada)*:
   - Razón social o nombre y apellidos, CIF/NIF, Código de Cuenta de Cotización (CCC) principal o secundario y domicilio del centro de trabajo.
2. **Datos del Trabajador** *(confirmación agrupada)*:
   - Nombre y apellidos, NIF/NIE, Número de la Seguridad Social (NUSS), domicilio completo, fecha de nacimiento y nacionalidad.
3. **Condiciones de la Contratación Laboral**:
   - Modalidad contractual (indefinido ordinario, fijo discontinuo, temporal por circunstancias de la producción, formativo).
   - Tipo de jornada (completa o parcial con coeficiente horario y horas semanales acordadas).
   - Grupo de cotización oficial (grupos 1 a 11 de la TGSS) y categoría/puesto profesional según convenio colectivo.
4. **Fechas de Efectos y Alta Previa**:
   - Fecha exacta de inicio de la actividad laboral (o fecha de cese y causa reglamentaria en caso de baja: despido, fin de contrato, baja voluntaria o periodo de prueba).
   - Verificación del cumplimiento del plazo de alta previa a la fecha de inicio.
5. **Canal y Domiciliación**:
   - Vía telemática de remisión (Sistema RED con número de autorización o portal Import@ss) e IBAN para cargos de cotizaciones cuando corresponda.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones de la hoja de datos, presenta al usuario el menú interactivo:
```markdown
La hoja de datos y el checklist de tramitación ante la TGSS han sido generados y actualizados en disco.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar datos del empleador, CCC o centro de trabajo.
2. Modificar datos del trabajador, NUSS o grupo de cotización.
3. Modificar la jornada, tipo de contrato o fecha de efectos.
4. Revisar la coherencia global y control de plazos previos a la transmisión.
5. Dar la hoja de datos por finalizada y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
Al cerrar la sesión, emite siempre las siguientes advertencias:
1. **Carácter DRAFT:** La hoja de datos generada es un borrador preparatorio que debe ser revisado y presentado telemáticamente por un graduado social, gestor administrativo o persona autorizada RED antes del inicio de la actividad.
2. **Carácter Imperativo del Alta Previa:** El alta en la Seguridad Social debe tramitarse **siempre antes del inicio real de la prestación de servicios**. Trabajar sin alta previa acarrea multas muy graves de 3.750 € a 12.000 € por trabajador (LISOS), la presunción de contrato indefinido y la pérdida de bonificaciones.
3. **Plazo de la Baja:** La baja del trabajador debe comunicarse de forma improrrogable dentro de los **3 días naturales** posteriores al cese de la relación laboral (6 días naturales en Sistema Especial de Empleadas de Hogar).
4. **Sede Oficial de Tramitación:**
   - Empresas y autorizados: Sistema RED Online / RED Directo en la Sede Electrónica de la Seguridad Social.
   - Empleadores de hogar y ciudadanos: Portal Import@ss de la TGSS mediante Cl@ve o certificado digital.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Infracción por Alta Extemporánea:** Advertir de forma inmediata y destacada si la fecha de inicio solicitada es anterior o coincide con el momento presente sin haber cursado el alta previa.
2. **Cero Invención de Códigos:** Queda prohibido inventar CCC, NUSS, NIFs o grupos de cotización. Todo dato desconocido debe figurar como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** Aplicar cualquier variación en modelos TA directamente en el workspace del usuario; nunca modificar los assets locales del plugin.
4. **Límites de Alcance:** No tramitar altas de autónomos (RETA), expedientes de regulación de empleo (ERE/ERTE), actas de liquidación o sanciones de la Inspección de Trabajo, las cuales deben derivarse a abogados laboralistas o graduados sociales colegiados.
