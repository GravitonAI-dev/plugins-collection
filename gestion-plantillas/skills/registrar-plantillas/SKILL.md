---
name: registrar-plantillas
description: >
  Permite al usuario crear, parametrizar y registrar sus propias plantillas de documentos (assets)
  asociadas a cualquier skill especializada de GravitonAI a partir de minutas o contratos de ejemplo aportados.
  Implementa un flujo consultivo de 5 fases con selección jerárquica de skill y asset objetivo, lectura y
  abstracción de datos reales a marcadores {{variable}} en Markdown limpio, previsualización en chat,
  y persistencia directa en el backend mediante la herramienta set_skill_template().
  NO usar para la redacción final de contratos de clientes ni para crear documentos en el workspace.
when_to_use: |
  - El usuario desea registrar o actualizar su propia minuta o modelo de contrato como plantilla oficial para una skill.
  - El usuario adjunta un documento real de ejemplo y solicita convertirlo en plantilla reutilizable para una skill.
  - El usuario desea redefinir o personalizar el asset de plantilla asignado a una skill del sistema.
inputs:
  - skill_destino: nombre de la skill objetivo a la que se asignará la plantilla (V1)
  - asset_destino: nombre exacto del archivo asset con prefijo template- (V2)
  - origen_documento: documento adjunto / texto pegado en el chat (V3)
  - documento_ejemplo: contenido textual del documento o minuta aportada por el usuario
outputs:
  - confirmacion_registro: mensaje de confirmación de registro de la plantilla en el backend
references:
  - references/reglas-parametrizacion-plantillas.md
assets:
  - assets/resumen-asignacion-plantilla.md
---

# Registrar Plantilla Personalizada en el Sistema

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para transformar minutas reales en plantillas oficiales registradas en el backend.

### REGLA FUNDAMENTAL DE ALCANCE:
> **CERO ARCHIVOS EN WORKSPACE:** Esta skill **NO** crea archivos en el workspace de la conversación (`create_file` está expresamente deshabilitado). Todo el intercambio y la previsualización se realizan a través del chat, y la persistencia se realiza **exclusivamente** mediante la herramienta `set_skill_template()`.

### Vectores de Estado (Uso Estrictamente Interno):
Para garantizar un enrutamiento determinista y la correcta ejecución de `set_skill_template`, el asistente resuelve y mantiene internamente en memoria los siguientes vectores de estado:
- **V1 (Skill Destino):** Nombre de la skill objetivo del sistema (ej: `arrendamiento-urbano`, `desahucio`, `divorcio`, `alta-baja-autonomo`, `transferencia-vehiculo`, etc.).
- **V2 (Asset Destino):** Nombre de archivo exacto del asset declarado en la skill de destino (ej: `template-contrato-arrendamiento-vivienda.md`, `template-demanda-desahucio-falta-pago.md`, etc.). *(Debe llevar obligatoriamente el prefijo `template-` y extensión `.md`)*.
- **V3 (Origen Documento):** `documento_adjunto` (disponible en `<attached_documents>`) | `texto_pegado_chat` (disponible en `<user_message>`).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`) y los resúmenes de validación con marcas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL Y SELECCIÓN JERÁRQUICA

Tu primer objetivo es identificar con precisión la skill (`V1`) y el asset (`V2`) que el usuario desea personalizar, así como verificar la disponibilidad del documento de ejemplo (`V3`).

### 1.1 Escucha Activa Previa
Antes de formular preguntas o abrir formularios, evalúa el mensaje del usuario y los adjuntos:
- Si el usuario **ya especificó claramente la skill de destino y el tipo de documento**, e incluyó el archivo adjunto (ej: *"Quiero registrar esta minuta adjunta como mi plantilla de vivienda para arrendamiento-urbano"*):
  - Fija `V1` = `arrendamiento-urbano`.
  - Fija `V2` = `template-contrato-arrendamiento-vivienda.md`.
  - Fija `V3` = `documento_adjunto`.
  - Avanza directamente a la **Fase 2**.
- Si falta determinar la skill objetivo, el asset específico o no se ha adjuntado documento, guía al usuario.

### 1.2 Selección Jerárquica (Plugin -> Skill -> Asset)
Si la skill o el asset no están completamente definidos, guía al usuario a través del **orden jerárquico de selección**:
1. **Paso 1 — Selección de Plugin (Área temática):** Identificar el plugin o área de trabajo (ej. `derecho-civil`, `laboral`, `fiscal`, etc.).
2. **Paso 2 — Selección de Skill (`V1`):** Identificar la skill especializada dentro del plugin seleccionado (ej. `arrendamiento-urbano`, `desahucio`, `divorcio`, etc.).
3. **Paso 3 — Selección de Asset (`V2`):** Identificar el asset o plantilla específica declarada en esa skill a ser reemplazada (ej. `template-contrato-arrendamiento-vivienda.md`, `template-contrato-arrendamiento-local.md`, etc.).

**Disponibilidad del Catálogo Oficial:**
- Dispones del catálogo jerárquico oficial en el bloque contextual `<document id="catalog:plugins-skills-assets">` del prompt.
- Si requieres consultar o filtrar dinámicamente, invoca la herramienta `list_skills_and_assets(plugin_name=..., skill_name=...)`.
- Si invocas `restricted_human_in_the_loop_request`, utiliza los identificadores y etiquetas extraídos del catálogo oficial.

### 1.3 Validación de Parámetros de Destino
Una vez identificados `V1` y `V2`:
- Asegurar que `V2` mantenga el prefijo estandarizado `template-` y la extensión `.md`.
- Proceder a la **Fase 2**.

---

## FASE 2 — ANÁLISIS DEL DOCUMENTO EJEMPLO Y PARAMETRIZACIÓN

En esta fase procesas la minuta aportada y generas la plantilla abstracta parametrizada en memoria.

### 2.1 Lectura e Inspección de la Minuta Aportada
1. **Acceso a Documentos Adjuntos:**
   Cuando el usuario sube o adjunta archivos (PDF, DOCX, TXT, MD, etc.), su contenido textual se proporciona íntegramente en el prompt de contexto bajo la sección:
   ```xml
   # ATTACHED DOCUMENTS
   <attached_documents>
       <attached_document name="nombre_archivo.pdf">
           "Contenido textual completo del documento adjunto..."
       </attached_document>
   </attached_documents>
   ```
   Lee e inspecciona directamente el contenido dentro de `<attached_document name="...">`.
2. **Texto en Chat:** Si el usuario pegó el texto directamente en la conversación, tómalo del bloque `<user_message>`.
3. Si no se detecta ningún documento en `<attached_documents>` ni texto en `<user_message>`, solicita amablemente al usuario que adjunte el archivo o proporcione el texto del documento para poder continuar.

### 2.2 Proceso de Abstracción y Parametrización
Consulta las directivas de `references/reglas-parametrizacion-plantillas.md` y aplica:
1. **Anonimización y Sustitución de Datos Particulares:**
   - Detectar todos los nombres de partes, números de identificación fiscal (NIF/CIF/DNI/NIE), domicilios, municipios, fechas, importes en euros, porcentajes, cuentas bancarias (IBAN) y referencias notariales/registrales del caso real.
   - Sustituirlos por marcadores en dobles llaves y snake_case: `{{nombre_arrendador}}`, `{{nif_arrendatario}}`, `{{domicilio_inmueble}}`, `{{renta_mensual}}`, `{{fecha_contrato}}`, etc.
2. **Garantía de Assets Limpios:**
   - Eliminar cualquier comentario HTML condicional (ej. `<!-- Si ... -->`).
   - Conservar íntegramente la redacción de las cláusulas, títulos (`#`, `##`), estructura numerada y tablas en Markdown limpio.
3. **Mapeo de Variables:**
   - Elaborar una lista ordenada con todas las variables creadas y su significado.

---

## FASE 3 — PROPUESTA Y PREVISUALIZACIÓN EN CHAT

Presenta al usuario en el chat (en texto conversacional limpio):
1. **Confirmación de Destino:** Indicar claramente la skill (`V1`) y el asset (`V2`) a los que se asignará la plantilla.
2. **Inventario de Variables:** Mostrar una tabla o lista clara con las variables `{{...}}` identificadas y parametrizadas.
3. **Vista Previa de la Plantilla:** Mostrar el contenido íntegro o los bloques principales de la plantilla parametrizada propuesta.
4. **Pregunta de Confirmación:** Preguntar al usuario si está de acuerdo con las variables y la estructura para proceder al guardado oficial en el sistema.

---

## FASE 4 — ASIGNACIÓN Y GUARDADO CON `set_skill_template`

Cuando el usuario confirme (o si ya proporcionó confirmación explícita):
1. **Invocación Inmediata de la Herramienta:**
   Invoca la herramienta especializada `set_skill_template`:
   ```json
   {
     "skill_name": "<valor_de_V1>",
     "asset_name": "<valor_de_V2>",
     "template_content": "<contenido_completo_en_markdown_de_la_plantilla_parametrizada>"
   }
   ```
2. **Validación de Respuesta:**
   - Si la herramienta devuelve `{"success": true, ...}`, la plantilla ha quedado guardada en la base de datos del sistema.
   - Si la herramienta devuelve un error, analiza el mensaje de error y corrige los parámetros.

---

## FASE 5 — CONFIRMACIÓN DE PERSISTENCIA Y CIERRE

Una vez ejecutada exitosamente la herramienta `set_skill_template`, informa al usuario:
1. **Confirmación Exitosa:** Notificar que la plantilla personalizada ha sido registrada y guardada en el backend para la skill indicada.
2. **Efecto en Futuras Conversaciones:** Explicar que, en todas las siguientes conversaciones en las que el usuario utilice esa skill, el sistema cargará automáticamente su plantilla personalizada en lugar de la plantilla por defecto.
3. **Opciones Finales:** Ofrecer la posibilidad de registrar otra plantilla o dar por concluida la configuración.
