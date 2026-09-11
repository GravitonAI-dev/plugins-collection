---
name: derecho-mercantil-contratos-mercantiles
description: >
  Redacta los contratos habituales entre empresas en Espana conforme al **Codigo Civil** (Arts. 1254 a
  1258 y 1543 y siguientes), que fija el regimen general de las obligaciones y contratos, al **Codigo
  de Comercio**, que rige los actos de comercio, y a la **Ley 12/1992** sobre contrato de agencia, que
  regula el estatuto del agente y su indemnizacion por clientela.


  Genera cuatro contratos: prestacion de servicios entre empresas, acuerdo de confidencialidad,
  contrato de agencia y contrato de distribucion.


  Incorpora los plazos maximos de pago de la normativa de morosidad, el regimen de encargado del
  tratamiento cuando el prestador accede a datos personales, la proteccion del secreto empresarial, y
  la ley aplicable y el fuero cuando la contraparte es extranjera. Advierte de la diferencia critica
  entre agencia y distribucion en materia de indemnizacion por clientela y de los indicios de
  laboralidad que pueden convertir al agente o al prestador en trabajador por cuenta ajena.


  NO usar cuando la contraparte sea un consumidor, que corresponde al plugin de consumo, ni para
  relaciones laborales o de trabajadores autonomos economicamente dependientes, que corresponden al
  plugin laboral, ni para contratos financieros, de seguro, de obra publica o de licencia de software
  con condiciones generales predispuestas.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Codigo Civil](https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763) y
  [Ley 12/1992 sobre Contrato de Agencia](https://www.boe.es/buscar/act.php?id=BOE-A-1992-12347).
when_to_use: |
  - Una empresa va a prestar o recibir servicios de otra empresa y necesita el contrato.
  - Dos empresas van a intercambiar informacion confidencial antes o durante una negociacion.
  - Una empresa va a nombrar un agente comercial que promueva sus productos de forma estable.
  - Una empresa va a nombrar un distribuidor que compre y revenda sus productos en un territorio.
  - El usuario pregunta la diferencia entre agente y distribuidor, o si tendra que indemnizar por clientela al terminar.
  - El usuario pregunta que plazo de pago puede pactar con un proveedor o cliente empresa.
inputs:
  - documento: prestacion de servicios / confidencialidad / agencia / distribucion (V1)
  - contraparte: empresa espanola / empresa extranjera (V2)
  - duracion: indefinida / plazo determinado (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_partes: razon social, CIF, domicilio, datos registrales y representante de cada parte
  - objeto_contrato: descripcion de los servicios, productos o informacion objeto del contrato
  - precio_y_pago: precio o comision, forma de calculo, periodicidad y plazo de pago
  - plazo_y_preaviso: duracion, prorrogas y plazo de preaviso para la terminacion
  - territorio_y_exclusiva: ambito territorial y caracter exclusivo o no de la relacion
  - objetivos_minimos: objetivos de venta o niveles de servicio exigidos y consecuencias de su incumplimiento
  - datos_personales: si el prestador accedera a datos personales y con que finalidad
  - propiedad_intelectual: titularidad y licencia de los resultados o de las marcas
  - ley_y_fuero: ley aplicable y sumision a tribunales o a arbitraje
outputs:
  - contrato_prestacion_servicios: contrato de prestacion de servicios entre empresas, DRAFT
  - acuerdo_confidencialidad: acuerdo de confidencialidad unilateral o reciproco, DRAFT
  - contrato_agencia: contrato de agencia mercantil con su regimen de comision e indemnizacion, DRAFT
  - contrato_distribucion: contrato de distribucion con territorio, objetivos y terminacion, DRAFT
references:
  - references/regimen-contratos-mercantiles.md
  - references/agencia-vs-distribucion-y-morosidad.md
  - references/estilo-redaccion-societaria.md
assets:
  - assets/template-contrato-prestacion-servicios.md
  - assets/template-acuerdo-confidencialidad.md
  - assets/template-contrato-agencia.md
  - assets/template-contrato-distribucion.md
---

# Redactar Contratos entre Empresas (Servicios, Confidencialidad, Agencia y Distribución)

> DRAFT — para revisión por un abogado mercantilista o notario antes de su firma, elevación a público o inscripción. No constituye asesoramiento jurídico vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva y rigurosa a través de un procedimiento estructurado en 5 fases secuenciales para redactar un contrato mercantil.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `prestacion_servicios` | `confidencialidad` | `agencia` | `distribucion` | `contraparte_consumidor`.
- **V2 (Contraparte):** `empresa_espanola` | `empresa_extranjera`.
- **V3 (Duración):** `indefinida` | `plazo_determinado`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar qué contrato se redacta y con quién.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un abogado mercantilista (de usted), confirmando que vais a preparar el contrato entre empresas que necesita.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca qué contrato necesita, si la contraparte es española o extranjera y si la duración es indefinida o determinada, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el contrato (`V1`), la contraparte (`V2`) o la duración (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar cual de los contratos mercantiles se redacta.",
      "question": "¿Qué contrato necesita?",
      "options": [
        {"id": "prestacion_servicios", "label": "Prestación de servicios entre empresas"},
        {"id": "confidencialidad", "label": "Acuerdo de confidencialidad"},
        {"id": "agencia", "label": "Agencia comercial (el agente promueve y no compra la mercancía)"},
        {"id": "distribucion", "label": "Distribución (el distribuidor compra y revende por su cuenta)"},
        {"id": "contraparte_consumidor", "label": "La otra parte es un consumidor o un particular, no una empresa"}
      ]
    },
    {
      "id": "contraparte",
      "rationale": "Resolver V2 para fijar ley aplicable, fuero y regimen de pago transfronterizo.",
      "question": "¿La otra parte es una empresa española o extranjera?",
      "options": [
        {"id": "empresa_espanola", "label": "Empresa española"},
        {"id": "empresa_extranjera", "label": "Empresa extranjera"}
      ]
    },
    {
      "id": "duracion",
      "rationale": "Resolver V3: la duracion indefinida obliga a regular el preaviso de terminacion.",
      "question": "¿La relación será indefinida o por un plazo determinado?",
      "options": [
        {"id": "indefinida", "label": "Indefinida, con posibilidad de terminar mediante preaviso"},
        {"id": "plazo_determinado", "label": "Por un plazo determinado, con o sin prórrogas"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `contraparte`
- `V3` — `duracion`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = contraparte_consumidor`:**
  - **DETENER.** Informar de que la contratación con consumidores está sujeta al régimen imperativo de protección de los consumidores y usuarios, con control de cláusulas abusivas, deberes de información precontractual y derecho de desistimiento, que esta skill no cubre. Derivar al plugin de consumo o a abogado especialista. No crear documento.
- **Si `V1 = prestacion_servicios`:**
  - Plantilla del sistema: `assets/template-contrato-prestacion-servicios.md`. Proceder a la **Fase 2**.
- **Si `V1 = confidencialidad`:**
  - Plantilla del sistema: `assets/template-acuerdo-confidencialidad.md`. Proceder a la **Fase 2**.
- **Si `V1 = agencia`:**
  - Plantilla del sistema: `assets/template-contrato-agencia.md`. Proceder a la **Fase 2**.
- **Si `V1 = distribucion`:**
  - Plantilla del sistema: `assets/template-contrato-distribucion.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina la redacción de la cláusula de ley aplicable y fuero, y si se incorpora la mención al régimen de la contratación internacional.
- `V3` no elige plantilla: determina si se regula el preaviso de terminación de la relación indefinida o el régimen de prórrogas del plazo determinado.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `regimen-contratos-mercantiles.md`, `agencia-vs-distribucion-y-morosidad.md` y `estilo-redaccion-societaria.md`.
2. Opcionalmente verifica mediante `web_search` la doctrina vigente sobre indemnización por clientela en distribución y los plazos de pago de la normativa de morosidad. Aplica la redacción vigente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal y Consecuencias Económicas:**
   - Si el contrato es de agencia: advertir de que la ley reconoce al agente, al terminar el contrato, una indemnización por clientela y, en su caso, por daños, y que es un régimen **imperativo** que no puede excluirse en perjuicio del agente. Explicar el preaviso legal de un mes por año de vigencia, con máximo de seis meses.
   - Si el contrato es de distribución: explicar que no hay ley específica, que la indemnización por clientela no se aplica de forma automática y que su procedencia se discute caso por caso, de modo que la redacción del contrato es decisiva.
   - Si es de servicios: advertir del plazo máximo de pago de la normativa de morosidad y de la necesidad de incorporar el contrato de encargado del tratamiento si hay acceso a datos personales.
   - Si es de confidencialidad: explicar que la protección legal del secreto empresarial exige haber adoptado medidas razonables para mantener la información secreta.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Nombrar por su ruta la plantilla **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
- **Si `origen_plantilla = plantilla_sistema`:** utiliza el asset enrutado y avanza a la **Fase 3**.
- **Si `origen_plantilla = plantilla_usuario`:** toma la plantilla adjunta en `<attached_documents>` o el texto pegado en `<user_message>`, verifica que no contenga pactos nulos o de validez dudosa (renuncia anticipada del agente a la indemnización por clientela, plazos de pago superiores al máximo legal, no competencia sin límite temporal, sumisión a fuero contraria a norma imperativa), advierte en el chat y propón la redacción válida, y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en el workspace del usuario, con el nombre `contrato_prestacion_servicios.md`, `acuerdo_confidencialidad.md`, `contrato_agencia.md` o `contrato_distribucion.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos de la clasificación y de la escucha activa. Todos los datos pendientes permanecen como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves. PROHIBIDO dejar archivos en blanco o con notas resumidas.
2. **Validación de Disco (`read_file`):** ejecuta `read_file` sobre el archivo creado para confirmar su integridad.
3. **Confirmación en Chat:** informa al usuario de la ruta del archivo generado e introduce de inmediato la primera sección de la **Fase 4** sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques. Para cada bloque, ejecuta estrictamente el ciclo interactivo:
```
[Anuncio de la sección + Pregunta] --> [Vista Previa en texto plano] --> [¿Confirmamos esta cláusula?] --> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Anuncio y Pregunta en Chat:** anuncia la sección sustantiva con una frase breve en registro jurídico-mercantil (por ejemplo, *"Pasamos ahora a fijar el precio y las condiciones de pago"*) y, en el mismo mensaje, formula ya la primera pregunta. No pidas permiso para pasar de sección: informa y continúa.
2. **Búsqueda prioritaria de partes e intervinientes y Regla de Cero Redundancia (`search_clients` / `get_client` — REG-CLI-01 y REG-CLI-02):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** conforme a `REG-CLI-01` de `CLAUDE.md`. Si los datos de una persona ya fueron obtenidos mediante `search_clients` o `get_client`, **queda TERMINANTEMENTE PROHIBIDO volver a pedir dicha información** (nombre, DNI/NIE/CIF, domicilio, contacto, etc.), ya sea en el chat o en `slot_filling_request` (`REG-CLI-02`). Si todos los datos requeridos constan en la ficha del cliente, **NO invoques `slot_filling_request`**: redacta directamente la cláusula, muestra la vista previa en texto plano en el chat y pide confirmación. Solo si faltan campos específicos ausentes en la ficha, invocarás `slot_filling_request` exclusivamente para los datos pendientes.
   - **Datos estructurados no de cliente agrupados (`slot_filling_request`, MANDATORIO):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
3. **Vista Previa (Preview):** muestra el texto redactado en texto plano, sin backticks de código.
4. **Confirmación:** pregunta literalmente: `¿Confirmamos esta cláusula?`.
5. **Persistencia en Disco:** tras la confirmación, aplica `edit_file` con coincidencia exacta y verifica inmediatamente con `read_file`.
6. **Validación de sentido, no solo de formato:** comprueba que el plazo de pago no excede del máximo legal, que la comisión y su base de cálculo son coherentes, que el preaviso pactado no es inferior al legal en la agencia y que el territorio y la exclusiva no se contradicen. Si algo no encaja, dialoga en el chat, señala el motivo y pide aclaración antes de volcarlo.

### Hoja de Ruta de Secciones — RAMA PRESTACIÓN DE SERVICIOS:

1. **Partes y representación** *(confirmación agrupada)*: razón social, CIF, domicilio, datos registrales y representante con su título de representación de cada parte.
2. **Objeto y alcance de los servicios**: descripción de los servicios, entregables, exclusiones expresas y, en su caso, niveles de servicio con sus indicadores.
3. **Precio, facturación y pago**: precio o tarifa, revisión, gastos repercutibles, periodicidad de facturación y plazo de pago con la advertencia del máximo legal, intereses de demora y suspensión por impago.
4. **Medios, personal y subcontratación**: medios que aporta el prestador, ausencia de dependencia y ajenidad respecto del cliente, régimen de subcontratación y responsabilidad por los subcontratistas.
5. **Propiedad intelectual y confidencialidad**: titularidad de los resultados, licencia de uso, material preexistente y deber de secreto con su duración.
6. **Protección de datos**: *Condicional acceso a datos personales:* incorporación del contrato de encargado del tratamiento, con finalidad, instrucciones, medidas de seguridad, subencargados, brechas y destino de los datos al finalizar.
7. **Responsabilidad, garantías y seguro**: régimen de responsabilidad por incumplimiento, límite de responsabilidad y su validez, exclusión del dolo, garantía de los trabajos y seguro exigido.
8. **Duración y terminación**: *Condicional `V3 = indefinida`:* preaviso de terminación. *Condicional `V3 = plazo_determinado`:* plazo, prórrogas y su denuncia. Causas de resolución anticipada y efectos.
9. **Ley aplicable, fuero y cláusulas finales**: *Condicional `V2 = empresa_extranjera`:* ley aplicable elegida, sumisión a tribunales o arbitraje e idioma del contrato. Notificaciones, cesión, nulidad parcial e integridad del acuerdo.

### Hoja de Ruta de Secciones — RAMA CONFIDENCIALIDAD:

1. **Partes y carácter del acuerdo** *(confirmación agrupada)*: identificación de las partes y determinación de si la obligación es unilateral o recíproca.
2. **Finalidad y definición de información confidencial**: propósito para el que se revela la información, definición de lo protegido y exclusiones (información pública, de desarrollo propio o recibida legítimamente de un tercero).
3. **Obligaciones del receptor y personas autorizadas**: deber de secreto, uso limitado a la finalidad, medidas de protección, personas a las que puede revelarse y su vinculación.
4. **Duración, devolución y excepciones**: plazo de vigencia de la obligación, devolución o destrucción del material y revelación exigida por ley o por autoridad.
5. **Incumplimiento, propiedad y cláusulas finales**: consecuencias del incumplimiento y penalización, ausencia de cesión de derechos por la mera revelación, ley aplicable y fuero.

### Hoja de Ruta de Secciones — RAMA AGENCIA:

1. **Partes y objeto de la agencia** *(confirmación agrupada)*: identificación de empresario y agente, y encargo de promover o promover y concluir operaciones, con constancia de que el agente actúa de forma independiente y no asume el riesgo de las operaciones salvo pacto expreso.
2. **Territorio, clientela y exclusiva**: ámbito territorial o grupo de clientes asignado y carácter exclusivo o no de la asignación.
3. **Obligaciones de las partes**: obligaciones del agente de actuar lealmente y de informar, y del empresario de facilitar muestras e información y de comunicar la aceptación o el rechazo de las operaciones.
4. **Comisión**: base de cálculo, porcentaje, operaciones que la devengan, momento del devengo y del nacimiento del derecho, liquidación y pago, y régimen de las operaciones concluidas tras la extinción.
5. **Duración y preaviso**: *Condicional `V3 = indefinida`:* preaviso de un mes por año de vigencia con el máximo legal de seis meses. *Condicional `V3 = plazo_determinado`:* plazo y advertencia de que la continuación de la ejecución tras su vencimiento transforma el contrato en indefinido.
6. **Indemnizaciones por extinción**: indemnización por clientela y, en su caso, por daños y perjuicios, con explicación de sus presupuestos y de la imposibilidad de renunciar a ellas anticipadamente en perjuicio del agente. Supuestos en que no procede.
7. **Pacto de limitación de la competencia tras la extinción**: *Condicional pacto expreso:* delimitación material, territorial y temporal, con el máximo legal de dos años, y forma escrita.
8. **Responsabilidad, ley aplicable y fuero**: régimen de responsabilidad, ley aplicable y sumisión, con la advertencia de las normas imperativas aplicables al agente.

### Hoja de Ruta de Secciones — RAMA DISTRIBUCIÓN:

1. **Partes y objeto de la distribución** *(confirmación agrupada)*: identificación de proveedor y distribuidor, y determinación de que el distribuidor adquiere en firme y revende en nombre y por cuenta propios, asumiendo el riesgo.
2. **Territorio, exclusiva y canal**: territorio asignado, exclusividad y su reciprocidad, canales de venta permitidos y régimen de las ventas fuera del territorio.
3. **Condiciones de compra y reventa**: precios de compra, descuentos, pedidos mínimos, plazos de entrega, transmisión del riesgo y régimen de devoluciones. Advertir de que el proveedor no puede imponer precios de reventa fijos o mínimos.
4. **Objetivos y niveles de compra**: objetivos periódicos, forma de medición y consecuencias de su incumplimiento.
5. **Marcas, imagen y stock**: licencia de uso de marcas limitada a la reventa, obligaciones de imagen, stock mínimo y servicio posventa.
6. **Duración y terminación**: *Condicional `V3 = indefinida`:* preaviso razonable de terminación, con advertencia de que un preaviso insuficiente es fuente frecuente de condena. *Condicional `V3 = plazo_determinado`:* plazo y prórrogas. Efectos de la terminación sobre el stock pendiente y sobre las operaciones en curso.
7. **Clientela a la extinción**: tratamiento expreso de la eventual compensación por clientela, con explicación de que su procedencia se discute caso por caso y de que el silencio del contrato no garantiza su exclusión.
8. **Responsabilidad, ley aplicable y fuero**: régimen de responsabilidad, ley aplicable, sumisión y, en su caso, arbitraje.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
El contrato ha sido generado y actualizado en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una cláusula (objeto, precio, duración, territorio o terminación).
2. Añadir cláusulas opcionales (no competencia, penalizaciones, niveles de servicio, seguro).
3. Añadir el anexo de encargado del tratamiento de datos personales.
4. Revisar la coherencia global y realizar control de calidad previo a la firma.
5. Dar el contrato por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT:** el contrato es un borrador preparatorio; debe ser revisado por un abogado antes de su firma.
2. **Agencia: derechos irrenunciables.** La indemnización por clientela y el preaviso mínimo son de régimen imperativo y no pueden pactarse en perjuicio del agente. Una cláusula de renuncia anticipada es ineficaz.
3. **Distribución: no hay ley propia.** Al no existir una regulación específica, lo que no diga el contrato lo decidirá un juez por analogía o por buena fe. Conviene regular expresamente preaviso, stock y clientela.
4. **Laboralidad.** Si el colaborador trabaja con horario, medios e instrucciones del empresario y sin organización propia, la relación puede calificarse como laboral, con las consecuencias correspondientes. Si además concentra en un solo cliente la mayor parte de sus ingresos, puede ser trabajador autónomo económicamente dependiente, con régimen propio.
5. **Plazos de pago.** La normativa de morosidad limita el plazo de pago entre empresas y sanciona los pactos que lo excedan. Los intereses de demora se devengan automáticamente.
6. **Protección de datos.** Si el prestador accede a datos personales, el contrato de encargado del tratamiento no es opcional: su ausencia es por sí misma una infracción.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias antes de citar preceptos, plazos o cuantías. No afirmar que la indemnización por clientela se aplica automáticamente a la distribución.
2. **Cero Invención de Datos:** prohibido inventar razones sociales, CIF, datos registrales, precios, comisiones o territorios. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas o doctrinales en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
4. **Límites de Alcance:** no redactar contratos con consumidores, contratos de trabajo, contratos financieros o de seguro, ni condiciones generales predispuestas para su imposición a una pluralidad de adherentes, que deben derivarse al plugin o al profesional competente.
