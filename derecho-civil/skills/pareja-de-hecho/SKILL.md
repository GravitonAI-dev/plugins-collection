---
name: pareja-de-hecho
description: >
  Genera la documentacion propia de la pareja de hecho en sus tres momentos: (1) CONSTITUCION —
  checklist de inscripcion en el registro autonomico de parejas de hecho, con los requisitos, la
  documentacion y el tramite verificados en el lanzamiento contra la normativa de la comunidad
  autonoma concreta; (2) CONVIVENCIA — pacto de convivencia otorgado al amparo del articulo 1255 del
  Codigo Civil, que regula el regimen de los bienes de cada uno, los bienes adquiridos en comun y las
  aportaciones desiguales (arts. 392 a 406 CC), la vivienda, la contribucion a los gastos, las deudas
  y, si asi se pacta expresamente, una compensacion economica por la dedicacion a la familia o al
  negocio del otro; y (3) RUPTURA — pacto de extincion de la convivencia y liquidacion de la comunidad
  de bienes, con la cancelacion de la inscripcion registral, el destino de la vivienda y del prestamo
  hipotecario, las deudas y la compensacion que en su caso se convenga. NO existe ley estatal de
  parejas de hecho ni registro estatal: la skill pregunta SIEMPRE la comunidad autonoma y verifica su
  ley y su registro con `web_search` en cada lanzamiento, sin afirmar nunca un requisito autonomico de
  memoria. NO regula custodia, alimentos ni visitas de los hijos comunes (deriva a
  `medidas-hijos-no-matrimoniales`), NO cubre matrimonio, separacion ni divorcio, NO
  tramita la inscripcion ante el registro, NO cubre extranjeria ni reagrupacion familiar y NO resuelve
  el derecho a la pension de viudedad, del que solo informa.
when_to_use: |
  - Una pareja quiere constituirse e inscribirse como pareja de hecho y necesita saber que requisitos y
    que documentacion exige el registro de su comunidad autonoma.
  - Una pareja que convive quiere regular por escrito los aspectos economicos de su convivencia
    (bienes, vivienda, gastos, deudas, compensaciones).
  - Han comprado juntos una vivienda con aportaciones desiguales y quieren dejar constancia de ello.
  - Una pareja de hecho se separa y quiere liquidar de comun acuerdo lo que tienen en comun.
  - El usuario pregunta que derechos le da inscribirse como pareja de hecho, si hereda de su pareja o
    si tendra derecho a una compensacion si se separan.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
- finalidad: constituir e inscribir la pareja / regular la convivencia mediante pacto / regular la ruptura
  - comunidad_autonoma: comunidad de residencia de la pareja (vector obligatorio en todas las ramas)
  - hijos_comunes: si / no (determina la derivacion a la skill de medidas de hijos no matrimoniales)
  - bienes_o_desequilibrio: hay bienes adquiridos en comun o desequilibrio economico entre ellos / no
  - datos_conviviente_a: nombre, documento de identidad, domicilio
  - datos_conviviente_b: nombre, documento de identidad, domicilio
  - datos_convivencia: fecha de inicio, domicilio comun, situacion registral y, en su caso, fecha de cese
  - bienes_comunes: relacion de bienes adquiridos conjuntamente, titularidad formal y aportaciones reales
  - vivienda: situacion juridica, titularidad, prestamo hipotecario y destino del uso
  - gastos_y_deudas: criterio de contribucion, cuenta comun, deudas conjuntas
  - dedicacion: dedicacion de uno a la familia o al negocio del otro y compensacion que se pacte
  - liquidacion: acuerdo de adjudicacion, venta o compensacion de cuotas (solo ruptura)
outputs:
- checklist_inscripcion_registro: checklist de requisitos, documentacion y tramite del registro
    autonomico, en markdown, DRAFT, con la fecha de verificacion de la normativa autonomica
  - pacto_convivencia: pacto de convivencia en markdown, DRAFT
  - pacto_ruptura_pareja_hecho: pacto de extincion de la convivencia y liquidacion en markdown, DRAFT
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

# Constitucion, Convivencia y Ruptura de la Pareja de Hecho

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
    "finalidad_pareja": {
      "type": "string",
      "description": "Finalidad de la documentaci\u00f3n (V1)",
      "enum": [
        "registro_constitucion",
        "pacto_convivencia",
        "pacto_ruptura"
      ]
    },
    "comunidad_autonoma": {
      "type": "string",
      "description": "Comunidad Aut\u00f3noma de residencia habitual (V2)",
      "enum": [
        "madrid",
        "cataluna",
        "andalucia",
        "valencia",
        "otras_ccaa"
      ]
    }
  },
  "required": [
    "finalidad_pareja",
    "comunidad_autonoma"
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = 1 → **HOJA INSCRIPCION**: `assets/template-checklist-inscripcion-registro.md`. V3 y V4 no se preguntan como vectores; la existencia de hijos comunes se recaba en la seccion de pension de viudedad porque altera sus requisitos.
- Si V1 = 2 → **HOJA CONVIVENCIA**: `assets/template-pacto-convivencia.md`. V4 determina si se activan los bloques de bienes comunes, aportaciones desiguales y compensacion pactada.
- Si V1 = 3 → **HOJA RUPTURA**: `assets/template-pacto-ruptura-pareja-hecho.md`. V3 activa el bloque de remision sobre hijos comunes y dispara la derivacion; V4 determina los bloques de liquidacion y compensacion.
- Si V1 = 3 y V3 = 1 → ademas de la HOJA RUPTURA, **DERIVAR** expresamente para todo lo relativo a los hijos: custodia, regimen de estancias y visitas, y alimentos se regulan en `medidas-hijos-no-matrimoniales`, exigen la intervencion del Ministerio Fiscal y no producen efecto sin aprobacion judicial. **Esta skill no los regula ni los incluye en el pacto**: activa el bloque de remision del asset y ofrece continuar con esa skill al cerrar el documento.
- Si lo que se pretende es un matrimonio, una separacion o un divorcio, o la liquidacion de un regimen economico matrimonial → **DETENER**: fuera de alcance. Derivar a `divorcio` o a `liquidacion-gananciales` segun corresponda.
- Si lo que se pretende es tramitar la inscripcion ante el registro, o presentar la solicitud en nombre del cliente → **DETENER** esa pretension concreta: la skill prepara la documentacion y el checklist, pero la solicitud la presenta la propia pareja. Continuar con la HOJA INSCRIPCION advirtiendolo.
- Si aparecen indicios de violencia entre los convivientes → **DETENER de inmediato**, en el mismo turno, sin crear ni continuar ningun documento. Advertir y escalar a asistencia juridica especializada.

### Validacion de presupuestos (interno, antes del Punto 3)

- **TODAS LAS HOJAS:** ninguno de los convivientes puede estar unido por vinculo matrimonial con otra persona ni tener otra pareja de hecho constituida. Si consta que si, advertir de que la constitucion de la pareja no es posible y de que un pacto entre ellos puede afectar a derechos de terceros; detener la rama de inscripcion y escalar.
- **TODAS LAS HOJAS:** si los convivientes residen en comunidades autonomas distintas, tienen vecindad civil distinta, o concurre elemento internacional (residencia fuera de Espana, pareja constituida en el extranjero) → advertir de que la determinacion de la ley aplicable y del registro competente excede de lo que puede resolverse aqui, y escalar. En la rama de inscripcion, no continuar sin esa aclaracion.
- **HOJA INSCRIPCION:** si de la verificacion del Punto 2 resulta un requisito temporal (tiempo minimo de convivencia previa o de empadronamiento conjunto) que la pareja aun no cumple, **no dar por presentable la solicitud**: hacerlo constar en el checklist, indicar desde cuando podra presentarse y advertir de que la presentacion anticipada conduce a la denegacion o al archivo.
- **HOJA RUPTURA:** si existe un pacto de convivencia previo, pedirlo y leerlo con `Read` antes de redactar la liquidacion: sus previsiones para el cese son ley entre las partes y el pacto de ruptura las desarrolla o las sustituye expresamente, nunca las contradice en silencio.
- **HOJA RUPTURA:** si el cliente pide que el pacto incluya medidas sobre los hijos, rechazarlo y explicar por que (cauce propio, Ministerio Fiscal, aprobacion judicial). Recoger la remision, no la medida.
- **HOJA CONVIVENCIA y HOJA RUPTURA:** si el cliente pide una clausula que pretenda crear entre ellos una sociedad de gananciales, unas capitulaciones matrimoniales o un convenio regulador, rechazarla: son instituciones privativas del matrimonio. Explicar la alternativa valida (comunidad de bienes pactada sobre bienes concretos, o el propio pacto) y ofrecerla.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Leyes autonómicas reguladoras de parejas de hecho en la CCAA de residencia; Art. 1.255 del Código Civil (autonomía de la voluntad en pactos privados); doctrina del Tribunal Constitucional (STC 93/2013 y concordantes sobre inexistencia de equiparación matrimonial automática); y Art. 174 TRLGSS (pensión de viudedad).
2. **Orientación Legal del Caso:**
Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la normativa aplicable, ya verificada.** Empieza siempre por la advertencia de ausencia de ley estatal, sigue con la ley autonomica concreta verificada en este lanzamiento y su enlace, y cierra con la base de derecho comun del documento. Textos fijos por hoja:
   - INSCRIPCION: "No existe una ley estatal de parejas de hecho ni un registro estatal: la materia la regula cada comunidad autonoma. A su caso le resulta de aplicacion {{denominacion_ley_autonomica}}, que he verificado hoy en su fuente oficial: {{enlace_ley_autonomica}}. El registro competente es el {{denominacion_registro}}: {{enlace_registro}}."
   - CONVIVENCIA: "No existe una ley estatal de parejas de hecho, y la convivencia no crea entre ustedes ningun regimen economico. El pacto que vamos a preparar se otorga al amparo del articulo 1255 del Codigo Civil, y a los bienes que hayan adquirido conjuntamente les resultan de aplicacion los articulos 392 y siguientes del mismo cuerpo legal, sobre la comunidad de bienes. Puede consultar el texto oficial en https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763. En cuanto a su comunidad autonoma, he verificado hoy {{denominacion_ley_autonomica}}: {{enlace_ley_autonomica}}."
   - RUPTURA: "Al no haber existido matrimonio entre ustedes, no hay regimen economico matrimonial que liquidar ni cabe un convenio regulador. Lo que vamos a preparar es un pacto otorgado al amparo del articulo 1255 del Codigo Civil, que liquida la comunidad de bienes sobre lo adquirido conjuntamente conforme a los articulos 392 y siguientes. Puede consultar el texto oficial en https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763. En cuanto a su comunidad autonoma, he verificado hoy {{denominacion_ley_autonomica}}: {{enlace_ley_autonomica}}."
   - Si la verificacion autonomica fallo, sustituye la parte autonomica por el texto del Punto 2.6. **Nunca inventes una denominacion de ley ni un enlace.**
   - **Correccion inmediata del malentendido, si el cliente ya lo ha planteado.** Si en sus mensajes ha preguntado o dado por supuesto que inscribirse equipara al matrimonio, que crea gananciales, que da derecho a heredar o que garantiza una compensacion, **respondele aqui, en este mismo mensaje**, sin esperar a la seccion de la edicion incremental que trate esa materia. Diez turnos despues es tarde: el cliente esta tomando su decision ahora. Di con todas las letras que no, y por que: la inscripcion no crea ningun regimen economico, lo adquirido en comun se rige por los articulos 392 y siguientes del Codigo Civil segun la titularidad, y **el conviviente no hereda sin testamento** salvo lo que prevea la normativa civil aplicable que hayas verificado. Si ha preguntado por heredar, anade que la unica via es otorgar testamento ante notario, con el limite de las legitimas, y ofrece continuar despues con `testamento-planificacion`. Esta correccion no sustituye a la seccion correspondiente del Punto 5: la anticipa.
   - Si V1 = 3 y V3 = 1 (hay hijos comunes), anade en el mismo mensaje: "Le adelanto que todo lo relativo a sus hijos — guarda y custodia, regimen de estancias y pension de alimentos — no puede regularse en este pacto: tiene un cauce propio, exige la intervencion del Ministerio Fiscal y no produce efecto sin aprobacion judicial. Lo trataremos en un documento aparte cuando cerremos este."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio (adviertele si el documento adjuntado los incumple, y en particular si contiene clausulas que presupongan un regimen economico inexistente o que regulen medidas sobre los hijos).
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-checklist-inscripcion-registro.md`).
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

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma parte se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las clausulas marcadas `[negociacion]` se explican y se confirman una a una. **La vista previa y la confirmacion agrupada de una parte se emiten en el turno SIGUIENTE a la respuesta del ultimo sub-apartado, nunca en el mismo turno en que aun se esta preguntando ese ultimo dato.**

**Regla propia de esta materia para las clausulas `[negociacion]`:** antes de pedir la decision, explica siempre **cual es el regimen por defecto si no se pacta nada** y que consecuencia tiene. En pareja de hecho el regimen por defecto es casi siempre "nada", y el cliente no lo sabe: si no se le explica, decide a ciegas. Esta explicacion es breve — dos o tres frases — y va en el mismo turno que la pregunta.

### Secciones — HOJA CONVIVENCIA

1. **Datos de cada conviviente** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de ambos convivientes." Sub-apartados, uno por turno, primero los del conviviente A y despues los del B: a) nombre completo; b) tipo y numero de documento de identidad; c) domicilio. Al recibir la respuesta al ultimo dato de cada conviviente, vista previa unica de esa parte y una sola confirmacion antes del `Edit`.
2. **La convivencia y su situacion registral** *(dato objetivo)*. Anuncio fijo: "Concretamos ahora los datos de su convivencia y su situacion registral." Sub-apartados, uno por turno: a) fecha de inicio de la convivencia; b) domicilio comun; c) si la pareja esta inscrita, tiene previsto inscribirse o no piensa hacerlo — y, si esta inscrita, fecha de inscripcion. Activa segun la respuesta el expositivo TERCERO que corresponda, en su unica variante.
3. **Regimen de los bienes de cada uno** *(negociacion)*. Anuncio fijo: "Abordamos ahora el regimen de sus bienes." Explica antes de preguntar: la convivencia no crea ningun regimen economico, cada uno conserva lo suyo y lo que gane durante la convivencia, y la ley no impone participacion alguna en lo del otro; eso seguira siendo asi salvo que lo pacten de otro modo. Pregunta despues si desean ademas inventariar en el pacto los bienes privativos de cada uno para facilitar la prueba de la titularidad, y activa o descarta ese bloque.
4. **Bienes adquiridos en comun y aportaciones desiguales** *(negociacion — la seccion mas importante del documento)*. Anuncio fijo: "Pasamos a los bienes que hayan adquirido conjuntamente." Explica antes: lo adquirido en comun se rige por la comunidad de bienes de los articulos 392 y siguientes del Codigo Civil, **las cuotas se presumen iguales salvo prueba en contrario** (articulo 393) y quien aporto mas dinero del que refleja la titularidad tiene la carga de probarlo. Sub-apartados, uno por turno: a) relacion de bienes adquiridos en comun, con su titularidad formal; b) si las aportaciones economicas reales coincidieron con esa titularidad y, si no, cuanto aporto cada uno. Si hubo desigualdad, pregunta despues cual de los tres efectos quieren darle, explicando los tres: que genere un credito exigible en la liquidacion, que se ajuste la cuota de titularidad a la aportacion real, o que se considere una liberalidad sin credito alguno. Advierte de que la tercera opcion es irreversible en la practica y de que la segunda exige otorgar despues la escritura que rectifique la titularidad. Confirmacion propia de cada decision.
5. **Vivienda que constituye el domicilio comun** *(negociacion)*. Anuncio fijo: "Determinamos ahora la situacion de la vivienda en la que conviven." Sub-apartados: a) situacion juridica (propiedad de uno, propiedad comun o arrendamiento), activando la variante correspondiente; b) si existe prestamo hipotecario y como se reparten las cuotas. Explica siempre que el reparto pactado **no vincula a la entidad prestamista**, frente a la cual ambos siguen respondiendo. Si la vivienda es propiedad de uno solo, explica que el otro la ocupa por tolerancia y sin derecho arrendaticio, y pregunta que plazo de desalojo quieren fijar para el caso de cese.
6. **Pacto de indivision** *(negociacion — condicional, solo si hay bienes comunes)*. Anuncio fijo: "Valoramos si les conviene pactar que algun bien comun no pueda dividirse durante un tiempo." Explica el articulo 400 del Codigo Civil: por defecto cualquiera de los dos puede pedir la division en cualquier momento, y si el bien es indivisible — una vivienda lo es — el desenlace legal es la venta y el reparto del precio (articulo 404); cabe pactar la indivision por un plazo no superior a diez anos. Pregunta si desean pactarla, sobre que bien y por cuanto tiempo.
7. **Contribucion a los gastos y cuenta comun** *(negociacion)*. Anuncio fijo: "Pasamos a la contribucion a los gastos de la convivencia." Explica: entre convivientes no existe deber legal de contribuir a las cargas, a diferencia del matrimonio; lo que se pacte aqui es lo unico que les obligara. Sub-apartados: a) criterio de contribucion (por mitades, proporcional a los ingresos u otro); b) si van a usar una cuenta comun y con que aportacion mensual.
8. **Deudas** *(negociacion)*. Anuncio fijo: "Concretamos ahora el regimen de las deudas." Explica: cada uno responde de lo que contrae a su nombre y el otro no queda obligado, salvo lo contraido conjuntamente o lo que derive de los bienes y gastos comunes. Pregunta si existe alguna deuda conjunta que quieran identificar.
9. **Dedicacion a la familia o al negocio del otro y compensacion pactada** *(negociacion — trato especialmente cuidadoso)*. Anuncio fijo: "Abordamos ahora la dedicacion de uno de ustedes a la familia o a la actividad del otro." Explica, sin prometer nada: si uno de los dos deja o reduce su actividad profesional para dedicarse a la casa, a los hijos o al negocio del otro, **la ley no le reconoce ninguna compensacion automatica** — las normas del matrimonio, incluida la compensacion por trabajo domestico, no se aplican por analogia a la pareja de hecho, y la unica via en defecto de pacto es el enriquecimiento injusto, que exige prueba y tiene resultado incierto; por eso, si esa dedicacion existe o va a existir, la forma segura de protegerla es pactar ahora la compensacion. Pregunta si concurre esa situacion y, si concurre: quien se dedica y a que, y que compensacion e importe acuerdan, con su forma de pago. Al redactar, **expresa siempre la causa** de la compensacion en la propia clausula (articulos 1274 y 1275 del Codigo Civil). Si el cliente pregunta si "le corresponde" una compensacion, responde que no le corresponde por ley y que lo que se esta creando es el derecho, no reconociendolo.
10. **Previsiones para el cese de la convivencia** *(negociacion)*. Anuncio fijo: "Preveamos ahora que ocurrira si la convivencia cesa." Explica que un pacto sin clausula de liquidacion deja a las partes igual que si no existiera. Pregunta el plazo que quieren fijar para liquidar los bienes comunes y las cuentas pendientes tras el cese.
11. **Hijos comunes** *(informativo con derivacion — condicional)*. Anuncio fijo: "Una precision sobre sus hijos comunes." Solo si existen. Explica que las medidas sobre los hijos no pueden regularse en este pacto, activa el bloque de remision del asset y ofrece tratarlas despues con `medidas-hijos-no-matrimoniales`. No pidas ningun dato de los hijos aqui.
12. **Prevision sucesoria** *(negociacion)*. Anuncio fijo: "Le informo de un punto que suele pasarse por alto: la sucesion." Explica: salvo lo que prevea la normativa civil aplicable, **el conviviente no hereda sin testamento**, por larga que sea la convivencia y este o no inscrita la pareja; para protegerse mutuamente hay que otorgar testamento ante notario, con el limite de las legitimas si hay descendientes o ascendientes. Ofrece continuar despues con `testamento-planificacion`, que prepara la minuta de testamento abierto para llevar a la notaria, advirtiendo de que esa skill cubre unicamente derecho civil comun y no vecindad civil foral. Pregunta si desean incluir en el pacto la clausula de prevision sucesoria, dejando constancia de esa voluntad.
13. **Duracion, controversias y eficacia** *(dato objetivo con explicacion)*. Anuncio fijo: "Cerramos con la vigencia del pacto y la forma de resolver discrepancias." Sub-apartados: a) fecha de entrada en vigor; b) medio de solucion de controversias al que se comprometen antes de acudir a los tribunales. Explica al cerrar que el documento privado carece de fuerza ejecutiva y que elevarlo a escritura publica le da fecha cierta y facilita su prueba.
14. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del pacto." Lugar de firma; fecha del dia salvo indicacion en contrario.

### Secciones — HOJA RUPTURA

1. **Datos de cada conviviente** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de ambos convivientes." Igual estructura que en la HOJA CONVIVENCIA.
2. **La convivencia, su cese y la situacion registral** *(dato objetivo)*. Anuncio fijo: "Concretamos ahora las fechas de la convivencia y su situacion registral." Sub-apartados, uno por turno: a) fecha de inicio; b) fecha de cese; c) si la pareja estaba inscrita y, en tal caso, fecha de inscripcion y plazo en que se comprometen a solicitar la cancelacion; d) si existe un pacto de convivencia previo (si lo hay, pedirlo y leerlo con `Read` antes de continuar). Explica al tratar la cancelacion que, mientras no se practique, la inscripcion sigue produciendo sus efectos.
3. **Hijos comunes** *(informativo con derivacion — condicional, se trata pronto a proposito)*. Anuncio fijo: "Antes de entrar en lo economico, una precision sobre sus hijos." Solo si V3 = 1. Explica que la guarda y custodia, el regimen de estancias y la pension de alimentos no se regulan en este pacto porque tienen cauce propio, exigen la intervencion del Ministerio Fiscal y no producen efecto sin aprobacion judicial; que ninguna clausula economica de este documento puede condicionar ni compensar los derechos de los hijos; y que al cerrar este pacto se puede continuar con `medidas-hijos-no-matrimoniales`. Activa el bloque de remision del asset. **No recabes ningun dato de los hijos**: nombres, edades o cualquier otro dato corresponden a la otra skill.
4. **Liquidacion de los bienes adquiridos en comun** *(negociacion)*. Anuncio fijo: "Pasamos a liquidar los bienes que adquirieron conjuntamente." Explica antes: no hay regimen economico matrimonial que liquidar, solo la comunidad de bienes sobre lo que figure a nombre de ambos; por defecto, si no hay acuerdo, cualquiera puede pedir la division y, si el bien es indivisible, se vende y se reparte el precio (articulos 400 y 404). Sub-apartados, uno por turno: a) relacion de bienes comunes y titularidad; b) para cada bien, si se adjudica a uno compensando al otro, si se vende, o si no hay acuerdo. Confirmacion por cada bien.
5. **Aportaciones desiguales** *(negociacion — condicional)*. Anuncio fijo: "Verificamos si las aportaciones a esos bienes fueron desiguales." Explica la presuncion de cuotas iguales del articulo 393 y la carga de la prueba. Pregunta cuanto aporto cada uno realmente y, si hubo desigualdad, si reconocen un credito, por que importe y con que forma de pago. Redacta el reconocimiento **expresando su causa**.
6. **Vivienda y prestamo hipotecario** *(negociacion)*. Anuncio fijo: "Determinamos ahora el destino de la vivienda que fue su domicilio." Sub-apartados: a) situacion juridica y titularidad; b) a quien se atribuye el uso y en que fecha desaloja el otro; c) reparto de los gastos a partir del cese; d) si hay prestamo hipotecario, capital pendiente, reparto de cuotas y hasta que hito. Explica siempre que el reparto **no vincula a la entidad prestamista** y que la liberacion de un prestatario exige su consentimiento expreso, que no esta obligada a dar. Si la vivienda es arrendada, trata la posicion arrendaticia y la fianza, advirtiendo de que puede requerir el consentimiento del arrendador.
7. **Cuentas y deudas** *(negociacion — condicional)*. Anuncio fijo: "Pasamos a las cuentas y deudas comunes." Sub-apartados: a) cuenta comun, plazo de cancelacion y reparto del saldo; b) deudas contraidas conjuntamente y como se atienden. Explica que el reparto interno no libera a ninguno frente al acreedor.
8. **Compensacion economica** *(negociacion — trato especialmente cuidadoso)*. Anuncio fijo: "Abordamos ahora si procede una compensacion economica entre ustedes." Explica, sin prometer nada: la ley **no reconoce automaticamente** una compensacion al conviviente en la ruptura; las normas del matrimonio no se aplican por analogia, y en defecto de pacto la unica via es el enriquecimiento injusto, que exige acreditar que la dedicacion de uno produjo un enriquecimiento correlativo del otro y cuyo resultado es incierto — el propio Tribunal Supremo la ha rechazado cuando falta esa prueba. Por eso, lo que da certeza es pactarla ahora. Pregunta si existio esa dedicacion, en que consistio y si acuerdan una compensacion, con importe y forma de pago. Redacta siempre **expresando la causa**. Si el cliente insiste en que "le corresponde por ley", corrigelo con claridad y sin dar falsas expectativas.
9. **Bienes muebles, ajuar y animales de compania** *(negociacion)*. Anuncio fijo: "Repartimos ahora los bienes muebles y el ajuar." Sub-apartados: a) reparto de muebles y ajuar y fecha de retirada; b) si hay animales de compania, su destino — explicando que el articulo 404 del Codigo Civil prohibe dividirlos mediante venta salvo acuerdo unanime y que, a falta de acuerdo, decide el juez atendiendo al bienestar del animal.
10. **Alcance de la liquidacion** *(negociacion)*. Anuncio fijo: "Precisamos el alcance de la liquidacion que estan acordando." Explica que la clausula de finiquito cierra cualquier reclamacion economica futura entre ellos derivada de la convivencia, incluida la fundada en enriquecimiento injusto, y que por eso solo debe firmarse cuando ambos consideren que la liquidacion es completa; explica tambien que **no alcanza a los derechos de los hijos**, que son irrenunciables. Pregunta si la aceptan en esos terminos.
11. **Controversias y eficacia** *(dato objetivo con explicacion)*. Anuncio fijo: "Cerramos con la forma de resolver discrepancias y la eficacia del pacto." Pregunta el medio de solucion de controversias. Explica que el documento privado carece de fuerza ejecutiva y que, si el pacto incluye pagos aplazados o adjudicacion de inmuebles, la elevacion a escritura publica es necesaria para el Registro de la Propiedad y muy recomendable en todo caso.
12. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del pacto."

### Secciones — HOJA INSCRIPCION

1. **Datos de cada conviviente** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de ambos convivientes." Igual estructura que en las otras hojas.
2. **Situacion de la pareja frente a los requisitos verificados** *(dato objetivo con validacion bloqueante)*. Anuncio fijo: "Contrastamos ahora su situacion con los requisitos que exige el registro." Recorre uno por uno **solo los requisitos que la verificacion del Punto 2.3 haya devuelto**, preguntando por cada uno la situacion de la pareja: edad, ausencia de vinculo, parentesco, tiempo de convivencia previa, empadronamiento conjunto, residencia. **Prohibido preguntar por un requisito que no conste en la verificacion, y prohibido dar por exigido uno que no se haya verificado.** Poda la tabla del asset conforme a la regla de tres situaciones del Punto 4: elimina entera la fila de requisito adicional si la verificacion no devolvio ninguno, y al cerrar la seccion ninguna fila puede quedar con un placeholder a la vista. **Un requisito que la verificacion devuelve como NO exigido no se borra: se conserva diciendo que no se exige.** Que la comunidad no imponga tiempo minimo de convivencia previa o empadronamiento conjunto es informacion que el cliente necesita — suele creer lo contrario — y borrar la fila se la oculta. Si algun requisito temporal no se cumple todavia, calcula desde cuando podra presentarse la solicitud, hazlo constar y advierte de que presentarla antes conduce a la denegacion o al archivo.
3. **Documentacion y tramite** *(dato objetivo)*. Anuncio fijo: "Relacionamos la documentacion y el tramite." Vuelca la documentacion, la forma de presentacion, el organo competente, la tasa y los plazos tal como los haya devuelto la verificacion. Pregunta el municipio de residencia y comprueba si existe ademas registro municipal; si lo hay, activa ese bloque y advierte de que los efectos de uno y otro pueden no coincidir.
4. **Que produce y que no produce la inscripcion** *(negociacion — es el nucleo pedagogico del documento)*. Anuncio fijo: "Le explico ahora que efectos tiene realmente la inscripcion." Explica los cuatro puntos, sin suavizarlos: no equipara la pareja al matrimonio, no crea ningun regimen economico, no genera derecho automatico a compensacion en caso de ruptura, y no convierte al conviviente en heredero. Explica tambien lo que si aporta: prueba de la existencia y de la fecha de la pareja, que es justo lo que despues exigen otras normas. Pregunta si desea que se incluyan en el documento los efectos que la ley autonomica verificada atribuye a la inscripcion.

**Trampa al volcar `{{efectos_inscripcion}}`: "sucesiones" casi nunca significa heredar.** Los portales autonomicos suelen listar la equiparacion al matrimonio "en materia de sucesiones", y se refieren al **Impuesto sobre Sucesiones y Donaciones**, que es un tributo cedido, no a los derechos sucesorios civiles. Copiar esa frase tal cual convierte el documento en autocontradictorio: afirmaria en este apartado lo que niega en el apartado de sucesion, y sobre el punto que mas le importa al cliente. Al volcar los efectos, **separa siempre lo fiscal de lo civil** y di expresamente si la comunidad tiene o no derecho civil propio que reconozca derechos sucesorios al conviviente. Si no lo has verificado, no lo afirmes en ninguno de los dos sentidos.
5. **Pension de viudedad** *(informativo con derivacion)*. Anuncio fijo: "Le informo de los requisitos propios de la pension de viudedad, que no son los del registro." Explica los cuatro requisitos del articulo 221 de la Ley General de la Seguridad Social, y en particular las dos consecuencias practicas: la antelacion minima de dos anos de la inscripcion respecto del fallecimiento, y que los cinco anos de convivencia se acreditan con el empadronamiento conjunto y no con la inscripcion. Pregunta si tienen hijos en comun, porque exime del requisito de los cinco anos, y activa el bloque correspondiente. Advierte de que la skill informa pero **no tramita ni valora** el derecho a la pension, y deriva al Instituto Nacional de la Seguridad Social o a un especialista.
6. **Sucesion y testamento** *(informativo)*. Anuncio fijo: "Un punto que suele pasarse por alto: la sucesion." Explica que el conviviente no hereda sin testamento salvo lo que prevea la normativa civil aplicable, y que la unica via de proteccion mutua es otorgar testamento ante notario, con el limite de las legitimas. Ofrece continuar despues con `testamento-planificacion`, advirtiendo de que esa skill cubre unicamente derecho civil comun y no vecindad civil foral, y de que el testamento se otorga siempre ante notario.
7. **Recomendacion de pacto de convivencia** *(negociacion)*. Anuncio fijo: "Por ultimo, le recomiendo valorar un pacto de convivencia." Explica que la inscripcion prueba que la pareja existe pero no regula nada entre ellos, y que todo lo economico solo queda regulado si se pacta. Ofrece preparar el pacto de convivencia a continuacion; si acepta, al cerrar este documento reinicia el flujo por la HOJA CONVIVENCIA reutilizando los datos ya recabados, **sin volver a preguntarlos**.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: expositivos numerados y breves, una idea por clausula, importes en cifra y letra, causa expresada en toda prestacion economica, sin latinismos, y ninguna clausula sobre una materia que el cliente no haya decidido.

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

1. **Nunca afirmar un requisito, un registro, un plazo o un efecto autonomico que no se haya verificado en este mismo lanzamiento** (Punto 2.3). No existe ley estatal de parejas de hecho: cualquier afirmacion autonomica no verificada es una invencion. Si la verificacion falla, decirlo con las palabras del Punto 2.6, dejar el punto pendiente en el documento y no afirmarlo.
2. **Nunca dar a entender que la pareja registrada equivale al matrimonio.** No hay equiparacion general: cada efecto tiene su propia norma y sus propios requisitos. Corregir activamente el malentendido cuando aparezca, aunque el cliente no pregunte.
3. **Nunca decir que la convivencia crea un regimen economico.** No nacen gananciales ni ningun otro regimen; cada uno conserva lo suyo y lo comun se rige por la comunidad de bienes segun la titularidad. Nadie queda sometido a un regimen por el mero hecho de convivir.
4. **Nunca prometer una compensacion economica como si fuera automatica.** Las normas del matrimonio, incluida la compensacion por trabajo domestico del articulo 1438 del Codigo Civil, **no se aplican por analogia** a la pareja de hecho. La via del enriquecimiento injusto existe solo en defecto de pacto, exige prueba de sus requisitos y tiene resultado incierto. Explicar que lo que da certeza es el pacto, y que el pacto crea el derecho, no lo reconoce.
5. **Nunca citar una sentencia que no se haya verificado en esta sesion.** Las unicas verificadas y registradas en `references/fuentes-plantillas-validadas.md` son la STC 81/2013, la STC 93/2013, la STS de 12 de septiembre de 2005 y la STS 17/2018, de 15 de enero. Cualquier otra se enuncia como criterio jurisprudencial sin atribucion, o no se enuncia.
6. **Nunca afirmar que el conviviente hereda.** Salvo lo que prevea la normativa civil aplicable y verificada, no hereda sin testamento. Advertirlo siempre en las tres hojas.
7. **Nunca resolver el derecho a la pension de viudedad.** Informar de los requisitos del articulo 221 de la Ley General de la Seguridad Social y derivar. No calcular, no valorar el caso, no anticipar el resultado.
8. **Nunca regular en estos pactos custodia, alimentos, estancias ni visitas de los hijos comunes.** Cauce propio, Ministerio Fiscal y aprobacion judicial. Derivar a `medidas-hijos-no-matrimoniales`, activar el bloque de remision y no recabar datos de los hijos.
9. **Nunca redactar clausulas que presupongan instituciones matrimoniales** (gananciales, capitulaciones, convenio regulador, pension compensatoria del articulo 97 del Codigo Civil): son privativas del matrimonio y una clausula asi seria ineficaz. Rechazar, explicar y ofrecer la alternativa valida.
10. **Nunca afirmar efectos frente a terceros que el pacto no puede producir.** El reparto de cuotas hipotecarias o de deudas no vincula al acreedor; la subrogacion arrendaticia puede requerir el consentimiento del arrendador; los efectos fiscales dependen de normativa que la skill no verifica y se derivan a asesor fiscal.
11. **Violencia entre los convivientes: detener y escalar de inmediato**, en el mismo turno y sin crear ni continuar documento alguno.
12. **Nunca inventar datos, importes, fechas, denominaciones de registro ni enlaces.** Los campos no proporcionados quedan como `{{dato}}` con su nombre propio. Un enlace inventado a una sede electronica es especialmente grave: el cliente lo seguira.
13. **Documento escrito sin comentarios HTML y con numeracion correlativa.** Resolver todos los bloques condicionales y renumerar las clausulas tras insertar o descartar cualquiera de ellos.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- **No regula la guarda y custodia, la pension de alimentos ni el regimen de estancias y visitas de los hijos comunes**: derivar a `medidas-hijos-no-matrimoniales`. Esta skill se ocupa exclusivamente de lo patrimonial entre los convivientes.
- **No tramita la inscripcion ante el registro autonomico ni municipal**: genera la documentacion y el checklist del tramite, pero la solicitud la presenta la propia pareja.
- **No cubre el matrimonio, la separacion ni el divorcio**, ni la liquidacion de un regimen economico matrimonial: derivar a `divorcio` o a `liquidacion-gananciales`.
- **No cubre extranjeria ni reagrupacion familiar**, aunque la pareja registrada tenga efectos en esa normativa: es derecho administrativo, fuera del plugin.
- **No resuelve el derecho a la pension de viudedad ni a ninguna otra prestacion de la Seguridad Social**: informa de los requisitos y deriva.
- **No redacta testamentos ni planifica la sucesion**: advertir de la necesidad del testamento y derivar a `testamento-planificacion`, que prepara la minuta para la notaria. `herencia` tampoco sirve para esto: excluye expresamente la redaccion de testamentos.
- **No presta asesoramiento fiscal** sobre las adjudicaciones, donaciones o transmisiones entre convivientes.
- **No se usa para reclamar judicialmente una compensacion frente al otro conviviente**: si no hay acuerdo, el pacto no es la via. Escalar.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.