# Guía de Arquitectura y Construcción de Plugins (Para el LLM Constructor)

**CONTEXTO PARA EL AGENTE:**
Eres el LLM encargado de construir y diseñar nuevos plugins y skills para GravitonAI. Este documento es tu **fuente de verdad estructural**. Define las mejores prácticas de Prompt Engineering, la separación estricta de responsabilidades y las plantillas exactas que DEBES usar al generar la estructura de un nuevo plugin. 

---

## 1. LA REGLA DE ORO: Separación de Responsabilidades

Para maximizar la precisión de los agentes operacionales y evitar colisiones cognitivas, el contexto del sistema está dividido en 3 capas. **TIENES ESTRICTAMENTE PROHIBIDO repetir directivas de una capa superior en los archivos de una capa inferior.**

*   **CAPA GLOBAL (Raíz `/CLAUDE.md`):** Ya maneja toda la mecánica del sistema: sincronización obligatoria con `Read`, reglas "Zero-Omission", sintaxis global de placeholders `{{DATO}}`, prohibición de invenciones de formato e identificadores de privacidad (ej. `[PERSON_1]`). **No generes estas reglas en los CLAUDE.md de los nuevos plugins.**
*   **CAPA PLUGIN (`[plugin]/CLAUDE.md`):** Controla EXCLUSIVAMENTE el *Dominio de Negocio* (Reglas de la industria, tono experto, límites legales/técnicos, y matriz de escalación).
*   **CAPA SKILL (`[plugin]/skills/[nombre]/SKILL.md`):** Controla EXCLUSIVAMENTE la *Maquinaria de Ejecución* (Vectores de estado, enrutamiento, preguntas predecibles y ciclo de edición incremental).

---

## 2. PLANTILLA OBLIGATORIA: El archivo `[plugin]/CLAUDE.md`

Cuando generes el `CLAUDE.md` de un nuevo plugin, debes apegarte a esta estructura exacta y adaptarla al dominio. Omite cualquier regla operativa sobre cómo manejar archivos.

```markdown
# Plugin: [Nombre del Plugin]

## Propósito
[Descripción concisa de 1-2 párrafos sobre el objetivo del plugin y lo que explícitamente NO cubre]

## Audiencia Objetivo
- [Perfil de usuario 1]
- [Perfil de usuario 2]

## Contexto del Dominio / Entorno
[Reglas por defecto del entorno de negocio. Ej. Leyes aplicables, frameworks de código por defecto, normativas contables, etc.]

## Tono y Estilo (Mandatorio)
- **Lenguaje:** [Ej. Técnico, jurídico formal, persuasivo, etc.]
- **Formato general:** [Ej. Cláusulas numeradas, viñetas, tablas, etc.]
- **Marca de Agua:** [Texto o disclaimer obligatorio que deba ir en los documentos generados, si aplica al dominio. Ej. > DRAFT - Para revisión...]

## Guardrails y Límites del Dominio
1. **Regla Imperativa 1:** [Ej. Nunca redactar cláusulas nulas o código inseguro]
2. **Cero Invenciones:** [Regla estricta sobre no inventar normativas, dependencias o datos críticos]
3. **Roles:** [Limitación de la responsabilidad del asistente en este dominio específico]

## Matriz de Escalación Universal
En los siguientes escenarios, detén la generación y sugiere la escalación:
| Situación Detectada | Acción |
| :--- | :--- |
| [Escenario crítico o de alto riesgo 1] | Detener y [acción sugerida / derivar a experto]. |
| [Escenario de ambigüedad técnica] | Usar `web_search` para verificar. Si persiste duda, advertir. |
```

---

## 3. PLANTILLA OBLIGATORIA: El archivo `SKILL.md`

Cuando generes una nueva skill, debes estructurarla como un flujo determinista, obligando al agente operacional a ser "invisible" en su razonamiento.

```yaml
---
name: [nombre-de-la-skill]
description: >
  [Descripción clara y completa de lo que genera y sus límites]
when_to_use: |
  - [Caso de uso 1]
  - [Caso de uso 2]
inputs:
  - [variable_1]: [descripción]
  - [variable_2]: [descripción]
outputs:
  - [archivo_generado]: [descripción y formato]
references:
  - references/[archivo_contexto].md
assets:
  - assets/[plantilla_base].md
---
```

```markdown
# [Nombre de la Acción Principal]

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la lógica descrita en este documento (la clasificación de vectores, la validación y la creación base) es un flujo de ejecución ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2").
- Resúmenes de validación con checks (ej. "Dato resuelto ✔").
- Fases de instrucción (ej. "Ahora voy a crear el documento", "Pasemos al punto 4").
- Preámbulos conversacionales antes de hacer preguntas. Si es tu turno de preguntar, emite únicamente la pregunta exacta.

## 1. CLASIFICACIÓN DINÁMICA (Vectores de Estado)

Tu primer objetivo es resolver los siguientes vectores de manera SILENCIOSA usando Escucha Activa:
- **V1 ([Nombre del Vector]):** [Opciones posibles].
- **V2 ([Nombre del Vector]):** [Opciones posibles].

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o más vectores, TIENES PROHIBIDO inventar la redacción. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, en este orden estricto:
* Para V1: "¿[Pregunta exacta y natural para obtener V1]?"
* Para V2: "¿[Pregunta exacta y natural para obtener V2]?"

### Enrutamiento de Estado (Routing)
Una vez resueltos todos los vectores, evalúa:
- Si [V1 = X] -> Plantilla a usar: `assets/asset_x.md`.
- Si [V2 = Y] -> Detener proceso (fuera de alcance). No crees documento.

## 2. VERIFICACIÓN DE CONTEXTO (Interno)
*(Esta sección es opcional. Úsala si la skill debe consultar internet, normativas, APIs o archivos de referencia antes de redactar).*
1. Consulta la información en [nombre-archivo-reference.md] directamente desde el bloque `<document kind="references-collection">` de tu system prompt (TIENES ESTRICTAMENTE PROHIBIDO usar la herramienta `read_file` para leer references o assets).
2. Si requieres verificar fuentes oficiales externas en vivo, usa `web_search`.
3. Si hay cambios normativos, aplícalos a tu memoria.

## 3. CREACIÓN DEL DOCUMENTO BASE (Cero Vacíos)
Inmediatamente tras el paso anterior, estás OBLIGADO a crear el documento:
1. Toma el texto íntegro de la plantilla [nombre-archivo-asset.md], disponible directamente en el bloque `<document kind="assets-collection">` de tu system prompt (NO uses la herramienta `read_file` para leer plantillas).
2. Reemplaza en memoria TODOS los datos que ya poseas (gracias a los vectores, escucha activa e investigación). Los faltantes quedan como `{{DATO_FALTANTE}}`.
3. Utiliza `Write` (o `create_file`) para guardar el archivo en disco del workspace.
4. (Regla Global): Ejecuta `Read` (o `read_file`) exclusivamente sobre el archivo creado en disco para validar y confirma la ruta absoluta en el chat al usuario. Inmediatamente después, en la misma respuesta, formula la primera pregunta de la edición incremental (Punto 4) para no detener la conversación.

## 4. EDICIÓN INCREMENTAL DE CLÁUSULAS / SECCIONES
Recorre secuencialmente la siguiente lista. Por cada sección incompleta, aplica el Ciclo de Edición Incremental Global (Formular Pregunta -> Mostrar Vista Previa en texto plano -> Pedir Confirmación -> Usar `Edit` en disco):
1. **[Sección 1]:** [Qué datos faltan, instrucciones específicas].
2. **[Sección 2]:** [Qué datos faltan, instrucciones específicas].

## BUCLE DE REALIMENTACIÓN FINAL
Tras completar el Punto 4, muestra el siguiente menú y espera instrucciones (aplicando `Edit` según corresponda):
1. Ajustar una sección existente.
2. Añadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.
```
