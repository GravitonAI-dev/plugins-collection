---
name: minuta-jura-cuentas
description: >
  Genera los documentos de facturación y reclamación de honorarios profesionales: minuta detallada de
  honorarios, requerimiento previo de pago al cliente, solicitud de jura de cuentas del artículo 35 de
  la **Ley 1/2000 de Enjuiciamiento Civil**, que regula el procedimiento de jura de cuentas para cobrar honorarios de un asunto judicial, y escrito de alegaciones frente a la impugnación de la minuta
  por indebida o por excesiva. Aplica la Ley 1/2000 de Enjuiciamiento Civil, el **Estatuto General de la
  Abogacía Española aprobado por Real Decreto 135/2021** y la **Ley 15/2007 de Defensa de la Competencia**
  en cuanto al uso de criterios orientativos de honorarios, en sus versiones consolidadas vigentes
  verificadas en el BOE, y contrasta la normativa deontológica del colegio de adscripción y sus
  criterios orientativos. Su primera función es de control: comprueba si existe hoja de encargo
  firmada y qué dice, si el honorario se devengó en un asunto judicial —único supuesto en que cabe la
  jura de cuentas— y si el cliente es consumidor. Metodología: clasificación del documento y de la vía
  mediante formulario interactivo, plan de acción con el desglose de actuaciones, creación del
  documento base en el workspace y edición incremental apartado a apartado. NO usar para pactar los
  honorarios, que corresponde a la skill `hoja-encargo`.
when_to_use: |
  - El despacho necesita emitir la minuta detallada de honorarios de un asunto.
  - El cliente no ha pagado y el despacho quiere requerirle de pago antes de acudir a la vía judicial.
  - El despacho quiere instar la jura de cuentas del artículo 35 de la Ley de Enjuiciamiento Civil.
  - El cliente ha impugnado la minuta por indebida o por excesiva y hay que contestar.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - tipo_documento: minuta de honorarios / requerimiento previo de pago / solicitud de jura de cuentas / alegaciones frente a impugnación
  - existe_hoja_encargo: sí, con su fecha y contenido económico / no
  - ambito_asunto: judicial, con identificación del órgano y del procedimiento / extrajudicial
  - naturaleza_cliente: persona física consumidora / empresa, autónomo o profesional
  - datos_despacho: denominación, NIF, domicilio, colegio de adscripción y número de colegiado
  - datos_cliente: nombre o razón social, NIF o CIF y domicilio
  - datos_asunto: referencia del expediente, órgano judicial, número de autos y objeto
  - actuaciones: relación fechada de las actuaciones profesionales realizadas
  - importes: base de honorarios, impuestos, retenciones, suplidos, provisiones recibidas y cantidades abonadas
outputs:
  - minuta_honorarios: minuta detallada en markdown, DRAFT, con desglose de actuaciones e importes
  - solicitud_jura_cuentas: escrito de reclamación del artículo 35 en markdown, DRAFT
references:
  - references/fuentes-y-normativa-colegial.md
  - references/jura-de-cuentas-y-procedimiento.md
  - references/contenido-de-la-minuta-y-secreto-profesional.md
  - references/vias-alternativas-de-reclamacion.md
assets:
  - assets/template-alegaciones-impugnacion-honorarios.md
  - assets/template-minuta-honorarios.md
  - assets/template-requerimiento-previo-pago-honorarios.md
  - assets/template-solicitud-jura-de-cuentas.md
---

# Generar la Minuta y la Reclamación de Honorarios

> DRAFT — para revisión por el profesional responsable antes de su firma, entrega o presentación. Debe adaptarse a la normativa deontológica del colegio de adscripción.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de documento):** `minuta` | `requerimiento_previo` | `jura_de_cuentas` | `alegaciones_impugnacion`.
- **V2 (Existencia de hoja de encargo):** `con_encargo_escrito` | `sin_encargo_escrito`. *(Determina la solidez de la posición y la estrategia de la reclamación.)*
- **V3 (Ámbito del asunto):** `judicial` | `extrajudicial`. *(La jura de cuentas solo cabe respecto de honorarios devengados en un asunto judicial.)*
- **V4 (Naturaleza del cliente):** `consumidor` | `empresa_profesional`. *(Determina el control de transparencia y de abusividad aplicable.)*
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

### 1.1 Escucha Activa Previa
Si el usuario ya ha identificado el documento, la existencia de encargo, el ámbito del asunto y la naturaleza del cliente, registra los vectores en silencio y pasa a la **Fase 2**. En todo caso, **resuelve primero el control de viabilidad del punto 1.3**.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "tipo_documento",
      "rationale": "Resolver V1: la minuta precede a toda reclamación, y el requerimiento previo condiciona los intereses y la posición procesal.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "minuta", "label": "Minuta detallada de honorarios para su entrega al cliente"},
        {"id": "requerimiento_previo", "label": "Requerimiento previo de pago al cliente que no ha abonado la minuta"},
        {"id": "jura_de_cuentas", "label": "Solicitud de jura de cuentas ante el juzgado que conoció del asunto"},
        {"id": "alegaciones_impugnacion", "label": "Alegaciones frente a la impugnación de la minuta por el cliente"}
      ]
    },
    {
      "id": "existe_hoja_encargo",
      "rationale": "Resolver V2: la existencia y el contenido de la hoja de encargo determina la solidez de la reclamación y la vía más conveniente.",
      "question": "¿Existe hoja de encargo firmada por el cliente con los honorarios pactados?",
      "options": [
        {"id": "con_encargo_escrito", "label": "Sí, con los honorarios pactados por escrito"},
        {"id": "encargo_sin_honorarios", "label": "Existe encargo escrito, pero sin pacto claro de honorarios"},
        {"id": "sin_encargo_escrito", "label": "No hay documento escrito: el encargo fue verbal"}
      ]
    },
    {
      "id": "ambito_asunto",
      "rationale": "Resolver V3: la jura de cuentas solo procede respecto de honorarios devengados en un asunto judicial y ante el órgano que conoció de él.",
      "question": "¿En qué asunto se devengaron los honorarios?",
      "options": [
        {"id": "judicial", "label": "En un procedimiento judicial en el que se dirigió la defensa del cliente"},
        {"id": "extrajudicial", "label": "En asesoramiento, negociación o redacción de documentos, sin procedimiento judicial"},
        {"id": "mixto", "label": "En ambos: parte extrajudicial y parte judicial"}
      ]
    },
    {
      "id": "naturaleza_cliente",
      "rationale": "Resolver V4: si el cliente es consumidor, opera el control de transparencia y de abusividad de las cláusulas económicas.",
      "question": "¿Quién es el cliente deudor?",
      "options": [
        {"id": "consumidor", "label": "Persona física que contrató al margen de una actividad empresarial o profesional"},
        {"id": "empresa_profesional", "label": "Empresa, entidad, autónomo o profesional"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `tipo_documento`
- `V2` — `existe_hoja_encargo`
- `V3` — `ambito_asunto`
- `V4` — `naturaleza_cliente`

### 1.3 Control de Viabilidad y Enrutamiento (PRIMERA ACCIÓN OBLIGATORIA)

**Comprobación 1 — Comprueba la hoja de encargo.** Antes de redactar cualquier reclamación, pide al usuario que aporte o describa la hoja de encargo y su cláusula económica.
- **Si `[V2 = con_encargo_escrito]`:** el honorario reclamable es el pactado. La minuta debe ajustarse a él; una minuta que se aparta del pacto es el mejor argumento del cliente.
- **Si `[V2 = encargo_sin_honorarios]` o `[V2 = sin_encargo_escrito]`:** advierte con claridad de que la posición del despacho es **notablemente más débil**, de que la determinación del honorario se hará por criterios objetivos —usos profesionales, criterios orientativos del colegio a los efectos legalmente admitidos, cuantía y complejidad del asunto—, y de que conviene reunir toda la prueba del encargo y de las actuaciones realizadas antes de reclamar. No oculte esta advertencia.

**Comprobación 2 — Comprueba la vía.**
- La **jura de cuentas del artículo 35** procede respecto de los honorarios devengados **en un asunto judicial** y se sustancia ante el órgano que conoció de él. **No cabe** para honorarios de asesoramiento extrajudicial.
- **Si `[V3 = extrajudicial]` y `[V1 = jura_de_cuentas]` → Detén la redacción.** Explícalo y ofrece las vías alternativas: requerimiento previo, proceso monitorio o juicio declarativo según la cuantía. Ofrece derivar a la skill `derecho-civil:reclamacion-cantidad` para la elección de la vía civil.
- **Si `[V3 = mixto]`:** advierte de que solo la parte devengada en el asunto judicial puede reclamarse por el artículo 35, y de que conviene separar ambos conceptos en la minuta desde el principio.

**Comprobación 3 — Comprueba la naturaleza del cliente.**
- **Si `[V4 = consumidor]`:** advierte de que en el procedimiento del artículo 35 puede operar el **control de la cláusula de honorarios** desde la perspectiva de la transparencia y de la abusividad, y de que una cláusula opaca puede resultar inoponible. **Verifica con `web_search` el estado actual de esta cuestión** antes de afirmar nada sobre su alcance.

**Comprobación 4 — Comprueba la prescripción.** Pide la fecha de terminación de la actuación y verifica el plazo de prescripción aplicable a la reclamación de honorarios profesionales en la normativa civil vigente. **Verifícalo con `web_search`**: el plazo general de las acciones personales fue modificado y existe régimen transitorio. Comunica la fecha límite.

**Comprobación 5 — Enrutamiento:**
* **Si `[V1 = minuta]` → Plantilla: `assets/template-minuta-honorarios.md`.**
* **Si `[V1 = requerimiento_previo]` → Plantilla: `assets/template-requerimiento-previo-pago-honorarios.md`.** Explica que el requerimiento fehaciente interrumpe la prescripción, acredita la mora y suele resolver el asunto sin litigio, y que además prepara la posición procesal.
* **Si `[V1 = jura_de_cuentas]` → Plantilla: `assets/template-solicitud-jura-de-cuentas.md`.**
* **Si `[V1 = alegaciones_impugnacion]` → Plantilla: `assets/template-alegaciones-impugnacion-honorarios.md`.** Pregunta si la impugnación es por honorarios **indebidos** o por **excesivos**, porque el trámite y la estrategia son distintos.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión consolidada vigente de la Ley 1/2000 de Enjuiciamiento Civil en el BOE, y en particular la redacción de los artículos 34 y 35 y sus plazos.
3. **Identifica el colegio de adscripción** y verifica si tiene publicados criterios orientativos de honorarios y en qué versión, recordando que solo pueden emplearse a los efectos legalmente admitidos, entre ellos la jura de cuentas.
4. Verifica los tipos vigentes de impuesto sobre el valor añadido y de retención a cuenta del IRPF, y el interés legal del dinero del ejercicio.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Viabilidad y vía procedente**, con la advertencia sobre la existencia o ausencia de hoja de encargo.
2. **Cómputo de la prescripción** con la fecha límite.
3. **Estructura del documento** y desglose económico que se va a construir.
4. **Advertencia sobre el secreto profesional:** la minuta necesita detalle para justificar el honorario, pero no puede revelar la estrategia del asunto, las confidencias del cliente ni datos de terceros. Explica que se describirán **actuaciones**, no contenidos.
5. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
6. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:** accede al adjunto y verifica que contenga la identificación de las partes, la referencia del asunto, el detalle de las actuaciones y el desglose económico con impuestos separados. Advierte si la minuta es global y sin desglose —el defecto más común y el que más impugnaciones provoca— o si revela información amparada por el secreto profesional.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura (`create_file`):** vuelca íntegramente la plantilla acordada en el workspace con nombre en `snake_case.md`, aplicando **Zero-Omission** y dejando los datos pendientes como marcador con su nombre propio de plantilla.
2. **Validación de Integridad:**
   - La comprobación de integridad y contenido del archivo creado se realiza consultando prioritariamente la sección `# WORKSPACE ACTIVE DOCUMENTS` del prompt, donde el sistema mantiene siempre la última versión de todos los documentos. Solo se debe invocar `read_file` si es estrictamente necesario y en algún caso extremo (ej. el archivo no aparece en dicha sección o contenido truncado).

3. **Confirmación y encadenamiento:** informa de la ruta absoluta y, en la misma respuesta, abre la primera sección de la Fase 4 con su anuncio y su primera solicitud de datos.

---

## FASE 4 — EDICIÓN INCREMENTAL APARTADO A APARTADO

### Protocolo Obligatorio de Edición
```
[slot_filling_request (grupos) / Chat (relación de actuaciones)] --> [Vista previa en texto plano]
      --> [«¿Confirmamos esta sección?»] --> [edit_file en el editor]
```

- **Búsqueda prioritaria, Cero Redundancia y Guardado de Nuevos Clientes (`search_clients` / `get_client` / `save_client` — REG-CLI-01, REG-CLI-02 y REG-CLI-03):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** conforme a `REG-CLI-01`. Si los datos ya constan en el sistema, **queda TERMINANTEMENTE PROHIBIDO volver a pedirlos** (`REG-CLI-02`) y se omite `slot_filling_request`. Si se especifican datos de una persona nueva (por formulario o chat), **DEBES invocar INMEDIATAMENTE `restricted_human_in_the_loop_request`** para preguntar al usuario si desea guardarla como nuevo cliente (`REG-CLI-03`), quedando **TERMINANTEMENTE PROHIBIDO emitir la vista previa de la cláusula o decir 'le preguntaré después' antes de resolver el guardado**. En caso afirmativo, invoca `save_client` con los campos disponibles. Solo tras resolver el guardado (o si el usuario lo rechaza), continúa con el flujo normal de vista previa y confirmación de la cláusula.

- **Grupos de datos estructurados no de cliente (MANDATORIO con `slot_filling_request`):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
- **Campos omitidos o negativa expresa (No insistencia):** Si el usuario pide explícitamente no aportar determinados campos de información, pásalos por alto de inmediato sin insistir en pedirlos ni presionar. Rellena la plantilla con los datos disponibles, conserva los no aportados como marcadores pendientes ({{NOMBRE_CAMPO}} o {{DATO_FALTANTE}}) e indica en la confirmación cuáles faltan antes de continuar con la siguiente sección.
- **Todo importe con su cálculo a la vista** antes de escribirlo.
- **Anuncio de sección visible** al pasar de una sección a la siguiente.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a identificar al despacho, al profesional responsable y al cliente deudor."
- Sección 2: "Identificadas las partes, corresponde precisar el asunto y el título del encargo."
- Sección 3: "Precisado el asunto, procede detallar las actuaciones profesionales realizadas."
- Sección 4: "Detalladas las actuaciones, corresponde fijar la base de honorarios y su fundamento."
- Sección 5: "Fijada la base, procede completar el desglose económico con impuestos, suplidos y cantidades ya percibidas."
- Sección 6: "Por último, procede fijar el requerimiento de pago y las advertencias que correspondan."

1. **Partes [dato objetivo].** Solicita en bloque mediante `slot_filling_request`: del despacho, denominación, NIF, domicilio, colegio de adscripción, nombre y número de colegiado del profesional; del cliente deudor, nombre o razón social, NIF o CIF y domicilio. Si el documento es una solicitud de jura de cuentas, añade el órgano judicial, el número de autos y la clase de procedimiento.
2. **Asunto y título del encargo [dato objetivo, con validación].** Referencia del expediente, objeto del asunto, fecha de inicio y de terminación de la actuación, y **título del encargo**: hoja de encargo con su fecha y cláusula económica, o descripción del encargo verbal con los elementos que lo acrediten. Si no hay encargo escrito, pregunta expresamente por: correos o mensajes que acrediten el encargo, apoderamiento o designación en el procedimiento, documentación aportada por el cliente, y actuaciones consentidas por él. Es la prueba del encargo, y sin ella la reclamación es frágil.
3. **Relación de actuaciones [negociación — con límite de secreto profesional].** Construye la relación **fechada y ordenada** de las actuaciones realizadas: estudio de documentación, reuniones con su fecha y duración, redacción de escritos identificados por su clase, presentaciones, comparecencias y vistas con su fecha, recursos, comunicaciones relevantes. **Describe actuaciones, no contenidos:** "redacción de escrito de oposición a la demanda" es correcto; transcribir la estrategia o las confidencias del cliente vulnera el secreto profesional. Advierte de este límite y aplícalo.
4. **Base de honorarios y su fundamento [negociación].**
   - *Si hay encargo escrito con honorarios pactados:* la base es la pactada. Reprodúcela citando la cláusula, y comprueba que la minuta se ajusta a ella. Si el asunto excedió del alcance pactado, sepáralo como concepto distinto y explica su título.
   - *Si no hay pacto claro:* explica que la determinación se hará por criterios objetivos —cuantía y complejidad del asunto, dedicación acreditada, usos profesionales del ámbito y, a los efectos legalmente admitidos, los criterios orientativos del colegio—, y construye la base razonándola con esos elementos. **No invoques criterios orientativos sin haber verificado que el colegio los tiene publicados y en qué versión.**
5. **Desglose económico [dato objetivo, con cálculo].** Base de honorarios, impuesto sobre el valor añadido con su tipo verificado, retención a cuenta del IRPF cuando el cliente esté obligado a practicarla, suplidos justificados uno a uno, provisiones de fondos recibidas, cantidades ya abonadas, y saldo resultante. Muestra el cálculo completo antes de escribirlo. **Separa siempre honorarios de suplidos:** su confusión es la causa más frecuente de impugnación por excesivos.
6. **Requerimiento y advertencias [negociación].** Fija el plazo de pago, el medio, la cuenta, y el interés de demora pactado o el interés legal. Según el documento: en el requerimiento previo, la advertencia de acciones y la finalidad de interrumpir la prescripción; en la jura de cuentas, la manifestación formal de que los honorarios son debidos y no han sido satisfechos —requisito legal del artículo 35—, y la relación de documentos que se acompañan. Recuerda que la reclamación debe presentarse ante el órgano que conoció del asunto.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar un apartado existente.
2. Ampliar o precisar la relación de actuaciones.
3. Revisar la base de honorarios o su fundamento.
4. Corregir el desglose económico, los suplidos o las cantidades percibidas.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas de Cierre
- **Carácter DRAFT:** revisión por el profesional responsable antes de su firma, entrega o presentación.
- **Entrega previa de la minuta:** no se reclama lo que no se ha minutado antes. Entregar la minuta detallada al cliente y acreditar su recepción es el paso previo a cualquier reclamación.
- **Prescripción:** recordar la fecha límite calculada y que el requerimiento fehaciente la interrumpe.
- **Secreto profesional:** revisar el documento antes de entregarlo o presentarlo para comprobar que no revela contenidos amparados por el secreto ni datos de terceros.
- **Jura de cuentas:** el decreto que fije la cantidad debida no es susceptible de recurso, pero **no prejuzga** la sentencia que pudiera recaer en un juicio ordinario posterior. Es un procedimiento rápido, no definitivo en cuanto al fondo.
- **Impugnación por el cliente:** si el cliente impugna, el trámite y el resultado difieren según impugne por indebidos o por excesivos. Verificar el trámite vigente antes de contestar.
- **Relación con el cliente:** advertir de que la reclamación judicial de honorarios frente a un cliente tiene coste reputacional y, con clientes consumidores, riesgo de queja deontológica. Valorar la negociación o el fraccionamiento antes de litigar.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre en el BOE la versión consolidada vigente de la Ley 1/2000 de Enjuiciamiento Civil y del Estatuto General de la Abogacía Española, y en el colegio de adscripción su normativa y sus criterios orientativos, antes de redactar.
2. **Comprobación previa de la hoja de encargo obligatoria:** no redactar reclamación alguna sin haber comprobado si existe encargo escrito y qué dice. Si no existe, advertirlo con claridad al usuario y no minimizar la debilidad de la posición.
3. **La jura de cuentas solo cabe respecto de honorarios devengados en un asunto judicial** y ante el órgano que conoció de él. No redactarla para honorarios de asesoramiento extrajudicial: derivar a las vías civiles alternativas.
4. **Minuta detallada, nunca global:** está PROHIBIDO redactar una minuta con un importe único sin relación de actuaciones ni desglose. Es el defecto que más impugnaciones provoca y el que hace inviable la jura de cuentas.
5. **Secreto profesional:** describir actuaciones, no contenidos. No transcribir estrategia, confidencias del cliente ni datos de terceros en la minuta ni en el escrito de reclamación.
6. **Separación de honorarios y suplidos:** los suplidos se justifican documentalmente uno a uno y se repercuten sin recargo. No integrarlos en la base de honorarios.
7. **Criterios orientativos:** solo pueden emplearse a los efectos legalmente admitidos. No invocarlos como baremo de precios frente al cliente ni sin verificar que el colegio los tiene publicados y en qué versión.
8. **Cliente consumidor:** advertir del control de transparencia y de abusividad de la cláusula de honorarios, y verificar el estado actual de la cuestión antes de afirmar su alcance en el procedimiento del artículo 35.
9. **Cero invención:** no inventar actuaciones, fechas, números de autos, órganos judiciales, números de colegiado, importes de criterios orientativos ni tipos impositivos. Lo no aportado permanece como marcador con su nombre propio de plantilla.
10. **Cita de jurisprudencia:** prohibido citar sentencias o doctrina no verificadas en la misma sesión en una fuente oficial.
11. **Sintaxis de los marcadores (`{{CLAVE: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real: nunca debe quedar rastro de la anotación en el documento escrito. Los marcadores cuyo dato aún no exista se conservan **íntegros, con su clave y su tipo**, para que el cliente y el profesional que revise vean qué falta y de qué naturaleza es. Está PROHIBIDO sustituir la clave propia del marcador por un literal genérico.
