---
name: medidas-apoyo-discapacidad
title: Medidas de apoyo a personas con discapacidad
i18n:
  en:
    name: disability-support-measures
    title: Disability support measures
    description: >
      Generates the right document to provide support to an adult with a disability under the
      system of **Law 8/2021**, which replaced judicial incapacitation with a system of support
      for persons with disabilities, verified in the BOE: draft deed of voluntary support
      measures and preventive power of attorney, including self-curatorship (Arts. 255 to 262
      and 271 to 274 CC); application for judicial authorisation to the de facto guardian for a
      specific act requiring representation (Art. 264 CC, through the voluntary jurisdiction
      procedure of Arts. 61 to 63 LJV); and application for judicial provision of support
      measures with appointment of a curator (Art. 269 CC, through the procedure of Art. 42 bis
      a) LJV or the contested proceedings of Arts. 756 to 761 LEC). Curatorship is SUBSIDIARY:
      the skill applies the Art. 269 filter before routing to it. Do not use for minors, for
      involuntary commitment (Art. 763 LEC), for incapacitation or modification of capacity
      (abolished in 2021), or for setting up a protected estate under Law 41/2003.
description: >
  Genera el documento adecuado para proveer de apoyo a una persona mayor de edad con discapacidad
  conforme al sistema de la **Ley 8/2021**, que sustituyo la incapacitación judicial por un sistema de apoyos a la persona con discapacidad, verificado en el BOE: minuta de escritura de medidas de apoyo
  voluntarias y poder preventivo, incluida la autocuratela (Arts. 255 a 262 y 271 a 274 CC); solicitud
  de autorización judicial al guardador de hecho para un acto concreto que exige actuación
  representativa (Art. 264 CC, por el expediente de jurisdicción voluntaria de los Arts. 61 a 63 LJV);
  y solicitud de provisión judicial de medidas de apoyo con constitución de curatela (Art. 269 CC, por
  el expediente del Art. 42 bis a) LJV, o por el proceso contencioso de los Arts. 756 a 761 LEC si el
  expediente terminó por oposición). La curatela es SUBSIDIARIA: la skill aplica el filtro del Art. 269
  antes de enrutar a ella. NO usar para menores de edad, para el internamiento no voluntario (Art. 763
  LEC), para la incapacitación ni la modificación de la capacidad (instituciones suprimidas en 2021),
  ni para constituir un patrimonio protegido de la Ley 41/2003.
when_to_use: |
  - Una persona quiere dejar previsto ahora quién le apoyara si en el futuro lo necesita: poder
    preventivo, autocuratela u otras medidas voluntarias.
  - Alguien viene ocupándose de hecho de un familiar y necesita realizar un acto concreto en su nombre
    (vender un inmueble, aceptar o repudiar una herencia, disponer de un depósito, interponer una
    demanda) que exige actuación representativa.
  - Una persona precisa apoyo de modo continuado, no hay nadie ocupándose de ella ni medida voluntaria
    alguna, y procede pedir judicialmente la constitución de una curatela.
  - El usuario pide "incapacitar" o "modificar la capacidad" de un familiar: la skill corrige la
    terminología, aplica el filtro de subsidiariedad y encamina el caso a la medida que corresponda.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - finalidad: previsión voluntaria / autorización al guardador de hecho / curatela
  - existe_guarda_hecho: sí / no, y si constituye apoyo suficiente
  - existe_medida_voluntaria: sí / no, y su alcance
  - tipo_curatela: asistencial / representativa para actos concretos
  - expresion_voluntad: la persona puede expresar su voluntad, deseos y preferencias / no puede pese a un esfuerzo considerable
  - via_procesal: expediente de jurisdicción voluntaria / proceso contencioso tras oposición
  - datos_persona_apoyada: nombre, DNI/NIE, fecha de nacimiento, residencia, situación personal y patrimonial
  - datos_promotor_o_guardador: nombre, DNI/NIE, domicilio, relación con la persona, desde cuando presta el apoyo
  - necesidades_apoyo: ámbitos concretos y observables en que se precisa apoyo, y si es continuado u ocasional
  - acto_concreto: descripción, bien o derecho identificado, motivo, necesidad, destino de la suma y valor económico
  - curador_propuesto: persona propuesta, razones de idoneidad, sustitutos, causas de exclusión
  - dictamen_pericial: autor, fecha y contenido del dictamen social y sanitario
  - interesados: cónyuge o pareja, descendientes, ascendientes y hermanos que deben ser citados
outputs:
  - minuta_poder_preventivo: minuta de escritura de medidas de apoyo voluntarias y poder preventivo en markdown, DRAFT
  - solicitud_autorizacion_guarda_hecho: solicitud de autorización judicial al guardador de hecho en markdown, DRAFT
  - demanda_curatela: solicitud de provisión judicial de medidas de apoyo con constitución de curatela en markdown, DRAFT
references:
  - references/curatela-designacion-actos-y-control.md
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/sistema-apoyos-ley-8-2021.md
assets:
  - assets/template-demanda-curatela.md
  - assets/template-minuta-poder-preventivo.md
  - assets/template-solicitud-autorizacion-guarda-hecho.md
---

# Provisión de Medidas de Apoyo a Personas con Discapacidad

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

Para garantizar un enrutamiento determinista y el cumplimiento normativo riguroso, el asistente resuelve y mantiene internamente en memoria los vectores de estado de la operación —cuyo catálogo y su correspondencia con las respuestas del formulario figuran en la Fase 1.2— y el origen de la plantilla (`origen_plantilla`).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas (por ejemplo, anotar un vector como resuelto) son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es clasificar con precisión la naturaleza del caso y fijar los vectores deterministas de estado.

### 1.1 Escucha Activa Previa
Antes de abrir formularios interactivos o hacer preguntas, analiza el mensaje inicial del usuario y la documentación aportada:
- Si el mensaje ya especifica inequívocamente los vectores de la operación, asígnalos de forma inmediata y silenciosa en memoria y pasa a la **Fase 2**.
- Si restan vectores por definir, no formules preguntas abiertas en turnos sucesivos: presenta el formulario estructurado interactivo mediante la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las opciones de triaje:

```json
{
  "form_data": [
    {
      "id": "finalidad",
      "rationale": "Resolver V1: la curatela es subsidiaria de las medidas voluntarias y de la guarda de hecho, y cada finalidad tiene su propio asset.",
      "question": "¿Qué medida de apoyo se pretende?",
      "options": [
        {"id": "prevision_voluntaria", "label": "Una previsión voluntaria de la propia persona: poder preventivo o autocuratela"},
        {"id": "autorizacion_guarda", "label": "Una autorización judicial puntual a quien ya ejerce la guarda de hecho"},
        {"id": "curatela", "label": "La constitución judicial de una curatela"}
      ]
    },
    {
      "id": "expresion_voluntad",
      "rationale": "Resolver V4: determina si cabe la curatela representativa y si la persona puede otorgar por sí misma medidas voluntarias.",
      "question": "¿Puede la persona expresar su voluntad, deseos y preferencias?",
      "options": [
        {"id": "puede_expresar", "label": "Sí, con los apoyos adecuados puede expresarlos"},
        {"id": "no_puede_expresar", "label": "No, pese a haberse hecho un esfuerzo considerable"}
      ]
    },
    {
      "id": "tipo_curatela",
      "rationale": "Resolver V3: activa o desactiva los bloques de facultades representativas, que deben justificarse acto por acto.",
      "question": "Si se solicita curatela, ¿de qué tipo?",
      "show_if": {"question_id": "finalidad", "option_ids": ["curatela"]},
      "options": [
        {"id": "asistencial", "label": "Asistencial: el curador acompaña y asiste en la toma de decisiones"},
        {"id": "representativa", "label": "Representativa para actos concretos, que deberán enumerarse y justificarse"},
        {"id": "no_procede", "label": "No procede: no se solicita curatela (es previsión voluntaria o guarda de hecho)"}
      ]
    },
    {
      "id": "existe_guarda_hecho",
      "rationale": "Resolver V5: si la guarda de hecho funciona adecuadamente, la curatela no procede por su carácter subsidiario.",
      "question": "¿Existe ya una guarda de hecho que preste apoyo suficiente?",
      "options": [
        {"id": "si_suficiente", "label": "Sí, y funciona adecuadamente"},
        {"id": "si_insuficiente", "label": "Sí, pero resulta insuficiente"},
        {"id": "no", "label": "No existe"}
      ]
    },
    {
      "id": "existe_medida_voluntaria",
      "rationale": "Resolver V2.b: la existencia de un poder preventivo o de una autocuratela otorgados con anterioridad hace subsidiaria la curatela.",
      "question": "¿Otorgó la persona con anterioridad un poder preventivo o una autocuratela?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"},
        {"id": "no_lo_se", "label": "No lo sé"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — respuesta a `finalidad`
- `V2.b` — respuesta a `existe_medida_voluntaria`
- `V3` — respuesta a `tipo_curatela`
- `V4` — respuesta a `expresion_voluntad`
- `V5` — respuesta a `existe_guarda_hecho`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalúa en este orden:

- Si V1 = prevision_voluntaria → **HOJA VOLUNTARIA**: `assets/template-minuta-poder-preventivo.md`.
- Si V1 = autorizacion_guarda → **HOJA GUARDA**: `assets/template-solicitud-autorizacion-guarda-hecho.md`, previa la validación de "acto concreto" descrita más abajo.
- Si V1 = curatela → **aplicar primero el FILTRO DE SUBSIDIARIEDAD** (sección siguiente). Solo si lo supera:
  - V3 = asistencial → **HOJA CURATELA**, `assets/template-demanda-curatela.md`, con los bloques de facultades representativas DESACTIVADOS.
  - V3 = representativa → **HOJA CURATELA**: `assets/template-demanda-curatela.md`, el mismo asset, con los bloques de facultades representativas ACTIVADOS y justificados acto por acto.
  - V3 = no_procede → **DETENER** la elección de hoja: la respuesta es incoherente, porque se pide curatela pero se indica que no se solicita. Aclarar en el chat (REG-VAL-01) si la curatela es asistencial o representativa, o si lo que se busca es una previsión voluntaria o una autorización de guarda, y volver a resolver V3 o V1. No crear documento hasta resolverlo.
- **Sub-pregunta de vía procesal (solo en la HOJA CURATELA, antes de la Fase 3).** El expediente de jurisdicción voluntaria es la vía ordinaria; el proceso contencioso solo procede si un expediente previo terminó por oposición o no pudo resolverse (Art. 756.1 LEC). Formula:
  "Sobre actuaciones judiciales anteriores por este mismo asunto:
  1. No se ha iniciado ninguna
  2. Se inicio un expediente que terminó porque alguien se opuso, o que no pudo resolverse"
  Respuesta 1 → variante de jurisdicción voluntaria del asset. Respuesta 2 → activar el bloque condicional de la variante contenciosa (Arts. 756 a 761 LEC) y ajustar los fundamentos de trámite y prueba (Art. 759 LEC en lugar del Art. 42 bis b) LJV).
- Si en cualquier momento consta que la persona es **menor de edad** → **DETENER**: fuera de alcance (patria potestad o tutela de menores). Advertir y escalar. No crear documento. Única excepción informativa: si es mayor de dieciséis años y se prevé que precisara apoyo al alcanzar la mayoría de edad, informar del Art. 254 CC y de que **el propio menor puede hacer sus propias previsiones**, y escalar.
- Si lo que se pretende es un **internamiento no voluntario** (Art. 763 LEC) → **DETENER SIEMPRE**: fuera de alcance, con independencia de lo urgente que parezca. Advertir y escalar de inmediato.
- Si lo que se pretende es una **incapacitación** o una **modificación de la capacidad** → no es un supuesto de "fuera de alcance" sino de institución inexistente: aplicar la corrección terminológica de la Fase 1 y reconducir el caso por V1, sin detener el flujo.
- Si lo que se pretende es constituir o administrar un **patrimonio protegido** de la Ley 41/2003 → **DETENER**: fuera de alcance. Advertir y escalar.
- Si la persona tiene **vecindad civil foral** (Cataluña, Aragon, Navarra, Galicia, Baleares) → **DETENER**: esta skill se apoya en el Código Civil estatal y no ha verificado la normativa autonómica. Advertir y escalar.

### FILTRO DE SUBSIDIARIEDAD (interno, BLOQUEANTE, solo si V1 = curatela)

Es el núcleo de esta skill. El Art. 269 del Código Civil solo permite constituir la curatela **cuando no exista otra medida de apoyo suficiente**, y el Art. 255 in fine añade que la autoridad judicial solo puede adoptar medidas supletorias "en defecto o por insuficiencia de las voluntarias, y a falta de guarda de hecho que suponga apoyo suficiente". Ver `references/sistema-apoyos-ley-8-2021.md`, apartado 6.

**Regla: si V5 = si_suficiente, o V2.b = si o no_lo_se, NO enrutes a la HOJA CURATELA todavía.** En su lugar, emite en un único mensaje, en el registro formal del plugin:

1. **La explicación del régimen.** Que la ley considera la guarda de hecho una medida de apoyo con el mismo rango que las demás (Art. 250 CC), que quien viene ejerciéndola adecuadamente continúa en su función (Art. 263 CC), y que la curatela solo se constituye cuando no existe otra medida de apoyo suficiente (Art. 269 CC). Si V2.b = si, añadir que el poder otorgado en su día puede seguir siendo operativo y que conviene leerlo antes de descartarlo (Arts. 256 a 259 CC).
2. **La alternativa concreta.** Que si el problema es un acto puntual que exige actuar en nombre de la persona, la vía es la autorización judicial del Art. 264 del Código Civil, más breve, más barata y sin necesidad de abogado ni procurador si el valor del acto no supera los 6.000 euros (Art. 62.3 LJV).
3. **La pregunta de salida**, con alternativas numeradas:
   "A la vista de lo anterior:
   1. Hay un acto concreto que necesita hacerse en su nombre y para el que basta esa autorización
   2. El apoyo actual no basta: hay ámbitos en los que se necesita un apoyo estable"

- Respuesta 1 → **HOJA GUARDA**. Continúa por esa rama.
- Respuesta 2 → el filtro queda superado por confirmación expresa del cliente. **Antes de seguir, pide la razón concreta por la que el apoyo actual no basta** (pregunta en prosa) y regístrala: es el contenido del hecho de subsidiariedad del escrito, y sin el la solicitud es rechazable. Después continúa con V3.

**Si V5 = no y V2.b = no**, el filtro queda superado sin necesidad de esta pregunta. Continúa con V3. **Si V5 = si_insuficiente**, el filtro queda superado por manifestación expresa del cliente, pero antes de seguir pide igualmente la razón concreta por la que el apoyo actual no basta y regístrala: es el contenido del hecho de la demanda que acredita la insuficiencia.

**Aplica además, en ambos casos, el filtro de la necesidad ocasional:** si de lo relatado resulta que el apoyo se necesita solo de vez en cuando, aunque sea de forma recurrente, la medida proporcionada es el **defensor judicial** (Arts. 250 y 295.5.º CC), no la curatela. Adviértelo, explica la diferencia y ofrece escalación: esta skill no genera la solicitud de defensor judicial.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **HOJA VOLUNTARIA (Arts. 255 y 260 CC):** las medidas voluntarias exigen que el otorgante **comprenda el alcance del acto en el momento de la firma**, y ese juicio corresponde al Notario. Si de lo relatado resulta que la persona ya no está en condiciones de otorgar, **adviértelo con claridad y reconduce**: la vía ya no es la voluntaria, sino la guarda de hecho o la curatela. No prepares una minuta que el notario no vaya a poder autorizar.
- **HOJA VOLUNTARIA (Art. 259 CC):** si el poder va a comprender todos los negocios del otorgante, adviértelo antes de redactarlo: el apoderado quedará sujeto a las reglas de la curatela en todo lo no previsto, incluidas las autorizaciones judiciales del Art. 287. Ofrece acotar las facultades.
- **HOJA GUARDA (Art. 264 CC) — validación de "acto concreto", BLOQUEANTE:** confirma que existe un acto determinado que exige actuación representativa. Si el cliente solo quiere "dejar constancia" de que se ocupa de la persona, **DETENTE y no crees documento**: explica que la guarda de hecho no se constituye, no se nombra y no se inscribe, que ya es la medida de apoyo aplicable, y que no hay nada que formalizar. Si además la persona conserva capacidad para otorgar, ofrece la HOJA VOLUNTARIA como vía para dar cobertura estable al apoyo.
- **HOJA GUARDA (Art. 264, párrafo 3, CC) — actos que NO requieren autorización:** si el acto consiste en solicitar una prestación económica a favor de la persona que no supone un cambio significativo en su forma de vida, o en un acto sobre bienes de escasa relevancia económica y sin especial significado personal o familiar, **informa de que no hace falta autorización judicial** y no crees el expediente. Solo continúa si el cliente confirma que el acto excede de esos límites.
- **HOJA GUARDA (Art. 287 CC):** si el acto es uno de los enumerados en el Art. 287, la autorización es preceptiva **en todo caso**. Identifica el ordinal concreto y regístralo: se cita en el escrito.
- **HOJA GUARDA (Art. 62.3 LJV):** determina el valor económico del acto. Si no supera los 6.000 euros, no son preceptivos abogado ni procurador; si lo supera, la solicitud inicial puede presentarse igualmente sin ellos, pero el Tribunal puede ordenar después la actuación por medio de abogado. Informa de ambas cosas; no afirmes que son preceptivos desde el inicio.
- **HOJA CURATELA (Art. 42 bis b).1 LJV) — dictamen pericial, BLOQUEANTE:** la solicitud debe acompañarse de **un dictamen pericial de profesionales especializados de los ámbitos social y sanitario** que aconseje las medidas idóneas. Pregunta si se dispone de él. Si no se dispone, **no impidas redactar el borrador**, pero advierte expresamente de que el escrito no puede presentarse sin ese dictamen y deja su referencia como placeholder pendiente. Nunca des por cumplido este requisito con un informe médico genérico que no aconseje medidas.
- **HOJA CURATELA (Art. 269, párrafos 2 y 4, CC) — individualización:** no se admite una petición genérica de curatela. Si el cliente no sabe concretar en que ámbitos se necesita apoyo, **no redactes una fórmula amplia**: dialoga hasta obtener ámbitos concretos y observables, orientándote por los del dictamen pericial.
- **HOJA CURATELA (Art. 269, párrafo final, CC):** está prohibido pedir la privación de derechos. Si el cliente pide que la persona "no pueda votar", "no pueda casarse", "no pueda disponer de nada", rechaza la instrucción, explica la prohibición legal y reconduce hacia la determinación de los actos en que se precisa asistencia.
- **HOJA CURATELA (Art. 275 y Art. 250 in fine CC) — idoneidad del curador:** verifica que la persona propuesta no incurre en causa de inhabilidad, no tiene conflicto de intereses con la persona apoyada y no le presta servicios asistenciales o residenciales en virtud de contrato. Si concurre alguna, adviértelo y pide otra propuesta.
- **TODAS LAS HOJAS — sospecha de abuso o de aprovechamiento patrimonial:** si de lo relatado resulta que el apoyo se busca para acceder al patrimonio de la persona, o hay indicios de presión, aislamiento o disposiciones patrimoniales recientes a favor de quien pide el apoyo, **DETENTE de inmediato**, no crees documento y escala. Ver la matriz de Escalación.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Ley 8/2021, de 2 de junio, por la que se reforma la legislación civil y procesal para el apoyo a las personas con discapacidad; Arts. 249 a 294 del Código Civil; y Ley 15/2015 de la Jurisdicción Voluntaria.
2. **Orientación Legal del Caso:**

**Informa la vía y la fuente aplicable.** Textos fijos por hoja:
   - VOLUNTARIA: "A su caso corresponden unas medidas de apoyo de naturaleza voluntaria, que se otorgan en escritura pública conforme a los artículos 255 y siguientes del Código Civil, en la redacción de la Ley 8/2021. El poder preventivo se regula en sus artículos 256 a 262 y la autocuratela en el 271. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - GUARDA: "A su caso corresponde una solicitud de autorización judicial al guardador de hecho, conforme al artículo 264 del Código Civil, que se tramita por el expediente de jurisdicción voluntaria de los artículos 61 a 63 de la Ley 15/2015, de Jurisdicción Voluntaria. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2015-7391"
   - CURATELA (vía de jurisdicción voluntaria): "A su caso corresponde una solicitud de provisión judicial de medidas de apoyo, conforme al artículo 269 del Código Civil, que se tramita por el expediente de jurisdicción voluntaria del artículo 42 bis a) de la Ley 15/2015, de Jurisdicción Voluntaria. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2015-7391"
   - CURATELA (vía contenciosa): "A su caso corresponde una demanda de adopción de medidas judiciales de apoyo, conforme al artículo 269 del Código Civil y a los artículos 756 y siguientes de la Ley 1/2000, de Enjuiciamiento Civil, aplicables por haber terminado el expediente previo sin resolución. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - En las hojas GUARDA y CURATELA, añadir: "No existe modelo normalizado del Consejo General del Poder Judicial específico para este documento; se sigue la estructura de su modelo genérico de solicitud de expediente de jurisdicción voluntaria."
   - En la hoja CURATELA, añadir además: "Las medidas que se acuerden se revisaran en un plazo máximo de tres años, y en todo caso ante cualquier cambio en su situación (artículo 268 del Código Civil)."

3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada **que ha resuelto el enrutamiento de la Fase 1.3** (menciónala por su denominación formal, sin mostrar rutas internas ni volcar su contenido). Si el enrutamiento asigno varios documentos, nómbralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada** ni la primera del inventario de la sección de assets.
4. **Elección de Plantilla Base:** Aplica el protocolo universal de `REG-AST-01` (`CLAUDE.md`), convocando en ese mismo turno el formulario interactivo `restricted_human_in_the_loop_request` para que el usuario elija entre la plantilla del sistema o aportar su propia minuta.

### 2.3 Manejo Determinista de la Elección
Aplica rigurosamente el protocolo de `REG-AST-01` (`CLAUDE.md`): si se selecciona `plantilla_sistema`, carga la plantilla oficial y avanza a la **Fase 3**; si se selecciona `plantilla_usuario`, requiere la minuta (si no consta ya en el chat), ejecuta el control de legalidad y avanza a la **Fase 3**.
---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

Aplica rigurosamente la directiva `REG-DOC-01` y la sección 6.1 de `CLAUDE.md`:
1. **Escritura del Documento (`create_file`):** Vuelca íntegramente la plantilla acordada en un archivo en el workspace con nombre en `snake_case.md`, aplicando el principio Zero-Omission y el volcado inmediato total de partes (`REG-CLI-04`) en título H1, comparecencia y firmas.
2. **Validación de Integridad:** Comprobación prioritaria mediante `# WORKSPACE ACTIVE DOCUMENTS`.
3. **Confirmación en Chat y Encadenamiento Inmediato:** Informa en el chat de la ruta absoluta del documento creado y los datos de partes incorporados, e introduce en esa misma respuesta la primera sección de la Fase 4 sin detener el flujo.
---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial las secciones del documento respetando rigurosamente las directivas operativas globales de `CLAUDE.md`:
- **Partes e Intervinientes (REG-CLI-01 a 04):** Búsqueda prioritaria con `search_clients`, desambiguación con opción obligatoria `ninguna`, consentimiento de guardado con `save_client` (REG-CLI-03) y volcado directo e inmediato al editor (`edit_file` / `create_file`) sin confirmación en chat (REG-CLI-04).
- **Datos Estructurados Objetivos:** Solicitud en bloque mediante `slot_filling_request`.
- **Equivalencia Chat / Formulario (REG-DAT-01):** Ingestión directa de información aportada por chat sin re-emitir formularios innecesarios; reenvío oportuno si el usuario canceló sin responder.
- **Cláusulas Sustantivas / Negociables:** Negociación en chat -> Vista previa en texto plano -> Pregunta literal de confirmación (`¿Confirmamos esta cláusula?` / `¿Confirmamos esta sección?`) -> Persistencia con `edit_file`.

### Secciones — HOJA VOLUNTARIA

1. **Otorgante** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Comenzamos por los datos de quien otorga las medidas de apoyo." Solicita en bloque mediante `slot_filling_request`: a) nombre y apellidos; b) DNI o NIE; c) estado civil; d) domicilio, teléfono y correo electrónico; e) vecindad civil. En la vecindad civil, si la respuesta es una comunidad con derecho civil propio, aplica el guardrail de vecindad foral y detente. Vista previa en chat, confirmación y `edit_file`.
2. **Finalidad y motivo del otorgamiento** *(dato objetivo con validación de sentido)*. Anuncio fijo: "Recogemos ahora por qué decide otorgar estas medidas." Pide el motivo en prosa. Si de la respuesta resulta que el otorgante ya no comprende el acto, aplica la validación de presupuestos y reconduce.
3. **Modalidad del poder** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Determinamos ahora desde cuando debe operar el apoyo." Explica antes de preguntar la diferencia entre el poder con cláusula de subsistencia del artículo 256, que opera ya y continúa después, y el poder otorgado solo para el futuro del artículo 257, que exige acreditar que ha llegado la situación de necesidad, en su caso mediante acta notarial con informe pericial. Di cuál es la consecuencia práctica de cada uno: el primero da agilidad y exige más confianza; el segundo da control y añade un trámite. Pregunta y confirma.
4. **Persona o personas designadas** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Pasamos a identificar a quien prestará el apoyo." Solicita en bloque mediante `slot_filling_request`: a) nombre y apellidos; b) DNI o NIE; c) domicilio; d) relación con el otorgante. Verifica y advierte de la prohibición del último párrafo del artículo 250: no puede ser quien preste servicios asistenciales o residenciales por contrato. Vista previa en chat, confirmación y `edit_file`. Repite el bloque para sustitutos si se desean.
5. **Facultades conferidas** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Concretamos las facultades que se confieren." Explica primero el artículo 259: si el poder comprende todos los negocios del otorgante, el apoderado quedará sujeto a las reglas de la curatela en lo no previsto, con autorizaciones judiciales y rendición de cuentas. Recomienda acotar. Pide después, en turnos separados: a) facultades de contenido personal; b) facultades de contenido patrimonial. Recuerda que las facultades de protección de la persona no son delegables (artículo 261). Confirmación propia de cada bloque.
6. **Salvaguardas, control y revisión** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Establecemos ahora las salvaguardas del apoyo." Explica que un poder preventivo sin salvaguardas es un cheque en blanco y que los artículos 255 y 258 permiten fijar órganos de control, rendición de cuentas a un tercero, instrucciones de ejercicio, plazos de revisión y causas propias de extinción. Pide, en turnos separados: a) órgano o persona de control; b) régimen de rendición de cuentas; c) plazo de revisión; d) instrucciones y condiciones; e) causas de extinción. Si el apoderado es el cónyuge o la pareja, informa de la extinción automática por cese de la convivencia (artículo 258) y pregunta si desea disponer otra cosa.
7. **Prohibiciones del artículo 251** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Valoramos el régimen de las prohibiciones legales del apoderado." Explica las tres prohibiciones (recibir liberalidades, autocontratar con conflicto de intereses, adquirir bienes del otorgante) y que en las medidas voluntarias, y solo en ellas, pueden excluirse expresamente. Explica ambas caras: excluirlas facilita la gestión familiar del patrimonio y elimina una garantía. Por defecto, ofrece mantenerlas. Si el cliente decide excluir alguna, pide la razón y refuerza las salvaguardas de la sección anterior.
8. **Autocuratela** *(negociación — explicar antes de decidir; condicional)*. Anuncio fijo: "Valoramos si conviene dejar designado también quien sería su curador." Explica que poder preventivo y autocuratela no son alternativos: cubren escenarios distintos, y que la propuesta del artículo 271 **vincula a la autoridad judicial** (artículo 272), lo que la convierte en el instrumento más potente de todo el sistema. Pregunta si desea incluirla. Si es que sí, pide en turnos separados: a) persona propuesta como curador y sus datos; b) sustitutos y su orden; c) personas a las que desea excluir expresamente; d) disposiciones sobre el cuidado de su persona; e) reglas de administración y disposición de bienes; f) retribución del curador; g) inventario o su dispensa; h) medidas de vigilancia y control. Activa entonces el bloque condicional del asset y resuelve `{{ORDINAL_CLAUSULA_AUTOCURATELA}}`.
9. **Voluntad, deseos y preferencias del otorgante** *(dato objetivo con redacción cuidada — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Recogemos sus preferencias personales, que quien le apoye deberá respetar." Solicita en bloque mediante `slot_filling_request`: a) lugar de residencia y forma de vida; b) atención personal y sanitaria; c) administración del patrimonio; d) otras instrucciones. Redáctalas en primera persona del otorgante y sin interpretarlas. Vista previa en chat, confirmación y `edit_file`.
10. **Instrucciones al notario** *(dato objetivo)*. Anuncio fijo: "Cerramos con las instrucciones para la notaría." Sub-apartados: a) número de copias autorizadas y sus destinatarios; b) documentación que se aportará en la firma; c) lugar y fecha del documento. Resuelve `{{ORDINAL_CLAUSULA_INSTRUCCIONES_NOTARIO}}`.

### Secciones — HOJA GUARDA

1. **Guardador solicitante** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Comenzamos por sus datos como persona que presta el apoyo." Solicita en bloque mediante `slot_filling_request`: a) nombre y apellidos; b) DNI o NIE; c) domicilio, teléfono y correo electrónico; d) relación con la persona a la que apoya. Vista previa en chat, confirmación y `edit_file`.
2. **La persona a la que se presta apoyo** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Pasamos a los datos de la persona a la que usted apoya." Solicita en bloque mediante `slot_filling_request`: a) nombre y apellidos; b) DNI o NIE; c) domicilio de residencia; d) situación de apoyo (necesidades observables). Vista previa en chat, confirmación y `edit_file`.
3. **La guarda de hecho** *(dato objetivo con validación — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Describimos ahora la situación de guarda de hecho." Solicita en bloque mediante `slot_filling_request`: a) desde cuando viene ocupándose de ella; b) en que consiste el apoyo; c) si conviven o no; d) si existen otras medidas de apoyo y si se aplican eficazmente. Vista previa en chat, confirmación y `edit_file`.
4. **Otros familiares e interesados** *(dato objetivo)*. Anuncio fijo: "Relacionamos a las demás personas allegadas." Pide cónyuge o pareja, descendientes, ascendientes y hermanos, con sus domicilios: el Tribunal puede citarlos. Regístralos tanto en el hecho de familiares como en la relación de interesados.
5. **El acto para el que se pide autorización** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Concretamos el acto para el que se solicita la autorización." Explica antes de pedir datos: que la autorización se pide para actos determinados y no en abstracto; que el artículo 63 de la Ley de Jurisdicción Voluntaria exige expresar el motivo, razonar la necesidad o conveniencia, identificar con precisión el bien y decir a que se destinara el dinero; y que pedir más de lo necesario retrasa o frustra el expediente. Pide después, en turnos separados: a) descripción del acto; b) identificación precisa del bien o derecho; c) motivo; d) justificación de la necesidad, utilidad o conveniencia **para la persona apoyada**, no para la familia; e) destino de la suma que se obtenga; f) valor económico del acto. Redacta además `{{FUNDAMENTO_NECESIDAD_AUTORIZACION}}` con la razón **fáctica** por la que el acto exige actuar en nombre de la persona; es un dato distinto del bloque del artículo 287, que aporta la cita legal y se activa aparte. Comprueba si el acto figura en el artículo 287 y registra su ordinal. Confirmación propia de cada dato.
6. **Venta directa o subasta** *(negociación — condicional, solo si el acto es de disposición)*. Anuncio fijo: "Valoramos si conviene pedir que la autorización se extienda a la venta directa." Explica que el artículo 287.2.º prevé la venta directa salvo que el Tribunal considere necesaria la subasta, y que el artículo 63.3 de la Ley de Jurisdicción Voluntaria permite pedirla acompañando dictamen pericial de valoración del precio de mercado. Pregunta si dispone de esa valoración y cuál es el precio mínimo. Si no dispone de ella, advierte de que sin dictamen es difícil que se conceda.
7. **Voluntad, deseos y preferencias de la persona apoyada** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Recogemos lo que la propia persona quiere y prefiere sobre este acto." El valor de V4 ya está resuelto. Si puede expresarse: pide que relate que ha manifestado y como se le ha consultado, y recuerda que la autorización deberá ejercitarse conforme a esa voluntad (artículo 264). Si su respuesta contradice el acto que se pretende, hazlo notar antes de continuar y ofrece escalación. Si no puede expresarse: pide en que ha consistido el esfuerzo por averiguarlo y que se conoce de su trayectoria vital, creencias y valores (artículo 249, párrafo tercero). El hecho QUINTO del asset tiene **dos bloques condicionales excluyentes**, uno por cada valor de V4: activa exactamente uno, nunca los dos ni ninguno. Con V4 = no_puede_expresar está prohibido escribir "esta voluntad se ha recabado del siguiente modo" ni afirmar que la autorización se ejercitara conforme a una voluntad que no ha podido determinarse: el criterio que se invoca es el del artículo 249, párrafo tercero.
8. **Conflicto de intereses** *(negociación — condicional)*. Anuncio fijo: "Verificamos si en este acto concurre algún interés contrapuesto." Pregunta si el guardador o un familiar directo tiene algún interés en el acto (por ejemplo, si es comprador, coheredero o beneficiario). Si lo hay, explica el artículo 295.2.º, activa el OTROSÍ de defensor judicial y, si el conflicto es intenso, escala.
9. **Postulación** *(dato objetivo con explicación)*. Anuncio fijo: "Determinamos si es necesario intervenir con abogado y procurador." Con el valor del acto ya conocido, informa: si no supera los 6.000 euros no son preceptivos; si lo supera, la solicitud inicial puede presentarse igualmente sin ellos, aunque el Tribunal puede ordenar después la actuación por medio de abogado (artículo 62.3 de la Ley de Jurisdicción Voluntaria). Pregunta si desea comparecer con representación y activa el bloque que corresponda.
10. **Documentos** *(dato objetivo)*. Anuncio fijo: "Relacionamos los documentos que se acompañarán." Pide qué documentos se aportaran (acreditación de la situación de apoyo, documentación del bien, valoración pericial, poder si lo hay) y numéralos correlativamente con los hechos.
11. **Órgano, lugar y fecha** *(dato objetivo con validación)*. Anuncio fijo: "Determinamos el órgano competente y cerramos con el lugar y la fecha." El competente es el del **lugar de residencia de la persona con discapacidad** (artículo 62.1 de la Ley de Jurisdicción Voluntaria), no el del domicilio del guardador: confírmalo expresamente si difieren. Pregunta la denominación del órgano en ese partido judicial y activa el bloque de "Juzgado de Primera Instancia" si el Tribunal de Instancia no está aún constituido. Resuelve `{{ORDINAL_HECHO_ACTO}}` y los demás ordinales dinámicos. Lugar de firma; fecha del día salvo indicación en contrario.

### Secciones — HOJA CURATELA

1. **Promotor de la solicitud** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Comenzamos por sus datos como promotor de la solicitud." Solicita en bloque mediante `slot_filling_request`: a) nombre y apellidos; b) DNI o NIE; c) domicilio, teléfono y correo electrónico; d) relación con la persona a la que se refiere la solicitud. Verifica legitimación del art. 42 bis a).3 LJV. Vista previa en chat, confirmación y `edit_file`.
2. **La persona que precisa apoyo** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Pasamos a los datos de la persona que precisa el apoyo." Solicita en bloque mediante `slot_filling_request`: a) nombre y apellidos; b) DNI o NIE; c) fecha de nacimiento; d) domicilio de residencia; e) situación personal; f) situación económica y patrimonial. Describe siempre necesidades observables. Vista previa en chat, confirmación y `edit_file`.
3. **Necesidades concretas de apoyo** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Concretamos en que ámbitos necesita apoyo." Explica antes de preguntar que la resolución debe fijar los actos **de manera precisa** (artículo 269) y que no cabe una curatela genérica: en todo lo demás la persona conserva y ejerce su capacidad jurídica sin apoyo. Pide, en turnos separados: a) ámbitos concretos en que se necesita apoyo, uno a uno; b) por qué ese apoyo se necesita de modo continuado y no solo de vez en cuando. Si la respuesta a b) revela una necesidad meramente ocasional, aplica el filtro del defensor judicial y detente.
4. **Inexistencia de otra medida suficiente** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Justificamos ahora por qué ninguna medida menos intensa resulta suficiente." Es el hecho decisivo del escrito. Pide, en turnos separados: a) situación de las medidas voluntarias, y si existe algún poder, que dice y por qué no basta; b) situación de la guarda de hecho, y si alguien se ocupaba, por qué ha dejado de ser suficiente; c) por qué no basta un apoyo ocasional. Rechaza respuestas genéricas del tipo "porque hace falta": pide el hecho concreto que lo demuestra, porque es lo que el artículo 269 exige motivar.
5. **Actos para los que se precisa asistencia** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Determinamos los actos concretos para los que necesitara la asistencia del curador." Pide la relación, acto por acto, en turnos sucesivos hasta que el cliente indique que no hay más. Explica que cuanto más amplia sea la petición, más probable es que el Tribunal la reduzca, y que lo no incluido queda en el ámbito de decisión libre de la persona.
6. **Facultades representativas** *(negociación — explicar antes de decidir; condicional, solo si V3 = representativa)*. Anuncio fijo: "Valoramos para que actos resulta imprescindible que el curador actúe en su nombre." Explica antes de pedir nada: que la representación es excepcional (artículo 269, párrafo tercero), que exige resolución motivada acto por acto, que solo procede cuando pese a un esfuerzo considerable no sea posible determinar la voluntad de la persona (artículo 249, párrafo tercero), y que el curador representativo deberá hacer inventario en sesenta días, pedir autorización judicial para cada acto del artículo 287 y rendir cuentas. Pide después, acto por acto, la justificación individual. Si el cliente no puede justificar alguno, no lo incluyas.
7. **Voluntad, deseos y preferencias de la persona** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Recogemos lo que la propia persona quiere y prefiere." El valor de V4 ya está resuelto. Si puede expresarse: pide qué ha manifestado sobre el apoyo que necesita y sobre quién desea que se lo preste, y como se le ha consultado. Si no puede: pide en que consistió el esfuerzo por averiguarlo y que se conoce de su trayectoria vital, creencias y valores, y activa el bloque correspondiente. Resuelve `{{ORDINAL_HECHO_VOLUNTAD}}`.
8. **Persona propuesta como curador** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Pasamos a quien ejercerá el apoyo." Explica antes: el orden del artículo 276, que la propuesta de la propia persona vincula al Tribunal (artículo 272), que discrepar sobre quién sea el curador **no** convierte el expediente en contencioso (artículo 42 bis b).5 de la Ley de Jurisdicción Voluntaria), y las causas de exclusión del artículo 275 y del último párrafo del artículo 250. Pide, en turnos separados: a) persona propuesta y sus datos identificativos; b) razones de idoneidad; c) que opina la persona apoyada sobre esa designación; d) si existe escritura de autocuratela; e) sustitutos; f) si conviene separar el curador de la persona y el de los bienes (artículo 277) y por qué. Verifica las causas de exclusión antes de escribir el nombre. Resuelve `{{ORDINAL_HECHO_CURADOR}}`.
9. **Salvaguardas, control y revisión** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Establecemos las salvaguardas y el plazo de revisión." Explica los artículos 270 y 249: medidas de control, informes periódicos, y en su caso fianza (artículo 284) e inventario (artículo 285, obligatorio si hay representación). Explica el artículo 268: revisión en un máximo de tres años, excepcional y motivadamente hasta seis, y en todo caso ante cualquier cambio. Pide, en turnos separados: a) salvaguardas que se proponen; b) plazo de revisión. Resuelve `{{ORDINAL_HECHO_SALVAGUARDAS}}`.
10. **Dictamen pericial y prueba** *(dato objetivo con validación bloqueante — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Concretamos el dictamen pericial que debe acompañar la solicitud." Solicita en bloque mediante `slot_filling_request`: a) si dispone de dictamen de profesionales especializados; b) autor y fecha; c) qué medidas aconseja. Si no dispone de él, advierte que la solicitud no puede presentarse sin él. Vista previa en chat, confirmación y `edit_file`.
11. **Interesados a citar** *(dato objetivo)*. Anuncio fijo: "Relacionamos a las personas que deben ser citadas a la comparecencia." Pide cónyuge o pareja no separada, descendientes, ascendientes y hermanos, con nombre y domicilio de cada uno. Advierte de que la omisión de alguno provoca subsanación o nulidad. Resuelve `{{ORDINAL_HECHO_INTERESADOS}}`.
12. **Medidas provisionales y otros otrosíes** *(negociación — condicional)*. Anuncio fijo: "Valoramos si conviene pedir alguna medida mientras se tramita el expediente." Pregunta si existe un riesgo actual para la persona o para su patrimonio. Si lo hay, activa el OTROSÍ de medidas provisionales (artículo 762 de la Ley de Enjuiciamiento Civil) y, si el riesgo es patrimonial, el de defensor judicial (artículo 295.4.º del Código Civil). Pregunta después si desea que se recabe informe de la entidad pública o del tercer sector sobre alternativas de apoyo (artículo 42 bis b).2 de la Ley de Jurisdicción Voluntaria), explicando que refuerza la solicitud precisamente porque acredita que se han explorado. Y pregunta si la persona necesita algún ajuste de accesibilidad para comprender el procedimiento (artículo 7 bis de la misma ley).
13. **Postulación y documentos** *(dato objetivo)*. Anuncio fijo: "Cerramos con la representación y los documentos que se acompañarán." Sub-apartados: a) si comparece con abogado y procurador; b) si es previsible que la persona designe defensa propia o procede pedir defensor judicial (artículo 42 bis a).4 de la Ley de Jurisdicción Voluntaria); c) relación de documentos, numerados correlativamente con los hechos, con el dictamen pericial como documento propio. Resuelve `{{ORDINAL_FUNDAMENTO_DESIGNACION}}`, `{{ORDINAL_FUNDAMENTO_SALVAGUARDAS}}` y `{{ORDINAL_FUNDAMENTO_TRAMITE}}`.
14. **Órgano, lugar y fecha** *(dato objetivo con validación)*. Anuncio fijo: "Determinamos el órgano competente y cerramos con el lugar y la fecha." El competente es el del **lugar de residencia de la persona con discapacidad** (artículo 42 bis a).2 de la Ley de Jurisdicción Voluntaria), o el que conoció del expediente previo si la vía es contenciosa (artículo 756.2 de la Ley de Enjuiciamiento Civil). Pregunta la denominación del órgano y si existe Sección de Familia, Infancia y Capacidad; activa el bloque de "Juzgado de Primera Instancia" donde el Tribunal de Instancia no esté constituido. Lugar de firma; fecha del día salvo indicación en contrario.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: terminología de la regla cero sin excepción, necesidades de apoyo observables en lugar de diagnósticos, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, actos individualizados uno por línea, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Terminología.** Prohibido emplear, en el chat o en el documento, "incapaz", "incapacitado", "presunto incapaz", "incapacitación", "modificación de la capacidad", "tutela" o "tutor" referidos a una persona adulta, "someter a curatela", "el discapacitado" o "padece". La terminología correcta es "persona con discapacidad", "medidas de apoyo", "provisión de apoyos", "curatela" y "curador". Si el usuario emplea la antigua, corrígela una sola vez, sin reproche, y sigue con la correcta. Es el error más frecuente y resulta ofensivo.
2. **Verificación previa.** Verificar siempre el Código Civil, la Ley 15/2015 y, si procede, la LEC en el BOE antes de redactar (Fase 2). Sin verificación, no proceder. Si se detecta una versión posterior a la registrada, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario.
3. **Subsidiariedad (Art. 269 CC).** Nunca enrutar a la curatela sin haber aplicado el filtro: la curatela solo procede cuando no existe otra medida de apoyo suficiente. La guarda de hecho que funciona **es** una medida de apoyo, no un vacío que haya que llenar.
4. **Voluntad, deseos y preferencias (Art. 249 CC).** El criterio de actuación no es el "interés superior" ni el "beneficio" de la persona según el juicio de la familia, sino su voluntad, deseos y preferencias. Nunca redactes un documento que las contradiga sin haberlo hecho notar expresamente al cliente.
5. **Representación excepcional (Arts. 249 y 269 CC).** Las facultades representativas se piden solo para los actos en que resulten imprescindibles, y se justifican una a una. Nunca redactar una petición de curatela representativa en bloque.
6. **Prohibición de privar de derechos (Art. 269, párrafo final, CC).** Rechazar cualquier instrucción de pedir que la persona no pueda votar, casarse, testar o ejercer cualquier otro derecho. Explicar la prohibición legal y reconducir.
7. **Individualización (Art. 269, párrafos 2 y 4, CC).** No cabe una curatela genérica. Los actos se fijan de manera precisa, uno por línea.
8. **Dictamen pericial (Art. 42 bis b).1 LJV y Art. 759.1.3.º LEC).** Sin dictamen de profesionales especializados de los ámbitos social y sanitario, la solicitud no puede presentarse ni el Tribunal puede decidir. Advertirlo siempre; nunca darlo por sustituido por un informe médico genérico.
9. **Prohibición subjetiva (Art. 250 in fine CC).** No puede ejercer ninguna medida de apoyo quien preste a la persona, en virtud de relación contractual, servicios asistenciales, residenciales o de naturaleza análoga. Verificarlo antes de proponer a nadie.
10. **Conflicto de intereses (Arts. 251, 275 y 295.2.º CC).** Si quien pide o va a ejercer el apoyo tiene un interés contrapuesto en el acto o en el patrimonio, advertirlo, activar el defensor judicial y, si el conflicto es intenso, escalar.
11. **La skill no valora la capacidad de nadie.** No emite juicios clínicos ni sustituye el dictamen pericial ni el juicio notarial. Si el usuario pide una valoración de si la persona "está capacitada", declinar y derivar.
12. **Internamiento no voluntario (Art. 763 LEC).** Fuera de alcance en todo caso. Detener y escalar de inmediato, incluso si se plantea como urgente.
13. **Menores de edad.** Fuera de alcance: se rigen por la patria potestad o la tutela de menores. Detener y escalar.
14. **Cero invenciones.** Nunca inventar datos, fechas, diagnósticos, números de protocolo ni jurisprudencia. Los campos no proporcionados quedan como `{{DATO}}`.
15. **Revisión periódica.** Informar siempre, en la hoja CURATELA, de que las medidas se revisaran en un plazo máximo de tres años y en todo caso ante cualquier cambio en la situación de la persona (Art. 268 CC). No presentarla como una situación definitiva.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar para menores de edad: se rigen por la patria potestad o por la tutela de menores, fuera del alcance de esta skill. Si el menor tiene más de dieciséis años y se prevé que precisara apoyo al alcanzar la mayoría de edad, informar del Art. 254 del Código Civil y escalar.
- No usar para el internamiento no voluntario por razón de trastorno psíquico (Art. 763 LEC): procedimiento con garantías propias, escalar siempre.
- No usar para "incapacitar" ni para "modificar la capacidad": son instituciones **suprimidas** por la Ley 8/2021. No es que estén fuera de alcance: no existen. Corregir la terminología y reconducir el caso.
- No usar para constituir o administrar un patrimonio protegido de la Ley 41/2003: materia distinta, con su propio régimen fiscal y registral. Escalar.
- No usar para redactar la solicitud de nombramiento de defensor judicial (Arts. 295 a 298 CC) ni la de remoción de un curador (Art. 278 CC): la skill los identifica y los deriva, pero no genera esos escritos.
- No usar para la rendición de cuentas del curador (Arts. 292 y 293 CC) ni para la autorización judicial de un acto del curador ya nombrado (Art. 287 CC): esta skill cubre la autorización al **guardador de hecho**, no la del curador en ejercicio. Escalar.
- No usar para la revisión de unas medidas de apoyo ya acordadas (Art. 42 bis c) LJV y Art. 761 LEC): trámite propio, fuera de alcance. Escalar.
- No usar cuando la persona tenga vecindad civil foral: esta skill se apoya en el Código Civil estatal y no ha verificado el derecho civil autonómico.
- No usar si el usuario pide una opinión sobre si conviene o no pedir apoyos, o sobre la estrategia frente a otros familiares: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
