---
name: responsabilidad-civil
description: >
  Genera el escrito adecuado para reclamar la indemnizacion de los danos y perjuicios sufridos por un
  perjudicado, con la normativa verificada en el BOE: reclamacion extrajudicial de danos (que interrumpe
  la prescripcion del Art. 1973 CC, abre la actividad negociadora previa del Art. 5 LO 1/2025 y, en
  circulacion, constituye la reclamacion previa al asegurador del Art. 7.1 TRLRCSCVM), demanda de
  responsabilidad civil contractual (Arts. 1101 y 1103 CC) o extracontractual (Arts. 1902, 1903, 1907 y
  1908 CC), con accion directa contra la aseguradora del responsable (Art. 76 LCS), y escrito de
  contestacion, aceptacion o rechazo de la oferta o respuesta motivada de una aseguradora (Arts. 7.2 a
  7.6, 9 y 14 TRLRCSCVM). Cubre los accidentes de circulacion con vehiculo a motor, los accidentes con
  vehiculo personal ligero o patinete (sujetos al seguro obligatorio creado por la disposicion adicional
  primera de la Ley 5/2025 desde el 02/01/2026), las caidas en establecimiento, los vicios y defectos
  constructivos (Arts. 17 y 18 LOE, Art. 1591 CC) y la negligencia profesional. Aplica un filtro de
  prescripcion BLOQUEANTE antes de redactar nada. NO usar para la responsabilidad civil derivada de
  delito ni para la pieza de responsabilidad civil de un proceso penal, para la responsabilidad
  patrimonial de la Administracion, ni para danos laborales o accidentes de trabajo.
when_to_use: |
  - El usuario ha sufrido un dano personal o material por un accidente de circulacion y quiere reclamar
    la indemnizacion al causante o a su aseguradora.
  - El usuario ha sido atropellado por un patinete o vehiculo personal ligero, o ha sufrido un accidente
    con uno de ellos, y quiere reclamar.
  - El usuario se ha caido o ha sufrido un dano en un establecimiento abierto al publico y quiere
    reclamar al titular.
  - El usuario tiene desperfectos o defectos constructivos en su vivienda o edificio y quiere reclamar a
    la promotora, la constructora o los tecnicos.
  - El usuario cree que un profesional (sanitario, letrado, tecnico) le ha causado un dano por una
    actuacion negligente y quiere reclamar.
  - El usuario ha sufrido un dano por el incumplimiento de un contrato y quiere reclamar la
    indemnizacion de los danos y perjuicios.
  - El usuario ya reclamo y la aseguradora le ha enviado una oferta motivada o una respuesta motivada, y
    quiere contestarla, aceptarla a cuenta o rechazarla.
  - El usuario quiere saber si su reclamacion esta todavia en plazo y como interrumpir la prescripcion.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - ambito_hecho: accidente de circulacion / otro suceso
  - tipo_vehiculo_causante: vehiculo a motor / vehiculo personal ligero o patinete
  - supuesto_no_circulatorio: caida en establecimiento o via publica / defecto o vicio constructivo / negligencia profesional
  - naturaleza_vinculo: contractual / extracontractual
  - momento_documento: primera reclamacion extrajudicial / contestacion a una oferta o respuesta motivada / demanda judicial
  - aseguradora_identificada: si / no o desconocida
  - fecha_hecho: fecha del hecho danoso
  - fecha_conocimiento_dano: fecha del alta medica o de la estabilizacion de secuelas, o de aparicion del dano
  - actos_interruptivos: relacion de reclamaciones previas fehacientes con su fecha y su medio
  - datos_perjudicado: nombre, documento de identidad, domicilio, telefono, email
  - datos_responsable: nombre o razon social, documento de identidad, domicilio
  - datos_aseguradora: denominacion, CIF, domicilio, numero de poliza, referencia del siniestro
  - danos: descripcion y soporte documental del dano personal, del dano material y del lucro cesante
  - cuantificacion: importe por partida y su fuente (tabla del baremo del ejercicio o informe pericial)
  - datos_oferta_motivada: tipo de comunicacion, fecha de notificacion, importe ofertado, requisitos cumplidos
outputs:
  - reclamacion_extrajudicial_danos: reclamacion extrajudicial fehaciente de danos en markdown, DRAFT
  - demanda_responsabilidad_civil: demanda de juicio ordinario o verbal de responsabilidad civil en markdown, DRAFT
  - respuesta_oferta_motivada: escrito de aceptacion, aceptacion a cuenta o rechazo de la oferta o respuesta motivada en markdown, DRAFT
references:
  - references/cuantificacion-danos-y-baremo.md
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/prescripcion-y-computo-de-plazos.md
  - references/regimenes-de-responsabilidad-por-supuesto.md
assets:
  - assets/template-demanda-responsabilidad-civil.md
  - assets/template-reclamacion-extrajudicial-danos.md
  - assets/template-respuesta-oferta-motivada.md
---

# Reclamacion de Danos y Perjuicios por Responsabilidad Civil

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
    "ambito_suceso": {
      "type": "string",
      "description": "\u00c1mbito del suceso da\u00f1oso (V1)",
      "enum": [
        "accidente_trafico",
        "caida_establecimiento",
        "contractual_profesional",
        "extracontractual_general"
      ]
    },
    "fase_reclamacion": {
      "type": "string",
      "description": "Fase de la reclamaci\u00f3n indemnizatoria (V3)",
      "enum": [
        "extrajudicial_previa",
        "respuesta_oferta",
        "demanda_judicial"
      ]
    }
  },
  "required": [
    "ambito_suceso",
    "fase_reclamacion"
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables y superado el filtro de prescripcion, evalua en este orden:

- Si V5 = 1 → **HOJA RECLAMACION**: `assets/template-reclamacion-extrajudicial-danos.md`.
- Si V5 = 2 → **HOJA OFERTA**: `assets/template-respuesta-oferta-motivada.md`.
- Si V5 = 3 → **HOJA DEMANDA**: `assets/template-demanda-responsabilidad-civil.md`, con la validacion de procedibilidad del apartado siguiente.
- Si V5 = 3, V1 = 1 y **no consta reclamacion previa al asegurador** → **NO crear la demanda**. Explicar que el Art. 7.8 TRLRCSCVM, en relacion con el Art. 403 LEC, impide admitir a tramite las demandas que no acompanen la oferta o la respuesta motivada o, en su defecto, la reclamacion previa al asegurador. Redirigir a la HOJA RECLAMACION y ofrecer preparar la demanda despues.
- Si V5 = 3, V1 = 2 y **no consta ninguna actividad negociadora previa** → **NO crear la demanda**. Explicar el requisito de procedibilidad del Art. 5 LO 1/2025 y del Art. 264.4.º LEC. Redirigir a la HOJA RECLAMACION. Excepcion: si el cliente **desconoce el domicilio del demandado o el medio por el que puede requerirle**, el Art. 264.4.º LEC admite en su lugar una declaracion responsable de la imposibilidad de llevar a cabo la actividad negociadora previa; en ese caso continuar con la HOJA DEMANDA y advertir de que debera aportarse esa declaracion.
- Si V5 = 2 y V1 = 2 → usar la HOJA OFERTA, **desactivando todos los bloques que invocan el Art. 7 TRLRCSCVM**: fuera de la circulacion la aseguradora no esta sujeta al procedimiento de oferta y respuesta motivada, y lo recibido es una oferta contractual ordinaria regida por los Arts. 18 y 20 LCS. Decirselo al cliente expresamente.
- Si V1 = 1, V2 = 2 y el hecho es **anterior al 02/01/2026** → el seguro obligatorio de vehiculos personales ligeros **no estaba en vigor**. No afirmar que existe. Reconducir al Art. 1902 CC con culpa probada frente al patrimonio del causante, preguntar si el causante tenia algun seguro voluntario de responsabilidad civil (a menudo el del hogar) y advertir de que el baremo del Anexo pasa a ser solo orientativo.
- Si V1 = 1, V2 = 2 y el hecho es **posterior al 02/01/2026** → antes de afirmar que hay seguro obligatorio, comprobar los tres requisitos acumulativos del apartado 1 de la disposicion adicional primera de la Ley 5/2025: certificado de circulacion, inscripcion en el Registro de Vehiculos de la DGT y etiqueta identificativa con el numero de inscripcion o matricula. Si no concurren, aplicar el mismo tratamiento que en el caso anterior.
- Si el vehiculo causante **circulaba sin seguro, no esta identificado o su aseguradora esta en liquidacion** → advertir de que la reclamacion corresponde al Consorcio de Compensacion de Seguros por el procedimiento propio del Art. 11 TRLRCSCVM y **escalar**: fuera de alcance. Puede prepararse la reclamacion extrajudicial frente al causante identificado, si lo hay.
- Si el hecho ocurrio **en la via publica o en una instalacion de titularidad publica**, o la asistencia sanitaria se presto en la **sanidad publica** → **DETENER**: es responsabilidad patrimonial de la Administracion, que se tramita por el procedimiento administrativo y, en su caso, ante la jurisdiccion contencioso-administrativa. Advertir, explicar la via correcta y escalar. No crear documento.
- Si el dano se sufrio **en el trabajo o con ocasion del trabajo** → **DETENER**: jurisdiccion social, con regimen propio. Advertir y escalar. No crear documento.
- Si hay o puede haber **proceso penal** por los mismos hechos, o el cliente pide denuncia, querella o la reclamacion de la responsabilidad civil dentro del proceso penal → **DETENER**: fuera de alcance. Advertir y escalar a especialista en penal.
- Si hubo **fallecimiento del perjudicado o gran invalidez / gran lesionado** → **ESCALAR antes de cifrar nada**. Puede prepararse la reclamacion extrajudicial para interrumpir la prescripcion, dejando la cuantificacion abierta, pero la valoracion se deriva a especialista.
- Si V3 = 3 y es **negligencia sanitaria** → advertir de que sin informe medico pericial que acredite la desviacion de la *lex artis* y el nexo causal la reclamacion no es viable, indicar que el primer paso material es obtener la historia clinica completa, y **escalar**.
- Si el dano deriva de un **producto defectuoso** → advertir de que el regimen es el del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios, no verificado por esta skill, y escalar.

### Validacion de presupuestos (interno, antes del Punto 3)

- **TODAS LAS HOJAS:** confirmar que existe un **dano real y acreditable**, no una molestia ni un riesgo de dano. Si el cliente no puede describir un menoscabo concreto ni el documento que lo soporta, decirlo antes de redactar: no hay reclamacion.
- **TODAS LAS HOJAS:** confirmar que existe **soporte documental de cada partida** que se va a reclamar. Una partida sin soporte no se abarata: se elimina. Ver `references/estilo-redaccion-escritos.md`, apartado de prueba.
- **HOJA DEMANDA:** determinar el procedimiento por la cuantia (Art. 253 LEC). **Juicio verbal si la cuantia no excede de 15.000 euros (Art. 250.2 LEC); juicio ordinario si excede de esa cifra (Art. 249.2 LEC), y tambien si el interes economico resulta imposible de calcular.** Verificar el umbral en el Punto 2 antes de fijarlo.
- **HOJA DEMANDA:** verificar que se demanda a quien responde. Si se ejercita la accion directa, la aseguradora es demandada por derecho propio (Art. 76 LCS), no un tercero llamado al proceso.
- **HOJA DEMANDA y HOJA RECLAMACION, si V6 = 2:** antes de dar por inexistente el seguro, incluir en la reclamacion el requerimiento del ultimo inciso del Art. 76 LCS (el asegurado esta obligado a manifestar al perjudicado la existencia del contrato de seguro y su contenido). En circulacion, indicar ademas la consulta del fichero de vehiculos asegurados del Consorcio de Compensacion de Seguros (Art. 2.2 TRLRCSCVM).
- **HOJA OFERTA:** calcular el **nuevo plazo de prescripcion de un ano** que se inicio con la notificacion fehaciente de la oferta o respuesta motivada (Art. 7.1 TRLRCSCVM) y comunicarlo. Es el plazo que mas casos hace perder, porque el cliente cree que sigue interrumpido mientras negocia.
- **HOJA OFERTA:** comprobar si la comunicacion recibida **cumple los requisitos del Art. 7.3** (oferta) o del **Art. 7.4** (respuesta). Si no los cumple, no concurre la causa de exoneracion de intereses del Art. 9.a) TRLRCSCVM: hacerlo constar en el escrito.
- **HOJA RECLAMACION, en circulacion:** recordar que la reclamacion del Art. 7.1 TRLRCSCVM **no requiere estar cuantificada**. Si el proceso curativo no ha terminado, **no retrasar el envio para cuantificar**: se remite con la cuantificacion abierta y reserva expresa de la diferencia.
- **CULPA CONCURRENTE:** si de los hechos se desprende que el perjudicado contribuyo al dano (no llevaba casco o cinturon, cruzo indebidamente, abandono el proceso curativo), decirselo antes de fijar la cuantia. En circulacion, la reduccion alcanza a **todas** las partidas y **hasta un maximo del 75 %** (Art. 1.2 TRLRCSCVM). Excepcion del parrafo segundo del mismo precepto: en secuelas y lesiones temporales, la culpa de victimas no conductoras **menores de catorce anos** o privadas de capacidad de culpa civil **no suprime ni reduce** la indemnizacion.
- **MASC:** a diferencia de la demanda ejecutiva, la demanda de responsabilidad civil **SI** esta sujeta al requisito de procedibilidad del Art. 5 LO 1/2025: es un proceso declarativo del Libro II de la LEC y la responsabilidad civil por danos no figura entre las materias exceptuadas del Art. 5.2. Nunca omitir este requisito en la HOJA DEMANDA.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 1.902 y 1.903 del Código Civil (responsabilidad extracontractual con prescripción anual Art. 1968.2 CC); Art. 1.101 CC (responsabilidad contractual); Texto Refundido de la Ley sobre Responsabilidad Civil y Seguro en la Circulación de Vehículos a Motor (TRLRCSCVM, Art. 7 sobre oferta motivada preceptiva y baremo legal).
2. **Orientación Legal del Caso:**
Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la via, el plazo y la fuente aplicable.** Textos fijos por hoja, a los que se anade siempre el plazo calculado en el filtro de prescripcion:
   - CIRCULACION CON VEHICULO A MOTOR: "A su caso corresponde el regimen de responsabilidad civil por los danos causados con motivo de la circulacion de vehiculos a motor, conforme al articulo 1 del texto refundido de la Ley sobre responsabilidad civil y seguro en la circulacion de vehiculos a motor, aprobado por Real Decreto Legislativo 8/2004. Los danos personales se cuantifican obligatoriamente con el sistema de valoracion de su Anexo, en las cuantias del ejercicio {{ejercicio_baremo}}. La accion prescribe al ano (articulo 1968.2.º del Codigo Civil y articulo 7.1 del citado texto refundido). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2004-18911"
   - CIRCULACION CON VEHICULO PERSONAL LIGERO: "A su caso corresponde el regimen de responsabilidad civil y seguro del texto refundido de la Ley sobre responsabilidad civil y seguro en la circulacion de vehiculos a motor, aplicable a los vehiculos personales ligeros por remision del apartado 6 de la disposicion adicional primera de la Ley 5/2025, de 24 de julio, vigente desde el 2 de enero de 2026. La cobertura minima del seguro obligatorio es de 6.450.000 euros por siniestro en danos a las personas y 1.300.000 euros en danos a los bienes. La accion prescribe al ano. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2025-15424"
   - CAIDA O SUCESO EN ESTABLECIMIENTO: "A su caso corresponde la responsabilidad civil extracontractual del articulo 1902 del Codigo Civil, y en su caso la del articulo 1903 si el dano lo causo un dependiente en el ejercicio de sus funciones. Debera acreditarse la omision del deber de cuidado imputable al titular: la caida, por si sola, no genera responsabilidad. La accion prescribe al ano desde que usted conocio el dano (articulo 1968.2.º del Codigo Civil). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - VICIO CONSTRUCTIVO: "A su caso corresponde el regimen de responsabilidad de los agentes de la edificacion del articulo 17 de la Ley 38/1999, de Ordenacion de la Edificacion, con plazos de garantia de diez, tres o un ano desde la recepcion de la obra segun el tipo de defecto, y un plazo de prescripcion de dos anos desde que se producen los danos (articulo 18.1 de la misma Ley). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1999-21567"
   - NEGLIGENCIA PROFESIONAL: "A su caso corresponde la responsabilidad civil del profesional, contractual conforme a los articulos 1101 y 1103 del Codigo Civil si mediaba contrato, o extracontractual conforme al articulo 1902 si no lo habia. Debera acreditarse que la actuacion se aparto del estandar de diligencia exigible, no solo que el resultado fue desfavorable: la obligacion del profesional es de medios y no de resultado. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - DANO CONTRACTUAL: "A su caso corresponde la responsabilidad contractual de los articulos 1101 y 1103 del Codigo Civil, con un plazo de prescripcion de cinco anos desde que pudo exigirse el cumplimiento (articulo 1964.2 del Codigo Civil). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - En la HOJA RECLAMACION, anadir: "La reclamacion extrajudicial fehaciente interrumpe el plazo de prescripcion, que vuelve a contarse de cero desde su recepcion (articulo 1973 del Codigo Civil), y constituye la actividad negociadora previa que la ley exige antes de demandar (articulo 5 de la Ley Organica 1/2025)."
   - En la HOJA DEMANDA, anadir: "Para presentar esta demanda es requisito de procedibilidad haber intentado previamente una solucion negociada, cuyo documento acreditativo debe acompanarse (articulo 5 de la Ley Organica 1/2025 y articulo 264.4.º de la Ley de Enjuiciamiento Civil)."
   - En la HOJA DEMANDA, si V1 = 1, anadir ademas: "Ademas, en un accidente de circulacion la demanda no se admite a tramite si no se acompana la oferta o la respuesta motivada de la aseguradora o, en su defecto, la reclamacion previa que se le dirigio (articulo 7.8 del texto refundido citado, en relacion con el articulo 403 de la Ley de Enjuiciamiento Civil)."
   - En la HOJA OFERTA, si V1 = 1, anadir: "La aseguradora esta obligada a presentar oferta motivada de indemnizacion en el plazo de tres meses desde su reclamacion, o respuesta motivada si no puede ofertar (articulo 7.2 del texto refundido citado). La notificacion fehaciente de una u otra inicia un nuevo plazo de prescripcion de un ano, cuyo vencimiento en su caso es el {{fecha_vencimiento_nuevo_plazo}}."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla del sistema, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio.
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-demanda-responsabilidad-civil.md`).
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

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma parte se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las clausulas y decisiones de negociacion se explican y se confirman una a una. **La vista previa y la confirmacion agrupada de una parte se emiten en el turno SIGUIENTE a la respuesta del ultimo sub-apartado, nunca en el mismo turno en que aun se esta preguntando ese ultimo dato**: primero se pregunta y se recibe la respuesta, y solo despues, en el turno posterior, se muestra la vista previa conjunta y se pide la confirmacion.

**Validacion de sentido en esta skill.** Eres un LLM, no un formulario. Rechaza y pide aclaracion cuando: la fecha del alta sea anterior a la del hecho; el importe de una partida no guarde relacion con el dano descrito; el cliente describa como "secuela" algo que aun esta en tratamiento; o afirme un importe de lucro cesante sin ingresos previos acreditables. **Nunca escribas en el documento una cifra que el cliente no pueda soportar con un documento.**

### Secciones — HOJA RECLAMACION

1. **Datos del perjudicado** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por sus datos identificativos." Sub-apartados, uno por turno: a) nombre y apellidos o razon social; b) DNI, NIE o CIF segun corresponda; c) domicilio a efectos de notificaciones; d) telefono y correo electronico de contacto; e) si interviene letrado, su nombre y numero de colegiado. Al recibir la respuesta al ultimo, vista previa unica y una sola confirmacion antes del `Edit`.
2. **Contra quien se dirige la reclamacion** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos ahora a quien debe dirigirse la reclamacion." **Explica antes de preguntar**, apoyandote en `references/regimenes-de-responsabilidad-por-supuesto.md`, apartado 6: dirigirla solo al causante obliga a cobrar contra su patrimonio, con riesgo de insolvencia; dirigirla a la aseguradora por la accion directa del Art. 76 LCS aporta solvencia y, sobre todo, **inmunidad frente a las excepciones que el asegurador tenga contra su asegurado** (impago de prima, incumplimiento de deberes de la poliza), aunque el asegurador si puede oponer la culpa exclusiva del perjudicado; y dirigirla a **ambos** cubre el exceso sobre el limite de la poliza y evita quedar sin nada si se discute la vigencia del seguro. **Recomienda por defecto dirigirla a ambos** cuando V6 = 1, y explica por que. Pregunta despues la decision y confirmala.
3. **Datos del destinatario o destinatarios** *(dato objetivo — confirmacion agrupada por parte, una por cada destinatario)*. Anuncio fijo: "Pasamos a los datos de la parte a la que se dirige la reclamacion." Por cada destinatario, en turnos separados: a) nombre o razon social; b) documento de identidad o CIF; c) domicilio. Si es aseguradora, ademas: numero de poliza y referencia del siniestro, si se conocen. Confirmacion agrupada por cada destinatario. **Si V6 = 2**, explica que se incluira el requerimiento del ultimo inciso del Art. 76 LCS para que el causante manifieste la existencia y el contenido de su seguro, y en circulacion menciona el fichero de vehiculos asegurados del Consorcio (Art. 2.2 TRLRCSCVM).
4. **El hecho danoso** *(dato objetivo con validacion)*. Anuncio fijo: "Describimos ahora el hecho que le causo el dano." Sub-apartados, uno por turno: a) fecha y hora (ya conocida por el filtro de prescripcion: **no la vuelvas a preguntar**); b) lugar exacto; c) descripcion de lo ocurrido, en sus propias palabras; d) circunstancias relevantes para la imputacion (senalizacion, estado del pavimento, maniobra del vehiculo, identidad del conductor o del dependiente); e) si existe atestado, informe policial, parte de incidencia o denuncia, su referencia y organismo. **En circulacion, informa de que las Fuerzas y Cuerpos de Seguridad de trafico facilitan gratuitamente copia del atestado a peticion del perjudicado (Art. 7.1 TRLRCSCVM)** y ofrece dejarlo solicitado en el escrito. **Si el supuesto es una caida en establecimiento, advierte en este mismo turno y con caracter urgente de que las grabaciones de videovigilancia se sobreescriben en dias** y de que el escrito incluira el requerimiento de conservacion de las imagenes.
5. **Los danos sufridos** *(dato objetivo con validacion)*. Anuncio fijo: "Concretamos los danos que ha sufrido y como se acreditan." Sub-apartados, uno por turno, omitiendo los que no apliquen: a) dano personal: lesiones, centro asistencial, si el proceso curativo ha terminado y con que documentacion se acredita; b) dano material: bienes danados, importe de reparacion o reposicion y su justificante; c) lucro cesante: ingresos dejados de obtener y su soporte documental. **Por cada partida, pregunta expresamente con que documento se acredita.** Si no hay documento, dilo: la partida no se incluye, y explica que una partida sin soporte debilita todo el escrito.
6. **Cuantificacion de la indemnizacion** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a cuantificar la indemnizacion que se reclama." **Explica antes de pedir cifras**, siguiendo el guion del apartado 7 de `references/cuantificacion-danos-y-baremo.md`: que partidas existen y que cada una necesita su soporte; si el baremo es obligatorio (circulacion, Art. 1.4 TRLRCSCVM) u **orientativo** (todo lo demas, donde hacen falta informes periciales); que las cuantias son las del ejercicio verificado en el Punto 2, citando la resolucion concreta; que una partida sin soporte se elimina, no se abarata; y que la culpa concurrente reduce todas las partidas, hasta el 75 % en circulacion. Pide despues, en turnos separados y con confirmacion propia de cada uno: a) importe del dano personal, con la tabla o el informe en que se apoya; b) importe del dano material; c) importe del lucro cesante. **Si el proceso curativo no ha terminado**, explica que la reclamacion del Art. 7.1 TRLRCSCVM **no requiere estar cuantificada**, que no conviene retrasar el envio para cuantificar, y activa el bloque de reserva expresa de la diferencia.
7. **Requerimiento y propuesta** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos el requerimiento con que se cierra la reclamacion." **Explica antes de preguntar**: el escrito debe contener una propuesta concreta y un plazo de respuesta, porque de ello depende que sirva como actividad negociadora del Art. 5 LO 1/2025 y que el Art. 7.1 de la misma Ley reinicie el computo si no hay respuesta en treinta dias naturales. **En circulacion, explica ademas que la aseguradora esta obligada a responder con oferta motivada en tres meses (Art. 7.2 TRLRCSCVM) y que su silencio devenga los intereses de demora del Art. 9, en relacion con el Art. 20 LCS: el interes legal incrementado en el 50 %, con un minimo del 20 % anual pasados dos anos del siniestro.** Pide despues: a) plazo de respuesta que se concede (**propon 30 dias naturales por defecto**, coherente con el Art. 7.1 LO 1/2025, y pregunta si desea otro); b) cuenta bancaria para el pago, si desea indicarla.
8. **Medio de envio, documentos y cierre** *(dato objetivo)*. Anuncio fijo: "Cerramos con la documentacion que se acompana y el medio de envio." Sub-apartados: a) relacion numerada de los documentos que se adjuntan; b) medio de envio. **Sobre el medio de envio, advierte siempre y no aceptes un medio no fehaciente sin decirlo:** un correo electronico sin acuse o una llamada no acreditan la interrupcion de la prescripcion; hace falta burofax con certificacion de contenido y acuse de recibo, o notificacion notarial, y conservar el justificante; c) lugar de firma y fecha (la del dia, salvo indicacion en contrario).

### Secciones — HOJA OFERTA

1. **Datos del perjudicado** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por sus datos identificativos." Igual estructura que en la HOJA RECLAMACION.
2. **Datos de la aseguradora y del expediente** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a los datos de la aseguradora y del expediente del siniestro." Sub-apartados, uno por turno: a) denominacion y CIF de la aseguradora; b) domicilio al que se dirige el escrito; c) numero de poliza; d) referencia del siniestro o del expediente.
3. **La comunicacion recibida** *(dato objetivo con validacion)*. Anuncio fijo: "Examinamos ahora la comunicacion que ha recibido de la aseguradora." Sub-apartados, uno por turno: a) si usted remitio reclamacion previa a la aseguradora y, en tal caso, su fecha y el medio empleado — **no des por supuesto que la hubo: es frecuente que sea la aseguradora la que abra el expediente a partir del parte de su asegurado o del atestado y oferte sin reclamacion del perjudicado.** Si no la hubo, pregunta a partir de que se abrio el expediente y como tuvo usted noticia de el, activa en el asset el bloque de apertura sin reclamacion previa en lugar del de reclamacion previa, y hazle saber que el plazo de tres meses del Art. 7.2 TRLRCSCVM se cuenta desde la reclamacion del perjudicado, de modo que en su caso aun no ha empezado a correr; b) fecha en que recibio la comunicacion de la aseguradora (ya conocida por el filtro de prescripcion: **no la vuelvas a preguntar**); c) si se trata de una oferta motivada (propone una indemnizacion) o de una respuesta motivada (explica por que no la propone) — **explica la diferencia antes de preguntarla**, porque el cliente rara vez la conoce; d) importe ofertado, si lo hay; e) que documentacion e informes le entregaron con ella. **Con la respuesta a e), comprueba tu mismo si se cumplen los requisitos del Art. 7.3 (oferta) o del Art. 7.4 (respuesta) TRLRCSCVM** e informa del resultado: si falta la entrega desglosada de los documentos, incluido el informe medico pericial definitivo, ese incumplimiento impide a la aseguradora aportarlos despues en juicio (Art. 7.3.c) y **elimina la exoneracion de intereses del Art. 9.a)**.
4. **Computo del nuevo plazo** *(dato objetivo con validacion bloqueante)*. Anuncio fijo: "Verificamos el plazo del que dispone desde esa comunicacion." Con la fecha de la letra b) de la seccion anterior, calcula tu mismo el vencimiento del nuevo plazo de un ano del Art. 7.1 TRLRCSCVM e informalo con la fecha exacta. **Si ese plazo ya esta agotado, detente**: aplica el filtro de prescripcion del Punto 1 con su regla de detencion. **Si quedan menos de 60 dias, advierte con prioridad** y explica que este escrito interrumpe de nuevo la prescripcion (Art. 1973 CC) y que la solicitud de informes periciales complementarios del Art. 7.5 mantiene el plazo interrumpido.
5. **Posicion frente a la oferta** *(negociacion — explicar antes de decidir; la decision central de esta hoja)*. Anuncio fijo: "Determinamos la posicion que va a adoptar frente a la oferta recibida." **Explica antes de preguntar, sin omitir ninguno de estos cuatro puntos:**
   - **Aceptar no obliga a renunciar a nada.** El Art. 7.3.d) TRLRCSCVM impide condicionar el pago a la renuncia del perjudicado al ejercicio de futuras acciones. Si el documento que le proponen firmar contiene un finiquito o una renuncia total, **no debe firmarlo sin revision**.
   - **Se puede aceptar a cuenta.** Cabe cobrar ya el importe ofertado como pago a cuenta, sin conformidad con el total y sin renunciar a reclamar la diferencia. Es la opcion conservadora cuando la valoracion se discute pero el importe ofrecido no se cuestiona como minimo.
   - **La oferta en plazo y con el contenido del Art. 7.3 exonera de intereses, pero solo respecto de la cantidad ofertada y satisfecha o consignada** (Art. 9.a) TRLRCSCVM). La diferencia entre lo ofertado y lo que finalmente se reconozca sigue devengando el interes del Art. 20 LCS.
   - **Si no hubo oferta en tres meses por causa imputable a la aseguradora, se devengan los intereses de demora del Art. 9** (Art. 7.2 TRLRCSCVM), y lo mismo si, aceptada la oferta, no se paga en cinco dias ni se consigna.
   Pregunta despues: "Su posicion frente a la oferta es:
   1. Aceptarla en su integridad
   2. Aceptar el importe a cuenta, sin conformidad con el total y sin renunciar a la diferencia
   3. Rechazarla y mantener su reclamacion"
   Confirma la decision antes del `Edit` y activa el bloque correspondiente del asset.
6. **Motivos de disconformidad** *(negociacion — solo si la posicion es 2 o 3)*. Anuncio fijo: "Concretamos los motivos de disconformidad, partida por partida." **Se discute partida por partida, nunca en bloque.** Sub-apartados, uno por turno, omitiendo los que no apliquen: a) partidas del baremo cuya cuantia no se corresponde con las tablas del ejercicio verificado; b) dias de perjuicio temporal o puntos de secuela no reconocidos, con la documentacion medica que los acredita; c) partidas de dano material o lucro cesante omitidas en la oferta, con su soporte; d) culpa concurrente imputada por la aseguradora que usted no acepta, y las razones. **En la letra d), si el lesionado es menor de catorce anos o carece de capacidad de culpa civil, informale de que el parrafo segundo del Art. 1.2 TRLRCSCVM impide que su culpa reduzca la indemnizacion por secuelas y lesiones temporales**, y activa el bloque correspondiente. **En la letra a), comprueba tu mismo si la aseguradora aplico las cuantias del ejercicio del accidente o las de un ejercicio anterior**: es una de las discrepancias mas frecuentes y la deteccion es automatica con el dato del Punto 2.
7. **Solicitudes** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos las solicitudes que se dirigen a la aseguradora." **Explica cada opcion antes de preguntar si la desea**, y preguntalas en turnos separados: a) **informe pericial complementario del Art. 7.5**: puede pedirse al Instituto de Medicina Legal y Ciencias Forenses **con cargo a la aseguradora aun sin su acuerdo**, obliga a esta a una nueva oferta motivada en un mes desde su entrega y mantiene interrumpido el plazo de prescripcion; el lesionado debe ser reconocido en tres meses y el informe emitirse en uno (Art. 7.6); b) **pago a cuenta** de los perjuicios ya consolidados, con el deber de la aseguradora de informar de la situacion del siniestro cada dos meses (Art. 7.4.a).1.º); c) **entrega de la documentacion no aportada** (Arts. 7.3.c) y 7.4.b)); d) **acudir a un medio adecuado de solucion de controversias** con profesional especializado (Art. 14 TRLRCSCVM); e) **anuncio de la via judicial** con un plazo de respuesta, si el cliente lo desea.
8. **Medio de envio, documentos y cierre** *(dato objetivo)*. Anuncio fijo: "Cerramos con la documentacion que se acompana y el medio de envio." Igual estructura y misma advertencia sobre la fehaciencia que en la HOJA RECLAMACION.

### Secciones — HOJA DEMANDA

1. **Requisito de procedibilidad** *(dato objetivo con validacion bloqueante — va PRIMERO)*. Anuncio fijo: "Comenzamos verificando que se cumple el requisito previo para presentar la demanda." Sub-apartados, uno por turno: a) fecha, medio y destinatario de la actividad negociadora previa, y el justificante de envio y recepcion de que dispone; b) resultado (sin respuesta, respuesta negativa, acuerdo parcial). **Si no hay ninguna actividad negociadora acreditada, aplica el enrutamiento del Punto 1: no continues con la demanda.** Si el cliente desconoce el domicilio del demandado o el medio por el que requerirle, informa de la declaracion responsable que admite el Art. 264.4.º LEC y continua.
2. **Parte demandante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la parte demandante." Sub-apartados, uno por turno: a) nombre y apellidos o razon social; b) DNI, NIE o CIF; c) domicilio; d) nombre del procurador y del letrado. **Abogado y procurador son preceptivos en el juicio ordinario; en el juicio verbal no lo son si la cuantia no excede de 2.000 euros (Arts. 23 y 31 LEC)**: si la cuantia esta por debajo de esa cifra, preguntale si va a comparecer por si mismo y adapta el encabezamiento.
3. **Parte demandada** *(negociacion para la eleccion + dato objetivo para los datos)*. Anuncio fijo: "Determinamos ahora contra quien se dirige la demanda." **Misma explicacion que en la seccion 2 de la HOJA RECLAMACION**, con el enfasis puesto en que la accion directa del Art. 76 LCS convierte a la aseguradora en demandada por derecho propio y es inmune a las excepciones que el asegurador tenga contra su asegurado. **Recomienda por defecto demandar a ambos solidariamente** cuando V6 = 1. Tras confirmar la eleccion, pide los datos de cada demandado en turnos separados, con confirmacion agrupada por cada uno.
4. **El hecho danoso** *(dato objetivo con validacion)*. Anuncio fijo: "Describimos el hecho que fundamenta la demanda." Igual estructura que en la HOJA RECLAMACION, seccion 4, anadiendo el numero de documento con que se acredita cada elemento.
5. **La imputacion de la responsabilidad** *(dato objetivo con explicacion)*. Anuncio fijo: "Concretamos el titulo por el que responde la parte demandada." Redacta el fundamento con el regimen que corresponda a la rama, tomandolo de `references/regimenes-de-responsabilidad-por-supuesto.md`, y **explicale al cliente que tendra que probar**: en circulacion, la responsabilidad es por el riesgo creado y es el demandado quien debe probar la culpa exclusiva de la victima o la fuerza mayor; fuera de ella, es el demandante quien debe probar la culpa o negligencia, y en negligencia profesional la desviacion de la *lex artis*. Pide el dato concreto que falte segun la rama: la omision del deber de cuidado, la obligacion contractual incumplida, el apartado del Art. 17.1 LOE en que encaja el defecto y la fecha de recepcion de la obra, o la desviacion del estandar profesional.
6. **Los danos y perjuicios** *(dato objetivo con validacion)*. Anuncio fijo: "Concretamos los danos y su acreditacion." Igual estructura que en la HOJA RECLAMACION, seccion 5, con un nivel de detalle mayor en el dano personal: dias de perjuicio temporal desglosados en muy grave, grave, moderado y basico; intervenciones quirurgicas; relacion de secuelas y puntos. **Numera cada documento y relacionalo en el hecho correspondiente.**
7. **Nexo causal y prueba pericial** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Valoramos como se acreditara la relacion entre el hecho y el dano." **Explica antes de preguntar** que el nexo causal es el punto en que fracasan la mayoria de las reclamaciones, y que en vicio constructivo y en negligencia profesional **sin dictamen pericial no hay demanda viable**. Pregunta si dispone ya de informe pericial, de que clase y de quien; si no lo tiene, adviertele de que debe obtenerlo antes de presentar y de las consecuencias de no hacerlo. Pregunta despues si desea anunciar en la demanda la proposicion de prueba pericial y testifical.
8. **Cuantificacion de la indemnizacion** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a cuantificar la indemnizacion que se reclama." Igual estructura y guion que en la HOJA RECLAMACION, seccion 6, con dos anadidos: a) **el detalle partida por partida con indicacion de la tabla aplicada a cada concepto** entra en el cuerpo del escrito, no en un anexo; b) si hay **culpa concurrente que el cliente reconoce**, explica la reduccion del Art. 1.2 TRLRCSCVM (hasta el 75 % en circulacion) o la moderacion judicial del Art. 1103 CC fuera de ella, y aplicala expresamente en el desglose. **No infles la cuantia**: encarece las costas si la estimacion es parcial y da a la contraparte el argumento del rechazo global.
9. **No prescripcion de la accion** *(dato objetivo con validacion bloqueante)*. Anuncio fijo: "Cerramos el apartado de hechos con el plazo de la accion." Con las fechas ya conocidas del filtro de prescripcion, redacta el hecho y el fundamento correspondientes: plazo aplicable, precepto, *dies a quo*, cada acto interruptivo con su fecha y su medio, y el documento que lo acredita. **En circulacion, si hubo oferta o respuesta motivada, computa desde su notificacion el nuevo plazo de un ano del Art. 7.1 TRLRCSCVM.** No omitas nunca este fundamento: es la primera excepcion que opondra la contraparte.
10. **Intereses** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos los intereses que se reclaman." **Explica antes de preguntar**: si se demanda a la aseguradora, la mora del Art. 20 LCS **se impone de oficio** por el organo judicial y consiste en el interes legal del dinero incrementado en el 50 %, computado desde la fecha del siniestro, con un minimo del 20 % anual transcurridos dos anos; en circulacion se aplica con las singularidades del Art. 9 TRLRCSCVM, y **no procede la exoneracion de su letra a) si la oferta no se presento en plazo o no reunia el contenido del Art. 7.3**. Pregunta si se reclaman ademas los intereses procesales del Art. 576 LEC. Recuerdale que el interes legal del ejercicio se fija en la Ley de Presupuestos y debe consultarse al liquidar.
11. **Procedimiento, cuantia y juzgado** *(dato objetivo con validacion)*. Anuncio fijo: "Determinamos el procedimiento y el juzgado competente." Con la cuantia ya fijada, calcula tu mismo el procedimiento: **juicio verbal si no excede de 15.000 euros (Art. 250.2 LEC), juicio ordinario si excede (Art. 249.2 LEC)**, e informalo. Pregunta despues el partido judicial y confirma el fuero: en responsabilidad extracontractual cabe el del lugar del hecho danoso; si se demanda a la aseguradora, tambien el de su domicilio o el del domicilio del asegurado. No admitas sumision a un fuero que no corresponda.
12. **Documentos** *(dato objetivo)*. Anuncio fijo: "Cerramos con la relacion de documentos que se acompanan." Pide la relacion completa y numerala correlativamente con los hechos. **Verifica tu mismo que estan incluidos los tres documentos sin los que la demanda no se admite:** el poder, el documento acreditativo de la actividad negociadora previa o la declaracion responsable (Art. 264.4.º LEC) y, en circulacion, el que acredite la oferta o la respuesta motivada o, en su defecto, la reclamacion previa al asegurador (Art. 7.8 TRLRCSCVM).
13. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito." Lugar de firma; fecha del dia salvo indicacion en contrario.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: HECHOS numerados con una idea por apartado y en el orden natural de la responsabilidad civil (hecho danoso, imputacion, dano y cuantificacion, nexo causal, reclamacion previa); documentos relacionados y numerados; desglose siempre por partidas; voz activa, sin latinismos; y **nunca describir el dano con adjetivos en lugar de con datos**.

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

1. **El filtro de prescripcion es lo primero y es bloqueante.** Si el plazo esta agotado, no se redacta ningun documento: se explica el computo y se ofrece escalacion. Nunca se da falsa esperanza redactando un escrito que la contraparte desactivara con una excepcion de prescripcion.
2. **Nunca se afirma que un plazo esta vivo sin haberlo computado con fechas concretas**, ni se comunica una fecha limite sin decir de que dato depende.
3. **Un medio de comunicacion no fehaciente no interrumpe la prescripcion.** Un correo electronico sin acuse, una llamada o un mensaje de mensajeria no se cuentan nunca como acto interruptivo: hay que decirselo al cliente.
4. **En circulacion, la reclamacion previa al asegurador no es opcional.** Sin ella —o sin la oferta o respuesta motivada— la demanda no se admite a tramite (Art. 7.8 TRLRCSCVM y Art. 403 LEC). Nunca crear la demanda sin verificarlo.
5. **La demanda de responsabilidad civil esta sujeta al requisito de procedibilidad del Art. 5 LO 1/2025.** A diferencia de la demanda ejecutiva, aqui el MASC SI se exige: es un proceso declarativo del Libro II de la LEC y la materia no esta exceptuada. Nunca omitir el documento del Art. 264.4.º LEC.
6. **Verificar el baremo del ejercicio en curso en cada lanzamiento.** PROHIBIDO cifrar con el Anexo del texto consolidado del BOE (que no incorpora las actualizaciones anuales por IPC) y PROHIBIDO calcular una cuantia aplicando un porcentaje a un importe recordado: se abre la tabla del ejercicio y se lee el importe. Si no se pudo verificar, no se cifran los danos personales.
7. **La tabla aplicable es la del ano del accidente, no la del ano de la reclamacion**, con la regla del Art. 49.2 TRLRCSCVM para las tablas de lucro cesante y de ayuda de tercera persona.
8. **Fuera de la circulacion el baremo es solo orientativo.** Nunca escribir que "procede aplicar el baremo": la formula correcta es que se toma como referencia orientativa, sin aplicacion directa, y la cifra debe apoyarse en informe pericial.
9. **Los danos en los bienes no se cuantifican nunca con el baremo**, ni en circulacion: se rigen por los Arts. 1902 y ss. CC (Art. 1.1, parrafo tercero, TRLRCSCVM).
10. **Una partida sin soporte documental no se incluye.** No se abarata: se elimina. Nunca escribir en el documento una cifra que el cliente no pueda acreditar.
11. **El seguro obligatorio de vehiculos personales ligeros no existia antes del 02/01/2026** y no alcanza a todo patinete: solo a los que reunen los tres requisitos acumulativos del apartado 1 de la disposicion adicional primera de la Ley 5/2025. Nunca darlo por supuesto: comprobar la fecha del hecho y los requisitos.
12. **La bicicleta electrica de pedaleo asistido de hasta 250 W no es vehiculo personal ligero ni vehiculo a motor** (apartado 3.c) de la citada disposicion adicional y Art. 1 bis TRLRCSCVM): se rige por el Art. 1902 CC.
13. **Aceptar una oferta no puede condicionarse a renunciar a futuras acciones** (Art. 7.3.d) TRLRCSCVM). Si al cliente le proponen firmar un finiquito o una renuncia total, advertirle de que no lo firme sin revision.
14. **Advertir siempre de la culpa concurrente cuando los hechos la sugieran**, antes de fijar la cuantia. En circulacion reduce todas las partidas hasta el 75 % (Art. 1.2 TRLRCSCVM), con la excepcion del parrafo segundo para menores de catorce anos y personas sin capacidad de culpa civil.
15. **Sin dictamen pericial no hay reclamacion viable en vicio constructivo ni en negligencia profesional.** No redactar dando por acreditado un nexo causal tecnico que solo un perito puede establecer.
16. **En caida en establecimiento, advertir de inmediato de la conservacion de las grabaciones de videovigilancia.** Se sobreescriben en dias y su perdida suele ser irreversible para el caso.
17. Nunca inventar datos, cuantias, fechas, numeros de poliza, referencias de siniestro ni jurisprudencia. Los campos no proporcionados quedan como `{{dato}}`.
18. Ante la duda sobre la naturaleza contractual o extracontractual del vinculo, **computar el plazo mas corto** y advertir de la conveniencia de interrumpir la prescripcion de inmediato. Nunca asegurar al cliente que dispone de cinco anos porque "podria ser contractual".

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar para la responsabilidad civil derivada de delito ni para la pieza de responsabilidad civil dentro de un proceso penal (Arts. 109 y ss. del Codigo Penal): orden jurisdiccional penal, fuera de alcance. Nunca redactar denuncia ni querella.
- No usar para la responsabilidad patrimonial de la Administracion, incluidos los danos en la via publica de titularidad municipal y la asistencia prestada en la sanidad publica: la via es administrativa y, en su caso, contencioso-administrativa.
- No usar para danos laborales, accidentes de trabajo o enfermedades profesionales: jurisdiccion social, con recargo de prestaciones y regimen propio.
- No usar para reclamar al Consorcio de Compensacion de Seguros cuando el vehiculo causante no esta asegurado, no esta identificado o su aseguradora esta en liquidacion (Art. 11 TRLRCSCVM): procedimiento propio, fuera de alcance.
- No usar para cuantificar un fallecimiento ni una gran invalidez: escalar antes de cifrar. Cabe, eso si, preparar la reclamacion extrajudicial para interrumpir la prescripcion, con la cuantificacion abierta.
- No usar para danos causados por producto defectuoso: regimen propio del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios, no verificado por esta skill.
- No usar para accidentes ocurridos en el extranjero ni con vehiculos con estacionamiento habitual fuera de Espana.
- No usar para redactar la contestacion a la demanda ni la oposicion del demandado: posicion contraria, fuera de alcance.
- No usar para ejecutar una sentencia de condena ya firme: derivar a `ejecucion-titulos`.
- No usar para reclamar una deuda contractual liquida sin dano indemnizable asociado: derivar a `reclamacion-cantidad` (monitorio, verbal u ordinario segun cuantia).
- No usar si el usuario pide opinion juridica sobre la viabilidad o la estrategia del asunto: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
