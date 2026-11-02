---
name: medidas-hijos-no-matrimoniales
title: Medidas sobre hijos no matrimoniales
i18n:
  en:
    name: measures-for-children-of-unmarried-parents
    title: Measures for children of unmarried parents
    description: >
      Generates the documents to SET FOR THE FIRST TIME the measures concerning the minor
      children of parents who are not and have never been married to each other (registered and
      unregistered couples and parents who never lived together), in the proceedings of Article
      748.4 of the **Civil Procedure Act (LEC)**, which governs family proceedings on minors,
      through two routes: (1) WITH AGREEMENT, a family relations agreement governing parental
      authority (Arts. 154 and 156 of the **Civil Code**), custody (Art. 92 CC), contact and
      visiting arrangements (Art. 94 CC), child maintenance (Arts. 93, 142, 146 and 148 CC) and
      use of the home, for court approval under Article 777 LEC; and (2) WITHOUT AGREEMENT, a
      petition for parental measures under the summary procedure of Article 770 LEC, with proof
      of the MASC attempt and mandatory intervention of the Public Prosecutor. It verifies the
      version in force in the BOE before drafting. Do not use between spouses (that is divorce
      or separation), to modify measures already set, for determination or challenge of
      parentage, for claiming unpaid maintenance or international relocation of the child, and
      it stops and escalates where there are indications of gender or domestic violence.
description: >
  Genera los documentos para FIJAR POR PRIMERA VEZ las medidas relativas a los hijos menores comunes
  de progenitores que no están ni han estado casados entre si (parejas de hecho registradas, parejas
  no registradas y progenitores que nunca convivieron), en el proceso del artículo 748.4.º de la **Ley
  de Enjuiciamiento Civil**, que regula los procesos de familia sobre menores, en sus dos vías: (1) CON ACUERDO — pacto de relaciones familiares que
  regula el ejercicio de la patria potestad (arts. 154 y 156 del **Código Civil**, CC), la guarda y custodia (art. 92 CC),
  el régimen de estancias, comunicación y visitas (art. 94 CC), la pensión de alimentos (arts. 93,
  142, 146 y 148 CC) y, en su caso, el uso de la vivienda en que residen los hijos, para su
  sometimiento a aprobación judicial por el cauce del artículo 777 de la LEC; y (2) SIN ACUERDO —
  demanda de medidas paternofiliales por los trámites del juicio verbal del artículo 770 de la LEC,
  con acreditación del intento de MASC (art. 5 LO 1/2025) e intervención preceptiva del Ministerio
  Fiscal (art. 749.2 LEC). Verifica la versión vigente de las normas en el BOE antes de redactar.
  NO usar entre cónyuges (eso es divorcio o separación), NO usar para modificar medidas ya fijadas,
  NO cubre la determinación ni la impugnación de la filiación, NO cubre la reclamación de pensiones
  impagadas ni el traslado internacional del menor, y se detiene y escala si existen indicios de
  violencia de género o doméstica.
when_to_use: |
  - Una pareja de hecho con hijos comunes se separa y necesita fijar custodia, estancias y alimentos.
  - Dos progenitores que nunca estuvieron casados no tienen ninguna medida judicial sobre sus hijos
    y quieren regularla, con acuerdo o sin él.
  - El usuario quiere reclamar al otro progenitor la pensión de alimentos de un hijo común cuando no
    hay sentencia ni convenio previo que la fije.
  - El usuario quiere que se le atribuya la guarda y custodia de su hijo, o un régimen de estancias,
    sin que haya habido matrimonio con el otro progenitor.
  - El usuario tiene un acuerdo con el otro progenitor y quiere darle validez y fuerza ejecutiva
    sometiéndolo a la aprobación del Juzgado.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - filiacion: determinada respecto de ambos progenitores / no determinada respecto del otro / se desconoce
  - acuerdo: existe acuerdo con el otro progenitor / no existe acuerdo
  - medidas: guarda y custodia con régimen de estancias / pensión de alimentos / ambas
  - atribucion_vivienda: se solicita la atribución del uso de la vivienda en que residen los hijos (sí / no)
  - convivencia: pareja de hecho inscrita en registro / convivencia sin inscripción / sin convivencia estable
  - alcance: solo el pacto de relaciones familiares / pacto y demanda conjunta (solo en la vía de acuerdo)
  - datos_progenitor_a: nombre, DNI o NIE, domicilio
  - datos_progenitor_b: nombre, DNI o NIE, domicilio
  - datos_hijos: nombre y fecha de nacimiento de cada hijo (únicos datos de menores que se recaban)
  - patria_potestad: decisiones que requerirán el acuerdo de ambos y vía de comunicación entre progenitores
  - custodia_estancias: modalidad de guarda, calendario de estancias, reparto de vacaciones y lugar de entregas
  - pension_alimentos: importe por hijo, día de pago, cuenta, actualización y reparto de gastos extraordinarios
  - vivienda_datos: dirección, titularidad, atribución del uso y plazo o condición de cese
  - masc: en la vía contenciosa, tipo y fechas del intento de MASC o motivo de imposibilidad
  - documentacion_economica: documentos que acreditan la situación económica (regla 1.ª del art. 770 LEC)
  - medidas_provisionales: en la vía contenciosa, si se interesan
  - partido_judicial: competencia del art. 769.3 LEC
outputs:
  - pacto_relaciones_familiares: pacto de relaciones familiares en markdown, DRAFT
  - demanda_medidas_paternofiliales: >
      demanda conjunta de mutuo acuerdo o demanda contenciosa de medidas paternofiliales en markdown, DRAFT (un mismo asset con dos variantes condicionales)
references:
  - references/cc-medidas-hijos-no-matrimoniales.md
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/lec-proceso-medidas-paternofiliales.md
assets:
  - assets/template-demanda-medidas-paternofiliales.md
  - assets/template-pacto-relaciones-familiares.md
---

# Fijar las Medidas Relativas a los Hijos de Progenitores no Casados

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
      "id": "filiacion",
      "rationale": "Resolver V1: sin filiación determinada respecto de ambos progenitores no cabe fijar medidas, y el proceso se detiene.",
      "question": "¿Está determinada legalmente la filiación respecto de ambos progenitores?",
      "options": [
        {"id": "ambos", "label": "Sí, respecto de ambos"},
        {"id": "solo_uno", "label": "No, no consta respecto del otro progenitor"},
        {"id": "desconocido", "label": "No lo sé con certeza"}
      ]
    },
    {
      "id": "acuerdo",
      "rationale": "Resolver V2: el acuerdo genera pacto de relaciones familiares y su ausencia la demanda de medidas paternofiliales.",
      "question": "¿Hay acuerdo con el otro progenitor?",
      "options": [
        {"id": "con_acuerdo", "label": "Sí, hay acuerdo"},
        {"id": "sin_acuerdo", "label": "No hay acuerdo"}
      ]
    },
    {
      "id": "medidas",
      "rationale": "Resolver V3: activa los bloques condicionales de custodia y estancias, de alimentos y de vivienda dentro de la hoja elegida.",
      "question": "¿Qué medidas deben fijarse?",
      "options": [
        {"id": "ambas", "label": "Guarda y custodia con régimen de estancias, y pensión de alimentos"},
        {"id": "solo_custodia", "label": "Solo guarda y custodia con régimen de estancias"},
        {"id": "solo_alimentos", "label": "Solo pensión de alimentos"}
      ]
    },
    {
      "id": "convivencia",
      "rationale": "Resolver V4: determina la variante del expositivo de convivencia y, si la pareja está inscrita, el documento acreditativo del registro.",
      "question": "¿Cuál era la situación de convivencia de los progenitores?",
      "options": [
        {"id": "pareja_inscrita", "label": "Pareja de hecho inscrita en registro"},
        {"id": "convivencia_sin_inscripcion", "label": "Convivencia estable sin inscripción"},
        {"id": "sin_convivencia", "label": "Sin convivencia estable"}
      ]
    },
    {
      "id": "alcance",
      "rationale": "Resolver V5: determina si además del pacto se redacta la demanda conjunta para su aprobación judicial.",
      "question": "Si hay acuerdo, ¿qué alcance tiene el encargo?",
      "show_if": {"question_id": "acuerdo", "option_ids": ["con_acuerdo"]},
      "options": [
        {"id": "solo_pacto", "label": "Solo el pacto de relaciones familiares"},
        {"id": "pacto_y_demanda", "label": "El pacto y la demanda conjunta para su aprobación judicial"},
        {"id": "no_procede", "label": "No procede: no hay acuerdo (vía contenciosa)"}
      ]
    },
    {
      "id": "atribucion_vivienda",
      "rationale": "Resolver V6: la atribución del uso de la vivienda en que residen los hijos es un bloque propio, distinto de la custodia y de los alimentos, y solo se redacta si se pretende.",
      "question": "¿Debe regularse también la atribución del uso de la vivienda en que residen los hijos?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `filiacion`
- `V2` — `acuerdo`
- `V3` — `medidas`
- `V4` — `convivencia`
- `V5` — `alcance`
- `V6` — `atribucion_vivienda`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalúa **en este orden**:

- Si **V1 = solo_uno o desconocido** (o no ha podido acreditarse) → **DETENER. No crear ningún documento y no pedir ningún otro dato.** Emite el texto fijo del Guardrail 1 y ofrece escalación. Sin filiación determinada no existe patria potestad del otro progenitor, ni deber de alimentos exigible frente a el (arts. 143.2.º y 154 CC), ni sujeto pasivo de las medidas: el proceso previo y necesario es el de determinación de la filiación (art. 748.2.º LEC), que esta skill no cubre.
- Si en cualquier momento aparecen indicios de violencia de género o doméstica → **DETENER** (Guardrail 3). No crear documento.
- Si **V2 = con_acuerdo** → **HOJA ACUERDO**: `assets/template-pacto-relaciones-familiares.md`. Si además V5 = pacto_y_demanda, se genera después `assets/template-demanda-medidas-paternofiliales.md` con los bloques condicionales de acuerdo ACTIVADOS y los de contencioso DESACTIVADOS.
- Si **V2 = sin_acuerdo** → **HOJA CONTENCIOSA**: `assets/template-demanda-medidas-paternofiliales.md` con los bloques condicionales de contencioso ACTIVADOS (intento de MASC, situación económica de la regla 1.ª del art. 770, apartado de medidas solicitadas, otrosíes de prueba y de medidas provisionales) y los de acuerdo DESACTIVADOS. No se genera pacto de relaciones familiares: es propio de la vía de acuerdo.
- V3 no elige asset: activa o desactiva los bloques de custodia y estancias y de alimentos dentro de la hoja ya elegida. V6 activa o desactiva el bloque de uso de la vivienda.
- V4 no elige asset: activa una de las tres variantes del expositivo de convivencia y, solo si V4 = pareja_inscrita, el Documento nº 2 con la certificación del registro de parejas de hecho.
- Si lo que se pretende es **modificar medidas ya fijadas** en sentencia o en un acuerdo aprobado judicialmente → **DETENER esta vía** y derivar a `modificacion-medidas`, explicando que lo que procede es una demanda de modificación de medidas y no la fijación por primera vez.
- Si los progenitores **están o han estado casados entre si** → **DETENER esta vía** y derivar a `divorcio`.
- Si lo que se reclama son **pensiones ya fijadas e impagadas** → **DETENER esta vía** y derivar a `ejecucion-titulos`.
- Si se pretende la **determinación o impugnación de la filiación**, el **traslado internacional del menor** o medidas de protección frente a un **riesgo actual** para el menor → **DETENER** y escalar (ver tabla de Escalación).
- **Requisito de procedibilidad (Ley Orgánica 1/2025).** Si el intento previo de un medio adecuado de solución de controversias no está acreditado y esta skill no genera por sí misma el documento que lo acredita, **deriva a `masc-acuerdos`**, que produce el requerimiento de negociación, el acta del intento, la oferta vinculante, el acuerdo transaccional y la declaración responsable de imposibilidad. Ofrece encadenar con ella antes de continuar, y advierte de que sin ese documento la demanda no se admite a trámite.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **Minoría de edad de los hijos (art. 748.4.º LEC):** el proceso versa sobre hijos MENORES. Si todos los hijos son ya mayores de edad, esta vía no procede: los alimentos del hijo mayor se reclaman por el cauce que corresponda y la guarda y custodia carece de objeto. Advertir y escalar. Si hay hijos menores y además hijos mayores sin ingresos que convivan, incluir solo a los menores en las medidas y advertir de que los alimentos del mayor tienen fundamento distinto (art. 93, párrafo 2.º, CC) y conviene revisión por especialista.
- **Objeto exclusivo (art. 748.4.º LEC):** el proceso debe versar **exclusivamente** sobre guarda, custodia y alimentos de los hijos menores. Si el usuario quiere acumular la división de un inmueble común, una reclamación de cantidad entre los progenitores o cualquier pretensión patrimonial entre ellos, separarla expresamente: advertir de que no cabe en este procedimiento y ofrecer la vía propia o la escalación. La atribución del uso de la vivienda en que residen los hijos si se admite en la práctica cuando se funda en el interés del menor: se recoge con la advertencia de la sección correspondiente.
- **Pensión compensatoria:** si el usuario la pide, **rechazar la instrucción** y explicar que el art. 97 CC es privativo del matrimonio y no cabe en este procedimiento. No incluirla en ningún documento. Si alega un desequilibrio económico grave derivado de la convivencia, ofrecer escalación: es una pretensión distinta y de fundamento propio.
- **MASC (art. 5.2 LO 1/2025) — solo en la HOJA CONTENCIOSA:** es requisito de procedibilidad. La guarda, la custodia y los alimentos de hijos menores **no** figuran entre las materias exceptuadas de las letras a) a h) del art. 5.2. Verificar si se intento; si no se intento y no concurre imposibilidad, advertir formalmente del riesgo de inadmisión antes de continuar. En la HOJA ACUERDO no se pregunta por el MASC: no hay controversia que negociar.
- **Fecha de efectos de los alimentos (art. 148 CC):** los alimentos no se abonan sino desde la interposición de la demanda. Si el usuario pide mensualidades anteriores, advertirle de que por esta vía no se obtienen y no incluir retroactividad en la medida.
- **Cuenta de abono:** si el importe de la pensión se fija sin cuenta de abono o sin día de pago, la medida es difícilmente ejecutable. No cerrar la sección de alimentos sin ambos datos, o dejarlos con su placeholder propio y advertirlo.
- **Custodia compartida sin acuerdo (art. 92.5 y 92.8 CC):** si V2 = sin_acuerdo y el usuario pide custodia compartida, advertir de que a instancia de una sola parte es excepcional (art. 92.8) y exige informe del Ministerio Fiscal y una fundamentación en que solo así se protege el interés del menor. No prometer su concesión.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 108, 110, 154, 92, 93 y 96 del Código Civil (igualdad absoluta de hijos matrimoniales y no matrimoniales, patria potestad, guarda y custodia, alimentos y vivienda), y Art. 770.6 de la LEC.
2. **Orientación Legal del Caso:**

**Informa la vía y la fuente aplicable.** Textos fijos por hoja:
   - **HOJA ACUERDO:** "A su caso corresponde un pacto de relaciones familiares que regule las medidas relativas a sus hijos comunes, conforme a los artículos 154, 156, 92, 93, 94, 142, 146 y 148 del Código Civil, y que se somete a la aprobación judicial en el proceso previsto en el artículo 748.4.º de la Ley 1/2000, de Enjuiciamiento Civil, por el cauce de su artículo 777. Al existir hijos menores de edad, la intervención del Ministerio Fiscal es preceptiva y este informará sobre los términos del pacto que les afecten (artículo 749.2 de la Ley de Enjuiciamiento Civil). Le advierto de que el pacto no queda aprobado por el hecho de firmarse ni de presentarse: hasta que lo apruebe el Juzgado por sentencia carece de fuerza ejecutiva. Puede consultar los textos oficiales en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - **HOJA CONTENCIOSA:** "A su caso corresponde una demanda de medidas paternofiliales en el proceso del artículo 748.4.º de la Ley 1/2000, de Enjuiciamiento Civil, que se sustancia por los trámites del juicio verbal conforme a su artículo 770, siendo competente el Juzgado que determina su artículo 769.3. Las medidas se fundan en los artículos 154, 156, 92, 93, 94, 142, 146 y 148 del Código Civil. Al existir hijos menores de edad, la intervención del Ministerio Fiscal es preceptiva (artículo 749.2 de la Ley de Enjuiciamiento Civil). Debe acreditarse el intento previo de un medio adecuado de solución de controversias: sin ese requisito la demanda puede ser inadmitida (artículo 5 de la Ley Orgánica 1/2025 y artículo 264.4.º de la Ley de Enjuiciamiento Civil). Puede consultar los textos oficiales en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763, https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 y https://www.boe.es/buscar/act.php?id=BOE-A-2025-76"
   - **En ambas hojas, añadir:** "Le confirmo que el hecho de que ustedes no hayan estado casados no altera en nada los derechos de sus hijos ni los deberes de ambos progenitores: se fija exactamente lo mismo que se fijaría en un divorcio en cuanto a los hijos. Lo único que no existe aquí es el vínculo matrimonial y, con él, ni régimen económico matrimonial que liquidar ni pensión compensatoria."

3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada **que ha resuelto el enrutamiento de la Fase 1.3** (menciónala por su denominación formal, sin mostrar rutas internas ni volcar su contenido). Si el enrutamiento asigno varios documentos, nómbralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada** ni la primera del inventario de la sección de assets.
4. **Elección de Plantilla Base:** Aplica el protocolo universal de `REG-AST-01` (`CLAUDE.md`), convocando en ese mismo turno el formulario interactivo `restricted_human_in_the_loop_request` para que el usuario elija entre la plantilla del sistema o aportar su propia minuta.

### 2.3 Manejo Determinista de la Elección
Aplica rigurosamente el protocolo de `REG-AST-01` (`CLAUDE.md`): si se selecciona `plantilla_sistema`, carga la plantilla oficial y avanza a la **Fase 3**; si se selecciona `plantilla_usuario`, requiere la minuta (si no consta ya en el chat), ejecuta el control de legalidad y avanza a la **Fase 3**.
---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

Aplica rigurosamente la directiva `REG-DOC-01` (ciclo de creación del documento base):
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

Recorre secuencialmente la lista que corresponda al documento activo (5-A pacto, 5-B demanda conjunta, 5-C demanda contenciosa). Por cada sección incompleta, aplica el Ciclo de Edición Incremental Global.

**Anuncio de sección y encadenamiento:** al terminar una sección y confirmar su edición en disco, emite en ese mismo turno el anuncio fijo de la sección que se abre y lanza de inmediato su formulario `slot_filling_request` (si es grupo de datos) o su planteamiento en chat (si es negociación). No pidas permiso para pasar de sección: informa y continúa. Los anuncios nombran la sección SUSTANTIVA del documento, nunca la mecánica interna. La vista previa y la confirmación siempre van en el chat.

**Marcas de cada sección.** Cada punto de las listas está marcado como *[dato objetivo]* o *[negociación]*:
- *[dato objetivo]*: se registra el valor, con validación de sentido. Los grupos de datos se recogen en lote con `slot_filling_request`.
- *[negociación]*: implica una decisión con consecuencias legales. **PRIMERO explica en el chat, de forma breve y con base en `references/cc-medidas-hijos-no-matrimoniales.md`, el régimen legal por defecto y las consecuencias de cada opción; DESPUÉS formula la pregunta.** Confirma que el cliente entiende y está de acuerdo antes de escribir. Estas secciones se debaten y confirman en el chat **una por una**, sin agrupación.

**Validación de sentido, no solo de formato:** razona si cada respuesta tiene sentido en el contexto. Una fecha de nacimiento futura, un DNI con forma de nombre, una pensión de 5 euros al mes o un régimen de estancias imposible de cumplir no se escriben en el documento: señala por qué no encaja y pide aclaración antes de continuar.

**Datos de menores:** de cada hijo se piden **únicamente el nombre y la fecha de nacimiento**. No preguntes ni escribas centro escolar, dirección del menor, datos de salud, ni ningún otro dato del menor, aunque el usuario los ofrezca espontáneamente. Si los ofrece, no los incorpores al documento.

### 5-A. Pacto de relaciones familiares (`pacto-relaciones-familiares.md`)

1. **Progenitores** *[dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si son nuevos, volcado directo a disco per REG-CLI-04]*. Anuncio de apertura: "Comenzamos por la identificación de ambos progenitores." Invoca `search_clients` prioritariamente. Si son nuevos, solicita en lote mediante `slot_filling_request` los datos identificativos (nombre completo, DNI o NIE, domicilio actual) de cada progenitor. Si son nuevos clientes, resuelve de inmediato `restricted_human_in_the_loop_request` (`REG-CLI-03`). Conforme a `REG-CLI-04`, vuelca de inmediato los datos al documento con `edit_file` (o ya volcados en `create_file`) de forma directa sin requerir confirmación en chat de los datos personales, sustituyendo exhaustivamente los nombres de los progenitores en todas sus apariciones a lo largo del documento (título/encabezado H1, comparecencia y firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones). Muestra un breve resumen de la comparecencia asentada en el chat y encadena con la siguiente sección.
2. **Hijos comunes** *[dato objetivo — recogida en lote con `slot_filling_request`, confirmación en chat]*. Anuncio: "Corresponde ahora identificar a los hijos comunes." Solicita de una vez vía `slot_filling_request` el nombre y fecha de nacimiento de cada hijo común (solo esos dos datos por hijo). Muestra vista previa del bloque de hijos en el chat y solicita confirmación antes de aplicar `edit_file`.
3. **Convivencia y su cese** *[dato objetivo]*. Anuncio: "Recogemos ahora los datos de la convivencia y de su cese, que se hacen constar únicamente como antecedente." V4 ya está resuelto: no lo vuelvas a preguntar. Si V4 = pareja_inscrita, solicita en lote vía `slot_filling_request`: (a) registro de parejas de hecho en que constaba la inscripción; (b) fecha de la inscripción; (c) fecha del cese de la convivencia. Si V4 = convivencia sin inscripción: (a) fecha aproximada de inicio de la convivencia; (b) fecha del cese. Si V4 = sin convivencia, la variante del expositivo se resuelve sola: no preguntes nada y pasa a la sección siguiente. Vista previa y confirmación en chat antes de `edit_file`.
4. **Patria potestad y su ejercicio** *[negociación]*. Anuncio: "Pasamos a la primera de las medidas: el ejercicio de la patria potestad." Explica antes de preguntar: la patria potestad corresponde a ambos progenitores por el hecho de la filiación y su ejercicio conjunto es la regla (art. 156 CC), **con independencia de a quién se atribuya la custodia**: son dos cosas distintas. Advierte del matiz del párrafo final del art. 156 CC: viviendo los progenitores separados, la ley prevé que la ejerza aquel con quien el hijo conviva, salvo atribución judicial del ejercicio conjunto, **por lo que conviene pactarlo expresamente**. Enumera las decisiones que requieren el acuerdo de ambos, y en particular el cambio del lugar de residencia habitual del menor (art. 154.3.º CC), y explica que los desacuerdos se resuelven por la vía del art. 156 CC. Después pregunta, en turnos separados: (a) si desea añadir alguna decisión concreta a la lista de las que requerirán acuerdo de ambos; (b) la vía de comunicación que pactan entre progenitores para los asuntos de los hijos.
5. **Guarda y custodia** *[negociación — solo si V3 incluye custodia]*. Anuncio: "Corresponde ahora determinar la guarda y custodia de los hijos." Explica antes de preguntar: no hay preferencia legal automática; la compartida requiere el acuerdo de ambos (art. 92.5 CC) y que exista una comunicación mínima entre los progenitores, que el juez valora expresamente (art. 92.6 CC); la exclusiva atribuye la convivencia a un progenitor y el otro conserva la patria potestad y un régimen de estancias (art. 94 CC). El criterio decisivo es el interés superior del menor (art. 92.2 CC), y el vínculo que unió a los progenitores es irrelevante para los derechos del hijo. Después pregunta la modalidad acordada.
6. **Régimen de estancias, comunicación y vacaciones** *[negociación — solo si V3 incluye custodia]*. Anuncio: "Fijada la custodia, corresponde concretar el régimen de estancias y comunicación." Explica antes de preguntar: la concreción es lo que evita futuros conflictos y ejecuciones; un régimen "amplio y flexible" garantiza un incidente. Pide días concretos, horas de inicio y fin, y a quién corresponde cada periodo en los años pares y en los impares. Después, en turnos separados: (a) calendario ordinario de estancias; (b) reparto de las vacaciones escolares; (c) lugar de entregas y recogidas y quién recoge y quién entrega; (d) régimen de comunicación telefónica o telemática con el progenitor con el que el hijo no se encuentre.
7. **Pensión de alimentos** *[negociación — solo si V3 incluye alimentos]*. Anuncio: "Pasamos a la pensión de alimentos de los hijos." Explica antes de preguntar: el deber de alimentos deriva de la filiación y existe igual sin matrimonio (art. 143.2.º CC); la cuantía es proporcionada al caudal o medios de quien los da y a las necesidades de quien los recibe (art. 146 CC), sin tarifa legal; las tablas orientadoras del CGPJ pueden servir de referencia no vinculante (https://www.poderjudicial.es/cgpj/es/Servicios/Utilidades/Calculo-de-pensiones-alimenticias/) **y, mientras el estado verificado en la Fase 2 siga siendo el de revisión, adviértelo expresamente para no remitir al cliente a una herramienta que no está operativa**; la pensión cubre los gastos ordinarios y previsibles, mientras los extraordinarios son los imprevisibles y no periódicos, que suelen repartirse al 50 % con comunicación y justificación previas y acuerdo previo si no son urgentes; conviene la actualización anual para que la pensión no se degrade; y **la pensión de los hijos menores no es renunciable ni negociable a la baja hasta hacerla irrisoria: un pacto así es dañoso para los hijos y no será aprobado**. Si la custodia acordada es compartida, usa la variante del asset prevista para ella (contribución de ambos a un fondo común o compensación por la diferencia de ingresos), no la de pago unidireccional. Después, en turnos separados: (a) importe mensual por hijo, o forma de contribución si la custodia es compartida; (b) día de pago y cuenta de abono; (c) criterio de actualización anual; (d) porcentaje de reparto de los gastos extraordinarios. Confirmación propia de cada uno.
8. **Uso de la vivienda en que residen los hijos** *[negociación — solo si V6 = si]*. Anuncio: "Corresponde ahora la atribución del uso de la vivienda en que residen los hijos." **Explica antes de preguntar, y hazlo con detalle porque es el punto que más confunde al cliente:** aquí no hay régimen económico matrimonial que liquidar; el art. 96 CC, que en los divorcios atribuye el uso al progenitor custodio, está redactado para los cónyuges y para los supuestos de nulidad, separación y divorcio, de modo que **no se aplica de forma directa**. Sin matrimonio, la vivienda se rige por las reglas ordinarias de la propiedad y de los contratos: si es privativa de un progenitor, es suya; si es de ambos en proindiviso, cualquiera puede pedir la división; si es de alquiler, por el contrato. Lo que si opera es el interés del menor, cuya necesidad de habitación forma parte de los alimentos (art. 142 CC), y por esa vía se invoca el criterio del art. 96.1 **por analogía**. Nunca afirmes que el progenitor no titular tiene derecho al uso por el solo hecho de tener la custodia. Si la vivienda es propiedad exclusiva del otro progenitor, advierte expresamente de que la atribución es una limitación de la facultad dispositiva del titular, de resultado incierto, y ofrece escalación antes de redactar la medida; pon sobre la mesa las alternativas: plazo cerrado en lugar de indefinido, compensación económica al titular, cuantificar la habitación dentro de la pensión, o venta o extinción del condominio si el inmueble es común. Después, en turnos separados: (a) dirección de la vivienda; (b) titularidad real; (c) a quién se atribuye el uso; (d) plazo o condición de cese; (e) reparto de los gastos derivados de la vivienda.
9. **Cierre del pacto** *[dato objetivo]*. Anuncio: "Cerramos el pacto con el lugar y la fecha de firma." Pregunta lugar y fecha de firma. La cláusula de sometimiento a la aprobación judicial se resuelve sola: no la preguntes.

### 5-B. Demanda conjunta de mutuo acuerdo (`demanda-medidas-paternofiliales.md`, solo si V5 = pacto_y_demanda)

Al crearla, vuelca sin volver a preguntar todos los datos ya recogidos en 5-A (progenitores, hijos, convivencia, fecha y lugar del pacto). Secciones pendientes:

1. **Juzgado competente** *[dato objetivo con explicación]*. Anuncio: "Pasamos a la demanda: en primer lugar, el Juzgado competente." Explica la regla del art. 769.3 LEC: es competente el Juzgado de Primera Instancia del último domicilio común de los progenitores y, si residen en distintos partidos judiciales, a elección del demandante, el del domicilio del demandado o el de la residencia del menor; el tribunal lo examina de oficio y no cabe pactar otro fuero (art. 769.4 LEC). Pregunta el partido judicial y el criterio por el que resulta competente. Si nunca existió domicilio común, adopta la posición conservadora del de la residencia del menor y explícalo.
2. **Situación actual de los hijos** *[dato objetivo con validación]*. Anuncio: "Recogemos brevemente la situación actual de los hijos." Pregunta con quién conviven los hijos en este momento y desde cuando. **No pidas ni escribas ningún otro dato del menor.**
3. **Representación procesal** *[dato objetivo — recogida con `slot_filling_request`, confirmación en chat]*. Anuncio: "Corresponde identificar la representación procesal." Solicita vía `slot_filling_request`: (a) nombre del procurador; (b) nombre del letrado. Si aún no están designados, cada uno queda con su propio placeholder del asset. Vista previa y confirmación en chat antes de `edit_file`.
4. **Costas y cierre** *[dato objetivo]*. Anuncio: "Cerramos la demanda con el pronunciamiento sobre costas, el lugar y la fecha." Explica que, presentándose de común acuerdo, lo habitual es no interesar condena en costas, y pregunta si desea ese pronunciamiento. Después, lugar y fecha. La relación de documentos (certificaciones literales de nacimiento, certificación del registro de parejas de hecho si V4 = pareja_inscrita, pacto firmado) se rellena sola según la clasificación: muéstrala en la vista previa sin preguntar.

### 5-C. Demanda contenciosa de medidas paternofiliales (`demanda-medidas-paternofiliales.md`)

1. **Progenitor demandante** *[dato objetivo — búsqueda prioritaria con `search_clients`, recogida con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04]*. Anuncio de apertura: "Procedemos a la identificación de la parte demandante." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: (a) nombre completo; (b) DNI o NIE; (c) domicilio. Si es nuevo cliente, resuelve de inmediato `restricted_human_in_the_loop_request` (`REG-CLI-03`). Conforme a `REG-CLI-04`, vuelca de inmediato a disco con `edit_file` (o ya volcado en `create_file`) sin requerir confirmación en chat de los datos de la parte.
2. **Progenitor demandado** *[dato objetivo — búsqueda prioritaria con `search_clients`, recogida con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04]*. Anuncio: "Identificada la parte demandante, pasamos a la parte demandada." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: (d) nombre completo; (e) DNI o NIE; (f) domicilio. Si se desconoce el domicilio, queda con su propio placeholder y afecta al MASC: se activa la declaración responsable del art. 264.4.º LEC (ver sección 4). Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca de inmediato a disco con `edit_file` sin turno de confirmación en chat per `REG-CLI-04`.
3. **Hijos comunes** *[dato objetivo — recogida en lote con `slot_filling_request`, confirmación en chat]*. Anuncio: "Corresponde identificar a los hijos comunes." Solicita de una vez vía `slot_filling_request` el nombre y fecha de nacimiento de cada hijo; solo esos dos datos. Muestra vista previa en el chat y pide confirmación. Con la fecha de nacimiento ya conocida, calcula tú mismo si algún hijo ha cumplido doce años e informa de que en ese caso será oído en todo caso (regla 4.ª del art. 770 LEC).
4. **Convivencia, cese e intento de solución extrajudicial** *[dato objetivo con advertencia]*. Anuncio: "Pasamos a los hechos: el cese de la convivencia y el intento de solución extrajudicial." Primero, según V4, los datos de la convivencia y su cese (mismos sub-apartados que en 5-A.3 vía `slot_filling_request`). Después explica el requisito de procedibilidad: el art. 5.2 de la LO 1/2025 exige acreditar el intento previo de un medio adecuado de solución de controversias en estos procesos, sin que la guarda, la custodia y los alimentos figuren entre las materias exceptuadas, y sin ese requisito la demanda puede ser inadmitida. Aclara que basta la actividad negociadora desarrollada directamente por las partes o entre sus abogados, y que debe existir identidad entre el objeto negociado y el del pleito. Pregunta si se intento (sí / no en la misma frase). Si sí: tipo de MASC y fechas de inicio y fin. Si no y se desconoce el domicilio del demandado o concurre otra imposibilidad: activa la declaración responsable del art. 264.4.º LEC y pregunta el motivo. Si no y no concurre imposibilidad: advierte formalmente del riesgo de inadmisión y recomienda intentarlo antes de presentar; si el cliente decide continuar, deja el bloque con su placeholder propio y la advertencia registrada. Vista previa y confirmación en chat.
5. **Riesgo de reconvención** *[negociación — informativo, no genera texto en el documento]*. Anuncio: "Antes de concretar las medidas, debo advertirle de un riesgo del procedimiento." Explica la regla 2.ª, letra d), del art. 770 LEC: la parte demandada puede reconvenir con la contestación pidiendo medidas que no se han solicitado en la demanda —por ejemplo, la custodia compartida frente a una demanda que solo pide alimentos— y el actor dispone de 10 días para contestarla. Pregunta si prevé que la otra parte formule esa pretensión y, en caso afirmativo, si desea pedir ya en la demanda las medidas correspondientes en lugar de dejar que el debate lo abra la contraparte. Registra la decisión para las secciones siguientes; si el cliente amplía las medidas solicitadas, actualiza V3 y activa los bloques correspondientes del asset.
6. **Situación actual de los hijos** *[dato objetivo con validación]*. Anuncio: "Recogemos la situación actual de los hijos." Pregunta con quién conviven en este momento y desde cuando, y si el otro progenitor mantiene contacto y con que frecuencia de hecho. **No pidas ni escribas ningún otro dato del menor.**
7. **Patria potestad** *[negociación]*. Anuncio: "Pasamos a la primera de las medidas que se solicitaran: el ejercicio de la patria potestad." Misma explicación que en 5-A.4, con el matiz de que aquí se **solicita** el ejercicio conjunto y la enumeración de decisiones que requerirán acuerdo de ambos. Pregunta si solicita el ejercicio conjunto y que decisiones desea que se reserven expresamente al acuerdo de ambos.
8. **Guarda, custodia y régimen de estancias solicitados** *[negociación — solo si V3 incluye custodia]*. Anuncio: "Corresponde concretar la guarda y custodia y el régimen de estancias que se solicitaran." Misma explicación que en 5-A.5 y 5-A.6, **añadiendo** que en la vía contenciosa la custodia compartida a instancia de una sola parte es excepcional y exige informe del Ministerio Fiscal y una fundamentación en que solo así se protege adecuadamente el interés del menor (art. 92.8 CC): no prometas su concesión. Después, en turnos separados: (a) modalidad de custodia que se solicita; (b) calendario de estancias propuesto; (c) reparto de vacaciones; (d) lugar de entregas y recogidas.
9. **Pensión de alimentos solicitada** *[negociación — solo si V3 incluye alimentos]*. Anuncio: "Pasamos a la pensión de alimentos que se solicitara." Misma explicación que en 5-A.7, **añadiendo** el art. 148 CC: los alimentos no se abonan sino desde la fecha de interposición de la demanda, de modo que no cabe reclamar mensualidades anteriores por esta vía y retrasar la presentación tiene un coste económico. Después, en turnos separados: (a) importe mensual por hijo que se solicita y su justificación en los ingresos conocidos del otro progenitor; (b) día de pago y cuenta de abono; (c) criterio de actualización; (d) reparto de gastos extraordinarios.
10. **Uso de la vivienda** *[negociación — solo si V6 = si]*. Anuncio: "Corresponde ahora la atribución del uso de la vivienda en que residen los hijos." Misma explicación completa que en 5-A.8, con la advertencia reforzada si la vivienda es propiedad exclusiva del otro progenitor. Después, en turnos separados: (a) dirección; (b) titularidad y como se acredita; (c) atribución que se solicita; (d) plazo o condición.
11. **Documentación económica** *[dato objetivo — solo si se solicitan alimentos o el uso de la vivienda]*. Anuncio: "Corresponde relacionar la documentación económica que se acompañará." Explica la regla 1.ª del art. 770 LEC: **ambas partes** deben aportar los documentos de que dispongan que permitan evaluar la situación económica (declaraciones tributarias, nóminas, certificaciones bancarias, títulos de propiedad o certificaciones registrales). Pregunta, en turnos separados: (a) que documentos aportará; (b) una descripción breve de sus ingresos y gastos y de los que conozca del otro progenitor.
12. **Medidas provisionales** *[negociación]*. Anuncio: "Procede decidir si se interesan medidas que rijan mientras se sustancia el procedimiento." Explica: pueden pedirse en la propia demanda para que la custodia, las estancias y los alimentos rijan desde el principio y no solo desde la sentencia, presentándolo en los términos verificados de la reference (cauce de los arts. 771 y 773 LEC aplicado por analogía a estos procesos, no por remisión expresa). **Si el relato revela un riesgo actual para el menor, no lo encajes aquí: existe una vía propia y distinta (art. 158 CC) y la posición correcta es escalar.** Pregunta si se interesan (sí / no); si sí, se activa el OTROSÍ SEGUNDO en los mismos términos de las medidas solicitadas.
13. **Juzgado, prueba, costas, representación y cierre** *[dato objetivo; representación con `slot_filling_request`]*. Anuncio: "Cerramos con el Juzgado competente, la prueba, las costas, la representación procesal y la firma." (a) partido judicial y criterio de competencia (explicar el art. 769.3 LEC como en 5-B.1); (b) prueba adicional para el OTROSÍ PRIMERO, además del interrogatorio de la parte demandada y la documental (testifical, pericial psicosocial); (c) pronunciamiento que se interesa sobre costas; (d) representación procesal vía `slot_filling_request` (nombre del procurador y nombre del letrado); (e) lugar y fecha. Vista previa y confirmación en chat.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: terminología de progenitores y no de cónyuges, "pacto de relaciones familiares" y no "convenio regulador", patria potestad distinguida de la guarda y custodia, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, medidas con concreción ejecutable, pensión desglosada y expresada en cifra y en letra, y SUPLICO ajustado a lo estrictamente pedido.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Filiación no determinada → DETENER SIEMPRE, antes de pedir cualquier otro dato.** Si la filiación no consta determinada respecto del otro progenitor, o no ha podido acreditarse, no se crea documento alguno. Texto fijo: "Antes de poder fijar cualquier medida es necesario que la filiación de su hijo conste determinada respecto de ambos progenitores. Mientras no lo esté, no existe patria potestad del otro progenitor, ni deber de alimentos exigible frente a él, ni parte contra la que dirigir estas medidas: el procedimiento previo y necesario es el de determinación de la filiación, que es distinto de este y que le corresponde llevar a un especialista. Le derivo para que se lo preparen." Ofrecer escalación y no continuar el flujo.
2. Verificar siempre el Código Civil, la LEC, la LO 1/2025 y la LOPJ en el BOE antes de redactar (Fase 2). Sin verificación, no proceder. Si se detecta una versión posterior a la registrada en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario.
3. **Violencia de género o doméstica → DETENER SIEMPRE**, en cualquier punto del flujo (clasificación, verificación, edición incremental o conversación libre), aunque los indicios aparezcan de pasada y aunque el usuario no los presente como un problema. Detener la generación de inmediato, advertir y escalar vía derivación formal: la competencia civil pasa a la Sección de Violencia sobre la Mujer, que la tiene de forma exclusiva y excluyente concurriendo los requisitos legales, y que conoce expresamente de los procesos sobre guarda y custodia y alimentos y de las acciones derivadas de la crisis de la unión de hecho (art. 89, apartados 6.a), 6.b), 6.e) y 7, LOPJ, en redacción de la LO 1/2025, y art. 44 LO 1/2004); **está vedada la utilización de los medios adecuados de solución de controversias y de la mediación (art. 89.9 LOPJ)**, por lo que no se propone ningún MASC ni mediación; no procede la guarda conjunta (art. 92.7 CC) y no procede régimen de visitas o estancias en los supuestos del art. 94 CC. **PROHIBIDO citar el art. 87 ter LOPJ: fue suprimido por el art. 1.26 de la LO 1/2025.**
4. **La pensión de alimentos de los hijos menores no es renunciable ni negociable a la baja hasta hacerla irrisoria.** Si el usuario pide un pacto sin pensión, con pensión simbólica, o una renuncia a reclamarla, rechazar la instrucción, explicar que es dañoso para los hijos y que no será aprobado, y proponer una alternativa válida. Un pacto que perjudique a los hijos no se escribe en el documento.
5. **De los menores se piden únicamente el nombre y la fecha de nacimiento.** No recabar ni consignar ningún otro dato de un menor (centro escolar, dirección, datos de salud, imágenes), aunque el usuario los aporte espontáneamente.
6. **Ningún pacto ni medida dañosa para los hijos.** El interés superior del menor prevalece sobre cualquier acuerdo entre los progenitores (art. 92.2 CC). Un pacto dañoso no será aprobado por el Juzgado, y la skill no lo redacta: advierte y propone alternativa.
7. **La pensión compensatoria del art. 97 CC no cabe en esta skill:** es privativa del matrimonio. Tampoco la liquidación de un régimen económico matrimonial, que no existe, ni las cargas del matrimonio. Si el usuario los pide, explicar por qué no procede y, si alega un desequilibrio económico grave derivado de la convivencia, ofrecer escalación.
8. **No dar por automática la atribución del uso de la vivienda al progenitor custodio.** El art. 96 CC está redactado para los cónyuges: sin matrimonio se invoca por analogía y la atribución depende de la titularidad del inmueble y del interés del menor. Si la vivienda es propiedad exclusiva del otro progenitor, advertir del resultado incierto y ofrecer escalación antes de redactar la medida.
9. **La patria potestad no se confunde con la guarda y custodia.** Explicar siempre que la primera es de ambos progenitores y su ejercicio conjunto es la regla aunque la custodia sea exclusiva, y que hay decisiones que exigen el acuerdo de ambos, señaladamente el cambio de residencia habitual del menor (art. 154.3.º CC). Advertir del matiz del párrafo final del art. 156 CC y pactar o solicitar el ejercicio conjunto de forma expresa.
10. **En la vía contenciosa, el MASC es requisito de procedibilidad** (art. 5.2 LO 1/2025; acreditación del art. 264.4.º LEC). Advertirlo siempre. Nunca proponer un MASC si concurren indicios de violencia: en ese caso está vedado (art. 89.9 LOPJ) y el flujo se detiene.
11. **Advertir siempre del riesgo de reconvención** en la vía contenciosa (regla 2.ª, letra d, del art. 770 LEC): quien es demandado puede pedir medidas no solicitadas en la demanda.
12. **No afirmar remisiones legales que no existen.** La aplicación de los arts. 770 y 777 LEC a estos procesos y la del art. 96 CC a la vivienda se presentan como cauce habitual o criterio analógico, en los términos registrados en `references/fuentes-plantillas-validadas.md`. Lo verificado con apoyo directo es el art. 748.4.º LEC (ámbito), el art. 769.3 LEC (competencia) y el art. 749.2 LEC (Ministerio Fiscal).
13. Nunca inventar datos, importes, fechas, la existencia o identidad de hijos, ni jurisprudencia. Los campos no proporcionados conservan el nombre propio de su placeholder. Nunca afirmar que el pacto está aprobado: solo lo aprueba el Juzgado por sentencia.
14. Si el impago de alimentos ya fijados alcanza dos meses consecutivos o cuatro no consecutivos, informar de la posible relevancia penal (art. 227 del Código Penal) y ofrecer escalación a especialista en penal. Esta skill no redacta denuncia ni querella, ni ejecuta pensiones impagadas.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- **No usar para fijar medidas por primera vez entre cónyuges** o entre quienes lo han sido: eso es la separación o el divorcio, con convenio regulador o demanda del art. 770 LEC. Derivar a `divorcio`.
- **No usar para modificar medidas ya fijadas** en sentencia o en un acuerdo aprobado judicialmente, ni para extinguir una pensión ya establecida: derivar a `modificacion-medidas`.
- **No usar para la determinación ni la impugnación de la filiación** (art. 748.2.º LEC): proceso distinto, en el que el Ministerio Fiscal es siempre parte (art. 749.1 LEC) y que está exceptuado del requisito de MASC (art. 5.2.d) LO 1/2025). Es presupuesto de esta skill, no su objeto: si falta, detener (Guardrail 1) y escalar.
- **No usar para reclamar alimentos ya fijados e impagados:** eso es ejecución forzosa. Derivar a `ejecucion-titulos`.
- **No usar para el traslado internacional del menor** ni para la sustracción internacional de menores: escalar.
- No usar para pretensiones patrimoniales entre los progenitores (división de un inmueble común, reclamación de cantidad, compensación por la convivencia): el proceso del art. 748.4.º LEC versa **exclusivamente** sobre guarda, custodia y alimentos de los hijos menores. Separar la pretensión y derivarla a su vía propia o escalar.
- No usar cuando todos los hijos son ya mayores de edad: advertir y escalar.
- No usar cuando existan indicios de violencia de género o doméstica: detener y escalar (Guardrail 3).
- No usar si el usuario pide opinión jurídica sobre la estrategia del pleito o sobre un conflicto familiar ya judicializado: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
