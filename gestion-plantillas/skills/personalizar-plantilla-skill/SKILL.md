---
name: personalizar-plantilla-skill
description: >
  Permite al usuario crear, parametrizar y registrar sus propias plantillas de documentos (assets)
  asociadas a cualquier skill especializada de GravitonAI a partir de minutas o contratos de ejemplo adjuntos.
  Implementa un flujo de 5 fases estructurado con identificación de skill y asset objetivo, lectura y
  abstracción de datos reales a marcadores {{variable}} en Markdown limpio, guardado de borrador en workspace,
  vista previa y confirmación interactiva, y persistencia en el backend mediante la herramienta set_skill_template().
  NO usar para la redacción final de contratos sustantivos de clientes ni para la tramitación de expedientes legales.
when_to_use: |
  - El usuario desea utilizar su propia minuta o modelo de contrato en una skill específica en lugar de la plantilla por defecto.
  - El usuario adjunta un documento real de ejemplo y solicita convertirlo en plantilla reutilizable para una skill.
  - El usuario desea redefinir o actualizar el asset de plantilla asignado a una skill del sistema.
inputs:
  - skill_destino: nombre de la skill objetivo a la que se asignará la plantilla (V1)
  - asset_destino: nombre exacto del archivo asset con prefijo template- (V2)
  - origen_documento: documento adjunto / texto pegado en el chat (V3)
  - documento_ejemplo: contenido textual del documento o minuta aportada por el usuario
outputs:
  - resumen_asignacion_plantilla: reporte markdown de confirmación de asignación y registro de la plantilla
references:
  - references/reglas-parametrizacion-plantillas.md
assets:
  - assets/template-resumen-asignacion-plantilla.md
---

# Personalizar y Asignar Plantilla a una Skill

> REPORTE DE CONFIGURACIÓN — Plantilla personalizada registrada en el sistema.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para transformar minutas reales en plantillas oficiales de usuario.

### Vectores de Estado (Uso Estrictamente Interno):
Para garantizar un enrutamiento determinista y la correcta ejecución de `set_skill_template`, el asistente resuelve y mantiene internamente en memoria los siguientes vectores de estado:
- **V1 (Skill Destino):** Nombre de la skill objetivo del sistema (ej: `arrendamiento-urbano`, `desahucio`, `convenio-regulador`, `alta-baja-autonomo`, `transferencia-vehiculo`, etc.).
- **V2 (Asset Destino):** Nombre de archivo exacto del asset declarado en la skill de destino (ej: `template-contrato-arrendamiento-vivienda.md`, `template-demanda-desahucio-falta-pago.md`, etc.). *(Debe llevar obligatoriamente el prefijo `template-` y extensión `.md`)*.
- **V3 (Origen Documento):** `documento_adjunto` (disponible en `<attached_documents>`) | `texto_pegado_chat` (disponible en `<user_message>`).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`) y los resúmenes de validación con marcas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL Y SELECCIÓN DE SKILL Y ASSET DESTINO

Tu primer objetivo es identificar con precisión la skill (`V1`) y el asset (`V2`) que el usuario desea personalizar, así como verificar la disponibilidad del documento de ejemplo (`V3`).

### 1.1 Escucha Activa Previa
Antes de formular preguntas o abrir formularios, evalúa el mensaje del usuario y los adjuntos:
- Si el usuario **ya especificó claramente la skill de destino y el tipo de documento**, e incluyó el archivo adjunto (ej: *"Quiero registrar esta minuta adjunta como mi plantilla de vivienda para arrendamiento-urbano"*):
  - Fija `V1` = `arrendamiento-urbano`.
  - Fija `V2` = `template-contrato-arrendamiento-vivienda.md`.
  - Fija `V3` = `documento_adjunto`.
  - Avanza directamente a la **Fase 2**.
- Si falta determinar la skill objetivo, el asset específico o no se ha adjuntado documento, formula la consulta correspondiente.

### 1.2 Formulario o Consulta de Selección
Si la skill o el asset no están definidos, formula una pregunta clara en el chat o invoca `restricted_human_in_the_loop_request` para que el usuario precise:
1. ¿Para qué skill del sistema desea registrar su plantilla personalizada?
2. ¿Qué plantilla o documento específico de esa skill desea sustituir? (ej. contrato de vivienda, contrato de local, demanda por falta de pago, etc.).
3. Si aún no ha adjuntado el documento de ejemplo, solicitarle que lo adjunte o pegue su contenido en el chat.

### 1.3 Validación de Parámetros de Destino
Una vez identificados `V1` y `V2`:
- Asegurar que `V2` mantenga el prefijo estandarizado `template-` y la extensión `.md`.
- Proceder a la **Fase 2**.

---

## FASE 2 — ANÁLISIS DEL DOCUMENTO EJEMPLO Y PARAMETRIZACIÓN (Vía Chat)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para presentar el análisis de la minuta y acordar el inventario de variables.

### 2.1 Lectura e Inspección de la Minuta Aportada
1. **Acceso a Documentos Adjuntos en el Contexto:**
   Cuando el usuario sube o adjunta archivos (PDF, DOCX, TXT, MD, etc.), su contenido ya procesado se proporciona íntegramente en el prompt de contexto bajo la sección:

   ```xml
   # ATTACHED DOCUMENTS
   <attached_documents>
       <attached_document name="nombre_archivo.pdf">
           "Contenido textual completo del documento adjunto..."
       </attached_document>
   </attached_documents>
   ```

   - **Extracción de la Minuta:** Lee e inspecciona directamente el contenido dentro de la etiqueta `<attached_document name="...">` para obtener el texto original de la minuta de ejemplo.
   - **Múltiples Adjuntos:** Si hay varios documentos adjuntos, selecciona el que corresponda al modelo o contrato a parametrizar según el atributo `name` y las indicaciones del usuario.
   - **Texto en Chat:** Si el usuario no adjuntó archivo pero pegó el texto directamente en la conversación, tómalo del bloque `# USER MESSAGE` / `<user_message>`.
2. Si no se detecta ningún documento en `<attached_documents>` ni texto en `<user_message>`, solicita amablemente al usuario que adjunte el archivo o proporcione el texto del documento para poder continuar.

### 2.2 Proceso de Abstracción y Parametrización
Consulta las directivas de `references/reglas-parametrizacion-plantillas.md` y aplica las siguientes transformaciones:
1. **Anonimización y Sustitución de Datos Concretos:**
   - Detectar todos los nombres de partes, números de identificación fiscal (NIF/CIF/DNI/NIE), domicilios, municipios, fechas, importes en euros, porcentajes, cuentas bancarias (IBAN) y referencias notariales/registrales del caso real.
   - Sustituirlos por marcadores en dobles llaves y snake_case: `{{nombre_arrendador}}`, `{{nif_arrendatario}}`, `{{domicilio_inmueble}}`, `{{renta_mensual}}`, `{{fecha_contrato}}`, etc.
2. **Garantía de Assets Limpios:**
   - Eliminar cualquier comentario HTML condicional (ej. `<!-- Si ... -->`).
   - Conservar íntegramente la redacción de las cláusulas, títulos (`#`, `##`), estructura numerada y tablas de datos en Markdown limpio.
3. **Mapeo de Variables:**
   - Elaborar una lista ordenada con todas las variables creadas y su significado.

### 2.3 Mensaje de Plan de Acción al Usuario
Envía un mensaje cordial en el chat que contenga:
1. Confirmación de la skill (`V1`) y asset (`V2`) a los que se vinculará la plantilla.
2. Resumen de las cláusulas y estructura identificadas en el documento adjunto.
3. Tabla o lista de las principales variables parametrizadas (ej: `{{nombre_arrendador}}`, `{{renta_mensual}}`, etc.).
4. Anuncio de que se va a generar el archivo borrador en el espacio de trabajo para su revisión.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura de la Plantilla en Workspace (`create_file`):**
   - Vuelca íntegramente el contenido de la plantilla parametrizada generada en el workspace bajo el nombre `plantilla_personalizada_{V1}.md` (ej: `plantilla_personalizada_arrendamiento_urbano.md`).
   - Aplica el principio **Zero-Omission**: el archivo debe contener la plantilla completa de principio a fin, sin resúmenes ni marcadores de omisión.
2. **Validación de Disco (`read_file`):**
   - Ejecuta `read_file` sobre el archivo recién creado para verificar que el contenido en disco es íntegro y correcto.
3. **Confirmación en Chat:**
   - Emite un mensaje indicando la ruta del archivo generado en el workspace.
   - En la misma respuesta, sin detener la marcha, pasa de inmediato a la **Fase 4** para mostrar la vista previa y pedir confirmación de asignación.

---

## FASE 4 — REVISIÓN INCREMENTAL Y ASIGNACIÓN CON `set_skill_template`

Recorre la validación de la plantilla junto al usuario y procede a su registro oficial:

```
[Vista Previa en texto plano] ──> [¿Confirmamos esta plantilla?] ──> [Tool: set_skill_template()]
```

### Protocolo de Asignación:
1. **Vista Previa (Preview):** Muestra en el chat el texto íntegro o los bloques principales de la plantilla parametrizada en texto plano (sin bloques de código con backticks).
2. **Petición de Confirmación Obligatoria:** Pregunta literalmente:
   > *"¿Confirmamos la asignación de esta plantilla personalizada como asset `{{V2}}` para la skill `{{V1}}`?"*
3. **Ejecución de la Tool (`set_skill_template`):**
   - Tras el "sí" o confirmación explícita del usuario, invoca la herramienta:
   ```json
   {
     "skill_name": "<valor_de_V1>",
     "asset_name": "<valor_de_V2>",
     "template_content": "<contenido_completo_en_markdown_de_la_plantilla_parametrizada>"
   }
   ```
4. **Generación del Reporte de Asignación (`create_file`):**
   - Genera el reporte final en el workspace (`reporte_asignacion_plantilla.md`) usando la plantilla `assets/template-resumen-asignacion-plantilla.md`, rellenando los datos de la skill, asset, fecha y variables parametrizadas.
   - Ejecuta `read_file` para validar la escritura.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez ejecutada la herramienta `set_skill_template` y generado el reporte, muestra en el chat el siguiente menú interactivo de opciones finales:

```markdown
La plantilla personalizada ha sido asignada y registrada exitosamente para la skill "{{skill_name}}".

Seleccione una opción si desea realizar alguna gestión adicional:
1. Ajustar o modificar nombres de variables en la plantilla.
2. Añadir una cláusula adicional a la plantilla registrada.
3. Personalizar otra plantilla (asset) para esta u otra skill.
4. Ver el inventario completo de variables que requerirá esta plantilla.
5. Dar la configuración por finalizada y cerrar la sesión.
```

### Mensaje de Confirmación al Cerrar:
Cuando el usuario seleccione finalizar la sesión, emite la confirmación:
1. **Persistencia Activa:** Confirmar que, en las siguientes conversaciones en las que el usuario active la skill `{{skill_name}}`, el sistema utilizará de manera preferente su plantilla personalizada recién registrada.
2. **Reversibilidad:** Recordar que si en cualquier momento desea actualizar la minuta o restablecer otra plantilla, podrá volver a invocar esta skill de personalización.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Cero Datos Sensibles (PII):** Queda estrictamente prohibido persistir plantillas en `set_skill_template` que contengan nombres reales, documentos de identidad, números de teléfono o importes específicos pertenecientes a personas o casos particulares. Toda la información contingente debe estar parametrizada con `{{variable}}`.
2. **Formato Obligatorio de Asset:** El nombre `asset_name` debe coincidir con la convención `template-*.md`.
3. **No Invención de Contenido:** La plantilla debe reflejar fielmente la estructura y cláusulas del documento original aportado por el usuario, sin omitir estipulaciones pactadas ni agregar cláusulas no solicitadas salvo la parametrización de variables.
4. **Invocación Condicionada:** `set_skill_template` se ejecuta ÚNICAMENTE tras la confirmación afirmativa del usuario en la Fase 4.
