---
name: derecho-civil-apelacion-y-medidas-cautelares
description: >
  Genera los escritos de segunda instancia y de tutela cautelar del proceso civil conforme a la **Ley
  1/2000 de Enjuiciamiento Civil**, que regula el recurso de apelacion y su oposicion (Arts. 455 a
  465) y las medidas cautelares con sus presupuestos y su caucion (Arts. 721 a 747), y al **Codigo
  Civil** en cuanto al derecho material que se invoca.


  Genera tres documentos: el recurso de apelacion contra la sentencia de primera instancia, el escrito
  de oposicion al recurso interpuesto de contrario con su eventual impugnacion, y la solicitud de
  medidas cautelares con su ofrecimiento de caucion.


  Computa el plazo de veinte dias habiles para interponer la apelacion y el de diez para oponerse,
  distingue los tres motivos utiles del recurso (infraccion procesal, error en la valoracion de la
  prueba e infraccion sustantiva), advierte del deposito para recurrir y de la ejecucion provisional
  de la sentencia recurrida, y en la via cautelar acredita la apariencia de buen derecho, el peligro
  por la mora procesal y la proporcionalidad de la medida.


  NO usar para el recurso de casacion ni para el recurso extraordinario por infraccion procesal, que
  exigen requisitos de acceso propios, ni para recursos en el orden social, penal o
  contencioso-administrativo, ni para la ejecucion de la sentencia firme.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Ley 1/2000 de Enjuiciamiento Civil](https://www.boe.es/buscar/act.php?id=BOE-A-2000-323) y
  [Codigo Civil](https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763).
when_to_use: |
  - Al usuario le han desestimado la demanda o le han estimado parcialmente y quiere recurrir.
  - La parte contraria ha recurrido la sentencia y hay que oponerse al recurso.
  - El usuario quiere impugnar tambien la sentencia al oponerse al recurso de la otra parte.
  - El usuario necesita asegurar el resultado del pleito antes de que termine (embargo preventivo, anotacion de demanda).
  - El usuario pregunta cuanto tiempo tiene para recurrir una sentencia civil.
  - El usuario pregunta si la sentencia recurrida se puede ejecutar mientras se resuelve el recurso.
inputs:
  - documento: recurso de apelacion / oposicion al recurso / medidas cautelares (V1)
  - posicion: apelante / apelado (V2)
  - momento_cautelar: con la demanda o durante el proceso / antes de la demanda (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_partes: identidad, NIF y domicilio de las partes, procurador y letrado de cada una
  - datos_procedimiento: juzgado, numero de autos, clase de juicio, cuantia y objeto del pleito
  - datos_resolucion: fecha de la sentencia, fallo, fecha de su notificacion y pronunciamiento sobre costas
  - motivos_recurso: infracciones procesales, errores en la valoracion de la prueba e infracciones sustantivas
  - prueba_controvertida: documentos y pruebas cuya valoracion se discute, con su folio en autos
  - pretension_recurso: pronunciamiento que se solicita del tribunal de apelacion
  - medida_solicitada: medida cautelar concreta que se pide y bien o actividad sobre la que recae
  - fundamento_cautelar: apariencia de buen derecho, peligro por la mora y proporcionalidad
  - caucion_ofrecida: tipo e importe de la caucion que se ofrece
outputs:
  - recurso_apelacion: recurso de apelacion contra sentencia civil, DRAFT
  - oposicion_recurso_apelacion: escrito de oposicion y, en su caso, de impugnacion, DRAFT
  - solicitud_medidas_cautelares: solicitud de medidas cautelares con ofrecimiento de caucion, DRAFT
  - checklist_plazos_y_deposito: computo de plazos, deposito para recurrir y efectos de la ejecucion provisional
references:
  - references/lec-apelacion-motivos-y-plazos.md
  - references/lec-medidas-cautelares-y-caucion.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/template-recurso-apelacion-civil.md
  - assets/template-oposicion-recurso-apelacion.md
  - assets/template-solicitud-medidas-cautelares.md
---

# Apelación Civil y Medidas Cautelares

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `recurso_apelacion` | `oposicion_apelacion` | `medidas_cautelares` | `casacion`.
- **V2 (Posición Procesal):** `apelante` | `apelado`.
- **V3 (Momento de la Medida Cautelar):** `con_demanda` | `antes_de_demanda`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar el escrito procesal y la posición del cliente.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un abogado de despacho (de usted), confirmando el escrito que vais a preparar y advirtiendo en una línea de que los plazos procesales son perentorios.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca qué escrito necesita, si recurre o se opone, y la fecha de notificación de la sentencia, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), la posición procesal (`V2`) o el momento de la medida cautelar (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar el escrito procesal que corresponde.",
      "question": "¿Qué escrito necesita preparar?",
      "options": [
        {"id": "recurso_apelacion", "label": "Recurso de apelación contra la sentencia de primera instancia"},
        {"id": "oposicion_apelacion", "label": "Oposición al recurso de apelación de la parte contraria"},
        {"id": "medidas_cautelares", "label": "Solicitud de medidas cautelares (embargo preventivo, anotación de demanda, otras)"},
        {"id": "casacion", "label": "Recurso de casación o extraordinario por infracción procesal ante el Tribunal Supremo"}
      ]
    },
    {
      "id": "posicion",
      "rationale": "Resolver V2: la estrategia y la carga argumental cambian segun se recurra o se defienda la sentencia.",
      "question": "¿En qué posición está su cliente respecto de la sentencia?",
      "options": [
        {"id": "apelante", "label": "Le perjudica la sentencia y quiere recurrirla"},
        {"id": "apelado", "label": "Le favorece la sentencia y quiere defenderla"}
      ]
    },
    {
      "id": "momento_cautelar",
      "rationale": "Resolver V3: la medida solicitada antes de la demanda exige urgencia y obliga a presentarla en veinte dias.",
      "question": "Si necesita medidas cautelares, ¿el pleito ya está iniciado o hay que pedirlas antes de demandar?",
      "options": [
        {"id": "con_demanda", "label": "Con la demanda o con el proceso ya iniciado"},
        {"id": "antes_de_demanda", "label": "Antes de presentar la demanda, por urgencia"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `posicion`
- `V3` — `momento_cautelar`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = casacion`:**
  - **DETENER.** Informar de que el recurso de casación y el extraordinario por infracción procesal tienen requisitos de acceso propios y muy estrictos, con exigencias de interés casacional, plazos y forma tasados, y que su preparación exige análisis especializado de la jurisprudencia. Derivar a abogado especialista en recursos ante el Tribunal Supremo. No crear documento.
- **Si `V1 = recurso_apelacion`:**
  - Plantilla del sistema: `assets/template-recurso-apelacion-civil.md`. Proceder a la **Fase 2**.
- **Si `V1 = oposicion_apelacion`:**
  - Plantilla del sistema: `assets/template-oposicion-recurso-apelacion.md`. Proceder a la **Fase 2**.
- **Si `V1 = medidas_cautelares`:**
  - Plantilla del sistema: `assets/template-solicitud-medidas-cautelares.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina la carga argumental del escrito y si procede la impugnación de la sentencia al oponerse.
- `V3` no elige plantilla: determina si se incorpora la justificación de la urgencia y el compromiso de presentar la demanda en el plazo legal.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `lec-apelacion-motivos-y-plazos.md`, `lec-medidas-cautelares-y-caucion.md` y `estilo-redaccion-escritos.md`.
2. **Cómputo del plazo como primera tarea:** solicita la fecha de notificación de la sentencia y calcula el vencimiento en días hábiles. Si el plazo ha vencido, **dilo de inmediato** antes de redactar nada.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal, Plazos y Riesgos:**
   - Para la apelación: comunicar el plazo de **veinte días hábiles** desde la notificación para interponer el recurso ante el mismo tribunal que dictó la sentencia, la exigencia del **depósito para recurrir** y su acreditación, y la advertencia de que la sentencia recurrida puede ser objeto de **ejecución provisional** por la parte favorecida.
   - Explicar los tres motivos útiles: infracción de normas o garantías procesales con indefensión, error en la valoración de la prueba, e infracción de normas sustantivas; y advertir de que en apelación **no cabe introducir pretensiones nuevas** ni, salvo los supuestos legales, prueba nueva.
   - Para la oposición: comunicar el plazo de **diez días** desde el traslado, y la posibilidad de **impugnar** la sentencia en ese mismo escrito respecto de los pronunciamientos que perjudiquen al apelado.
   - Para las medidas cautelares: explicar los tres presupuestos (apariencia de buen derecho, peligro por la mora procesal y proporcionalidad), la exigencia de **caución** y el régimen de la responsabilidad por los daños si la medida se alza. *Condicional `V3 = antes_de_demanda`:* advertir de que la medida obtenida antes de la demanda queda sin efecto si la demanda no se presenta en el plazo legal de veinte días.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Nombrar por su ruta la plantilla **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
- **Si `origen_plantilla = plantilla_sistema`:** utiliza el asset enrutado y avanza a la **Fase 3**.
- **Si `origen_plantilla = plantilla_usuario`:** toma la plantilla adjunta en `<attached_documents>` o el texto pegado en `<user_message>`, verifica que no introduzca pretensiones nuevas en apelación, que no omita el depósito ni la identificación precisa de los pronunciamientos que se impugnan, y que en la vía cautelar no falte el ofrecimiento de caución, advierte en el chat y propón la redacción válida, y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en el workspace del usuario, con el nombre `recurso_apelacion.md`, `oposicion_recurso_apelacion.md` o `solicitud_medidas_cautelares.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos de la clasificación y de la escucha activa, incluidas la fecha del sistema y las fechas límite calculadas. Todos los datos pendientes permanecen como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves. PROHIBIDO dejar archivos en blanco o con notas resumidas.
2. **Validación de Disco (`read_file`):** ejecuta `read_file` sobre el archivo creado para confirmar su integridad.
3. **Confirmación en Chat:** informa al usuario de la ruta del archivo generado e introduce de inmediato la primera sección de la **Fase 4** sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques. Para cada bloque, ejecuta estrictamente el ciclo interactivo:
```
[Anuncio de la sección + Pregunta] --> [Vista Previa en texto plano] --> [¿Confirmamos esta sección?] --> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Anuncio y Pregunta en Chat:** anuncia la sección sustantiva con una frase breve en registro jurídico-procesal (por ejemplo, *"Pasamos ahora al error en la valoración de la prueba"*) y, en el mismo mensaje, formula ya la primera pregunta. No pidas permiso para pasar de sección: informa y continúa.
2. **Búsqueda prioritaria de partes e intervinientes (MANDATORIO con `search_clients` — MÁXIMA PRIORIDAD):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** antes de solicitar datos al usuario o llamar a formularios, conforme a la regla global `REG-CLI-01` de `CLAUDE.md`. Solo si `search_clients` devuelve 0 resultados o si tras recuperar la ficha faltan campos puntuales, invocarás `slot_filling_request` exclusivamente para los campos pendientes.
   - **Datos estructurados no de cliente agrupados (`slot_filling_request`, MANDATORIO):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
3. **Vista Previa (Preview):** muestra el texto redactado en texto plano, sin backticks de código.
4. **Confirmación:** pregunta literalmente: `¿Confirmamos esta sección?`.
5. **Persistencia en Disco:** tras la confirmación, aplica `edit_file` con coincidencia exacta y verifica inmediatamente con `read_file`.
6. **Validación de sentido, no solo de formato:** comprueba que la fecha de notificación es anterior a la del escrito y que el plazo no ha vencido, que cada motivo del recurso identifica el pronunciamiento concreto que combate, que las pruebas citadas constan en autos con su folio y que la medida cautelar solicitada es idónea y proporcionada respecto de la pretensión principal. Si un motivo pretende introducir una cuestión nueva no debatida en primera instancia, **advierte de su inadmisibilidad antes de volcarlo**.

### Hoja de Ruta de Secciones — RAMA RECURSO DE APELACIÓN:

1. **Encabezamiento, partes y procedimiento** *(confirmación agrupada)*: tribunal, número de autos, clase de juicio, identidad de las partes y de su representación y defensa, y determinación de la resolución que se recurre.
2. **Cumplimiento de los requisitos de admisión**: fecha de notificación de la sentencia, cómputo del plazo con su fecha límite, acreditación del **depósito para recurrir** y, en su caso, de la tasa que proceda.
3. **Antecedentes**: síntesis de lo pedido en la demanda o en la contestación, de la prueba practicada y del fallo, con identificación precisa de los pronunciamientos que se combaten y de los que se aceptan.
4. **Motivo primero: infracción de normas o garantías procesales**: *Condicional concurrencia:* norma infringida, actuación en que se produjo, indefensión causada y constancia de la denuncia oportuna en la instancia.
5. **Motivo segundo: error en la valoración de la prueba**: identificación del documento o medio probatorio con su folio en autos, contraste con lo declarado probado por la sentencia, y explicación de por qué la valoración es ilógica, arbitraria o contraria a las reglas de la sana crítica.
6. **Motivo tercero: infracción de normas sustantivas**: precepto infringido, interpretación que se defiende, y su aplicación a los hechos declarados probados.
7. **Costas y pronunciamientos accesorios**: impugnación del pronunciamiento sobre costas, intereses y, en su caso, de la denegación de pruebas.
8. **Petición y otrosí**: pronunciamiento concreto que se solicita del tribunal de apelación, solicitud de vista si procede, prueba en segunda instancia en los supuestos legalmente admitidos, y solicitud de suspensión de la ejecución provisional cuando proceda.

### Hoja de Ruta de Secciones — RAMA OPOSICIÓN AL RECURSO:

1. **Encabezamiento, partes y traslado recibido** *(confirmación agrupada)*: identificación del procedimiento, de la resolución recurrida y del recurso al que se responde, con la fecha del traslado y el cómputo del plazo de diez días.
2. **Posición general**: defensa del acierto de la sentencia, con exposición sintética de por qué su razonamiento es correcto.
3. **Oposición motivo por motivo**: rebatir cada motivo del recurso con el mismo orden, señalando cuando el apelante pretende una nueva valoración de la prueba sin acreditar error patente, cuando introduce cuestiones nuevas no debatidas y cuando no denunció en la instancia la infracción procesal que ahora alega.
4. **Impugnación de la sentencia**: *Condicional pronunciamientos desfavorables al apelado:* impugnación de los pronunciamientos que le perjudican, con la misma estructura de motivos, aprovechando que la ley permite impugnar en el escrito de oposición.
5. **Costas y petición**: solicitud de desestimación íntegra del recurso con imposición de costas al apelante, y, en su caso, estimación de la impugnación formulada.

### Hoja de Ruta de Secciones — RAMA MEDIDAS CAUTELARES:

1. **Partes, procedimiento y medida solicitada** *(confirmación agrupada)*: identificación de solicitante y demandado, procedimiento en que se pide o que se va a iniciar, y **medida concreta** que se solicita con identificación del bien, cuenta o actividad sobre la que recae.
2. **Apariencia de buen derecho**: exposición de los indicios que permiten fundar un juicio provisional favorable a la pretensión principal, con la documentación que los acredita.
3. **Peligro por la mora procesal**: descripción de las situaciones concretas que impedirían o dificultarían la efectividad de la tutela si la medida no se adopta, con hechos objetivos (actos de disposición, insolvencia, deslocalización de bienes, riesgo de destrucción de prueba), evitando afirmaciones genéricas.
4. **Idoneidad y proporcionalidad**: justificación de que la medida es la menos gravosa e idónea para asegurar la efectividad de la sentencia, y de que no cabe una alternativa menos onerosa.
5. **Urgencia y momento**: *Condicional `V3 = antes_de_demanda`:* justificación de la urgencia que habilita a pedirla antes de la demanda, con el compromiso expreso de presentarla en el plazo legal de veinte días, y solicitud, en su caso, de adopción sin audiencia del demandado con exposición de las razones que la justifican.
6. **Caución**: tipo e importe de la caución que se ofrece, con su justificación en relación con la naturaleza de la pretensión y con los perjuicios que la medida podría causar.
7. **Petición y prueba**: petición de la medida con su alcance exacto, solicitud de vista, proposición de prueba y relación de documentos que se acompañan.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
El escrito ha sido generado y actualizado en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección (motivos, prueba, petición o caución).
2. Añadir un motivo adicional al recurso o a la oposición.
3. Preparar el escrito complementario (impugnación, solicitud de suspensión de la ejecución provisional).
4. Revisar la coherencia global y realizar control de calidad previo a la presentación.
5. Dar el escrito por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT:** el escrito es un borrador preparatorio; debe ser revisado y firmado por abogado colegiado, y presentado con la representación procesal que corresponda.
2. **Plazos perentorios:** veinte días hábiles para interponer la apelación desde la notificación de la sentencia, y diez para el escrito de oposición desde el traslado. Vencidos, la sentencia queda firme sin remedio.
3. **Depósito para recurrir:** su falta de constitución y acreditación impide la admisión del recurso, y es subsanable solo en los términos legalmente previstos. Verificarlo antes de presentar.
4. **Ejecución provisional:** la sentencia recurrida puede ejecutarse provisionalmente a instancia de la parte favorecida. Si conviene evitarlo, hay que oponerse a la ejecución provisional por el cauce y en el plazo propios, que corren en paralelo al recurso.
5. **Nada nuevo en apelación:** no cabe introducir pretensiones ni cuestiones que no se debatieron en la instancia, y la prueba en segunda instancia solo se admite en los supuestos legalmente tasados. Un recurso construido sobre cuestiones nuevas se inadmite en ese punto.
6. **Infracción procesal:** para alegarla es necesario haberla denunciado oportunamente en la instancia, cuando ello fuera posible. Sin esa denuncia previa, el motivo decae.
7. **Medidas cautelares:** exigen caución y generan responsabilidad por los daños causados si la medida se alza o la demanda se desestima. Si se obtienen antes de la demanda, esta debe presentarse en el plazo legal de veinte días o la medida queda sin efecto con imposición de costas y daños.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias antes de citar preceptos, plazos o importes de depósito. No citar artículos de memoria.
2. **Cómputo del plazo como paso bloqueante:** antes de redactar, calcular el plazo desde la notificación. Si ha vencido, comunicarlo con claridad y no redactar un recurso inadmisible sin advertirlo.
3. **Cero Invención de Datos:** prohibido inventar números de autos, fechas de notificación, folios de documentos o contenidos de la sentencia. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
4. **Cero Invención de Jurisprudencia:** está terminantemente prohibido citar sentencias, sus fechas o sus números de recurso sin haberlas verificado en una fuente consultada en la sesión. Si no se dispone de la cita, argumentar sin ella.
5. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
6. **Límites de Alcance:** no preparar recursos de casación ni extraordinarios por infracción procesal, ni recursos de otros órdenes jurisdiccionales, ni la ejecución de sentencia firme, que corresponden a otras skills o a profesional especializado.
