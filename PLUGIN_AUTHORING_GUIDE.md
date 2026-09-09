# Guía de Arquitectura y Construcción de Plugins (Para el LLM Constructor)

**CONTEXTO PARA EL AGENTE:**
Eres el LLM encargado de construir y diseñar nuevos plugins y skills para GravitonAI. Este documento es tu **fuente de verdad estructural**. Define las mejores prácticas de Prompt Engineering, la separación estricta de responsabilidades y las plantillas exactas que DEBES usar al generar la estructura de un nuevo plugin. 

---

## 1. LA REGLA DE ORO: Separación de Responsabilidades

Para maximizar la precisión de los agentes operacionales y evitar colisiones cognitivas, el contexto del sistema está dividido en 3 capas. **TIENES ESTRICTAMENTE PROHIBIDO repetir directivas de una capa superior en los archivos de una capa inferior.**

*   **CAPA GLOBAL (Raíz `/CLAUDE.md`):** Ya maneja toda la mecánica del sistema: sincronización obligatoria con `Read`, reglas "Zero-Omission", captura obligatoria en bloque de grupos de datos estructurados mediante `slot_filling_request`, confirmación de secciones/cláusulas exclusivamente en chat (`¿Confirmamos esta cláusula?`), sintaxis global de placeholders `{{DATO}}`, prohibición de corchetes para placeholders, emails/URLs como texto plano (sin `mailto:` ni auto-links), y reserva exclusiva de corchetes simples para identificadores de privacidad (ej. `[PERSON_1]`). *(Nota de arquitectura: Las reglas de "Zero-Omission" y resolución de placeholders aplican a skills sustantivas de tramitación documental para clientes. En plugins de gestión y diseño de plantillas como `gestion-plantillas`, los documentos del workspace son activos de plantilla y los marcadores `{{VARIABLE}}` constituyen el resultado deliberado y final, quedando exentos de ser rellenados con datos de clientes).* **No generes estas reglas en los CLAUDE.md de los nuevos plugins.**
*   **CAPA PLUGIN (`[plugin]/CLAUDE.md`):** Controla EXCLUSIVAMENTE el *Dominio de Negocio* (Reglas de la industria, tono experto, límites legales/técnicos, y matriz de escalación).
*   **CAPA ASSETS (`[plugin]/skills/[nombre]/assets/*.md`):** Recursos y archivos base limpios (ej. esquemas, datos base, reportes o plantillas estructuradas). **Solo aquellos assets que sean plantillas propiamente dichas (formatos estrictos con marcadores `{{variable}}`) llevan el prefijo obligatorio `template-`**; los demás assets (formatos libres, tablas de apoyo o reportes) se nombran en `kebab-case` sin prefijo. Tienen **ESTRICTAMENTE PROHIBIDO** contener comentarios HTML con condicionales (ej. `<!-- Si ... -->`), opciones alternativas (`<!-- Opcion A ... -->`) o directivas procedimentales.
*   **CAPA SKILL (`[plugin]/skills/[nombre]/SKILL.md`):** Controla EXCLUSIVAMENTE la *Maquinaria de Ejecución* (Vectores de estado, enrutamiento, preguntas predecibles, resolución de condicionales y ciclo de edición incremental). **Toda la lógica condicional, variantes de redacción, cláusulas opcionales e instrucciones de sustitución dinámica residen ÚNICA y EXCLUSIVAMENTE en este archivo.**

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

## 3. PLANTILLA OBLIGATORIA: El archivo `SKILL.md` (Estándar Canónico de 5 Fases)

Toda skill en GravitonAI debe estructurarse obligatoriamente bajo el **flujo determinista de 5 fases secuenciales** (referencia canónica: `arrendamiento-urbano`). Este estándar garantiza consultas interactivas fluidas, cero vacíos en disco, validación estricta de minutas y edición incremental controlada.

```yaml
---
name: [nombre-de-la-skill]
description: >
  [Descripción densa de 1-2 párrafos: qué genera y adapta con precisión, marco normativo/técnico
  consolidado y verificado en fuentes oficiales, metodología operativa (clasificación inicial de
  vectores mediante formulario interactivo, plan de acción y negociación de assets vía chat,
  creación del documento base en workspace y edición incremental cláusula a cláusula / sección a sección).
  Si la skill se basa en una ley concreta, esa ley DEBE aparecer aquí con su nombre y número,
  en negrita con doble asterisco, seguida de una frase breve que explique qué regula
  (ej. la **Ley 29/1994 de Arrendamientos Urbanos (LAU)**, que rige los alquileres de vivienda y
  de uso distinto). Esta description es la que se muestra en la tarjeta (card) de la skill.
  Delimitación negativa explícita: NO usar para X, Y, Z.]
when_to_use: |
  - [Caso de activación específico 1]
  - [Caso de activación específico 2]
  - [Caso de activación específico 3 (ej. uso de plantilla del sistema o minuta propia del usuario)]
inputs:
  - [variable_vector_1]: [valores posibles] (V1)
  - [variable_vector_2]: [valores posibles] (V2)
  - [variable_vector_3]: [valores posibles] (V3)
  - [variable_vector_4]: [valores posibles] (V4)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - [variable_esencial_1]: [descripción y formato]
  - [variable_esencial_2]: [descripción y formato]
  - [pactos_opcionales]: [descripción de cláusulas facultativas o parámetros variables]
outputs:
  - [archivo_generado]: [documento completo generado en markdown, DRAFT, conforme al marco legal/técnico]
references:
  - references/[archivo_contexto_1].md
  - references/[archivo_contexto_2].md
assets:
  - assets/template-[plantilla_base_1].md
  - assets/template-[plantilla_base_2].md
---
```

```markdown
# [Nombre de la Acción Principal]

> DRAFT — para revisión por un [perfil profesional: abogado / asesor / especialista] antes de su firma o presentación. No constituye [límite legal/técnico: asesoramiento jurídico definitivo / dictamen vinculante].

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):
Para garantizar un enrutamiento determinista y el cumplimiento de las normas imperativas del dominio, el asistente resuelve y mantiene internamente en memoria los siguientes vectores:
- **V1 ([Destino / Materia Principal]):** `[opcion_a]` | `[opcion_b]` | `[fuera_de_alcance]`.
- **V2 ([Tipo Objeto / Subtipo]):** `[subtipo_a]` | `[subtipo_b]`. *(Inferido o clasificado)*.
- **V3 ([Naturaleza Parte A / Sujeto]):** `persona_fisica` | `persona_juridica`.
- **V4 ([Naturaleza Parte B / Contraparte]):** `persona_fisica` | `persona_juridica`.
- **V5 (Origen Plantilla / Asset):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD Y COMUNICACIÓN AMIGABLE (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`, etc.), los resúmenes de validación con marcas (ej. "V1 resuelto ✔"), y **cualquier mención a términos de arquitectura interna de software (como "backend", "frontend", "orquestador", "runtime", "base de datos", o nombres de herramientas técnicas como `set_skill_template`, `read_file`, `edit_file`, etc.) son estrictamente de control interno y están TERMINANTEMENTE PROHIBIDOS en el chat con el usuario**.
> - Toda interacción debe ser comprensible, asistencial, empática, profesional y no técnica respecto a la estructura del software.
> - Para referirse a la infraestructura general, utiliza de forma natural **"el sistema"** o **"la plataforma"**. Sin embargo, al pedir confirmación o referirte a espacios de trabajo y destinos visibles al usuario, sé específico según el área de la interfaz: utiliza **"la sección de plantillas"** (o *"tu catálogo de plantillas"*) al guardar o gestionar modelos (ej. *"¿Quieres que guarde en la sección de plantillas?"*), y **"el editor"** o **"tu espacio de trabajo"** al interactuar con borradores de documentos (ej. *"he preparado el borrador en el editor"*). Evita fórmulas impersonales genéricas como *"en el sistema"* o tecnicismos como *"en disco"*.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

Tu primer objetivo es resolver los vectores de estado de clasificación **V1, V2, V3 y V4**.

### 1.1 Escucha Activa Previa
Antes de invocar formularios, evalúa el mensaje inicial y el historial de la conversación:
- Si el usuario **ya proporcionó de forma inequívoca** los datos para resolver los vectores de clasificación, regístralos en silencio y avanza directamente a la **Fase 2**.
- Si falta resolver alguno de los vectores de clasificación o existe ambigüedad, invoca de inmediato la herramienta `restricted_human_in_the_loop_request` para formular el árbol de decisión interactivo.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas necesarias para completar la resolución de los vectores pendientes:

```json
{
  "form_data": [
    {
      "id": "vector_1_id",
      "rationale": "Resolver V1 para determinar el régimen y alcance aplicable.",
      "question": "¿[Pregunta clara y directa sobre la finalidad/objeto principal]?",
      "options": [
        {"id": "opcion_a", "label": "[Descripción clara de la opción A]"},
        {"id": "opcion_b", "label": "[Descripción clara de la opción B]"},
        {"id": "fuera_de_alcance", "label": "[Opción no cubierta por la skill]"}
      ]
    },
    {
      "id": "vector_3_id",
      "rationale": "Resolver V3 para fijar la estructura de partes y límites imperativos.",
      "question": "¿[Pregunta sobre la naturaleza jurídica de la parte principal]?",
      "options": [
        {"id": "persona_fisica", "label": "Persona física (particular)"},
        {"id": "persona_juridica", "label": "Persona jurídica (empresa, entidad)"}
      ]
    }
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez fijados los vectores de clasificación, evalúa la rama de ejecución:
* **Si `[V1 = fuera_de_alcance]` $\rightarrow$ Detener proceso (Fuera de Alcance):**
  - Informa en el chat de que el caso se rige por normativas o supuestos distintos, quedando excluido del alcance de esta skill.
  - Ofrece derivar el caso al profesional o plugin competente. **No crees documento.**
* **Si `[V1 = opcion_a]` (Dentro de alcance):**
  - Régimen aplicable y directivas de dominio.
  - Plantilla del sistema propuesta: `assets/template-[plantilla_a].md`.
  - Proceder a la **Fase 2**.
* **Si `[V1 = opcion_b]` (Dentro de alcance):**
  - Régimen aplicable y directivas de dominio.
  - Plantilla del sistema propuesta: `assets/template-[plantilla_b].md`.
  - Proceder a la **Fase 2**.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias correspondientes directamente desde el bloque `<document kind="references-collection">` de tu system prompt.
2. Opcionalmente verifica fuentes oficiales en vivo mediante `web_search` si se requieren confirmar índices, tipos o reformas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y cordial que contenga:
1. **Marco Legal / Técnico Aplicable:**
   - Cita la normativa o estándares vigentes y explica con claridad el impacto de la clasificación obtenida (`V1-V4`).
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Detalla que dispones de la plantilla oficial adaptada (`assets/template-[plantilla].md`), con una estructura jurídica y técnica completa y equilibrada.
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación de V5 (Origen Plantilla) y Manejo de la Elección
* **Si `[V5 = plantilla_sistema]` (El usuario acepta la plantilla propuesta):**
  Toma el texto íntegro de la plantilla correspondiente directamente desde el bloque `<document kind="assets-collection">` de tu system prompt y procede de inmediato a la **Fase 3**.
* **Si `[V5 = plantilla_usuario]` (El usuario aporta su propia minuta adjuntando un documento o pegando texto):**
  1. **Acceso al Contenido del Adjunto:**
     - Si el usuario adjunta un archivo, su contenido está disponible en el bloque `# ATTACHED DOCUMENTS` / `<attached_documents>` del contexto.
     - Si el usuario pegó el texto directamente en el chat, tómalo del bloque `# USER MESSAGE` / `<user_message>`.
  2. **Guardrail de Verificación de Normas Imperativas:**
     - Analiza el contenido de la plantilla aportada. Si contiene estipulaciones ilegales, cláusulas nulas o contrarias a normas imperativas:
       - Advierte expresamente al usuario en el chat sobre la nulidad de dichas cláusulas.
       - Propón la redacción legalmente válida y ajustada a Derecho.
  3. **Adopción de la Plantilla:**
     - Adopta el texto íntegro de la plantilla del usuario como base y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada (`V5`: ya sea el asset del catálogo desde `<document kind="assets-collection">` o la plantilla adjunta por el usuario desde `<attached_documents>` / `<user_message>`) en el archivo del workspace (ej: `[nombre_documento].md`).
   - Aplica el principio **Zero-Omission**:
     - Sustituye todos los datos ya resueltos a través de los vectores `V1-V4` y la escucha activa inicial.
     - Todos los datos o campos pendientes deben permanecer explícitamente como marcadores `{{DATO_FALTANTE}}` en mayúsculas entre dobles llaves.
     - PROHIBIDO dejar archivos en blanco, sólo con títulos o crear resúmenes.
2. **Validación de Integridad:**
   - La comprobación de integridad y contenido del archivo creado se realiza consultando prioritariamente la sección `# WORKSPACE ACTIVE DOCUMENTS` del prompt, donde el sistema mantiene siempre la última versión de todos los documentos. Solo se debe invocar `read_file` si es estrictamente necesario y en algún caso extremo (ej. el archivo no aparece en dicha sección o contenido truncado).
3. **Confirmación en Chat:**
   - Emite un mensaje indicando que el documento base ha quedado preparado en el editor (en el espacio de trabajo).
   - En la misma respuesta, sin detener la marcha, introduce la primera sección de la Fase 4 para iniciar la edición incremental (invocando `slot_filling_request` si la primera sección requiere un grupo de datos, o formulando la consulta correspondiente).

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los siguientes bloques del documento. Por cada sección que contenga placeholders `{{...}}` o requiera pacto/detalle, ejecuta el **Ciclo de Edición Incremental**:

```
[Recogida de datos: slot_filling_request (grupos de datos) / Chat (negociación)]
                                  │
                                  ▼
               [Vista Previa en texto plano en CHAT]
                                  │
                                  ▼
           [Confirmación en CHAT: "¿Confirmamos esta cláusula?"]
                                  │
                                  ▼
                    [edit_file en el editor]
```

### Protocolo Obligatorio por Sección:
1. **Recogida de Datos y Diálogo:**
   - **Grupos de datos estructurados (MANDATORIO con `slot_filling_request`):** Siempre que la sección requiera capturar grupos de datos de personas físicas o jurídicas (nombre, DNI/NIE/CIF, domicilio, teléfono, correo), datos descriptivos de inmuebles (dirección, referencia catastral, superficie), vehículos (matrícula, bastidor, marca/modelo), importes desglosados, deudas o cuentas bancarias, **DEBES invocar `slot_filling_request`** para solicitar todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
   - **Negociación y asesoramiento técnico/legal:** Cuando la cláusula dependa de una decisión o pacto (duración, reparto de gastos, compensaciones), explica en el chat las consecuencias legales del régimen por defecto y las opciones disponibles (o usa `restricted_human_in_the_loop_request` si son opciones predefinidas cerradas).
2. **Vista Previa (Preview) en CHAT:** Tras recibir los datos del formulario o la elección del usuario, redacta la cláusula y muestra el texto exacto redactado en texto plano en el chat (sin bloques de código ni backticks).
3. **Petición de Confirmación en CHAT:** Pregunta literalmente en el chat: `¿Confirmamos esta cláusula?` (o `¿Confirmamos esta sección?`).
4. **Edición en Disco:** Tras el "sí" o confirmación del usuario en el chat, aplica `edit_file` sustituyendo con exactitud milimétrica el texto antiguo por el nuevo. La verificación del documento se apoya prioritariamente en `# WORKSPACE ACTIVE DOCUMENTS`, recurriendo a `read_file` únicamente en casos extremos y estrictamente necesarios.

---

### Hoja de Ruta de Secciones y Cláusulas Condicionales:

#### 1. [Nombre de la Sección 1 - Ej. Encabezamiento y Partes]
- **Recogida con `slot_filling_request`:** Solicitar en bloque todos los datos de identificación de las partes (`{{nombre}}`, `{{nif}}`, `{{domicilio}}`, etc.) mediante formulario por lotes.
- **Condicional [Sujeto / Persona Jurídica]:**
  - *Si [Condición A - Persona Jurídica]:* Redactar e insertar: `Representado por: {{nombre_representante}}, con NIF {{nif_representante}}, en calidad de {{cargo_representante}} según escritura de poder.`
  - *Si [Condición B - Persona Física]:* Redactar e insertar comparecencia en su propio nombre y derecho.
- **Vista previa y confirmación en chat:** Mostrar la comparecencia completa redactada en texto plano y preguntar: `¿Confirmamos estos datos de las partes?` Tras la confirmación en chat, aplicar `edit_file`.

#### 2. [Nombre de la Sección 2 - Ej. Objeto y Alcance]
- **Recogida con `slot_filling_request` (si hay datos identificativos):** Dirección, referencia catastral, superficie, etc.
- **Condicional [Elementos Accesorios / Variantes]:**
  - *Si incluye variantes opcionales:* Insertar estipulación detallando los anejos o prestaciones complementarias.
- **Vista previa y confirmación en chat:** `¿Confirmamos esta cláusula?` $\rightarrow$ `edit_file`.

#### 3. [Nombre de la Sección 3 - Ej. Duración y Plazos]
- Plazos pactados y vigencia inicial.
- **Reglas Imperativas y Condicionales de Plazo:**
  - *Si plazo pactado < mínimo legal:* Redactar e insertar cláusula de prórroga obligatoria conforme a la ley aplicable.

#### 4. [Nombre de la Sección 4 - Ej. Condiciones Económicas / Régimen de Pago]
- Importes, periodicidad y medio de pago.
- **Condicionales de Distribución de Cargas / Gastos:**
  - *Opción A:* [Texto exacto de la estipulación para Opción A].
  - *Opción B:* [Texto exacto de la estipulación para Opción B].

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, muestra en el chat el siguiente menú interactivo de opciones finales:

```markdown
El borrador completo del documento ha sido redactado y actualizado en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección/cláusula existente.
2. Añadir una estipulación o cláusula adicional a medida.
3. Eliminar contenido opcional.
4. Corregir datos identificativos o importes.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Obligatorias al Cerrar:
Cuando el usuario seleccione finalizar el documento, emite las advertencias preceptivas:
1. **Carácter de Borrador (DRAFT):** El documento generado es una propuesta sujeta a revisión por un profesional cualificado antes de su firma o presentación oficial.
2. **Obligaciones Administrativas / Tributarias:** Recordar los tributos, depósitos obligatorios o comunicaciones que deban formalizarse ante las autoridades competentes.
3. **Formalización y Registros:** Recordar la conveniencia o necesidad de elevación a público, liquidación fiscal o inscripción en registros correspondientes.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Normas Imperativas y Cláusulas Nulas:** Especificar las estipulaciones que bajo ningún concepto pueden pactarse en perjuicio de las partes protegidas por ley. Si el usuario solicita una cláusula prohibida, rechazar la redacción, citar el precepto legal correspondiente y proponer la alternativa legal válida.
2. **Límites de Plazo y Garantías:** Detallar las restricciones fijadas por los vectores `V1`-`V4`.
3. **Fuero y Jurisdicción Imperativa:** Restricciones de sumisión judicial o administrativa.
4. **Cero Invención de Datos y Normas:** Todos los datos reales no aportados deben permanecer como `{{DATO_FALTANTE}}`. Queda estrictamente prohibido inventar números identificativos, referencias catastrales, jurisprudencia o artículos legales.
```
