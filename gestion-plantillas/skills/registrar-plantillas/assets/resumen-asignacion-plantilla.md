# Reporte de Configuración de Plantilla

> REPORTE DE CONFIGURACIÓN — Plantilla registrada/actualizada exitosamente en el sistema.

## 1. Datos del Registro

| Parámetro | Valor Asignado |
|---|---|
| Tipo de Plantilla | {{tipo_plantilla}} (Skill / Global) |
| Skill Objetivo | {{skill_name}} |
| Nombre / Título | {{nombre_plantilla}} |
| Identificador de Asset | `{{asset_name}}` |
| Herramienta Utilizada | `{{herramienta_usada}}` (`set_skill_template` / `update_user_template` / `save_user_template`) |
| Canal de Origen | {{canal_origen}} (Texto en el chat / Archivo en el editor / Creación asistida) |
| Fecha de Registro | {{fecha_registro}} |
| Estado en Orquestador | {{estado_asignacion}} |

---

## 2. Descripción y Propósito

{{descripcion_plantilla}}

---

## 3. Inventario de Variables Parametrizadas

A continuación se detallan los marcadores identificados y abstraídos en la plantilla:

| Variable | Tipo de Dato / Descripción |
|---|---|
| `{{variable_1}}` | {{descripcion_variable_1}} |
| `{{variable_2}}` | {{descripcion_variable_2}} |
| `{{variable_3}}` | {{descripcion_variable_3}} |

---

## 4. Instrucciones de Uso y Activación

{{instrucciones_activacion}}
- **Si es Plantilla de Skill (`set_skill_template`):** En todas las siguientes conversaciones en las que actives la skill `{{skill_name}}`, el orquestador utilizará automáticamente esta plantilla personalizada como base para redactar tus documentos.
- **Si es Plantilla Global (`save_user_template` / `update_user_template`):** La plantilla queda registrada en el catálogo de plantillas generales del usuario (`{{asset_name}}`), disponible para ser reutilizada o actualizada en cualquier momento.
