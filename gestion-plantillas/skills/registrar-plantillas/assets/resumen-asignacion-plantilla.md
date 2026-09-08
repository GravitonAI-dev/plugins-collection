# Reporte de Configuración de Plantilla

> Plantilla registrada/actualizada exitosamente en el sistema.

## 1. Datos del Registro

| Parámetro | Detalle |
|---|---|
| Tipo de Plantilla | {{TIPO_PLANTILLA}} (Skill / Global) |
| Skill Objetivo | {{SKILL_NAME}} |
| Nombre / Título | {{NOMBRE_PLANTILLA}} |
| Identificador de Asset | `{{ASSET_NAME}}` |
| Herramienta Utilizada | `{{HERRAMIENTA_USADA}}` (`set_skill_template` / `update_user_template` / `save_user_template`) |
| Canal de Origen | {{CANAL_ORIGEN}} (Texto en el chat / Archivo en el editor / Creación asistida) |
| Fecha de Registro | {{FECHA_REGISTRO}} |
| Estado en Orquestador | {{ESTADO_ASIGNACION}} |

---

## 2. Descripción y Propósito

{{DESCRIPCION_PLANTILLA}}

---

## 3. Inventario de Variables Parametrizadas

A continuación se detallan los campos variables identificados en la plantilla:

| Variable | Descripción / Campo |
|---|---|
| `{{VARIABLE_1}}` | {{DESCRIPCION_VARIABLE_1}} |
| `{{VARIABLE_2}}` | {{DESCRIPCION_VARIABLE_2}} |
| `{{VARIABLE_3}}` | {{DESCRIPCION_VARIABLE_3}} |

---

## 4. Disponibilidad y Próximos Pasos

{{INSTRUCCIONES_ACTIVACION}}
- **Si es Plantilla de Skill (`set_skill_template`):** En todas las siguientes conversaciones en las que actives la skill `{{SKILL_NAME}}`, el orquestador utilizará automáticamente esta plantilla personalizada como base para redactar tus documentos.
- **Si es Plantilla Global (`save_user_template` / `update_user_template`):** La plantilla queda registrada en el catálogo de plantillas generales del usuario (`{{ASSET_NAME}}`), disponible para ser reutilizada o actualizada en cualquier momento.
