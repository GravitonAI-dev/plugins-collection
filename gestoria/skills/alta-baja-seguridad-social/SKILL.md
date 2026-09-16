---
name: alta-baja-seguridad-social
description: >
  Prepara altas y bajas en la Seguridad Social (Regimen General) que corresponden al empleador y al
  trabajador por cuenta ajena en Espana: (1) afiliacion inicial y numero de la Seguridad Social (NUSS)
  con el modelo TA.1; (2) inscripcion de empresa y apertura del Codigo de Cuenta de Cotizacion (CCC),
  y sus variaciones o baja, con el modelo TA.6; (3) alta y baja de trabajadores por cuenta ajena en el
  Regimen General por el empleador via Sistema RED o Import@ss; (4) alta y baja de empleadas de hogar
  (Sistema Especial del Regimen General), conforme al **texto refundido de la Ley General de la Seguridad Social (LGSS, RD-legislativo 8/2015)**, que regula la afiliacion, las altas y las bajas de trabajadores y empresas,
  y al **Reglamento general de inscripcion, afiliacion, altas y bajas (RD 84/1996)**, en su version consolidada
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
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
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
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas (por ejemplo, anotar un vector como resuelto) son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

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

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `tipo_operacion`
- `V2` — `tipo_sujeto_tramite`
- `V3` — naturaleza del empleador: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo
- `V4` — naturaleza del trabajador: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V2 = afiliacion_nuss_ta1`:**
  - Hoja de datos propuesta: `assets/template-hoja-datos-afiliacion-ta1.md`. Proceder a la **Fase 2**.
- **Si `V2 = inscripcion_empresa_ccc_ta6`:**
  - Hoja de datos propuesta: `assets/template-hoja-datos-inscripcion-empresa-ccc.md`. Proceder a la **Fase 2**.
- **Si `V2 = cuenta_ajena_regimen_general` o `V2 = empleada_hogar`:**
  - Hoja de datos propuesta: `assets/template-hoja-datos-alta-baja-trabajador.md`. Proceder a la **Fase 2**.
- `V1` no elige hoja por si solo: determina si se preparan los tramites de alta y afiliacion o los de cese y baja.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

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
   - Nombra por su ruta la hoja **que ha resuelto el enrutamiento de la Fase 1.3**; si el enrutamiento asigno varias, nombralas todas y en el orden en que se van a rellenar. **No propongas una hoja distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
Aplica el protocolo determinista de `REG-AST-01` (`CLAUDE.md`): si el usuario acepta la plantilla predeterminada propuesta (`plantilla_sistema`), carga el asset enrutado y avanza a la **Fase 3**; si aporta su propia minuta (`plantilla_usuario`), realiza el control de legalidad advirtiendo de cláusulas nulas o contrarias a normas imperativas, adopta la minuta revisada como base y avanza a la **Fase 3**.
---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

Aplica rigurosamente la directiva `REG-DOC-01` y la sección 6.1 de `CLAUDE.md`:
1. **Escritura del Documento (`create_file`):** Vuelca íntegramente la plantilla acordada en un archivo en el workspace con nombre en `snake_case.md`, aplicando el principio Zero-Omission y el volcado inmediato total de partes (`REG-CLI-04`) en título H1, comparecencia y firmas.
2. **Validación de Integridad:** Comprobación prioritaria mediante `# WORKSPACE ACTIVE DOCUMENTS`.
3. **Confirmación en Chat y Encadenamiento Inmediato:** Informa en el chat de la ruta absoluta del documento creado y los datos de partes incorporados, e introduce en esa misma respuesta la primera sección de la Fase 4 sin detener el flujo.
---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial las secciones del documento respetando rigurosamente las directivas operativas globales de `CLAUDE.md`:
- **Partes e Intervinientes (REG-CLI-01 a 04):** Búsqueda prioritaria con `search_clients`, desambiguación con opción obligatoria `ninguna`, consentimiento de guardado con `save_client` (REG-CLI-03) y volcado directo e inmediato al editor (`edit_file` / `create_file`) sin confirmación en chat (REG-CLI-04).
- **Datos Estructurados Objetivos:** Solicitud en bloque mediante `slot_filling_request`.
- **Equivalencia Chat / Formulario (REG-DAT-01):** Ingestión directa de información aportada por chat sin re-emitir formularios innecesarios; reenvío oportuno si el usuario canceló sin responder.
- **Cláusulas Sustantivas / Negociables:** Negociación en chat -> Vista previa en texto plano -> Pregunta literal de confirmación (`¿Confirmamos esta cláusula?` / `¿Confirmamos esta sección?`) -> Persistencia con `edit_file`.

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

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Infracción por Alta Extemporánea:** Advertir de forma inmediata y destacada si la fecha de inicio solicitada es anterior o coincide con el momento presente sin haber cursado el alta previa.
2. **Cero Invención de Códigos:** Queda prohibido inventar CCC, NUSS, NIFs o grupos de cotización. Todo dato desconocido debe figurar como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** Aplicar cualquier variación en modelos TA directamente en el workspace del usuario; nunca modificar los assets locales del plugin.
4. **Límites de Alcance:** No tramitar altas de autónomos (RETA), expedientes de regulación de empleo (ERE/ERTE), actas de liquidación o sanciones de la Inspección de Trabajo, las cuales deben derivarse a abogados laboralistas o graduados sociales colegiados.
