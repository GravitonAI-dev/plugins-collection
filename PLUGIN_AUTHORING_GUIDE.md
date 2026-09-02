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

**PRINCIPIO OBLIGATORIO: Toda skill empieza con una introducción.** Ninguna skill puede lanzar su primera pregunta en frío. El primer turno de la conversación SIEMPRE incluye, en el mismo mensaje que la primera pregunta de clasificación, una introducción fija de una o dos frases (ver detalle y ejemplo en el Punto 1 de la plantilla). Si al auditar o actualizar una skill existente detectas que carece de esta introducción, añádela antes de dar la skill por conforme con esta guía.

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
- Preámbulos conversacionales antes de hacer preguntas. Si es tu turno de preguntar, emite únicamente la pregunta exacta — con la única excepción de la introducción fija del Punto 1, que solo se usa una vez, en el primer turno de toda la conversación.

## 0. CONFIRMACIÓN DE CARGA Y ARRANQUE (visible, una sola vez)

**Sección OBLIGATORIA en toda skill.** Al cargarse la skill, lo PRIMERO que el agente emite en el chat, antes de cualquier otro texto, es esta línea fija:

**Skill cargada satisfactoriamente.**

A continuación, en el MISMO mensaje y sin esperar ninguna confirmación del usuario, ARRANCA la ejecución del procedimiento: emite la introducción fija del Punto 1 y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa. Si el procedimiento arranca con una verificación normativa interna (Punto 2), se ejecuta en silencio y se continúa hasta la primera pregunta o hasta la Confirmación visible del Punto 3, según corresponda.

Está PROHIBIDO detenerse tras la línea de carga, preguntar si desea empezar, o emitir la línea a solas en un turno propio: la skill queda cargada y en ejecución en ese mismo turno. La línea se emite una única vez, al cargar, y no se repite en ningún turno posterior.

Esta línea es, junto con la introducción fija, la única excepción a la Directiva de Invisibilidad: al redactar esa directiva en una skill nueva, recógela expresamente como excepción para que no entren en contradicción.

## 1. CLASIFICACIÓN DINÁMICA (Vectores de Estado)

**Introducción (solo en el primer turno, una única vez):** antes de la primera pregunta de clasificación, y solo la primera vez, añade en el mismo mensaje una introducción fija de una o dos frases, con el tono y registro del dominio definidos en `[plugin]/CLAUDE.md` (ver "Tono y Estilo del Chat"), que enmarque qué se va a hacer sin mencionar mecánica interna (vectores, skills, fases). No se repite en turnos posteriores. **No afirmes en esta introducción una norma, artículo o alcance concreto que dependa de vectores aún no resueltos** — si la clasificación (Punto 1) es la que determina si el caso entra o no dentro de una norma dada (p. ej. un vector de "finalidad" que puede dejar el caso fuera de ámbito), la introducción debe quedarse en términos genéricos y dejar la norma aplicable para el Punto 3 (Confirmación), una vez resuelta la clasificación. Ejemplo genérico (dominio jurídico, tono de abogado): "Vamos a proceder a la elaboración de su [documento]. Para ajustarlo correctamente a su caso, es necesario precisar antes algunos datos."

Tu primer objetivo es resolver los siguientes vectores de manera SILENCIOSA usando Escucha Activa:
- **V1 ([Nombre del Vector]):** [Opciones posibles].
- **V2 ([Nombre del Vector]):** [Opciones posibles].

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o más vectores, TIENES PROHIBIDO inventar la redacción. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, en este orden estricto. Cada pregunta es un enunciado breve terminado en dos puntos, seguido de sus alternativas numeradas: nunca repitas el texto de las opciones dentro del enunciado (evita "¿es A o B? 1. A 2. B", que duplica la información). El usuario del árbol de decisión responde con el número o la palabra, nunca con texto libre sin opciones:
* Para V1:
  "[Enunciado breve sobre qué se decide con V1]:
  1. [Opción A]
  2. [Opción B]"
* Para V2:
  "[Enunciado breve sobre qué se decide con V2]:
  1. [Opción A]
  2. [Opción B]"

**PRINCIPIO: Preguntas simples, no mega-preguntas.**
Cada pregunta debe resolver un único punto de decisión del árbol, con 2-3 opciones simples y excluyentes, y avanzar visiblemente hacia qué asset/plantilla se va a cargar. Nunca comprimas varias categorías en una sola pregunta larga: obliga al usuario a procesar varias decisiones a la vez y dificulta enrutar la respuesta a un vector concreto. Si un vector tiene más de 2-3 categorías posibles, divídelo en una pregunta principal binaria más una sub-pregunta de desambiguación que solo se formula si la respuesta a la principal es ambigua.

INCORRECTO (mega-pregunta, tres categorías comprimidas en una frase):
"¿El uso previsto es permanente en el tiempo, o es de temporada (vacacional, de verano, por trabajo temporal) o se trata de una vivienda turística gestionada como alojamiento?"

INCORRECTO (duplica el texto de las opciones entre el enunciado y la lista):
"¿El uso será permanente o temporal?
1. Permanente
2. Temporal"

CORRECTO (enunciado breve sin repetir las opciones + alternativas numeradas + sub-pregunta condicional, solo si hace falta):
"El uso será:
1. Permanente, sin plazo predeterminado
2. Temporal (de temporada o alojamiento turístico)"
→ Solo si la respuesta es "temporal" y no queda claro cuál de las dos: "El uso temporal es:
1. De temporada
2. Alojamiento turístico"

**Alcance de las alternativas numeradas: solo clasificación, no relleno de datos.** Las alternativas numeradas son exclusivas de las preguntas de clasificación del Punto 1 (las que enrutan a un asset/plantilla). Las preguntas de relleno de datos del documento (nombres, direcciones, importes, fechas) se formulan en prosa natural y el usuario responde con texto libre — nunca las conviertas en lista numerada. Si dentro de una pregunta de relleno aparece un dato puntual con un numero pequeño y cerrado de respuestas (ej. "¿es zona de mercado tensionado? sí/no/no lo sé"), ofrece esas opciones en la misma frase sin forzar el resto de datos de texto libre a un formato de lista.

El orden también importa: pregunta primero por los vectores más concretos y fáciles de responder (p. ej. tipo de inmueble), y deja para después los más abstractos o los que solo sirven de filtro de alcance (p. ej. finalidad del uso), salvo que preguntarlos antes ahorre trabajo al usuario cuando la respuesta probable sea "fuera de alcance".

### Enrutamiento de Estado (Routing)
Una vez resueltos todos los vectores, evalúa:
- Si [V1 = X] -> Plantilla a usar: `assets/asset_x.md`.
- Si [V2 = Y] -> Detener proceso (fuera de alcance). No crees documento.

## 2. VERIFICACIÓN Y AUTO-ACTUALIZACIÓN DE LA FUENTE (Interno)
*(OBLIGATORIA y BLOQUEANTE en toda skill que se apoye en una norma, estándar o fuente externa versionada — en el dominio jurídico, siempre. Solo es omisible en skills que no dependan de ninguna fuente externa).*

**Principio: la skill se actualiza a sí misma en cada lanzamiento.** Nunca se redacta con la versión que la skill trae escrita: se comprueba primero si existe una posterior y, si la hay, la skill reescribe sus propios archivos antes de redactar.

1. **Leer la versión registrada localmente** en `references/fuentes-plantillas-validadas.md`.
2. **Consultar la fuente oficial vigente** (en derecho español, el texto consolidado del BOE de cada norma que use la skill, más el modelo normalizado del CGPJ si existe para ese documento). Registrar la URL exacta en la reference, nunca de memoria.
3. **Comparar** la versión oficial con la registrada y con el texto de las references.
4. **Auto-actualizar (obligatorio si hay cambios):** reescribir con `Write`/`Edit` las references y los assets afectados con la redacción vigente, actualizar la tabla "Versión registrada" y las fechas, e informar brevemente al usuario de la norma y fecha detectadas. No redactar hasta completarlo.
5. **Fallback si la fuente no es accesible:** intentar `WebSearch`; si tampoco, usar la reference local, advertir expresamente al usuario ("no se pudo verificar la versión vigente; verifique manualmente antes de presentar") y marcar el dato como pendiente en la reference. **Prohibido dar por vigente lo que no se ha podido verificar.**

**Datos que cambian solos:** si la skill depende de una magnitud que se actualiza periódicamente (índices de actualización de renta, SMI y tramos de embargo, intereses legales, umbrales de cuantía), la skill la verifica en cada lanzamiento en su fuente oficial en lugar de dejarla escrita fija en el asset.

## 3. CONFIRMACIÓN (visible al usuario)
*(Sección OBLIGATORIA siempre que la skill verifique una fuente normativa, legal o técnica externa en el Punto 2 — no es opcional en esos casos. A diferencia de los Puntos 1 y 2, esta sección SÍ es visible para el usuario.)*

Tras completar la verificación de contexto (Punto 2), en un único mensaje:
1. **Informa la fuente aplicable.** Indica qué norma/artículo/versión concreta aplica al caso ya clasificado (Punto 1), con el dato verificado en el Punto 2. Incluye SIEMPRE el enlace a la fuente oficial (la misma URL consultada en el Punto 2) para que el usuario pueda comprobarlo por su cuenta.
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje, informa de que existe una plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores, basada en esa fuente, y pregunta cuál usar como base (alternativas numeradas, es una decisión que cambia el flujo):
   "¿Qué [documento] desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio [documento]"
3. **Enruta según la respuesta:** si elige la plantilla, continúa con el Punto 4 usando el asset correspondiente; si elige adjuntar el suyo, pide que lo adjunte, léelo con `Read` y úsalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio (adviértele si el documento adjuntado los incumple).

## 4. CREACIÓN DEL DOCUMENTO BASE (Cero Vacíos)
Inmediatamente tras el paso anterior (Confirmación, Punto 3, o Verificación de Contexto si el Punto 3 no aplica), estás OBLIGADO a crear el documento:
1. Utiliza `Read` para leer el documento base decidido (la plantilla, o el que adjuntó el usuario en el Punto 3).
2. Reemplaza en memoria TODOS los datos que ya poseas (gracias a los vectores, escucha activa e investigación). Los faltantes quedan como `{{DATO_FALTANTE}}`.
3. Utiliza `Write` para guardar el archivo en disco.
4. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. Inmediatamente después, en la misma respuesta, pregunta si quiere empezar a rellenar los datos del documento. Solo tras la confirmación, formula la primera pregunta de la edición incremental (Punto 5) para no detener la conversación.

## 5. EDICIÓN INCREMENTAL DE CLÁUSULAS / SECCIONES

**Anuncio de sección (visible, sin esperar confirmación aparte):** al terminar una sección de la lista (aplicado su `Edit`, o tras la confirmación agrupada si es un bloque identificativo de parte), no lances en frío la pregunta de la siguiente sección. En el mismo mensaje, antes de esa pregunta, añade una frase breve — en el registro y tono del dominio definidos en `[plugin]/CLAUDE.md` — que anuncie qué sección del documento se abre ahora (ej. "Pasamos ahora a determinar el objeto del contrato."), y a continuación formula ya la primera pregunta de esa sección. El anuncio y la pregunta van en el mismo turno: no pidas permiso para pasar de sección, solo informa y continúa. Esto es un anuncio de la sección SUSTANTIVA del documento (identificable por el cliente: "objeto", "duración", "renta"...), no de la mecánica interna de la skill — sigue estrictamente prohibido nombrar vectores, puntos numerados o fases de la instrucción (Directiva de Invisibilidad). Al redactar la lista de secciones de una skill nueva, define el texto fijo del anuncio de cada sección junto a su descripción, igual que se hace con las preguntas de clasificación del Punto 1.

Recorre secuencialmente la siguiente lista. Por cada sección incompleta, aplica el Ciclo de Edición Incremental Global (Formular Pregunta -> Mostrar Vista Previa en texto plano -> Pedir Confirmación -> Usar `Edit` en disco). **Un dato por turno, salvo bloque identificativo de una misma parte:** si un punto de la lista agrupa más de un dato, pídalos en turnos separados, nunca juntos en el mismo mensaje — divide ese punto en sub-apartados (a, b, c...), uno por turno. Cuando un dato de un sub-apartado dependa de un vector de clasificación ya resuelto (ej. pedir DNI si es persona física pero NIF/CIF si es jurídica), usa el valor del Punto 1 sin volver a preguntarlo. **Excepción — confirmación agrupada por parte:** cuando el sub-apartado son datos puramente identificativos o de contacto de una misma parte/firmante (nombre o razón social, documento de identidad, domicilio, teléfono, email...), sigue preguntando un dato por turno, pero NO ejecutes el Ciclo de Edición Incremental completo (vista previa + confirmación + `Edit`) tras cada uno: acumúlalos en memoria sin escribir aún en el documento. Solo tras RECIBIR la respuesta al último dato de esa parte —nunca en el mismo turno en que todavía se está preguntando ese último dato— muestra, ya en el turno siguiente, una única vista previa con TODOS sus datos juntos y pide una única confirmación conjunta antes de aplicar el `Edit` que los vuelca todos a la vez. Esta excepción es exclusiva de datos identificativos objetivos; no aplica a cláusulas de negociación entre partes (duración, renta, garantías, reparto de gastos...), que siguen confirmándose una por una. **Validación de sentido, no solo de formato:** el agente operacional es un LLM, no un formulario — no debe aceptar mecánicamente cualquier texto como si fuera automáticamente un dato válido. Antes de dar por buena una respuesta, debe razonar si tiene sentido en el contexto de lo preguntado. Si es absurda, imposible o no responde a lo preguntado, no debe escribirla en el documento: debe dialogar con el cliente, señalar por qué no encaja y pedir aclaración antes de continuar. **Diálogo y acuerdo en las cláusulas de negociación entre partes:** no todas las cláusulas son datos objetivos (nombre, dirección, identificador) — algunas implican una decisión o un pacto entre las partes con consecuencias legales o contractuales (plazos, importes, reparto de obligaciones, garantías, pactos opcionales). En esas cláusulas no te limites a registrar el valor que dé el cliente: explica brevemente el régimen por defecto o la implicación relevante, y confirma que el cliente entiende y está de acuerdo antes de escribirlo en el documento. Al identificar las secciones de una skill nueva, marca cuáles son de este tipo (frente a las de puro dato objetivo) para que la instrucción de cada una lo refleje.
1. **[Sección 1]:** [Qué datos faltan, instrucciones específicas].
2. **[Sección 2]:** [Qué datos faltan, instrucciones específicas].

## BUCLE DE REALIMENTACIÓN FINAL
Tras completar el Punto 5, muestra el siguiente menú y espera instrucciones (aplicando `Edit` según corresponda):
1. Ajustar una sección existente.
2. Añadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.
```

## 4. CONVENCIONES DE PLANTILLAS (`assets/*.md`) — Markdown render-safe

Los documentos generados se abren en el editor de la GUI, que los renderiza como texto enriquecido. El markdown de las plantillas debe sobrevivir a ese render. Reglas obligatorias al escribir o auditar un asset:

1. **Placeholders desnudos, nunca en comentarios, nunca con texto de ayuda ni anidados.** Un placeholder se escribe `{{dato}}` a pelo. PROHIBIDO envolverlo en comentarios HTML (`<!-- {{dato}} -->`): un renderizador sin soporte de HTML crudo lo muestra como basura literal, y uno con soporte lo oculta por completo (el cliente ni ve que falta el dato). PROHIBIDO tambien meter texto de ayuda o una lista de opciones dentro de las llaves (`{{naturaleza: persona fisica / persona juridica}}`) o anidar un placeholder dentro de otro (`{{formula: activo {{total_activo}} - pasivo {{total_pasivo}}}}`): si no se resuelve antes del `Write` final, el cliente ve ese texto de ayuda o la sintaxis rota como si fuera contenido real del documento. La guia de que opcion elegir o el valor por defecto legal va en el `SKILL.md` (la seccion `[negociacion]` que recoge ese dato), nunca dentro del placeholder del asset. Un dato faltante conserva el nombre propio de su placeholder (`{{fecha_firmeza}}`); un marcador generico como `{{DATO_FALTANTE}}` solo vale para un hueco suelto sin placeholder propio y nunca debe repetirse dos veces en el mismo documento, porque el `Edit` posterior necesita un `oldString` unico para localizar cada dato por separado.
2. **Comentarios HTML solo como instrucción interna.** `<!-- Si X: ... -->` se admite en la plantilla únicamente como bloque condicional o nota de redacción dirigida al agente. El documento escrito en disco lleva CERO comentarios HTML: se resuelven en el Write inicial y en la edición incremental (regla global de Comment resolution en el `CLAUDE.md` raíz, sección 6.1).
3. **Saltos de línea duros en bloques de datos.** Markdown estándar colapsa los saltos simples en un solo párrafo. Toda línea de un bloque de líneas consecutivas (datos de las partes, dirección del inmueble, expositivos I/II/III, líneas de una cita `>`) debe terminar en **dos espacios** para forzar el salto duro. Los párrafos de prosa corrida van en una sola línea de texto, separados por línea en blanco.
4. **Sin HTML crudo de ningún otro tipo.** Nada de `<br>`, `<div>`, `<span>` ni entidades: solo markdown puro (encabezados, negrita, citas, tablas, separadores `---`).

Al auditar una skill existente, verificar sus assets contra estas cuatro reglas igual que se verifica el flujo del `SKILL.md`.
