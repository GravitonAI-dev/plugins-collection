# Plugin: gestion-plantillas

Plugin de GravitonAI para la creación, parametrización, actualización y registro de plantillas de documentos personalizadas (assets), tanto asociadas a skills del sistema como globales de usuario.

## Qué hace este plugin
- Permite a los usuarios registrar plantillas a partir de texto preexistente (texto en el chat o abrir archivo en el editor / archivos del workspace) o crearlas de manera asistida desde cero. (Queda excluida la opción de adjuntar archivos).
- Soporta dos alcances: **Plantilla para una skill** (reemplazando el asset oficial de una skill del catálogo) o **Global (sin skill)** (plantillas generales de usuario).
- Analiza o redacta colaborativamente el documento y lo estructura en Markdown limpio con marcadores `{{nombre_variable}}`.
- Garantiza assets limpios (cero datos personales PII y cero comentarios HTML condicionales).
- Realiza una auditoría obligatoria de compatibilidad con la skill antes de guardar (bloqueando el guardado si no es compatible).
- Persiste la plantilla en el backend mediante la herramienta especializada adecuada:
  - `set_skill_template(skill_name, asset_name, template_content)`: Si la plantilla pertenece a una skill.
  - `update_user_template(asset_name, template_content)`: Si la plantilla no pertenece a ninguna skill y ya existe (documento en el workspace cuyo nombre es el `asset_name`).
  - `save_user_template(name, template_content, description)`: Si la plantilla no pertenece a ninguna skill y aún no existe (creación asistida desde cero).

## Skills incluidas
- `registrar-plantillas`: Flujo estructurado y consultivo para clasificar, obtener o crear asistidamente, verificar compatibilidad estricta y persistir plantillas de skill o de usuario.

## Herramientas requeridas
- `io.gravitonai.tools.list_skills_and_assets`: Descubrimiento dinámico de plugins, skills y assets del catálogo.
- `io.gravitonai.tools.set_skill_template`: Persistencia de plantillas asignadas a una skill.
- `io.gravitonai.tools.update_user_template`: Actualización de plantillas de usuario existentes.
- `io.gravitonai.tools.save_user_template`: Creación de nuevas plantillas de usuario con descripción.
- `io.gravitonai.tools.read_file`: Lectura de archivos existentes en el espacio de trabajo activo (editor).
- `io.gravitonai.tools.create_file`: Creación de archivos en el workspace para volcar y visualizar el borrador en el editor.
- `io.gravitonai.tools.edit_file`: Edición incremental y refinamiento de plantillas en el editor.
- `io.gravitonai.tools.restricted_human_in_the_loop_request`: Selección guiada de opciones cerradas (alcance, origen, catálogo).
- `io.gravitonai.tools.human_in_the_loop_request`: Formularios de consulta y confirmación al usuario.
- `io.gravitonai.tools.slot_filling_request`: Captura de metadatos o nombres de variables en lotes.
