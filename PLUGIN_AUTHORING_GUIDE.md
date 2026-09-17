# Guía de Arquitectura y Construcción de Plugins (Para el LLM Constructor)

**CONTEXTO PARA EL AGENTE:**
Eres el LLM encargado de construir y diseñar nuevos plugins y skills para GravitonAI. Este documento es tu **fuente de verdad estructural**. Define las mejores prácticas de Prompt Engineering, la separación estricta de responsabilidades y las plantillas exactas que DEBES usar al generar la estructura de un nuevo plugin. 

---

## 1. LA REGLA DE ORO: Separación de Responsabilidades

Para maximizar la precisión de los agentes operacionales y evitar colisiones cognitivas, el contexto del sistema está dividido en 3 capas. **TIENES ESTRICTAMENTE PROHIBIDO repetir directivas de una capa superior en los archivos de una capa inferior.**

*   **CAPA GLOBAL (Raíz `/CLAUDE.md`):** Ya maneja toda la mecánica del sistema: sincronización obligatoria con `Read`, reglas "Zero-Omission", triaje silencioso y regla de no bloqueo en wizard HITL (`REG-TRI-01`), protocolo universal de elección de plantilla (`REG-AST-01`), creación del documento base en disco (`REG-DOC-01`), búsqueda y resolución prioritaria de personas/partes mediante `search_clients` (`REG-CLI-01`), prohibición de repregunta (`REG-CLI-02`), consentimiento previo para guardar nuevos clientes con `save_client` (`REG-CLI-03`), volcado directo e inmediato de datos de partes a disco sin confirmación en chat sustituyendo exhaustivamente en título H1, comparecencia y firmas (`REG-CLI-04`), asignación y desambiguación universal de roles entre clientes conocidos mediante opciones nominales completas (`REG-CLI-05`), captura en bloque de datos estructurados y equivalencia chat/formulario (`REG-DAT-01`), cero insistencia ante negativa expresa (`REG-INS-01`), validación de sentido y coherencia fáctica/jurídica (`REG-VAL-01`), diálogo y asesoramiento en cláusulas negociables (`REG-NEG-01`), anuncio obligatorio de sección y avance sin permiso (`REG-SEC-01`), confirmación de cláusulas sustantivas en chat (`¿Confirmamos esta cláusula?`), bucle de realimentación final con menú de 5 opciones (`REG-FDB-01`), advertencias legales preceptivas de cierre (`REG-CLO-01`), sintaxis global de placeholders `{{DATO}}`, prohibición de corchetes para placeholders, emails/URLs como texto plano (sin `mailto:` ni auto-links), y reserva exclusiva de corchetes simples para identificadores de privacidad (ej. `[PERSON_1]`). *(Nota de arquitectura: Las reglas de "Zero-Omission" y resolución de placeholders aplican a skills sustantivas de tramitación documental para clientes. En plugins de gestión y diseño de plantillas como `gestion-plantillas`, los documentos del workspace son activos de plantilla y los marcadores `{{VARIABLE}}` constituyen el resultado deliberado y final, quedando exentos de ser rellenados con datos de clientes).* **No generes estas reglas en los CLAUDE.md de los nuevos plugins ni dupliques los algoritmos procedimentales en las skills: en su lugar, incluye en las skills únicamente directivas referenciales concisas a `CLAUDE.md`.**
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
  en negrita Markdown (la tarjeta de la skill SÍ renderiza Markdown, así que la negrita se ve
  como negrita), seguida de una frase breve que explique qué regula (ej. la **Ley 29/1994** de
  Arrendamientos Urbanos (LAU), que rige los alquileres de vivienda y de uso distinto). Esta
  description es la que se muestra en la tarjeta (card) de la skill.
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

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL — REG-TRI-01)

Tu primer objetivo es resolver los vectores de estado de clasificación **V1, V2, V3 y V4**.

### 1.1 Escucha Activa Previa
Antes de invocar formularios, evalúa el mensaje inicial y el historial de la conversación:
- Si el usuario **ya proporcionó de forma inequívoca** los datos para resolver los vectores de clasificación, regístralos en silencio y avanza directamente a la **Fase 2**.
- Si falta resolver alguno de los vectores de clasificación o existe ambigüedad, invoca de inmediato la herramienta `restricted_human_in_the_loop_request` para formular el árbol de decisión interactivo.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas necesarias para completar la resolución de los vectores pendientes:

> **ESTÁNDAR MANDATORIO DE COBERTURA UNIVERSAL DE ÁRBOLES LÓGICOS (WIZARD HITL):**
> El frontend de la aplicación presenta el bloque `form_data` de `restricted_human_in_the_loop_request` como un asistente (*wizard*) interactivo secuencial paso a paso (Pasos 1, 2, 3, etc.), donde cada pregunta requiere una selección obligatoria para avanzar.
> 1. **Preguntas Condicionales:** Cuando una pregunta dependa de una rama o respuesta anterior (ej. preguntas que comiencen por *"Si es..."*, *"En caso de..."*, o que solo apliquen si en un paso anterior se eligió cierta opción):
>    - **Enunciado explícito:** Debe reflejar con claridad la condición previa (ej. *"Si es un contrato nuevo, ¿qué se arrienda?"*, *"Si es una comunicación sobre un contrato vigente, ¿de qué tipo?"*, *"Si hay acuerdo, ¿qué alcance tiene el encargo?"*).
>    - **Opción de escape / negación obligatoria:** Debe incluir **OBLIGATORIAMENTE** al final de su lista `options` una opción de negación con `"id": "no_procede"` (o `"no_aplica"`), cuya etiqueta visible exprese inequívocamente la no aplicación de la premisa (ej. `{"id": "no_procede", "label": "No es un contrato nuevo"}`, `{"id": "no_procede", "label": "No es una comunicación sobre un contrato vigente"}`, `{"id": "no_procede", "label": "No procede: no hay acuerdo (vía contenciosa)"}`).
> 2. **Prohibición de Bloqueos Lógicos:** Queda **TERMINANTEMENTE PROHIBIDO** crear preguntas condicionales en `form_data` que asuman una respuesta afirmativa previa sin ofrecer una opción explícita de negación. Todo árbol lógico debe permitir que un usuario que haya elegido otra rama pueda transitar por los pasos restantes marcando la opción de no procedencia sin verse forzado a elegir una opción ficticia o errónea.

```json
{
  "form_data": [
    {
      "id": "vector_1_id",
      "rationale": "Resolver V1 para determinar el régimen y alcance aplicable.",
      "question": "¿Qué necesita tramitar?",
      "options": [
        {"id": "opcion_a", "label": "[Descripción clara de la opción A]"},
        {"id": "opcion_b", "label": "[Descripción clara de la opción B]"},
        {"id": "fuera_de_alcance", "label": "[Opción no cubierta por la skill]"}
      ]
    },
    {
      "id": "vector_2_id",
      "rationale": "Resolver V2 condicional a la opción A.",
      "question": "Si eligió la opción A, ¿cuál es el subtipo aplicable?",
      "options": [
        {"id": "subtipo_a1", "label": "[Subtipo A1]"},
        {"id": "subtipo_a2", "label": "[Subtipo A2]"},
        {"id": "no_procede", "label": "No procede: no corresponde a la opción A"}
      ]
    },
    {
      "id": "vector_3_id",
      "rationale": "Resolver V3 para fijar la estructura de partes y límites imperativos.",
      "question": "¿[Pregunta general sobre la naturaleza jurídica de la parte principal]?",
      "options": [
        {"id": "persona_fisica", "label": "Persona física (particular)"},
        {"id": "persona_juridica", "label": "Persona jurídica (empresa, entidad)"}
      ]
    }
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez fijados los vectores de clasificación, evalúa la rama de ejecución. Los vectores que hayan recibido `no_procede` quedan en estado inactivo/neutro y no interfieren con la rama sustantiva activada:
* **Si `[V1 = fuera_de_alcance]` $\rightarrow$ Detener proceso (Fuera de Alcance):**
  - Informa en el chat de que el caso se rige por normativas o supuestos distintos, quedando excluido del alcance de esta skill.
  - Ofrece derivar el caso al profesional o plugin competente. **No crees documento.**
* **Si `[V1 = opcion_a]` (Dentro de alcance):**
  - Régimen aplicable y directivas de dominio (evaluando `V2` entre sus subtipos activos).
  - Plantilla del sistema propuesta: `assets/template-[plantilla_a].md`.
  - Proceder a la **Fase 2**.
* **Si `[V1 = opcion_b]` (Dentro de alcance):**
  - Régimen aplicable y directivas de dominio (`V2 = no_procede` queda ignorado).
  - Plantilla del sistema propuesta: `assets/template-[plantilla_b].md`.
  - Proceder a la **Fase 2**.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas o sectoriales desde el bloque `<document kind="references-collection">` de tu system prompt.
2. Opcionalmente verifica fuentes oficiales en vivo mediante `web_search` si se requieren confirmar índices, tipos o reformas recientes en el BOE.

### 2.2 Mensaje de Plan de Acción y Formulario de Selección de Plantilla
Envía un mensaje estructurado y cordial en el chat, convocando en el mismo turno la herramienta HITL:
1. **Marco Legal / Técnico Aplicable:** Cita la normativa o estándares consolidados y explica con claridad el impacto de la clasificación obtenida (`V1-V4`).
2. **Propuesta de Plantilla Oficial del Sistema:** Menciona únicamente por su denominación formal que dispones de la plantilla oficial validada que ha resuelto el enrutamiento de la Fase 1.3. **Queda TERMINANTEMENTE PROHIBIDO mostrar rutas internas de archivo (ej. `assets/...`, `.md`) y TERMINANTEMENTE PROHIBIDO volcar o previsualizar el contenido íntegro de la plantilla oficial en el chat.**
3. **Formulario Interactivo Preceptivo (`restricted_human_in_the_loop_request`):** En ese mismo turno, convoca la herramienta con:
   - `id`: `"origen_plantilla"`
   - `rationale`: `"Determinar si se utilizará la plantilla base predeterminada del sistema o una minuta propia aportada por el usuario."`
   - `question`: `"¿Desea utilizar la plantilla base predeterminada del sistema o prefiere aportar su propia minuta?"`
   - `options`:
     - `{"id": "plantilla_sistema", "label": "Utilizar la plantilla base predeterminada del sistema"}`
     - `{"id": "plantilla_usuario", "label": "Aportar mi propia minuta (pegar en el chat o abrir en el editor)"}`
   *(Regla de Escucha Activa: Si el usuario ya pegó previamente su minuta en el chat o indicó expresamente su elección en el mensaje inicial, se asigna V5 en silencio sin convocar el formulario).*

### 2.3 Fijación de V5 (Origen Plantilla) y Manejo de la Elección
- **Si `[V5 = plantilla_sistema]` (Acepta la plantilla oficial):** Toma el contenido de la plantilla desde `<document kind="assets-collection">` y procede de inmediato a la **Fase 3** (`create_file` / `REG-DOC-01`).
- **Si `[V5 = plantilla_usuario]` (Aporta su propia minuta vía chat o editor):** Si aún no la ha aportado, solicita amablemente que pegue el texto en el chat o la abra en el editor; accede a la minuta desde `<user_message>`, realiza el control de legalidad verificando que no contenga cláusulas nulas de orden público ni contrarias a normas imperativas, advierte en el chat de posibles nulidades proponiendo la redacción válida, adopta la minuta revisada como base y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

Aplica rigurosamente la directiva `REG-DOC-01` y la sección 6.1 de `CLAUDE.md`:
1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada (`V5`) en el archivo del workspace con formato `[nombre_documento].md`.
   - Aplica el principio **Zero-Omission**: sustituye inmediatamente todos los datos ya conocidos de la escucha activa y la clasificación.
   - **Volcado Inmediato de Partes (REG-CLI-04):** Sustituye INMEDIATAMENTE en la creación del archivo (`create_file`) todos los datos identificativos de las partes que ya se conozcan (procedentes de fichas de clientes vinculadas en la conversación, de `search_clients`, o aportados en el chat). **Esta sustitución debe ser TOTAL en el documento completo: abarca el TÍTULO/ENCABEZADO H1 (`# ... — {{NOMBRE_1}} / {{NOMBRE_2}}`), la COMPARECENCIA/REUNIDOS y el bloque final de FIRMAS (`Nombre: {{NOMBRE_...}}`).**
   - Los campos pendientes permanecen explícitamente como marcadores `{{DATO_FALTANTE}}` en mayúsculas entre dobles llaves. PROHIBIDO dejar archivos en blanco, sólo con títulos o crear resúmenes.
2. **Validación de Integridad:** Se realiza prioritariamente mediante `# WORKSPACE ACTIVE DOCUMENTS`. No invocar `read_file` de forma rutinaria.
3. **Confirmación en Chat y Encadenamiento Inmediato:** Informa en el chat de la ruta absoluta del documento creado y los datos de partes incorporados, e introduce en esa misma respuesta la primera sección de la Fase 4 sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

### Protocolo de Ejecución de la Fase 4
Recorre de forma secuencial las secciones del documento respetando rigurosamente las directivas operativas globales de `CLAUDE.md`:
- **Partes e Intervinientes (REG-CLI-01 a 05):** Búsqueda prioritaria con `search_clients`, desambiguación con opción obligatoria `ninguna`, consentimiento de guardado con `save_client` (REG-CLI-03), volcado directo e inmediato al editor (`edit_file` / `create_file`) sin confirmación en chat (REG-CLI-04) y asignación nominal completa de roles entre clientes conocidos mediante formulario atómico de exactamente 1 pregunta (REG-CLI-05, prohibido mezclar con preguntas de objeto o inmueble).
- **Datos Estructurados Objetivos:** Solicitud en bloque mediante `slot_filling_request` (herramienta exclusiva para datos a rellenar; nunca mediante `restricted_human_in_the_loop_request`).
- **Equivalencia Chat / Formulario (REG-DAT-01):** Ingestión directa de información aportada por chat sin re-emitir formularios innecesarios; reenvío oportuno si el usuario canceló sin responder.
- **Cero Insistencia ante Negativa Expresa (REG-INS-01):** Respeto inmediato a campos omitidos por el usuario, rellenando con datos disponibles y conservando marcadores pendientes sin presionar ni insistir.
- **Validación de Sentido y Coherencia (REG-VAL-01):** Verificación de coherencia fáctica y jurídica en chat antes de volcar datos incongruentes.
- **Diálogo y Asesoramiento en Negociación (REG-NEG-01):** Explicación del régimen legal por defecto y consecuencias antes de redactar cláusulas dispositivas.
- **Cláusulas Sustantivas / Negociables:** Negociación en chat -> Vista previa en texto plano -> Pregunta literal de confirmación (`¿Confirmamos esta cláusula?` / `¿Confirmamos esta sección?`) -> Persistencia con `edit_file`.
- **Anuncio Obligatorio y Avance sin Permiso (REG-SEC-01):** Anuncio formal y visible de la sección entrante y avance inmediato sin pedir permiso para continuar.

> **REGLA DE AUTORÍA (DRY — Cero Duplicación de Procedimientos):**
> Las directivas operativas completas, la casuística exhaustiva de resolución de clientes y el manejo de canales residen de forma centralizada en el `CLAUDE.md` global (que el orquestador ubica al final del system prompt para garantizar máxima recencia y prevalencia sobre todo lo anterior).
> Las skills individuales **NO deben duplicar** los algoritmos procedimentales de `search_clients`, formularios de descarte o `REG-CLI-01..05` / `REG-DAT-01`. Su función es definir exclusivamente la **Hoja de Ruta de Secciones**: qué campos específicos solicitar en cada bloque, qué comprobaciones jurídicas debe realizar el asistente y qué cláusulas sustantivas requieren negociación.

### Hoja de Ruta de Secciones y Cláusulas Condicionales:

#### 1. [Nombre de la Sección 1 - Ej. Encabezamiento y Partes]
- **Búsqueda prioritaria, Cero Redundancia y Guardado de Nuevos Clientes (REG-CLI-01 a REG-CLI-05):** Localizar las fichas de las partes intervinientes ejecutando `search_clients` (llamadas paralelas si se mencionan varias partes). Si hay 1 coincidencia, usar sus datos directamente y no volver a pedir datos ni llamar a formulario si la ficha cubre la comparecencia; si hay varias, desambiguar con `restricted_human_in_the_loop_request` (incluyendo siempre la opción de negación `{"id": "ninguna", "label": "Ninguna de las personas identificadas (otra persona)"}`); si intervienen múltiples clientes conocidos, formular opciones nominales completas per REG-CLI-05; si es una persona nueva, preguntar inmediatamente al usuario mediante formulario (`restricted_human_in_the_loop_request`) si desea guardarla en la plataforma (`save_client`) antes de redactar cláusulas sustantivas, y reanudar el flujo tras su respuesta.
- **Condicional [Sujeto / Persona Jurídica]:**
  - *Si [Condición A - Persona Jurídica]:* Redactar e insertar: `Representado por: {{nombre_representante}}, con NIF {{nif_representante}}, en calidad de {{cargo_representante}} según escritura de poder.`
  - *Si [Condición B - Persona Física]:* Redactar e insertar comparecencia en su propio nombre y derecho.
- **Volcado directo a disco (REG-CLI-04):** Aplicar `edit_file` directamente en el editor (o en `create_file` si ya constaban los datos). Informar en el chat de los datos asentados y los campos pendientes (si los hubiera), pasando de inmediato a la siguiente sección sin solicitar confirmación previa en el chat.

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

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica las directivas globales `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones (1. Ajustar cláusula o sección existente, 2. Añadir estipulación adicional a medida, 3. Eliminar contenido opcional o corregir datos, 4. Revisar coherencia global y control de calidad, 5. Dar el documento por finalizado y cerrar la sesión).
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre:
   - **Carácter DRAFT:** Borrador profesional para revisión por profesional colegiado antes de firma o presentación.
   - **Obligaciones Fiscales y Plazos:** Plazos de liquidación de tributos (ej. 30 días hábiles para ITP/AJD o Plusvalía) cuando proceda.
   - **Elevación a Instrumento Público:** Preceptivo ante Notario para eficacia registral y fuerza ejecutiva.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Normas Imperativas y Cláusulas Nulas:** Especificar las estipulaciones que bajo ningún concepto pueden pactarse en perjuicio de las partes protegidas por ley. Si el usuario solicita una cláusula prohibida, rechazar la redacción, citar el precepto legal correspondiente y proponer la alternativa legal válida.
2. **Límites de Plazo y Garantías:** Detallar las restricciones fijadas por los vectores `V1`-`V4`.
3. **Fuero y Jurisdicción Imperativa:** Restricciones de sumisión judicial o administrativa.
4. **Cero Invención de Datos y Normas:** Todos los datos reales no aportados deben permanecer como `{{DATO_FALTANTE}}`. Queda estrictamente prohibido inventar números identificativos, referencias catastrales, jurisprudencia o artículos legales.
```
