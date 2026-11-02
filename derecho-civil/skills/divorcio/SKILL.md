---
name: divorcio
title: Divorcio y separación
i18n:
  en:
    name: divorce
    title: Divorce and separation
    description: >
      Generates the documents for separation or divorce in Spain through its three routes: (1)
      judicial MUTUAL AGREEMENT, with the regulatory agreement under Article 90 of the **Civil
      Code** and, optionally, the joint petition under Article 777 of the **Civil Procedure Act
      (Law 1/2000, LEC)**; (2) MUTUAL AGREEMENT before a notary or court clerk, with the
      regulatory agreement for execution as a public deed (Arts. 82 and 87 CC and Art. 54
      Notarial Act; only without minor or dependent children); and (3) CONTESTED, with the
      petition under Article 770 LEC, the definitive measures of Articles 91 to 97 of the Civil
      Code and proof of the MASC attempt (Organic Law 1/2025). It verifies the version in force
      in the BOE before drafting. Do not use for marriage annulment, modification of measures
      already agreed, enforcement of breached agreements, unmarried couples, or where there are
      indications of gender or domestic violence (in which case it stops and escalates).
description: >
  Genera los documentos de la separación o el divorcio en España, en sus tres vías: (1) MUTUO ACUERDO
  judicial — convenio regulador conforme al artículo 90 del **Código Civil**, que regula las causas y los efectos de la separación y el divorcio, y, si se desea, demanda
  conjunta del artículo 777 de la **Ley 1/2000 de Enjuiciamiento Civil (LEC)** (con intervención del Ministerio Fiscal si hay hijos menores o
  mayores con discapacidad dependientes); (2) MUTUO ACUERDO notarial o ante el Letrado de la
  Administración de Justicia — convenio regulador para su otorgamiento en escritura pública (arts. 82
  y 87 CC y art. 54 Ley del Notariado; solo sin hijos menores ni dependientes); y (3) CONTENCIOSO —
  demanda de separación o divorcio del artículo 770 de la LEC con las medidas definitivas de los
  artículos 91 a 97 del Código Civil y acreditación del intento de MASC (LO 1/2025). Verifica la
  versión vigente de las normas en el BOE antes de redactar. NO usar para nulidad matrimonial,
  modificación de medidas ya acordadas, ejecución de convenios incumplidos, parejas de hecho, ni
  cuando existan indicios de violencia de género o doméstica (en ese caso se detiene y escala).
when_to_use: |
  - El usuario quiere divorciarse o separarse, de mutuo acuerdo o sin acuerdo con su cónyuge.
  - El usuario pide un convenio regulador, una demanda de divorcio o separación (de mutuo acuerdo o
    contenciosa), o pregunta por la vía notarial del divorcio.
  - El usuario necesita pactar o solicitar custodia, visitas, pensión de alimentos, uso de la
    vivienda o pensión compensatoria dentro de una ruptura matrimonial.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - modalidad: mutuo acuerdo / contencioso
  - tipo_ruptura: divorcio / separación
  - hijos: existencia de hijos menores no emancipados o mayores con discapacidad dependientes (sí / no)
  - via: judicial / notarial (solo mutuo acuerdo sin hijos menores ni dependientes)
  - alcance: solo convenio regulador / convenio + demanda de mutuo acuerdo (solo vía judicial de mutuo acuerdo)
  - datos_conyuges: nombre, DNI, domicilio de cada cónyuge
  - datos_hijos: nombre y fecha de nacimiento de cada hijo, si los hay
  - datos_matrimonio: fecha y lugar de celebración, registro civil, régimen económico
  - custodia_visitas: modalidad de guarda (exclusiva / compartida) y régimen de estancias
  - pension_alimentos: importe, día de pago, cuenta, actualización y gastos extraordinarios
  - vivienda_familiar: dirección, titularidad y atribución del uso
  - liquidacion_regimen: reparto de bienes y deudas comunes, si procede
  - pension_compensatoria: si hay desequilibrio, importe, duración y forma; o renuncia
  - masc: en contencioso, tipo y fechas del intento de MASC o motivo de imposibilidad
  - medidas_provisionales: en contencioso, si se interesan (art. 773 LEC)
  - partido_judicial: competencia (art. 769 LEC), en las vías judiciales
outputs:
  - convenio_regulador: convenio regulador de separación o divorcio en markdown, DRAFT
  - demanda_mutuo_acuerdo: opcional, demanda conjunta del Art. 777 LEC en markdown, DRAFT
  - demanda_contenciosa: demanda de separación o divorcio del Art. 770 LEC en markdown, DRAFT
references:
  - references/cc-convenio-regulador-art90.md
  - references/cc-divorcio-separacion-art81-87.md
  - references/cc-medidas-custodia-alimentos-arts92-97.md
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/lec-proceso-contencioso-arts770-774.md
  - references/lec-proceso-mutuo-acuerdo-art777.md
assets:
  - assets/template-convenio-regulador.md
  - assets/template-demanda-divorcio-contencioso.md
  - assets/template-demanda-divorcio-mutuo-acuerdo.md
---

# Generar Convenio Regulador y Demandas de Separación o Divorcio

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
      "id": "modalidad",
      "rationale": "Resolver V1: el mutuo acuerdo genera convenio regulador y el contencioso una demanda con medidas, con documentos y trámites incompatibles.",
      "question": "¿Hay acuerdo entre los cónyuges?",
      "options": [
        {"id": "mutuo_acuerdo", "label": "Sí, ambos están de acuerdo"},
        {"id": "contencioso", "label": "No hay acuerdo: procede vía contenciosa"}
      ]
    },
    {
      "id": "tipo_ruptura",
      "rationale": "Resolver V2: determina el precepto aplicable y los efectos sobre el vínculo matrimonial.",
      "question": "¿Qué se solicita?",
      "options": [
        {"id": "divorcio", "label": "Divorcio, con disolución del vínculo"},
        {"id": "separacion", "label": "Separación, manteniendo el vínculo"}
      ]
    },
    {
      "id": "hijos",
      "rationale": "Resolver V3: la existencia de hijos menores o dependientes impone la vía judicial con intervención del Ministerio Fiscal y excluye la notarial.",
      "question": "¿Hay hijos menores no emancipados, o mayores con discapacidad dependientes?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"}
      ]
    },
    {
      "id": "via",
      "rationale": "Resolver V4: en mutuo acuerdo sin hijos dependientes cabe la vía notarial, que no genera demanda.",
      "question": "Si hay mutuo acuerdo y no hay hijos dependientes, ¿qué vía prefiere?",
      "show_if": {"question_id": "modalidad", "option_ids": ["mutuo_acuerdo"]},
      "options": [
        {"id": "judicial", "label": "Judicial, con presentación de demanda de mutuo acuerdo"},
        {"id": "notarial", "label": "Notarial, mediante escritura pública"},
        {"id": "no_procede", "label": "No procede: no hay mutuo acuerdo o existen hijos dependientes"}
      ]
    },
    {
      "id": "alcance",
      "rationale": "Resolver V5: determina si además del convenio se redacta la demanda de mutuo acuerdo.",
      "question": "Si la vía es judicial de mutuo acuerdo, ¿qué alcance tiene el encargo?",
      "show_if": {"question_id": "modalidad", "option_ids": ["mutuo_acuerdo"]},
      "options": [
        {"id": "solo_convenio", "label": "Solo el convenio regulador"},
        {"id": "convenio_y_demanda", "label": "El convenio regulador y la demanda de mutuo acuerdo"},
        {"id": "no_procede", "label": "No procede: no es vía judicial de mutuo acuerdo"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — respuesta a `modalidad`
- `V2` — respuesta a `tipo_ruptura`
- `V3` — respuesta a `hijos`
- `V4` — respuesta a `via`
- `V5` — respuesta a `alcance`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores necesarios, evalúa:
- Si [V1 = contencioso] -> Plantilla a usar: `assets/template-demanda-divorcio-contencioso.md`. V4 y V5 no aplican. No se genera convenio regulador (es propio del mutuo acuerdo).
- Si [V1 = mutuo_acuerdo] y [V3 = si] -> Vía judicial obligatoria con Ministerio Fiscal. Resolver V5. Plantillas: `assets/template-convenio-regulador.md` y, si V5 = convenio_y_demanda, además `assets/template-demanda-divorcio-mutuo-acuerdo.md`.
- Si [V1 = mutuo_acuerdo] y [V3 = no] y [V4 = notarial] -> Plantilla a usar: `assets/template-convenio-regulador.md` (la escritura la otorga el notario; no se genera demanda). V5 no aplica.
- Si [V1 = mutuo_acuerdo] y [V3 = no] y [V4 = judicial] -> Resolver V5. Plantillas: `assets/template-convenio-regulador.md` y, si V5 = convenio_y_demanda, además `assets/template-demanda-divorcio-mutuo-acuerdo.md`.
- Si [V1 = mutuo_acuerdo] y [V3 = no] y [V4 = no_procede] -> DETENER la elección de plantilla: la respuesta es incoherente, porque hay mutuo acuerdo y no hay hijos dependientes, que es justo el supuesto en que se elige vía. Aclarar en el chat (REG-VAL-01) si se prefiere la vía judicial o la notarial, o si en realidad falta el acuerdo o hay hijos dependientes, y volver a resolver el vector que corresponda. No crear documento hasta resolverlo.
- Si en cualquier momento hay indicios de violencia de género o doméstica -> Detén el proceso (Guardrail 3). No crees documento.
- `V2` no elige plantilla: determina si el escrito pide el divorcio o la separación, y con ello el precepto invocado y los efectos sobre el vínculo matrimonial.
- **Requisito de procedibilidad (Ley Orgánica 1/2025).** Si el intento previo de un medio adecuado de solución de controversias no está acreditado y esta skill no genera por sí misma el documento que lo acredita, **deriva a `masc-acuerdos`**, que produce el requerimiento de negociación, el acta del intento, la oferta vinculante, el acuerdo transaccional y la declaración responsable de imposibilidad. Ofrece encadenar con ella antes de continuar, y advierte de que sin ese documento la demanda no se admite a trámite.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 81 a 97 del Código Civil (separación, divorcio, medidas paternofiliales, pensión de alimentos y pensión compensatoria), y Arts. 769, 770 y 777 de la Ley de Enjuiciamiento Civil (LEC).
2. **Orientación Legal del Caso:**

**Informa la norma aplicable y las consecuencias de la ruta.** Con registro formal (usted, tono de abogado), indica qué ley y que artículos concretos aplican al caso ya clasificado, con la versión vigente verificada, e incluye SIEMPRE el enlace al BOE consultado. Además, según la ruta:
- Con hijos menores o dependientes (mutuo acuerdo): informar de que la vía es judicial y de que el Ministerio Fiscal informará sobre las medidas que afecten a los hijos (Ley 1/2000, de Enjuiciamiento Civil, artículo 777.5).
- Vía notarial: informar de que la escritura se otorga ante el notario del último domicilio común o del domicilio de cualquiera de los solicitantes, con asistencia letrada preceptiva (Ley del Notariado, artículo 54), y de que los hijos mayores sin ingresos que convivan en el domicilio deberán consentir las medidas que les afecten (Código Civil, artículo 82).
- Contencioso: informar del requisito de acreditar el intento previo de un medio adecuado de solución de controversias (Ley Orgánica 1/2025, artículo 5) y de la posibilidad de solicitar medidas provisionales (Ley de Enjuiciamiento Civil, artículos 771 y 773).

Ejemplo (ruta mutuo acuerdo judicial con hijos): "Al presente caso le resulta de aplicación el Código Civil, en concreto los artículos 81 y 86 (divorcio de mutuo acuerdo y plazo de tres meses) y 90 (contenido del convenio regulador), y la Ley 1/2000, de Enjuiciamiento Civil, artículo 777, en su versión consolidada vigente verificada hoy. Al existir hijos menores, la vía es judicial y el Ministerio Fiscal informará sobre las medidas que les afecten. Puede consultar los textos oficiales en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"

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

### 5-A. Convenio regulador (`convenio-regulador.md`)

Los marcadores `{{NUMERO_CLAUSULA_...}}` (vivienda, liquidación, compensatoria, cargas, aprobación) se resuelven como el ordinal en letras (CUARTA, QUINTA...) que corresponda a la posición real de esa cláusula entre las que están efectivamente presentes en el documento en ese momento: cuenta solo las cláusulas numeradas ya escritas por encima (custodia/visitas/alimentos solo cuentan si V3 = Sí; la de animales de compañía solo si existen). Como las secciones se recorren en el orden fijo de esta lista, al llegar al turno de cada cláusula ya se sabe cuantas la preceden: resuélvela en ese momento, sin dejar el marcador sin resolver ni renumerar cláusulas ya escritas.

Anuncios fijos y secciones:

1. **Cónyuges (dato objetivo — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04).** Anuncio de apertura: "Procedemos a la identificación de ambos cónyuges." Ejecute prioritariamente `search_clients`. Si la ficha cubre los datos, úselos directamente; si no constan o faltan campos, solicite en bloque mediante `slot_filling_request`. Si son nuevos clientes, aplique `REG-CLI-03`. Conforme a `REG-CLI-04`, vuelque inmediatamente los datos al documento con `edit_file` (o en `create_file` si ya constaban), sustituyendo exhaustivamente los nombres de los cónyuges en todas sus apariciones a lo largo del documento entero (título/encabezado H1, comparecencia y bloque final de firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones), informe en chat de los datos incorporados y continúe de inmediato hacia la siguiente sección sin solicitar confirmación en el chat ("¿Confirmamos...?").
2. **Matrimonio (dato objetivo).** Anuncio: "Identificados los cónyuges, pasamos a los datos del matrimonio." Solicita mediante `slot_filling_request` o pregunta: (a) fecha y lugar de celebración; (b) registro civil de inscripción; (c) régimen económico (gananciales / separación de bienes). Vista previa en chat, confirmación y `edit_file`.
3. **Hijos (solo si V3 = Sí; dato objetivo — `slot_filling_request` con confirmación en el chat).** Anuncio: "Corresponde ahora identificar a los hijos comunes." Solicita en bloque mediante `slot_filling_request` nombre y fecha de nacimiento de cada hijo (solo datos imprescindibles). Vista previa en el chat, confirmación agrupada y `edit_file`.
4. **Cuidado de los hijos: custodia y visitas (solo si V3 = Sí; NEGOCIACIÓN).** Anuncio: "Pasamos a la primera de las medidas: la guarda y custodia de los hijos y el régimen de estancias." Explica antes de preguntar: patria potestad normalmente conjunta; custodia compartida (exige acuerdo de ambos, Art. 92.5 CC) frente a exclusiva con régimen de visitas para el otro progenitor (Art. 94 CC: contenido habitual — fines de semana alternos, tardes entre semana, mitad de vacaciones); el criterio rector es el interés superior del menor y el Ministerio Fiscal informará. Después pregunta la modalidad y, en turno aparte, el detalle del régimen de estancias y el lugar de entregas y recogidas.
5. **Pensión de alimentos (solo si V3 = Sí; NEGOCIACIÓN).** Anuncio: "Fijada la custodia, corresponde determinar la pensión de alimentos de los hijos." Explica antes de preguntar: concepto y proporcionalidad (Arts. 93, 142 y 146 CC), la referencia orientadora de las tablas del CGPJ (https://www.poderjudicial.es/cgpj/es/Servicios/Utilidades/Calculo-de-pensiones-alimenticias/ — orientadoras, no vinculantes), y que una pensión inexistente o irrisoria no sería aprobada (Art. 90.2 CC). El asset tiene una variante de esta cláusula para custodia exclusiva (un progenitor paga al otro) y otra para custodia compartida (fondo común o compensación por la diferencia de ingresos): usa la que corresponda según lo ya resuelto en el punto 4. Después, en turnos separados: importe mensual por hijo (o compensación, si la custodia es compartida); día de pago y cuenta; actualización (IPC por defecto); reparto de gastos extraordinarios (50 % por defecto).
6. **Animales de compañía (NEGOCIACIÓN, condicional).** Anuncio: "Procede determinar, si los hay, el destino de los animales de compañía." Pregunta si existen (sí / no en la misma frase). Si no existen, omite la cláusula sin dejar rastro. Si existen, explica el Art. 90.1.b) bis CC (destino, reparto de tiempos y cargas según el bienestar del animal) e inserta una cláusula adicional numerada, siguiendo el estilo del asset, con el pacto alcanzado.
7. **Vivienda familiar (NEGOCIACIÓN).** Anuncio: "Corresponde ahora la atribución del uso de la vivienda familiar." Explica antes de preguntar el régimen por defecto del Art. 96 CC: con hijos menores, el uso corresponde a estos y al cónyuge en cuya compañía queden hasta su mayoría de edad; sin hijos, cabe atribuirlo temporalmente al cónyuge no titular si su interés es el más necesitado de protección. Después, en turnos separados: dirección; titularidad (común / privativa / arrendada); a quién se atribuye el uso y por qué plazo o condición.
8. **Liquidación del régimen económico (NEGOCIACIÓN).** Anuncio: "Pasamos a la liquidación del régimen económico del matrimonio." Según el régimen del punto 2: en gananciales, preguntar si liquidan en el propio convenio (relación de bienes y deudas y su adjudicación) o lo aplazan; en separación de bienes, preguntar si existen bienes en proindiviso y su reparto. Si el patrimonio es complejo, aplicar el Guardrail 10 antes de redactar.
9. **Pensión compensatoria (NEGOCIACIÓN).** Anuncio: "Corresponde ahora valorar la pensión compensatoria." Explica antes de preguntar: no es automática — solo procede si la ruptura produce desequilibrio económico a uno de los cónyuges (Art. 97 CC); puede ser temporal, indefinida o prestación única; si ninguno la reclama, se hace constar la renuncia recíproca. Después pregunta si existe desequilibrio y, en su caso, en turnos separados: beneficiario e importe; duración y forma de pago.
10. **Cargas y gastos comunes (NEGOCIACIÓN).** Anuncio: "Por último, el reparto de las cargas y gastos comunes pendientes." Preguntar el reparto de deudas y cargas comunes (por mitad por defecto).
11. **Cierre del convenio (dato objetivo).** Anuncio: "Cerramos el convenio con el lugar y la fecha de firma." Preguntar lugar y fecha de firma. La cláusula de eficacia se resuelve sola con la vía ya clasificada (judicial: sometimiento a aprobación del Juzgado; notarial/LAJ: otorgamiento en escritura o decreto), sin preguntar.

### 5-B. Demanda de mutuo acuerdo (`demanda-divorcio-mutuo-acuerdo.md`, solo si V5 = convenio_y_demanda)

Al crearla, vuelca sin volver a preguntar todos los datos ya recogidos en 5-A (cónyuges, matrimonio, hijos). Secciones pendientes:

1. **Juzgado competente (dato objetivo).** Anuncio: "Pasamos a la demanda: primero, el Juzgado competente." Explica que es competente el Juzgado de Primera Instancia del último domicilio común o el del domicilio de cualquiera de los solicitantes (Art. 769.2 LEC) y pregunta el partido judicial.
2. **Representación procesal (dato objetivo — `slot_filling_request` con confirmación en el chat).** Anuncio: "Corresponde identificar la representación procesal." Solicita en bloque mediante `slot_filling_request`: (a) nombre del procurador; (b) nombre del letrado. Vista previa en chat, confirmación y `edit_file`.
3. **Cierre (dato objetivo).** Anuncio: "Cerramos la demanda con el lugar y la fecha." Preguntar lugar y fecha. La relación de documentos (certificación de matrimonio, certificaciones de nacimiento si hay hijos, convenio firmado) se rellena sola según la clasificación; muéstrala en la vista previa sin preguntar.

### 5-C. Demanda contenciosa (`demanda-divorcio-contencioso.md`)

1. **Cónyuge demandante (dato objetivo — `slot_filling_request` con confirmación en el chat).** Anuncio de apertura: "Procedemos a la identificación de la parte demandante." Solicita en bloque mediante `slot_filling_request`: (a) nombre completo; (b) DNI o NIE; (c) domicilio. Vista previa en chat, confirmación y `edit_file`.
2. **Cónyuge demandado (dato objetivo — `slot_filling_request` con confirmación en el chat).** Anuncio: "Identificada la parte demandante, pasamos a la parte demandada." Solicita en bloque mediante `slot_filling_request`: (a) nombre completo; (b) DNI o NIE; (c) domicilio. Vista previa en chat, confirmación y `edit_file`.
3. **Matrimonio (dato objetivo).** Anuncio: "Pasamos a los datos del matrimonio." Solicita mediante `slot_filling_request` o pregunta: (a) fecha y lugar de celebración; (b) registro civil; (c) régimen económico (gananciales / separación de bienes). Vista previa en chat, confirmación y `edit_file`.
4. **Hijos (solo si V3 = Sí; dato objetivo — `slot_filling_request` con confirmación en el chat).** Anuncio: "Corresponde identificar a los hijos comunes." Solicita en bloque mediante `slot_filling_request` nombre y fecha de nacimiento de cada hijo. Vista previa en chat, confirmación agrupada y `edit_file`.
5. **Cese de la convivencia e intento de MASC (dato objetivo con advertencia).** Anuncio: "Pasamos a los hechos: el cese de la convivencia y el intento de solución extrajudicial." Primero pregunta, en un turno, la fecha y circunstancias del cese (sin exigir causa: no es necesaria). Después explica el requisito de procedibilidad (Art. 5 LO 1/2025: sin acreditar el intento de MASC la demanda puede ser inadmitida) y pregunta si se intento (sí / no en la misma frase). Si sí: tipo de MASC y fechas de inicio y fin, en turnos separados. Si no y se desconoce el domicilio del demandado: activar la declaración responsable del Art. 264.4.º LEC. Si no y no concurre imposibilidad: advertir formalmente del riesgo de inadmisión y recomendar intentar un MASC antes de presentar; si el cliente decide continuar, dejar el bloque con el placeholder propio de MASC del asset (no el genérico `{{DATO_FALTANTE}}`) con la advertencia registrada.
6. **Medidas sobre los hijos (solo si V3 = Sí; NEGOCIACIÓN).** Anuncio: "Corresponde ahora concretar las medidas que se solicitaran respecto de los hijos." Explica antes de preguntar (con base en `references/cc-medidas-custodia-alimentos-arts92-97.md`): custodia exclusiva frente a compartida (en contencioso, la compartida a instancia de una sola parte es excepcional, Art. 92.8 CC), régimen de visitas habitual, y pensión de alimentos con la referencia de las tablas del CGPJ. Después, en turnos separados: custodia solicitada; régimen de estancias propuesto; alimentos solicitados (importe, pago, actualización, gastos extraordinarios).
7. **Vivienda y pensión compensatoria (NEGOCIACIÓN).** Anuncio: "Pasamos al uso de la vivienda familiar y, en su caso, a la pensión compensatoria." Explica el Art. 96 CC (régimen por defecto) y el Art. 97 CC (la compensatoria no es automática: exige desequilibrio). Después, en turnos separados: dirección de la vivienda y atribución que se solicita; si se solicita pensión compensatoria y, en su caso, importe y duración. Si hay animales de compañía (preguntar sí / no), añadir la medida de su destino.
8. **Cargas del matrimonio (NEGOCIACIÓN).** Anuncio: "Corresponde el reparto de las cargas del matrimonio." Preguntar la contribución que se solicita a las cargas y deudas comunes.
9. **Medidas provisionales (NEGOCIACIÓN).** Anuncio: "Procede decidir si se interesan medidas provisionales durante el proceso." Explica: pueden pedirse en la propia demanda (Art. 773 LEC) para que rijan custodia, alimentos, vivienda y cargas mientras se tramita el pleito. Pregunta si se interesan (sí / no). Si sí, se activa el OTROSÍ SEGUNDO en los mismos términos de las medidas definitivas.
10. **Documentación económica (dato objetivo, solo si hay medidas patrimoniales).** Anuncio: "Corresponde relacionar la documentación económica que se acompañará." Explica la regla 1.ª del Art. 770 LEC y pregunta qué documentos aportará (declaraciones tributarias, nóminas, certificaciones bancarias, títulos de propiedad).
11. **Juzgado, representación y cierre (dato objetivo; representación con confirmación agrupada).** Anuncio: "Cerramos con el Juzgado competente, la representación procesal y la firma." (a) partido judicial (explicar Art. 769.1 LEC: domicilio conyugal; si residen en partidos distintos, último domicilio del matrimonio o residencia del demandado, a elección); (b) nombre del procurador; (c) nombre del letrado -> confirmación agrupada de la representación; (d) prueba adicional para el OTROSÍ PRIMERO (testifical, pericial; si no hay, se deja la documental y el interrogatorio); (e) lugar y fecha.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre el Código Civil y la LEC en el BOE antes de redactar. Sin verificación, no proceder.
2. Verificar siempre la versión consolidada vigente de la norma en el BOE antes de redactar. Si se detectan cambios normativos, aplicar la redacción vigente en el documento a generar en el workspace sin usar versiones desactualizadas.
3. **Violencia de género o doméstica → DETENER SIEMPRE.** Si en cualquier momento del flujo (clasificación, edición incremental o conversación libre) aparecen indicios de violencia de género o doméstica entre los cónyuges o hacia los hijos, detener la generación de inmediato, advertir y escalar vía derivación formal: la competencia pasa a la Sección de Violencia sobre la Mujer (Art. 89.6 y 89.7 LOPJ, redacción LO 1/2025; Art. 44 LO 1/2004), está vedada la utilización de los MASC y de la mediación (Art. 89.9 LOPJ), no procede la custodia compartida (Art. 92.7 CC) y este flujo no es aplicable. No citar el antiguo Art. 87 ter LOPJ: fue suprimido por la LO 1/2025.
4. El mutuo acuerdo exige la conformidad de ambos cónyuges y el transcurso de tres meses desde el matrimonio (Arts. 81 y 86 CC; la excepción por riesgo del Art. 81 no se tramita por esta vía: escalar). Si no hay acuerdo, la vía es la contenciosa, que esta skill también cubre.
5. Con hijos menores no emancipados o hijos mayores con discapacidad y medidas de apoyo atribuidas a sus progenitores, el mutuo acuerdo es SIEMPRE judicial, con intervención del Ministerio Fiscal (Arts. 81 CC y 777.5 LEC). No proponer nunca la vía notarial en ese caso. Los asuntos con menores se tratan con especial cautela: el interés superior del menor prevalece sobre cualquier pacto y ningún acuerdo dañoso para los hijos será aprobado (Art. 90.2 CC).
6. Sin hijos menores ni dependientes, informar de que cabe la vía notarial o ante el Letrado de la Administración de Justicia (Arts. 82 y 87 CC; Art. 54 Ley del Notariado): más ágil, con asistencia letrada preceptiva y ante el notario del último domicilio común o del domicilio o residencia de cualquiera de los solicitantes.
7. En el contencioso, advertir del requisito de procedibilidad: acreditar el intento previo de un MASC (Art. 5 LO 1/2025 y Art. 264.4.º LEC); sin él, la demanda puede ser inadmitida. La pensión de alimentos de los hijos menores no es renunciable ni negociable a la baja hasta ser irrisoria.
8. El convenio debe cubrir todos los extremos aplicables del Art. 90.1 CC (incluido el destino de los animales de compañía si los hay). Los no aplicables se omiten con mención breve de que no proceden; no dejar cláusulas vacías.
9. Los datos faltantes conservan el nombre propio del placeholder del asset (p. ej. `{{FECHA_CESE_CONVIVENCIA}}`, `{{DOMICILIO_CONYUGE_DEMANDADO}}`); usa el marcador genérico `{{DATO_FALTANTE}}` solo para un hueco suelto dentro de una frase ya redactada que no tenga placeholder propio. Nunca generes dos `{{DATO_FALTANTE}}` en el mismo documento: al repetirse el mismo texto literal, `edit_file` ya no puede localizar uno sin el otro por `oldString` único. Nunca inventar datos, importes, fechas, la existencia o identidad de hijos, ni jurisprudencia. Nunca afirmar que el convenio está aprobado: solo lo aprueba el juez por sentencia, el LAJ por decreto o se formaliza ante notario.
10. Si el régimen económico es complejo (empresas, inmuebles en varios países, deudas relevantes), advertir de la conveniencia de asesoramiento especializado y ofrecer escalación antes de redactar la liquidación.
