---
name: registrar-plantillas
description: >
  Permite al usuario registrar, parametrizar, actualizar y crear sus propias plantillas de documentos (assets),
  ya sea a partir de texto preexistente o mediante creación asistida desde cero.
  Soporta dos alcances: plantillas asignadas a una skill especializada del sistema o plantillas globales de usuario
  (sin skill). Admite como vías de especificación: texto en el chat, abrir archivo en el editor (archivos del
  workspace) o creación asistida desde cero (excluyendo adjuntar archivos).
  Implementa una verificación estricta de compatibilidad previa con la skill antes de guardar (bloqueando el guardado
  si es incompatible). Enruta la persistencia en el backend mediante set_skill_template(), update_user_template() o
  save_user_template().
  NO usar para la tramitación sustantiva de expedientes ni para crear documentos de clientes en el workspace.
when_to_use: |
  - El usuario desea registrar o actualizar su propia minuta o modelo de contrato como plantilla oficial para una skill del sistema.
  - El usuario desea registrar una plantilla general de usuario (global, sin skill) para reutilización en la plataforma.
  - El usuario desea crear una plantilla desde cero de manera asistida y guiada.
  - El usuario desea convertir en plantilla un texto pegado en el chat o un archivo abierto en el editor (workspace).
  - El usuario desea actualizar una plantilla de usuario ya existente a partir de un archivo del editor (workspace).
inputs:
  - alcance_plantilla: plantilla para una skill / global (sin skill) (V1)
  - origen_contenido: texto en el chat / abrir archivo en el editor (workspace) / creación asistida (desde cero) (V2)
  - skill_destino: nombre de la skill objetivo del catálogo (si alcance es skill)
  - asset_destino: nombre exacto del archivo asset con prefijo template- y extensión .md
  - nombre_plantilla: nombre o título de la plantilla (si alcance es global)
  - descripcion_plantilla: descripción obligatoria del propósito y uso de la plantilla (si es global nueva)
  - documento_fuente: texto en el chat, ruta del archivo en el editor/workspace o especificaciones de diseño
outputs:
  - confirmacion_registro: reporte estructurado de confirmación de registro/actualización en el backend
references:
  - references/reglas-parametrizacion-plantillas.md
assets:
  - assets/resumen-asignacion-plantilla.md
---

# Registrar y Gestionar Plantillas Personalizadas en el Sistema

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado para transformar textos preexistentes o diseñar colaborativamente desde cero plantillas oficiales persistidas en el backend de la plataforma.

### DIRECTIVA DE GESTIÓN EN WORKSPACE Y PERSISTENCIA EN EL BACKEND:
> - **Creación y edición interactiva en el workspace (`create_file` y `edit_file`):** Durante la interacción —especialmente en el **modo de creación asistida desde cero** o al refinar documentos en el editor—, el asistente utiliza `create_file` para generar el borrador de la plantilla en el workspace y `edit_file` para incorporar cláusulas o ajustes de manera incremental. Esto permite al usuario visualizar los cambios en tiempo real en el editor.
> - **Persistencia oficial en el backend:** El archivo del workspace opera como entorno de trabajo interactivo; sin embargo, para que la plantilla quede oficialmente registrada y disponible de manera recurrente en el sistema, DEBE persistirse en el backend mediante las herramientas especializadas:
>   - `set_skill_template`: Si la plantilla pertenece a una skill.
>   - `update_user_template`: Si la plantilla no pertenece a ninguna skill y ya existe (documento en el workspace cuyo nombre es el `asset_name`).
>   - `save_user_template`: Si la plantilla no pertenece a ninguna skill y aún no existe (creación asistida desde cero o nuevo registro).

### VÍAS ADMITIDAS PARA ESPECIFICAR PLANTILLAS:
> Las únicas vías para especificar plantillas son:
> 1. **Texto en el chat:** Pegar el texto directamente en la conversación.
> 2. **Abrir archivo en el editor (archivos del workspace):** Indicar un archivo existente en el editor/workspace para su lectura vía `read_file`.
> 3. **Creación asistida (desde cero):** Redacción guiada e interactiva desde el chat.
> *(Queda expresamente excluida la opción de adjuntar archivos).*

### Vectores de Estado (Uso Estrictamente Interno):
Para garantizar un enrutamiento determinista y la correcta ejecución de las herramientas, el asistente resuelve y mantiene internamente en memoria los siguientes vectores de estado:
- **V1 (Alcance de la Plantilla):** `skill` (asociada a una skill del sistema) | `global` (general de usuario, sin skill).
- **V2 (Vía de Especificación):** `texto_chat` (texto en el chat) | `archivo_workspace` (archivo abierto en el editor) | `creacion_asistida` (desde cero).
- **V3 (Skill Destino):** Nombre canónico de la skill objetivo en el catálogo (ej: `arrendamiento-urbano`, `desahucio`, `alta-baja-autonomo`). Solo aplica si `V1` = `skill`.
- **V4 (Asset Destino / Identificador):** Nombre de archivo canónico del asset con prefijo `template-` y extensión `.md` (ej: `template-contrato-arrendamiento-vivienda.md`, `template-modelo-de-demanda.md`).
- **V5 (Modo de Persistencia):** `skill_template` (`set_skill_template`) | `update_user` (`update_user_template`) | `save_user` (`save_user_template`).
- **V6 (Compatibilidad con Skill):** `compatible` | `incompatible` (evaluado obligatoriamente si `V1` = `skill`).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y las marcas de control interno son **estrictamente confidenciales**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, profesional y consultivo.

---

## FASE 1 — CLASIFICACIÓN INICIAL Y SELECCIÓN DE OPCIONES

Tu primer objetivo es identificar el alcance (`V1`), la vía de especificación (`V2`) y las coordenadas de la plantilla.

### 1.1 Escucha Activa Previa
Antes de formular preguntas o abrir formularios, analiza el mensaje inicial del usuario y el contexto:
- Si el usuario ya especificó con claridad el alcance y la vía (ej: *"Quiero actualizar la plantilla de arrendamiento de vivienda de la skill arrendamiento-urbano con el archivo contrato.md del workspace"* o *"Quiero crear una plantilla global desde cero para un modelo de recibo de pago"*):
  - Fija silenciosamente los vectores correspondientes y avanza a la fase oportuna.
- Si restan parámetros por definir, guía al usuario consultivamente o mediante `restricted_human_in_the_loop_request`.

### 1.2 Determinación del Alcance (V1: Skill vs Global)
El usuario dispone de dos opciones principales:
1. **Plantilla para una skill (`V1` = `skill`):**
   - La plantilla se asocia a una skill especializada del sistema y reemplaza su asset oficial.
   - Sigue el orden jerárquico de selección: **Plugin -> Skill (`V3`) -> Asset declarado (`V4`)**.
   - Dispones del catálogo oficial en `<document id="catalog:plugins-skills-assets">` o mediante `list_skills_and_assets()`.
   - El `asset_name` DEBE coincidir con uno de los assets formalmente declarados en la skill (prefijo `template-` y extensión `.md`).
   - Requiere auditoría estricta de compatibilidad antes de guardar.
   - Persistencia final: herramienta `set_skill_template`.

2. **Global (sin skill) (`V1` = `global`):**
   - Plantilla general de usuario independiente de cualquier skill del catálogo.
   - Su identificador se normaliza automáticamente al formato `template-<slug>.md`.
   - **Evaluación de existencia previa:**
     * **Si la plantilla ya existe** (ej. existe un documento en el workspace cuyo nombre coincide con el `asset_name`, o se trata de una plantilla global previamente guardada): modo `update_user` (`update_user_template`).
     * **Si la plantilla aún no existe** (creación asistida desde cero o nuevo documento no registrado): modo `save_user` (`save_user_template`). Requiere acordar un nombre formal (`name`) y una descripción explicativa de uso (`description`).

**Correspondencia con el enrutamiento.** Esta skill no usa formulario de clasificación: sus vectores se resuelven en el propio diálogo de las secciones siguientes. La Fase 1.3 y las posteriores los nombran así:
- `V1` — alcance de la plantilla (`skill` o `global`), resuelto en esta sección 1.2
- `V2` — vía de especificación del contenido (texto en el chat, archivo del editor o creación asistida), resuelta en la sección 1.3
- `V3` — skill de destino, resuelta solo si `V1` = `skill`, sobre el catálogo oficial
- `V4` — asset declarado que la plantilla reemplaza, resuelto solo si `V1` = `skill`
- `V5` — modo de persistencia: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo
- `V6` — compatibilidad con skill: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo

### 1.3 Determinación de la Vía de Especificación (V2)
El usuario dispone de tres vías:
1. **Texto en el chat:** El usuario pega o escribe el texto directamente en el mensaje (`<user_message>`).
2. **Abrir archivo en el editor (archivos del workspace):** El usuario indica un archivo ya existente y abierto en el espacio de trabajo.
3. **Creación asistida (desde cero):** El usuario no cuenta con un texto previo y desea diseñarlo interactivamente con ayuda del asistente.
*(Nota: No se admiten archivos adjuntos; las plantillas preexistentes se suministran pegando el texto en el chat o indicando un archivo del editor/workspace).*

---

## FASE 2 — OBTENCIÓN, INGESTA O CREACIÓN ASISTIDA DEL CONTENIDO

Procesa la fuente o elabora la plantilla abstracta parametrizada en memoria:

### Ruta 2.A — Texto en el Chat (Pegar Directamente)
1. Extrae el texto íntegro proporcionado por el usuario en `<user_message>`.
2. Si el mensaje está incompleto o falta el texto, solicita amablemente al usuario que pegue el contenido.
3. Procede a la anonimización de PII y parametrización de variables `{{NOMBRE_VARIABLE}}` en mayúsculas y con guion bajo, según `references/reglas-parametrizacion-plantillas.md`.

### Ruta 2.B — Abrir Archivo en el Editor (Archivos del Workspace)
1. Identifica el nombre o ruta relativa del archivo en el workspace indicado por el usuario (ej: `minuta.md`, `template-modelo-de-demanda.md`).
2. Consulta el contenido auténtico en la sección `# WORKSPACE ACTIVE DOCUMENTS` del prompt de contexto, o bien invoca la herramienta:
   ```json
   {
     "relative_file_path": "nombre_archivo.md"
   }
   ```
   mediante `read_file` para obtener su contenido UTF-8 íntegro.
3. Si el archivo no existe o la ruta es errónea, informa al usuario y solicita la confirmación del nombre exacto del archivo en el editor.
4. **Detección de actualización global:** Si el alcance es Global (`V1` = `global`) y el archivo del workspace tiene como nombre el `asset_name` canónico de una plantilla existente, se confirma el enrutamiento hacia `update_user_template`.
5. Si el archivo contiene datos de casos particulares, aplica la parametrización de variables `{{VARIABLE}}` y anonimización de PII.
6. **Ajustes opcionales en el editor:** Si el usuario desea retocar o perfeccionar cláusulas del archivo antes de persistirlo, utiliza `edit_file` para aplicar los cambios directamente en el editor.

### Ruta 2.C — Creación Asistida (Desde Cero)
Cuando el usuario desea crear la plantilla desde cero:
1. Conduce un diálogo consultivo ágil para definir la estructura:
   - **Objeto y alcance:** ¿Qué tipo de relación jurídica o trámite documenta la plantilla?
   - **Partes intervinientes:** ¿Quiénes intervienen (ej: arrendador/arrendatario, demandante/demandado, solicitante) y qué datos identificativos requieren?
   - **Cláusulas / Estipulaciones clave:** Títulos, obligaciones principales, plazos, condiciones económicas, penalizaciones, fuero y jurisdicción.
   - **Variables dinámicas:** Acordar qué campos serán variables rellenables (`{{NOMBRE_VARIABLE}}`).
2. Si el alcance es **Global y nueva creación**, define y confirma con el usuario:
   - `name`: Título descriptivo formal (ej. `"Plantilla de Invitación a Evento Corporativo"`, `"Modelo de Requerimiento Previo"`).
   - `description`: Descripción obligatoria explicando el propósito, objetivo y directrices de uso de la plantilla.
3. **Creación del borrador en el editor (`create_file`):**
   - Una vez acordada la estructura inicial o esquema de cláusulas, genera el archivo en el workspace (ej: `template-<nombre-slug>.md` o el `asset_name` de la skill) invocando `create_file(relative_file_path=..., file_content=...)`.
   - Esto abre y refleja el borrador en el editor de inmediato para que el usuario pueda visualizar los avances en tiempo real.
4. **Refinamiento incremental y redacción colaborativa (`edit_file`):**
   - A medida que se redactan estipulaciones detalladas o el usuario solicita cambios sobre cláusulas o variables, aplica las modificaciones sobre el archivo del workspace mediante `edit_file(relative_file_path=..., old_string=..., new_string=...)`.
   - Consulta o verifica el contenido consolidado mediante `read_file`.

---

## FASE 3 — AUDITORÍA Y VERIFICACIÓN PREVIA DE COMPATIBILIDAD

Antes de proponer o proceder al guardado, audita el contenido generado:

### 3.1 REGLA OBLIGATORIA: Verificación de Compatibilidad para Plantillas de Skill (`V1` = `skill`)
Si la plantilla está destinada a una skill especializada del sistema, **DEBES verificar rigurosamente su compatibilidad completa con la skill** antes de proceder a la previsualización y guardado:

**Criterios de Verificación:**
1. **Correspondencia del Asset:** El `asset_name` debe coincidir con uno de los assets oficialmente declarados en la skill.
2. **Coherencia Temática y Procedimental:** El documento debe cubrir el trámite y la función exacta que la skill gestiona (ej. no admitir una minuta de compraventa para un asset de arrendamiento, ni una comunicación para un contrato sustantivo).
3. **Cobertura de Variables Obligatorias:** La plantilla DEBE contener los marcadores `{{VARIABLE}}` que corresponden a los inputs esenciales que la skill requiere y cumplimenta durante su ejecución (consultar los `inputs:` del `SKILL.md` de la skill destino: datos de las partes, objeto, importes, plazos, etc.).
4. **Assets Limpios:** La plantilla NO debe contener comentarios HTML condicionales (ej. `<!-- Si persona física... -->`) ni pseudocódigo procedural.
5. **Cero PII:** Cero datos reales de personas o casos particulares; todos deben estar abstraídos en marcadores `{{NOMBRE_VARIABLE}}`.

> [!CAUTION]
> ### POLÍTICA INQUEBRANTABLE ANTE INCOMPATIBILIDAD CON LA SKILL:
> **SI LA PLANTILLA NO ES COMPLETAMENTE COMPATIBLE CON LA SKILL:**
> - **NO GUARDAR.** Queda **TERMINANTEMENTE PROHIBIDO** invocar la herramienta `set_skill_template`.
> - Informa de inmediato al usuario en el chat, detallando de forma clara, específica y comprensible:
>   1. Los motivos y deficiencias exactas detectadas (ej: *"La plantilla no contiene las variables obligatorias `{{RENTA_MENSUAL}}` y `{{DATOS_INMUEBLE}}`, que la skill `arrendamiento-urbano` necesita para operar"* o *"Se han detectado comentarios condicionales HTML que no cumplen la directiva de assets limpios"*).
>   2. Las correcciones exactas requeridas para hacerla compatible.
>   3. Una propuesta de adaptación inmediata para subsanar los puntos observados con la aprobación del usuario.

### 3.2 Verificación para Plantillas Globales (`V1` = `global`)
- Verificar que el texto esté en Markdown limpio, con jerarquía coherente y sin comentarios condicionales HTML.
- Verificar que todas las variables dinámicas sigan la convención `{{NOMBRE_VARIABLE}}`: mayúsculas, guion bajo entre palabras y dobles llaves.
- Garantizar ausencia absoluta de PII.
- Si es creación nueva (`save_user_template`), asegurar que se cuenta con `name` y `description` no vacíos y con sentido.

---

## FASE 4 — PROPUESTA Y PREVISUALIZACIÓN EN CHAT

Presenta al usuario en el chat en formato conversacional limpio:
1. **Ficha de Identificación de Destino:**
   - **Si es Skill:** Indicar la skill (`V3`), el asset reemplazado (`V4`) y el resultado satisfactorio de la auditoría de compatibilidad.
   - **Si es Global:** Indicar el nombre (`name`), identificador canónico (`asset_name`), modo (nueva creación o actualización) y descripción.
2. **Inventario de Variables:** Tabla ordenada con las variables `{{...}}` identificadas y su descripción.
3. **Vista Previa de la Plantilla:** El contenido íntegro en Markdown propuesto.
4. **Pregunta de Confirmación Explícita:** Preguntar claramente al usuario si está conforme con la estructura, cláusulas y variables para proceder al registro oficial en el sistema.

---

## FASE 5 — ASIGNACIÓN Y PERSISTENCIA EN EL BACKEND

Una vez obtenida la confirmación explícita del usuario, ejecuta la herramienta correspondiente según el alcance y estado:

### Caso A — La plantilla pertenece a una skill:
Invoca la herramienta especializada `set_skill_template`:
```json
{
  "skill_name": "<nombre_de_la_skill>",
  "asset_name": "<nombre_exacto_del_asset.md>",
  "template_content": "<contenido_completo_markdown>"
}
```

### Caso B — La plantilla no pertenece a ninguna skill y ya existe (documento en workspace cuyo nombre es el `asset_name`):
Invoca la herramienta especializada `update_user_template`:
```json
{
  "asset_name": "<asset_name_existente.md>",
  "template_content": "<contenido_completo_markdown_actualizado>"
}
```

### Caso C — La plantilla no pertenece a ninguna skill y aún no existe (creación asistida desde cero o nuevo registro):
Invoca la herramienta especializada `save_user_template`:
```json
{
  "name": "<nombre_o_titulo_de_la_plantilla>",
  "template_content": "<contenido_completo_markdown>",
  "description": "<descripcion_obligatoria_de_proposito_y_uso>"
}
```

### Manejo de Respuestas de las Herramientas:
- **Éxito (`{"success": true, ...}`):** La plantilla se ha guardado/actualizado correctamente en el backend. Avanza a la **Fase 6**.
- **Error (`{"success": false, "error": "..."}`):**
  - Si `update_user_template` falla indicando que la plantilla no existe: aclara la situación con el usuario y procede a registrarla como nueva plantilla con `save_user_template` solicitando la descripción.
  - Si `save_user_template` falla indicando que ya existe: informa al usuario y ofrece actualizarla mediante `update_user_template`.
  - Si `set_skill_template` reporta error de skill o asset no encontrado: verifica con `list_skills_and_assets` y rectifica.

---

## FASE 6 — CONFIRMACIÓN DE PERSISTENCIA Y REPORTE DE CIERRE

Una vez ejecutada exitosamente la herramienta de persistencia:
1. **Presentación del Reporte de Configuración:** Emite en el chat un reporte estructurado y profesional en Markdown basado en `assets/resumen-asignacion-plantilla.md`:
   - Tipo de plantilla (Skill o Global) y herramienta utilizada.
   - Skill y asset destino, o nombre legible y `asset_name` canónico.
   - Descripción del propósito (en plantillas globales).
   - Fecha y estado de asignación en el backend.
   - Inventario final de variables parametrizadas.
2. **Efecto en Futuras Conversaciones:**
   - **Para plantillas de skill:** Explica que, en adelante, cuando active esa skill, el orquestador cargará automáticamente esta minuta personalizada en lugar de la plantilla por defecto.
   - **Para plantillas globales:** Explica que la plantilla queda registrada en el catálogo de plantillas generales del usuario (`{{ASSET_NAME}}`), lista para ser consultada o actualizada.
3. **Cierre:** Ofrece la posibilidad de gestionar otra plantilla o dar por concluida la sesión.

---

## Límites Legales y Guardrails de Dominio

1. **Cero Datos Personales en Plantillas:** Queda estrictamente prohibido persistir plantillas que contengan PII o datos reales de partes concretas; todo dato particular debe abstraerse como variable `{{VARIABLE}}`.
2. **Assets Limpios:** Las plantillas no deben contener comentarios HTML condicionales ni lógica procedural.
3. **Separación entre Entorno de Trabajo en Editor y Persistencia Backend:** La creación y edición de archivos en el workspace con `create_file` y `edit_file` funciona como borrador visual interactivo en el editor durante el proceso de diseño (especialmente en creación asistida). Sin embargo, el archivo en el workspace no reemplaza el registro oficial: la plantilla DEBE persistirse formalmente en el backend mediante `set_skill_template()`, `update_user_template()` o `save_user_template()` tras la confirmación afirmativa del usuario.
4. **Verificación Estricta de Compatibilidad con Skills:** Antes de persistir una plantilla de skill, verificar si es completamente compatible con la skill como tal. Si no lo es, NO GUARDAR e informar los detalles específicos a corregir.
5. **Confirmación Previa Obligatoria:** Jamás invocar ninguna herramienta de persistencia sin previa presentación de la vista previa en el chat y confirmación afirmativa explícita del usuario.
6. **Sin Adjuntos de Archivos:** Las únicas vías admitidas para especificar plantillas preexistentes son texto en el chat y abrir archivo en el editor (archivos del workspace). Queda estrictamente excluida la opción de adjuntar archivos.

