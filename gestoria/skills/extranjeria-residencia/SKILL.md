---
name: extranjeria-residencia
description: >
  Prepara el tramite administrativo de solicitud del Numero de Identidad de Extranjero (NIE) o de
  autorizacion de residencia (residencia temporal no lucrativa, residencia por arraigo, reagrupacion
  familiar u otra) ante la Oficina de Extranjeria, conforme a la Ley Organica 4/2000 (LOEX) y al
  Reglamento de Extranjeria (RD 1155/2024, en vigor desde el 20/05/2025) verificados en el BOE.
  Opera bajo el flujo de 5 fases canonicas con clasificacion HITL, consulta de assets, creacion
  zero-vacios en workspace y edicion incremental seccion a seccion. Genera la hoja de datos para el
  formulario EX correspondiente, el escrito motivado de solicitud, el checklist de documentos y la
  tasa oficial (modelo 790). NO usar para solicitar visados consulares desde el extranjero, ni para
  nacionalidad espanola, asilo o proteccion internacional, ni para recursos contenciosos contra denegaciones.
when_to_use: |
  - El usuario (extranjero o su representante) quiere obtener el NIE por interes economico, profesional o social.
  - El usuario quiere solicitar una autorizacion de residencia: no lucrativa, por arraigo o por reagrupacion familiar.
  - El usuario pide preparar el formulario EX, el checklist de documentos y la tasa de un tramite de extranjeria.
inputs:
  - tipo_tramite: nie / residencia_no_lucrativa / residencia_arraigo / reagrupacion_familiar (V1)
  - tipo_arraigo_subtipo: social / sociolaboral / socioformativo / familiar / segunda_oportunidad / general (V2)
  - naturaleza_solicitante: persona_fisica (V3)
  - via_presentacion_lugar: en_espana_oficina_extranjeria / desde_extranjero_consulado (V4)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - datos_extranjero: nombre y apellidos, nacionalidad, numero de pasaporte, fecha de nacimiento
  - nie_previo: si el extranjero ya tiene NIE asignado (si / no)
  - motivo: motivo del NIE o de la residencia
  - domicilio_espana: domicilio en Espana a efectos de notificaciones, si lo hay
  - datos_apoyo: medios economicos, seguro medico, tiempo de permanencia, familiar reagrupante, contrato u oferta de trabajo
  - representante: si actua un representante (gestor, abogado, familiar) y sus datos
outputs:
  - hoja_datos_ex: hoja de datos para el formulario EX, checklist de documentos, organismo y tasa, en markdown, DRAFT
  - escrito_solicitud: escrito formal de solicitud y alegaciones de residencia en markdown, DRAFT
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

# Preparar Solicitud de NIE o Autorización de Residencia (Extranjería)

> DRAFT — para revisión por un gestor administrativo o abogado especialista en extranjería antes de su presentación oficial. No constituye dictamen vinculante ni garantiza la concesión de la autorización, cuya resolución es potestad reglada y discrecional de la Administración.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para preparar la solicitud de NIE o autorización de residencia conforme a la LOEX y al Reglamento de Extranjería vigente (RD 1155/2024).

### Vectores de Estado (Uso Estrictamente Interno):
Para garantizar un enrutamiento determinista y el cumplimiento riguroso de la normativa migratoria, el asistente resuelve y mantiene internamente en memoria los siguientes vectores de estado:
- **V1 (Tipo de Trámite Principal):** `nie` (asignación) | `residencia_no_lucrativa` | `residencia_arraigo` | `reagrupacion_familiar`.
- **V2 (Subtipo / Modalidad Arraigo):** `social` | `sociolaboral` | `socioformativo` | `familiar` | `segunda_oportunidad` | `general_no_aplica`.
- **V3 (Naturaleza del Solicitante):** `persona_fisica`.
- **V4 (Lugar / Vía de Tramitación):** `en_espana_oficina_extranjeria` (vía Mercurio / sede electrónica o cita presencial) | `desde_extranjero_consulado` *(advertencia de visado consular previo)*.
- **V5 (Origen Plantilla / Asset):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`, `V4`, `V5`) y los resúmenes de validación con marcas técnicas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

Tu primer objetivo es identificar la figura migratoria exacta y el formulario oficial correspondiente.

### 1.1 Escucha Activa Previa
Antes de invocar formularios, evalúa el mensaje inicial del usuario:
- Si el usuario ya especificó con precisión el tipo de trámite (ej. solicitar NIE de no residente para comprar un inmueble, solicitar residencia temporal no lucrativa o tramitar un arraigo social con contrato), registra los vectores y avanza a la **Fase 2**.
- Si falta delimitar la figura migratoria (`V1`) o el subtipo de arraigo (`V2`), invoca de inmediato la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las opciones de triaje:

```json
{
  "form_data": [
    {
      "id": "tipo_tramite",
      "rationale": "Resolver V1 para determinar la base jurídica de la LOEX y el modelo de formulario EX.",
      "question": "¿Qué trámite de extranjería necesita preparar?",
      "options": [
        {"id": "nie", "label": "Asignación de NIE (interés económico, profesional o social, sin residencia)"},
        {"id": "residencia_arraigo", "label": "Autorización de residencia por circunstancias excepcionales (Arraigo)"},
        {"id": "residencia_no_lucrativa", "label": "Autorización de residencia temporal no lucrativa (fondos propios)"},
        {"id": "reagrupacion_familiar", "label": "Autorización de residencia por reagrupación familiar"}
      ]
    },
    {
      "id": "lugar_presentacion",
      "rationale": "Resolver V4 para validar la competencia territorial y la necesidad de visado consular.",
      "question": "¿Dónde se encuentra actualmente el solicitante?",
      "options": [
        {"id": "en_espana_oficina_extranjeria", "label": "En España (Oficina de Extranjería / Plataforma Mercurio)"},
        {"id": "desde_extranjero_consulado", "label": "En el extranjero (Consulado o Embajada de España)"}
      ]
    }
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V4 = desde_extranjero_consulado` y `V1 = residencia_no_lucrativa`:**
  - Advertir expresamente de que la solicitud inicial de residencia y el correspondiente visado deben tramitarse ante la demarcación consular española en el país de origen. La skill preparará la hoja de datos y el escrito de soporte, pero no sustituye la tramitación consular.
- **En todos los casos dentro de alcance:**
  - Plantillas del sistema propuestas: `assets/template-hoja-datos-solicitud-ex.md` y `assets/template-escrito-solicitud-residencia.md`. Proceder a la **Fase 2**.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `loex-y-reglamento.md` (con especial atención al Reglamento RD 1155/2024 en vigor desde el 20/05/2025), `formularios-ex-y-tasas.md` y `documentacion-por-tramite.md`.
2. Opcionalmente verifica mediante `web_search` las cuantías exactas de las tasas vigentes (Tasa 790 código 052 o código 012). Aplica cualquier actualización normativa directamente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Normativo y Requisitos Esenciales:**
   - Citar el RD 1155/2024 y la LO 4/2000.
   - Detallar los requisitos sustantivos según el trámite: carecer de antecedentes penales en España y países de residencia anterior (5 años), seguro médico privado sin copagos (en no lucrativa), acreditación de fondos (400% del IPREM anual en no lucrativa) o permanencia mínima y vínculos en arraigo.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Presentar la hoja de datos para el formulario EX (identificando el modelo: EX-15 para NIE, EX-10 para arraigo, EX-01 para no lucrativa, EX-02 para reagrupación) y el escrito formal de solicitud.
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación de V5 (Origen Plantilla) y Manejo de la Elección
- **Si `V5 = plantilla_sistema`:** Utiliza los assets oficiales seleccionados y avanza a la **Fase 3**.
- **Si `V5 = plantilla_usuario`:** Adopta la minuta del usuario desde `<attached_documents>` o `<user_message>`, valida la observancia de la LOEX y el RD 1155/2024 y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura de los Documentos (`create_file`):**
   - Vuelca íntegramente las plantillas acordadas en el workspace del usuario:
     - `hoja_datos_solicitud_extranjeria.md` (adaptada al modelo EX correspondiente).
     - `escrito_solicitud_residencia.md` (escrito formal motivado dirigido a la Oficina de Extranjería).
   - Aplica el principio **Zero-Omission**:
     - Sustituye los datos ya conocidos del triaje.
     - Todos los campos pendientes deben permanecer como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves.
     - PROHIBIDO dejar archivos vacíos o con anotaciones provisionales fuera del estándar.
2. **Validación de Disco (`read_file`):**
   - Verifica la correcta creación física de los archivos en disco.
3. **Confirmación en Chat:**
   - Comunica las rutas de los archivos generados en disco y formula de inmediato la primera pregunta de la **Fase 4**.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques de datos aplicando el ciclo interactivo:
```
[Pregunta al Usuario] ──> [Vista Previa en texto plano] ──> [¿Confirmamos esta sección?] ──> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Pregunta en Chat:** Solicita los datos específicos del bloque orientando sobre la validez de los documentos probatorios.
2. **Vista Previa (Preview):** Muestra el bloque redactado en texto plano.
3. **Confirmación:** Pregunta literalmente: `¿Confirmamos esta sección?`.
4. **Persistencia en Disco:** Aplica `edit_file` con precisión milimétrica y verifica inmediatamente con `read_file`.

### Hoja de Ruta de Secciones:

1. **Datos de Filiación del Extranjero** *(confirmación agrupada)*:
   - Nombre y apellidos, nacionalidad, número de pasaporte completo y fecha de caducidad, fecha y lugar de nacimiento, estado civil y NIE previo (si ya disponía de uno).
2. **Domicilio a Efectos de Notificaciones en España**:
   - Domicilio completo en territorio español (imprescindible para determinar la Oficina de Extranjería provincial competente) y consentimiento para notificaciones telemáticas.
   - *Condicional representante voluntario:* Si interviene abogado o gestor, consignar datos del apoderado y acreditación de representación.
3. **Motivación y Fundamentación del Trámite**:
   - Para NIE: Motivo económico (adquisición de inmueble, constitución de sociedad, apertura de cuenta bancaria), profesional o social.
   - Para Residencia No Lucrativa: Acreditación de fondos económicos suficientes (certificados bancarios, ingresos pasivos) y póliza de seguro de salud con entidad aseguradora autorizada en España.
   - Para Arraigo: Vía de arraigo elegida, tiempo acreditado de estancia continuada en España (empadronamiento histórico) y contrato u oferta de trabajo / informe de inserción social / vínculo familiar.
4. **Checklist Documental y Tasas Oficiales**:
   - Relación detallada de documentos extranjeros preceptivos (certificados de antecedentes penales del país de origen apostillados/legalizados y con traducción jurada oficial, certificados de matrimonio/nacimiento, etc.).
   - Determinación del importe y código de la Tasa oficial (Modelo 790 código 052 a abonar previamente a la resolución).
5. **Petición Formal al Órgano Competente (Suplico)**:
   - Identificación de la Delegación o Subdelegación del Gobierno / Oficina de Extranjería provincial correspondiente y redacción formal de la solicitud.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones de los documentos, presenta al usuario el menú interactivo:
```markdown
La hoja de datos del formulario oficial, el escrito de solicitud y el checklist documental han sido generados y actualizados en disco.

Seleccione una opción si desea realizar ajustes adicionales:
1. Modificar datos personales o del pasaporte del solicitante.
2. Ajustar la motivación o la documentación de apoyo aportada.
3. Modificar el domicilio de notificaciones o designar representante.
4. Revisar la coherencia global y los requisitos del RD 1155/2024.
5. Dar los documentos por finalizados y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
Al concluir, emite siempre las siguientes advertencias:
1. **Carácter DRAFT:** Los documentos son borradores técnicos preparatorios que deben ser revisados por un abogado de extranjería o gestor administrativo colegiado antes de su presentación oficial.
2. **Potestad Discrecional de la Administración:** La concesión de autorizaciones de residencia es una potestad reglada pero sometida a valoración de la Oficina de Extranjería. El cumplimiento formal no garantiza automáticamente la resolución favorable.
3. **Caducidad de Documentos Extranjeros:** Los certificados de antecedentes penales y actas del estado civil emitidos en el extranjero caducan habitualmente a los 3 o 6 meses de su expedición; deben presentarse debidamente apostillados (Convenio de La Haya) o legalizados por vía diplomática, y traducidos al castellano por traductor jurado oficial.
4. **Vía de Presentación:**
   - Presentación telemática oficial: A través de la plataforma MERCURIO de la Administración Pública (requiere certificado digital del interesado o de profesional habilitado).
   - Presentación presencial: Requiere cita previa en la Oficina de Extranjería correspondiente.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Vigencia Normativa RD 1155/2024:** Queda estrictamente prohibido fundamentar solicitudes en el derogado RD 557/2011. Toda solicitud debe ceñirse a las figuras del nuevo reglamento.
2. **Cero Invención de Datos:** No inventar números de NIE, pasaportes ni referencias de expedientes. Todo campo no confirmado debe permanecer como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** Aplicar cualquier cambio en tasas o criterios administrativos directamente en el workspace del usuario; nunca modificar los archivos internos del plugin.
4. **Límites de Alcance:** No gestionar solicitudes de asilo político, protección internacional, recursos contencioso-administrativos ante Tribunales Superiores de Justicia ni trámites de adquisición de nacionalidad española por residencia, que deben derivarse a letrados colegiados.
