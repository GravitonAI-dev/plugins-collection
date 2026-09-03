---
name: medidas-hijos-no-matrimoniales
description: >
  Genera los documentos para FIJAR POR PRIMERA VEZ las medidas relativas a los hijos menores comunes
  de progenitores que no estan ni han estado casados entre si (parejas de hecho registradas, parejas
  no registradas y progenitores que nunca convivieron), en el proceso del articulo 748.4.º de la Ley
  de Enjuiciamiento Civil, en sus dos vias: (1) CON ACUERDO — pacto de relaciones familiares que
  regula el ejercicio de la patria potestad (arts. 154 y 156 CC), la guarda y custodia (art. 92 CC),
  el regimen de estancias, comunicacion y visitas (art. 94 CC), la pension de alimentos (arts. 93,
  142, 146 y 148 CC) y, en su caso, el uso de la vivienda en que residen los hijos, para su
  sometimiento a aprobacion judicial por el cauce del articulo 777 de la LEC; y (2) SIN ACUERDO —
  demanda de medidas paternofiliales por los tramites del juicio verbal del articulo 770 de la LEC,
  con acreditacion del intento de MASC (art. 5 LO 1/2025) e intervencion preceptiva del Ministerio
  Fiscal (art. 749.2 LEC). Verifica la version vigente de las normas en el BOE antes de redactar.
  NO usar entre conyuges (eso es divorcio o separacion), NO usar para modificar medidas ya fijadas,
  NO cubre la determinacion ni la impugnacion de la filiacion, NO cubre la reclamacion de pensiones
  impagadas ni el traslado internacional del menor, y se detiene y escala si existen indicios de
  violencia de genero o domestica.
when_to_use: |
  - Una pareja de hecho con hijos comunes se separa y necesita fijar custodia, estancias y alimentos.
  - Dos progenitores que nunca estuvieron casados no tienen ninguna medida judicial sobre sus hijos
    y quieren regularla, con acuerdo o sin el.
  - El usuario quiere reclamar al otro progenitor la pension de alimentos de un hijo comun cuando no
    hay sentencia ni convenio previo que la fije.
  - El usuario quiere que se le atribuya la guarda y custodia de su hijo, o un regimen de estancias,
    sin que haya habido matrimonio con el otro progenitor.
  - El usuario tiene un acuerdo con el otro progenitor y quiere darle validez y fuerza ejecutiva
    sometiendolo a la aprobacion del Juzgado.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - filiacion: determinada respecto de ambos progenitores / no determinada respecto del otro / se desconoce
  - acuerdo: existe acuerdo con el otro progenitor / no existe acuerdo
  - medidas: guarda y custodia con regimen de estancias / pension de alimentos / ambas
  - vivienda: se solicita la atribucion del uso de la vivienda en que residen los hijos (si / no)
  - convivencia: pareja de hecho inscrita en registro / convivencia sin inscripcion / sin convivencia estable
  - alcance: solo el pacto de relaciones familiares / pacto y demanda conjunta (solo en la via de acuerdo)
  - datos_progenitor_a: nombre, DNI o NIE, domicilio
  - datos_progenitor_b: nombre, DNI o NIE, domicilio
  - datos_hijos: nombre y fecha de nacimiento de cada hijo (unicos datos de menores que se recaban)
  - patria_potestad: decisiones que requeriran el acuerdo de ambos y via de comunicacion entre progenitores
  - custodia_estancias: modalidad de guarda, calendario de estancias, reparto de vacaciones y lugar de entregas
  - pension_alimentos: importe por hijo, dia de pago, cuenta, actualizacion y reparto de gastos extraordinarios
  - vivienda_datos: direccion, titularidad, atribucion del uso y plazo o condicion de cese
  - masc: en la via contenciosa, tipo y fechas del intento de MASC o motivo de imposibilidad
  - documentacion_economica: documentos que acreditan la situacion economica (regla 1.ª del art. 770 LEC)
  - medidas_provisionales: en la via contenciosa, si se interesan
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

Para garantizar un enrutamiento determinista y el cumplimiento normativo riguroso, el asistente resuelve y mantiene internamente en memoria los vectores de estado de la operación (V1 a V4) y el origen de la plantilla (V5).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`, `V4`, `V5`) y los resúmenes de validación con marcas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

Tu primer objetivo es clasificar con precisión la naturaleza del caso y fijar los vectores deterministas de estado.

### 1.1 Escucha Activa Previa
Antes de abrir formularios interactivos o hacer preguntas, analiza el mensaje inicial del usuario y la documentación aportada:
- Si el mensaje ya especifica inequívocamente los vectores de la operación, asígnalos de forma inmediata y silenciosa en memoria y pasa a la **Fase 2**.
- Si restan vectores por definir, no formules preguntas abiertas en turnos sucesivos: presenta el formulario estructurado interactivo mediante la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Presenta al usuario las opciones estructuradas para resolver los vectores pendientes:
```json
{
  "type": "object",
  "properties": {
    "acuerdo_progenitores": {
      "type": "string",
      "description": "Grado de consenso entre los progenitores (V1)",
      "enum": [
        "mutuo_acuerdo",
        "contencioso"
      ]
    },
    "regimen_custodia": {
      "type": "string",
      "description": "R\u00e9gimen de guarda y custodia propuesto (V3)",
      "enum": [
        "compartida",
        "monoparental"
      ]
    },
    "uso_vivienda": {
      "type": "string",
      "description": "Atribuci\u00f3n del uso de la vivienda com\u00fan (V4)",
      "enum": [
        "atribucion_hijos",
        "sin_atribucion"
      ]
    }
  },
  "required": [
    "acuerdo_progenitores",
    "regimen_custodia"
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalua **en este orden**:

- Si **V2 = no consta la filiacion respecto del otro progenitor** (o no ha podido acreditarse) → **DETENER. No crear ningun documento y no pedir ningun otro dato.** Emite el texto fijo del Guardrail 1 y ofrece escalacion. Sin filiacion determinada no existe patria potestad del otro progenitor, ni deber de alimentos exigible frente a el (arts. 143.2.º y 154 CC), ni sujeto pasivo de las medidas: el proceso previo y necesario es el de determinacion de la filiacion (art. 748.2.º LEC), que esta skill no cubre.
- Si en cualquier momento aparecen indicios de violencia de genero o domestica → **DETENER** (Guardrail 3). No crear documento.
- Si **V1 = existe acuerdo** → **HOJA ACUERDO**: `assets/template-pacto-relaciones-familiares.md`. Si ademas V5 = 2, se genera despues `assets/template-demanda-medidas-paternofiliales.md` con los bloques condicionales de acuerdo ACTIVADOS y los de contencioso DESACTIVADOS.
- Si **V1 = no existe acuerdo** → **HOJA CONTENCIOSA**: `assets/template-demanda-medidas-paternofiliales.md` con los bloques condicionales de contencioso ACTIVADOS (intento de MASC, situacion economica de la regla 1.ª del art. 770, apartado de medidas solicitadas, otrosies de prueba y de medidas provisionales) y los de acuerdo DESACTIVADOS. No se genera pacto de relaciones familiares: es propio de la via de acuerdo.
- V3 y V3-bis no eligen asset: activan o desactivan los bloques de custodia y estancias, de alimentos y de vivienda dentro de la hoja ya elegida.
- V4 no elige asset: activa una de las tres variantes del expositivo de convivencia y, solo si V4 = 1, el Documento nº 2 con la certificacion del registro de parejas de hecho.
- Si lo que se pretende es **modificar medidas ya fijadas** en sentencia o en un acuerdo aprobado judicialmente → **DETENER esta via** y derivar a `modificacion-medidas`, explicando que lo que procede es una demanda de modificacion de medidas y no la fijacion por primera vez.
- Si los progenitores **estan o han estado casados entre si** → **DETENER esta via** y derivar a `divorcio`.
- Si lo que se reclama son **pensiones ya fijadas e impagadas** → **DETENER esta via** y derivar a `ejecucion-titulos`.
- Si se pretende la **determinacion o impugnacion de la filiacion**, el **traslado internacional del menor** o medidas de proteccion frente a un **riesgo actual** para el menor → **DETENER** y escalar (ver tabla de Escalacion).

### Validacion de presupuestos (interno, antes del Punto 3)

- **Minoria de edad de los hijos (art. 748.4.º LEC):** el proceso versa sobre hijos MENORES. Si todos los hijos son ya mayores de edad, esta via no procede: los alimentos del hijo mayor se reclaman por el cauce que corresponda y la guarda y custodia carece de objeto. Advertir y escalar. Si hay hijos menores y ademas hijos mayores sin ingresos que convivan, incluir solo a los menores en las medidas y advertir de que los alimentos del mayor tienen fundamento distinto (art. 93, parrafo 2.º, CC) y conviene revision por especialista.
- **Objeto exclusivo (art. 748.4.º LEC):** el proceso debe versar **exclusivamente** sobre guarda, custodia y alimentos de los hijos menores. Si el usuario quiere acumular la division de un inmueble comun, una reclamacion de cantidad entre los progenitores o cualquier pretension patrimonial entre ellos, separarla expresamente: advertir de que no cabe en este procedimiento y ofrecer la via propia o la escalacion. La atribucion del uso de la vivienda en que residen los hijos si se admite en la practica cuando se funda en el interes del menor: se recoge con la advertencia de la seccion correspondiente.
- **Pension compensatoria:** si el usuario la pide, **rechazar la instruccion** y explicar que el art. 97 CC es privativo del matrimonio y no cabe en este procedimiento. No incluirla en ningun documento. Si alega un desequilibrio economico grave derivado de la convivencia, ofrecer escalacion: es una pretension distinta y de fundamento propio.
- **MASC (art. 5.2 LO 1/2025) — solo en la HOJA CONTENCIOSA:** es requisito de procedibilidad. La guarda, la custodia y los alimentos de hijos menores **no** figuran entre las materias exceptuadas de las letras a) a h) del art. 5.2. Verificar si se intento; si no se intento y no concurre imposibilidad, advertir formalmente del riesgo de inadmision antes de continuar. En la HOJA ACUERDO no se pregunta por el MASC: no hay controversia que negociar.
- **Fecha de efectos de los alimentos (art. 148 CC):** los alimentos no se abonan sino desde la interposicion de la demanda. Si el usuario pide mensualidades anteriores, advertirle de que por esta via no se obtienen y no incluir retroactividad en la medida.
- **Cuenta de abono:** si el importe de la pension se fija sin cuenta de abono o sin dia de pago, la medida es dificilmente ejecutable. No cerrar la seccion de alimentos sin ambos datos, o dejarlos con su placeholder propio y advertirlo.
- **Custodia compartida sin acuerdo (art. 92.5 y 92.8 CC):** si V1 = no existe acuerdo y el usuario pide custodia compartida, advertir de que a instancia de una sola parte es excepcional (art. 92.8) y exige informe del Ministerio Fiscal y una fundamentacion en que solo asi se protege el interes del menor. No prometer su concesion.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 108, 110, 154, 92, 93 y 96 del Código Civil (igualdad absoluta de hijos matrimoniales y no matrimoniales, patria potestad, guarda y custodia, alimentos y vivienda), y Art. 770.6 de la LEC.
2. **Orientación Legal del Caso:**
Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la via y la fuente aplicable.** Textos fijos por hoja:
   - **HOJA ACUERDO:** "A su caso corresponde un pacto de relaciones familiares que regule las medidas relativas a sus hijos comunes, conforme a los articulos 154, 156, 92, 93, 94, 142, 146 y 148 del Codigo Civil, y que se somete a la aprobacion judicial en el proceso previsto en el articulo 748.4.º de la Ley 1/2000, de Enjuiciamiento Civil, por el cauce de su articulo 777. Al existir hijos menores de edad, la intervencion del Ministerio Fiscal es preceptiva y este informara sobre los terminos del pacto que les afecten (articulo 749.2 de la Ley de Enjuiciamiento Civil). Le advierto de que el pacto no queda aprobado por el hecho de firmarse ni de presentarse: hasta que lo apruebe el Juzgado por sentencia carece de fuerza ejecutiva. Puede consultar los textos oficiales en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - **HOJA CONTENCIOSA:** "A su caso corresponde una demanda de medidas paternofiliales en el proceso del articulo 748.4.º de la Ley 1/2000, de Enjuiciamiento Civil, que se sustancia por los tramites del juicio verbal conforme a su articulo 770, siendo competente el Juzgado que determina su articulo 769.3. Las medidas se fundan en los articulos 154, 156, 92, 93, 94, 142, 146 y 148 del Codigo Civil. Al existir hijos menores de edad, la intervencion del Ministerio Fiscal es preceptiva (articulo 749.2 de la Ley de Enjuiciamiento Civil). Debe acreditarse el intento previo de un medio adecuado de solucion de controversias: sin ese requisito la demanda puede ser inadmitida (articulo 5 de la Ley Organica 1/2025 y articulo 264.4.º de la Ley de Enjuiciamiento Civil). Puede consultar los textos oficiales en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763, https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 y https://www.boe.es/buscar/act.php?id=BOE-A-2025-76"
   - **En ambas hojas, anadir:** "Le confirmo que el hecho de que ustedes no hayan estado casados no altera en nada los derechos de sus hijos ni los deberes de ambos progenitores: se fija exactamente lo mismo que se fijaria en un divorcio en cuanto a los hijos. Lo unico que no existe aqui es el vinculo matrimonial y, con el, ni regimen economico matrimonial que liquidar ni pension compensatoria."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla del sistema, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio. Si el documento adjuntado contiene clausulas de contenido matrimonial (liquidacion de gananciales, pension compensatoria, cargas del matrimonio), advierteselo expresamente: es sintoma de que se ha reutilizado un convenio regulador de divorcio y esas clausulas no proceden.
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-demanda-medidas-paternofiliales.md`).
4. **Pregunta Explícita al Usuario (Vía Chat):** Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación de V5 (Origen Plantilla) y Manejo de la Elección
* **Si `[V5 = plantilla_sistema]` (El usuario acepta la plantilla propuesta):**
  Toma el texto íntegro de la plantilla correspondiente directamente desde el catálogo del prompt y procede de inmediato a la **Fase 3**.
* **Si `[V5 = plantilla_usuario]` (El usuario aporta su propia minuta adjuntando un documento o pegando texto):**
  1. Accede al contenido del adjunto desde `<attached_documents>` o el mensaje del usuario.
  2. **Guardrail de Verificación Legal:** Analiza el texto aportado. Si contiene cláusulas nulas, contrarias a normas imperativas o de imposible cumplimiento, adviértelo expresamente en el chat y propón la redacción legalmente válida.
  3. Adopta la minuta revisada como base y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en un archivo en el workspace con nombre en `snake_case.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos e inserta `{{DATO_FALTANTE}}` para aquellos que deban resolverse durante la redacción.
   - PROHIBIDO dejar archivos en blanco, crear resúmenes o esquemas provisionales.
2. **Validación de Integridad (`read_file`):**
   - Ejecuta inmediatamente `read_file` sobre el archivo recién creado para comprobar que el volcado es íntegro y que el archivo existe en disco.
3. **Confirmación en Chat y Encadenamiento Inmediato:**
   - Informa al usuario de la ruta absoluta del documento creado.
   - En esa **misma respuesta**, introduce la primera sección/cláusula de la **Fase 4** y formula ya su primera pregunta, sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

### Protocolo Obligatorio de Edición
Para cada cláusula o bloque temático del documento, ejecuta estrictamente el siguiente ciclo interactivo:
```
[Pregunta al Usuario] ──> [Vista Previa en texto plano] ──> [¿Confirmamos?] ──> [edit_file + read_file]
```
1. **Pregunta en Chat:** Solicita los datos específicos de la sección.
2. **Vista Previa:** Muestra el texto exacto redactado en texto plano en el chat.
3. **Confirmación:** Consulta al usuario si está conforme o desea algún ajuste.
4. **Persistencia en Disco:** Una vez confirmado, ejecuta `edit_file` con `old_string` y `new_string` exactos, y verifica con `read_file`.

### Hoja de Ruta de Secciones y Cláusulas Condicionales

Recorre secuencialmente la lista que corresponda al documento activo (5-A pacto, 5-B demanda conjunta, 5-C demanda contenciosa). Por cada seccion incompleta, aplica el Ciclo de Edicion Incremental Global (Formular Pregunta → Mostrar Vista Previa en texto plano → Pedir Confirmacion → Tras confirmacion, usar `Edit` en disco y verificar con `Read`).

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. No pidas permiso para pasar de seccion: informa y continua. Los anuncios nombran la seccion SUSTANTIVA del documento, nunca la mecanica interna.

**Un dato por turno.** Si un punto agrupa varios datos, pidelos en turnos separados, uno por sub-apartado.

**Confirmacion agrupada por parte (datos identificativos):** los datos puramente identificativos de una misma persona (nombre, documento de identidad y domicilio de un progenitor; nombre y fecha de nacimiento de un hijo) se preguntan igualmente uno por turno, pero SIN vista previa ni `Edit` tras cada uno: acumulalos en memoria. **Solo tras RECIBIR la respuesta al ultimo dato de esa parte —nunca en el mismo turno en que aun se esta preguntando ese ultimo dato— muestra, ya en el turno siguiente, una unica vista previa con todos sus datos juntos y pide una unica confirmacion conjunta antes de aplicar el `Edit` que los vuelca todos a la vez.** Esta excepcion es exclusiva de datos identificativos objetivos.

**Marcas de cada seccion.** Cada punto de las listas esta marcado como *[dato objetivo]* o *[negociacion]*:
- *[dato objetivo]*: se registra el valor, con validacion de sentido.
- *[negociacion]*: implica una decision con consecuencias legales. **PRIMERO explica en el chat, de forma breve y con base en `references/cc-medidas-hijos-no-matrimoniales.md`, el regimen legal por defecto y las consecuencias de cada opcion; DESPUES formula la pregunta.** Confirma que el cliente entiende y esta de acuerdo antes de escribir. Estas secciones se confirman **una por una**, sin agrupacion.

**Validacion de sentido, no solo de formato:** razona si cada respuesta tiene sentido en el contexto. Una fecha de nacimiento futura, un DNI con forma de nombre, una pension de 5 euros al mes o un regimen de estancias imposible de cumplir no se escriben en el documento: senala por que no encaja y pide aclaracion antes de continuar.

**Datos de menores:** de cada hijo se piden **unicamente el nombre y la fecha de nacimiento**. No preguntes ni escribas centro escolar, direccion del menor, datos de salud, ni ningun otro dato del menor, aunque el usuario los ofrezca espontaneamente. Si los ofrece, no los incorpores al documento.

### 5-A. Pacto de relaciones familiares (`pacto-relaciones-familiares.md`)

1. **Progenitores** *[dato objetivo — confirmacion agrupada por parte]*. Anuncio de apertura: "Comenzamos por la identificacion de ambos progenitores." Sub-apartados, uno por turno: (a) nombre completo del primer progenitor; (b) su DNI o NIE; (c) su domicilio actual → confirmacion agrupada del primer progenitor. Anuncio: "Identificado el primer progenitor, pasamos a los datos del otro." (d) nombre completo del segundo progenitor; (e) su DNI o NIE; (f) su domicilio actual → confirmacion agrupada del segundo progenitor.
2. **Hijos comunes** *[dato objetivo — confirmacion agrupada del bloque]*. Anuncio: "Corresponde ahora identificar a los hijos comunes." Por cada hijo, nombre y fecha de nacimiento, un hijo por turno. Solo esos dos datos. Confirmacion agrupada de todos los hijos al terminar.
3. **Convivencia y su cese** *[dato objetivo]*. Anuncio: "Recogemos ahora los datos de la convivencia y de su cese, que se hacen constar unicamente como antecedente." V4 ya esta resuelto: no lo vuelvas a preguntar. Si V4 = 1, en turnos separados: (a) registro de parejas de hecho en que constaba la inscripcion; (b) fecha de la inscripcion; (c) fecha del cese de la convivencia. Si V4 = 2: (a) fecha aproximada de inicio de la convivencia; (b) fecha del cese. Si V4 = 3, la variante del expositivo se resuelve sola: no preguntes nada y pasa a la seccion siguiente.
4. **Patria potestad y su ejercicio** *[negociacion]*. Anuncio: "Pasamos a la primera de las medidas: el ejercicio de la patria potestad." Explica antes de preguntar: la patria potestad corresponde a ambos progenitores por el hecho de la filiacion y su ejercicio conjunto es la regla (art. 156 CC), **con independencia de a quien se atribuya la custodia**: son dos cosas distintas. Advierte del matiz del parrafo final del art. 156 CC: viviendo los progenitores separados, la ley preve que la ejerza aquel con quien el hijo conviva, salvo atribucion judicial del ejercicio conjunto, **por lo que conviene pactarlo expresamente**. Enumera las decisiones que requieren el acuerdo de ambos, y en particular el cambio del lugar de residencia habitual del menor (art. 154.3.º CC), y explica que los desacuerdos se resuelven por la via del art. 156 CC. Despues pregunta, en turnos separados: (a) si desea anadir alguna decision concreta a la lista de las que requeriran acuerdo de ambos; (b) la via de comunicacion que pactan entre progenitores para los asuntos de los hijos.
5. **Guarda y custodia** *[negociacion — solo si V3 incluye custodia]*. Anuncio: "Corresponde ahora determinar la guarda y custodia de los hijos." Explica antes de preguntar: no hay preferencia legal automatica; la compartida requiere el acuerdo de ambos (art. 92.5 CC) y que exista una comunicacion minima entre los progenitores, que el juez valora expresamente (art. 92.6 CC); la exclusiva atribuye la convivencia a un progenitor y el otro conserva la patria potestad y un regimen de estancias (art. 94 CC). El criterio decisivo es el interes superior del menor (art. 92.2 CC), y el vinculo que unio a los progenitores es irrelevante para los derechos del hijo. Despues pregunta la modalidad acordada.
6. **Regimen de estancias, comunicacion y vacaciones** *[negociacion — solo si V3 incluye custodia]*. Anuncio: "Fijada la custodia, corresponde concretar el regimen de estancias y comunicacion." Explica antes de preguntar: la concrecion es lo que evita futuros conflictos y ejecuciones; un regimen "amplio y flexible" garantiza un incidente. Pide dias concretos, horas de inicio y fin, y a quien corresponde cada periodo en los anos pares y en los impares. Despues, en turnos separados: (a) calendario ordinario de estancias; (b) reparto de las vacaciones escolares; (c) lugar de entregas y recogidas y quien recoge y quien entrega; (d) regimen de comunicacion telefonica o telematica con el progenitor con el que el hijo no se encuentre.
7. **Pension de alimentos** *[negociacion — solo si V3 incluye alimentos]*. Anuncio: "Pasamos a la pension de alimentos de los hijos." Explica antes de preguntar: el deber de alimentos deriva de la filiacion y existe igual sin matrimonio (art. 143.2.º CC); la cuantia es proporcionada al caudal o medios de quien los da y a las necesidades de quien los recibe (art. 146 CC), sin tarifa legal; las tablas orientadoras del CGPJ pueden servir de referencia no vinculante (https://www.poderjudicial.es/cgpj/es/Servicios/Utilidades/Calculo-de-pensiones-alimenticias/) **y, mientras el estado verificado en el Punto 2 siga siendo el de revision, adviertelo expresamente para no remitir al cliente a una herramienta que no esta operativa**; la pension cubre los gastos ordinarios y previsibles, mientras los extraordinarios son los imprevisibles y no periodicos, que suelen repartirse al 50 % con comunicacion y justificacion previas y acuerdo previo si no son urgentes; conviene la actualizacion anual para que la pension no se degrade; y **la pension de los hijos menores no es renunciable ni negociable a la baja hasta hacerla irrisoria: un pacto asi es danoso para los hijos y no sera aprobado**. Si la custodia acordada es compartida, usa la variante del asset prevista para ella (contribucion de ambos a un fondo comun o compensacion por la diferencia de ingresos), no la de pago unidireccional. Despues, en turnos separados: (a) importe mensual por hijo, o forma de contribucion si la custodia es compartida; (b) dia de pago y cuenta de abono; (c) criterio de actualizacion anual; (d) porcentaje de reparto de los gastos extraordinarios. Confirmacion propia de cada uno.
8. **Uso de la vivienda en que residen los hijos** *[negociacion — solo si V3-bis = 1]*. Anuncio: "Corresponde ahora la atribucion del uso de la vivienda en que residen los hijos." **Explica antes de preguntar, y hazlo con detalle porque es el punto que mas confunde al cliente:** aqui no hay regimen economico matrimonial que liquidar; el art. 96 CC, que en los divorcios atribuye el uso al progenitor custodio, esta redactado para los conyuges y para los supuestos de nulidad, separacion y divorcio, de modo que **no se aplica de forma directa**. Sin matrimonio, la vivienda se rige por las reglas ordinarias de la propiedad y de los contratos: si es privativa de un progenitor, es suya; si es de ambos en proindiviso, cualquiera puede pedir la division; si es de alquiler, por el contrato. Lo que si opera es el interes del menor, cuya necesidad de habitacion forma parte de los alimentos (art. 142 CC), y por esa via se invoca el criterio del art. 96.1 **por analogia**. Nunca afirmes que el progenitor no titular tiene derecho al uso por el solo hecho de tener la custodia. Si la vivienda es propiedad exclusiva del otro progenitor, advierte expresamente de que la atribucion es una limitacion de la facultad dispositiva del titular, de resultado incierto, y ofrece escalacion antes de redactar la medida; pon sobre la mesa las alternativas: plazo cerrado en lugar de indefinido, compensacion economica al titular, cuantificar la habitacion dentro de la pension, o venta o extincion del condominio si el inmueble es comun. Despues, en turnos separados: (a) direccion de la vivienda; (b) titularidad real; (c) a quien se atribuye el uso; (d) plazo o condicion de cese; (e) reparto de los gastos derivados de la vivienda.
9. **Cierre del pacto** *[dato objetivo]*. Anuncio: "Cerramos el pacto con el lugar y la fecha de firma." Pregunta lugar y fecha de firma. La clausula de sometimiento a la aprobacion judicial se resuelve sola: no la preguntes.

### 5-B. Demanda conjunta de mutuo acuerdo (`demanda-medidas-paternofiliales.md`, solo si V5 = 2)

Al crearla, vuelca sin volver a preguntar todos los datos ya recogidos en 5-A (progenitores, hijos, convivencia, fecha y lugar del pacto). Secciones pendientes:

1. **Juzgado competente** *[dato objetivo con explicacion]*. Anuncio: "Pasamos a la demanda: en primer lugar, el Juzgado competente." Explica la regla del art. 769.3 LEC: es competente el Juzgado de Primera Instancia del ultimo domicilio comun de los progenitores y, si residen en distintos partidos judiciales, a eleccion del demandante, el del domicilio del demandado o el de la residencia del menor; el tribunal lo examina de oficio y no cabe pactar otro fuero (art. 769.4 LEC). Pregunta el partido judicial y el criterio por el que resulta competente. Si nunca existio domicilio comun, adopta la posicion conservadora del de la residencia del menor y explicalo.
2. **Situacion actual de los hijos** *[dato objetivo con validacion]*. Anuncio: "Recogemos brevemente la situacion actual de los hijos." Pregunta con quien conviven los hijos en este momento y desde cuando. **No pidas ni escribas ningun otro dato del menor.**
3. **Representacion procesal** *[dato objetivo — confirmacion agrupada]*. Anuncio: "Corresponde identificar la representacion procesal." (a) nombre del procurador; (b) nombre del letrado → confirmacion agrupada. Si aun no estan designados, cada uno queda con su propio placeholder del asset.
4. **Costas y cierre** *[dato objetivo]*. Anuncio: "Cerramos la demanda con el pronunciamiento sobre costas, el lugar y la fecha." Explica que, presentandose de comun acuerdo, lo habitual es no interesar condena en costas, y pregunta si desea ese pronunciamiento. Despues, lugar y fecha. La relacion de documentos (certificaciones literales de nacimiento, certificacion del registro de parejas de hecho si V4 = 1, pacto firmado) se rellena sola segun la clasificacion: muestrala en la vista previa sin preguntar.

### 5-C. Demanda contenciosa de medidas paternofiliales (`demanda-medidas-paternofiliales.md`)

1. **Progenitor demandante** *[dato objetivo — confirmacion agrupada por parte]*. Anuncio de apertura: "Procedemos a la identificacion de la parte demandante." (a) nombre completo; (b) DNI o NIE; (c) domicilio → confirmacion agrupada.
2. **Progenitor demandado** *[dato objetivo — confirmacion agrupada por parte]*. Anuncio: "Identificada la parte demandante, pasamos a la parte demandada." (d) nombre completo; (e) DNI o NIE; (f) domicilio → confirmacion agrupada. Si se desconoce el domicilio, queda con su propio placeholder y afecta al MASC: se activa la declaracion responsable del art. 264.4.º LEC (ver seccion 4).
3. **Hijos comunes** *[dato objetivo — confirmacion agrupada del bloque]*. Anuncio: "Corresponde identificar a los hijos comunes." Nombre y fecha de nacimiento de cada hijo, uno por turno; solo esos dos datos; confirmacion agrupada. Con la fecha de nacimiento ya conocida, calcula tu mismo si algun hijo ha cumplido doce anos e informa de que en ese caso sera oido en todo caso (regla 4.ª del art. 770 LEC).
4. **Convivencia, cese e intento de solucion extrajudicial** *[dato objetivo con advertencia]*. Anuncio: "Pasamos a los hechos: el cese de la convivencia y el intento de solucion extrajudicial." Primero, segun V4, los datos de la convivencia y su cese (mismos sub-apartados que en 5-A.3). Despues explica el requisito de procedibilidad: el art. 5.2 de la LO 1/2025 exige acreditar el intento previo de un medio adecuado de solucion de controversias en estos procesos, sin que la guarda, la custodia y los alimentos figuren entre las materias exceptuadas, y sin ese requisito la demanda puede ser inadmitida. Aclara que basta la actividad negociadora desarrollada directamente por las partes o entre sus abogados, y que debe existir identidad entre el objeto negociado y el del pleito. Pregunta si se intento (si / no en la misma frase). Si si: tipo de MASC y fechas de inicio y fin, en turnos separados. Si no y se desconoce el domicilio del demandado o concurre otra imposibilidad: activa la declaracion responsable del art. 264.4.º LEC y pregunta el motivo. Si no y no concurre imposibilidad: advierte formalmente del riesgo de inadmision y recomienda intentarlo antes de presentar; si el cliente decide continuar, deja el bloque con su placeholder propio y la advertencia registrada.
5. **Riesgo de reconvencion** *[negociacion — informativo, no genera texto en el documento]*. Anuncio: "Antes de concretar las medidas, debo advertirle de un riesgo del procedimiento." Explica la regla 2.ª, letra d), del art. 770 LEC: la parte demandada puede reconvenir con la contestacion pidiendo medidas que no se han solicitado en la demanda —por ejemplo, la custodia compartida frente a una demanda que solo pide alimentos— y el actor dispone de 10 dias para contestarla. Pregunta si prevee que la otra parte formule esa pretension y, en caso afirmativo, si desea pedir ya en la demanda las medidas correspondientes en lugar de dejar que el debate lo abra la contraparte. Registra la decision para las secciones siguientes; si el cliente amplia las medidas solicitadas, actualiza V3 y activa los bloques correspondientes del asset.
6. **Situacion actual de los hijos** *[dato objetivo con validacion]*. Anuncio: "Recogemos la situacion actual de los hijos." Pregunta con quien conviven en este momento y desde cuando, y si el otro progenitor mantiene contacto y con que frecuencia de hecho. **No pidas ni escribas ningun otro dato del menor.**
7. **Patria potestad** *[negociacion]*. Anuncio: "Pasamos a la primera de las medidas que se solicitaran: el ejercicio de la patria potestad." Misma explicacion que en 5-A.4, con el matiz de que aqui se **solicita** el ejercicio conjunto y la enumeracion de decisiones que requeriran acuerdo de ambos. Pregunta si solicita el ejercicio conjunto y que decisiones desea que se reserven expresamente al acuerdo de ambos.
8. **Guarda, custodia y regimen de estancias solicitados** *[negociacion — solo si V3 incluye custodia]*. Anuncio: "Corresponde concretar la guarda y custodia y el regimen de estancias que se solicitaran." Misma explicacion que en 5-A.5 y 5-A.6, **anadiendo** que en la via contenciosa la custodia compartida a instancia de una sola parte es excepcional y exige informe del Ministerio Fiscal y una fundamentacion en que solo asi se protege adecuadamente el interes del menor (art. 92.8 CC): no prometas su concesion. Despues, en turnos separados: (a) modalidad de custodia que se solicita; (b) calendario de estancias propuesto; (c) reparto de vacaciones; (d) lugar de entregas y recogidas.
9. **Pension de alimentos solicitada** *[negociacion — solo si V3 incluye alimentos]*. Anuncio: "Pasamos a la pension de alimentos que se solicitara." Misma explicacion que en 5-A.7, **anadiendo** el art. 148 CC: los alimentos no se abonan sino desde la fecha de interposicion de la demanda, de modo que no cabe reclamar mensualidades anteriores por esta via y retrasar la presentacion tiene un coste economico. Despues, en turnos separados: (a) importe mensual por hijo que se solicita y su justificacion en los ingresos conocidos del otro progenitor; (b) dia de pago y cuenta de abono; (c) criterio de actualizacion; (d) reparto de gastos extraordinarios.
10. **Uso de la vivienda** *[negociacion — solo si V3-bis = 1]*. Anuncio: "Corresponde ahora la atribucion del uso de la vivienda en que residen los hijos." Misma explicacion completa que en 5-A.8, con la advertencia reforzada si la vivienda es propiedad exclusiva del otro progenitor. Despues, en turnos separados: (a) direccion; (b) titularidad y como se acredita; (c) atribucion que se solicita; (d) plazo o condicion.
11. **Documentacion economica** *[dato objetivo — solo si se solicitan alimentos o el uso de la vivienda]*. Anuncio: "Corresponde relacionar la documentacion economica que se acompanara." Explica la regla 1.ª del art. 770 LEC: **ambas partes** deben aportar los documentos de que dispongan que permitan evaluar la situacion economica (declaraciones tributarias, nominas, certificaciones bancarias, titulos de propiedad o certificaciones registrales). Pregunta, en turnos separados: (a) que documentos aportara; (b) una descripcion breve de sus ingresos y gastos y de los que conozca del otro progenitor.
12. **Medidas provisionales** *[negociacion]*. Anuncio: "Procede decidir si se interesan medidas que rijan mientras se sustancia el procedimiento." Explica: pueden pedirse en la propia demanda para que la custodia, las estancias y los alimentos rijan desde el principio y no solo desde la sentencia, presentandolo en los terminos verificados de la reference (cauce de los arts. 771 y 773 LEC aplicado por analogia a estos procesos, no por remision expresa). **Si el relato revela un riesgo actual para el menor, no lo encajes aqui: existe una via propia y distinta (art. 158 CC) y la posicion correcta es escalar.** Pregunta si se interesan (si / no); si si, se activa el OTROSI SEGUNDO en los mismos terminos de las medidas solicitadas.
13. **Juzgado, prueba, costas, representacion y cierre** *[dato objetivo; representacion con confirmacion agrupada]*. Anuncio: "Cerramos con el Juzgado competente, la prueba, las costas, la representacion procesal y la firma." (a) partido judicial y criterio de competencia (explicar el art. 769.3 LEC como en 5-B.1); (b) prueba adicional para el OTROSI PRIMERO, ademas del interrogatorio de la parte demandada y la documental (testifical, pericial psicosocial); (c) pronunciamiento que se interesa sobre costas; (d) nombre del procurador; (e) nombre del letrado → confirmacion agrupada de la representacion; (f) lugar y fecha.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: terminologia de progenitores y no de conyuges, "pacto de relaciones familiares" y no "convenio regulador", patria potestad distinguida de la guarda y custodia, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, medidas con concrecion ejecutable, pension desglosada y expresada en cifra y en letra, y SUPLICO ajustado a lo estrictamente pedido.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones del documento, presenta al usuario un menú interactivo:
```
1. Modificar o ajustar una cláusula o sección existente.
2. Añadir una estipulación o pacto adicional a medida.
3. Eliminar contenido opcional o corregir datos de partes/fincas.
4. Revisar la coherencia global y realizar control de calidad final.
5. Dar el documento por finalizado y cerrar la sesión.
```
### Advertencias Legales Preceptivas de Cierre:
Al dar por finalizado el documento, emite siempre las siguientes advertencias:
- **Carácter DRAFT:** El documento generado es un borrador profesional que debe ser revisado por un abogado colegiado antes de su firma o presentación procesal.
- **Obligaciones Fiscales y Plazos:** Recuerda los plazos de liquidación de tributos (ITP/AJD o Plusvalía municipal en 30 días hábiles) cuando proceda.
- **Elevación a Instrumento Público:** Recuerda que para la inscripción en el Registro de la Propiedad o Mercantil, o para su ejecución forzosa directa, es necesario el otorgamiento ante Notario público.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Filiacion no determinada → DETENER SIEMPRE, antes de pedir cualquier otro dato.** Si la filiacion no consta determinada respecto del otro progenitor, o no ha podido acreditarse, no se crea documento alguno. Texto fijo: "Antes de poder fijar cualquier medida es necesario que la filiacion de su hijo conste determinada respecto de ambos progenitores. Mientras no lo este, no existe patria potestad del otro progenitor, ni deber de alimentos exigible frente a el, ni parte contra la que dirigir estas medidas: el procedimiento previo y necesario es el de determinacion de la filiacion, que es distinto de este y que le corresponde llevar a un especialista. Le derivo para que se lo preparen." Ofrecer escalacion y no continuar el flujo.
2. Verificar siempre el Codigo Civil, la LEC, la LO 1/2025 y la LOPJ en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder. Si se detecta una version posterior a la registrada en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario.
3. **Violencia de genero o domestica → DETENER SIEMPRE**, en cualquier punto del flujo (clasificacion, verificacion, edicion incremental o conversacion libre), aunque los indicios aparezcan de pasada y aunque el usuario no los presente como un problema. Detener la generacion de inmediato, advertir y escalar via derivación formal: la competencia civil pasa a la Seccion de Violencia sobre la Mujer, que la tiene de forma exclusiva y excluyente concurriendo los requisitos legales, y que conoce expresamente de los procesos sobre guarda y custodia y alimentos y de las acciones derivadas de la crisis de la union de hecho (art. 89, apartados 6.a), 6.b), 6.e) y 7, LOPJ, en redaccion de la LO 1/2025, y art. 44 LO 1/2004); **esta vedada la utilizacion de los medios adecuados de solucion de controversias y de la mediacion (art. 89.9 LOPJ)**, por lo que no se propone ningun MASC ni mediacion; no procede la guarda conjunta (art. 92.7 CC) y no procede regimen de visitas o estancias en los supuestos del art. 94 CC. **PROHIBIDO citar el art. 87 ter LOPJ: fue suprimido por el art. 1.26 de la LO 1/2025.**
4. **La pension de alimentos de los hijos menores no es renunciable ni negociable a la baja hasta hacerla irrisoria.** Si el usuario pide un pacto sin pension, con pension simbolica, o una renuncia a reclamarla, rechazar la instruccion, explicar que es danoso para los hijos y que no sera aprobado, y proponer una alternativa valida. Un pacto que perjudique a los hijos no se escribe en el documento.
5. **De los menores se piden unicamente el nombre y la fecha de nacimiento.** No recabar ni consignar ningun otro dato de un menor (centro escolar, direccion, datos de salud, imagenes), aunque el usuario los aporte espontaneamente.
6. **Ningun pacto ni medida danosa para los hijos.** El interes superior del menor prevalece sobre cualquier acuerdo entre los progenitores (art. 92.2 CC). Un pacto danoso no sera aprobado por el Juzgado, y la skill no lo redacta: advierte y propone alternativa.
7. **La pension compensatoria del art. 97 CC no cabe en esta skill:** es privativa del matrimonio. Tampoco la liquidacion de un regimen economico matrimonial, que no existe, ni las cargas del matrimonio. Si el usuario los pide, explicar por que no procede y, si alega un desequilibrio economico grave derivado de la convivencia, ofrecer escalacion.
8. **No dar por automatica la atribucion del uso de la vivienda al progenitor custodio.** El art. 96 CC esta redactado para los conyuges: sin matrimonio se invoca por analogia y la atribucion depende de la titularidad del inmueble y del interes del menor. Si la vivienda es propiedad exclusiva del otro progenitor, advertir del resultado incierto y ofrecer escalacion antes de redactar la medida.
9. **La patria potestad no se confunde con la guarda y custodia.** Explicar siempre que la primera es de ambos progenitores y su ejercicio conjunto es la regla aunque la custodia sea exclusiva, y que hay decisiones que exigen el acuerdo de ambos, senaladamente el cambio de residencia habitual del menor (art. 154.3.º CC). Advertir del matiz del parrafo final del art. 156 CC y pactar o solicitar el ejercicio conjunto de forma expresa.
10. **En la via contenciosa, el MASC es requisito de procedibilidad** (art. 5.2 LO 1/2025; acreditacion del art. 264.4.º LEC). Advertirlo siempre. Nunca proponer un MASC si concurren indicios de violencia: en ese caso esta vedado (art. 89.9 LOPJ) y el flujo se detiene.
11. **Advertir siempre del riesgo de reconvencion** en la via contenciosa (regla 2.ª, letra d, del art. 770 LEC): quien es demandado puede pedir medidas no solicitadas en la demanda.
12. **No afirmar remisiones legales que no existen.** La aplicacion de los arts. 770 y 777 LEC a estos procesos y la del art. 96 CC a la vivienda se presentan como cauce habitual o criterio analogico, en los terminos registrados en `references/fuentes-plantillas-validadas.md`. Lo verificado con apoyo directo es el art. 748.4.º LEC (ambito), el art. 769.3 LEC (competencia) y el art. 749.2 LEC (Ministerio Fiscal).
13. Nunca inventar datos, importes, fechas, la existencia o identidad de hijos, ni jurisprudencia. Los campos no proporcionados conservan el nombre propio de su placeholder. Nunca afirmar que el pacto esta aprobado: solo lo aprueba el Juzgado por sentencia.
14. Si el impago de alimentos ya fijados alcanza dos meses consecutivos o cuatro no consecutivos, informar de la posible relevancia penal (art. 227 del Codigo Penal) y ofrecer escalacion a especialista en penal. Esta skill no redacta denuncia ni querella, ni ejecuta pensiones impagadas.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- **No usar para fijar medidas por primera vez entre conyuges** o entre quienes lo han sido: eso es la separacion o el divorcio, con convenio regulador o demanda del art. 770 LEC. Derivar a `divorcio`.
- **No usar para modificar medidas ya fijadas** en sentencia o en un acuerdo aprobado judicialmente, ni para extinguir una pension ya establecida: derivar a `modificacion-medidas`.
- **No usar para la determinacion ni la impugnacion de la filiacion** (art. 748.2.º LEC): proceso distinto, en el que el Ministerio Fiscal es siempre parte (art. 749.1 LEC) y que esta exceptuado del requisito de MASC (art. 5.2.d) LO 1/2025). Es presupuesto de esta skill, no su objeto: si falta, detener (Guardrail 1) y escalar.
- **No usar para reclamar alimentos ya fijados e impagados:** eso es ejecucion forzosa. Derivar a `ejecucion-titulos`.
- **No usar para el traslado internacional del menor** ni para la sustraccion internacional de menores: escalar.
- No usar para pretensiones patrimoniales entre los progenitores (division de un inmueble comun, reclamacion de cantidad, compensacion por la convivencia): el proceso del art. 748.4.º LEC versa **exclusivamente** sobre guarda, custodia y alimentos de los hijos menores. Separar la pretension y derivarla a su via propia o escalar.
- No usar cuando todos los hijos son ya mayores de edad: advertir y escalar.
- No usar cuando existan indicios de violencia de genero o domestica: detener y escalar (Guardrail 3).
- No usar si el usuario pide opinion juridica sobre la estrategia del pleito o sobre un conflicto familiar ya judicializado: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
