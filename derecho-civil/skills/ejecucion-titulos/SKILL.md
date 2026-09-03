---
name: ejecucion-titulos
description: >
  Genera el escrito adecuado para ejecutar forzosamente un titulo ejecutivo dinerario conforme al
  Libro III de la LEC verificado en el BOE: demanda de ejecucion de titulo judicial (sentencia,
  decreto o auto firme, incluido el decreto que pone fin a un proceso monitorio sin oposicion, Art.
  517.2.1º y 9º LEC), demanda de ejecucion de titulo no judicial (escritura publica notarial, laudo
  arbitral o acuerdo de mediacion u otro MASC elevado a escritura publica, Art. 517.2.2º y 4º LEC,
  con el limite de 300 euros del Art. 520), demanda de ejecucion de pensiones y medidas de familia
  con las especialidades del Art. 776 LEC, y solicitud posterior de embargo de bienes designados y de
  investigacion judicial del patrimonio (Arts. 589, 590 y 592 LEC) cuando la ejecucion ya esta
  despachada. NO usar para la ejecucion hipotecaria (Art. 681 LEC), la ejecucion provisional de
  resoluciones no firmes, la oposicion del ejecutado, ni cuando el ejecutado este en concurso de
  acreedores.
when_to_use: |
  - El usuario tiene una sentencia, decreto o auto firme y el deudor no paga voluntariamente.
  - El usuario tiene una escritura publica, un laudo arbitral o un acuerdo de mediacion elevado a
    publico y quiere ejecutarlo por impago.
  - El usuario tiene un monitorio que termino sin oposicion ni pago y quiere instar el despacho de
    la ejecucion.
  - El usuario quiere ejecutar pensiones de alimentos, compensatoria u otras medidas de una sentencia
    o convenio de familia que no se estan pagando.
  - El usuario ya tiene una ejecucion despachada y quiere designar bienes, pedir el embargo o solicitar
    que el juzgado investigue el patrimonio del ejecutado.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - momento: demanda ejecutiva inicial / escrito posterior en ejecucion ya despachada
  - tipo_titulo: judicial (sentencia, decreto, auto, incluido monitorio firme) / no judicial (escritura, laudo, acuerdo MASC) / familia (pensiones y medidas)
  - subtipo_no_judicial: escritura publica notarial / laudo arbitral / acuerdo de mediacion u otro MASC elevado a publico
  - datos_ejecutante: nombre o razon social, NIF/CIF, domicilio, procurador y letrado si proceden
  - datos_ejecutado: nombre o razon social, NIF/CIF, domicilio
  - datos_titulo: descripcion, fecha, organo o notario, numero de autos o de protocolo
  - fecha_firmeza_o_vencimiento: firmeza del titulo judicial, o vencimiento de la obligacion no judicial
  - cantidad: principal, intereses vencidos, cantidad presupuestada para intereses y costas
  - bienes_conocidos: si / no, y su relacion si los hay
  - destinatarios_averiguacion: entidades u organismos a los que se pide oficio, y razon de cada uno
  - datos_familia: concepto (alimentos / compensatoria / mixto), relacion de mensualidades impagadas, si hay gastos extraordinarios no previstos
outputs:
  - demanda_ejecucion_titulo_judicial: demanda ejecutiva de titulo judicial o de familia en markdown, DRAFT
  - demanda_ejecucion_titulo_no_judicial: demanda ejecutiva de titulo no judicial en markdown, DRAFT
  - solicitud_embargo_averiguacion: escrito de designacion de bienes y averiguacion patrimonial en markdown, DRAFT
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

# Ejecucion Forzosa de Titulos Dinerarios

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
    "tipo_titulo": {
      "type": "string",
      "description": "Naturaleza del t\u00edtulo ejecutivo (V2)",
      "enum": [
        "titulo_judicial",
        "titulo_no_judicial",
        "familia_pensiones"
      ]
    },
    "momento_procesal": {
      "type": "string",
      "description": "Momento procesal del escrito (V1)",
      "enum": [
        "demanda_inicial",
        "mejora_embargo"
      ]
    },
    "bienes_conocidos": {
      "type": "string",
      "description": "Bienes del ejecutado conocidos (V4)",
      "enum": [
        "con_bienes",
        "sin_bienes"
      ]
    }
  },
  "required": [
    "tipo_titulo",
    "momento_procesal"
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = 2 → **HOJA AVERIGUACION**: `assets/template-solicitud-embargo-averiguacion-patrimonial.md`. V2, V3 y V4 no se preguntan como vectores: los datos del titulo y de los bienes se recogen en prosa en la Seccion 5 de esta hoja.
- Si V1 = 1 y V2 = 1 → **HOJA JUDICIAL**: `assets/template-demanda-ejecucion-titulo-judicial.md`, con los bloques condicionales de familia DESACTIVADOS.
- Si V1 = 1 y V2 = 3 → **HOJA FAMILIA**: el mismo asset `assets/template-demanda-ejecucion-titulo-judicial.md`, con los bloques condicionales de familia ACTIVADOS (relacion de mensualidades, especialidades del Art. 776, Art. 608 si son alimentos o compensatoria).
- Si V1 = 1 y V2 = 2 → **HOJA NO-JUDICIAL**: `assets/template-demanda-ejecucion-titulo-no-judicial.md`, activando segun V3 el bloque de escritura publica, laudo o acuerdo de MASC elevado a publico.
- Si V1 = 1 y V2 = 2 y el titulo alegado es un titulo al portador o un certificado de anotaciones en cuenta (Art. 517.2.6º y 7º LEC) → estos supuestos no tienen bloque propio en el asset: recoger la descripcion en prosa, advertir de que es un supuesto poco frecuente y ofrecer escalacion si el usuario no esta seguro de que el documento lleve aparejada ejecucion.
- Si en cualquier momento consta o se sospecha que el ejecutado esta en concurso de acreedores → **DETENER**: no pueden iniciarse ejecuciones singulares contra la masa activa y las que estuvieran en curso quedan en suspenso y son nulas las actuaciones posteriores a la declaracion (Arts. 142 y 143 TRLC). Advertir y escalar a concursal. No crear documento.
- Si lo que se pretende es la ejecucion hipotecaria, la ejecucion provisional de una resolucion no firme, o redactar la oposicion del ejecutado → **DETENER**: fuera de alcance. Advertir y escalar.

### Validacion de presupuestos (interno, antes del Punto 3)

- **HOJA JUDICIAL y HOJA FAMILIA (Art. 518 LEC):** confirmar la fecha de firmeza y calcular si han transcurrido menos de cinco anos. Si el plazo esta agotado, **detener y advertir**: no crear el documento. En pensiones periodicas, cada mensualidad tiene su propio vencimiento: la caducidad puede afectar solo a las mensualidades mas antiguas; en caso de duda sobre mensualidades concretas, escalar.
- **HOJA JUDICIAL y HOJA FAMILIA (Art. 548 LEC):** confirmar que han transcurrido veinte dias desde la firmeza (o desde la notificacion de la aprobacion del convenio). Si no han transcurrido, advertir de que el juzgado no despachara la ejecucion todavia y ofrecer esperar. En familia, aplicar la misma regla de forma conservadora (ver `references/especialidades-familia-776.md`, apartado 6, y la nota de verificacion manual de `references/fuentes-plantillas-validadas.md`): no afirmar que el plazo no aplica a las pensiones sin haberlo verificado.
- **HOJA NO-JUDICIAL (Art. 520 LEC):** confirmar que la cantidad reclamada excede de 300 euros y es liquida (Art. 572.1). Si no llega a 300 euros con un unico titulo, preguntar si hay otros titulos ejecutivos de la misma naturaleza para sumarlos (Art. 520.2). Si aun asi no se alcanza el limite, **detener**: no procede esta via, advertir y ofrecer el juicio declarativo que corresponda por cuantia (derivar a `reclamacion-cantidad`).
- **HOJA NO-JUDICIAL:** si el titulo es un laudo o un acuerdo de mediacion, si se aplica el plazo de espera de veinte dias del Art. 548; si es escritura publica notarial, NO se aplica y puede ejecutarse desde el vencimiento.
- **HOJA FAMILIA (Art. 776.4ª LEC):** si el cliente incluye un gasto extraordinario que NO figura en el titulo con su reparto ya fijado, ese concepto NO puede reclamarse en esta misma demanda: requiere antes una declaracion judicial de que tiene la consideracion de gasto extraordinario. Separar ese concepto, advertir de la doble via y no incluirlo en el desglose de la demanda ejecutiva salvo que el cliente confirme que ya cuenta con esa declaracion previa.
- **TODAS LAS HOJAS (Art. 538 LEC):** verificar que el despacho se pide solo frente a quien figura como deudor en el titulo, o frente a quien responda personalmente por ley o afianzamiento en documento publico, o frente al titular de bienes especialmente afectos. Nunca dirigir la ejecucion contra un tercero no amparado por el titulo: genera responsabilidad por danos y perjuicios (Art. 538.4).
- **HOJA NO-JUDICIAL, titulo de consumo (Arts. 551.2.5º y 552 LEC):** si el titulo deriva de un contrato entre empresario o profesional y consumidor, advertir del control de oficio de clausulas abusivas y, si alguna clausula que determina la cantidad exigible es potencialmente abusiva (intereses moratorios desproporcionados, vencimiento anticipado, comisiones), ofrecer revision por especialista antes de cerrar la cuantia.
- **MASC:** no es requisito de procedibilidad de ninguna demanda ejecutiva (Art. 5.3 LO 1/2025). No preguntar por el intento de solucion previa en ninguna hoja de esta skill.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 517 a 592 de la Ley de Enjuiciamiento Civil (LEC): Art. 517 (títulos ejecutivos), Art. 548 (plazo de espera de cortesía de 20 días en resoluciones judiciales), Art. 572-574 (títulos no judiciales), Art. 589-591 (manifestación e investigación judicial de bienes) y Art. 607 (escala de inembargabilidad de salarios).
2. **Orientación Legal del Caso:**
Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la via y la fuente aplicable.** Textos fijos por hoja:
   - JUDICIAL: "A su caso corresponde la ejecucion de un titulo judicial, conforme a los articulos 517.2 y 549 de la Ley 1/2000, de Enjuiciamiento Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - NO-JUDICIAL: "A su caso corresponde la ejecucion de un titulo no judicial, conforme a los articulos 517.2, 520 y 549 de la Ley 1/2000, de Enjuiciamiento Civil. Solo procede si la cantidad reclamada excede de 300 euros. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - FAMILIA: "A su caso corresponde la ejecucion de pensiones o medidas de familia, que se tramita conforme al Libro III de la Ley 1/2000, de Enjuiciamiento Civil, con las especialidades de su articulo 776. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - AVERIGUACION: "Corresponde un escrito de designacion de bienes y de solicitud de investigacion patrimonial dentro de la ejecucion ya despachada, conforme a los articulos 589, 590 y 592 de la Ley 1/2000, de Enjuiciamiento Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - En las tres hojas de demanda, anadir: "No es necesario acreditar el intento de una solucion extrajudicial previa para presentar una demanda ejecutiva (articulo 5.3 de la Ley Organica 1/2025)."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla del sistema, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio.
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-demanda-ejecucion-titulo-judicial.md`).
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

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma parte se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las clausulas de negociacion se explican y se confirman una a una. **La vista previa y la confirmacion agrupada de una parte se emiten en el turno SIGUIENTE a la respuesta del ultimo sub-apartado, nunca en el mismo turno en que aun se esta preguntando ese ultimo dato**: primero se pregunta y se recibe la respuesta, y solo despues, en el turno posterior, se muestra la vista previa conjunta y se pide la confirmacion.

### Secciones — HOJA JUDICIAL y HOJA FAMILIA

1. **Parte ejecutante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la parte ejecutante." Sub-apartados, uno por turno: a) nombre completo o razon social; b) NIF o CIF; c) domicilio a efectos de notificaciones; d) nombre del procurador y del letrado, si intervienen. Pregunta antes, en prosa y con las dos opciones en la misma frase: "En el procedimiento de origen del titulo, ¿eran preceptivos abogado y procurador, o se trata de un decreto de monitorio sin oposicion o de un laudo o acuerdo de mediacion por una cantidad que no supera 2.000 euros?" y activa segun la respuesta el parrafo de comparecencia con o sin representacion. Al completar el ultimo dato, vista previa unica y una sola confirmacion antes del `Edit`.
2. **Parte ejecutada** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la parte ejecutada." Sub-apartados: a) nombre o razon social; b) NIF o CIF; c) domicilio. Confirmacion agrupada.
3. **El titulo ejecutivo** *(dato objetivo con validacion)*. Anuncio fijo: "Describimos ahora el titulo en que se funda la ejecucion." Sub-apartados, uno por turno: a) tipo de resolucion (sentencia, decreto o auto) y organo que la dicto; b) numero de autos del procedimiento de origen; c) contenido de la condena tal como figura en el fallo; d) fecha de firmeza. Si el titulo es el decreto de un monitorio sin oposicion, sustituye el hecho por la variante del asset (terminacion del monitorio, Art. 816 LEC) y pide la fecha del decreto en lugar de la de firmeza.
4. **Plazos** *(dato objetivo con validacion bloqueante)*. Anuncio fijo: "Verificamos ahora los plazos de la ejecucion." Con la fecha de firmeza ya conocida, calcula tu mismo si han transcurrido los veinte dias del Art. 548 y si no han pasado los cinco anos del Art. 518. Si el primero no se ha cumplido, informa de la fecha en que se cumplira y pregunta si desea continuar preparando el escrito para presentarlo entonces. Si el segundo esta agotado, aplica el guardrail correspondiente y detente.
5. **Cantidad reclamada** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a determinar la cantidad por la que se despachara la ejecucion." Explica antes de pedir cifras: se reclama el principal, los intereses ya vencidos y una cantidad presupuestada para intereses de la ejecucion y costas que no puede superar el 30 % de lo anterior (Art. 575 LEC), salvo justificacion excepcional; si el bien a ejecutar es la vivienda habitual del ejecutado, las costas exigibles no pueden superar el 5 %. En HOJA FAMILIA, sustituye la pregunta de principal por la relacion mensualidad a mensualidad (mes e importe) siguiendo `references/especialidades-familia-776.md`, apartado 3, y pregunta si el titulo prevee actualizacion periodica antes de aplicarla. Pide despues, en turnos separados: a) principal (o relacion de mensualidades); b) intereses vencidos y su fundamento de calculo; c) porcentaje presupuestado para intereses y costas (por defecto, ofrece el 30 %, o el 5 % si es vivienda habitual, y pregunta si desea un porcentaje menor). Confirmacion propia de cada uno.
6. **Gastos extraordinarios de familia** *(clausula de negociacion — solo HOJA FAMILIA, condicional)*. Anuncio fijo: "Concretamos si existen gastos extraordinarios que reclamar." Explica antes de preguntar: solo pueden incluirse en esta demanda los gastos extraordinarios que el titulo ya prevea con su reparto; los demas exigen una declaracion judicial previa (Art. 776.4ª LEC) y no pueden mezclarse en este escrito. Pregunta si hay gastos extraordinarios y, para cada uno, si figura en el titulo con su reparto. Los que no lo esten, apartalos, adviertelo expresamente y no los incluyas en el desglose.
7. **Bienes del ejecutado** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos ahora los bienes sobre los que actuara la ejecucion." El valor de V4 ya esta resuelto. Si se conocen bienes: explica el orden del Art. 592 LEC (mayor facilidad de enajenacion y menor onerosidad primero; la escala de nueve rangos solo si eso no es posible, y recuerda que los inmuebles ocupan el puesto 7 y los sueldos el 8) y pide la relacion de bienes con datos identificativos suficientes para trabarlos sin nueva investigacion. Si no se conocen: explica que se pedira el requerimiento de manifestacion de bienes del Art. 589 y, si el cliente puede indicar destinatarios concretos de oficios de investigacion (Art. 590), pide cada destinatario y la razon por la que se cree que dispone de informacion; si no tiene ninguno, deja el OTROSI con la peticion generica de manifestacion de bienes y advierte de que la investigacion patrimonial exige destinatarios concretos que podra completar mas adelante con el escrito de la HOJA AVERIGUACION.
8. **Ampliacion automatica** *(clausula de negociacion — explicar antes de decidir; solo si quedan plazos pendientes de vencer)*. Anuncio fijo: "Valoramos si interesa que la ejecucion se amplie automaticamente con los proximos vencimientos." Aplica solo si la obligacion es de tracto sucesivo (pensiones, rentas, plazos pendientes). Explica el Art. 578 LEC: evita presentar un escrito nuevo cada vez que venza una mensualidad y no se pague. Pregunta si desea solicitarla; si la deuda esta integramente vencida, omite la seccion sin preguntar.
9. **Multas coercitivas** *(clausula de negociacion — solo HOJA FAMILIA, condicional)*. Anuncio fijo: "Valoramos si procede pedir multas coercitivas por el incumplimiento reiterado." Explica que son acumulativas al cobro de lo debido, no sustitutivas (Art. 776.1ª LEC), y que requieren incumplimiento reiterado, no un unico impago. Pregunta si el incumplimiento ha sido reiterado y, si es asi, incluye el OTROSI.
10. **Inaplicacion del limite de embargo de sueldos** *(clausula de negociacion — solo HOJA FAMILIA y solo si se reclaman alimentos o compensatoria)*. Anuncio fijo: "Determinamos el regimen de embargo de sueldos aplicable." Si es alimentos: explica que el Art. 607 no se aplica por ministerio de la ley (Art. 608) y que sera el tribunal quien fije la cantidad embargable; no requiere mas dato. Si es compensatoria: explica que la exclusion es rogada y exige acreditar una necesidad economica; pregunta si puede acreditarla y con que medios, y si no puede, informa de que se aplicara la escala ordinaria del Art. 607.
11. **Clausulas abusivas** *(informativo, solo si el titulo no judicial deriva de un contrato con consumidor — se resuelve realmente en la HOJA NO-JUDICIAL, pero si el titulo de familia incorporase un pacto de esa naturaleza, adviertelo igual)*.
12. **Postulacion y documentos** *(dato objetivo)*. Anuncio fijo: "Cerramos con los documentos que se acompanaran." Pregunta que documentos se aportaran ademas del titulo (poder, testimonios, certificaciones) y numeralos correlativamente con los hechos.
13. **Juzgado, lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Determinamos el juzgado competente y cerramos con el lugar y la fecha." El competente es el que conocio del asunto en primera instancia o el que homologo la transaccion o acuerdo (Art. 545.1 LEC): confirma con el usuario cual fue y no admitas sumision a otro fuero. Lugar de firma; fecha del dia salvo indicacion en contrario.

### Secciones — HOJA NO-JUDICIAL

1. **Parte ejecutante** *(dato objetivo — confirmacion agrupada por parte)*. Igual que en la HOJA JUDICIAL, pero la pregunta de postulacion se formula solo si V3 = laudo o acuerdo de mediacion: "¿La cantidad por la que va a despachar la ejecucion supera los 2.000 euros?" (si supera, preceptivos; si no, no preceptivos). Si V3 = escritura publica notarial, abogado y procurador son siempre preceptivos: no preguntar.
2. **Parte ejecutada** *(dato objetivo — confirmacion agrupada por parte)*. Igual que en la HOJA JUDICIAL.
3. **El titulo no judicial** *(dato objetivo con validacion, segun V3)*. Anuncio fijo: "Describimos ahora el titulo en que se funda la ejecucion." Segun V3: escritura publica (notario, plaza, fecha, numero de protocolo), laudo arbitral (fecha, arbitro o institucion, referencia del procedimiento, y confirmar que se aportaran el convenio arbitral y la acreditacion de notificacion), o acuerdo de mediacion u otro MASC elevado a publico (tipo de MASC, fecha del acuerdo, notario, fecha y numero de protocolo de la escritura, y confirmar que se aportaran las actas de la sesion constitutiva y final).
4. **Obligacion y vencimiento** *(dato objetivo)*. Anuncio fijo: "Pasamos a la obligacion documentada y a su vencimiento." Sub-apartados: a) descripcion de la obligacion; b) fecha de vencimiento. Verifica que la cantidad supera los 300 euros (Art. 520 LEC); si no, aplica la validacion de presupuestos ya descrita.
5. **Liquidacion por saldo** *(clausula de negociacion — solo si el titulo pacto liquidacion unilateral, Art. 572.2 LEC)*. Anuncio fijo: "Abordamos la liquidacion del saldo prevista en el titulo." Explica los requisitos acumulativos: notificacion previa al ejecutado y al fiador, y los tres documentos del Art. 573.1. Pregunta la clausula que lo pacta, el saldo resultante y si se acredita la notificacion. Si el interes es variable, pide ademas las operaciones de calculo del Art. 574.
6. **Cantidad reclamada** *(clausula de negociacion — explicar antes de decidir)*. Igual estructura que en la HOJA JUDICIAL (principal, intereses, porcentaje presupuestado con el limite del 30 %).
7. **Bienes del ejecutado** *(clausula de negociacion — explicar antes de decidir)*. Igual que en la HOJA JUDICIAL.
8. **Clausulas abusivas** *(clausula de negociacion — solo si el titulo deriva de un contrato con un consumidor)*. Anuncio fijo: "Verificamos si el titulo esta sujeto al control de clausulas abusivas." Explica que el juzgado examinara de oficio si las clausulas que fundan la ejecucion y determinan la cantidad exigible son abusivas (Arts. 551.2.5º y 552 LEC). Pregunta si el ejecutado es consumidor y, si lo es, si alguna clausula relevante (intereses moratorios, vencimiento anticipado, comisiones) podria ser desproporcionada; si hay duda razonable, advierte y ofrece revision por especialista antes de continuar.
9. **Reserva de partidas dudosas** *(clausula de negociacion — solo si hay liquidacion por saldo y el acreedor duda de alguna partida)*. Anuncio fijo: "Valoramos si conviene reservar alguna partida dudosa." Explica el Art. 573.3: cabe pedir el despacho por la cantidad indubitada y reservar el resto para el declarativo. Pregunta si desea acogerse a esta reserva.
10. **Ampliacion automatica** *(clausula de negociacion — solo si quedan plazos pendientes de vencer)*. Igual que en la HOJA JUDICIAL.
11. **Juzgado, lugar y fecha** *(dato objetivo con explicacion)*. Anuncio fijo: "Determinamos el juzgado competente y cerramos con el lugar y la fecha." Explica la regla del Art. 545.2 y 545.3 LEC segun V3 (laudo o mediacion: lugar donde se dicto o se firmo; demas titulos: a eleccion del ejecutante, el de los Arts. 50-51, el del lugar de cumplimiento o el de donde haya bienes embargables, sin sumision posible) y pide la eleccion. Lugar de firma; fecha del dia salvo indicacion en contrario.

### Secciones — HOJA AVERIGUACION

1. **Datos de la ejecucion en curso** *(dato objetivo)*. Anuncio fijo: "Comenzamos por identificar la ejecucion ya despachada." Sub-apartados, uno por turno: a) juzgado y numero de autos de la ejecucion; b) fecha del auto de despacho; c) cantidad total por la que se despacho, desglosada en principal, intereses vencidos y cantidad presupuestada; d) estado del cobro (nada cobrado, o cantidad ya obtenida y pendiente restante).
2. **Parte ejecutante** *(dato objetivo — confirmacion agrupada por parte)*. Igual estructura que en las otras hojas, con la pregunta de postulacion si procede.
3. **Bienes designados** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos los bienes que se designan para el embargo." Igual explicacion del orden del Art. 592 LEC. Si no hay bienes que designar, pide una breve descripcion de las gestiones ya realizadas para localizarlos.
4. **Insuficiencia y peticion de investigacion** *(dato objetivo con validacion)*. Anuncio fijo: "Justificamos ahora por que es necesaria la investigacion patrimonial." Recuerda que el requerimiento del Art. 589 solo se acuerda si el ejecutante no ha senalado bienes suficientes: si los designados en la seccion anterior ya cubren la cantidad, adviertelo y desactiva esta seccion.
5. **Destinatarios de los oficios** *(dato objetivo con validacion de sentido)*. Anuncio fijo: "Relacionamos los destinatarios de los oficios de investigacion y la razon de cada uno." Por cada destinatario, uno por turno: nombre de la entidad u organismo y razon concreta por la que se cree que dispone de informacion (usa `references/embargo-averiguacion-inembargabilidad.md`, apartado 3, para orientar al cliente si no sabe que destinatarios proponer). Rechaza una razon generica del tipo "por si acaso": pide que la concrete antes de escribirla, porque el Art. 590 exige expresarla sucintamente.
6. **Limites de inembargabilidad** *(informativo, con excepcion condicional)*. Anuncio fijo: "Le informo de los limites de inembargabilidad aplicables." Si la ejecucion es de alimentos o de compensatoria con necesidad acreditada, aplica la excepcion del Art. 608 y explica que es el tribunal quien fija la cantidad embargable; en los demas casos, recuerda la escala del Art. 607 sobre el SMI vigente verificado en el Punto 2. No requiere mas dato salvo, en compensatoria, la acreditacion de la necesidad economica.
7. **Multas coercitivas por incumplimiento del Art. 589** *(clausula de negociacion — condicional, solo si el ejecutado ya fue requerido y no respondio)*. Anuncio fijo: "Valoramos si procede pedir multas coercitivas por no haber manifestado bienes." Pregunta la fecha del requerimiento anterior y el detalle del incumplimiento.
8. **Ampliacion de la ejecucion por nuevos vencimientos** *(clausula de negociacion — condicional)*. Anuncio fijo: "Valoramos si han vencido nuevos plazos que ampliar." Si la obligacion es de tracto sucesivo y han vencido nuevos plazos desde el despacho, pregunta su importe y detalle.
9. **Juzgado, lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito."

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: escrito breve (una ejecucion no reargumenta el pleito), HECHOS o ALEGACIONES numerados con una idea por apartado, documentos relacionados y numerados, desglose siempre por conceptos, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

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

1. Verificar siempre la LEC, la LO 1/2025 y el TRLC en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder.
2. Si se detecta una version posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar. No usar una version desactualizada, y nunca calcular un tramo de embargo de sueldo con un SMI de un ejercicio anterior sin verificarlo.
3. La accion ejecutiva de titulos judiciales, laudos y acuerdos de mediacion caduca a los cinco anos desde la firmeza (Art. 518 LEC). Si el plazo esta agotado, no redactar la demanda: advertir y ofrecer escalacion. Este plazo NO se aplica a la escritura publica notarial.
4. No se despachara ejecucion de titulos judiciales, laudos o acuerdos de mediacion dentro de los veinte dias posteriores a la firmeza o notificacion (Art. 548 LEC). Advertir siempre de esta espera; no aplica a los demas titulos no judiciales.
5. Solo cabe despachar ejecucion frente a quien figure como deudor en el titulo o se encuentre en los supuestos tasados de los Arts. 538 a 544 LEC. Nunca dirigir la ejecucion contra un tercero no amparado por el titulo: genera responsabilidad por danos y perjuicios (Art. 538.4).
6. En titulo no judicial, la cantidad debe exceder de 300 euros y ser liquida (Art. 520 LEC). Sin ese minimo, no procede esta via.
7. La cantidad presupuestada para intereses de la ejecucion y costas no puede superar el 30 % de lo reclamado (5 % si es vivienda habitual del ejecutado, Art. 575.1 bis LEC), salvo justificacion excepcional. Nunca redactar un desglose sin esta cantidad ni por encima de estos limites sin justificarlo.
8. En familia, los gastos extraordinarios no previstos expresamente en el titulo con su reparto NO pueden incluirse en la demanda ejecutiva sin la previa declaracion judicial del Art. 776.4ª LEC. Separarlos siempre y no mezclarlos con el resto de la deuda.
9. En alimentos, el limite del Art. 607 no se aplica por ministerio de la ley (Art. 608). En pension compensatoria, esa exclusion es rogada y exige acreditar necesidad economica: nunca aplicarla sin que el cliente la acredite.
10. Si consta o se sospecha que el ejecutado esta en concurso de acreedores, detener de inmediato: no pueden iniciarse ejecuciones singulares contra la masa activa (Arts. 142 y 143 TRLC).
11. No es exigible acreditar el intento de un medio adecuado de solucion de controversias para presentar una demanda ejecutiva (Art. 5.3 LO 1/2025). Nunca pedir ese dato en esta skill.
12. Nunca inventar datos, cuantias, fechas, numeros de protocolo ni jurisprudencia. Los campos no proporcionados quedan como `{{dato}}`.
13. Cuando el impago de pensiones de familia alcance dos meses consecutivos o cuatro no consecutivos, informar de que la conducta puede tener relevancia penal (Art. 227 del Codigo Penal) y ofrecer escalacion a un especialista en penal. Nunca redactar denuncia ni querella: excede el alcance de esta skill.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar para la ejecucion hipotecaria ni para el lanzamiento derivado de ella (Art. 681 LEC y siguientes): proceso especial, fuera de alcance.
- No usar para la ejecucion provisional de resoluciones no firmes (Art. 524 LEC).
- No usar para redactar la oposicion del ejecutado (Arts. 556 y 557 LEC): posicion contraria, fuera de alcance.
- No usar para el extenso de vivienda y ejecuciones de desahucio: derivar a `desahucio`.
- No usar para reclamar una deuda que aun no tiene titulo ejecutivo: derivar a `reclamacion-cantidad` (monitorio, verbal u ordinario segun cuantia).
- No usar para modificar el regimen de custodia o visitas por incumplimiento reiterado (Art. 776, especialidad 3ª): derivar a `modificacion-medidas` si existe en el marketplace, o escalar.
- No usar si el usuario pide opinion juridica sobre la estrategia de la ejecucion: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
