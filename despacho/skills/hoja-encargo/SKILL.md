---
name: hoja-encargo
description: >
  Genera la documentación contractual de la relación entre el despacho y su cliente: hoja de encargo
  profesional con delimitación del alcance y presupuesto de honorarios, presupuesto previo
  independiente, hoja de encargo con retribución vinculada al resultado, y comunicación de
  finalización o renuncia al encargo. Aplica el Estatuto General de la Abogacía Española aprobado por
  Real Decreto 135/2021, la normativa deontológica del colegio de adscripción, la normativa de
  protección de consumidores cuando el cliente es persona física que actúa al margen de una actividad
  empresarial, y la Ley 15/2007 de Defensa de la Competencia en cuanto al uso de criterios
  orientativos de honorarios, en sus versiones consolidadas vigentes verificadas en el BOE.
  Metodología: clasificación de la modalidad de honorarios y de la naturaleza del cliente mediante
  formulario interactivo, plan de acción con el desglose económico completo, creación del documento
  base en el workspace y edición incremental cláusula a cláusula. NO usar para redactar documentos del
  asunto del cliente, ni para reclamar honorarios impagados, que corresponde a la skill
  `minuta-jura-cuentas`.
when_to_use: |
  - El despacho va a aceptar un nuevo encargo y necesita formalizarlo por escrito antes de empezar.
  - El despacho necesita presentar un presupuesto de honorarios a un cliente potencial.
  - El despacho quiere pactar una retribución vinculada al resultado del asunto.
  - El despacho va a dar por terminado un encargo, o va a renunciar a él, y necesita documentarlo.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - tipo_documento: hoja de encargo / presupuesto / hoja de encargo con retribución por resultado / comunicación de fin de encargo
  - modalidad_honorarios: importe fijo por actuación / por horas / mixta / vinculada al resultado / provisión periódica
  - naturaleza_cliente: persona física consumidora / empresa, autónomo o profesional
  - ambito_asunto: extrajudicial / judicial / ambos
  - datos_despacho: denominación, NIF, domicilio, colegio de adscripción, número de colegiado del profesional responsable y datos del seguro de responsabilidad civil
  - datos_cliente: nombre o razón social, NIF o CIF, domicilio, representante y datos de contacto
  - objeto_encargo: descripción del asunto y de las actuaciones incluidas
  - exclusiones: actuaciones expresamente excluidas del encargo
  - honorarios: importe o tarifa, hitos de facturación, provisión de fondos, impuestos y retenciones
  - gastos_y_suplidos: gastos previsibles, tasas, provisión de fondos para terceros profesionales
outputs:
  - hoja_encargo: hoja de encargo profesional completa en markdown, DRAFT, con espacio de firma de ambas partes
  - presupuesto_honorarios: presupuesto detallado en markdown, DRAFT, con su plazo de validez
references:
  - references/fuentes-y-normativa-colegial.md
  - references/honorarios-modalidades-y-transparencia.md
  - references/alcance-del-encargo-y-exclusiones.md
  - references/deberes-del-profesional-y-conflicto-de-intereses.md
assets:
  - assets/template-comunicacion-fin-encargo.md
  - assets/template-hoja-encargo-profesional.md
  - assets/template-hoja-encargo-resultado.md
  - assets/template-presupuesto-honorarios.md
---

# Generar la Hoja de Encargo Profesional

> DRAFT — para revisión por el profesional responsable antes de su firma y entrega. Debe adaptarse a la normativa deontológica del colegio de adscripción.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de documento):** `hoja_encargo` | `presupuesto` | `encargo_resultado` | `fin_encargo`.
- **V2 (Modalidad de honorarios):** `fijo` | `por_horas` | `mixta` | `resultado` | `provision_periodica`.
- **V3 (Naturaleza del cliente):** `consumidor` | `empresa_profesional`. *(Determina el control de transparencia aplicable y la información precontractual exigible.)*
- **V4 (Ámbito del asunto):** `extrajudicial` | `judicial` | `ambos`. *(Determina la referencia a procurador, tasas, costas y plazos preclusivos.)*
- **V5 (Origen plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

### 1.1 Escucha Activa Previa
Si el usuario ya ha identificado inequívocamente el documento, la modalidad retributiva, la naturaleza del cliente y el ámbito del asunto, registra los vectores en silencio y pasa a la **Fase 2**.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "tipo_documento",
      "rationale": "Resolver V1: el presupuesto precede al encargo, y la comunicación de fin de encargo tiene requisitos propios de preaviso y de entrega de documentación.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "hoja_encargo", "label": "Hoja de encargo profesional para formalizar un nuevo asunto"},
        {"id": "presupuesto", "label": "Presupuesto de honorarios para un cliente potencial"},
        {"id": "encargo_resultado", "label": "Hoja de encargo con retribución vinculada al resultado del asunto"},
        {"id": "fin_encargo", "label": "Comunicación de finalización del encargo o de renuncia a la dirección del asunto"}
      ]
    },
    {
      "id": "modalidad_honorarios",
      "rationale": "Resolver V2: cada modalidad exige una redacción distinta del apartado económico y genera un riesgo de conflicto distinto.",
      "question": "¿Cómo se van a retribuir los servicios?",
      "options": [
        {"id": "fijo", "label": "Importe fijo cerrado por la actuación o por hitos"},
        {"id": "por_horas", "label": "Por horas efectivamente dedicadas, con tarifa por perfil profesional"},
        {"id": "mixta", "label": "Mixta: importe fijo mínimo más un componente variable"},
        {"id": "resultado", "label": "Vinculada al resultado del asunto"},
        {"id": "provision_periodica", "label": "Cuota periódica de asesoramiento continuado"}
      ]
    },
    {
      "id": "naturaleza_cliente",
      "rationale": "Resolver V3: si el cliente es consumidor, la hoja de encargo queda sujeta al control de transparencia y de abusividad, y la información precontractual es más exigente.",
      "question": "¿Quién es el cliente?",
      "options": [
        {"id": "consumidor", "label": "Persona física que contrata al margen de una actividad empresarial o profesional"},
        {"id": "empresa_profesional", "label": "Empresa, entidad, autónomo o profesional que contrata en el marco de su actividad"}
      ]
    },
    {
      "id": "ambito_asunto",
      "rationale": "Resolver V4: el asunto judicial obliga a informar de plazos preclusivos, procurador, tasas, costas y régimen de recursos.",
      "question": "¿Cuál es el ámbito del encargo?",
      "options": [
        {"id": "extrajudicial", "label": "Extrajudicial: asesoramiento, negociación, redacción de documentos"},
        {"id": "judicial", "label": "Judicial: dirección procesal en un procedimiento"},
        {"id": "ambos", "label": "Ambos: gestión extrajudicial y, si fracasa, vía judicial"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `tipo_documento`
- `V2` — `modalidad_honorarios`
- `V3` — `naturaleza_cliente`
- `V4` — `ambito_asunto`

### 1.3 Enrutamiento de Estado (Routing por Vectores)

* **Si `[V1 = hoja_encargo]` → Plantilla: `assets/template-hoja-encargo-profesional.md`.**
* **Si `[V1 = presupuesto]` → Plantilla: `assets/template-presupuesto-honorarios.md`.** Explica que el presupuesto no sustituye al encargo: si el cliente lo acepta, hay que formalizar la hoja de encargo antes de iniciar la actuación.
* **Si `[V1 = encargo_resultado]` o `[V2 = resultado]` → Plantilla: `assets/template-hoja-encargo-resultado.md`.** **Advertencia obligatoria en el chat:** la retribución vinculada al resultado exige una redacción especialmente cuidadosa —definición exacta del resultado que genera el derecho, tratamiento de los acuerdos transaccionales, de la renuncia del cliente y del desistimiento, y régimen de las costas percibidas—, y su admisibilidad y límites deben comprobarse en la **normativa deontológica vigente del colegio de adscripción**, que puede imponer condiciones. Verifícalo con `web_search` y adviértelo antes de redactar.
* **Si `[V1 = fin_encargo]` → Plantilla: `assets/template-comunicacion-fin-encargo.md`.** **Advertencia obligatoria:** la renuncia a la dirección de un asunto judicial en curso exige un preaviso que evite la indefensión del cliente y la pérdida de plazos, con puesta a disposición de la documentación. Pregunta expresamente por los plazos vivos del asunto antes de redactar y adviértelo en el propio documento.
* **Si `[V3 = consumidor]` → Régimen reforzado.** Explica que la hoja de encargo queda sujeta al **control de transparencia**: las cláusulas económicas deben ser comprensibles para un cliente medio, no basta con que sean claras para un jurista. Una cláusula de honorarios que el cliente no pudo entender puede resultar inoponible en una reclamación posterior.
* **Si `[V4 = judicial]` o `[V4 = ambos]` → Contenido adicional obligatorio.** El documento debe informar de: la necesidad de procurador cuando la ley lo exija y su coste independiente; las tasas y gastos judiciales; el régimen de **costas** y que su eventual condena a favor del cliente no equivale al honorario pactado ni lo sustituye; la existencia de plazos preclusivos; y el alcance del encargo respecto de los **recursos**, que deben pactarse expresamente porque no se presumen incluidos.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión consolidada vigente del Estatuto General de la Abogacía Española en el BOE.
3. **Identifica el colegio de adscripción** y verifica con `web_search` su normativa deontológica y, si existen, sus criterios orientativos de honorarios, recordando que estos solo pueden emplearse a los efectos legalmente admitidos.
4. Verifica los **tipos vigentes** de impuesto sobre el valor añadido aplicable a los servicios profesionales y de retención a cuenta del impuesto sobre la renta cuando el cliente sea empresario o profesional obligado a retener, incluida la reducción aplicable a profesionales de inicio de actividad. No los escribas de memoria.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Estructura del documento** que se va a construir y por qué, con el contenido adicional que exija la clasificación obtenida.
2. **Advertencias específicas** de la modalidad retributiva y de la naturaleza del cliente.
3. **Recordatorio de comprobación previa:** conflicto de intereses con clientes anteriores o con la parte contraria, competencia profesional para el objeto del encargo, y cobertura del seguro de responsabilidad civil.
4. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
5. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación del origen de la plantilla
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:** accede al adjunto y aplica el **guardrail de cláusulas problemáticas**: honorarios sin importe ni criterio determinable; remisión genérica a criterios colegiales como única definición del honorario; exclusión total de responsabilidad del profesional; cláusula que atribuya al despacho la propiedad de la documentación del cliente; renuncia del cliente a reclamar; sumisión a fuero distinto del que corresponda cuando el cliente sea consumidor; y ausencia de información sobre el tratamiento de datos. Advierte de cada una y propón la redacción válida.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura (`create_file`):** vuelca íntegramente la plantilla acordada en el workspace con nombre en `snake_case.md`, aplicando **Zero-Omission** y dejando los datos pendientes como marcador con su nombre propio de plantilla.
2. **Validación (`read_file`):** comprueba el volcado íntegro.
3. **Confirmación y encadenamiento:** informa de la ruta absoluta y, en la misma respuesta, abre la primera sección de la Fase 4 con su anuncio y su primera solicitud de datos.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA

### Protocolo Obligatorio de Edición
```
[slot_filling_request (grupos) / Chat (negociación económica)] ──> [Vista previa en texto plano]
      ──> [«¿Confirmamos esta cláusula?»] ──> [edit_file + read_file]
```

- **Datos estructurados agrupados (`slot_filling_request`, MANDATORIO):** despacho, cliente, datos económicos y datos bancarios se piden en bloque.
- **Anuncio de sección visible** al pasar de una cláusula a la siguiente.

### Hoja de Ruta de Cláusulas

Anuncios fijos:
- Cláusula 1: "Procedemos a identificar al despacho, al profesional responsable y al cliente."
- Cláusula 2: "Identificadas las partes, corresponde delimitar el objeto del encargo, por inclusión y por exclusión."
- Cláusula 3: "Delimitado el objeto, procede fijar los honorarios y su forma de devengo."
- Cláusula 4: "Fijados los honorarios, corresponde determinar los gastos, suplidos y provisión de fondos."
- Cláusula 5: "Determinada la parte económica, procede establecer las obligaciones de ambas partes y el régimen de comunicación."
- Cláusula 6: "Establecidas las obligaciones, corresponde fijar la duración, la terminación y el régimen de la documentación."
- Cláusula 7: "Por último, procede incorporar la información sobre protección de datos y las cláusulas de cierre."

1. **Partes [dato objetivo].** Solicita en bloque mediante `slot_filling_request`: del despacho, denominación, NIF, domicilio, **colegio de adscripción**, nombre y **número de colegiado del profesional responsable**, y datos del seguro de responsabilidad civil profesional con su entidad y cobertura; del cliente, nombre o razón social, NIF o CIF, domicilio, representante con su cargo si es persona jurídica, y correo electrónico y teléfono a efectos de comunicación. La identificación del profesional responsable con su número de colegiado no es un formalismo: acredita la habilitación y delimita la responsabilidad.
2. **Objeto del encargo [negociación — la cláusula que evita el conflicto].** Describe el asunto y **enumera las actuaciones incluidas** una por una. Después, y con la misma precisión, **enumera las excluidas**. Explica al usuario por qué importa: la mayoría de los conflictos por honorarios no nacen del precio, sino de la discrepancia sobre qué estaba incluido. Excluye siempre de forma expresa, salvo pacto en contrario: los recursos frente a la resolución que ponga fin a la instancia; la ejecución de la resolución; los procedimientos conexos o incidentales; la intervención de procurador, peritos, notarios y traductores; y las actuaciones ante organismos distintos del previsto.
3. **Honorarios [negociación — con desglose económico completo].**
   - *Importe fijo:* importe, hitos de devengo y qué actuación cubre cada hito.
   - *Por horas:* tarifa por perfil profesional, unidad mínima de facturación, periodicidad de la facturación y **compromiso de información periódica del tiempo consumido**. Explica que sin ese compromiso el cliente no puede controlar el gasto y el conflicto es previsible; recomienda además pactar una **estimación máxima orientativa** con obligación de avisar antes de superarla.
   - *Mixta:* importe fijo mínimo y definición precisa del componente variable.
   - *Provisión periódica:* cuota, servicios incluidos en la cuota, límite de horas o actuaciones y tratamiento del exceso.
   - En todas: **base, impuesto sobre el valor añadido y retención a cuenta separados**, con los tipos verificados; medio y plazo de pago; consecuencias del impago, incluido el interés de demora pactado y su límite; y advertencia de que la condena en costas a favor del cliente no equivale ni sustituye al honorario pactado.
4. **Gastos, suplidos y provisión de fondos [negociación].** Distingue con claridad **honorarios** de **gastos y suplidos**: tasas, aranceles, notaría, registros, peritos, procurador, desplazamientos, traducciones. Fija la provisión de fondos, su importe, su destino y el régimen de rendición de cuentas y devolución del saldo no consumido. Advierte de que los fondos del cliente destinados a terceros deben tratarse con separación de los propios del despacho.
5. **Obligaciones de las partes y comunicación [negociación].** Del despacho: diligencia profesional, información periódica del estado del asunto, secreto profesional, y advertencia de plazos. Del cliente: aportación de documentación completa y veraz, comunicación de cualquier notificación que reciba, y disponibilidad para las actuaciones que requieran su presencia. Fija el **canal y la periodicidad** de la información y las consecuencias de la falta de colaboración del cliente. Incluye la advertencia expresa de que el despacho **no garantiza un resultado**: la obligación es de medios, no de resultado.
6. **Duración, terminación y documentación [negociación].** Duración del encargo, causas de terminación, **preaviso** para la renuncia y para la revocación, liquidación de honorarios devengados hasta la terminación, y régimen de la documentación: la del cliente es del cliente y debe entregarse a su terminación; el despacho conserva copia por el plazo legalmente exigible. Si `[V4 = judicial]`, advierte del deber de evitar la indefensión del cliente y de coordinar la renuncia con los plazos vivos del procedimiento.
7. **Protección de datos y cierre [dato objetivo].** Información sobre el tratamiento de los datos del cliente con su finalidad, base jurídica, plazo de conservación y derechos, remitiendo al registro de actividades del despacho. Cláusulas de cierre: integridad del acuerdo, modificación por escrito, y fuero, que si `[V3 = consumidor]` debe ser el que legalmente corresponda sin sumisión que perjudique al cliente. Cierra con la firma de ambas partes y la entrega de un ejemplar al cliente.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar una cláusula existente.
2. Precisar el objeto del encargo o ampliar las exclusiones.
3. Revisar el desglose económico, los hitos o la provisión de fondos.
4. Añadir un pacto adicional a medida.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas de Cierre
- **Carácter DRAFT:** revisión por el profesional responsable y adaptación a la normativa deontológica del colegio de adscripción antes de la firma.
- **Firma previa al inicio de la actuación:** la hoja de encargo debe estar firmada **antes** de empezar. Un encargo iniciado sin documento escrito deja al despacho sin base para reclamar y sin defensa frente a una discrepancia sobre el alcance.
- **Entrega de ejemplar al cliente** y conservación del firmado en el expediente.
- **Comprobaciones previas cumplidas:** ausencia de conflicto de intereses, competencia profesional para el objeto, y cobertura del seguro de responsabilidad civil.
- **Diligencia debida:** si el asunto entra en el ámbito de la normativa de prevención del blanqueo de capitales, recuerda la obligación de identificación y de expediente de diligencia debida, y ofrece la skill `prevencion-blanqueo`.
- **Protección de datos:** si el encargo implica acceso a datos personales de terceros por cuenta del cliente, valorar la necesidad de contrato de encargado de tratamiento, y ofrecer la skill `proteccion-datos-despacho`.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre en el BOE la versión consolidada vigente del Estatuto General de la Abogacía Española y de la normativa de consumidores aplicable, y en el colegio de adscripción su normativa deontológica, antes de redactar.
2. **Honorarios determinados o determinables:** está PROHIBIDO redactar una cláusula de honorarios sin importe, tarifa o criterio objetivo de cálculo. La remisión genérica a criterios colegiales no es una definición válida del honorario frente al cliente: los criterios orientativos solo pueden emplearse a los efectos legalmente admitidos, señaladamente la tasación de costas y la jura de cuentas.
3. **Control de transparencia con clientes consumidores:** las cláusulas económicas deben ser comprensibles para un cliente medio. Una cláusula clara para un jurista pero opaca para el cliente puede resultar inoponible.
4. **Exclusiones expresas:** no dar el documento por cerrado sin enumerar las actuaciones excluidas, señaladamente recursos, ejecución, procedimientos conexos e intervención de terceros profesionales.
5. **Obligación de medios:** no redactar compromisos de resultado ni garantías de éxito. Hacer constar expresamente que la obligación es de medios.
6. **Retribución vinculada al resultado:** verificar su admisibilidad y sus límites en la normativa deontológica vigente del colegio antes de redactarla, y definir con precisión el resultado que genera el derecho, el tratamiento de la transacción, del desistimiento y de la revocación, y el régimen de las costas.
7. **Separación de fondos de terceros:** los fondos del cliente destinados a pagos a terceros no se confunden con los propios del despacho, y su régimen de rendición de cuentas debe constar.
8. **Cero invención:** no inventar números de colegiado, denominaciones de colegio, datos de seguro, tipos impositivos, importes de tasas ni criterios de honorarios. Lo no aportado permanece como marcador con su nombre propio de plantilla.
9. **Renuncia al encargo:** no redactar una renuncia sin haber comprobado los plazos vivos del asunto y sin preaviso suficiente para evitar la indefensión del cliente.
10. **Sintaxis de los marcadores (`{{clave: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real: nunca debe quedar rastro de la anotación en el documento escrito. Los marcadores cuyo dato aún no exista se conservan **íntegros, con su clave y su tipo**, para que el cliente y el profesional que revise vean qué falta y de qué naturaleza es. Está PROHIBIDO sustituir la clave propia del marcador por un literal genérico.
