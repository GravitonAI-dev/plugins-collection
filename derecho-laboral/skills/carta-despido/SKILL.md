---
name: carta-despido
description: >
  Genera la comunicación escrita de extinción del contrato de trabajo por decisión del empresario en
  sus cuatro modalidades individuales: despido disciplinario (artículo 54 del Estatuto de los
  Trabajadores), despido objetivo (artículos 52 y 53), desistimiento durante el periodo de prueba
  (artículo 14) y comunicación de finalización de contrato temporal (artículo 49.1.c). Aplica el texto
  refundido del Estatuto de los Trabajadores aprobado por Real Decreto Legislativo 2/2015 y la Ley
  36/2011 reguladora de la Jurisdicción Social, en sus versiones consolidadas vigentes verificadas en
  el BOE, y contrasta siempre el régimen disciplinario y los preavisos del convenio colectivo
  aplicable. Metodología: clasificación inicial de la modalidad y la causa mediante formulario
  interactivo, plan de acción con el cálculo desglosado de indemnización y plazos, creación del
  documento base en el workspace y edición incremental apartado a apartado. NO usar para despido
  colectivo (artículo 51), suspensión o reducción de jornada (artículo 47), extinción por voluntad del
  trabajador (artículos 49.1.d y 50), extinción por mutuo acuerdo, jubilación, ni para relaciones
  laborales especiales como alta dirección o empleados de hogar.
when_to_use: |
  - El usuario quiere redactar una carta de despido disciplinario por incumplimiento del trabajador.
  - El usuario quiere redactar un despido objetivo por ineptitud, falta de adaptación o causas económicas, técnicas, organizativas o de producción.
  - El usuario quiere comunicar la no superación del periodo de prueba o la finalización de un contrato temporal.
  - El usuario aporta datos de empresa y trabajador y describe hechos, causas o fechas de efectos de una extinción contractual.
  - El usuario pide que la comunicación cumpla los requisitos de forma del Estatuto de los Trabajadores.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - modalidad_extintiva: disciplinario / objetivo / periodo de prueba / fin de contrato temporal
  - causa_concreta: apartado del artículo 54.2 o del artículo 52 en que se funda la decisión
  - naturaleza_empleador: persona física o persona jurídica
  - garantias_trabajador: representante legal o sindical / situación de especial protección / ninguna
  - datos_empresa: razón social, CIF, domicilio, código de cuenta de cotización, representante y cargo
  - datos_trabajador: nombre, DNI o NIE, domicilio, número de afiliación a la Seguridad Social
  - datos_relacion_laboral: fecha de antigüedad, categoría o grupo profesional, tipo de contrato, jornada, salario bruto anual con prorrateo de pagas
  - convenio_colectivo: denominación, ámbito y código de convenio aplicable
  - hechos_imputados: relato concreto, fechado e individualizado de cada incumplimiento (solo disciplinario)
  - causa_objetiva: acreditación de la ineptitud, la falta de adaptación o la concurrencia de causas empresariales (solo objetivo)
  - fecha_efectos: fecha en que la extinción produce efectos
  - indemnizacion: importe calculado y forma de puesta a disposición (solo objetivo y fin de contrato temporal)
outputs:
  - carta_extincion: comunicación escrita completa en markdown, DRAFT, con acuse de recibo y reserva de acciones
references:
  - references/fuentes-plantillas-validadas.md
  - references/et-despido-disciplinario-arts54-55.md
  - references/et-despido-objetivo-arts52-53.md
  - references/calculo-indemnizacion-y-salario-regulador.md
  - references/plazos-caducidad-y-calificacion.md
assets:
  - assets/template-carta-despido-disciplinario.md
  - assets/template-carta-despido-objetivo.md
  - assets/template-carta-no-superacion-periodo-prueba.md
  - assets/template-comunicacion-fin-contrato-temporal.md
---

# Generar la Comunicación de Extinción del Contrato de Trabajo

> DRAFT — para revisión por un abogado o graduado social colegiado antes de su firma y entrega. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

Para garantizar un enrutamiento determinista y el cumplimiento de los requisitos de forma imperativos, el asistente resuelve y mantiene internamente en memoria:

- **V1 (Modalidad extintiva):** `disciplinario` | `objetivo` | `periodo_prueba` | `fin_contrato_temporal` | `fuera_de_alcance`.
- **V2 (Causa concreta):** apartado del artículo 54.2 (disciplinario) o del artículo 52 (objetivo) del Estatuto de los Trabajadores. *(Inferido del relato del usuario y confirmado)*.
- **V3 (Naturaleza del empleador):** `persona_fisica` | `persona_juridica`.
- **V4 (Garantías reforzadas del trabajador):** `representante_legal` | `especial_proteccion` | `ninguna`.
- **V5 (Origen plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`, `V4`, `V5`) y los resúmenes de validación con marcas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural formal y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

Tu primer objetivo es clasificar con precisión la modalidad extintiva y las garantías aplicables.

### 1.1 Escucha Activa Previa
Antes de abrir formularios, analiza el mensaje inicial y la documentación aportada:
- Si el usuario ya ha identificado inequívocamente la modalidad, la causa y la condición del trabajador, regístralas en silencio y pasa a la **Fase 2**.
- Si resta algún vector por resolver, no formules preguntas abiertas en turnos sucesivos: presenta el formulario estructurado mediante `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "modalidad_extintiva",
      "rationale": "Resolver V1: cada modalidad tiene requisitos de forma, preaviso e indemnización distintos y no intercambiables.",
      "question": "¿Por qué motivo se extingue el contrato?",
      "options": [
        {"id": "disciplinario", "label": "Incumplimiento grave y culpable del trabajador (despido disciplinario)"},
        {"id": "objetivo", "label": "Ineptitud, falta de adaptación o causas económicas, técnicas, organizativas o de producción (despido objetivo)"},
        {"id": "periodo_prueba", "label": "No superación del periodo de prueba en curso"},
        {"id": "fin_contrato_temporal", "label": "Llegada del término del contrato temporal"},
        {"id": "fuera_de_alcance", "label": "Despido colectivo, baja voluntaria, mutuo acuerdo, jubilación u otra causa"}
      ]
    },
    {
      "id": "garantias_trabajador",
      "rationale": "Resolver V4: determina si es preceptivo el expediente contradictorio y si existe riesgo cualificado de nulidad.",
      "question": "¿Concurre en el trabajador alguna de estas circunstancias?",
      "options": [
        {"id": "representante_legal", "label": "Es representante legal de los trabajadores, delegado sindical o delegado de prevención"},
        {"id": "especial_proteccion", "label": "Embarazo, permiso por nacimiento o cuidado, reducción de jornada, excedencia por cuidado, víctima de violencia, o ha reclamado o denunciado recientemente"},
        {"id": "ninguna", "label": "Ninguna de las anteriores"}
      ]
    },
    {
      "id": "naturaleza_empleador",
      "rationale": "Resolver V3: fija la estructura de comparecencia y la representación en la carta.",
      "question": "¿Quién es el empleador?",
      "options": [
        {"id": "persona_juridica", "label": "Empresa, sociedad o entidad (persona jurídica)"},
        {"id": "persona_fisica", "label": "Empresario individual o particular (persona física)"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `modalidad_extintiva`
- `V3` — `naturaleza_empleador`
- `V4` — `garantias_trabajador`
- `V2` — no se pregunta en el formulario: se deriva durante el propio enrutamiento a partir de la norma aplicable y de los hechos que relate el usuario

### 1.3 Enrutamiento de Estado (Routing por Vectores)

* **Si `[V1 = fuera_de_alcance]` → Detener proceso.** Informa en el chat de que el despido colectivo (artículo 51), la suspensión de contratos (artículo 47), la extinción por voluntad del trabajador (artículos 49.1.d y 50) y el mutuo acuerdo se rigen por trámites propios con periodo de consultas o documentos distintos, quedando fuera del alcance de esta skill. Ofrece la derivación al profesional competente. **No crees documento.**
* **Si `[V4 = representante_legal]` → Parada obligatoria antes de continuar.** Advierte en el chat de que el artículo 55.1 del Estatuto de los Trabajadores exige la apertura de **expediente contradictorio previo** con audiencia del interesado y de los restantes miembros de la representación, y de que su omisión determina la improcedencia. Ofrece tramitar primero el pliego de cargos con la skill `sancion-disciplinaria`. Solo continúa si el usuario confirma que el expediente ya está instruido y concluido.
* **Si `[V4 = especial_proteccion]` → Advertencia obligatoria antes de continuar.** Explica en el chat que en estos supuestos el despido que no se declare procedente por acreditarse plenamente la causa es **nulo**, no improcedente (artículo 55.5 del Estatuto de los Trabajadores), con readmisión obligatoria, abono de salarios de tramitación y eventual indemnización adicional por daños. Recomienda la revisión por letrado antes de la entrega. Continúa solo si el usuario lo confirma.
* **Si `[V1 = disciplinario]` → Plantilla: `assets/template-carta-despido-disciplinario.md`.** Resuelve V2 identificando el apartado del artículo 54.2. Verifica en el convenio colectivo la tipificación y graduación de la falta y el plazo de prescripción de faltas del artículo 60.2 del Estatuto de los Trabajadores. Sin indemnización si se acredita la causa.
* **Si `[V1 = objetivo]` → Plantilla: `assets/template-carta-despido-objetivo.md`.** Resuelve V2 identificando el apartado del artículo 52. Requisitos acumulativos e inexcusables del artículo 53.1: comunicación escrita con expresión de la causa, puesta a disposición **simultánea** de la indemnización de 20 días por año con el tope de 12 mensualidades, y preaviso de 15 días.
* **Si `[V1 = periodo_prueba]` → Plantilla: `assets/template-carta-no-superacion-periodo-prueba.md`.** Verifica que el periodo de prueba conste **por escrito en el contrato**, que no haya expirado y que respete la duración máxima del convenio o, en su defecto, del artículo 14.1. Sin indemnización.
* **Si `[V1 = fin_contrato_temporal]` → Plantilla: `assets/template-comunicacion-fin-contrato-temporal.md`.** Verifica la modalidad contractual conforme al artículo 15 en la redacción dada por el Real Decreto-ley 32/2021, el preaviso de 15 días si la duración excede de un año y la indemnización de 12 días por año del artículo 49.1.c, que no procede en los contratos formativos ni en el de sustitución.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

En esta fase interactúas **directamente en el chat, en texto plano conversacional y sin formularios**.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto (carpeta `references/`).
2. Verifica con `web_search` la versión consolidada vigente del Estatuto de los Trabajadores en el BOE y localiza el convenio colectivo aplicable en el registro oficial correspondiente (REGCON estatal o registro autonómico o provincial), tomando de él la tipificación de faltas, la graduación de sanciones y los preavisos.
3. Si la modalidad es disciplinaria, verifica además el estado de la doctrina jurisprudencial sobre la **audiencia previa al trabajador** derivada del artículo 7 del Convenio 158 de la Organización Internacional del Trabajo antes de afirmar nada sobre ella en el chat.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Marco legal aplicable:** norma, artículos y convenio identificado, explicando el efecto de la clasificación obtenida.
2. **Cómputo del plazo y calendario de la operación:** fecha de efectos propuesta, preaviso exigible, y advertencia expresa de que el trabajador dispone de **20 días hábiles** desde la fecha de efectos para impugnar el despido (artículo 59.3 del Estatuto de los Trabajadores y artículo 103 LRJS), con conciliación previa obligatoria que suspende el cómputo.
3. **Cálculo económico preliminar desglosado**, cuando la modalidad conlleve indemnización, con la fórmula a la vista y la advertencia de que el importe definitivo depende del salario regulador acreditado.
4. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
5. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el texto íntegro del asset correspondiente desde el bloque `<document kind="assets-collection">` y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:**
  1. Accede al contenido desde `<attached_documents>` o el mensaje del usuario.
  2. **Guardrail de verificación:** analiza el texto aportado. Si carece de fecha de efectos, si las imputaciones son genéricas o no fechadas, si omite la puesta a disposición de la indemnización en un despido objetivo, o si contiene renuncias anticipadas de derechos, adviértelo expresamente en el chat y propón la redacción válida.
  3. Adopta la minuta revisada como base y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en un archivo del workspace con nombre en `snake_case.md`.
   - Aplica **Zero-Omission**: sustituye todos los datos ya resueltos por la clasificación y la escucha activa; deja como marcador con su nombre propio de plantilla (`{{razon_social_empresa: razón social}}`, `{{fecha_efectos: fecha (DD/MM/AAAA)}}`) los que resten.
   - PROHIBIDO dejar el archivo en blanco, con solo el título o con un resumen.
2. **Validación de integridad (`read_file`):** ejecuta `read_file` sobre el archivo recién creado y comprueba que el volcado es íntegro.
3. **Confirmación en chat y encadenamiento inmediato:** informa de la ruta absoluta y, en esa **misma respuesta**, abre la primera sección de la Fase 4 con su anuncio y su primera solicitud de datos, sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL APARTADO A APARTADO

### Protocolo Obligatorio de Edición
```
[Recogida de datos: slot_filling_request (grupos) / Chat (negociación)]
                          │
                          ▼
            [Vista previa en texto plano en CHAT]
                          │
                          ▼
          [Confirmación en CHAT: "¿Confirmamos esta sección?"]
                          │
                          ▼
                [edit_file + read_file en DISCO]
```

- **Datos estructurados agrupados (`slot_filling_request`, MANDATORIO):** todo grupo de datos identificativos —empresa, trabajador, relación laboral, importes, cuenta bancaria— se solicita en bloque mediante `slot_filling_request`. Queda prohibido pedirlos uno a uno en turnos sucesivos.
- **Validación de sentido, no solo de formato:** comprueba la coherencia interna de los datos (que la antigüedad sea anterior a la fecha de efectos, que el salario declarado sea compatible con la jornada y el convenio, que el DNI o CIF tenga formato válido). Si algo es incongruente, dialógalo en el chat antes de volcarlo.
- **Anuncio de sección (visible, sin pedir permiso aparte):** al cerrar una sección y antes de la primera solicitud de la siguiente, añade en el mismo mensaje el anuncio fijo de la sección, en tono de abogado y de usted, y continúa. No preguntes si se puede pasar de sección: informa y sigue.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a identificar a la empresa y al trabajador, así como el convenio colectivo de aplicación."
- Sección 2: "Identificadas las partes, corresponde precisar los datos de la relación laboral que se extingue."
- Sección 3: "Fijados los datos del contrato, procede concretar la causa de la extinción." *(En periodo de prueba y fin de contrato temporal: "Fijados los datos del contrato, procede concretar el fundamento de la comunicación.")*
- Sección 4: "Concretada la causa, corresponde fijar la fecha de efectos y el preaviso."
- Sección 5: "Determinada la fecha de efectos, procede liquidar los importes derivados de la extinción."
- Sección 6: "Por último, procede fijar la fórmula de entrega y acuse de recibo de la comunicación."

1. **Partes y convenio [dato objetivo].** Solicita en bloque mediante `slot_filling_request`: de la empresa, razón social o nombre, CIF o NIF, domicilio, código de cuenta de cotización y, si V3 es persona jurídica, nombre, NIF y cargo del representante que firma; del trabajador, nombre completo, DNI o NIE, domicilio a efectos de notificaciones y número de afiliación a la Seguridad Social. Pide también la denominación y el ámbito del convenio colectivo. Si el usuario no lo conoce, dedúcelo de la actividad y el domicilio y **verifícalo tú mismo con `web_search`** en el registro oficial, informando del resultado en la vista previa.
2. **Relación laboral [dato objetivo, con validación].** Solicita en bloque mediante `slot_filling_request`: fecha de antigüedad, modalidad contractual, categoría o grupo profesional, porcentaje de jornada y salario bruto anual con prorrateo de pagas extraordinarias. Calcula y muestra el **salario/día regulador** resultante, explicando en el chat que es la base de toda indemnización y que debe incluir el prorrateo de las pagas extraordinarias y los complementos de devengo superior al mes.
3. **Causa de la extinción [negociación — el apartado decisivo].**
   - *Si `[V1 = disciplinario]`:* solicita en el chat el **relato de hechos**. Exige, para cada hecho, fecha o periodo concreto, lugar, conducta descrita objetivamente y, si existen, medios de acreditación y advertencias o sanciones previas. Rechaza expresamente las fórmulas genéricas y explica el motivo: el artículo 105.2 LRJS impide alegar en juicio causas distintas de las consignadas en la carta, de modo que lo que no esté escrito no podrá probarse después. Comprueba la **prescripción de faltas** del artículo 60.2 del Estatuto de los Trabajadores —60 días desde que la empresa tuvo conocimiento y 6 meses desde su comisión, en las faltas muy graves— y advierte si algún hecho está prescrito. Encaja la conducta en el apartado del artículo 54.2 y en la falta tipificada del convenio, citando ambos.
   - *Si `[V1 = objetivo]`:* solicita la acreditación de la causa. En ineptitud sobrevenida (artículo 52.a), la ineptitud debe ser posterior a la colocación efectiva y no conocida ni conocible antes. En falta de adaptación (artículo 52.b), es preceptivo haber ofrecido un **curso de adaptación** con salario medio y esperar dos meses desde la modificación o el curso. En causas económicas, técnicas, organizativas o de producción (artículo 52.c), concreta y cuantifica la causa con datos objetivos —resultados, ventas, pedidos, cambios de proceso— y explica que la carta debe expresarla con detalle suficiente para permitir la defensa. Advierte de que si la medida afecta a varios trabajadores en periodos de 90 días deben comprobarse los umbrales del artículo 51.1 para descartar un despido colectivo encubierto.
   - *Si `[V1 = periodo_prueba]`:* verifica que el pacto conste por escrito en el contrato, su duración y que no haya expirado. Advierte de que el desistimiento no requiere causa, pero de que la decisión no puede fundarse en un motivo discriminatorio ni lesivo de derechos fundamentales, en cuyo caso sería nula. Por ello, **no consignes causa alguna** en la carta más allá de la no superación del periodo de prueba.
   - *Si `[V1 = fin_contrato_temporal]`:* identifica la modalidad y la causa de temporalidad consignada en el contrato y comprueba que el término ha llegado efectivamente y que no se han encadenado contratos por encima de los límites del artículo 15.5, que convertirían la relación en indefinida.
4. **Fecha de efectos y preaviso [negociación].** Fija la fecha de efectos y comprueba el preaviso exigible: 15 días naturales en el despido objetivo (artículo 53.1.c) y en la finalización de contratos temporales de duración superior a un año (artículo 49.1.c), y el que establezca el convenio en los demás casos. Explica que en el despido objetivo el incumplimiento del preaviso **no invalida** la extinción pero obliga a abonar los salarios correspondientes a ese periodo. Comunica el plazo de caducidad de 20 días hábiles que se abre para el trabajador y la fecha límite resultante.
5. **Liquidación e indemnización [negociación, con cálculo desglosado].**
   - *Despido objetivo:* calcula la indemnización de **20 días de salario por año de servicio, prorrateándose por meses los periodos inferiores al año, con el máximo de 12 mensualidades** (artículo 53.1.b). Muestra la fórmula completa y el resultado. La indemnización debe ponerse a disposición del trabajador de forma **simultánea** a la entrega de la carta: concreta el medio (transferencia, cheque nominativo, efectivo con recibí). Si la causa es económica y la empresa no puede abonarla en ese momento, la carta debe hacerlo constar expresamente conforme al artículo 53.1.b, párrafo segundo, y el pago se difiere al momento de la efectividad de la extinción; adviértelo.
   - *Fin de contrato temporal:* calcula la indemnización de **12 días de salario por año de servicio** (artículo 49.1.c), advirtiendo de que no procede en los contratos formativos ni en el contrato de sustitución.
   - *Disciplinario y periodo de prueba:* no procede indemnización. Explícalo y advierte de que ello no exime de la liquidación de partes proporcionales.
   - En todas las modalidades, recuerda que debe entregarse el **finiquito** con la liquidación de salarios pendientes, vacaciones no disfrutadas y pagas extraordinarias devengadas, y ofrece continuar con la skill `finiquito-liquidacion`.
6. **Entrega, acuse de recibo y documentación [dato objetivo].** Fija la fórmula de entrega en mano con firma de recibí, y la alternativa de burofax con certificación de texto y acuse de recibo al domicilio del trabajador si este se niega a firmar o no acude. Advierte de que la negativa a firmar no impide la eficacia de la entrega si se acredita ante dos testigos. Recuerda las obligaciones anejas: entrega del certificado de empresa a la Seguridad Social, baja en el sistema con efectos de la fecha de extinción y, en el despido objetivo por causas del artículo 52.c, entrega de copia de la comunicación a la representación legal de los trabajadores.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, presenta el menú:
```
1. Modificar o ajustar un apartado existente.
2. Añadir o precisar hechos imputados o la acreditación de la causa.
3. Corregir datos identificativos, fechas o importes.
4. Revisar la coherencia global y realizar el control de calidad final.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Legales Preceptivas de Cierre
- **Carácter DRAFT:** el documento es un borrador profesional que debe ser revisado por un abogado o graduado social colegiado antes de su firma y entrega.
- **Plazo de impugnación:** el trabajador dispone de 20 días hábiles desde la fecha de efectos para presentar papeleta de conciliación; recuerda la fecha límite calculada.
- **Obligaciones anejas a la extinción:** entrega del finiquito, certificado de empresa, baja en la Seguridad Social en plazo, y liquidación de la indemnización puesta a disposición.
- **Conservación de la prueba:** conserva el acuse de recibo firmado o el justificante del burofax y todos los medios de acreditación de los hechos imputados, que serán la única base admisible de la defensa en juicio.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre en el BOE la versión consolidada vigente del Estatuto de los Trabajadores y de la LRJS, y localizar el convenio colectivo aplicable en su registro oficial, antes de redactar. Si se detectan cambios normativos, aplicar la redacción vigente al documento del workspace sin usar versiones desactualizadas.
2. **Concreción imperativa de los hechos:** está PROHIBIDO redactar imputaciones genéricas o no fechadas. Cada hecho debe llevar fecha o periodo, conducta descrita objetivamente y encaje en el apartado legal y convencional. Si el usuario no los concreta, el marcador permanece pendiente y el documento no se cierra.
3. **Requisitos acumulativos del despido objetivo (artículo 53.1):** comunicación escrita con expresión de causa, puesta a disposición simultánea de la indemnización y preaviso de 15 días. Nunca redactar un despido objetivo omitiendo la puesta a disposición sin la salvedad expresa de iliquidez del artículo 53.1.b para las causas económicas.
4. **Expediente contradictorio:** si el trabajador es representante legal, sindical o delegado de prevención, o si el convenio lo exige para su categoría, no redactar la carta sin expediente previo instruido y concluido (artículo 55.1).
5. **Prescripción de faltas (artículo 60.2):** faltas leves, 10 días; graves, 20 días; muy graves, 60 días desde que la empresa tuvo conocimiento, y en todo caso 6 meses desde su comisión. Verificar siempre antes de imputar y advertir de los hechos prescritos.
6. **Nulidad:** en los supuestos del artículo 55.5 —discriminación, vulneración de derechos fundamentales, embarazo, permisos y reducciones por cuidado, víctimas de violencia— el despido no procedente es nulo, con readmisión obligatoria. Advertirlo siempre que V4 no sea `ninguna`.
7. **Indemnización por improcedencia (artículo 56.1):** 33 días de salario por año de servicio con el tope de 24 mensualidades. Para contratos anteriores al 12 de febrero de 2012 rige el régimen transitorio de la disposición transitoria undécima, con 45 días por año hasta esa fecha. No calcular un importe transitorio sin verificar la disposición vigente.
8. **Periodo de prueba:** no consignar causa ni imputación alguna en la carta de no superación. Verificar que el pacto conste por escrito y no haya expirado.
9. **Cero invención:** no inventar hechos, fechas, advertencias previas, partes de incidencia, artículos de convenio ni jurisprudencia. Todos los datos no aportados permanecen como marcador con su nombre propio de plantilla (`{{fecha_hecho_1: fecha (DD/MM/AAAA)}}`), nunca sustituidos por un literal genérico repetido que rompería la precisión del `edit_file`.
10. **Cita de jurisprudencia:** no citar sentencias ni doctrina jurisprudencial que no se haya verificado en esta misma sesión mediante `web_search` en una fuente oficial. Si no se puede verificar, no citarla.
11. **Sintaxis de los marcadores (`{{clave: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real: nunca debe quedar rastro de la anotación en el documento escrito. Los marcadores cuyo dato aún no exista se conservan **íntegros, con su clave y su tipo**, para que el cliente y el profesional que revise vean qué falta y de qué naturaleza es. Está PROHIBIDO sustituir la clave propia del marcador por un literal genérico.
