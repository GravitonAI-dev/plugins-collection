---
name: responsabilidad-civil
title: Responsabilidad civil
i18n:
  en:
    name: civil-liability
    title: Civil liability
    description: >
      Generates the right filing to claim compensation for damage suffered by an injured party
      under the **Civil Code**, which governs the obligation to repair damage caused by breach
      or fault (Arts. 1902 et seq.), and the **Consolidated Act on civil liability and insurance
      in motor vehicle traffic (TRLRCSCVM, Royal Legislative Decree 8/2004)**, verified in the
      BOE: out-of-court damages claim (which interrupts limitation under Art. 1973 CC, opens the
      MASC negotiation and, in traffic cases, constitutes the prior claim to the insurer under
      Art. 7.1 TRLRCSCVM), contractual (Arts. 1101 and 1103 CC) or non-contractual (Arts. 1902,
      1903, 1907 and 1908 CC) liability claim with direct action against the insurer (Art. 76
      LCS), and reply accepting or rejecting an insurer's offer or reasoned response. It covers
      motor vehicle accidents, personal mobility vehicle accidents (subject to compulsory
      insurance since 2 January 2026), falls on premises, construction defects (Arts. 17 and 18
      LOE, Art. 1591 CC) and professional negligence, with a BLOCKING limitation-period filter
      before drafting. Do not use for civil liability arising from a crime, for state liability
      of the public administration, or for workplace injuries.
description: >
  Genera el escrito adecuado para reclamar la indemnización de los daños y perjuicios sufridos por un
  perjudicado, conforme al **Código Civil**, que regula la obligación de reparar el daño causado por incumplimiento o por culpa, (Arts. 1902 y ss.) y al **Texto Refundido de la Ley sobre responsabilidad civil y seguro en la circulación de vehículos a motor (TRLRCSCVM, Real Decreto Legislativo 8/2004)**, que regula la responsabilidad y el seguro obligatorio en los accidentes de circulación, verificados en el BOE: reclamación extrajudicial de daños (que interrumpe
  la prescripción del Art. 1973 CC, abre la actividad negociadora previa del Art. 5 LO 1/2025 y, en
  circulación, constituye la reclamación previa al asegurador del Art. 7.1 TRLRCSCVM), demanda de
  responsabilidad civil contractual (Arts. 1101 y 1103 CC) o extracontractual (Arts. 1902, 1903, 1907 y
  1908 CC), con acción directa contra la aseguradora del responsable (Art. 76 LCS), y escrito de
  contestación, aceptación o rechazo de la oferta o respuesta motivada de una aseguradora (Arts. 7.2 a
  7.6, 9 y 14 TRLRCSCVM). Cubre los accidentes de circulación con vehículo a motor, los accidentes con
  vehículo personal ligero o patinete (sujetos al seguro obligatorio creado por la disposición adicional
  primera de la Ley 5/2025 desde el 02/01/2026), las caídas en establecimiento, los vicios y defectos
  constructivos (Arts. 17 y 18 LOE, Art. 1591 CC) y la negligencia profesional. Aplica un filtro de
  prescripción BLOQUEANTE antes de redactar nada. NO usar para la responsabilidad civil derivada de
  delito ni para la pieza de responsabilidad civil de un proceso penal, para la responsabilidad
  patrimonial de la Administración, ni para daños laborales o accidentes de trabajo.
when_to_use: |
  - El usuario ha sufrido un daño personal o material por un accidente de circulación y quiere reclamar
    la indemnización al causante o a su aseguradora.
  - El usuario ha sido atropellado por un patinete o vehículo personal ligero, o ha sufrido un accidente
    con uno de ellos, y quiere reclamar.
  - El usuario se ha caído o ha sufrido un daño en un establecimiento abierto al público y quiere
    reclamar al titular.
  - El usuario tiene desperfectos o defectos constructivos en su vivienda o edificio y quiere reclamar a
    la promotora, la constructora o los técnicos.
  - El usuario cree que un profesional (sanitario, letrado, técnico) le ha causado un daño por una
    actuación negligente y quiere reclamar.
  - El usuario ha sufrido un daño por el incumplimiento de un contrato y quiere reclamar la
    indemnización de los daños y perjuicios.
  - El usuario ya reclamó y la aseguradora le ha enviado una oferta motivada o una respuesta motivada, y
    quiere contestarla, aceptarla a cuenta o rechazarla.
  - El usuario quiere saber si su reclamación está todavía en plazo y como interrumpir la prescripción.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - ambito_hecho: accidente de circulación / otro suceso
  - tipo_vehiculo_causante: vehículo a motor / vehículo personal ligero o patinete
  - supuesto_no_circulatorio: caída en establecimiento o vía pública / defecto o vicio constructivo / negligencia profesional
  - naturaleza_vinculo: contractual / extracontractual
  - momento_documento: primera reclamación extrajudicial / contestación a una oferta o respuesta motivada / demanda judicial
  - aseguradora_identificada: sí / no o desconocida
  - fecha_hecho: fecha del hecho dañoso
  - fecha_conocimiento_dano: fecha del alta médica o de la estabilización de secuelas, o de aparición del daño
  - actos_interruptivos: relación de reclamaciones previas fehacientes con su fecha y su medio
  - datos_perjudicado: nombre, documento de identidad, domicilio, teléfono, email
  - datos_responsable: nombre o razón social, documento de identidad, domicilio
  - datos_aseguradora: denominación, CIF, domicilio, número de póliza, referencia del siniestro
  - danos: descripción y soporte documental del daño personal, del daño material y del lucro cesante
  - cuantificacion: importe por partida y su fuente (tabla del baremo del ejercicio o informe pericial)
  - datos_oferta_motivada: tipo de comunicación, fecha de notificación, importe ofertado, requisitos cumplidos
outputs:
  - reclamacion_extrajudicial_danos: reclamación extrajudicial fehaciente de daños en markdown, DRAFT
  - demanda_responsabilidad_civil: demanda de juicio ordinario o verbal de responsabilidad civil en markdown, DRAFT
  - respuesta_oferta_motivada: escrito de aceptación, aceptación a cuenta o rechazo de la oferta o respuesta motivada en markdown, DRAFT
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

# Reclamación de Daños y Perjuicios por Responsabilidad Civil

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

Para garantizar un enrutamiento determinista y el cumplimiento normativo riguroso, el asistente resuelve y mantiene internamente en memoria los vectores de estado de la operación —cuyo catálogo y su correspondencia con las respuestas del formulario figuran en la Fase 1.2— y el origen de la plantilla (`origen_plantilla`).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas (por ejemplo, anotar un vector como resuelto) son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es clasificar con precisión la naturaleza del caso y fijar los vectores deterministas de estado.

### 1.1 Escucha Activa Previa
Antes de abrir formularios interactivos o hacer preguntas, analiza el mensaje inicial del usuario y la documentación aportada:
- Si el mensaje ya especifica inequívocamente los vectores de la operación, asígnalos de forma inmediata y silenciosa en memoria y pasa a la **Fase 2**.
- Si restan vectores por definir, no formules preguntas abiertas en turnos sucesivos: presenta el formulario estructurado interactivo mediante la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las opciones de triaje:

```json
{
  "form_data": [
    {
      "id": "momento_documento",
      "rationale": "Resolver V1: cada momento de la reclamación tiene su propio asset y su propia validación de procedibilidad.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "reclamacion_extrajudicial", "label": "Primera reclamación extrajudicial de los daños"},
        {"id": "respuesta_oferta", "label": "Contestación a una oferta o respuesta motivada de la aseguradora"},
        {"id": "demanda", "label": "Demanda judicial de reclamación de daños"}
      ]
    },
    {
      "id": "ambito_hecho",
      "rationale": "Resolver V2: el accidente de circulación se rige por el texto refundido de la Ley de responsabilidad civil y seguro en la circulación de vehículos a motor y por su baremo; fuera de la circulación el régimen es el del Código Civil.",
      "question": "¿Cómo se produjo el daño?",
      "options": [
        {"id": "circulacion", "label": "En un accidente de circulación"},
        {"id": "otro_suceso", "label": "En otro tipo de suceso"}
      ]
    },
    {
      "id": "supuesto_no_circulatorio",
      "rationale": "Resolver V3: determina el régimen de responsabilidad aplicable y la carga de la prueba fuera de la circulación.",
      "question": "Si no fue un accidente de circulación, ¿de qué supuesto se trata?",
      "show_if": {"question_id": "ambito_hecho", "option_ids": ["otro_suceso"]},
      "options": [
        {"id": "caida", "label": "Caída en establecimiento o en vía pública"},
        {"id": "vicio_constructivo", "label": "Defecto o vicio de la construcción"},
        {"id": "negligencia_profesional", "label": "Negligencia profesional"},
        {"id": "otro", "label": "Otro supuesto"},
        {"id": "no_procede", "label": "No procede: fue un accidente de circulación"}
      ]
    },
    {
      "id": "aseguradora_identificada",
      "rationale": "Resolver V4: la reclamación previa al asegurador es requisito de procedibilidad de la demanda en el ámbito de la circulación.",
      "question": "¿Está identificada la aseguradora del causante del daño?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No, o se desconoce"}
      ]
    },
    {
      "id": "tipo_vehiculo",
      "rationale": "Resolver V5: el seguro obligatorio de los vehículos personales ligeros no existía antes del 02/01/2026 y, después, depende de los tres requisitos acumulativos de la disposición adicional primera de la Ley 5/2025. Preguntar únicamente si V2 = circulación.",
      "question": "Si fue un accidente de circulación, ¿qué clase de vehículo causó el daño?",
      "show_if": {"question_id": "ambito_hecho", "option_ids": ["circulacion"]},
      "options": [
        {"id": "turismo_o_similar", "label": "Turismo, motocicleta, furgoneta o camión"},
        {"id": "vehiculo_personal_ligero", "label": "Patinete o vehículo de movilidad personal"},
        {"id": "no_procede", "label": "No procede: no intervino ningún vehículo (suceso no circulatorio)"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `momento_documento`
- `V2` — `ambito_hecho`
- `V3` — `supuesto_no_circulatorio`
- `V4` — `aseguradora_identificada`
- `V5` — `tipo_vehiculo`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables y superado el filtro de prescripción, evalúa en este orden:

- Si V1 = reclamacion_extrajudicial → **HOJA RECLAMACIÓN**: `assets/template-reclamacion-extrajudicial-danos.md`.
- Si V1 = respuesta_oferta → **HOJA OFERTA**: `assets/template-respuesta-oferta-motivada.md`.
- Si V1 = demanda → **HOJA DEMANDA**: `assets/template-demanda-responsabilidad-civil.md`, con la validación de procedibilidad del apartado siguiente.
- Si V1 = demanda, V2 = circulación y **no consta reclamación previa al asegurador** → **NO crear la demanda**. Explicar que el Art. 7.8 TRLRCSCVM, en relación con el Art. 403 LEC, impide admitir a trámite las demandas que no acompañen la oferta o la respuesta motivada o, en su defecto, la reclamación previa al asegurador. Redirigir a la HOJA RECLAMACIÓN y ofrecer preparar la demanda después.
- Si V1 = demanda, V2 = otro_suceso y **no consta ninguna actividad negociadora previa** → **NO crear la demanda**. Explicar el requisito de procedibilidad del Art. 5 LO 1/2025 y del Art. 264.4.º LEC. Redirigir a la HOJA RECLAMACIÓN. Excepción: si el cliente **desconoce el domicilio del demandado o el medio por el que puede requerirle**, el Art. 264.4.º LEC admite en su lugar una declaración responsable de la imposibilidad de llevar a cabo la actividad negociadora previa; en ese caso continuar con la HOJA DEMANDA y advertir de que deberá aportarse esa declaración.
- Si V1 = respuesta_oferta y V2 = otro_suceso → usar la HOJA OFERTA, **desactivando todos los bloques que invocan el Art. 7 TRLRCSCVM**: fuera de la circulación la aseguradora no está sujeta al procedimiento de oferta y respuesta motivada, y lo recibido es una oferta contractual ordinaria regida por los Arts. 18 y 20 LCS. Decírselo al cliente expresamente.
- Si V2 = circulación, V5 = vehiculo_personal_ligero y el hecho es **anterior al 02/01/2026** → el seguro obligatorio de vehículos personales ligeros **no estaba en vigor**. No afirmar que existe. Reconducir al Art. 1902 CC con culpa probada frente al patrimonio del causante, preguntar si el causante tenía algún seguro voluntario de responsabilidad civil (a menudo el del hogar) y advertir de que el baremo del Anexo pasa a ser solo orientativo.
- Si V2 = circulación, V5 = vehiculo_personal_ligero y el hecho es **posterior al 02/01/2026** → antes de afirmar que hay seguro obligatorio, comprobar los tres requisitos acumulativos del apartado 1 de la disposición adicional primera de la Ley 5/2025: certificado de circulación, inscripción en el Registro de Vehículos de la DGT y etiqueta identificativa con el número de inscripción o matrícula. Si no concurren, aplicar el mismo tratamiento que en el caso anterior.
- Si el vehículo causante **circulaba sin seguro, no está identificado o su aseguradora está en liquidación** → advertir de que la reclamación corresponde al Consorcio de Compensación de Seguros por el procedimiento propio del Art. 11 TRLRCSCVM y **escalar**: fuera de alcance. Puede prepararse la reclamación extrajudicial frente al causante identificado, si lo hay.
- Si el hecho ocurrió **en la vía pública o en una instalación de titularidad pública**, o la asistencia sanitaria se presto en la **sanidad pública** → **DETENER**: es responsabilidad patrimonial de la Administración, que se tramita por el procedimiento administrativo y, en su caso, ante la jurisdicción contencioso-administrativa. Advertir, explicar la vía correcta y escalar. No crear documento.
- Si el daño se sufrió **en el trabajo o con ocasión del trabajo** → **DETENER**: jurisdicción social, con régimen propio. Advertir y escalar. No crear documento.
- Si hay o puede haber **proceso penal** por los mismos hechos, o el cliente pide denuncia, querella o la reclamación de la responsabilidad civil dentro del proceso penal → **DETENER**: fuera de alcance. Advertir y escalar a especialista en penal.
- Si hubo **fallecimiento del perjudicado o gran invalidez / gran lesionado** → **ESCALAR antes de cifrar nada**. Puede prepararse la reclamación extrajudicial para interrumpir la prescripción, dejando la cuantificación abierta, pero la valoración se deriva a especialista.
- Si V3 = negligencia_profesional y es **sanitaria** → advertir de que sin informe médico pericial que acredite la desviación de la *lex artis* y el nexo causal la reclamación no es viable, indicar que el primer paso material es obtener la historia clínica completa, y **escalar**.
- Si el daño deriva de un **producto defectuoso** → advertir de que el régimen es el del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios, no verificado por esta skill, y escalar.
- **Requisito de procedibilidad (Ley Orgánica 1/2025).** Si el intento previo de un medio adecuado de solución de controversias no está acreditado y esta skill no genera por sí misma el documento que lo acredita, **deriva a `masc-acuerdos`**, que produce el requerimiento de negociación, el acta del intento, la oferta vinculante, el acuerdo transaccional y la declaración responsable de imposibilidad. Ofrece encadenar con ella antes de continuar, y advierte de que sin ese documento la demanda no se admite a trámite.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **TODAS LAS HOJAS:** confirmar que existe un **daño real y acreditable**, no una molestia ni un riesgo de daño. Si el cliente no puede describir un menoscabo concreto ni el documento que lo soporta, decirlo antes de redactar: no hay reclamación.
- **TODAS LAS HOJAS:** confirmar que existe **soporte documental de cada partida** que se va a reclamar. Una partida sin soporte no se abarata: se elimina. Ver `references/estilo-redaccion-escritos.md`, apartado de prueba.
- **HOJA DEMANDA:** determinar el procedimiento por la cuantía (Art. 253 LEC). **Juicio verbal si la cuantía no excede de 15.000 euros (Art. 250.2 LEC); juicio ordinario si excede de esa cifra (Art. 249.2 LEC), y también si el interés económico resulta imposible de calcular.** Verificar el umbral en la Fase 2 antes de fijarlo.
- **HOJA DEMANDA:** verificar que se demanda a quien responde. Si se ejercita la acción directa, la aseguradora es demandada por derecho propio (Art. 76 LCS), no un tercero llamado al proceso.
- **HOJA DEMANDA y HOJA RECLAMACIÓN, si V4 = no:** antes de dar por inexistente el seguro, incluir en la reclamación el requerimiento del último inciso del Art. 76 LCS (el asegurado está obligado a manifestar al perjudicado la existencia del contrato de seguro y su contenido). En circulación, indicar además la consulta del fichero de vehículos asegurados del Consorcio de Compensación de Seguros (Art. 2.2 TRLRCSCVM).
- **HOJA OFERTA:** calcular el **nuevo plazo de prescripción de un año** que se inicio con la notificación fehaciente de la oferta o respuesta motivada (Art. 7.1 TRLRCSCVM) y comunicarlo. Es el plazo que más casos hace perder, porque el cliente cree que sigue interrumpido mientras negocia.
- **HOJA OFERTA:** comprobar si la comunicación recibida **cumple los requisitos del Art. 7.3** (oferta) o del **Art. 7.4** (respuesta). Si no los cumple, no concurre la causa de exoneración de intereses del Art. 9.a) TRLRCSCVM: hacerlo constar en el escrito.
- **HOJA RECLAMACIÓN, en circulación:** recordar que la reclamación del Art. 7.1 TRLRCSCVM **no requiere estar cuantificada**. Si el proceso curativo no ha terminado, **no retrasar el envío para cuantificar**: se remite con la cuantificación abierta y reserva expresa de la diferencia.
- **CULPA CONCURRENTE:** si de los hechos se desprende que el perjudicado contribuyo al daño (no llevaba casco o cinturón, cruzo indebidamente, abandono el proceso curativo), decírselo antes de fijar la cuantía. En circulación, la reducción alcanza a **todas** las partidas y **hasta un máximo del 75 %** (Art. 1.2 TRLRCSCVM). Excepción del párrafo segundo del mismo precepto: en secuelas y lesiones temporales, la culpa de víctimas no conductoras **menores de catorce años** o privadas de capacidad de culpa civil **no suprime ni reduce** la indemnización.
- **MASC:** a diferencia de la demanda ejecutiva, la demanda de responsabilidad civil **SI** está sujeta al requisito de procedibilidad del Art. 5 LO 1/2025: es un proceso declarativo del Libro II de la LEC y la responsabilidad civil por daños no figura entre las materias exceptuadas del Art. 5.2. Nunca omitir este requisito en la HOJA DEMANDA.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 1.902 y 1.903 del Código Civil (responsabilidad extracontractual con prescripción anual Art. 1968.2 CC); Art. 1.101 CC (responsabilidad contractual); Texto Refundido de la Ley sobre Responsabilidad Civil y Seguro en la Circulación de Vehículos a Motor (TRLRCSCVM, Art. 7 sobre oferta motivada preceptiva y baremo legal).
2. **Orientación Legal del Caso:**

**Informa la vía, el plazo y la fuente aplicable.** Textos fijos por hoja, a los que se añade siempre el plazo calculado en el filtro de prescripción:
   - CIRCULACIÓN CON VEHÍCULO A MOTOR: "A su caso corresponde el régimen de responsabilidad civil por los daños causados con motivo de la circulación de vehículos a motor, conforme al artículo 1 del texto refundido de la Ley sobre responsabilidad civil y seguro en la circulación de vehículos a motor, aprobado por Real Decreto Legislativo 8/2004. Los daños personales se cuantifican obligatoriamente con el sistema de valoración de su Anexo, en las cuantías del ejercicio {{EJERCICIO_BAREMO}}. La acción prescribe al año (artículo 1968.2.º del Código Civil y artículo 7.1 del citado texto refundido). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2004-18911"
   - CIRCULACIÓN CON VEHÍCULO PERSONAL LIGERO: "A su caso corresponde el régimen de responsabilidad civil y seguro del texto refundido de la Ley sobre responsabilidad civil y seguro en la circulación de vehículos a motor, aplicable a los vehículos personales ligeros por remisión del apartado 6 de la disposición adicional primera de la Ley 5/2025, de 24 de julio, vigente desde el 2 de enero de 2026. La cobertura mínima del seguro obligatorio es de 6.450.000 euros por siniestro en daños a las personas y 1.300.000 euros en daños a los bienes. La acción prescribe al año. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2025-15424"
   - CAÍDA O SUCESO EN ESTABLECIMIENTO: "A su caso corresponde la responsabilidad civil extracontractual del artículo 1902 del Código Civil, y en su caso la del artículo 1903 si el daño lo causo un dependiente en el ejercicio de sus funciones. Deberá acreditarse la omisión del deber de cuidado imputable al titular: la caída, por si sola, no genera responsabilidad. La acción prescribe al año desde que usted conoció el daño (artículo 1968.2.º del Código Civil). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - VICIO CONSTRUCTIVO: "A su caso corresponde el régimen de responsabilidad de los agentes de la edificación del artículo 17 de la Ley 38/1999, de Ordenación de la Edificación, con plazos de garantía de diez, tres o un año desde la recepción de la obra según el tipo de defecto, y un plazo de prescripción de dos años desde que se producen los daños (artículo 18.1 de la misma Ley). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1999-21567"
   - NEGLIGENCIA PROFESIONAL: "A su caso corresponde la responsabilidad civil del profesional, contractual conforme a los artículos 1101 y 1103 del Código Civil si mediaba contrato, o extracontractual conforme al artículo 1902 si no lo había. Deberá acreditarse que la actuación se aparto del estándar de diligencia exigible, no solo que el resultado fue desfavorable: la obligación del profesional es de medios y no de resultado. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - DAÑO CONTRACTUAL: "A su caso corresponde la responsabilidad contractual de los artículos 1101 y 1103 del Código Civil, con un plazo de prescripción de cinco años desde que pudo exigirse el cumplimiento (artículo 1964.2 del Código Civil). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - En la HOJA RECLAMACIÓN, añadir: "La reclamación extrajudicial fehaciente interrumpe el plazo de prescripción, que vuelve a contarse de cero desde su recepción (artículo 1973 del Código Civil), y constituye la actividad negociadora previa que la ley exige antes de demandar (artículo 5 de la Ley Orgánica 1/2025)."
   - En la HOJA DEMANDA, añadir: "Para presentar esta demanda es requisito de procedibilidad haber intentado previamente una solución negociada, cuyo documento acreditativo debe acompañarse (artículo 5 de la Ley Orgánica 1/2025 y artículo 264.4.º de la Ley de Enjuiciamiento Civil)."
   - En la HOJA DEMANDA, si V2 = circulación, añadir además: "Además, en un accidente de circulación la demanda no se admite a trámite si no se acompaña la oferta o la respuesta motivada de la aseguradora o, en su defecto, la reclamación previa que se le dirigió (artículo 7.8 del texto refundido citado, en relación con el artículo 403 de la Ley de Enjuiciamiento Civil)."
   - En la HOJA OFERTA, si V2 = circulación, añadir: "La aseguradora está obligada a presentar oferta motivada de indemnización en el plazo de tres meses desde su reclamación, o respuesta motivada si no puede ofertar (artículo 7.2 del texto refundido citado). La notificación fehaciente de una u otra inicia un nuevo plazo de prescripción de un año, cuyo vencimiento en su caso es el {{FECHA_VENCIMIENTO_NUEVO_PLAZO}}."

3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada **que ha resuelto el enrutamiento de la Fase 1.3** (menciónala por su denominación formal, sin mostrar rutas internas ni volcar su contenido). Si el enrutamiento asigno varios documentos, nómbralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada** ni la primera del inventario de la sección de assets.
4. **Elección de Plantilla Base:** Aplica el protocolo universal de `REG-AST-01` (`CLAUDE.md`), convocando en ese mismo turno el formulario interactivo `restricted_human_in_the_loop_request` para que el usuario elija entre la plantilla del sistema o aportar su propia minuta.

### 2.3 Manejo Determinista de la Elección
Aplica rigurosamente el protocolo de `REG-AST-01` (`CLAUDE.md`): si se selecciona `plantilla_sistema`, carga la plantilla oficial y avanza a la **Fase 3**; si se selecciona `plantilla_usuario`, requiere la minuta (si no consta ya en el chat), ejecuta el control de legalidad y avanza a la **Fase 3**.
---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

Aplica rigurosamente la directiva `REG-DOC-01` (ciclo de creación del documento base):
1. **Escritura del Documento (`create_file`):** Vuelca íntegramente la plantilla acordada en un archivo en el workspace con nombre en `snake_case.md`, aplicando el principio Zero-Omission y el volcado inmediato total de partes (`REG-CLI-04`) en título H1, comparecencia y firmas.
2. **Validación de Integridad:** Comprobación prioritaria mediante `# WORKSPACE ACTIVE DOCUMENTS`.
3. **Confirmación en Chat y Encadenamiento Inmediato:** Informa en el chat de la ruta absoluta del documento creado y los datos de partes incorporados, e introduce en esa misma respuesta la primera sección de la Fase 4 sin detener el flujo.
---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial las secciones del documento respetando rigurosamente las directivas operativas globales de `CLAUDE.md`:
- **Partes e Intervinientes (REG-CLI-01 a 04):** Búsqueda prioritaria con `search_clients`, desambiguación con opción obligatoria `ninguna`, consentimiento de guardado con `save_client` (REG-CLI-03) y volcado directo e inmediato al editor (`edit_file` / `create_file`) sin confirmación en chat (REG-CLI-04).
- **Datos Estructurados Objetivos:** Solicitud en bloque mediante `slot_filling_request`.
- **Equivalencia Chat / Formulario (REG-DAT-01):** Ingestión directa de información aportada por chat sin re-emitir formularios innecesarios; reenvío oportuno si el usuario canceló sin responder.
- **Cláusulas Sustantivas / Negociables:** Negociación en chat -> Vista previa en texto plano -> Pregunta literal de confirmación (`¿Confirmamos esta cláusula?` / `¿Confirmamos esta sección?`) -> Persistencia con `edit_file`.

### Hoja de Ruta de Secciones y Cláusulas Condicionales

**Anuncio de sección y encadenamiento:** al terminar una sección y confirmar su edición en disco, emite en ese mismo turno el anuncio fijo de la sección que se abre y lanza de inmediato su formulario `slot_filling_request` (si es grupo de datos) o su planteamiento en chat (si es negociación). No pidas permiso para pasar de sección: informa y continúa. Los anuncios nombran la sección SUSTANTIVA del documento, nunca la mecánica interna. La vista previa y la confirmación siempre van en el chat. Las cláusulas y decisiones de negociación se explican y se confirman una a una en el chat.

**Validación de sentido en esta skill.** Eres un LLM, no un formulario. Rechaza y pide aclaración cuando: la fecha del alta sea anterior a la del hecho; el importe de una partida no guarde relación con el daño descrito; el cliente describa como "secuela" algo que aún está en tratamiento; o afirme un importe de lucro cesante sin ingresos previos acreditables. **Nunca escribas en el documento una cifra que el cliente no pueda soportar con un documento.**

### Secciones — HOJA RECLAMACIÓN

1. **Datos del perjudicado** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por sus datos identificativos." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: a) nombre y apellidos o razón social; b) DNI, NIE o CIF según corresponda; c) domicilio a efectos de notificaciones; d) teléfono y correo electrónico de contacto; e) si interviene letrado, su nombre y número de colegiado. Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Conforme a `REG-CLI-04`, vuelca de inmediato a disco con `edit_file` (o ya volcado en `create_file`) sin confirmación en chat, sustituyendo exhaustivamente los nombres en todas sus apariciones a lo largo del documento (título/encabezado H1, comparecencia y firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones).
2. **Contra quién se dirige la reclamación** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Determinamos ahora a quién debe dirigirse la reclamación." **Explica antes de preguntar**, apoyándote en `references/regimenes-de-responsabilidad-por-supuesto.md`, apartado 6: dirigirla solo al causante obliga a cobrar contra su patrimonio, con riesgo de insolvencia; dirigirla a la aseguradora por la acción directa del Art. 76 LCS aporta solvencia y, sobre todo, **inmunidad frente a las excepciones que el asegurador tenga contra su asegurado** (impago de prima, incumplimiento de deberes de la póliza), aunque el asegurador si puede oponer la culpa exclusiva del perjudicado; y dirigirla a **ambos** cubre el exceso sobre el límite de la póliza y evita quedar sin nada si se discute la vigencia del seguro. **Recomienda por defecto dirigirla a ambos** cuando V4 = si, y explica por qué. Pregunta después la decisión y confírmala.
3. **Datos del destinatario o destinatarios** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si son nuevos, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a los datos de la parte a la que se dirige la reclamación." Invoca `search_clients` prioritariamente. Por cada destinatario nuevo, solicita en bloque vía `slot_filling_request`: a) nombre o razón social; b) documento de identidad o CIF; c) domicilio. Si es aseguradora, además: número de póliza y referencia del siniestro, si se conocen. Si son nuevos clientes/entidades, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca de inmediato a disco con `edit_file` sin turno de confirmación en chat per `REG-CLI-04`, sustituyendo exhaustivamente los nombres en todas sus apariciones (título H1, comparecencia y firmas). **Si V4 = no**, explica que se incluirá el requerimiento del último inciso del Art. 76 LCS para que el causante manifieste la existencia y el contenido de su seguro, y en circulación menciona el fichero de vehículos asegurados del Consorcio (Art. 2.2 TRLRCSCVM).
4. **El hecho dañoso** *(dato objetivo con validación — recogida con `slot_filling_request`, confirmación en chat)*. Anuncio fijo: "Describimos ahora el hecho que le causo el daño." La fecha y hora ya son conocidas por el filtro de prescripción: **no la vuelvas a preguntar**. Solicita vía `slot_filling_request`: a) lugar exacto; b) descripción de lo ocurrido, en sus propias palabras; c) circunstancias relevantes para la imputación (señalización, estado del pavimento, maniobra del vehículo, identidad del conductor o del dependiente); d) si existe atestado, informe policial, parte de incidencia o denuncia, su referencia y organismo. **En circulación, informa de que las Fuerzas y Cuerpos de Seguridad de tráfico facilitan gratuitamente copia del atestado a petición del perjudicado (Art. 7.1 TRLRCSCVM)** y ofrece dejarlo solicitado en el escrito. **Si el supuesto es una caída en establecimiento, advierte en este mismo turno y con carácter urgente de que las grabaciones de videovigilancia se sobreescriben en días** y de que el escrito incluirá el requerimiento de conservación de las imágenes. Vista previa y confirmación en chat.
5. **Los daños sufridos** *(dato objetivo con validación)*. Anuncio fijo: "Concretamos los daños que ha sufrido y como se acreditan." Partidas a concretar, omitiendo las que no apliquen: a) daño personal: lesiones, centro asistencial, si el proceso curativo ha terminado y con que documentación se acredita; b) daño material: bienes dañados, importe de reparación o reposición y su justificante; c) lucro cesante: ingresos dejados de obtener y su soporte documental. **Por cada partida, pregunta expresamente con que documento se acredita.** Si no hay documento, dilo: la partida no se incluye, y explica que una partida sin soporte debilita todo el escrito. Vista previa y confirmación en chat.
6. **Cuantificación de la indemnización** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Pasamos a cuantificar la indemnización que se reclama." **Explica antes de pedir cifras**, siguiendo el guion del apartado 7 de `references/cuantificacion-danos-y-baremo.md`: que partidas existen y que cada una necesita su soporte; si el baremo es obligatorio (circulación, Art. 1.4 TRLRCSCVM) u **orientativo** (todo lo demás, donde hacen falta informes periciales); que las cuantías son las del ejercicio verificado en la Fase 2, citando la resolución concreta; que una partida sin soporte se elimina, no se abarata; y que la culpa concurrente reduce todas las partidas, hasta el 75 % en circulación. Pide después, en turnos separados y con confirmación propia de cada uno: a) importe del daño personal, con la tabla o el informe en que se apoya; b) importe del daño material; c) importe del lucro cesante. **Si el proceso curativo no ha terminado**, explica que la reclamación del Art. 7.1 TRLRCSCVM **no requiere estar cuantificada**, que no conviene retrasar el envío para cuantificar, y activa el bloque de reserva expresa de la diferencia.
7. **Requerimiento y propuesta** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Determinamos el requerimiento con que se cierra la reclamación." **Explica antes de preguntar**: el escrito debe contener una propuesta concreta y un plazo de respuesta, porque de ello depende que sirva como actividad negociadora del Art. 5 LO 1/2025 y que el Art. 7.1 de la misma Ley reinicie el cómputo si no hay respuesta en treinta días naturales. **En circulación, explica además que la aseguradora está obligada a responder con oferta motivada en tres meses (Art. 7.2 TRLRCSCVM) y que su silencio devenga los intereses de demora del Art. 9, en relación con el Art. 20 LCS: el interés legal incrementado en el 50 %, con un mínimo del 20 % anual pasados dos años del siniestro.** Pide después: a) plazo de respuesta que se concede (**propón 30 días naturales por defecto**, coherente con el Art. 7.1 LO 1/2025, y pregunta si desea otro); b) cuenta bancaria para el pago, si desea indicarla.
8. **Medio de envío, documentos y cierre** *(dato objetivo)*. Anuncio fijo: "Cerramos con la documentación que se acompaña y el medio de envío." Sub-apartados: a) relación numerada de los documentos que se adjuntan; b) medio de envío. **Sobre el medio de envío, advierte siempre y no aceptes un medio no fehaciente sin decirlo:** un correo electrónico sin acuse o una llamada no acreditan la interrupción de la prescripción; hace falta burofax con certificación de contenido y acuse de recibo, o notificación notarial, y conservar el justificante; c) lugar de firma y fecha (la del día, salvo indicación en contrario).

### Secciones — HOJA OFERTA

1. **Datos del perjudicado** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por sus datos identificativos." Igual estructura que en la HOJA RECLAMACIÓN vía `slot_filling_request`, volcando directamente a disco per `REG-CLI-04`.
2. **Datos de la aseguradora y del expediente** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nueva, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a los datos de la aseguradora y del expediente del siniestro." Invoca `search_clients` prioritariamente. Si es nueva, solicita en bloque vía `slot_filling_request`: a) denominación y CIF de la aseguradora; b) domicilio al que se dirige el escrito; c) número de póliza; d) referencia del siniestro o del expediente. Si es nueva entidad cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca de inmediato a disco con `edit_file` sin confirmación en chat per `REG-CLI-04`.
3. **La comunicación recibida** *(dato objetivo con validación)*. Anuncio fijo: "Examinamos ahora la comunicación que ha recibido de la aseguradora." Sub-apartados: a) si usted remitió reclamación previa a la aseguradora y, en tal caso, su fecha y el medio empleado — **no des por supuesto que la hubo: es frecuente que sea la aseguradora la que abra el expediente a partir del parte de su asegurado o del atestado y oferte sin reclamación del perjudicado.** Si no la hubo, pregunta a partir de que se abrió el expediente y como tuvo usted noticia de él, activa en el asset el bloque de apertura sin reclamación previa en lugar del de reclamación previa, y hazle saber que el plazo de tres meses del Art. 7.2 TRLRCSCVM se cuenta desde la reclamación del perjudicado, de modo que en su caso aún no ha empezado a correr; b) fecha en que recibió la comunicación de la aseguradora (ya conocida por el filtro de prescripción: **no la vuelvas a preguntar**); c) si se trata de una oferta motivada (propone una indemnización) o de una respuesta motivada (explica por qué no la propone) — **explica la diferencia antes de preguntarla**, porque el cliente rara vez la conoce; d) importe ofertado, si lo hay; e) que documentación e informes le entregaron con ella. **Con la respuesta a e), comprueba tú mismo si se cumplen los requisitos del Art. 7.3 (oferta) o del Art. 7.4 (respuesta) TRLRCSCVM** e informa del resultado: si falta la entrega desglosada de los documentos, incluido el informe médico pericial definitivo, ese incumplimiento impide a la aseguradora aportarlos después en juicio (Art. 7.3.c) y **elimina la exoneración de intereses del Art. 9.a)**. Vista previa y confirmación en chat.
4. **Cómputo del nuevo plazo** *(dato objetivo con validación bloqueante)*. Anuncio fijo: "Verificamos el plazo del que dispone desde esa comunicación." Con la fecha de la letra b) de la sección anterior, calcula tú mismo el vencimiento del nuevo plazo de un año del Art. 7.1 TRLRCSCVM e infórmalo con la fecha exacta. **Si ese plazo ya está agotado, detente**: aplica el filtro de prescripción de la Fase 1 con su regla de detención. **Si quedan menos de 60 días, advierte con prioridad** y explica que este escrito interrumpe de nuevo la prescripción (Art. 1973 CC) y que la solicitud de informes periciales complementarios del Art. 7.5 mantiene el plazo interrumpido.
5. **Posición frente a la oferta** *(negociación — explicar antes de decidir; la decisión central de esta hoja)*. Anuncio fijo: "Determinamos la posición que va a adoptar frente a la oferta recibida." **Explica antes de preguntar, sin omitir ninguno de estos cuatro puntos:**
   - **Aceptar no obliga a renunciar a nada.** El Art. 7.3.d) TRLRCSCVM impide condicionar el pago a la renuncia del perjudicado al ejercicio de futuras acciones. Si el documento que le proponen firmar contiene un finiquito o una renuncia total, **no debe firmarlo sin revisión**.
   - **Se puede aceptar a cuenta.** Cabe cobrar ya el importe ofertado como pago a cuenta, sin conformidad con el total y sin renunciar a reclamar la diferencia. Es la opción conservadora cuando la valoración se discute pero el importe ofrecido no se cuestiona como mínimo.
   - **La oferta en plazo y con el contenido del Art. 7.3 exonera de intereses, pero solo respecto de la cantidad ofertada y satisfecha o consignada** (Art. 9.a) TRLRCSCVM). La diferencia entre lo ofertado y lo que finalmente se reconozca sigue devengando el interés del Art. 20 LCS.
   - **Si no hubo oferta en tres meses por causa imputable a la aseguradora, se devengan los intereses de demora del Art. 9** (Art. 7.2 TRLRCSCVM), y lo mismo si, aceptada la oferta, no se paga en cinco días ni se consigna.
   Pregunta después: "Su posición frente a la oferta es:
   1. Aceptarla en su integridad
   2. Aceptar el importe a cuenta, sin conformidad con el total y sin renunciar a la diferencia
   3. Rechazarla y mantener su reclamación"
   Confirma la decisión en el chat antes del `edit_file` y activa el bloque correspondiente del asset.
6. **Motivos de disconformidad** *(negociación — solo si la posición es 2 o 3)*. Anuncio fijo: "Concretamos los motivos de disconformidad, partida por partida." **Se discute partida por partida en el chat, nunca en bloque.** Sub-apartados, omitiendo los que no apliquen: a) partidas del baremo cuya cuantía no se corresponde con las tablas del ejercicio verificado; b) días de perjuicio temporal o puntos de secuela no reconocidos, con la documentación médica que los acredita; c) partidas de daño material o lucro cesante omitidas en la oferta, con su soporte; d) culpa concurrente imputada por la aseguradora que usted no acepta, y las razones. **En la letra d), si el lesionado es menor de catorce años o carece de capacidad de culpa civil, infórmale de que el párrafo segundo del Art. 1.2 TRLRCSCVM impide que su culpa reduzca la indemnización por secuelas y lesiones temporales**, y activa el bloque correspondiente. **En la letra a), comprueba tú mismo si la aseguradora aplico las cuantías del ejercicio del accidente o las de un ejercicio anterior**: es una de las discrepancias más frecuentes y la detección es automática con el dato de la Fase 2.
7. **Solicitudes** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Determinamos las solicitudes que se dirigen a la aseguradora." **Explica cada opción antes de preguntar si la desea**, y pregúntalas en turnos separados: a) **informe pericial complementario del Art. 7.5**: puede pedirse al Instituto de Medicina Legal y Ciencias Forenses **con cargo a la aseguradora aun sin su acuerdo**, obliga a esta a una nueva oferta motivada en un mes desde su entrega y mantiene interrumpido el plazo de prescripción; el lesionado debe ser reconocido en tres meses y el informe emitirse en uno (Art. 7.6); b) **pago a cuenta** de los perjuicios ya consolidados, con el deber de la aseguradora de informar de la situación del siniestro cada dos meses (Art. 7.4.a).1.º); c) **entrega de la documentación no aportada** (Arts. 7.3.c) y 7.4.b)); d) **acudir a un medio adecuado de solución de controversias** con profesional especializado (Art. 14 TRLRCSCVM); e) **anuncio de la vía judicial** con un plazo de respuesta, si el cliente lo desea.
8. **Medio de envío, documentos y cierre** *(dato objetivo)*. Anuncio fijo: "Cerramos con la documentación que se acompaña y el medio de envío." Igual estructura y misma advertencia sobre la fehaciencia que en la HOJA RECLAMACIÓN.

### Secciones — HOJA DEMANDA

1. **Requisito de procedibilidad** *(dato objetivo con validación bloqueante — va PRIMERO)*. Anuncio fijo: "Comenzamos verificando que se cumple el requisito previo para presentar la demanda." Solicita en bloque vía `slot_filling_request`: a) fecha, medio y destinatario de la actividad negociadora previa, y el justificante de envío y recepción de que dispone; b) resultado (sin respuesta, respuesta negativa, acuerdo parcial). **Si no hay ninguna actividad negociadora acreditada, aplica el enrutamiento de la Fase 1: no continues con la demanda.** Si el cliente desconoce el domicilio del demandado o el medio por el que requerirle, informa de la declaración responsable que admite el Art. 264.4.º LEC y continúa. Vista previa y confirmación en chat.
2. **Parte demandante** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a la identificación de la parte demandante." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: a) nombre y apellidos o razón social; b) DNI, NIE o CIF; c) domicilio; d) nombre del procurador y del letrado. **Abogado y procurador son preceptivos en el juicio ordinario; en el juicio verbal no lo son si la cuantía no excede de 2.000 euros (Arts. 23 y 31 LEC)**: si la cuantía está por debajo de esa cifra, pregúntale si va a comparecer por sí mismo y adapta el encabezamiento. Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca de inmediato a disco con `edit_file` (o en `create_file`) sin confirmación en chat per `REG-CLI-04`.
3. **Parte demandada** *(negociación para la elección + dato objetivo para los datos — búsqueda prioritaria con `search_clients`, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Determinamos ahora contra quién se dirige la demanda." **Misma explicación que en la sección 2 de la HOJA RECLAMACIÓN**, con el énfasis puesto en que la acción directa del Art. 76 LCS convierte a la aseguradora en demandada por derecho propio y es inmune a las excepciones que el asegurador tenga contra su asegurado. **Recomienda por defecto demandar a ambos solidariamente** cuando V4 = si. Tras confirmar la elección, pide los datos de cada demandado vía `slot_filling_request` (si no constan en `search_clients`). Si son nuevas entidades/personas, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca directamente al documento con `edit_file` sin confirmación en chat per `REG-CLI-04`.
4. **El hecho dañoso** *(dato objetivo con validación)*. Anuncio fijo: "Describimos el hecho que fundamenta la demanda." Igual estructura que en la HOJA RECLAMACIÓN, sección 4, añadiendo el número de documento con que se acredita cada elemento.
5. **La imputación de la responsabilidad** *(dato objetivo con explicación)*. Anuncio fijo: "Concretamos el título por el que responde la parte demandada." Redacta el fundamento con el régimen que corresponda a la rama, tomándolo de `references/regimenes-de-responsabilidad-por-supuesto.md`, y **explícale al cliente que tendrá que probar**: en circulación, la responsabilidad es por el riesgo creado y es el demandado quien debe probar la culpa exclusiva de la víctima o la fuerza mayor; fuera de ella, es el demandante quien debe probar la culpa o negligencia, y en negligencia profesional la desviación de la *lex artis*. Pide el dato concreto que falte según la rama: la omisión del deber de cuidado, la obligación contractual incumplida, el apartado del Art. 17.1 LOE en que encaja el defecto y la fecha de recepción de la obra, o la desviación del estándar profesional.
6. **Los daños y perjuicios** *(dato objetivo con validación)*. Anuncio fijo: "Concretamos los daños y su acreditación." Igual estructura que en la HOJA RECLAMACIÓN, sección 5, con un nivel de detalle mayor en el daño personal: días de perjuicio temporal desglosados en muy grave, grave, moderado y básico; intervenciones quirúrgicas; relación de secuelas y puntos. **Numera cada documento y relaciónalo en el hecho correspondiente.**
7. **Nexo causal y prueba pericial** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Valoramos como se acreditará la relación entre el hecho y el daño." **Explica antes de preguntar** que el nexo causal es el punto en que fracasan la mayoría de las reclamaciones, y que en vicio constructivo y en negligencia profesional **sin dictamen pericial no hay demanda viable**. Pregunta si dispone ya de informe pericial, de que clase y de quién; si no lo tiene, adviértele de que debe obtenerlo antes de presentar y de las consecuencias de no hacerlo. Pregunta después si desea anunciar en la demanda la proposición de prueba pericial y testifical.
8. **Cuantificación de la indemnización** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Pasamos a cuantificar la indemnización que se reclama." Igual estructura y guion que en la HOJA RECLAMACIÓN, sección 6, con dos añadidos: a) **el detalle partida por partida con indicación de la tabla aplicada a cada concepto** entra en el cuerpo del escrito, no en un anexo; b) si hay **culpa concurrente que el cliente reconoce**, explica la reducción del Art. 1.2 TRLRCSCVM (hasta el 75 % en circulación) o la moderación judicial del Art. 1103 CC fuera de ella, y aplícala expresamente en el desglose. **No infles la cuantía**: encarece las costas si la estimación es parcial y da a la contraparte el argumento del rechazo global.
9. **No prescripción de la acción** *(dato objetivo con validación bloqueante)*. Anuncio fijo: "Cerramos el apartado de hechos con el plazo de la acción." Con las fechas ya conocidas del filtro de prescripción, redacta el hecho y el fundamento correspondientes: plazo aplicable, precepto, *dies a quo*, cada acto interruptivo con su fecha y su medio, y el documento que lo acredita. **En circulación, si hubo oferta o respuesta motivada, computa desde su notificación el nuevo plazo de un año del Art. 7.1 TRLRCSCVM.** No omitas nunca este fundamento: es la primera excepción que opondrá la contraparte.
10. **Intereses** *(negociación — explicar antes de decidir)*. Anuncio fijo: "Determinamos los intereses que se reclaman." **Explica antes de preguntar**: si se demanda a la aseguradora, la mora del Art. 20 LCS **se impone de oficio** por el órgano judicial y consiste en el interés legal del dinero incrementado en el 50 %, computado desde la fecha del siniestro, con un mínimo del 20 % anual transcurridos dos años; en circulación se aplica con las singularidades del Art. 9 TRLRCSCVM, y **no procede la exoneración de su letra a) si la oferta no se presentó en plazo o no reunía el contenido del Art. 7.3**. Pregunta si se reclaman además los intereses procesales del Art. 576 LEC. Recuérdale que el interés legal del ejercicio se fija en la Ley de Presupuestos y debe consultarse al liquidar.
11. **Procedimiento, cuantía y juzgado** *(dato objetivo con validación)*. Anuncio fijo: "Determinamos el procedimiento y el juzgado competente." Con la cuantía ya fijada, calcula tú mismo el procedimiento: **juicio verbal si no excede de 15.000 euros (Art. 250.2 LEC), juicio ordinario si excede (Art. 249.2 LEC)**, e infórmalo. Pregunta después el partido judicial y confirma el fuero: en responsabilidad extracontractual cabe el del lugar del hecho dañoso; si se demanda a la aseguradora, también el de su domicilio o el del domicilio del asegurado. No admitas sumisión a un fuero que no corresponda.
12. **Documentos** *(dato objetivo)*. Anuncio fijo: "Cerramos con la relación de documentos que se acompañan." Pide la relación completa y numérala correlativamente con los hechos. **Verifica tú mismo que están incluidos los tres documentos sin los que la demanda no se admite:** el poder, el documento acreditativo de la actividad negociadora previa o la declaración responsable (Art. 264.4.º LEC) y, en circulación, el que acredite la oferta o la respuesta motivada o, en su defecto, la reclamación previa al asegurador (Art. 7.8 TRLRCSCVM).
13. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito." Lugar de firma; fecha del día salvo indicación en contrario.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: HECHOS numerados con una idea por apartado y en el orden natural de la responsabilidad civil (hecho dañoso, imputación, daño y cuantificación, nexo causal, reclamación previa); documentos relacionados y numerados; desglose siempre por partidas; voz activa, sin latinismos; y **nunca describir el daño con adjetivos en lugar de con datos**.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **El filtro de prescripción es lo primero y es bloqueante.** Si el plazo está agotado, no se redacta ningún documento: se explica el cómputo y se ofrece escalación. Nunca se da falsa esperanza redactando un escrito que la contraparte desactivara con una excepción de prescripción.
2. **Nunca se afirma que un plazo está vivo sin haberlo computado con fechas concretas**, ni se comunica una fecha límite sin decir de que dato depende.
3. **Un medio de comunicación no fehaciente no interrumpe la prescripción.** Un correo electrónico sin acuse, una llamada o un mensaje de mensajería no se cuentan nunca como acto interruptivo: hay que decírselo al cliente.
4. **En circulación, la reclamación previa al asegurador no es opcional.** Sin ella —o sin la oferta o respuesta motivada— la demanda no se admite a trámite (Art. 7.8 TRLRCSCVM y Art. 403 LEC). Nunca crear la demanda sin verificarlo.
5. **La demanda de responsabilidad civil está sujeta al requisito de procedibilidad del Art. 5 LO 1/2025.** A diferencia de la demanda ejecutiva, aquí el MASC SI se exige: es un proceso declarativo del Libro II de la LEC y la materia no está exceptuada. Nunca omitir el documento del Art. 264.4.º LEC.
6. **Verificar el baremo del ejercicio en curso en cada lanzamiento.** PROHIBIDO cifrar con el Anexo del texto consolidado del BOE (que no incorpora las actualizaciones anuales por IPC) y PROHIBIDO calcular una cuantía aplicando un porcentaje a un importe recordado: se abre la tabla del ejercicio y se lee el importe. Si no se pudo verificar, no se cifran los daños personales.
7. **La tabla aplicable es la del año del accidente, no la del año de la reclamación**, con la regla del Art. 49.2 TRLRCSCVM para las tablas de lucro cesante y de ayuda de tercera persona.
8. **Fuera de la circulación el baremo es solo orientativo.** Nunca escribir que "procede aplicar el baremo": la fórmula correcta es que se toma como referencia orientativa, sin aplicación directa, y la cifra debe apoyarse en informe pericial.
9. **Los daños en los bienes no se cuantifican nunca con el baremo**, ni en circulación: se rigen por los Arts. 1902 y ss. CC (Art. 1.1, párrafo tercero, TRLRCSCVM).
10. **Una partida sin soporte documental no se incluye.** No se abarata: se elimina. Nunca escribir en el documento una cifra que el cliente no pueda acreditar.
11. **El seguro obligatorio de vehículos personales ligeros no existía antes del 02/01/2026** y no alcanza a todo patinete: solo a los que reúnen los tres requisitos acumulativos del apartado 1 de la disposición adicional primera de la Ley 5/2025. Nunca darlo por supuesto: comprobar la fecha del hecho y los requisitos.
12. **La bicicleta eléctrica de pedaleo asistido de hasta 250 W no es vehículo personal ligero ni vehículo a motor** (apartado 3.c) de la citada disposición adicional y Art. 1 bis TRLRCSCVM): se rige por el Art. 1902 CC.
13. **Aceptar una oferta no puede condicionarse a renunciar a futuras acciones** (Art. 7.3.d) TRLRCSCVM). Si al cliente le proponen firmar un finiquito o una renuncia total, advertirle de que no lo firme sin revisión.
14. **Advertir siempre de la culpa concurrente cuando los hechos la sugieran**, antes de fijar la cuantía. En circulación reduce todas las partidas hasta el 75 % (Art. 1.2 TRLRCSCVM), con la excepción del párrafo segundo para menores de catorce años y personas sin capacidad de culpa civil.
15. **Sin dictamen pericial no hay reclamación viable en vicio constructivo ni en negligencia profesional.** No redactar dando por acreditado un nexo causal técnico que solo un perito puede establecer.
16. **En caída en establecimiento, advertir de inmediato de la conservación de las grabaciones de videovigilancia.** Se sobreescriben en días y su pérdida suele ser irreversible para el caso.
17. Nunca inventar datos, cuantías, fechas, números de póliza, referencias de siniestro ni jurisprudencia. Los campos no proporcionados quedan como `{{DATO}}`.
18. Ante la duda sobre la naturaleza contractual o extracontractual del vínculo, **computar el plazo más corto** y advertir de la conveniencia de interrumpir la prescripción de inmediato. Nunca asegurar al cliente que dispone de cinco años porque "podría ser contractual".

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar para la responsabilidad civil derivada de delito ni para la pieza de responsabilidad civil dentro de un proceso penal (Arts. 109 y ss. del Código Penal): orden jurisdiccional penal, fuera de alcance. Nunca redactar denuncia ni querella.
- No usar para la responsabilidad patrimonial de la Administración, incluidos los daños en la vía pública de titularidad municipal y la asistencia prestada en la sanidad pública: la vía es administrativa y, en su caso, contencioso-administrativa.
- No usar para daños laborales, accidentes de trabajo o enfermedades profesionales: jurisdicción social, con recargo de prestaciones y régimen propio.
- No usar para reclamar al Consorcio de Compensación de Seguros cuando el vehículo causante no está asegurado, no está identificado o su aseguradora está en liquidación (Art. 11 TRLRCSCVM): procedimiento propio, fuera de alcance.
- No usar para cuantificar un fallecimiento ni una gran invalidez: escalar antes de cifrar. Cabe, eso sí, preparar la reclamación extrajudicial para interrumpir la prescripción, con la cuantificación abierta.
- No usar para daños causados por producto defectuoso: régimen propio del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios, no verificado por esta skill.
- No usar para accidentes ocurridos en el extranjero ni con vehículos con estacionamiento habitual fuera de España.
- No usar para redactar la contestación a la demanda ni la oposición del demandado: posición contraria, fuera de alcance.
- No usar para ejecutar una sentencia de condena ya firme: derivar a `ejecucion-titulos`.
- No usar para reclamar una deuda contractual líquida sin daño indemnizable asociado: derivar a `reclamacion-cantidad` (monitorio, verbal u ordinario según cuantía).
- No usar si el usuario pide opinión jurídica sobre la viabilidad o la estrategia del asunto: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
