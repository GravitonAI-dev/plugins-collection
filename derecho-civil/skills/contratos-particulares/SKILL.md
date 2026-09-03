---
name: contratos-particulares
description: >
  Genera el contrato adecuado para una operacion patrimonial entre particulares, conforme al Codigo Civil
  verificado en el BOE: contrato de prestamo de dinero entre particulares (simple prestamo o mutuo, Arts.
  1740 y 1753 a 1757 CC, con control de usura conforme a la Ley de 23 de julio de 1908), reconocimiento de
  deuda y compromiso de pago (Arts. 1255, 1274 a 1277 y 1973 CC), contrato de comodato o prestamo de uso
  gratuito de una cosa (Arts. 1740 a 1752 CC) y contrato de compraventa de un bien mueble (Arts. 1445 y
  siguientes CC). Explica y documenta la decision entre documento privado y escritura publica (Arts. 1278 a
  1280 CC y Art. 517.2.4.º LEC). NO usar para prestamos con entidad financiera ni credito al consumo, para
  prestamos hipotecarios, para la compraventa de inmuebles, para reclamar una deuda ya impagada, ni para
  contratos mercantiles o entre empresas.
when_to_use: |
  - El usuario quiere prestar dinero a un familiar, amigo o conocido y necesita dejarlo por escrito.
  - El usuario quiere documentar una deuda ya existente y fijar un calendario de pago.
  - El usuario quiere ceder gratuitamente el uso de una cosa (local, vehiculo, maquinaria) sin cobrar nada
    por ella y con obligacion de devolverla.
  - El usuario quiere vender o comprar un bien mueble concreto (vehiculo, maquinaria, mobiliario, obra de
    arte) a otro particular.
  - El usuario pregunta si le conviene firmar un contrato privado o ir al notario, y necesita el documento.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - tipo_contrato: prestamo de dinero / reconocimiento de deuda / comodato / compraventa de bien mueble
  - datos_parte_acreedora: nombre o razon social, documento de identidad, domicilio, telefono, email
  - datos_parte_deudora: nombre o razon social, documento de identidad, domicilio, telefono, email
  - objeto: importe del prestamo o de la deuda, descripcion e identificacion del bien, o precio de venta
  - causa: origen de la deuda en el reconocimiento, finalidad del prestamo, relacion entre las partes en el comodato
  - interes: si se pacta interes remuneratorio y a que tipo; si se pacta interes de demora distinto del legal
  - plazo: pago o devolucion en un solo vencimiento, o calendario de cuotas con fechas e importes
  - garantia: fianza simple, fianza solidaria, prenda, reserva de dominio, o ninguna
  - datos_fiador: nombre, documento de identidad, domicilio, telefono, email
  - forma: documento privado, documento privado con compromiso de elevacion, o escritura publica
outputs:
  - contrato_prestamo_particulares: contrato de prestamo entre particulares en markdown, DRAFT
  - reconocimiento_deuda: reconocimiento de deuda y compromiso de pago en markdown, DRAFT
  - contrato_comodato: contrato de comodato o prestamo de uso en markdown, DRAFT
  - contrato_compraventa_mueble: contrato de compraventa de bien mueble en markdown, DRAFT
references:
  - references/estilo-redaccion-contratos.md
  - references/forma-documento-privado-o-publico.md
  - references/fuentes-plantillas-validadas.md
  - references/usura-y-limites-del-interes.md
assets:
  - assets/template-contrato-comodato.md
  - assets/template-contrato-compraventa-mueble.md
  - assets/template-contrato-prestamo-particulares.md
  - assets/template-reconocimiento-deuda.md
---

# Contratos Patrimoniales entre Particulares

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
    "naturaleza_operacion": {
      "type": "string",
      "description": "Naturaleza de la operaci\u00f3n patrimonial (V1)",
      "enum": [
        "prestamo_dinero",
        "reconocimiento_deuda",
        "comodato",
        "compraventa_mueble"
      ]
    },
    "pacto_interes": {
      "type": "string",
      "description": "Pacto de intereses remuneratorios (V2)",
      "enum": [
        "gratuito",
        "con_interes"
      ]
    },
    "garantia": {
      "type": "string",
      "description": "Garant\u00edas del cumplimiento (V3)",
      "enum": [
        "sin_garantia",
        "afianzamiento"
      ]
    },
    "forma_documento": {
      "type": "string",
      "description": "Forma y formalizaci\u00f3n del documento (V4)",
      "enum": [
        "privado",
        "publico"
      ]
    }
  },
  "required": [
    "naturaleza_operacion",
    "pacto_interes"
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = 1 y V1b = 1 → **HOJA PRESTAMO**: `assets/template-contrato-prestamo-particulares.md`.
- Si V1 = 1 y V1b = 2 → **HOJA COMODATO**: `assets/template-contrato-comodato.md`.
- Si V1 = 2 → **HOJA RECONOCIMIENTO**: `assets/template-reconocimiento-deuda.md`.
- Si V1 = 3 → **HOJA COMPRAVENTA**: `assets/template-contrato-compraventa-mueble.md`.
- Si V1 = 1, V1b = 2 y **el cesionario debe pagar algo** por el uso de la cosa (renta, canon, cuota de gastos que exceda de los ordinarios, cualquier emolumento) → **NO es comodato**: el Art. 1741 CC dice que, si interviene emolumento, la convencion deja de ser comodato. Si la cosa es un inmueble urbano, derivar a `arrendamiento`. Si es otra cosa, advertir de que se trata de un arrendamiento y ofrecer escalacion. No crear documento de comodato.
- Si lo que el usuario pretende es **cobrar una deuda que ya esta impagada** (no documentarla ni pactar su pago futuro) → derivar a `reclamacion-cantidad`. No crear documento.
- Si ya existe un **titulo ejecutivo** (sentencia, escritura publica, laudo) y lo que se quiere es ejecutarlo → derivar a `ejecucion-titulos`. No crear documento.
- Si el bien objeto de la operacion es un **inmueble** y la operacion es una compraventa → derivar a `compraventa-inmueble`. No crear documento.
- Si el prestamo se garantiza con **hipoteca sobre un inmueble** → **DETENER**: puede entrar en el ambito de la Ley 5/2019 reguladora de los contratos de credito inmobiliario, con requisitos de transparencia y acta notarial previa que exceden el alcance de esta skill. Advertir y escalar.
- Si **una de las partes es un consumidor y la otra actua como empresario o profesional** → **DETENER**: no es un contrato entre particulares. Se aplica la normativa de proteccion de consumidores (y, si es credito, la de credito al consumo), con controles de transparencia y abusividad propios. Advertir y escalar o derivar a `reclamacion-clausulas-abusivas` si lo que se pretende es impugnar una clausula ya firmada. No crear documento con estos assets.

### Validacion de presupuestos (interno, antes del Punto 3)

- **TODAS LAS HOJAS (Art. 1261 CC):** confirmar que concurren consentimiento, objeto cierto y causa. Si el objeto no esta determinado ni es determinable sin nuevo acuerdo entre las partes (Art. 1273 CC), no redactar: pedir que se concrete.
- **TODAS LAS HOJAS (Art. 1255 CC):** ningun pacto puede ser contrario a las leyes, a la moral ni al orden publico. Si el usuario pide un pacto que lo sea, rechazar la instruccion, explicar por que es nulo y proponer una alternativa valida.
- **TODAS LAS HOJAS — condicion de particulares:** verificar que ninguna de las partes actua como empresario o profesional en el marco de esa actividad. Si lo hace, aplicar la regla de enrutamiento correspondiente y detener.
- **HOJA PRESTAMO (control de usura, BLOQUEANTE):** si V2 = se pacta interes, calcular el **coste real total** de la operacion tal como el usuario la plantea: no solo el tipo nominal, sino todo lo que el prestatario devolvera por encima del principal, incluidas comisiones, gastos y penalizaciones. Contrastarlo con el orden de magnitud del interes legal del dinero vigente verificado en el Punto 2 y con el coste normal de operaciones equivalentes. Si la desproporcion es manifiesta, **advertir expresamente ANTES de continuar**, con el texto del guardrail 3, explicando que la consecuencia es la **nulidad del prestamo** y no una rebaja del interes. No redactar la clausula de interes hasta que el usuario confirme que, conocida la advertencia, mantiene o modifica su decision. Si el usuario mantiene un interes que sigue siendo manifiestamente desproporcionado, ofrecer escalacion y dejar constancia de la advertencia en las advertencias finales del documento.
- **HOJA PRESTAMO (Art. 1 parrafo 2.º de la Ley Azcarate, BLOQUEANTE):** si el importe que figuraria como prestado es superior al efectivamente entregado (por descuento del interes en el momento de la entrega o por cualquier otra via), **DETENER**: ese contrato es nulo por el propio precepto. Explicarlo, no redactarlo y ofrecer escalacion.
- **HOJA PRESTAMO (Art. 1755 CC):** si V2 = no se pacta interes, recordar al usuario que sin pacto expreso no se deberan intereses, y que esa es la regla legal por defecto, no un olvido del documento.
- **HOJA RECONOCIMIENTO (Arts. 1275 y 1276 CC y Art. 9 de la Ley Azcarate, BLOQUEANTE):** si la causa real de la deuda reconocida es un prestamo con interes desproporcionado, un importe superior al realmente debido, o cualquier causa ilicita, **DETENER**: el reconocimiento no puede usarse como envoltorio. Explicar que la Ley Azcarate se aplica a toda operacion sustancialmente equivalente a un prestamo cualquiera que sea la forma del contrato, y que un contrato con causa ilicita no produce efecto alguno. No redactar y ofrecer escalacion.
- **HOJA COMODATO (Arts. 1740 y 1741 CC):** confirmar que no hay contraprestacion alguna a cargo del comodatario. La asuncion de los gastos ordinarios de uso y conservacion (Art. 1743 CC) no es contraprestacion; el pago de una renta, canon o cuota por el uso, si. Si la hay, aplicar la regla de enrutamiento y detener.
- **HOJA COMPRAVENTA (Art. 1445 CC):** confirmar que hay cosa determinada y precio cierto en dinero o signo que lo represente. Si la contraprestacion no es dineraria, es una permuta y no una compraventa: advertir y escalar.
- **HOJA COMPRAVENTA:** si el bien es un vehiculo, comprobar que se dispone de matricula y numero de bastidor. Si el bien es un inmueble, aplicar la regla de enrutamiento y detener.
- **PRESCRIPCION (informativo, HOJA RECONOCIMIENTO):** las acciones personales sin plazo especial prescriben a los cinco años (Art. 1964.2 CC). Si la deuda que se reconoce es antigua, informar de que el reconocimiento **interrumpe** la prescripcion (Art. 1973 CC) y reinicia el computo, lo que beneficia al acreedor y perjudica al deudor. Si quien pide el documento es el deudor, advertirselo expresamente antes de continuar.
- **DERECHO FORAL:** si la vecindad civil de alguna de las partes o el lugar de celebracion apunta a un territorio con derecho civil propio (Cataluña, Navarra, Aragon, Baleares, Galicia, Pais Vasco), advertir de que puede desplazar reglas del Codigo Civil comun y ofrecer escalacion.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Código Civil (Arts. 1.740-1.757 para préstamo y comodato; Arts. 1.445-1.537 para compraventa mueble; Arts. 1.156 y 1.255 para reconocimiento de deuda), Ley de 23 de julio de 1908 (represión de la usura) y Real Decreto Legislativo 1/1993 (ITPAJD, operaciones exentas con obligación de declaración).
2. **Orientación Legal del Caso:**
Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa el tipo de contrato y la fuente aplicable.** Textos fijos por hoja:
   - PRESTAMO: "A su caso corresponde un contrato de prestamo entre particulares, de los denominados simple prestamo o mutuo, regulado en los articulos 1.740 y 1.753 a 1.757 del Codigo Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - RECONOCIMIENTO: "A su caso corresponde un reconocimiento de deuda con compromiso de pago, que se ampara en la libertad de pacto del articulo 1.255 del Codigo Civil y se rige por sus normas generales sobre obligaciones y contratos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - COMODATO: "A su caso corresponde un contrato de comodato o prestamo de uso, regulado en los articulos 1.740 a 1.752 del Codigo Civil. Se trata de un contrato esencialmente gratuito. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - COMPRAVENTA: "A su caso corresponde un contrato de compraventa de bien mueble entre particulares, regulado en los articulos 1.445 y siguientes del Codigo Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - **Añadir en la HOJA PRESTAMO si V2 = se pacta interes:** "Le informo ademas de que el interes pactado esta sujeto al control de la Ley de 23 de julio de 1908 sobre nulidad de los contratos de prestamos usurarios, que sigue vigente. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1908-5579"
   - **Añadir en la HOJA PRESTAMO si V2 = no se pacta interes:** "Conforme al articulo 1.755 del Codigo Civil, no se deberan intereses sino cuando expresamente se hubiesen pactado, de modo que su prestamo sera gratuito."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla del sistema, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio (adviertele si el documento adjuntado los incumple, en particular si contiene un interes potencialmente usurario o una clausula nula).
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-contrato-comodato.md`).
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

**Marcas de tipo de seccion.** Cada seccion lleva una de estas dos marcas, que determina como se trata:

- `[dato objetivo]`: se pregunta y se registra. Si son datos identificativos de una misma parte, confirmacion agrupada. Validacion de sentido, no solo de formato: si la respuesta es absurda, imposible o no responde a lo preguntado, no la escribas — dialoga con el cliente, señala por que no encaja y pide aclaracion.
- `[negociacion]`: **explica primero el regimen legal por defecto y las consecuencias de cada opcion, y solo despues pide la decision.** Nunca registres el valor sin haber explicado. Confirma que el cliente entiende antes de escribirlo.

### Secciones — HOJA PRESTAMO

1. **Parte prestamista** *(`[dato objetivo]` — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de quien entrega el dinero." Sub-apartados, uno por turno: a) nombre completo o razon social; b) DNI, NIE o CIF; c) domicilio a efectos de notificaciones; d) telefono y correo electronico. Si es persona juridica, pide ademas representante y cargo. Al recibir la respuesta al ultimo dato, en el turno siguiente muestra una unica vista previa con todos ellos y pide una sola confirmacion antes del `Edit`.
2. **Parte prestataria** *(`[dato objetivo]` — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de quien recibe el prestamo." Mismos sub-apartados y misma confirmacion agrupada.
3. **Importe y entrega del capital** *(`[dato objetivo]` con validacion)*. Anuncio fijo: "Determinamos ahora el importe del prestamo y la forma en que se entrega el dinero." Sub-apartados, uno por turno: a) importe (lo escribes en cifra y en letra); b) finalidad del prestamo, para el expositivo; c) si el dinero ya se entrego o se entrega con la firma, y en que fecha; d) medio de entrega y, si es transferencia, IBAN de destino. Al preguntar (d), recomienda la transferencia bancaria frente al efectivo y explica por que: lo que mas se discute despues no es el pacto, sino si el dinero llego a entregarse, y la transferencia lo acredita.
4. **Intereses remuneratorios** *(`[negociacion]` — control de usura BLOQUEANTE)*. Anuncio fijo: "Abordamos ahora los intereses del prestamo." **Explica antes de preguntar nada:** (i) conforme al articulo 1.755 del Codigo Civil, sin pacto expreso no se deben intereses, de modo que el prestamo es gratuito por defecto; (ii) si decide pactarlos, la Ley de 23 de julio de 1908 sobre nulidad de los contratos de prestamos usurarios sigue vigente y declara nulo el prestamo cuyo interes sea notablemente superior al normal del dinero y manifiestamente desproporcionado; (iii) **la consecuencia de la usura no es que un juez rebaje el interes: el contrato se anula, el prestatario devuelve solo el capital que recibio, el prestamista debe reintegrar lo que hubiera cobrado por encima de ese capital y carga con las costas** (articulos 1, 3 y 8 de esa ley); (iv) no existe un porcentaje legal seguro: lo aprecia el tribunal caso por caso. Solo despues pide el tipo. Recibido, ejecuta la validacion de usura del Punto 1 sobre el coste real total, no sobre el tipo nominal. Si es manifiestamente desproporcionado, aplica el guardrail 3 antes de escribir nada. **Si el tipo queda en la franja intermedia** — claramente por encima del interes legal del dinero verificado en el Punto 2, pero sin desproporcion manifiesta, que es donde cae la mayoria de los prestamos entre particulares —, **no guardes silencio: el silencio se lee como una validacion**. Dile expresamente que el tipo esta por encima del interes normal del dinero, que **eso no lo hace por si solo usurario** porque la ley no fija ningun umbral y la desproporcion se aprecia caso por caso atendiendo a las circunstancias de la operacion (articulo 2 de la Ley de 23 de julio de 1908), y que por esa misma razon tampoco puedes garantizarle que un tribunal lo respalde. Prohibido responder "ese tipo es correcto", "no hay problema" o cualquier formula equivalente de validacion, y prohibido igualmente presentarlo como usurario sin base. Comunicale ademas el coste total de la operacion que resulta de su tipo (capital, intereses totales y total a devolver), que es el dato que le permite juzgarla. Si no se pacta interes, inserta la Variante A y hazlo constar expresamente en el documento, no por omision.
5. **Plazo y forma de devolucion** *(`[negociacion]`)*. Anuncio fijo: "Pasamos a determinar el plazo y la forma en que se devolvera el dinero." Explica antes de preguntar la diferencia practica entre un vencimiento unico y un calendario de cuotas: el vencimiento unico es mas simple pero concentra todo el riesgo en una fecha; las cuotas permiten detectar el incumplimiento antes y activar el vencimiento anticipado. Pide despues, en turnos separados: a) pago unico o cuotas; b) si es pago unico, la fecha; si son cuotas, numero, periodicidad, importe y fecha de la primera; c) medio de pago e IBAN del prestamista. Con las cuotas, construye tu la tabla completa del calendario y muestrala en la vista previa.
6. **Mora e intereses de demora** *(`[negociacion]`)*. Anuncio fijo: "Concretamos ahora que sucede si el prestatario no devuelve el dinero en la fecha pactada." Explica antes de preguntar: (i) por regla general la mora exige un requerimiento previo del acreedor (articulo 1.100 del Codigo Civil), pero puede pactarse que se produzca automaticamente al vencimiento, y eso es lo que hace el contrato; (ii) a falta de pacto, la cantidad impagada devenga el interes legal del dinero (articulo 1.108); (iii) puede pactarse un interes de demora superior, pero un interes de demora desproporcionado se valora dentro del juicio global de usura y esta expuesto a la moderacion judicial del articulo 1.154. Pregunta despues si desea el interes legal o un tipo pactado, y en este segundo caso cual.
7. **Amortizacion anticipada** *(`[negociacion]` — condicional)*. Anuncio fijo: "Valoramos si el prestatario podra devolver el dinero antes de tiempo." Explica que, salvo pacto, no hay obligacion del prestamista de aceptar la devolucion anticipada, y que pactarla sin comision es lo habitual entre particulares. Pregunta si desea incluirla y con que preaviso. Si dice que no, descarta el bloque y renumera.
8. **Vencimiento anticipado** *(`[negociacion]` — condicional, solo si la devolucion es en cuotas)*. Anuncio fijo: "Valoramos si el impago de alguna cuota debe hacer exigible toda la deuda de una vez." Explica que sin esta clausula el prestamista solo puede reclamar las cuotas ya vencidas, teniendo que esperar al resto. Pregunta si desea incluirla, tras cuantas cuotas impagadas y con que plazo de subsanacion. Si la devolucion es en un pago unico, omite la seccion sin preguntar.
9. **Garantias** *(`[negociacion]` — resuelve V3)*. Anuncio fijo: "Determinamos ahora si el prestamo contara con alguna garantia." Explica antes de preguntar: (i) **que aporta un fiador**: una persona mas que responde con todo su patrimonio si el prestatario no paga (articulos 1.822 y 1.911 del Codigo Civil); (ii) **la diferencia entre fianza simple y solidaria**: en la simple, el fiador goza del beneficio de excusion y no puede ser compelido a pagar sin que antes se hayan perseguido todos los bienes del prestatario (articulo 1.830); en la solidaria, el fiador renuncia a ese beneficio y el prestamista puede dirigirse directamente contra el, o contra ambos a la vez, sin reclamar antes al prestatario (articulo 1.831.1.º y 2.º) — la solidaria es sensiblemente mas protectora para el prestamista y sensiblemente mas gravosa para el fiador; (iii) **que aporta una prenda**: una cosa concreta queda afecta al pago, pero exige entregar su posesion al acreedor o a un tercero (articulo 1.863) y solo surte efecto frente a terceros si su fecha consta en documento publico (articulo 1.865). Pregunta despues, en turnos separados: a) si habra garantia y de que tipo; b) si es fianza, sus datos identificativos (sub-apartados con confirmacion agrupada como los de las demas partes) y si es simple o solidaria, informando al fiador del alcance de la renuncia; c) si es prenda, descripcion del bien y quien lo conservara. Inserta los bloques que correspondan y renumera.
10. **Gastos e impuestos** *(`[dato objetivo]` con explicacion)*. Anuncio fijo: "Cerramos el reparto de los gastos de formalizacion y las obligaciones fiscales." Informa de que el prestamo entre particulares esta sujeto y exento del Impuesto sobre Transmisiones Patrimoniales y Actos Juridicos Documentados, pero que la autoliquidacion debe presentarse igualmente ante la Administracion tributaria competente. Pregunta a cargo de quien van los gastos de formalizacion y quien presentara la autoliquidacion.
11. **Forma del contrato** *(`[negociacion]` — resuelve V4)*. Anuncio fijo: "Decidimos ahora la forma en que se documentara el prestamo." Aplica la explicacion completa de la seccion "Explicacion comun de la forma" mas abajo. Pregunta despues la opcion elegida e inserta la variante correspondiente.
12. **Notificaciones y cierre** *(`[dato objetivo]`)*. Anuncio fijo: "Cerramos con las comunicaciones entre las partes y con el lugar y la fecha de firma." Sub-apartados, uno por turno: a) plazo para comunicar un cambio de domicilio; b) lugar de firma; c) fecha, que sera la del dia salvo indicacion en contrario; d) numero de ejemplares. Comprueba en este momento que no queda ningun placeholder de ordinal sin resolver ni ninguna remision interna incorrecta.

### Secciones — HOJA RECONOCIMIENTO

1. **Parte acreedora** *(`[dato objetivo]` — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la parte acreedora." Mismos sub-apartados que en la HOJA PRESTAMO.
2. **Parte deudora** *(`[dato objetivo]` — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la parte deudora."
3. **Importe de la deuda** *(`[dato objetivo]` con validacion)*. Anuncio fijo: "Determinamos ahora el importe exacto de la deuda que se reconoce." Sub-apartados, uno por turno: a) importe total (lo escribes en cifra y en letra); b) fecha a la que se determina ese importe; c) si procede de un solo concepto o de varios y, si son varios, su desglose para la tabla. Valida que la suma del desglose coincide con el total: si no coincide, no lo escribas, señalalo y pide aclaracion.
4. **Causa de la deuda** *(`[negociacion]` — control de causa BLOQUEANTE)*. Anuncio fijo: "Abordamos ahora el origen de la deuda que se reconoce." **Explica antes de preguntar:** (i) este documento **no crea la deuda, la reconoce**: la obligacion nace de su origen real, y el reconocimiento la confirma y fija su importe; (ii) conforme al articulo 1.277 del Codigo Civil, aunque la causa no se exprese se presume que existe y que es licita mientras el deudor no pruebe lo contrario, de modo que un reconocimiento sin causa expresada es valido y traslada al deudor la carga de la prueba; (iii) **aun asi conviene expresarla**: si el deudor logra probar que no habia causa o que era ilicita, un reconocimiento abstracto cae entero (articulos 1.275 y 1.276), mientras que uno con causa veraz y licita expresada resiste y evita que se discuta despues de que venia la deuda. Pregunta despues si desea expresar la causa y, en caso afirmativo, cual es exactamente. **Ejecuta la validacion de causa del Punto 1 sobre la respuesta:** si la causa real es un prestamo con interes desproporcionado, un importe superior al realmente debido o cualquier causa ilicita, detente y aplica el guardrail 5.
5. **Naturaleza declarativa y prescripcion** *(informativo, sin dato)*. Anuncio fijo: "Le informo del efecto que la firma de este documento produce sobre los plazos." Informa de que el reconocimiento interrumpe la prescripcion (articulo 1.973 del Codigo Civil) y de que el plazo de las acciones personales, de cinco años (articulo 1.964.2), vuelve a contarse desde la fecha de la firma. Si quien encarga el documento es el deudor, adviertele expresamente de que esto le perjudica.
6. **Forma y plazo de pago** *(`[negociacion]`)*. Anuncio fijo: "Pasamos a determinar como y cuando se pagara la deuda." Misma estructura y explicacion que la seccion 5 de la HOJA PRESTAMO (pago unico frente a calendario de cuotas, con tabla).
7. **Mora e intereses** *(`[negociacion]`)*. Anuncio fijo: "Concretamos ahora que sucede si la deuda no se paga en las fechas pactadas." Misma explicacion que la seccion 6 de la HOJA PRESTAMO. Pregunta ademas si el aplazamiento concedido devengara un interes remuneratorio: si el usuario lo pacta, el conjunto vuelve a quedar sujeto al control de usura del guardrail 3, porque la Ley Azcarate se aplica a toda operacion sustancialmente equivalente a un prestamo (articulo 9).
8. **Vencimiento anticipado** *(`[negociacion]` — condicional, solo si el pago es en cuotas)*. Anuncio fijo: "Valoramos si el impago de alguna cuota debe hacer exigible toda la deuda de una vez." Igual que la seccion 8 de la HOJA PRESTAMO.
9. **Compensacion de creditos reciprocos** *(`[negociacion]` — condicional)*. Anuncio fijo: "Verificamos si existen deudas en sentido contrario que deban compensarse." Explica los cinco requisitos del articulo 1.196 del Codigo Civil (reciprocidad como obligados principales, homogeneidad, vencimiento, liquidez y exigibilidad, y ausencia de retencion o contienda de tercero). Pregunta si el acreedor adeuda a su vez algo al deudor y, en caso afirmativo, su importe y concepto. Si se compensa, deja claro en el documento que el importe reconocido ya es el neto.
10. **Garantias** *(`[negociacion]` — resuelve V3)*. Anuncio fijo: "Determinamos ahora si el pago contara con alguna garantia." Misma explicacion de fianza simple frente a solidaria que en la seccion 9 de la HOJA PRESTAMO. La prenda no se ofrece por defecto en esta hoja: si el usuario la pide, usa el bloque de la HOJA PRESTAMO y adapta la denominacion de las partes.
11. **Efectos del pago integro** *(`[negociacion]`)*. Anuncio fijo: "Determinamos que efectos tendra el pago completo de la deuda." Explica la diferencia entre la simple carta de pago (extingue la deuda reconocida) y el finiquito de la relacion (cierra ademas cualquier otra reclamacion derivada de esa misma relacion). Pregunta cual desea. Si el usuario es el acreedor, adviertele de que el finiquito le impide reclamar despues otros conceptos de la misma relacion.
12. **Forma del documento** *(`[negociacion]` — resuelve V4)*. Anuncio fijo: "Decidimos ahora la forma en que se documentara el reconocimiento." Aplica la explicacion comun de la forma.
13. **Notificaciones y cierre** *(`[dato objetivo]`)*. Anuncio fijo: "Cerramos con las comunicaciones entre las partes y con el lugar y la fecha de firma." Igual que en la HOJA PRESTAMO.

### Secciones — HOJA COMODATO

1. **Parte comodante** *(`[dato objetivo]` — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de quien cede el uso de la cosa."
2. **Parte comodataria** *(`[dato objetivo]` — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de quien recibe la cosa en uso."
3. **El bien cedido** *(`[dato objetivo]` con validacion)*. Anuncio fijo: "Describimos ahora la cosa cuyo uso se cede." Sub-apartados, uno por turno: a) descripcion y datos de identificacion (si es inmueble, direccion, municipio, codigo postal, referencia catastral y superficie; si es vehiculo, marca, modelo, matricula y bastidor; en otro caso, marca, modelo y numero de serie); b) titulo por el que el comodante puede cederlo; c) estado en el momento de la entrega; d) elementos accesorios, llaves o documentacion que se entregan. Recomienda documentar el estado con fotografias en el anexo y explica por que: es la unica forma de discutir despues si un deterioro deriva del uso normal o de un uso indebido.
4. **Gratuidad** *(`[negociacion]` — validacion BLOQUEANTE)*. Anuncio fijo: "Confirmamos ahora el caracter gratuito de la cesion." **Explica antes de preguntar:** (i) el comodato es **esencialmente gratuito** por definicion legal (articulo 1.740, parrafo segundo, del Codigo Civil); (ii) si el cesionario debe pagar cualquier emolumento por el uso, **la convencion deja de ser comodato** (articulo 1.741) y pasa a regirse como arrendamiento, con un regimen completamente distinto de duracion, renta y proteccion del cesionario; (iii) que el comodatario asuma los gastos ordinarios de uso y conservacion **no es contraprestacion** y no rompe la gratuidad (articulo 1.743). Pregunta despues si el comodatario abonara alguna cantidad por el uso. Si la respuesta es afirmativa y se trata de una contraprestacion real, aplica el enrutamiento del Punto 1 y detente.
5. **Destino y duracion** *(`[negociacion]`)*. Anuncio fijo: "Determinamos ahora para que se usara la cosa y durante cuanto tiempo." **Explica antes de preguntar** las tres situaciones y sus consecuencias: (i) **con plazo pactado**, el comodante no puede reclamar la cosa antes de esa fecha, salvo que tenga urgente necesidad de ella y la justifique (articulo 1.749); (ii) **sin plazo pero con un uso concreto pactado**, el comodante no puede reclamarla hasta que concluya ese uso, con la misma excepcion de urgente necesidad; (iii) **sin plazo ni uso determinado**, el comodante puede reclamarla a su voluntad, en cualquier momento (articulo 1.750), lo que da maxima flexibilidad al comodante y minima seguridad al comodatario. Advierte ademas de que, si el bien es un inmueble, la tercera situacion se aproxima a la del precario y su recuperacion, si el ocupante se niega a devolverlo, exige acudir a la via judicial. Pregunta despues cual de las tres desea, el uso previsto y, segun el caso, las fechas o el preaviso.
6. **Obligaciones y gastos** *(`[negociacion]`)*. Anuncio fijo: "Repartimos ahora los gastos y las obligaciones de conservacion de la cosa." Explica el reparto legal por defecto: los gastos ordinarios de uso y conservacion son del comodatario (articulo 1.743) y los extraordinarios de conservacion son del comodante siempre que se le avisen antes de hacerlos, salvo urgencia (articulo 1.751). Pregunta si desea mantener ese reparto legal o precisarlo, y si prohibe la cesion del uso a terceros.
7. **Tasacion y seguro** *(`[negociacion]` — condicional)*. Anuncio fijo: "Valoramos si conviene tasar la cosa y asegurarla." Explica que, si la cosa se entrega con tasacion, el comodatario responde de su valor aunque se pierda por caso fortuito (articulo 1.745), lo que protege al comodante y agrava al comodatario. Pregunta si desea tasarla y por que valor, y si existe una poliza de seguro y a cargo de quien va la prima. Si no desea ninguna de las dos cosas, descarta los bloques y renumera.
8. **Restitucion** *(`[dato objetivo]`)*. Anuncio fijo: "Concretamos como y donde se devolvera la cosa." Sub-apartados, uno por turno: a) lugar de restitucion; b) si se suscribira documento acreditativo de la devolucion. Recuerda al comodatario, al hilo, que no puede retener la cosa alegando que el comodante le debe algo, ni siquiera por gastos (articulo 1.747).
9. **Forma del contrato** *(`[negociacion]` — resuelve V4)*. Anuncio fijo: "Decidimos ahora la forma en que se documentara la cesion." Aplica la explicacion comun de la forma, **omitiendo la parte relativa a la fuerza ejecutiva**: en el comodato no hay deuda dineraria que ejecutar, de modo que lo relevante es solo la fecha cierta frente a terceros y el coste. No recomiendes escritura publica por defecto en un comodato de escaso valor.
10. **Notificaciones y cierre** *(`[dato objetivo]`)*. Anuncio fijo: "Cerramos con las comunicaciones entre las partes y con el lugar y la fecha de firma."

### Secciones — HOJA COMPRAVENTA

1. **Parte vendedora** *(`[dato objetivo]` — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la parte vendedora."
2. **Parte compradora** *(`[dato objetivo]` — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la parte compradora."
3. **El bien vendido** *(`[dato objetivo]` con validacion)*. Anuncio fijo: "Describimos ahora el bien objeto de la venta." Sub-apartados, uno por turno: a) descripcion; b) datos de identificacion (si es vehiculo, marca, modelo, matricula, bastidor, fecha de primera matriculacion y kilometraje; en otro caso, marca, modelo, numero de serie y año); c) estado; d) accesorios y documentacion incluidos. Rechaza una descripcion generica que no permita identificar el bien de forma inconfundible: pide que la concrete.
4. **Precio** *(`[dato objetivo]`)*. Anuncio fijo: "Determinamos ahora el precio de la venta." Pide el precio y escribelo en cifra y en letra. Si el precio no es dinerario, aplica la validacion de presupuestos: es una permuta, no una compraventa.
5. **Forma de pago** *(`[negociacion]`)*. Anuncio fijo: "Pasamos a determinar como se pagara el precio." Explica antes de preguntar que el precio aplazado **no devenga interes salvo pacto expreso**, salvo que la cosa produzca fruto o renta o el comprador incurra en mora (articulo 1.501 del Codigo Civil). Pregunta despues, en turnos separados: a) si el precio se paga integro al contado o se aplaza; b) si se aplaza, el importe entregado en el acto, el aplazado y el calendario; c) si el aplazado devengara interes y a que tipo; d) medio de pago e IBAN.
6. **Entrega y transmision del riesgo** *(`[negociacion]`)*. Anuncio fijo: "Determinamos cuando se entrega el bien y desde cuando corre su riesgo." Explica que la venta se perfecciona por el acuerdo sobre cosa y precio aunque ninguno se haya entregado (articulo 1.450), pero que la propiedad y el riesgo de perdida se transmiten con la entrega. Pregunta si el bien se entrega en el acto o en fecha posterior y, en su caso, lugar y fecha, y a cargo de quien van los gastos de entrega.
7. **Reserva de dominio** *(`[negociacion]` — condicional, solo si el precio esta aplazado)*. Anuncio fijo: "Valoramos si el vendedor debe conservar la propiedad hasta el pago completo." Explica que la reserva de dominio permite al vendedor recuperar el bien si el comprador no paga, pero que su plena oponibilidad frente a terceros exige la inscripcion en el Registro de Bienes Muebles, que esta skill no tramita. Pregunta si desea incluirla. Si el precio se paga al contado, omite la seccion sin preguntar.
8. **Estado del bien y saneamiento** *(`[negociacion]`)*. Anuncio fijo: "Abordamos ahora la responsabilidad del vendedor por los defectos del bien." **Explica antes de preguntar:** (i) el vendedor responde de los defectos **ocultos** que hagan el bien impropio para su uso o disminuyan tal uso, pero **no de los defectos manifiestos o que estuvieran a la vista** (articulo 1.484); (ii) el plazo para reclamar por vicios ocultos es de **seis meses desde la entrega** (articulo 1.490), un plazo notablemente breve que conviene que el comprador conozca; (iii) puede pactarse la exoneracion del saneamiento, pero **solo produce efecto si el vendedor ignoraba efectivamente los vicios**: si los conocia y no los manifesto, responde pese al pacto (articulo 1.485). Pregunta despues si se pacta exoneracion y si el bien se vende expresamente como usado y a revisar. Si el usuario es el comprador, advierte de que la exoneracion le perjudica; si es el vendedor, advierte de que no le protege si conocia el defecto.
9. **Cargas y declaraciones del vendedor** *(`[dato objetivo]` con validacion)*. Anuncio fijo: "Verificamos ahora la situacion juridica del bien." Sub-apartados, uno por turno: a) si el bien esta libre de cargas, gravamenes, embargos y reservas de dominio, y si no, cuales; b) si esta al corriente de los tributos que le afecten; c) si es vehiculo, fecha de caducidad de la Inspeccion Tecnica de Vehiculos y si consta alguna anotacion en el Registro de Vehiculos. Si el vendedor no puede afirmar que el bien esta libre de cargas, no escribas esa declaracion: recogela con la salvedad que corresponda.
10. **Impuestos y tramites** *(`[dato objetivo]` con explicacion)*. Anuncio fijo: "Cerramos las obligaciones fiscales y los tramites posteriores a la venta." Informa de que el Impuesto sobre Transmisiones Patrimoniales y Actos Juridicos Documentados corresponde al comprador. Pregunta el reparto de los demas gastos y, si es vehiculo, el plazo para el cambio de titularidad ante la Jefatura de Trafico, advirtiendo al vendedor de que mientras el vehiculo figure a su nombre puede seguir recibiendo sanciones y el impuesto de circulacion.
11. **Forma del contrato** *(`[negociacion]` — resuelve V4)*. Anuncio fijo: "Decidimos ahora la forma en que se documentara la compraventa." Aplica la explicacion comun de la forma. Si el bien se entrega y se paga integramente en el acto, informa de que el contrato se agota en la firma y que la escritura publica rara vez se justifica.
12. **Notificaciones y cierre** *(`[dato objetivo]`)*. Anuncio fijo: "Cerramos con las comunicaciones entre las partes y con el lugar y la fecha de firma."

### Explicacion comun de la forma del documento (secciones marcadas "resuelve V4")

Antes de preguntar por la forma, explica siempre, apoyandote en `references/forma-documento-privado-o-publico.md`:

1. **El documento privado es plenamente valido y obligatorio entre las partes** (articulos 1.278 y 1.225 del Codigo Civil). No hace falta notario para que el contrato exista y vincule.
2. **Lo que le falta al documento privado es fecha cierta frente a terceros**: un tercero puede negar que se firmara en la fecha que dice, salvo en los tres supuestos del articulo 1.227 (inscripcion en registro publico, muerte de un firmante, entrega a funcionario publico). Importa cuando hay otros acreedores, una herencia o un divorcio de por medio.
3. **Y le falta fuerza ejecutiva**: si el deudor no paga, hay que ganar antes un pleito declarativo para obtener un titulo con el que embargar. La copia de la escritura publica matriz expedida con caracter ejecutivo **si es titulo ejecutivo** (articulo 517.2.4.º de la Ley 1/2000, de Enjuiciamiento Civil) y permite ir directamente a la ejecucion, sin declarativo previo, siempre que la cantidad exceda de 300 euros (articulo 520). Esta explicacion se **omite en la HOJA COMODATO**, donde no hay deuda dineraria que ejecutar.
4. **La escritura tiene un coste** proporcional a la cuantia, segun el arancel notarial. No cifres ese coste: informa de que existe y remite a la notaria para un presupuesto.
5. **Se puede firmar ahora en privado y elevar despues**: el articulo 1.279 del Codigo Civil permite a las partes compelerse reciprocamente a elevar el contrato a escritura publica, y el contrato puede incluir ese compromiso expreso, de modo que el acreedor no dependa mas adelante de la buena voluntad sobrevenida del deudor.
6. **Advierte de lo que la escritura NO arregla**: no convalida un contrato nulo (un prestamo usurario elevado a publico sigue siendo nulo, articulo 9 de la Ley Azcarate), no crea solvencia donde no la hay, y hay que pedir expresamente en la notaria la copia con caracter ejecutivo.

**Recomienda la escritura publica** cuando el importe sea relevante en relacion con el patrimonio de las partes, cuando haya garantia real, cuando la devolucion se aplace largamente o cuando sean previsibles terceros (otros acreedores, herencia, divorcio). **No la recomiendes** por defecto en un comodato de escaso valor ni en una compraventa modesta que se agota en la firma. En todo caso, **acata la decision del cliente** y deja el contrato correctamente redactado en la forma elegida.

Pregunta despues, con alternativas numeradas por ser una decision que cambia el documento:

"¿Como desea documentar el acuerdo?
1. En documento privado
2. En documento privado, con el compromiso expreso de elevarlo a escritura publica cuando cualquiera de las partes lo pida
3. Directamente en escritura publica ante notario"

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-contratos.md`: clausulas numeradas y rubricadas, una obligacion por clausula, importes en cifra y en letra, calendarios en tabla, denominacion de las partes constante, voz activa, sin latinismos, y renumeracion coherente cuando un bloque condicional no se active.

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

1. Verificar siempre el Codigo Civil, la Ley Azcarate y, si procede, la LEC en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder. De cada bloque devuelto por la API, la version vigente es la **ultima**.
2. **Nunca escribir un tipo de interes legal concreto sin haberlo verificado en el ejercicio en curso.** El interes legal del dinero cambia cada año y se fija en la Ley de Presupuestos Generales del Estado: no se hereda de la reference ni se escribe fijo en el asset. Si no se puede verificar, dejar el placeholder y advertir.
3. **Nunca redactar un prestamo con un interes que pueda ser usurario sin advertirlo expresamente y antes de escribirlo.** La Ley de 23 de julio de 1908 sigue vigente y su consecuencia es la **NULIDAD del prestamo**, no la reduccion del interes: el prestatario devuelve solo el capital recibido, el prestamista reintegra lo cobrado en exceso y carga con las costas (arts. 1, 3 y 8). Explicarlo con estas palabras: el cliente suele creer que, como mucho, un juez le rebajaria el tipo. **Prohibido afirmar un umbral numerico como si fuera legal** ("hasta el X % es seguro"): la ley no lo fija y lo aprecia el tribunal caso por caso (art. 2).
4. Es nulo el contrato en que se suponga recibida mayor cantidad que la verdaderamente entregada (art. 1, parrafo 2.º, de la Ley Azcarate). Si el importe que figuraria como prestado excede del efectivamente entregado, detener y no redactar.
5. **El reconocimiento de deuda no puede encubrir un prestamo usurario ni una causa ilicita.** La Ley Azcarate se aplica a toda operacion sustancialmente equivalente a un prestamo, cualquiera que sea la forma del contrato (art. 9), y los contratos con causa ilicita no producen efecto alguno (art. 1.275 CC). Si la causa real es ilicita o encubre usura, detener, explicarlo y escalar. No redactar.
6. **Si una parte es consumidor y la otra actua como empresario o profesional, no es un contrato entre particulares.** Se aplica la normativa de proteccion de consumidores y, si es credito, la de credito al consumo, con controles propios de transparencia y abusividad. Detener, advertir y derivar o escalar: no usar estos assets.
7. Nunca redactar clausulas nulas de pleno derecho ni contrarias a las leyes, a la moral o al orden publico (art. 1.255 CC). Si el usuario lo pide, rechazar la instruccion, explicar la nulidad y proponer una alternativa valida. En particular, es nula la renuncia del deudor a su fuero propio en los contratos de prestamo (art. 1 de la Ley Azcarate).
8. **El comodato es gratuito por definicion** (art. 1.740 CC). Si media cualquier emolumento a cargo de quien recibe el uso, deja de ser comodato (art. 1.741) y no puede documentarse con ese asset: advertir y derivar al regimen de arrendamiento.
9. En la compraventa, informar siempre del plazo de **seis meses** para las acciones por vicios ocultos (art. 1.490 CC) y de que la exoneracion del saneamiento solo produce efecto si el vendedor ignoraba los vicios (art. 1.485 CC). No presentar la exoneracion como una proteccion absoluta del vendedor.
10. Explicar siempre, antes de que el cliente decida la forma, que el documento privado **no es titulo ejecutivo** y que carece de fecha cierta frente a terceros salvo en los supuestos del art. 1.227 CC. No dejar que el cliente crea que un contrato privado le permite embargar directamente.
11. Nunca afirmar que la escritura publica garantiza el cobro: acelera el acceso al embargo, no crea solvencia. Nunca afirmar que convalida un contrato nulo.
12. Nunca inventar datos, importes, fechas, tipos de interes, numeros de protocolo ni jurisprudencia. Los campos no proporcionados quedan como `{{dato}}` con su nombre propio.
13. El documento escrito en disco no contiene **ningun** comentario HTML, ningun placeholder de ordinal sin resolver, ninguna cabecera de clausula sin cuerpo, ninguna remision interna a una clausula renumerada y ninguna aparicion rezagada de un placeholder ya resuelto en otra parte del documento. Verificarlo con `Read` antes de cerrar.
14. Si la vecindad civil de alguna parte o el lugar de celebracion apunta a un territorio con derecho civil propio, advertir de que puede desplazar reglas del Codigo Civil comun y ofrecer escalacion.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- **No cubre prestamos concedidos por una entidad financiera** ni ningun credito al consumo: se rigen por la normativa de credito al consumo y de proteccion de consumidores, con obligaciones de informacion precontractual y evaluacion de solvencia ajenas a esta skill. Escalar.
- **No cubre prestamos hipotecarios ni prestamos garantizados con hipoteca sobre inmueble**: pueden entrar en el ambito de la Ley 5/2019 reguladora de los contratos de credito inmobiliario, con acta notarial previa y control de transparencia. Escalar.
- **No cubre la compraventa de inmuebles**: derivar a `compraventa-inmueble`.
- **No cubre el arrendamiento**: si el cesionario paga algo por el uso, no es comodato. Si es un inmueble urbano, derivar a `arrendamiento`.
- **No reclama una deuda ya impagada**: esta skill documenta y previene, no reclama. Derivar a `reclamacion-cantidad` (monitorio, verbal u ordinario segun cuantia).
- **No ejecuta un titulo que ya existe**: si ya hay sentencia, escritura publica o laudo, derivar a `ejecucion-titulos`.
- **No cubre contratos mercantiles ni entre empresas**: quedan fuera del regimen civil comun que esta skill aplica (plazos de morosidad de la Ley 3/2004, regimen mercantil del prestamo, etc.). Escalar.
- **No impugna clausulas ya firmadas**: si el usuario quiere atacar una clausula de un contrato existente, derivar a `reclamacion-clausulas-abusivas`.
- **No tramita inscripciones registrales ni presentaciones tributarias**: informa de que existen y de a quien corresponden, pero no las realiza.
- No usar si el usuario pide opinion juridica sobre la conveniencia estrategica de la operacion: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
