---
name: ejecucion-titulos
title: Ejecución de títulos
i18n:
  en:
    name: enforcement-of-titles
    title: Enforcement of titles
    description: >
      Generates the right filing to enforce a monetary enforceable title under Book III of the
      **Civil Procedure Act (Law 1/2000, LEC)**, which governs enforcement of judgments and
      other enforceable titles, verified in the BOE: enforcement of a judicial title (final
      judgment, decree or order, including the decree closing an unopposed order-for-payment
      procedure, Art. 517.2.1 and 9 LEC), enforcement of a non-judicial title (notarial deed,
      arbitral award or mediation or MASC agreement raised to public deed, Art. 517.2.2 and 4
      LEC, with the 300-euro threshold of Art. 520), enforcement of family maintenance and
      measures under Art. 776 LEC, and subsequent request for attachment of designated assets
      and judicial asset investigation (Arts. 589, 590 and 592 LEC). Do not use for mortgage
      foreclosure (Art. 681 LEC), provisional enforcement of non-final decisions, the debtor's
      opposition, or when the debtor is in insolvency proceedings.
description: >
  Genera el escrito adecuado para ejecutar forzosamente un título ejecutivo dinerario conforme al
  Libro III de la **Ley 1/2000 de Enjuiciamiento Civil (LEC)**, que regula la ejecución forzosa de sentencias y demás títulos ejecutivos, verificado en el BOE: demanda de ejecución de título judicial (sentencia,
  decreto o auto firme, incluido el decreto que pone fin a un proceso monitorio sin oposición, Art.
  517.2.1º y 9º LEC), demanda de ejecución de título no judicial (escritura pública notarial, laudo
  arbitral o acuerdo de mediación u otro MASC elevado a escritura pública, Art. 517.2.2º y 4º LEC,
  con el límite de 300 euros del Art. 520), demanda de ejecución de pensiones y medidas de familia
  con las especialidades del Art. 776 LEC, y solicitud posterior de embargo de bienes designados y de
  investigación judicial del patrimonio (Arts. 589, 590 y 592 LEC) cuando la ejecución ya está
  despachada. NO usar para la ejecución hipotecaria (Art. 681 LEC), la ejecución provisional de
  resoluciones no firmes, la oposición del ejecutado, ni cuando el ejecutado esté en concurso de
  acreedores.
when_to_use: |
  - El usuario tiene una sentencia, decreto o auto firme y el deudor no paga voluntariamente.
  - El usuario tiene una escritura pública, un laudo arbitral o un acuerdo de mediación elevado a
    público y quiere ejecutarlo por impago.
  - El usuario tiene un monitorio que terminó sin oposición ni pago y quiere instar el despacho de
    la ejecución.
  - El usuario quiere ejecutar pensiones de alimentos, compensatoria u otras medidas de una sentencia
    o convenio de familia que no se están pagando.
  - El usuario ya tiene una ejecución despachada y quiere designar bienes, pedir el embargo o solicitar
    que el juzgado investigue el patrimonio del ejecutado.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - momento: demanda ejecutiva inicial / escrito posterior en ejecución ya despachada
  - tipo_titulo: judicial (sentencia, decreto, auto, incluido monitorio firme) / no judicial (escritura, laudo, acuerdo MASC) / familia (pensiones y medidas)
  - subtipo_no_judicial: escritura pública notarial / laudo arbitral / acuerdo de mediación u otro MASC elevado a público
  - datos_ejecutante: nombre o razón social, NIF/CIF, domicilio, procurador y letrado si proceden
  - datos_ejecutado: nombre o razón social, NIF/CIF, domicilio
  - datos_titulo: descripción, fecha, órgano o notario, número de autos o de protocolo
  - fecha_firmeza_o_vencimiento: firmeza del título judicial, o vencimiento de la obligación no judicial
  - cantidad: principal, intereses vencidos, cantidad presupuestada para intereses y costas
  - bienes_conocidos: sí / no, y su relación si los hay
  - destinatarios_averiguacion: entidades u organismos a los que se pide oficio, y razón de cada uno
  - datos_familia: concepto (alimentos / compensatoria / mixto), relación de mensualidades impagadas, si hay gastos extraordinarios no previstos
outputs:
  - demanda_ejecucion_titulo_judicial: demanda ejecutiva de título judicial o de familia en markdown, DRAFT
  - demanda_ejecucion_titulo_no_judicial: demanda ejecutiva de título no judicial en markdown, DRAFT
  - solicitud_embargo_averiguacion: escrito de designación de bienes y averiguación patrimonial en markdown, DRAFT
references:
  - references/embargo-averiguacion-inembargabilidad.md
  - references/especialidades-familia-776.md
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/lec-titulos-ejecutivos-y-plazos.md
assets:
  - assets/template-demanda-ejecucion-titulo-judicial.md
  - assets/template-demanda-ejecucion-titulo-no-judicial.md
  - assets/template-solicitud-embargo-averiguacion-patrimonial.md
---

# Ejecución Forzosa de Títulos Dinerarios

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
      "id": "momento",
      "rationale": "Resolver V1: separa la demanda ejecutiva inicial del escrito posterior en una ejecución ya despachada, que usan assets distintos.",
      "question": "¿En qué momento se encuentra la ejecución?",
      "options": [
        {"id": "demanda_inicial", "label": "Todavía no se ha instado: hay que presentar la demanda ejecutiva"},
        {"id": "escrito_posterior", "label": "La ejecución ya está despachada y hace falta un escrito de embargo o de averiguación patrimonial"}
      ]
    },
    {
      "id": "tipo_titulo",
      "rationale": "Resolver V2: el título determina el asset, el plazo de caducidad de la acción ejecutiva y los bloques condicionales aplicables.",
      "question": "¿Qué título se pretende ejecutar?",
      "options": [
        {"id": "judicial", "label": "Judicial: sentencia, decreto o auto, incluido el monitorio firme"},
        {"id": "no_judicial", "label": "No judicial: escritura pública, laudo arbitral o acuerdo de mediación"},
        {"id": "familia", "label": "De familia: pensiones de alimentos o compensatoria y demás medidas económicas"}
      ]
    },
    {
      "id": "subtipo_no_judicial",
      "rationale": "Resolver V3: activa el bloque condicional correspondiente al tipo de título no judicial.",
      "question": "Si el título no es judicial, ¿de qué clase es?",
      "show_if": {"question_id": "tipo_titulo", "option_ids": ["no_judicial"]},
      "options": [
        {"id": "escritura_publica", "label": "Escritura pública notarial"},
        {"id": "laudo_arbitral", "label": "Laudo arbitral"},
        {"id": "acuerdo_mediacion", "label": "Acuerdo de mediación u otro medio adecuado de solución de controversias elevado a público"},
        {"id": "no_procede", "label": "No procede: el título es judicial o de familia"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — respuesta a `momento`
- `V2` — respuesta a `tipo_titulo`
- `V3` — respuesta a `subtipo_no_judicial`
- `V4` — bienes conocidos del ejecutado: no se pregunta en el formulario, se recoge en la Fase 4

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalúa en este orden:

- Si V1 = escrito posterior → **HOJA AVERIGUACIÓN**: `assets/template-solicitud-embargo-averiguacion-patrimonial.md`. V2, V3 y V4 no se preguntan como vectores: los datos del título y de los bienes se recogen en prosa en la Sección 5 de esta hoja.
- Si V1 = demanda inicial y V2 = judicial → **HOJA JUDICIAL**: `assets/template-demanda-ejecucion-titulo-judicial.md`, con los bloques condicionales de familia DESACTIVADOS.
- Si V1 = demanda inicial y V2 = familia → **HOJA FAMILIA**: el mismo asset `assets/template-demanda-ejecucion-titulo-judicial.md`, con los bloques condicionales de familia ACTIVADOS (relación de mensualidades, especialidades del Art. 776, Art. 608 si son alimentos o compensatoria).
- Si V1 = demanda inicial y V2 = no judicial → **HOJA NO-JUDICIAL**: `assets/template-demanda-ejecucion-titulo-no-judicial.md`, activando según V3 el bloque de escritura pública, laudo o acuerdo de MASC elevado a público.
- Si V1 = demanda inicial y V2 = no judicial y el título alegado es un título al portador o un certificado de anotaciones en cuenta (Art. 517.2.6º y 7º LEC) → estos supuestos no tienen bloque propio en el asset: recoger la descripción en prosa, advertir de que es un supuesto poco frecuente y ofrecer escalación si el usuario no está seguro de que el documento lleve aparejada ejecución.
- Si en cualquier momento consta o se sospecha que el ejecutado está en concurso de acreedores → **DETENER**: no pueden iniciarse ejecuciones singulares contra la masa activa y las que estuvieran en curso quedan en suspenso y son nulas las actuaciones posteriores a la declaración (Arts. 142 y 143 TRLC). Advertir y escalar a concursal. No crear documento.
- Si lo que se pretende es la ejecución hipotecaria, la ejecución provisional de una resolución no firme, o redactar la oposición del ejecutado → **DETENER**: fuera de alcance. Advertir y escalar.
- **Requisito de procedibilidad (Ley Orgánica 1/2025).** Si el intento previo de un medio adecuado de solución de controversias no está acreditado y esta skill no genera por sí misma el documento que lo acredita, **deriva a `masc-acuerdos`**, que produce el requerimiento de negociación, el acta del intento, la oferta vinculante, el acuerdo transaccional y la declaración responsable de imposibilidad. Ofrece encadenar con ella antes de continuar, y advierte de que sin ese documento la demanda no se admite a trámite.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **HOJA JUDICIAL y HOJA FAMILIA (Art. 518 LEC):** confirmar la fecha de firmeza y calcular si han transcurrido menos de cinco años. Si el plazo está agotado, **detener y advertir**: no crear el documento. En pensiones periódicas, cada mensualidad tiene su propio vencimiento: la caducidad puede afectar solo a las mensualidades más antiguas; en caso de duda sobre mensualidades concretas, escalar.
- **HOJA JUDICIAL y HOJA FAMILIA (Art. 548 LEC):** confirmar que han transcurrido veinte días desde la firmeza (o desde la notificación de la aprobación del convenio). Si no han transcurrido, advertir de que el juzgado no despachara la ejecución todavía y ofrecer esperar. En familia, aplicar la misma regla de forma conservadora (ver `references/especialidades-familia-776.md`, apartado 6, y la nota de verificación manual de `references/fuentes-plantillas-validadas.md`): no afirmar que el plazo no aplica a las pensiones sin haberlo verificado.
- **HOJA NO-JUDICIAL (Art. 520 LEC):** confirmar que la cantidad reclamada excede de 300 euros y es líquida (Art. 572.1). Si no llega a 300 euros con un único título, preguntar si hay otros títulos ejecutivos de la misma naturaleza para sumarlos (Art. 520.2). Si aun así no se alcanza el límite, **detener**: no procede esta vía, advertir y ofrecer el juicio declarativo que corresponda por cuantía (derivar a `reclamacion-cantidad`).
- **HOJA NO-JUDICIAL:** si el título es un laudo o un acuerdo de mediación, si se aplica el plazo de espera de veinte días del Art. 548; si es escritura pública notarial, NO se aplica y puede ejecutarse desde el vencimiento.
- **HOJA FAMILIA (Art. 776.4ª LEC):** si el cliente incluye un gasto extraordinario que NO figura en el título con su reparto ya fijado, ese concepto NO puede reclamarse en esta misma demanda: requiere antes una declaración judicial de que tiene la consideración de gasto extraordinario. Separar ese concepto, advertir de la doble vía y no incluirlo en el desglose de la demanda ejecutiva salvo que el cliente confirme que ya cuenta con esa declaración previa.
- **TODAS LAS HOJAS (Art. 538 LEC):** verificar que el despacho se pide solo frente a quien figura como deudor en el título, o frente a quien responda personalmente por ley o afianzamiento en documento público, o frente al titular de bienes especialmente afectos. Nunca dirigir la ejecución contra un tercero no amparado por el título: genera responsabilidad por daños y perjuicios (Art. 538.4).
- **HOJA NO-JUDICIAL, título de consumo (Arts. 551.2.5º y 552 LEC):** si el título deriva de un contrato entre empresario o profesional y consumidor, advertir del control de oficio de cláusulas abusivas y, si alguna cláusula que determina la cantidad exigible es potencialmente abusiva (intereses moratorios desproporcionados, vencimiento anticipado, comisiones), ofrecer revisión por especialista antes de cerrar la cuantía.
- **MASC:** no es requisito de procedibilidad de ninguna demanda ejecutiva (Art. 5.3 LO 1/2025). No preguntar por el intento de solución previa en ninguna hoja de esta skill.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 517 a 592 de la Ley de Enjuiciamiento Civil (LEC): Art. 517 (títulos ejecutivos), Art. 548 (plazo de espera de cortesía de 20 días en resoluciones judiciales), Art. 572-574 (títulos no judiciales), Art. 589-591 (manifestación e investigación judicial de bienes) y Art. 607 (escala de inembargabilidad de salarios).
2. **Orientación Legal del Caso:**

**Informa la vía y la fuente aplicable.** Textos fijos por hoja:
   - JUDICIAL: "A su caso corresponde la ejecución de un título judicial, conforme a los artículos 517.2 y 549 de la Ley 1/2000, de Enjuiciamiento Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - NO-JUDICIAL: "A su caso corresponde la ejecución de un título no judicial, conforme a los artículos 517.2, 520 y 549 de la Ley 1/2000, de Enjuiciamiento Civil. Solo procede si la cantidad reclamada excede de 300 euros. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - FAMILIA: "A su caso corresponde la ejecución de pensiones o medidas de familia, que se tramita conforme al Libro III de la Ley 1/2000, de Enjuiciamiento Civil, con las especialidades de su artículo 776. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - AVERIGUACIÓN: "Corresponde un escrito de designación de bienes y de solicitud de investigación patrimonial dentro de la ejecución ya despachada, conforme a los artículos 589, 590 y 592 de la Ley 1/2000, de Enjuiciamiento Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - En las tres hojas de demanda, añadir: "No es necesario acreditar el intento de una solución extrajudicial previa para presentar una demanda ejecutiva (artículo 5.3 de la Ley Orgánica 1/2025)."

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

### Secciones — HOJA JUDICIAL y HOJA FAMILIA

1. **Parte ejecutante** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Comenzamos por la identificación de la parte ejecutante." Pregunta antes si intervenían abogado y procurador. Solicita en bloque mediante `slot_filling_request`: a) nombre completo o razón social; b) NIF o CIF; c) domicilio a efectos de notificaciones; d) nombre del procurador y del letrado si intervienen. Vista previa única en el chat, confirmación y `edit_file`.
2. **Parte ejecutada** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Pasamos a la identificación de la parte ejecutada." Solicita en bloque mediante `slot_filling_request`: a) nombre o razón social; b) NIF o CIF; c) domicilio. Vista previa en chat, confirmación y `edit_file`.
3. **El título ejecutivo** *(dato objetivo con validación — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Describimos ahora el título en que se funda la ejecución." Solicita en bloque mediante `slot_filling_request`: a) tipo de resolución y órgano que la dictó; b) número de autos del procedimiento; c) contenido de la condena del fallo; d) fecha de firmeza (o del decreto en monitorio sin oposición). Vista previa en chat, confirmación y `edit_file`.
4. **Plazos** *(dato objetivo con validación bloqueante)*. Anuncio fijo: "Verificamos ahora los plazos de la ejecución." Con la fecha de firmeza ya conocida, calcula tú mismo si han transcurrido los veinte días del Art. 548 y si no han pasado los cinco años del Art. 518. Si el primero no se ha cumplido, informa de la fecha en que se cumplirá y pregunta si desea continuar preparando el escrito para presentarlo entonces. Si el segundo está agotado, aplica el guardrail correspondiente y detente.
5. **Cantidad reclamada** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Pasamos a determinar la cantidad por la que se despachara la ejecución." Explica antes de pedir cifras: se reclama el principal, los intereses ya vencidos y una cantidad presupuestada para intereses de la ejecución y costas que no puede superar el 30 % de lo anterior (Art. 575 LEC), salvo justificación excepcional; si el bien a ejecutar es la vivienda habitual del ejecutado, las costas exigibles no pueden superar el 5 %. En HOJA FAMILIA, sustituye la pregunta de principal por la relación mensualidad a mensualidad (mes e importe) siguiendo `references/especialidades-familia-776.md`, apartado 3, y pregunta si el título prevé actualización periódica antes de aplicarla. Pide después, en turnos separados: a) principal (o relación de mensualidades); b) intereses vencidos y su fundamento de cálculo; c) porcentaje presupuestado para intereses y costas (por defecto, ofrece el 30 %, o el 5 % si es vivienda habitual, y pregunta si desea un porcentaje menor). Confirmación propia de cada uno.
6. **Gastos extraordinarios de familia** *(cláusula de negociación — solo HOJA FAMILIA, condicional)*. Anuncio fijo: "Concretamos si existen gastos extraordinarios que reclamar." Explica antes de preguntar: solo pueden incluirse en esta demanda los gastos extraordinarios que el título ya prevea con su reparto; los demás exigen una declaración judicial previa (Art. 776.4ª LEC) y no pueden mezclarse en este escrito. Pregunta si hay gastos extraordinarios y, para cada uno, si figura en el título con su reparto. Los que no lo estén, apártalos, adviértelo expresamente y no los incluyas en el desglose.
7. **Bienes del ejecutado** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Determinamos ahora los bienes sobre los que actuará la ejecución." El valor de V4 ya está resuelto. Si se conocen bienes: explica el orden del Art. 592 LEC (mayor facilidad de enajenación y menor onerosidad primero; la escala de nueve rangos solo si eso no es posible, y recuerda que los inmuebles ocupan el puesto 7 y los sueldos el 8) y pide la relación de bienes con datos identificativos suficientes para trabarlos sin nueva investigación. Si no se conocen: explica que se pedirá el requerimiento de manifestación de bienes del Art. 589 y, si el cliente puede indicar destinatarios concretos de oficios de investigación (Art. 590), pide cada destinatario y la razón por la que se cree que dispone de información; si no tiene ninguno, deja el OTROSÍ con la petición genérica de manifestación de bienes y advierte de que la investigación patrimonial exige destinatarios concretos que podrá completar más adelante con el escrito de la HOJA AVERIGUACIÓN.
8. **Ampliación automática** *(cláusula de negociación — explicar antes de decidir; solo si quedan plazos pendientes de vencer)*. Anuncio fijo: "Valoramos si interesa que la ejecución se amplíe automáticamente con los próximos vencimientos." Aplica solo si la obligación es de tracto sucesivo (pensiones, rentas, plazos pendientes). Explica el Art. 578 LEC: evita presentar un escrito nuevo cada vez que venza una mensualidad y no se pague. Pregunta si desea solicitarla; si la deuda está íntegramente vencida, omite la sección sin preguntar.
9. **Multas coercitivas** *(cláusula de negociación — solo HOJA FAMILIA, condicional)*. Anuncio fijo: "Valoramos si procede pedir multas coercitivas por el incumplimiento reiterado." Explica que son acumulativas al cobro de lo debido, no sustitutivas (Art. 776.1ª LEC), y que requieren incumplimiento reiterado, no un único impago. Pregunta si el incumplimiento ha sido reiterado y, si es así, incluye el OTROSÍ.
10. **Inaplicación del límite de embargo de sueldos** *(cláusula de negociación — solo HOJA FAMILIA y solo si se reclaman alimentos o compensatoria)*. Anuncio fijo: "Determinamos el régimen de embargo de sueldos aplicable." Si es alimentos: explica que el Art. 607 no se aplica por ministerio de la ley (Art. 608) y que será el tribunal quien fije la cantidad embargable; no requiere más dato. Si es compensatoria: explica que la exclusión es rogada y exige acreditar una necesidad económica; pregunta si puede acreditarla y con que medios, y si no puede, informa de que se aplicará la escala ordinaria del Art. 607.
11. **Cláusulas abusivas** *(informativo, solo si el título no judicial deriva de un contrato con consumidor — se resuelve realmente en la HOJA NO-JUDICIAL, pero si el título de familia incorporase un pacto de esa naturaleza, adviértelo igual)*.
12. **Postulación y documentos** *(dato objetivo)*. Anuncio fijo: "Cerramos con los documentos que se acompañarán." Pregunta qué documentos se aportaran además del título (poder, testimonios, certificaciones) y numéralos correlativamente con los hechos.
13. **Juzgado, lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Determinamos el juzgado competente y cerramos con el lugar y la fecha." El competente es el que conoció del asunto en primera instancia o el que homologo la transacción o acuerdo (Art. 545.1 LEC): confirma con el usuario cuál fue y no admitas sumisión a otro fuero. Lugar de firma; fecha del día salvo indicación en contrario.

### Secciones — HOJA NO-JUDICIAL

1. **Parte ejecutante** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Igual que en la HOJA JUDICIAL, pero la pregunta de postulación se formula solo si V3 = laudo_arbitral o acuerdo de mediación.
2. **Parte ejecutada** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Igual que en la HOJA JUDICIAL.
3. **El título no judicial** *(dato objetivo con validación, según V3 — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Describimos ahora el título en que se funda la ejecución." Solicita en bloque mediante `slot_filling_request` los datos identificativos del título (notario, fecha, protocolo o árbitro/institución o MASC). Vista previa en chat, confirmación y `edit_file`.
4. **Obligación y vencimiento** *(dato objetivo)*. Anuncio fijo: "Pasamos a la obligación documentada y a su vencimiento." Sub-apartados: a) descripción de la obligación; b) fecha de vencimiento. Verifica que la cantidad supera los 300 euros (Art. 520 LEC); si no, aplica la validación de presupuestos ya descrita.
5. **Liquidación por saldo** *(cláusula de negociación — solo si el título pacto liquidación unilateral, Art. 572.2 LEC)*. Anuncio fijo: "Abordamos la liquidación del saldo prevista en el título." Explica los requisitos acumulativos: notificación previa al ejecutado y al fiador, y los tres documentos del Art. 573.1. Pregunta la cláusula que lo pacta, el saldo resultante y si se acredita la notificación. Si el interés es variable, pide además las operaciones de cálculo del Art. 574.
6. **Cantidad reclamada** *(cláusula de negociación — explicar antes de decidir)*. Igual estructura que en la HOJA JUDICIAL (principal, intereses, porcentaje presupuestado con el límite del 30 %).
7. **Bienes del ejecutado** *(cláusula de negociación — explicar antes de decidir)*. Igual que en la HOJA JUDICIAL.
8. **Cláusulas abusivas** *(cláusula de negociación — solo si el título deriva de un contrato con un consumidor)*. Anuncio fijo: "Verificamos si el título está sujeto al control de cláusulas abusivas." Explica que el juzgado examinara de oficio si las cláusulas que fundan la ejecución y determinan la cantidad exigible son abusivas (Arts. 551.2.5º y 552 LEC). Pregunta si el ejecutado es consumidor y, si lo es, si alguna cláusula relevante (intereses moratorios, vencimiento anticipado, comisiones) podría ser desproporcionada; si hay duda razonable, advierte y ofrece revisión por especialista antes de continuar.
9. **Reserva de partidas dudosas** *(cláusula de negociación — solo si hay liquidación por saldo y el acreedor duda de alguna partida)*. Anuncio fijo: "Valoramos si conviene reservar alguna partida dudosa." Explica el Art. 573.3: cabe pedir el despacho por la cantidad indubitada y reservar el resto para el declarativo. Pregunta si desea acogerse a esta reserva.
10. **Ampliación automática** *(cláusula de negociación — solo si quedan plazos pendientes de vencer)*. Igual que en la HOJA JUDICIAL.
11. **Juzgado, lugar y fecha** *(dato objetivo con explicación)*. Anuncio fijo: "Determinamos el juzgado competente y cerramos con el lugar y la fecha." Explica la regla del Art. 545.2 y 545.3 LEC según V3 (laudo o mediación: lugar donde se dictó o se firmo; demás títulos: a elección del ejecutante, el de los Arts. 50-51, el del lugar de cumplimiento o el de donde haya bienes embargables, sin sumisión posible) y pide la elección. Lugar de firma; fecha del día salvo indicación en contrario.

### Secciones — HOJA AVERIGUACIÓN

1. **Datos de la ejecución en curso** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Comenzamos por identificar la ejecución ya despachada." Solicita en bloque mediante `slot_filling_request`: a) juzgado y número de autos; b) fecha del auto de despacho; c) cantidad total por la que se despacho; d) estado del cobro. Vista previa en chat, confirmación y `edit_file`.
2. **Parte ejecutante** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Igual estructura que en las otras hojas.
3. **Bienes designados** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Determinamos los bienes que se designan para el embargo." Igual explicación del orden del Art. 592 LEC. Si no hay bienes que designar, pide una breve descripción de las gestiones ya realizadas para localizarlos.
4. **Insuficiencia y petición de investigación** *(dato objetivo con validación)*. Anuncio fijo: "Justificamos ahora por qué es necesaria la investigación patrimonial." Recuerda que el requerimiento del Art. 589 solo se acuerda si el ejecutante no ha señalado bienes suficientes: si los designados en la sección anterior ya cubren la cantidad, adviértelo y desactiva esta sección.
5. **Destinatarios de los oficios** *(dato objetivo con validación de sentido — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Relacionamos los destinatarios de los oficios de investigación y la razón de cada uno." Solicita los destinatarios y sus motivos concretos (usa `references/embargo-averiguacion-inembargabilidad.md`, apartado 3). Rechaza razones genéricas. Vista previa en el chat, confirmación y `edit_file`.
6. **Límites de inembargabilidad** *(informativo, con excepción condicional)*. Anuncio fijo: "Le informo de los límites de inembargabilidad aplicables." Si la ejecución es de alimentos o de compensatoria con necesidad acreditada, aplica la excepción del Art. 608 y explica que es el tribunal quien fija la cantidad embargable; en los demás casos, recuerda la escala del Art. 607 sobre el SMI vigente verificado en la Fase 2. No requiere más dato salvo, en compensatoria, la acreditación de la necesidad económica.
7. **Multas coercitivas por incumplimiento del Art. 589** *(cláusula de negociación — condicional, solo si el ejecutado ya fue requerido y no respondió)*. Anuncio fijo: "Valoramos si procede pedir multas coercitivas por no haber manifestado bienes." Pregunta la fecha del requerimiento anterior y el detalle del incumplimiento.
8. **Ampliación de la ejecución por nuevos vencimientos** *(cláusula de negociación — condicional)*. Anuncio fijo: "Valoramos si han vencido nuevos plazos que ampliar." Si la obligación es de tracto sucesivo y han vencido nuevos plazos desde el despacho, pregunta su importe y detalle.
9. **Juzgado, lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito."

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: escrito breve (una ejecución no reargumenta el pleito), HECHOS o ALEGACIONES numerados con una idea por apartado, documentos relacionados y numerados, desglose siempre por conceptos, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre la LEC, la LO 1/2025 y el TRLC en el BOE antes de redactar (Fase 2). Sin verificación, no proceder.
2. Si se detecta una versión posterior a la registrada en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario. No usar una versión desactualizada, y nunca calcular un tramo de embargo de sueldo con un SMI de un ejercicio anterior sin verificarlo.
3. La acción ejecutiva de títulos judiciales, laudos y acuerdos de mediación caduca a los cinco años desde la firmeza (Art. 518 LEC). Si el plazo está agotado, no redactar la demanda: advertir y ofrecer escalación. Este plazo NO se aplica a la escritura pública notarial.
4. No se despachara ejecución de títulos judiciales, laudos o acuerdos de mediación dentro de los veinte días posteriores a la firmeza o notificación (Art. 548 LEC). Advertir siempre de esta espera; no aplica a los demás títulos no judiciales.
5. Solo cabe despachar ejecución frente a quien figure como deudor en el título o se encuentre en los supuestos tasados de los Arts. 538 a 544 LEC. Nunca dirigir la ejecución contra un tercero no amparado por el título: genera responsabilidad por daños y perjuicios (Art. 538.4).
6. En título no judicial, la cantidad debe exceder de 300 euros y ser líquida (Art. 520 LEC). Sin ese mínimo, no procede esta vía.
7. La cantidad presupuestada para intereses de la ejecución y costas no puede superar el 30 % de lo reclamado (5 % si es vivienda habitual del ejecutado, Art. 575.1 bis LEC), salvo justificación excepcional. Nunca redactar un desglose sin esta cantidad ni por encima de estos límites sin justificarlo.
8. En familia, los gastos extraordinarios no previstos expresamente en el título con su reparto NO pueden incluirse en la demanda ejecutiva sin la previa declaración judicial del Art. 776.4ª LEC. Separarlos siempre y no mezclarlos con el resto de la deuda.
9. En alimentos, el límite del Art. 607 no se aplica por ministerio de la ley (Art. 608). En pensión compensatoria, esa exclusión es rogada y exige acreditar necesidad económica: nunca aplicarla sin que el cliente la acredite.
10. Si consta o se sospecha que el ejecutado está en concurso de acreedores, detener de inmediato: no pueden iniciarse ejecuciones singulares contra la masa activa (Arts. 142 y 143 TRLC).
11. No es exigible acreditar el intento de un medio adecuado de solución de controversias para presentar una demanda ejecutiva (Art. 5.3 LO 1/2025). Nunca pedir ese dato en esta skill.
12. Nunca inventar datos, cuantías, fechas, números de protocolo ni jurisprudencia. Los campos no proporcionados quedan como `{{DATO}}`.
13. Cuando el impago de pensiones de familia alcance dos meses consecutivos o cuatro no consecutivos, informar de que la conducta puede tener relevancia penal (Art. 227 del Código Penal) y ofrecer escalación a un especialista en penal. Nunca redactar denuncia ni querella: excede el alcance de esta skill.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar para la ejecución hipotecaria ni para el lanzamiento derivado de ella (Art. 681 LEC y siguientes): proceso especial, fuera de alcance.
- No usar para la ejecución provisional de resoluciones no firmes (Art. 524 LEC).
- No usar para redactar la oposición del ejecutado (Arts. 556 y 557 LEC): posición contraria, fuera de alcance.
- No usar para el extenso de vivienda y ejecuciones de desahucio: derivar a `desahucio`.
- No usar para reclamar una deuda que aún no tiene título ejecutivo: derivar a `reclamacion-cantidad` (monitorio, verbal u ordinario según cuantía).
- No usar para modificar el régimen de custodia o visitas por incumplimiento reiterado (Art. 776, especialidad 3ª): derivar a `modificacion-medidas` si existe en el marketplace, o escalar.
- No usar si el usuario pide opinión jurídica sobre la estrategia de la ejecución: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
