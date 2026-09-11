---
name: derecho-consumo-reclamacion-sectorial
description: >
  Genera las reclamaciones de consumo de los tres sectores con regimen propio y mayor volumen en
  Espana, conforme al **Real Decreto Legislativo 1/2007**, texto refundido de la Ley General para la
  Defensa de los Consumidores y Usuarios, que regula el derecho de desistimiento y la atencion de
  reclamaciones, y al **Reglamento (CE) 261/2004**, que fija la compensacion y asistencia a los
  pasajeros aereos en caso de denegacion de embarque, cancelacion y gran retraso.


  Genera tres documentos: la reclamacion a la compania aerea por vuelo cancelado, retrasado o embarque
  denegado con su escalado a la Agencia Estatal de Seguridad Aerea, la reclamacion en materia de
  suministros y telecomunicaciones (facturacion indebida, baja no atendida, portabilidad o
  permanencia) con su escalado al organismo sectorial, y la comunicacion de desistimiento de una
  compra a distancia con la solicitud de reembolso.


  Calcula la compensacion que corresponde por distancia de vuelo, distingue el retraso indemnizable de
  la circunstancia extraordinaria que exonera, computa el plazo de catorce dias naturales del
  desistimiento y su ampliacion cuando la empresa no informo del derecho, y en cada caso identifica el
  organismo que continua la reclamacion cuando la empresa no responde.


  NO usar para la reclamacion judicial de la cantidad, que corresponde a la skill de reclamacion de
  cantidad de derecho civil, ni para la nulidad de clausulas abusivas, ni para danos personales en
  accidente de transporte, ni para reclamaciones entre empresas, que no son relaciones de consumo.


  Normas aplicadas, en su texto consolidado:
  [Ley General para la Defensa de los Consumidores y Usuarios](https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555)
  en el BOE, y
  [Reglamento (CE) 261/2004](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32004R0261)
  en el Diario Oficial de la Union Europea.
when_to_use: |
  - Al usuario le han cancelado o retrasado un vuelo, o le han denegado el embarque, y quiere reclamar.
  - Al usuario le han perdido o danado el equipaje y pregunta que puede reclamar.
  - El usuario tiene una factura de luz, gas, agua, telefono o internet que considera indebida.
  - El usuario pidio la baja de un servicio y la empresa sigue facturando, o le reclaman penalizacion por permanencia.
  - El usuario ha comprado online y quiere devolverlo dentro del plazo de desistimiento.
  - El usuario reclamo a la empresa y no le han contestado, y pregunta a donde acudir ahora.
inputs:
  - documento: transporte aereo / suministros y telecomunicaciones / desistimiento de compra a distancia (V1)
  - modalidad_contratacion: a distancia u online / presencial (V2)
  - fase_reclamacion: primera reclamacion a la empresa / la empresa ya respondio o no contesto (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_consumidor: nombre y apellidos, NIF/NIE, domicilio, telefono y correo electronico
  - datos_empresa: razon social, CIF si se conoce, domicilio y direccion de atencion al cliente
  - datos_contrato: numero de contrato, de reserva, de linea o de pedido, y fecha de contratacion
  - hechos: descripcion de lo ocurrido con sus fechas, importes y comunicaciones previas
  - datos_vuelo: numero de vuelo, origen, destino, fecha, hora prevista y hora real, y motivo alegado por la compania
  - distancia_vuelo: distancia ortodromica entre origen y destino en kilometros
  - importes_reclamados: compensacion, reembolso, gastos acreditados e indemnizacion por danos
  - datos_pedido: fecha del pedido, fecha de recepcion, importe y medio de pago
  - prueba: billetes, facturas, tarjetas de embarque, capturas, partes de irregularidad y comunicaciones
outputs:
  - reclamacion_transporte_aereo: reclamacion a la compania aerea con escalado a la Agencia Estatal de Seguridad Aerea, DRAFT
  - reclamacion_suministros: reclamacion de suministros y telecomunicaciones con escalado sectorial, DRAFT
  - comunicacion_desistimiento: comunicacion de desistimiento de compra a distancia con solicitud de reembolso, DRAFT
  - checklist_plazos_y_organismos: plazos aplicables, organismo competente en cada fase y prueba a conservar
references:
  - references/transporte-aereo-compensacion-y-aesa.md
  - references/desistimiento-suministros-y-organismos-sectoriales.md
  - references/estilo-redaccion-reclamaciones.md
assets:
  - assets/template-reclamacion-transporte-aereo.md
  - assets/template-reclamacion-suministros-telecomunicaciones.md
  - assets/template-desistimiento-compra-online.md
---

# Reclamaciones de Consumo Sectoriales (Vuelos, Suministros y Desistimiento)

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para preparar su reclamación de consumo.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `transporte_aereo` | `suministros_telecomunicaciones` | `desistimiento_compra` | `reclamacion_judicial`.
- **V2 (Modalidad de Contratación):** `a_distancia` | `presencial`.
- **V3 (Fase de la Reclamación):** `primera_reclamacion` | `empresa_ya_respondio`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar el sector y la fase de la reclamación.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un abogado de despacho (de usted), confirmando que vais a preparar su reclamación.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca el sector, cómo contrató y si ya reclamó a la empresa, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), la modalidad de contratación (`V2`) o la fase (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar el sector y su regimen y organismo propios.",
      "question": "¿Sobre qué es su reclamación?",
      "options": [
        {"id": "transporte_aereo", "label": "Un vuelo: cancelación, retraso, embarque denegado o equipaje"},
        {"id": "suministros_telecomunicaciones", "label": "Luz, gas, agua, teléfono o internet: facturas, baja o permanencia"},
        {"id": "desistimiento_compra", "label": "Devolver una compra hecha por internet o a distancia"},
        {"id": "reclamacion_judicial", "label": "Ya agoté la vía con la empresa y quiero demandar judicialmente"}
      ]
    },
    {
      "id": "modalidad_contratacion",
      "rationale": "Resolver V2: el derecho de desistimiento solo nace en la contratacion a distancia o fuera de establecimiento.",
      "question": "¿Cómo contrató o compró?",
      "options": [
        {"id": "a_distancia", "label": "Por internet, teléfono o fuera del establecimiento"},
        {"id": "presencial", "label": "En una tienda u oficina físicamente"}
      ]
    },
    {
      "id": "fase_reclamacion",
      "rationale": "Resolver V3: el escalado al organismo sectorial exige acreditar la reclamacion previa a la empresa.",
      "question": "¿Ha reclamado ya a la empresa?",
      "options": [
        {"id": "primera_reclamacion", "label": "No, esta es la primera reclamación"},
        {"id": "empresa_ya_respondio", "label": "Sí: me respondieron negativamente o no me han contestado"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `modalidad_contratacion`
- `V3` — `fase_reclamacion`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = reclamacion_judicial`:**
  - **DETENER.** Informar de que la reclamación judicial de la cantidad se prepara con la skill de reclamación de cantidad del plugin de derecho civil, que elige la vía procesal según la cuantía, y de que antes conviene acreditar el intento de solución extrajudicial. Derivar a esa skill. No crear documento.
- **Si `V1 = transporte_aereo`:**
  - Plantilla del sistema: `assets/template-reclamacion-transporte-aereo.md`. Proceder a la **Fase 2**.
- **Si `V1 = suministros_telecomunicaciones`:**
  - Plantilla del sistema: `assets/template-reclamacion-suministros-telecomunicaciones.md`. Proceder a la **Fase 2**.
- **Si `V1 = desistimiento_compra`:**
  - Plantilla del sistema: `assets/template-desistimiento-compra-online.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina si existe derecho de desistimiento y su plazo, y las menciones sobre información precontractual.
- `V3` no elige plantilla: determina si el escrito se dirige a la empresa o si incorpora el escalado al organismo sectorial con la acreditación de la reclamación previa.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `transporte-aereo-compensacion-y-aesa.md`, `desistimiento-suministros-y-organismos-sectoriales.md` y `estilo-redaccion-reclamaciones.md`.
2. Opcionalmente verifica mediante `web_search` la sede y el formulario vigente del organismo sectorial competente (Agencia Estatal de Seguridad Aérea, oficina de atención al usuario de telecomunicaciones, organismo autonómico de energía o de consumo). Aplica la redacción vigente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal, Cuantías y Plazos:**
   - Para transporte aéreo: explicar que la compensación es una cantidad **fija por tramos de distancia**, independiente del precio del billete, que se devenga por cancelación, embarque denegado y retraso relevante en la llegada, y que la compañía se libera si acredita una circunstancia extraordinaria. Explicar además el derecho a reembolso o transporte alternativo y a la asistencia (comida, comunicación y alojamiento) como derechos distintos y acumulables a la compensación.
   - Para suministros y telecomunicaciones: explicar que la reclamación a la empresa es **previa y obligatoria**, que la empresa dispone de un plazo para responder y que, transcurrido sin respuesta satisfactoria, se abre el escalado al organismo sectorial, con un plazo propio que conviene no dejar pasar.
   - Para desistimiento: explicar que el plazo es de **catorce días naturales** desde la recepción del bien, que no hay que motivar la decisión, que los gastos de devolución solo corren a cargo del consumidor si la empresa lo informó previamente, que el reembolso debe practicarse en catorce días naturales, y que si la empresa no informó del derecho el plazo se amplía sustancialmente.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Nombrar por su ruta la plantilla **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
- **Si `origen_plantilla = plantilla_sistema`:** utiliza el asset enrutado y avanza a la **Fase 3**.
- **Si `origen_plantilla = plantilla_usuario`:** toma la plantilla adjunta en `<attached_documents>` o el texto pegado en `<user_message>`, verifica que no renuncie a derechos irrenunciables del consumidor ni acepte importes inferiores a los que legalmente corresponden, advierte en el chat y propón la redacción válida, y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en el workspace del usuario, con el nombre `reclamacion_transporte_aereo.md`, `reclamacion_suministros.md` o `comunicacion_desistimiento.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos de la clasificación y de la escucha activa, incluida la fecha del sistema y el cómputo de plazos. Todos los datos pendientes permanecen como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves. PROHIBIDO dejar archivos en blanco o con notas resumidas.
2. **Validación de Disco (`read_file`):** ejecuta `read_file` sobre el archivo creado para confirmar su integridad.
3. **Confirmación en Chat:** informa al usuario de la ruta del archivo generado e introduce de inmediato la primera sección de la **Fase 4** sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques. Para cada bloque, ejecuta estrictamente el ciclo interactivo:
```
[Anuncio de la sección + Pregunta] --> [Vista Previa en texto plano] --> [¿Confirmamos esta sección?] --> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Anuncio y Pregunta en Chat:** anuncia la sección sustantiva con una frase breve en registro jurídico (por ejemplo, *"Pasamos ahora a cuantificar lo que le corresponde"*) y, en el mismo mensaje, formula ya la primera pregunta. No pidas permiso para pasar de sección: informa y continúa.
2. **Búsqueda prioritaria de partes e intervinientes (MANDATORIO con `search_clients` — MÁXIMA PRIORIDAD):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** antes de solicitar datos al usuario o llamar a formularios, conforme a la regla global `REG-CLI-01` de `CLAUDE.md`. Solo si `search_clients` devuelve 0 resultados o si tras recuperar la ficha faltan campos puntuales, invocarás `slot_filling_request` exclusivamente para los campos pendientes.
   - **Datos estructurados no de cliente agrupados (`slot_filling_request`, MANDATORIO):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
3. **Vista Previa (Preview):** muestra el texto redactado en texto plano, sin backticks de código.
4. **Confirmación:** pregunta literalmente: `¿Confirmamos esta sección?`.
5. **Persistencia en Disco:** tras la confirmación, aplica `edit_file` con coincidencia exacta y verifica inmediatamente con `read_file`.
6. **Validación de sentido, no solo de formato:** comprueba que la fecha del vuelo o del pedido es anterior a la de la reclamación, que la compensación reclamada corresponde al tramo de distancia, que el plazo de desistimiento no ha vencido y que los importes suman lo que se pide. Si el plazo ya venció o el derecho no procede, **dilo con claridad antes de seguir redactando**.

### Hoja de Ruta de Secciones — RAMA TRANSPORTE AÉREO:

1. **Pasajero y compañía** *(confirmación agrupada)*: identidad, NIF, domicilio, teléfono y correo del pasajero y de los demás pasajeros de la misma reserva; razón social y dirección de atención al cliente de la compañía.
2. **Datos del vuelo y de la incidencia**: número de vuelo, localizador de la reserva, origen y destino, fecha, hora prevista y hora real de salida y de llegada, y motivo alegado por la compañía.
3. **Calificación de la incidencia y compensación**: determinación de si se trata de cancelación, embarque denegado o retraso relevante en la llegada, cálculo de la distancia y del tramo aplicable, e importe de la compensación por pasajero. Análisis de la circunstancia extraordinaria alegada y de su insuficiencia cuando proceda.
4. **Derechos adicionales**: reembolso o transporte alternativo, asistencia recibida o denegada (comida, comunicaciones, alojamiento y transporte), y gastos acreditados que se reclaman.
5. **Equipaje**: *Condicional incidencia de equipaje:* referencia al parte de irregularidad emitido en el aeropuerto, naturaleza del daño, pérdida o retraso, y advertencia de los plazos breves y del régimen de límites indemnizatorios del convenio internacional aplicable.
6. **Petición, plazo de respuesta y escalado**: cuantificación total, cuenta para el pago, plazo que se concede a la compañía y, *Condicional `V3 = empresa_ya_respondio`*, escalado a la Agencia Estatal de Seguridad Aérea con la acreditación de la reclamación previa y la advertencia de que su informe no es vinculante.

### Hoja de Ruta de Secciones — RAMA SUMINISTROS Y TELECOMUNICACIONES:

1. **Usuario y empresa** *(confirmación agrupada)*: identidad, NIF, domicilio de suministro y de notificaciones, teléfono y correo; razón social de la empresa y su servicio de atención al cliente.
2. **Contrato y servicio afectado**: número de contrato, de póliza, de línea o de referencia de suministro, fecha de contratación, servicio contratado y condiciones pactadas relevantes.
3. **Hechos y comunicaciones previas**: cronología con fechas, importes facturados y discutidos, números de incidencia o de reclamación asignados por la empresa, y contenido de las respuestas recibidas.
4. **Fundamento de la reclamación**: identificación del incumplimiento (facturación de servicios no prestados, subida no comunicada, baja solicitada y no atendida, penalización por permanencia no informada, portabilidad defectuosa, avería no reparada) y del derecho del usuario que se invoca.
5. **Petición**: rectificación de la facturación, devolución de lo indebidamente cobrado, baja efectiva con fecha, anulación de la penalización, indemnización o compensación automática cuando el sector la prevea, y plazo de respuesta.
6. **Escalado sectorial**: *Condicional `V3 = empresa_ya_respondio`:* identificación del organismo competente según el sector y el territorio, con la acreditación de la reclamación previa, la fecha en que se formuló y el plazo transcurrido sin respuesta satisfactoria.

### Hoja de Ruta de Secciones — RAMA DESISTIMIENTO DE COMPRA A DISTANCIA:

1. **Consumidor y empresa** *(confirmación agrupada)*: identidad, NIF, domicilio, teléfono y correo del consumidor; razón social, CIF y dirección de la empresa vendedora.
2. **Pedido y cómputo del plazo**: número de pedido, fecha del pedido, fecha de recepción del bien o de celebración del contrato de servicio, importe total y medio de pago; cómputo expreso de los catorce días naturales y fecha límite. *Condicional falta de información del derecho:* invocación de la ampliación del plazo.
3. **Declaración de desistimiento**: manifestación inequívoca de desistir, sin necesidad de motivación, con referencia al bien o servicio afectado.
4. **Devolución del bien y gastos**: forma y plazo de devolución, quién asume los gastos de devolución según la información precontractual recibida, y estado en que se devuelve el bien.
5. **Reembolso y advertencias**: solicitud de reembolso íntegro del precio y de los gastos de entrega estándar en el plazo legal de catorce días naturales, por el mismo medio de pago, con advertencia de las excepciones legales al desistimiento cuando alguna pudiera concurrir.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
La reclamación ha sido generada y actualizada en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección (hechos, cuantificación o petición).
2. Añadir otro pasajero, otra línea o otro pedido a la misma reclamación.
3. Preparar el escalado al organismo sectorial competente.
4. Revisar la coherencia global y realizar control de calidad previo al envío.
5. Dar la reclamación por finalizada y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT:** el escrito es un borrador preparatorio; debe ser revisado por un profesional antes de su envío.
2. **Prueba del envío:** conviene remitir la reclamación por un medio que deje constancia (formulario con acuse, correo electrónico con confirmación de lectura o burofax). Sin prueba del envío, el escalado posterior se complica.
3. **Reclamación previa obligatoria:** los organismos sectoriales y las administraciones de consumo exigen acreditar que se reclamó antes a la empresa y que esta no respondió satisfactoriamente. Conservar el número de incidencia que la empresa asigne.
4. **Naturaleza del pronunciamiento:** los informes de los organismos sectoriales y las resoluciones de consumo no siempre son vinculantes ni ejecutivas. Si la empresa no cumple, la vía siguiente es la judicial o el arbitraje de consumo cuando la empresa esté adherida.
5. **Plazos:** el desistimiento tiene un plazo perentorio de catorce días naturales; las incidencias de equipaje tienen plazos muy breves; las acciones de reclamación de cantidad tienen su propio plazo de prescripción. Vencidos, el derecho se pierde o su reclamación se dificulta gravemente.
6. **Acumulación de derechos:** en transporte aéreo, la compensación, el reembolso o transporte alternativo y la asistencia son derechos distintos: aceptar un vale o una gestión comercial no implica renunciar a la compensación, y conviene no firmar renuncias.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias antes de citar cuantías, plazos u organismos. No inventar importes de compensación distintos de los tramos legalmente establecidos.
2. **Cero Invención de Datos:** prohibido inventar números de vuelo, localizadores, números de contrato, importes o fechas. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **Condición de consumidor:** comprobar que el usuario actúa como consumidor. Si contrató en el marco de su actividad empresarial o profesional, advertir de que no le amparan los derechos de consumo y derivar al cauce contractual o mercantil.
4. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
5. **Límites de Alcance:** no preparar demandas judiciales, ni reclamaciones por daños personales derivados de accidente de transporte, ni reclamaciones entre empresas, que deben derivarse al plugin o al profesional competente.
