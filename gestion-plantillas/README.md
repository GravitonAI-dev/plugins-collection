# Plugin: gestion-plantillas

Plugin de GravitonAI para la creación, parametrización y registro de plantillas de documentos personalizadas (assets) asociadas a las skills del sistema.

## Qué hace este plugin
- Permite a los usuarios proporcionar sus propias minutas o contratos de ejemplo (mediante archivos adjuntos o texto en el chat).
- Analiza el documento y lo convierte automáticamente en una plantilla estandarizada en Markdown con marcadores `{{nombre_variable}}`.
- Garantiza que la plantilla cumpla las convenciones de assets limpios del sistema (sin datos personales y sin comentarios condicionales).
- Registra la plantilla en el backend de LangGraph invocando la herramienta `set_skill_template(skill_name, asset_name, template_content)`.

## Skills incluidas
- `personalizar-plantilla-skill`: Flujo guiado en 5 fases para procesar un documento de ejemplo, parametrizarlo y asignarlo como asset de una skill objetivo.

## Herramientas requeridas
- `io.gravitonai.tools.set_skill_template`: Persistencia de la plantilla personalizada en el orquestador.
- `io.gravitonai.tools.read_file`: Inspección y verificación de archivos del workspace.
- `io.gravitonai.tools.create_file`: Creación del borrador de la plantilla en el workspace.
- `io.gravitonai.tools.edit_file`: Ajustes incrementales de la plantilla en el workspace.
- `io.gravitonai.tools.restricted_human_in_the_loop_request`: Selección guiada de skill y asset.
- `io.gravitonai.tools.human_in_the_loop_request`: Formularios de consulta al usuario.
- `io.gravitonai.tools.slot_filling_request`: Captura de metadatos o nombres de variables.
