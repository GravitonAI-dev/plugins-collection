---
name: pareja-de-hecho
title: Pareja de hecho
i18n:
  en:
    name: unmarried-couple
    title: Unmarried couple
    description: >
      Generates the documentation of an unmarried couple (pareja de hecho) at its three stages:
      (1) FORMATION, a checklist for registration in the regional register of unmarried couples,
      with the requirements, documents and procedure verified against the specific region's
      regulations; (2) COHABITATION, a cohabitation agreement under Article 1255 of the **Civil
      Code**, governing each partner's assets, jointly acquired assets and unequal contributions
      (Arts. 392 to 406 CC), the home, contribution to expenses, debts and, if expressly agreed,
      financial compensation; and (3) BREAKUP, an agreement terminating cohabitation and
      liquidating joint property, with cancellation of the registration, the fate of the home
      and mortgage, debts and any agreed compensation. There is no national unmarried couples
      act or register, so the skill always asks for the region and verifies its law and register
      with a web search. Do not use for custody, maintenance or visiting arrangements for common
      children (measures for children of unmarried parents skill), for marriage, separation or
      divorce, for immigration or family reunification, or to resolve survivor's pension
      entitlement, on which it only informs.
description: >
  Genera la documentación propia de la pareja de hecho en sus tres momentos: (1) CONSTITUCIÓN —
  checklist de inscripción en el registro autonómico de parejas de hecho, con los requisitos, la
  documentación y el trámite verificados en el lanzamiento contra la normativa de la comunidad
  autónoma concreta; (2) CONVIVENCIA — pacto de convivencia otorgado al amparo del artículo 1255 del
  **Código Civil**, que regula el régimen de los bienes de cada uno, los bienes adquiridos en común y las
  aportaciones desiguales (arts. 392 a 406 CC), la vivienda, la contribución a los gastos, las deudas
  y, si así se pacta expresamente, una compensación económica por la dedicación a la familia o al
  negocio del otro; y (3) RUPTURA — pacto de extinción de la convivencia y liquidación de la comunidad
  de bienes, con la cancelación de la inscripción registral, el destino de la vivienda y del préstamo
  hipotecario, las deudas y la compensación que en su caso se convenga. NO existe ley estatal de
  parejas de hecho ni registro estatal: la skill pregunta SIEMPRE la comunidad autónoma y verifica su
  ley y su registro con `web_search` en cada lanzamiento, sin afirmar nunca un requisito autonómico de
  memoria. NO regula custodia, alimentos ni visitas de los hijos comunes (deriva a
  `medidas-hijos-no-matrimoniales`), NO cubre matrimonio, separación ni divorcio, NO
  tramita la inscripción ante el registro, NO cubre extranjería ni reagrupación familiar y NO resuelve
  el derecho a la pensión de viudedad, del que solo informa.
when_to_use: |
  - Una pareja quiere constituirse e inscribirse como pareja de hecho y necesita saber qué requisitos y
    que documentación exige el registro de su comunidad autónoma.
  - Una pareja que convive quiere regular por escrito los aspectos económicos de su convivencia
    (bienes, vivienda, gastos, deudas, compensaciones).
  - Han comprado juntos una vivienda con aportaciones desiguales y quieren dejar constancia de ello.
  - Una pareja de hecho se separa y quiere liquidar de común acuerdo lo que tienen en común.
  - El usuario pregunta qué derechos le da inscribirse como pareja de hecho, si hereda de su pareja o
    si tendrá derecho a una compensación si se separan.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - finalidad: constituir e inscribir la pareja / regular la convivencia mediante pacto / regular la ruptura
  - comunidad_autonoma: comunidad de residencia de la pareja (vector obligatorio en todas las ramas)
  - hijos_comunes: sí / no (determina la derivación a la skill de medidas de hijos no matrimoniales)
  - bienes_o_desequilibrio: hay bienes adquiridos en común o desequilibrio económico entre ellos / no
  - datos_conviviente_a: nombre, documento de identidad, domicilio
  - datos_conviviente_b: nombre, documento de identidad, domicilio
  - datos_convivencia: fecha de inicio, domicilio común, situación registral y, en su caso, fecha de cese
  - bienes_comunes: relación de bienes adquiridos conjuntamente, titularidad formal y aportaciones reales
  - vivienda: situación jurídica, titularidad, préstamo hipotecario y destino del uso
  - gastos_y_deudas: criterio de contribución, cuenta común, deudas conjuntas
  - dedicacion: dedicación de uno a la familia o al negocio del otro y compensación que se pacte
  - liquidacion: acuerdo de adjudicación, venta o compensación de cuotas (solo ruptura)
outputs:
  - checklist_inscripcion_registro: >
      checklist de requisitos, documentación y trámite del registro autonómico, en markdown, DRAFT, con la fecha de verificación de la normativa autonómica
  - pacto_convivencia: pacto de convivencia en markdown, DRAFT
  - pacto_ruptura_pareja_hecho: pacto de extinción de la convivencia y liquidación en markdown, DRAFT
references:
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/regimen-pareja-hecho-derecho-comun.md
  - references/verificacion-normativa-autonomica.md
assets:
  - assets/template-checklist-inscripcion-registro.md
  - assets/template-pacto-convivencia.md
  - assets/template-pacto-ruptura-pareja-hecho.md
---

# Constitución, Convivencia y Ruptura de la Pareja de Hecho

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
      "rationale": "Resolver V1: cada finalidad tiene su propio asset, y no existe ley estatal de parejas de hecho.",
      "question": "¿Qué necesita preparar?",
      "options": [
        {"id": "constituir_inscribir", "label": "Constituir la pareja de hecho e inscribirla en el registro"},
        {"id": "pacto_convivencia", "label": "Regular la convivencia mediante un pacto entre los convivientes"},
        {"id": "pacto_ruptura", "label": "Regular los efectos de la ruptura de la pareja"}
      ]
    },
    {
      "id": "hijos_comunes",
      "rationale": "Resolver V2: la existencia de hijos comunes obliga a derivar todo lo relativo a custodia, estancias y alimentos a la skill de medidas sobre hijos no matrimoniales.",
      "question": "¿Hay hijos comunes de la pareja?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"}
      ]
    },
    {
      "id": "bienes_o_desequilibrio",
      "rationale": "Resolver V3: activa los bloques de bienes comunes, aportaciones desiguales y compensación económica.",
      "question": "¿Hay bienes adquiridos en común, o desequilibrio económico entre los convivientes?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `finalidad`
- `V2` — `hijos_comunes`
- `V3` — `bienes_o_desequilibrio`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalúa en este orden:

- Si V1 = constituir_inscribir → **HOJA INSCRIPCIÓN**: `assets/template-checklist-inscripcion-registro.md`. En esta hoja V2 y V3 no eligen asset; la existencia de hijos comunes se recaba en la sección de pensión de viudedad porque altera sus requisitos.
- Si V1 = pacto_convivencia → **HOJA CONVIVENCIA**: `assets/template-pacto-convivencia.md`. V3 determina si se activan los bloques de bienes comunes, aportaciones desiguales y compensación pactada.
- Si V1 = pacto_ruptura → **HOJA RUPTURA**: `assets/template-pacto-ruptura-pareja-hecho.md`. V2 activa el bloque de remisión sobre hijos comunes y dispara la derivación; V3 determina los bloques de liquidación y compensación.
- Si V1 = pacto_ruptura y V2 = si → además de la HOJA RUPTURA, **DERIVAR** expresamente para todo lo relativo a los hijos: custodia, régimen de estancias y visitas, y alimentos se regulan en `medidas-hijos-no-matrimoniales`, exigen la intervención del Ministerio Fiscal y no producen efecto sin aprobación judicial. **Esta skill no los regula ni los incluye en el pacto**: activa el bloque de remisión del asset y ofrece continuar con esa skill al cerrar el documento.
- Si lo que se pretende es un matrimonio, una separación o un divorcio, o la liquidación de un régimen económico matrimonial → **DETENER**: fuera de alcance. Derivar a `divorcio` o a `liquidacion-gananciales` según corresponda.
- Si lo que se pretende es tramitar la inscripción ante el registro, o presentar la solicitud en nombre del cliente → **DETENER** esa pretensión concreta: la skill prepara la documentación y el checklist, pero la solicitud la presenta la propia pareja. Continuar con la HOJA INSCRIPCIÓN advirtiéndolo.
- Si aparecen indicios de violencia entre los convivientes → **DETENER de inmediato**, en el mismo turno, sin crear ni continuar ningún documento. Advertir y escalar a asistencia jurídica especializada.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **TODAS LAS HOJAS:** ninguno de los convivientes puede estar unido por vínculo matrimonial con otra persona ni tener otra pareja de hecho constituida. Si consta que sí, advertir de que la constitución de la pareja no es posible y de que un pacto entre ellos puede afectar a derechos de terceros; detener la rama de inscripción y escalar.
- **TODAS LAS HOJAS:** si los convivientes residen en comunidades autónomas distintas, tienen vecindad civil distinta, o concurre elemento internacional (residencia fuera de España, pareja constituida en el extranjero) → advertir de que la determinación de la ley aplicable y del registro competente excede de lo que puede resolverse aquí, y escalar. En la rama de inscripción, no continuar sin esa aclaración.
- **HOJA INSCRIPCIÓN:** si de la verificación de la Fase 2 resulta un requisito temporal (tiempo mínimo de convivencia previa o de empadronamiento conjunto) que la pareja aún no cumple, **no dar por presentable la solicitud**: hacerlo constar en el checklist, indicar desde cuando podrá presentarse y advertir de que la presentación anticipada conduce a la denegación o al archivo.
- **HOJA RUPTURA:** si existe un pacto de convivencia previo en el workspace, consultarlo prioritariamente en la sección `# WORKSPACE ACTIVE DOCUMENTS` (o mediante `read_file` en caso extremo) antes de redactar la liquidación: sus previsiones para el cese son ley entre las partes y el pacto de ruptura las desarrolla o las sustituye expresamente, nunca las contradice en silencio.
- **HOJA RUPTURA:** si el cliente pide que el pacto incluya medidas sobre los hijos, rechazarlo y explicar por qué (cauce propio, Ministerio Fiscal, aprobación judicial). Recoger la remisión, no la medida.
- **HOJA CONVIVENCIA y HOJA RUPTURA:** si el cliente pide una cláusula que pretenda crear entre ellos una sociedad de gananciales, unas capitulaciones matrimoniales o un convenio regulador, rechazarla: son instituciones privativas del matrimonio. Explicar la alternativa válida (comunidad de bienes pactada sobre bienes concretos, o el propio pacto) y ofrecerla.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Leyes autonómicas reguladoras de parejas de hecho en la CCAA de residencia; Art. 1.255 del Código Civil (autonomía de la voluntad en pactos privados); doctrina del Tribunal Constitucional (STC 93/2013 y concordantes sobre inexistencia de equiparación matrimonial automática); y Art. 174 TRLGSS (pensión de viudedad).
2. **Orientación Legal del Caso:**

**Informa la normativa aplicable, ya verificada.** Empieza siempre por la advertencia de ausencia de ley estatal, sigue con la ley autonómica concreta verificada en este lanzamiento y su enlace, y cierra con la base de derecho común del documento. Textos fijos por hoja:
   - INSCRIPCIÓN: "No existe una ley estatal de parejas de hecho ni un registro estatal: la materia la regula cada comunidad autónoma. A su caso le resulta de aplicación {{DENOMINACION_LEY_AUTONOMICA}}, que he verificado hoy en su fuente oficial: {{ENLACE_LEY_AUTONOMICA}}. El registro competente es el {{DENOMINACION_REGISTRO}}: {{ENLACE_REGISTRO}}."
   - CONVIVENCIA: "No existe una ley estatal de parejas de hecho, y la convivencia no crea entre ustedes ningún régimen económico. El pacto que vamos a preparar se otorga al amparo del artículo 1255 del Código Civil, y a los bienes que hayan adquirido conjuntamente les resultan de aplicación los artículos 392 y siguientes del mismo cuerpo legal, sobre la comunidad de bienes. Puede consultar el texto oficial en https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763. En cuanto a su comunidad autónoma, he verificado hoy {{DENOMINACION_LEY_AUTONOMICA}}: {{ENLACE_LEY_AUTONOMICA}}."
   - RUPTURA: "Al no haber existido matrimonio entre ustedes, no hay régimen económico matrimonial que liquidar ni cabe un convenio regulador. Lo que vamos a preparar es un pacto otorgado al amparo del artículo 1255 del Código Civil, que liquida la comunidad de bienes sobre lo adquirido conjuntamente conforme a los artículos 392 y siguientes. Puede consultar el texto oficial en https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763. En cuanto a su comunidad autónoma, he verificado hoy {{DENOMINACION_LEY_AUTONOMICA}}: {{ENLACE_LEY_AUTONOMICA}}."
   - Si la verificación autonómica fallo, no cites ley autonómica alguna: advierte expresamente de que no se ha podido verificar la normativa de la comunidad autónoma y de que el punto queda pendiente de verificación manual. **Nunca inventes una denominación de ley ni un enlace.**
   - **Corrección inmediata del malentendido, si el cliente ya lo ha planteado.** Si en sus mensajes ha preguntado o dado por supuesto que inscribirse equipara al matrimonio, que crea gananciales, que da derecho a heredar o que garantiza una compensación, **respóndele aquí, en este mismo mensaje**, sin esperar a la sección de la edición incremental que trate esa materia. Diez turnos después es tarde: el cliente está tomando su decisión ahora. Di con todas las letras que no, y por qué: la inscripción no crea ningún régimen económico, lo adquirido en común se rige por los artículos 392 y siguientes del Código Civil según la titularidad, y **el conviviente no hereda sin testamento** salvo lo que prevea la normativa civil aplicable que hayas verificado. Si ha preguntado por heredar, añade que la única vía es otorgar testamento ante notario, con el límite de las legitimas, y ofrece continuar después con `testamento-planificacion`. Esta corrección no sustituye a la sección correspondiente de la Fase 4: la anticipa.
   - Si V1 = pacto_ruptura y V2 = si (hay hijos comunes), añade en el mismo mensaje: "Le adelanto que todo lo relativo a sus hijos — guarda y custodia, régimen de estancias y pensión de alimentos — no puede regularse en este pacto: tiene un cauce propio, exige la intervención del Ministerio Fiscal y no produce efecto sin aprobación judicial. Lo trataremos en un documento aparte cuando cerremos este."

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

### Hoja de Ruta de Secciones y Cláusulas Condicionales

**Anuncio de sección y encadenamiento:** al terminar una sección y confirmar su edición en disco, emite en ese mismo turno el anuncio fijo de la sección que se abre y lanza de inmediato su formulario `slot_filling_request` (si es grupo de datos) o su planteamiento en chat (si es negociación). Las cláusulas marcadas `[negociacion]` se explican y se confirman una a una en el chat. **La vista previa y la confirmación siempre van en el chat.**

**Regla propia de esta materia para las cláusulas `[negociacion]`:** antes de pedir la decisión, explica siempre **cuál es el régimen por defecto si no se pacta nada** y que consecuencia tiene. En pareja de hecho el régimen por defecto es casi siempre "nada", y el cliente no lo sabe: si no se le explica, decide a ciegas. Esta explicación es breve — dos o tres frases — y va en el mismo turno que la pregunta.

### Secciones — HOJA CONVIVENCIA

1. **Datos de cada conviviente** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si son nuevos, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por la identificación de ambos convivientes." Invoca `search_clients` prioritariamente. Si son nuevos, invoca de inmediato `slot_filling_request` con dos grupos de campos (Conviviente A y Conviviente B) para recabar a la vez: a) nombre completo; b) tipo y número de documento de identidad; c) domicilio a efectos de notificaciones. Si son nuevos clientes, resuelve de inmediato `restricted_human_in_the_loop_request` (`REG-CLI-03`). Conforme a `REG-CLI-04`, vuelca de inmediato los datos al documento con `edit_file` (o ya volcados en `create_file`) de forma directa sin requerir confirmación en chat de los datos personales, sustituyendo exhaustivamente los nombres de los convivientes en todas sus apariciones a lo largo del documento (título/encabezado H1, comparecencia y firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones). Muestra en el chat un resumen de la comparecencia asentada y encadena directamente con la siguiente sección.
2. **La convivencia y su situación registral** *(dato objetivo — recogida en lote con `slot_filling_request`, confirmación en chat)*. Anuncio fijo: "Concretamos ahora los datos de su convivencia y su situación registral." Solicita en bloque mediante `slot_filling_request` los datos objetivos: a) fecha de inicio de la convivencia; b) domicilio común; c) situación registral (si está inscrita y fecha de inscripción, o previsión de hacerlo). Tras recibir el formulario, emite la vista previa en el chat, pide confirmación en el chat ("¿Confirmamos esta cláusula?") y aplica `edit_file`. Activa según la respuesta el expositivo TERCERO que corresponda, en su única variante.
3. **Régimen de los bienes de cada uno** *(negociación)*. Anuncio fijo: "Abordamos ahora el régimen de sus bienes." Explica antes de preguntar: la convivencia no crea ningún régimen económico, cada uno conserva lo suyo y lo que gane durante la convivencia, y la ley no impone participación alguna en lo del otro; eso seguirá siendo así salvo que lo pacten de otro modo. Pregunta después si desean además inventariar en el pacto los bienes privativos de cada uno para facilitar la prueba de la titularidad, y activa o descarta ese bloque.
4. **Bienes adquiridos en común y aportaciones desiguales** *(negociación — la sección más importante del documento)*. Anuncio fijo: "Pasamos a los bienes que hayan adquirido conjuntamente." Explica antes: lo adquirido en común se rige por la comunidad de bienes de los artículos 392 y siguientes del Código Civil, **las cuotas se presumen iguales salvo prueba en contrario** (artículo 393) y quien aportó más dinero del que refleja la titularidad tiene la carga de probarlo. Sub-apartados: a) relación de bienes adquiridos en común, con su titularidad formal; b) si las aportaciones económicas reales coincidieron con esa titularidad y, si no, cuánto aportó cada uno. Si hubo desigualdad, pregunta después cuál de los tres efectos quieren darle, explicando los tres: que genere un crédito exigible en la liquidación, que se ajuste la cuota de titularidad a la aportación real, o que se considere una liberalidad sin crédito alguno. Advierte de que la tercera opción es irreversible en la práctica y de que la segunda exige otorgar después la escritura que rectifique la titularidad. Confirmación propia de cada decisión en chat.
5. **Vivienda que constituye el domicilio común** *(negociación)*. Anuncio fijo: "Determinamos ahora la situación de la vivienda en la que conviven." Sub-apartados: a) situación jurídica (propiedad de uno, propiedad común o arrendamiento), activando la variante correspondiente; b) si existe préstamo hipotecario y como se reparten las cuotas. Explica siempre que el reparto pactado **no vincula a la entidad prestamista**, frente a la cual ambos siguen respondiendo. Si la vivienda es propiedad de uno solo, explica que el otro la ocupa por tolerancia y sin derecho arrendaticio, y pregunta qué plazo de desalojo quieren fijar para el caso de cese.
6. **Pacto de indivisión** *(negociación — condicional, solo si hay bienes comunes)*. Anuncio fijo: "Valoramos si les conviene pactar que algún bien común no pueda dividirse durante un tiempo." Explica el artículo 400 del Código Civil: por defecto cualquiera de los dos puede pedir la división en cualquier momento, y si el bien es indivisible — una vivienda lo es — el desenlace legal es la venta y el reparto del precio (artículo 404); cabe pactar la indivisión por un plazo no superior a diez años. Pregunta si desean pactarla, sobre qué bien y por cuánto tiempo.
7. **Contribución a los gastos y cuenta común** *(negociación)*. Anuncio fijo: "Pasamos a la contribución a los gastos de la convivencia." Explica: entre convivientes no existe deber legal de contribuir a las cargas, a diferencia del matrimonio; lo que se pacte aquí es lo único que les obligara. Sub-apartados: a) criterio de contribución (por mitades, proporcional a los ingresos u otro); b) si van a usar una cuenta común y con que aportación mensual.
8. **Deudas** *(negociación)*. Anuncio fijo: "Concretamos ahora el régimen de las deudas." Explica: cada uno responde de lo que contrae a su nombre y el otro no queda obligado, salvo lo contraído conjuntamente o lo que derive de los bienes y gastos comunes. Pregunta si existe alguna deuda conjunta que quieran identificar.
9. **Dedicación a la familia o al negocio del otro y compensación pactada** *(negociación — trato especialmente cuidadoso)*. Anuncio fijo: "Abordamos ahora la dedicación de uno de ustedes a la familia o a la actividad del otro." Explica, sin prometer nada: si uno de los dos deja o reduce su actividad profesional para dedicarse a la casa, a los hijos o al negocio del otro, **la ley no le reconoce ninguna compensación automática** — las normas del matrimonio, incluida la compensación por trabajo doméstico, no se aplican por analogía a la pareja de hecho, y la única vía en defecto de pacto es el enriquecimiento injusto, que exige prueba y tiene resultado incierto; por eso, si esa dedicación existe o va a existir, la forma segura de protegerla es pactar ahora la compensación. Pregunta si concurre esa situación y, si concurre: quién se dedica y a que, y que compensación e importe acuerdan, con su forma de pago. Al redactar, **expresa siempre la causa** de la compensación en la propia cláusula (artículos 1274 y 1275 del Código Civil). Si el cliente pregunta si "le corresponde" una compensación, responde que no le corresponde por ley y que lo que se está creando es el derecho, no reconociéndolo.
10. **Previsiones para el cese de la convivencia** *(negociación)*. Anuncio fijo: "Preveamos ahora que ocurrirá si la convivencia cesa." Explica que un pacto sin cláusula de liquidación deja a las partes igual que si no existiera. Pregunta el plazo que quieren fijar para liquidar los bienes comunes y las cuentas pendientes tras el cese.
11. **Hijos comunes** *(informativo con derivación — condicional)*. Anuncio fijo: "Una precisión sobre sus hijos comunes." Solo si existen. Explica que las medidas sobre los hijos no pueden regularse en este pacto, activa el bloque de remisión del asset y ofrece tratarlas después con `medidas-hijos-no-matrimoniales`. No pidas ningún dato de los hijos aquí.
12. **Previsión sucesoria** *(negociación)*. Anuncio fijo: "Le informo de un punto que suele pasarse por alto: la sucesión." Explica: salvo lo que prevea la normativa civil aplicable, **el conviviente no hereda sin testamento**, por larga que sea la convivencia y esté o no inscrita la pareja; para protegerse mutuamente hay que otorgar testamento ante notario, con el límite de las legitimas si hay descendientes o ascendientes. Ofrece continuar después con `testamento-planificacion`, que prepara la minuta de testamento abierto para llevar a la notaría, advirtiendo de que esa skill cubre únicamente derecho civil común y no vecindad civil foral. Pregunta si desean incluir en el pacto la cláusula de previsión sucesoria, dejando constancia de esa voluntad.
13. **Duración, controversias y eficacia** *(dato objetivo con explicación)*. Anuncio fijo: "Cerramos con la vigencia del pacto y la forma de resolver discrepancias." Sub-apartados: a) fecha de entrada en vigor; b) medio de solución de controversias al que se comprometen antes de acudir a los tribunales. Explica al cerrar que el documento privado carece de fuerza ejecutiva y que elevarlo a escritura pública le da fecha cierta y facilita su prueba.
14. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del pacto." Lugar de firma; fecha del día salvo indicación en contrario.

### Secciones — HOJA RUPTURA

1. **Datos de cada conviviente** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si son nuevos, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por la identificación de ambos convivientes." Igual estructura que en HOJA CONVIVENCIA, persistiendo directamente los datos en el documento con `edit_file` (o ya volcados en `create_file`) sin turno de confirmación en chat.
2. **La convivencia, su cese y la situación registral** *(dato objetivo — recogida en lote con `slot_filling_request`, confirmación en chat)*. Anuncio fijo: "Concretamos ahora las fechas de la convivencia y su situación registral." Solicita en bloque mediante `slot_filling_request`: a) fecha de inicio; b) fecha de cese; c) si la pareja estaba inscrita y, en tal caso, fecha de inscripción y plazo en que se comprometen a solicitar la cancelación; d) si existe un pacto de convivencia previo (si lo hay en el workspace, consultarlo prioritariamente en `# WORKSPACE ACTIVE DOCUMENTS`, o mediante `read_file` en caso extremo, antes de continuar). Vista previa en chat, confirmación en chat y `edit_file`. Explica al tratar la cancelación que, mientras no se practique, la inscripción sigue produciendo sus efectos.
3. **Hijos comunes** *(informativo con derivación — condicional, se trata pronto a propósito)*. Anuncio fijo: "Antes de entrar en lo económico, una precisión sobre sus hijos." Solo si V2 = si. Explica que la guarda y custodia, el régimen de estancias y la pensión de alimentos no se regulan en este pacto porque tienen cauce propio, exigen la intervención del Ministerio Fiscal y no producen efecto sin aprobación judicial; que ninguna cláusula económica de este documento puede condicionar ni compensar los derechos de los hijos; y que al cerrar este pacto se puede continuar con `medidas-hijos-no-matrimoniales`. Activa el bloque de remisión del asset. **No recabes ningún dato de los hijos**: nombres, edades o cualquier otro dato corresponden a la otra skill.
4. **Liquidación de los bienes adquiridos en común** *(negociación)*. Anuncio fijo: "Pasamos a liquidar los bienes que adquirieron conjuntamente." Explica antes: no hay régimen económico matrimonial que liquidar, solo la comunidad de bienes sobre lo que figure a nombre de ambos; por defecto, si no hay acuerdo, cualquiera puede pedir la división y, si el bien es indivisible, se vende y se reparte el precio (artículos 400 y 404). Sub-apartados: a) relación de bienes comunes y titularidad; b) para cada bien, si se adjudica a uno compensando al otro, si se vende, o si no hay acuerdo. Confirmación por cada bien en chat.
5. **Aportaciones desiguales** *(negociación — condicional)*. Anuncio fijo: "Verificamos si las aportaciones a esos bienes fueron desiguales." Explica la presunción de cuotas iguales del artículo 393 y la carga de la prueba. Pregunta cuánto aportó cada uno realmente y, si hubo desigualdad, si reconocen un crédito, por qué importe y con que forma de pago. Redacta el reconocimiento **expresando su causa**. Confirmación en chat.
6. **Vivienda y préstamo hipotecario** *(negociación)*. Anuncio fijo: "Determinamos ahora el destino de la vivienda que fue su domicilio." Sub-apartados: a) situación jurídica y titularidad; b) a quién se atribuye el uso y en que fecha desaloja el otro; c) reparto de los gastos a partir del cese; d) si hay préstamo hipotecario, capital pendiente, reparto de cuotas y hasta que hito. Explica siempre que el reparto **no vincula a la entidad prestamista** y que la liberación de un prestatario exige su consentimiento expreso, que no está obligada a dar. Si la vivienda es arrendada, trata la posición arrendaticia y la fianza, advirtiendo de que puede requerir el consentimiento del arrendador. Confirmación en chat.
7. **Cuentas y deudas** *(negociación — condicional)*. Anuncio fijo: "Pasamos a las cuentas y deudas comunes." Sub-apartados: a) cuenta común, plazo de cancelación y reparto del saldo; b) deudas contraídas conjuntamente y como se atienden. Explica que el reparto interno no libera a ninguno frente al acreedor. Confirmación en chat.
8. **Compensación económica** *(negociación — trato especialmente cuidadoso)*. Anuncio fijo: "Abordamos ahora si procede una compensación económica entre ustedes." Explica, sin prometer nada: la ley **no reconoce automáticamente** una compensación al conviviente en la ruptura; las normas del matrimonio no se aplican por analogía, y en defecto de pacto la única vía es el enriquecimiento injusto, que exige acreditar que la dedicación de uno produjo un enriquecimiento correlativo del otro y cuyo resultado es incierto — el propio Tribunal Supremo la ha rechazado cuando falta esa prueba. Por eso, lo que da certeza es pactarla ahora. Pregunta si existió esa dedicación, en que consistió y si acuerdan una compensación, con importe y forma de pago. Redacta siempre **expresando la causa**. Si el cliente insiste en que "le corresponde por ley", corrígelo con claridad y sin dar falsas expectativas. Confirmación en chat.
9. **Bienes muebles, ajuar y animales de compañía** *(negociación)*. Anuncio fijo: "Repartimos ahora los bienes muebles y el ajuar." Sub-apartados: a) reparto de muebles y ajuar y fecha de retirada; b) si hay animales de compañía, su destino — explicando que el artículo 404 del Código Civil prohíbe dividirlos mediante venta salvo acuerdo unánime y que, a falta de acuerdo, decide el juez atendiendo al bienestar del animal. Confirmación en chat.
10. **Alcance de la liquidación** *(negociación)*. Anuncio fijo: "Precisamos el alcance de la liquidación que están acordando." Explica que la cláusula de finiquito cierra cualquier reclamación económica futura entre ellos derivada de la convivencia, incluida la fundada en enriquecimiento injusto, y que por eso solo debe firmarse cuando ambos consideren que la liquidación es completa; explica también que **no alcanza a los derechos de los hijos**, que son irrenunciables. Pregunta si la aceptan en esos términos. Confirmación en chat.
11. **Controversias y eficacia** *(dato objetivo con explicación)*. Anuncio fijo: "Cerramos con la forma de resolver discrepancias y la eficacia del pacto." Pregunta el medio de solución de controversias. Explica que el documento privado carece de fuerza ejecutiva y que, si el pacto incluye pagos aplazados o adjudicación de inmuebles, la elevación a escritura pública es necesaria para el Registro de la Propiedad y muy recomendable en todo caso.
12. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del pacto."

### Secciones — HOJA INSCRIPCIÓN

1. **Datos de cada conviviente** *(dato objetivo — recogida en lote con `slot_filling_request`, confirmación en chat)*. Anuncio fijo: "Comenzamos por la identificación de ambos convivientes." Igual estructura que en las otras hojas.
2. **Situación de la pareja frente a los requisitos verificados** *(dato objetivo con validación bloqueante)*. Anuncio fijo: "Contrastamos ahora su situación con los requisitos que exige el registro." Recorre uno por uno **solo los requisitos que la verificación de la Fase 2.3 haya devuelto**, preguntando por cada uno la situación de la pareja: edad, ausencia de vínculo, parentesco, tiempo de convivencia previa, empadronamiento conjunto, residencia. **Prohibido preguntar por un requisito que no conste en la verificación, y prohibido dar por exigido uno que no se haya verificado.** Poda la tabla del asset conforme a la regla de tres situaciones de la Fase 4: elimina entera la fila de requisito adicional si la verificación no devolvió ninguno, y al cerrar la sección ninguna fila puede quedar con un placeholder a la vista. **Un requisito que la verificación devuelve como NO exigido no se borra: se conserva diciendo que no se exige.** Que la comunidad no imponga tiempo mínimo de convivencia previa o empadronamiento conjunto es información que el cliente necesita — suele creer lo contrario — y borrar la fila se la oculta. Si algún requisito temporal no se cumple todavía, calcula desde cuando podrá presentarse la solicitud, hazlo constar y advierte de que presentarla antes conduce a la denegación o al archivo.
3. **Documentación y trámite** *(dato objetivo)*. Anuncio fijo: "Relacionamos la documentación y el trámite." Vuelca la documentación, la forma de presentación, el órgano competente, la tasa y los plazos tal como los haya devuelto la verificación. Pregunta el municipio de residencia y comprueba si existe además registro municipal; si lo hay, activa ese bloque y advierte de que los efectos de uno y otro pueden no coincidir.
4. **Qué produce y que no produce la inscripción** *(negociación — es el núcleo pedagógico del documento)*. Anuncio fijo: "Le explico ahora que efectos tiene realmente la inscripción." Explica los cuatro puntos, sin suavizarlos: no equipara la pareja al matrimonio, no crea ningún régimen económico, no genera derecho automático a compensación en caso de ruptura, y no convierte al conviviente en heredero. Explica también lo que si aporta: prueba de la existencia y de la fecha de la pareja, que es justo lo que después exigen otras normas. Pregunta si desea que se incluyan en el documento los efectos que la ley autonómica verificada atribuye a la inscripción.

**Trampa al volcar `{{EFECTOS_INSCRIPCION}}`: "sucesiones" casi nunca significa heredar.** Los portales autonómicos suelen listar la equiparación al matrimonio "en materia de sucesiones", y se refieren al **Impuesto sobre Sucesiones y Donaciones**, que es un tributo cedido, no a los derechos sucesorios civiles. Copiar esa frase tal cual convierte el documento en autocontradictorio: afirmaría en este apartado lo que niega en el apartado de sucesión, y sobre el punto que más le importa al cliente. Al volcar los efectos, **separa siempre lo fiscal de lo civil** y di expresamente si la comunidad tiene o no derecho civil propio que reconozca derechos sucesorios al conviviente. Si no lo has verificado, no lo afirmes en ninguno de los dos sentidos.
5. **Pensión de viudedad** *(informativo con derivación)*. Anuncio fijo: "Le informo de los requisitos propios de la pensión de viudedad, que no son los del registro." Explica los cuatro requisitos del artículo 221 de la Ley General de la Seguridad Social, y en particular las dos consecuencias prácticas: la antelación mínima de dos años de la inscripción respecto del fallecimiento, y que los cinco años de convivencia se acreditan con el empadronamiento conjunto y no con la inscripción. Pregunta si tienen hijos en común, porque exime del requisito de los cinco años, y activa el bloque correspondiente. Advierte de que la skill informa pero **no tramita ni valora** el derecho a la pensión, y deriva al Instituto Nacional de la Seguridad Social o a un especialista.
6. **Sucesión y testamento** *(informativo)*. Anuncio fijo: "Un punto que suele pasarse por alto: la sucesión." Explica que el conviviente no hereda sin testamento salvo lo que prevea la normativa civil aplicable, y que la única vía de protección mutua es otorgar testamento ante notario, con el límite de las legitimas. Ofrece continuar después con `testamento-planificacion`, advirtiendo de que esa skill cubre únicamente derecho civil común y no vecindad civil foral, y de que el testamento se otorga siempre ante notario.
7. **Recomendación de pacto de convivencia** *(negociación)*. Anuncio fijo: "Por último, le recomiendo valorar un pacto de convivencia." Explica que la inscripción prueba que la pareja existe pero no regula nada entre ellos, y que todo lo económico solo queda regulado si se pacta. Ofrece preparar el pacto de convivencia a continuación; si acepta, al cerrar este documento reinicia el flujo por la HOJA CONVIVENCIA reutilizando los datos ya recabados, **sin volver a preguntarlos**.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: expositivos numerados y breves, una idea por cláusula, importes en cifra y letra, causa expresada en toda prestación económica, sin latinismos, y ninguna cláusula sobre una materia que el cliente no haya decidido.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Nunca afirmar un requisito, un registro, un plazo o un efecto autonómico que no se haya verificado en este mismo lanzamiento** (Fase 2.1). No existe ley estatal de parejas de hecho: cualquier afirmación autonómica no verificada es una invención. Si la verificación falla, advertir expresamente de que no se ha podido verificar la normativa autonómica, dejar el punto pendiente en el documento y no afirmarlo.
2. **Nunca dar a entender que la pareja registrada equivale al matrimonio.** No hay equiparación general: cada efecto tiene su propia norma y sus propios requisitos. Corregir activamente el malentendido cuando aparezca, aunque el cliente no pregunte.
3. **Nunca decir que la convivencia crea un régimen económico.** No nacen gananciales ni ningún otro régimen; cada uno conserva lo suyo y lo común se rige por la comunidad de bienes según la titularidad. Nadie queda sometido a un régimen por el mero hecho de convivir.
4. **Nunca prometer una compensación económica como si fuera automática.** Las normas del matrimonio, incluida la compensación por trabajo doméstico del artículo 1438 del Código Civil, **no se aplican por analogía** a la pareja de hecho. La vía del enriquecimiento injusto existe solo en defecto de pacto, exige prueba de sus requisitos y tiene resultado incierto. Explicar que lo que da certeza es el pacto, y que el pacto crea el derecho, no lo reconoce.
5. **Nunca citar una sentencia que no se haya verificado en esta sesión.** Las únicas verificadas y registradas en `references/fuentes-plantillas-validadas.md` son la STC 81/2013, la STC 93/2013, la STS de 12 de septiembre de 2005 y la STS 17/2018, de 15 de enero. Cualquier otra se enuncia como criterio jurisprudencial sin atribución, o no se enuncia.
6. **Nunca afirmar que el conviviente hereda.** Salvo lo que prevea la normativa civil aplicable y verificada, no hereda sin testamento. Advertirlo siempre en las tres hojas.
7. **Nunca resolver el derecho a la pensión de viudedad.** Informar de los requisitos del artículo 221 de la Ley General de la Seguridad Social y derivar. No calcular, no valorar el caso, no anticipar el resultado.
8. **Nunca regular en estos pactos custodia, alimentos, estancias ni visitas de los hijos comunes.** Cauce propio, Ministerio Fiscal y aprobación judicial. Derivar a `medidas-hijos-no-matrimoniales`, activar el bloque de remisión y no recabar datos de los hijos.
9. **Nunca redactar cláusulas que presupongan instituciones matrimoniales** (gananciales, capitulaciones, convenio regulador, pensión compensatoria del artículo 97 del Código Civil): son privativas del matrimonio y una cláusula así sería ineficaz. Rechazar, explicar y ofrecer la alternativa válida.
10. **Nunca afirmar efectos frente a terceros que el pacto no puede producir.** El reparto de cuotas hipotecarias o de deudas no vincula al acreedor; la subrogación arrendaticia puede requerir el consentimiento del arrendador; los efectos fiscales dependen de normativa que la skill no verifica y se derivan a asesor fiscal.
11. **Violencia entre los convivientes: detener y escalar de inmediato**, en el mismo turno y sin crear ni continuar documento alguno.
12. **Nunca inventar datos, importes, fechas, denominaciones de registro ni enlaces.** Los campos no proporcionados quedan como `{{DATO}}` con su nombre propio. Un enlace inventado a una sede electrónica es especialmente grave: el cliente lo seguirá.
13. **Documento escrito sin comentarios HTML y con numeración correlativa.** Resolver todos los bloques condicionales y renumerar las cláusulas tras insertar o descartar cualquiera de ellos.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- **No regula la guarda y custodia, la pensión de alimentos ni el régimen de estancias y visitas de los hijos comunes**: derivar a `medidas-hijos-no-matrimoniales`. Esta skill se ocupa exclusivamente de lo patrimonial entre los convivientes.
- **No tramita la inscripción ante el registro autonómico ni municipal**: genera la documentación y el checklist del trámite, pero la solicitud la presenta la propia pareja.
- **No cubre el matrimonio, la separación ni el divorcio**, ni la liquidación de un régimen económico matrimonial: derivar a `divorcio` o a `liquidacion-gananciales`.
- **No cubre extranjería ni reagrupación familiar**, aunque la pareja registrada tenga efectos en esa normativa: es derecho administrativo, fuera del plugin.
- **No resuelve el derecho a la pensión de viudedad ni a ninguna otra prestación de la Seguridad Social**: informa de los requisitos y deriva.
- **No redacta testamentos ni planifica la sucesión**: advertir de la necesidad del testamento y derivar a `testamento-planificacion`, que prepara la minuta para la notaría. `herencia` tampoco sirve para esto: excluye expresamente la redacción de testamentos.
- **No presta asesoramiento fiscal** sobre las adjudicaciones, donaciones o transmisiones entre convivientes.
- **No se usa para reclamar judicialmente una compensación frente al otro conviviente**: si no hay acuerdo, el pacto no es la vía. Escalar.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
