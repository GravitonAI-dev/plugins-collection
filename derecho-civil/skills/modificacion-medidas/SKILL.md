---
name: modificacion-medidas
title: Modificación de medidas
i18n:
  en:
    name: modification-of-family-measures
    title: Modification of family measures
    description: >
      Generates the filings to MODIFY definitive measures already set in a judgment or approved
      regulatory agreement in Spain, under Article 775 of the **Civil Procedure Act (Law 1/2000,
      LEC)**, which governs the procedure to modify family measures, and Article 90.3 of the
      **Civil Code**, through two routes: (1) BY CONSENT, a petition by both parties or by one
      with the other's consent, with a proposed new regulatory agreement, under Article 777 LEC;
      and (2) CONTESTED, a petition under Article 770 LEC with proof of the MASC attempt
      (Organic Law 1/2025). It covers changes to custody and contact arrangements, increase or
      reduction of child maintenance, modification or termination of spousal maintenance (Arts.
      100 and 101 CC), use of the family home, and TERMINATION of child maintenance under
      Articles 93.2, 142 and 152 of the Civil Code, with a prior feasibility filter when the
      alleged change is voluntary or attributable to the applicant. Do not use to set measures
      for the first time, for stand-alone provisional measures, to claim unpaid maintenance
      (enforcement under Article 776 LEC), or where there are indications of gender or domestic
      violence (in which case it stops and escalates).
description: >
  Genera los escritos para MODIFICAR medidas definitivas ya fijadas en sentencia o convenio regulador
  aprobado, en España, conforme al artículo 775 de la **Ley 1/2000 de Enjuiciamiento Civil (LEC)**, que regula el procedimiento para modificar medidas de familia, y al artículo 90.3 del **Código Civil**, en sus
  dos vías: (1) CONSENSUADA — petición de ambas partes, o de una con el consentimiento de la otra,
  acompañando propuesta de nuevo convenio regulador, por el procedimiento del artículo 777 de la LEC;
  y (2) CONTENCIOSA — demanda por el procedimiento del artículo 770 de la LEC (juicio verbal con
  reglas especiales desde el RDL 6/2023), con acreditación del intento de MASC (LO 1/2025). Cubre la
  modificación de guarda y custodia y régimen de estancias, el aumento o reducción de la pensión de
  alimentos, la modificación o extinción de la pensión compensatoria (arts. 100 y 101 CC), el uso de
  la vivienda familiar, y la EXTINCIÓN de la pensión de alimentos por las causas de los artículos
  93.2, 142 y 152 del Código Civil. Aplica un filtro previo de viabilidad: si el cambio alegado es
  voluntario o imputable al propio solicitante, advierte del riesgo de desestimación antes de
  continuar. Verifica la versión vigente de las normas en el BOE antes de redactar. NO usar para
  fijar medidas por primera vez, para medidas provisionales autónomas, para reclamar pensiones
  impagadas (eso es ejecución del artículo 776 LEC), ni cuando existan indicios de violencia de
  género o doméstica (en ese caso se detiene y escala).
when_to_use: |
  - El usuario quiere cambiar la custodia, el régimen de visitas o estancias, la pensión de alimentos,
    la pensión compensatoria o el uso de la vivienda ya fijados en una sentencia o convenio anterior.
  - El usuario quiere subir o bajar la pensión que paga o cobra porque su situación económica ha
    cambiado (despido, baja de ingresos, aumento de ingresos, nuevas necesidades del hijo).
  - El usuario quiere dejar de pagar la pensión de alimentos de un hijo que ya trabaja, se ha
    independizado o ha terminado su formación.
  - El usuario quiere extinguir la pensión compensatoria porque el beneficiario se ha vuelto a casar
    o convive maritalmente con otra persona.
  - Ambas partes están de acuerdo en cambiar lo pactado y necesitan formalizarlo ante el Juzgado.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - ambito: medidas sobre los hijos / medidas entre los excónyuges / ambas
  - medida_concreta: custodia y estancias / pensión de alimentos / pensión compensatoria / vivienda
  - sentido: aumentar / reducir / extinguir (en pensión de alimentos y compensatoria)
  - modalidad: consensuada / contenciosa
  - causa_extincion: independencia económica del hijo / fin de la formación / cambio de convivencia / otra
  - resolucion_origen: tipo, fecha, juzgado, número de procedimiento y transcripción literal del pronunciamiento
  - cambio_alegado: que cambio, desde cuando y con que se acredita
  - datos_solicitante: nombre, DNI, domicilio
  - datos_otra_parte: nombre, DNI, domicilio
  - datos_hijos: nombre y fecha de nacimiento de cada hijo afectado
  - medida_nueva: redacción completa de la medida que se solicita
  - masc: en contencioso, tipo y fechas del intento de MASC o motivo de imposibilidad
  - modificacion_provisional: si se interesa (art. 775.3 LEC)
  - partido_judicial: el del Juzgado que acordó las medidas (art. 775.1 LEC)
outputs:
  - demanda_modificacion_medidas: escrito del Art. 775 LEC en markdown, DRAFT, en variante consensuada o contenciosa
  - solicitud_extincion_alimentos: escrito de extinción de la pensión de alimentos en markdown, DRAFT
references:
  - references/cc-alimentos-extincion-arts142-152.md
  - references/cc-modificacion-medidas-arts90-101.md
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/lec-modificacion-medidas-art775-776.md
  - references/requisitos-alteracion-sustancial.md
assets:
  - assets/template-demanda-modificacion-medidas.md
  - assets/template-solicitud-extincion-pension-alimentos.md
---

# Generar Escritos de Modificación de Medidas Definitivas

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
      "id": "medida_concreta",
      "rationale": "Resolver V1: determina el asset aplicable, ya que la extinción de la pensión de alimentos tiene escrito propio.",
      "question": "¿Qué medida se pretende modificar?",
      "options": [
        {"id": "custodia_estancias", "label": "Guarda y custodia o régimen de estancias"},
        {"id": "pension_alimentos", "label": "Pensión de alimentos"},
        {"id": "pension_compensatoria", "label": "Pensión compensatoria"},
        {"id": "vivienda", "label": "Uso de la vivienda familiar"},
        {"id": "varias", "label": "Varias medidas a la vez"}
      ]
    },
    {
      "id": "sentido",
      "rationale": "Resolver V2: la extinción de la pensión de alimentos enruta a su propio asset; el aumento y la reducción usan la demanda de modificación.",
      "question": "En las pensiones, ¿en qué sentido se pretende la modificación?",
      "show_if": {"question_id": "medida_concreta", "option_ids": ["pension_alimentos", "pension_compensatoria", "varias"]},
      "options": [
        {"id": "aumentar", "label": "Aumentar su importe"},
        {"id": "reducir", "label": "Reducir su importe"},
        {"id": "extinguir", "label": "Extinguirla"},
        {"id": "no_aplica", "label": "No se trata de una pensión"}
      ]
    },
    {
      "id": "modalidad",
      "rationale": "Resolver V3: activa la variante de mutuo acuerdo o la contenciosa, con su régimen procesal y su acreditación del intento de MASC.",
      "question": "¿Hay acuerdo con la otra parte sobre la modificación?",
      "options": [
        {"id": "consensuada", "label": "Sí, la modificación es consensuada"},
        {"id": "contenciosa", "label": "No hay acuerdo: vía contenciosa"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `medida_concreta`
- `V2` — `sentido`
- `V3` — `modalidad`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores necesarios y superado el filtro de viabilidad, evalúa:

- Si [V1 = pension_alimentos] y [V2 = extinguir] -> Plantilla a usar: `assets/template-solicitud-extincion-pension-alimentos.md`.
- En **todos los demás casos** (custodia y estancias, aumento o reducción de alimentos, modificación o extinción de la pensión compensatoria, uso de la vivienda, o varias medidas a la vez) -> Plantilla a usar: `assets/template-demanda-modificacion-medidas.md`.
- Si [V3 = consensuada] -> activar en el asset la variante de **mutuo acuerdo** (Art. 775.2 in fine en relación con el Art. 777 LEC): comparecencia conjunta o con consentimiento del otro, hecho del acuerdo, propuesta de nuevo convenio regulador como documento. **No** se activan los bloques de MASC, ni el OTROSÍ de prueba, ni el OTROSÍ de modificación provisional.
- Si [V3 = contenciosa] -> activar en el asset la variante **contenciosa** (Art. 775.2 en relación con el Art. 770 LEC, juicio verbal): bloque de acreditación del MASC, OTROSÍ de prueba y, si se interesa, OTROSÍ de modificación provisional. **No** se activa ningún bloque de acuerdo ni de propuesta de convenio.
- Si [V1 = varias] o se modifican varias medidas -> un único escrito con `assets/template-demanda-modificacion-medidas.md`, activando el bloque de medida adicional. **Excepción:** si una de las pretensiones es la extinción de la pensión de alimentos y las demás no, crea DOS documentos: primero la demanda de modificación, y después la solicitud de extinción, reutilizando sin volver a preguntar todos los datos ya recogidos. Advierte al cliente de que, si ambas pretensiones se dirigen contra la misma parte y ante el mismo Juzgado, su abogado valorará acumularlas en un único escrito.
- Si no existe resolución o convenio previo -> Detén el proceso (Guardrail 4) y deriva a `divorcio`. No crees documento.
- Si lo que se pretende es cobrar pensiones impagadas -> Detén el proceso (Guardrail 5) y deriva o escala. No crees documento.
- Si en cualquier momento hay indicios de violencia de género o doméstica -> Detén el proceso (Guardrail 3). No crees documento.
- **Requisito de procedibilidad (Ley Orgánica 1/2025).** Si el intento previo de un medio adecuado de solución de controversias no está acreditado y esta skill no genera por sí misma el documento que lo acredita, **deriva a `masc-acuerdos`**, que produce el requerimiento de negociación, el acta del intento, la oferta vinculante, el acuerdo transaccional y la declaración responsable de imposibilidad. Ofrece encadenar con ella antes de continuar, y advierte de que sin ese documento la demanda no se admite a trámite.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículo 775 de la Ley de Enjuiciamiento Civil (LEC, requisito de alteración sustancial y sobrevenida de circunstancias), Arts. 90.3, 91, 100, 101 y 152 del Código Civil (extinción y modificación de alimentos y compensatoria).
2. **Orientación Legal del Caso:**

**Informa la norma aplicable y las consecuencias de la ruta.** Con registro formal (usted, tono de abogado), indica qué ley y que artículos concretos aplican al caso ya clasificado, con la versión vigente verificada, e incluye SIEMPRE el enlace al BOE consultado. Además, según la ruta:
- **Siempre:** que la competencia corresponde al Juzgado que acordó las medidas definitivas (Ley 1/2000, de Enjuiciamiento Civil, artículo 775.1), y que la modificación no produce efectos hasta que sea acordada por resolución judicial, siguiendo la medida vigente plenamente exigible hasta entonces (Código Civil, artículo 148).
- **Consensuada:** que el procedimiento es el del artículo 777 de la Ley de Enjuiciamiento Civil y que es imprescindible acompañar una propuesta de nuevo convenio regulador; con hijos menores o con discapacidad dependientes, que el Ministerio Fiscal informará (Ley 1/2000, artículos 749.2 y 777.5) y que un acuerdo dañoso para los hijos no será aprobado (Código Civil, artículo 90.2).
- **Contenciosa:** que el procedimiento es el del artículo 770 de la Ley de Enjuiciamiento Civil, que se sustancia por los trámites del juicio verbal; que debe acreditarse el intento previo de un medio adecuado de solución de controversias (Ley Orgánica 1/2025, artículo 5) porque sin el la demanda puede ser inadmitida (Ley 1/2000, artículo 264.4.º); y que la otra parte puede formular reconvención con su contestación y solicitar medidas distintas o contrarias a las pedidas (Ley 1/2000, artículo 770, regla 2.ª, letra d).
- **Extinción de alimentos:** que la extinción se fundamenta en el artículo 93, párrafo segundo, del Código Civil y en el artículo 152 del mismo texto, y que la mayoría de edad no extingue por si sola la pensión.
- **Extinción o modificación de la pensión compensatoria:** que el artículo 100 del Código Civil exige alteraciones en la fortuna de uno u otro cónyuge, y que el artículo 101 tasa las causas de extinción (cese de la causa, nuevo matrimonio o convivencia marital del beneficiario).

Ejemplo (ruta contenciosa, reducción de alimentos): "Al presente caso le resulta de aplicación la Ley 1/2000, de Enjuiciamiento Civil, artículo 775, que atribuye la modificación al Juzgado que acordó las medidas definitivas y exige que las circunstancias hayan variado sustancialmente, y el Código Civil, artículos 90.3, 91, 93 y 146, en su versión consolidada vigente verificada hoy. Al no existir acuerdo, el procedimiento será el del artículo 770 de la Ley de Enjuiciamiento Civil, por los trámites del juicio verbal, y deberá acreditarse el intento previo de un medio adecuado de solución de controversias (Ley Orgánica 1/2025, artículo 5). Debe usted saber que la parte contraria podrá formular reconvención y solicitar medidas distintas de las que pedimos. Puede consultar los textos oficiales en: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 y https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"

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

Recorre secuencialmente la lista que corresponda al documento activo (5-A demanda de modificación, 5-B solicitud de extinción de alimentos). Por cada sección incompleta, aplica el Ciclo de Edición Incremental del sistema global.

**Anuncio de sección y encadenamiento:** al terminar una sección y confirmar su edición en disco, emite en ese mismo turno el anuncio fijo de la sección que se abre y lanza de inmediato su formulario `slot_filling_request` (si es grupo de datos) o su planteamiento en chat (si es negociación). No pidas permiso para pasar de sección: informa y continúa. Los anuncios nombran la sección SUSTANTIVA del documento, nunca la mecánica interna. La vista previa y la confirmación siempre van en el chat.

**Diálogo y acuerdo en las secciones de negociación:** las secciones marcadas como (NEGOCIACIÓN) implican una decisión con consecuencias legales. En ellas NO te límites a registrar el valor que de el cliente: primero explica en el chat, de forma breve y con base en `references/cc-modificacion-medidas-arts90-101.md`, `references/cc-alimentos-extincion-arts142-152.md` y `references/requisitos-alteracion-sustancial.md`, el régimen legal y las consecuencias de cada opción, y solo después formula la pregunta. Confirma que el cliente entiende y está de acuerdo antes de escribir. Nunca registres una pretensión manifiestamente inviable sin haberla advertido, ni un pacto dañoso para los hijos (Art. 90.2 CC).

**Validación de sentido, no solo de formato:** razona si cada respuesta tiene sentido en el contexto (una fecha de resolución posterior a hoy, una edad del alimentista incompatible con la fecha de nacimiento aportada, un DNI con forma de nombre o un importe absurdo no se escriben en el documento: señala por qué no encaja y pide aclaración).

### 5-A. Demanda de modificación de medidas (`demanda-modificacion-medidas.md`)

Anuncios fijos y secciones:

1. **Parte solicitante (dato objetivo, búsqueda prioritaria con `search_clients`, recogida con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04).** Anuncio de apertura: "Procedemos a la identificación de la parte que solicita la modificación." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: (a) nombre completo; (b) DNI o NIE; (c) domicilio actual. Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Conforme a `REG-CLI-04`, vuelca de inmediato al documento con `edit_file` (o ya volcado en `create_file`) de forma directa sin requerir confirmación en chat de los datos de la parte, sustituyendo exhaustivamente los nombres en todas sus apariciones a lo largo del documento (título/encabezado H1, comparecencia y firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones).
2. **Otra parte (dato objetivo, búsqueda prioritaria con `search_clients`, recogida con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04).** Anuncio: "Identificada la parte solicitante, pasamos a la otra parte del procedimiento." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: (a) nombre completo; (b) DNI o NIE; (c) domicilio actual. Si se desconoce el domicilio y la vía es contenciosa, queda con su propio placeholder de domicilio (no el genérico `{{DATO_FALTANTE}}`) y habilita la declaración responsable del Art. 264.4.º LEC en la sección de MASC. Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca de inmediato al documento con `edit_file` sin turno de confirmación en chat per `REG-CLI-04`, sustituyendo exhaustivamente los nombres en todas sus apariciones (título H1, comparecencia y firmas).
3. **Resolución o convenio de origen (dato objetivo, recogida con `slot_filling_request`, confirmación en chat).** Anuncio: "Pasamos ahora a identificar la resolución que fijo las medidas vigentes, que es el punto de partida del escrito." Solicita en lote vía `slot_filling_request`: (a) tipo de resolución y fecha (sentencia / decreto / auto); (b) Juzgado que la dictó y número de procedimiento; (c) si las medidas se fijaron aprobando un convenio regulador o en defecto de acuerdo; (d) **transcripción literal del pronunciamiento que se quiere modificar** (o placeholder `{{TRANSCRIPCION_MEDIDA_VIGENTE}}` si no lo tiene a mano). Vista previa y confirmación en chat antes de `edit_file`.
4. **Hijos afectados (solo si los hay; dato objetivo, recogida en lote con `slot_filling_request`, confirmación en chat).** Anuncio: "Corresponde ahora identificar a los hijos a los que afectan las medidas." Solicita de una vez vía `slot_filling_request` el nombre y fecha de nacimiento de cada hijo. Pide SOLO los datos imprescindibles; no recabes datos adicionales de menores. Vista previa y confirmación en el chat.
5. **La alteración de circunstancias (NEGOCIACIÓN).** Anuncio: "Pasamos al núcleo del escrito: la alteración de circunstancias que justifica la modificación." Ya conoces el cambio, la fecha y la prueba por el filtro de viabilidad: **no los vuelvas a preguntar**. Explica antes de continuar que la alteración debe ser sustancial, sobrevenida, acreditada, no imputable a quien la alega y con vocación de permanencia, y que el escrito debe emparejar cada cambio con su documento. Después, en turnos separados: (a) muestra la redacción propuesta del hecho de la alteración, con la fecha, y pide confirmación o corrección; (b) la relación concreta de documentos que se acompañarán para acreditarla, orientando con la tabla de prueba típica si el cliente duda.
6. **Documentación económica (dato objetivo, solo si la medida es de carácter patrimonial).** Anuncio: "Corresponde relacionar la documentación económica que se acompañará al escrito." Explica la regla 1.ª del Art. 770 LEC (ambas partes deben aportar documentación económica, y debe acreditarse la resolución o acuerdo del que resulta el uso de la vivienda familiar si existe) y pregunta qué documentos aportará.
7. **Intento de solución extrajudicial (solo si la vía es contenciosa; dato objetivo con advertencia).** Anuncio: "Pasamos al intento previo de solución extrajudicial, que es requisito para admitir la demanda." Explica el requisito (Art. 5 LO 1/2025: sin acreditar el intento la demanda puede ser inadmitida) y precisa que debe existir identidad entre lo negociado y lo que se pide en la demanda. Pregunta si se intento (sí / no en la misma frase). Si sí: tipo de MASC y fechas de inicio y fin, en turnos separados. Si no y se desconoce el domicilio de la otra parte: activar la declaración responsable del Art. 264.4.º LEC. Si no y no concurre imposibilidad: advertir formalmente del riesgo de inadmisión y recomendar intentarlo antes de presentar; si el cliente decide continuar, dejar el bloque con el placeholder propio de MASC del asset (no el genérico `{{DATO_FALTANTE}}`) con la advertencia registrada.
8. **Acuerdo alcanzado y propuesta de nuevo convenio (solo si la vía es consensuada; NEGOCIACIÓN).** Anuncio: "Corresponde ahora reflejar el acuerdo alcanzado y la propuesta de nuevo convenio." Explica que la vía del Art. 777 LEC exige acompañar una propuesta de nuevo convenio regulador, que hasta su aprobación judicial la medida vigente sigue rigiendo, y que con hijos menores el Ministerio Fiscal informará y no se aprobara un acuerdo dañoso para ellos. Pregunta si la otra parte ha prestado su consentimiento por escrito y en que términos concretos se ha alcanzado el acuerdo. Si el acuerdo perjudica gravemente a los hijos, adviértelo y propón alternativa antes de escribirlo.
9. **Redacción de la medida nueva (NEGOCIACIÓN).** Anuncio: "Corresponde ahora redactar exactamente la medida que se solicita en sustitución de la vigente." Explica antes de preguntar: la medida debe pedirse redactada de forma completa y autónoma, tal como se quiere que figure en el fallo (si es económica: importe en número y letra, día de pago, cuenta de abono y sistema de actualización); y **advierte expresamente de los efectos temporales** — la modificación no rige hacia atrás de la interposición de la demanda (Art. 148 CC), lo devengado conforme a la resolución anterior sigue siendo exigible y ejecutable, y dejar de pagar por cuenta propia genera una deuda ejecutable con posibles consecuencias penales. Después pregunta, en turnos separados: (a) el contenido de la medida solicitada; (b) la fecha de efectos que se interesa. Si se modifican varias medidas, repite el ciclo por cada una.
10. **Modificación provisional (solo si la vía es contenciosa; NEGOCIACIÓN).** Anuncio: "Procede decidir si se interesa que la medida nueva rija ya durante la tramitación del procedimiento." Explica el Art. 775.3 LEC (cabe pedir en la propia demanda la modificación provisional, que se tramita conforme al Art. 773 LEC con comparecencia de las partes) y en que casos conviene. Pregunta si se interesa (sí / no) y, si sí, cuál es la situación de urgencia que la justifica.
11. **Prueba (solo si la vía es contenciosa; dato objetivo).** Anuncio: "Corresponde concretar la prueba que se propondrá." Explica que la documental aportada y el interrogatorio de la parte demandada se proponen siempre, y pregunta qué prueba adicional desea proponer (testifical, pericial, oficios a organismos). Si no hay ninguna, se deja solo la documental y el interrogatorio.
12. **Juzgado, representación y cierre (dato objetivo; representación con `slot_filling_request`).** Anuncio: "Cerramos con el Juzgado competente, la representación procesal y la firma." (a) confirmar el Juzgado y partido judicial — explica que es competente el que acordó las medidas definitivas (Art. 775.1 LEC) y, si el hijo o las partes han trasladado su residencia a otro partido judicial, adviértelo y aplica la fila correspondiente de Escalación; (b) datos de la representación procesal vía `slot_filling_request` (nombre del procurador y letrado); (c) lugar y fecha. Vista previa y confirmación en chat.

### 5-B. Solicitud de extinción de la pensión de alimentos (`solicitud-extincion-pension-alimentos.md`)

1. **Parte solicitante (dato objetivo, búsqueda prioritaria con `search_clients`, recogida con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04).** Anuncio de apertura: "Procedemos a la identificación de la parte que solicita la extinción." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: (a) nombre completo; (b) DNI o NIE; (c) domicilio. Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Conforme a `REG-CLI-04`, vuelca de inmediato a disco con `edit_file` (o ya volcado en `create_file`) sin requerir confirmación en chat de los datos de la parte.
2. **Otra parte (dato objetivo, búsqueda prioritaria con `search_clients`, recogida con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04).** Anuncio: "Identificada la parte solicitante, pasamos al progenitor que percibe la pensión." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: (a) nombre completo; (b) DNI o NIE; (c) domicilio. Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca de inmediato a disco con `edit_file` sin turno de confirmación en chat per `REG-CLI-04`.
3. **Resolución o convenio de origen (dato objetivo, recogida con `slot_filling_request`, confirmación en chat).** Anuncio: "Pasamos a identificar la resolución que fijo la pensión, que es el punto de partida del escrito." Mismos datos que en 5-A.3 vía `slot_filling_request`, incluida la transcripción literal del pronunciamiento. Vista previa y confirmación en chat.
4. **Alimentista (dato objetivo, recogida con `slot_filling_request`, confirmación en chat).** Anuncio: "Corresponde identificar al hijo a cuyo favor se fijo la pensión." Solicita vía `slot_filling_request`: (a) nombre; (b) fecha de nacimiento. Calcula tú la edad a partir de la fecha de nacimiento y de la fecha del sistema: **no la preguntes**. Si la edad calculada no encaja con lo que dijo el cliente, señálalo y pide aclaración antes de escribir. Vista previa y confirmación en chat.
5. **Causa de extinción (NEGOCIACIÓN).** Anuncio: "Pasamos al núcleo del escrito: la causa por la que procede extinguir la pensión." Explica antes de preguntar, con base en `references/cc-alimentos-extincion-arts142-152.md`: que la mayoría de edad no extingue por si sola la pensión; que el hijo mayor que **convive** en el domicilio familiar y **carece de ingresos propios** conserva el derecho (Art. 93, párrafo segundo, CC); que basta con que decaiga uno de esos dos presupuestos; que los alimentos alcanzan a la formación no terminada por causa no imputable al hijo (Art. 142 CC); y que la causa nuclear de cese es que el alimentista disponga de medios propios suficientes para su subsistencia (Art. 152.3.º CC). Después, según la causa ya clasificada, pregunta en turnos separados los datos que el bloque condicional requiere: en independencia económica, ocupación, empleador, fecha de inicio e ingresos aproximados, y si ha dejado de convivir, desde cuando y dónde reside; en fin de formación, fecha y circunstancia de la finalización o abandono; en cambio de convivencia, desde cuando y en que domicilio. **Si de las respuestas resulta que el hijo sigue conviviendo y sin ingresos propios, detén la redacción y adviértelo: la extinción no prosperaría.**
6. **Acreditación de la causa (dato objetivo).** Anuncio: "Corresponde relacionar la documentación que acreditará la causa de extinción." Pregunta qué documentos aportará, orientando con la tabla de prueba típica de `references/requisitos-alteracion-sustancial.md`. Si el cliente no dispone de ninguno, adviértele de que la pretensión no prosperara sin prueba y sugiere el oficio a la Tesorería General de la Seguridad Social como prueba a proponer.
7. **Requerimiento extrajudicial previo (NEGOCIACIÓN, condicional).** Anuncio: "Procede valorar si se ha dirigido o se dirigirá un requerimiento previo a la otra parte." Explica su doble utilidad (puede evitar el pleito, y documentado como negociación sirve para acreditar el intento de MASC del Art. 5 LO 1/2025 si versa sobre el mismo objeto) y **advierte expresamente de que el requerimiento no autoriza a dejar de pagar**. Pregunta si ya se envío (sí / no en la misma frase). Si sí: fecha, medio y resultado, en turnos separados. Si no y la vía es contenciosa, informa de que conviene enviarlo antes de presentar y de que puede servir simultáneamente de MASC.
8. **Intento de solución extrajudicial (solo si la vía es contenciosa; dato objetivo con advertencia).** Anuncio: "Pasamos al intento previo de solución extrajudicial, que es requisito para admitir la demanda." Mismo tratamiento que en 5-A.7. Si el requerimiento de la sección anterior cumple los requisitos del Art. 5.1 LO 1/2025 (negociación directa sobre el mismo objeto, con plazo de respuesta), reutilízalo como acreditación y no vuelvas a preguntar sus fechas.
9. **Fecha de efectos solicitada (NEGOCIACIÓN).** Anuncio: "Corresponde determinar desde que fecha se solicita la extinción." Explica antes de preguntar: por regla general la extinción no rige hacia atrás de la interposición de la demanda (Art. 148 CC); la práctica de las Audiencias no es uniforme sobre si opera desde la demanda o desde la sentencia, por lo que conviene solicitarla desde la fecha en que se produjo la causa y, subsidiariamente, desde la interposición; y hasta que haya resolución la pensión se sigue debiendo íntegramente. Después pregunta la fecha de efectos que desea interesar.
10. **Subsistencia del resto de medidas (dato objetivo).** Anuncio: "Corresponde precisar que medidas se mantienen inalteradas." Pregunta si existen otros hijos con pensión o si subsisten otras medidas que no se ven afectadas, para activar los bloques correspondientes. Si hay otros hijos menores con pensión, deja constancia expresa de que la extinción no les alcanza.
11. **Prueba, Juzgado, representación y cierre (dato objetivo; representación con `slot_filling_request`).** Anuncio: "Cerramos con la prueba, el Juzgado competente, la representación procesal y la firma." (a) prueba adicional que se propondrá (solo en vía contenciosa; explicar la utilidad del oficio a la Tesorería General de la Seguridad Social para acreditar la vida laboral del hijo); (b) confirmar el Juzgado y partido judicial (Art. 775.1 LEC); (c) representación procesal vía `slot_filling_request` (nombre del procurador y del letrado); (d) lugar y fecha. Vista previa y confirmación en chat.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre el Código Civil y la LEC en el BOE antes de redactar. Sin verificación, no proceder.
2. Verificar siempre la versión consolidada vigente de la norma en el BOE antes de redactar. Si se detectan cambios normativos, aplicar la redacción vigente en el documento a generar en el workspace sin usar versiones desactualizadas.
3. **Violencia de género o doméstica → DETENER SIEMPRE.** Si en cualquier momento del flujo aparecen indicios de violencia de género o doméstica entre las partes o hacia los hijos, detener la generación de inmediato, advertir y escalar vía derivación formal: la competencia pasa a la Sección de Violencia sobre la Mujer, que conoce expresamente de la modificación de medidas (Art. 89.6.a) y 89.6.c) LOPJ, redacción LO 1/2025; Art. 89.7 competencia exclusiva y excluyente; Art. 44 LO 1/2004), y está vedada la utilización de los MASC y de la mediación (Art. 89.9 LOPJ). No citar el antiguo Art. 87 ter LOPJ: fue suprimido por la LO 1/2025.
4. **Debe existir una resolución o convenio previo.** Esta skill modifica medidas YA fijadas. Si no hay sentencia, decreto o convenio regulador aprobado anterior, no procede modificación: es un primer establecimiento de medidas y corresponde a `divorcio`. Verificarlo antes de crear ningún documento.
5. **Impago no es modificación.** Reclamar pensiones impagadas es ejecución forzosa (Art. 776 LEC), no modificación. Si lo que el cliente quiere es cobrar atrasos, esta skill no es la vía: derivar o escalar. La única pasarela es el Art. 776, regla 3.ª LEC (el incumplimiento reiterado del régimen de visitas puede fundamentar la modificación del régimen de guarda y visitas). Un mismo caso puede necesitar ambas cosas: advertirlo y separarlas, nunca mezclarlas en un solo escrito.
6. **Filtro de imputabilidad (Fase 1.B), obligatorio antes de redactar.** Si el cambio alegado es voluntario o imputable al propio solicitante (baja voluntaria en el empleo, reducción de jornada sin causa, cese de actividad por decisión propia, asunción voluntaria de nuevas cargas), advertir formalmente del riesgo de desestimación ANTES de continuar, con base en `references/requisitos-alteracion-sustancial.md`. Solo continuar si el cliente lo confirma expresamente, y dejar el riesgo reflejado en el escrito y en las advertencias finales.
7. **La mayoría de edad no extingue los alimentos.** El hijo mayor de edad que convive en el domicilio familiar y carece de ingresos propios conserva el derecho (Art. 93, párrafo segundo, CC), y los alimentos alcanzan a la formación no terminada por causa no imputable al hijo (Art. 142 CC). Si el cliente pide extinguir por el mero cumplimiento de los dieciocho años, corregirlo y explicar los presupuestos antes de redactar.
8. **Efectos no retroactivos: advertirlo siempre.** La modificación no despliega efectos hacia atrás de la interposición de la demanda (Art. 148 CC), y lo devengado conforme a la resolución anterior sigue siendo exigible y ejecutable. Advertir expresamente que **dejar de pagar por cuenta propia mientras se tramita el procedimiento genera una deuda ejecutable (Art. 776 LEC) y puede tener consecuencias penales**. La práctica de las Audiencias no es uniforme sobre si la modificación rige desde la demanda o desde la sentencia: no zanjar ese punto como si fuera pacifico.
9. **Riesgo de reconvención: advertirlo antes de que el cliente decida presentar.** En la vía contenciosa, la otra parte puede pedir con su contestación medidas distintas o contrarias a las solicitadas (Art. 770, regla 2.ª, letra d) LEC).
10. La pensión de alimentos de los hijos menores no es renunciable ni negociable a la baja hasta hacerla irrisoria. En la vía consensuada, un nuevo convenio dañoso para los hijos no será aprobado (Art. 90.2 CC): advertir y proponer alternativa válida.
11. Los datos faltantes conservan el nombre propio del placeholder del asset (p. ej. `{{TRANSCRIPCION_MEDIDA_VIGENTE}}`, `{{DOMICILIO_OTRA_PARTE}}`); usa el marcador genérico `{{DATO_FALTANTE}}` solo para un hueco suelto dentro de una frase ya redactada que no tenga placeholder propio. Nunca generes dos `{{DATO_FALTANTE}}` en el mismo documento: al repetirse el mismo texto literal, `edit_file` ya no puede localizar uno sin el otro por `oldString` único. **Nunca inventar** datos, importes, fechas, el contenido del pronunciamiento de origen, ni jurisprudencia. La transcripción literal de la medida vigente se toma de lo que aporte el cliente: si no la tiene delante, queda con su propio placeholder y se le pide que la copie de su resolución. Nunca afirmar que la modificación está concedida: solo la concede el juez por sentencia.
12. **Prohibido citar sentencias.** Los requisitos de la alteración sustancial se enuncian como criterio general con base en los Arts. 775.1 LEC, 90.3 y 91 in fine CC. No citar resoluciones del Tribunal Supremo ni de Audiencias Provinciales sin haberlas verificado en CENDOJ en la misma sesión.
