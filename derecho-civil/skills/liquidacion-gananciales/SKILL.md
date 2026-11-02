---
name: liquidacion-gananciales
title: Liquidación de gananciales
i18n:
  en:
    name: community-property-liquidation
    title: Community property liquidation
    description: >
      Generates the documents to liquidate the community of property (sociedad de gananciales)
      under Arts. 1392 and 1396 to 1410 of the **Civil Code**, which governs the community of
      property, its dissolution and liquidation, and Arts. 806 to 810 of the **Civil Procedure
      Act (Law 1/2000, LEC)**, verified in the BOE: (1) WITH AGREEMENT, a liquidation agreement
      with inventory, valuation, settlement and allocations, which may stand alone, be raised to
      a public deed if there is real estate, or be included in the divorce regulatory agreement
      (Art. 90.1.e CC); and (2) WITHOUT AGREEMENT, the inventory proposal of Art. 808.2 LEC and
      the application to the court for formation of inventory (Arts. 807 and 808 LEC). It
      explains the presumption of community property, reimbursements between estates, the effect
      of allocating a mortgaged home and excess allocation. Do not use under separation of
      property, under the participation regime (Art. 811 LEC), under regional civil law regimes,
      or where there is a family business, companies, assets abroad, tax or Social Security
      debts or indications of concealment of assets, in which case it stops and escalates.
description: >
  Genera los documentos para liquidar la sociedad de gananciales conforme a los Arts. 1392 y 1396 a 1410 del
  **Código Civil**, que regula la sociedad de gananciales, su disolución y su liquidación, y a los Arts. 806 a 810 de la **Ley 1/2000 de Enjuiciamiento Civil (LEC)**, verificados en el BOE: (1) CON ACUERDO — convenio de
  liquidación con la estructura de inventario, avalúo, liquidación y adjudicaciones, que puede documentarse de
  forma autónoma, elevarse a escritura pública si hay inmuebles, o integrarse en el convenio regulador del
  divorcio (Art. 90.1.e) CC); y (2) SIN ACUERDO — propuesta de inventario del Art. 808.2 LEC y solicitud
  judicial de formación de inventario ante el juzgado del proceso matrimonial (Arts. 807 y 808 LEC). Explica la
  presunción de ganancialidad del Art. 1361 CC, los reintegros entre masas del Art. 1358 CC, el efecto real de
  adjudicar una vivienda hipotecada y el exceso de adjudicación. NO usar en régimen de separación de bienes (no
  hay masa común que liquidar), en régimen de participación (Art. 811 LEC, cauce distinto), en regímenes de
  derecho civil propio o foral, ni cuando haya empresa familiar, sociedades, patrimonio en el extranjero, deudas
  con Hacienda o la Seguridad Social o indicios de ocultación de bienes: en esos casos se detiene y escala.
when_to_use: |
  - El usuario se está divorciando o separando y necesita repartir los bienes y deudas del matrimonio.
  - El usuario ya está divorciado y la sociedad de gananciales sigue sin liquidar.
  - El usuario pide un convenio de liquidación de gananciales, un inventario de bienes gananciales o una
    solicitud judicial de formación de inventario.
  - El usuario discute con su cónyuge si un bien concreto es privativo o ganancial.
  - El usuario aportó dinero propio (una herencia, una donación, ahorros anteriores) a un bien común, o al
    contrario, y quiere recuperarlo en el reparto.
  - El usuario quiere quedarse la vivienda familiar hipotecada, o que se la quede el otro cónyuge.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - regimen: sociedad de gananciales / separación de bienes / participación / desconocido
  - acuerdo: existe acuerdo sobre el inventario y el reparto / no existe acuerdo
  - momento: liquidación unida a un proceso matrimonial en curso / posterior a una resolución ya firme
  - vivienda_hipotecada: existe vivienda familiar con préstamo hipotecario pendiente (sí / no)
  - datos_conyuges: nombre, NIF y domicilio de cada cónyuge
  - datos_matrimonio: fecha y lugar de celebración, registro civil, origen del régimen
  - disolucion: estado (ya disuelta / en curso / no disuelta), y fecha y causa de la disolución o fecha de referencia del inventario (Arts. 1392 y 1397.1.º CC)
  - datos_proceso_matrimonial: juzgado, clase de procedimiento, número de autos, fecha de admisión o de firmeza
  - activo: relación de bienes gananciales con su valor, y créditos de la sociedad contra un cónyuge
  - pasivo: deudas pendientes a cargo de la sociedad, y reintegros debidos a cada cónyuge con su actualización
  - bienes_discutidos: bienes cuyo carácter privativo o ganancial se discute, y prueba disponible de cada uno
  - datos_vivienda: dirección, datos registrales, referencia catastral, valor, entidad acreedora y saldo pendiente
  - adjudicaciones: bienes que se adjudican a cada cónyuge y su valor
  - compensacion: importe, forma y medio de pago del exceso de adjudicación, si lo hay
  - documentos: documentos justificativos de cada partida del inventario
  - postulacion: procurador y letrado, en la vía judicial
outputs:
  - convenio_liquidacion_gananciales: convenio de liquidación en markdown, DRAFT
  - propuesta_inventario: propuesta de inventario del Art. 808.2 LEC en markdown, DRAFT
  - solicitud_formacion_inventario: solicitud judicial de formación de inventario en markdown, DRAFT
references:
  - references/cc-activo-pasivo-y-presuncion.md
  - references/cc-liquidacion-division-adjudicacion.md
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/lec-procedimiento-liquidacion-806-811.md
  - references/vivienda-hipotecada-y-exceso-adjudicacion.md
assets:
  - assets/template-convenio-liquidacion-gananciales.md
  - assets/template-propuesta-inventario.md
  - assets/template-solicitud-formacion-inventario.md
---

# Liquidación de la Sociedad de Gananciales

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
      "id": "regimen",
      "rationale": "Resolver V4: solo la sociedad de gananciales genera masa común liquidable; los demás regímenes quedan fuera del alcance de esta skill.",
      "question": "¿Cuál es el régimen económico matrimonial?",
      "options": [
        {"id": "gananciales", "label": "Sociedad de gananciales"},
        {"id": "separacion_bienes", "label": "Separación de bienes"},
        {"id": "participacion", "label": "Régimen de participación"},
        {"id": "desconocido", "label": "No lo sé con certeza"}
      ]
    },
    {
      "id": "acuerdo",
      "rationale": "Resolver V1: el acuerdo genera convenio de liquidación y su ausencia el procedimiento judicial de los artículos 806 y siguientes de la LEC.",
      "question": "¿Hay acuerdo sobre el inventario y el reparto?",
      "options": [
        {"id": "con_acuerdo", "label": "Sí, hay acuerdo entre los cónyuges"},
        {"id": "sin_acuerdo", "label": "No hay acuerdo"}
      ]
    },
    {
      "id": "momento",
      "rationale": "Resolver V2: determina el bloque condicional de eficacia y si la liquidación se une a un proceso matrimonial en curso.",
      "question": "¿En qué momento se plantea la liquidación?",
      "options": [
        {"id": "unida_a_proceso", "label": "Unida a un proceso matrimonial todavía en curso"},
        {"id": "posterior_a_firmeza", "label": "Posterior a una resolución ya firme"}
      ]
    },
    {
      "id": "vivienda_hipotecada",
      "rationale": "Resolver V3: la vivienda con préstamo hipotecario pendiente exige tratar el exceso de adjudicación y la subsistencia de la responsabilidad frente al banco.",
      "question": "¿Hay vivienda familiar con préstamo hipotecario pendiente?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — respuesta a `acuerdo`
- `V2` — respuesta a `momento`
- `V3` — respuesta a `vivienda_hipotecada`
- `V4` — respuesta a `regimen`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalúa en este orden:

- Si V4 = separacion_bienes → **DETENER**: en el régimen de separación de bienes no existe masa común de bienes y derechos (Art. 1435 CC), por lo que **no hay sociedad que liquidar** y el procedimiento de los Arts. 806 y siguientes de la LEC no es aplicable. Explicarlo con el texto fijo de la Fase 3 para este supuesto, informar de que si existen bienes adquiridos por ambos en proindiviso su reparto es una división de cosa común (Arts. 400 y siguientes del Código Civil) y no una liquidación de régimen, y ofrecer escalación. **No crear ningún documento.**
- Si V4 = participación → **DETENER**: el régimen de participación se liquida por el Art. 811 de la LEC, cuya propuesta exige una estimación del patrimonio inicial y final de cada cónyuge, no un inventario de masa común. Los assets de esta skill no sirven para ese cauce. Advertir y escalar. **No crear ningún documento.**
- Si V4 = desconocido → **NO ENRUTAR TODAVÍA**: el régimen económico determina si hay masa común que liquidar y no puede presumirse. Pide en el chat las capitulaciones matrimoniales, o en su defecto la certificación literal de matrimonio del Registro Civil, donde constan inscritas. Explica que a falta de capitulaciones el régimen legal supletorio es el de gananciales en el derecho común, pero que varía en los territorios con derecho civil propio. Solo cuando el régimen quede acreditado, vuelve a evaluar este enrutamiento. **No crear ningún documento mientras el régimen sea desconocido.**
- Si concurre el vector de guarda de derecho civil propio o foral → **DETENER**: verificar la norma autonómica aplicable y escalar. **No crear ningún documento.**
- Si V4 = gananciales y V1 = con acuerdo (acuerdo) → **HOJA CONVENIO**: `assets/template-convenio-liquidacion-gananciales.md`. V2 determina el bloque condicional de eficacia (integración en el proceso matrimonial en curso, o convenio autónomo) y V3 el bloque condicional de la vivienda hipotecada.
- Si V4 = gananciales y V1 = sin acuerdo (sin acuerdo) → **HOJA JUDICIAL**: dos documentos, en este orden: primero `assets/template-propuesta-inventario.md` (es el contenido sustantivo y la propuesta que el Art. 808.2 LEC exige acompañar) y después `assets/template-solicitud-formacion-inventario.md` (el escrito procesal, que se remite a la propuesta). V2 determina el bloque condicional del hecho tercero de la solicitud y V3 el tratamiento de la vivienda dentro del inventario.
- Si V1 = sin_acuerdo pero el cliente manifiesta que aún no ha intentado el acuerdo → antes de enrutar a la HOJA JUDICIAL, aplica la explicación de la sección de diálogo previo descrita más abajo: no se le impone el acuerdo, pero se le informa del coste real de la vía judicial. Si tras la explicación decide intentar el acuerdo, reenruta a la HOJA CONVENIO.
- Si el usuario pide únicamente la propuesta de inventario como documento de trabajo para remitírsela a su cónyuge o a su abogado, sin escrito judicial → generar solo `assets/template-propuesta-inventario.md`, sin la solicitud.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **Estado de la disolución (Art. 1392 CC), en las dos hojas — distinguir tres situaciones y NO confundirlas.** La causa de disolución es la disolución del matrimonio, la declaración de nulidad, la separación legal o el pacto de otro régimen en capitulaciones.
  1. **Sociedad ya disuelta** (resolución matrimonial firme, o capitulaciones ya otorgadas): confirmar la fecha y la causa, y activar en el asset los bloques de disolución ya producida y de fecha de corte.
  2. **Disolución en curso** (demanda matrimonial admitida a trámite, aun sin resolución firme): **la sociedad NO está todavía disuelta, y eso no impide continuar.** El Art. 808.1 LEC permite expresamente solicitar la formación de inventario "admitida la demanda de nulidad, separación o divorcio", es decir, **antes de que la disolución se produzca**; y en la vía de acuerdo, la liquidación se pacta como extremo del convenio regulador y despliega su eficacia con la aprobación judicial (Art. 90.1.e) CC). Activar los bloques condicionales de disolución en curso y de fecha de referencia. **PROHIBIDO escribir que la sociedad "quedó disuelta" cuando aún no lo está**, y prohibido decirle al cliente que debe esperar a la sentencia para pedir el inventario. Advertir, en cambio, de que **la segunda fase, la solicitud de liquidación del Art. 810.1 LEC, si exige que sea firme la resolución que declare disuelto el régimen**: el inventario puede formarse antes, la división no.
  3. **Solo separación de hecho, sin demanda matrimonial presentada ni capitulaciones:** la sociedad sigue vigente y no hay cauce. Informar de que para liquidarla hace falta antes disolverla (demanda de separación o divorcio, o capitulaciones pactando otro régimen), **no crear ningún documento** y ofrecer derivación a `divorcio`.
- **Fecha de corte o de referencia del inventario (Art. 1397.1.º CC), en las dos hojas.** Si la sociedad ya está disuelta, fijar la fecha de disolución como fecha de corte y advertir de que los bienes adquiridos y las deudas contraídas después no entran en el inventario; si el cliente pretende inventariar un bien posterior, explicarlo y no incluirlo. Si la disolución está en curso, fijar una fecha de referencia expresa, advertir de que el activo lo determinará el momento de la disolución y recoger el compromiso de actualizar el inventario si media alguna alteración relevante.
- **Presupuesto temporal del Art. 808.1 LEC (HOJA JUDICIAL).** Confirmar que la demanda matrimonial está admitida a trámite o que el proceso de disolución está iniciado. Si el cliente aún no ha presentado ninguna demanda matrimonial y no hay resolución firme, la solicitud de inventario es prematura: advertirlo y derivar a `divorcio`. Si el divorcio ya es firme, aplicar la posición conservadora del punto 1 del apartado "Verificar manualmente" de `references/fuentes-plantillas-validadas.md`: tramitar ante el juzgado que conoció del divorcio y advertir al cliente de que conviene confirmar el criterio del juzgado antes de presentar. **Nunca afirmar que el Art. 808.1 contempla literalmente el supuesto de sentencia ya firme.**
- **Competencia (Art. 807 LEC, HOJA JUDICIAL).** Es competente el juzgado que está conociendo, ha conocido o hubiera tenido la competencia para conocer del proceso matrimonial. **No hay elección de fuero ni sumisión posible:** nunca preguntar al cliente en que juzgado desea presentarlo; preguntar cuál conoció o está conociendo de su proceso matrimonial. Si el proceso se siguió ante un Juzgado de Violencia sobre la Mujer, concurren por definición los presupuestos del guardrail de violencia del plugin: detener y escalar.
- **Masa común con contenido (Art. 806 LEC), en las dos hojas.** Si tras recorrer el inventario resulta que no existe ningún bien ni deuda ganancial, no hay nada que liquidar: informarlo y no generar un documento vacío.
- **Pasivo superior al activo, en las dos hojas.** Si el pasivo inventariado supera al activo, no hay remanente que dividir conforme al Art. 1404 CC. Advertirlo expresamente, activar el bloque condicional correspondiente del asset y tratar la contribución de cada cónyuge al déficit. **Nunca escribir un haber negativo como si fuera un reparto ordinario.**
- **Supuestos de escalación patrimonial, en las dos hojas.** Si el inventario incluye empresa familiar, participaciones en sociedades, explotación económica en funcionamiento o patrimonio situado en el extranjero, detener y escalar antes de valorar esas partidas. Si existen deudas con la Agencia Tributaria o con la Tesorería General de la Seguridad Social, detener y escalar: su tratamiento en la liquidación y la responsabilidad de cada cónyuge exigen análisis especializado. Si el cliente manifiesta indicios de que el otro cónyuge ha ocultado, distraído o enajenado bienes, detener y escalar: la partida del Art. 1397.2.º CC y las medidas de aseguramiento exigen estrategia procesal propia.
- **Documentación de las partidas (Art. 808.2 LEC, HOJA JUDICIAL).** Cada partida de la propuesta necesita su documento justificativo. Al recorrer el inventario, preguntar por el documento de cada partida y advertir expresamente de las que queden sin justificación documental. No presentar como acreditada una partida que no lo está.
- **Prueba del carácter privativo (Art. 1361 CC), en las dos hojas.** Nunca escribir que un bien es privativo por la sola afirmación del cliente. Preguntar con que documentación lo acredita y, si no la hay, advertir de que la presunción de ganancialidad opera contra su pretensión y que la carga de la prueba le corresponde.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 1.344 a 1.410 del Código Civil (sociedad de gananciales, activo, pasivo, cargas y liquidación), y Arts. 806 a 811 de la Ley de Enjuiciamiento Civil (procedimiento para la liquidación del régimen económico matrimonial).
2. **Orientación Legal del Caso:**

**Informa el cauce y la fuente aplicable.** Textos fijos por hoja:
   - CONVENIO: "A su caso corresponde la liquidación de la sociedad de gananciales de mutuo acuerdo, que se rige por los artículos 1392 y 1396 a 1410 del Código Civil. El artículo 806 de la Ley 1/2000, de Enjuiciamiento Civil, reserva el procedimiento judicial para el caso de falta de acuerdo entre los cónyuges, de modo que, existiendo acuerdo, no es necesario acudir a él. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - JUDICIAL: "A su caso corresponde el procedimiento de liquidación del régimen económico matrimonial de los artículos 806 a 810 de la Ley 1/2000, de Enjuiciamiento Civil, que se desarrolla en dos fases sucesivas: primero la formación del inventario y después la liquidación y división. La solicitud de formación de inventario debe acompañarse de una propuesta con las partidas debidamente separadas y de los documentos que las justifiquen, conforme al artículo 808.2 de dicha ley. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - En la HOJA JUDICIAL, añadir: "Los artículos 807, 808 y 810 de la Ley de Enjuiciamiento Civil se encuentran en la redacción dada por la Ley Orgánica 2/2022, de 21 de marzo, vigente desde el 23 de marzo de 2022, que ha sido la verificada."
   - En la HOJA JUDICIAL, si V2 = unida a proceso (proceso matrimonial en curso), añadir: "No es necesario esperar a la sentencia para iniciar esta primera fase: el artículo 808.1 de la Ley de Enjuiciamiento Civil permite solicitar la formación de inventario desde que la demanda de separación o divorcio ha sido admitida a trámite. Lo que si requiere que la resolución sea firme es la segunda fase, la solicitud de liquidación y división del artículo 810.1 de la misma ley."
   - En la HOJA CONVENIO, si V2 = unida a proceso (proceso matrimonial en curso), añadir: "Al encontrarse su proceso matrimonial en trámite, la liquidación puede incorporarse al convenio regulador como uno de sus extremos, conforme al artículo 90.1.e) del Código Civil."
   - En la HOJA CONVENIO, si el inventario comprende inmuebles, añadir: "Si el inventario comprende bienes inmuebles, el convenio deberá elevarse a escritura pública notarial para poder inscribir las adjudicaciones en el Registro de la Propiedad."
   - **Texto fijo de DETENCIÓN por separación de bienes** (V4 = separacion_bienes; se emite en lugar de todo lo anterior y no se ofrece plantilla ni se crea documento): "En el régimen de separación de bienes no existe una masa común de bienes y derechos, por lo que no hay sociedad conyugal que liquidar: cada cónyuge conserva la titularidad de lo que le pertenece, conforme al artículo 1435 del Código Civil, y el procedimiento de los artículos 806 y siguientes de la Ley de Enjuiciamiento Civil no le resulta aplicable, pues ese artículo lo circunscribe a los regímenes que determinan la existencia de una masa común. Si durante el matrimonio adquirieron bienes conjuntamente, esos bienes les pertenecen en proindiviso y su reparto se articula como una división de cosa común de los artículos 400 y siguientes del Código Civil, que es una operación distinta. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - **Texto fijo de DETENCIÓN por régimen de participación** (V4 = participación): "El régimen de participación no se liquida mediante el inventario de una masa común, porque no existe tal masa: en el, cada cónyuge conserva su propio patrimonio y lo que se liquida es un derecho de crédito a participar en las ganancias del otro, conforme al artículo 1411 del Código Civil. Su liquidación se rige por el artículo 811 de la Ley de Enjuiciamiento Civil y exige una propuesta con la estimación del patrimonio inicial y final de cada cónyuge, de contenido distinto al de las plantillas de que disponemos. Le recomiendo la intervención de un abogado especializado. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
### Diálogo previo sobre la vía cuando no se ha intentado el acuerdo

Si V1 = sin acuerdo (sin acuerdo) y el cliente no ha intentado realmente negociar, antes de crear los documentos judiciales explícaselo con este contenido (redáctalo con tus palabras, en registro formal, sin listas numeradas ni mecánica interna): el procedimiento judicial se desarrolla en dos fases sucesivas —primero se determina qué bienes y deudas componen la masa común, y solo después se reparte—; cada fase tiene su comparecencia, su posible juicio verbal o su nombramiento de contador y peritos, y su propia vía de recurso; los plazos de diez días que fija la ley son los de señalamiento por el Letrado de la Administración de Justicia, no la duración del procedimiento, que en la práctica se mide en meses o años; y el coste del contador y de los peritos recae sobre la propia masa a repartir. Añade que el acuerdo, cuando es posible, se documenta en semanas y deja el reparto en manos de los cónyuges en lugar de en las de un contador. Termina preguntando si desea intentar el acuerdo antes o prefiere preparar ya la vía judicial. **No presiones ni condiciones la continuación a que acepte negociar:** informado el cliente, respeta su decisión.

3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada **que ha resuelto el enrutamiento de la Fase 1.3** (menciónala por su denominación formal, sin mostrar rutas internas ni volcar su contenido). Si el enrutamiento asigno varios documentos, nómbralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada** ni la primera del inventario de la sección de assets.
4. **Elección de Plantilla Base:** Aplica el protocolo universal de `REG-AST-01` (`CLAUDE.md`), convocando en ese mismo turno el formulario interactivo `restricted_human_in_the_loop_request` para que el usuario elija entre la plantilla del sistema o aportar su propia minuta.

### 2.3 Manejo Determinista de la Elección
Aplica rigurosamente el protocolo de `REG-AST-01` (`CLAUDE.md`): si se selecciona `plantilla_sistema`, carga la plantilla oficial y avanza a la **Fase 3**; si se selecciona `plantilla_usuario`, requiere la minuta (si no consta ya en el chat), ejecuta el control de legalidad y avanza a la **Fase 3**.
---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

Aplica rigurosamente la directiva `REG-DOC-01` y la sección 6.1 de `CLAUDE.md`:
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

### Secciones — HOJA CONVENIO (`convenio-liquidacion-gananciales.md`)

1. **Primer cónyuge** *(dato objetivo — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por la identificación de ambos cónyuges." Búsqueda prioritaria con `search_clients`, volcado directo a disco per `REG-CLI-04`, sustituyendo exhaustivamente los nombres en todas sus apariciones a lo largo del documento (título/encabezado H1, comparecencia y firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones), informe en chat y continúe sin confirmación previa en chat.
2. **Segundo cónyuge** *(dato objetivo — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Identificado el primer cónyuge, pasamos al segundo." Búsqueda prioritaria con `search_clients`, volcado directo a disco per `REG-CLI-04`, sustituyendo exhaustivamente los nombres en todas sus apariciones (título H1, comparecencia y firmas), informe en chat y continúe sin confirmación previa en chat.
3. **Matrimonio y disolución de la sociedad** *(dato objetivo con validación — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Pasamos a los datos del matrimonio y a la disolución de la sociedad de gananciales." Solicita en bloque mediante `slot_filling_request`: a) fecha y lugar de celebración; b) registro civil de inscripción; c) origen del régimen; d) fecha y causa de la disolución (o de admisión de la demanda). Aplica validaciones, muestra vista previa en chat, pide confirmación y aplica `edit_file`.
4. **Activo: bienes gananciales** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Pasamos ahora al inventario del activo: los bienes y derechos comunes." Explica antes de pedir la relación, con base en `references/cc-activo-pasivo-y-presuncion.md`. Después solicita la relación de bienes y sus datos (descripción, valor, datos registrales y referencia catastral en inmuebles). Vista previa en chat, confirmación y `edit_file`.
5. **Activo: créditos de la sociedad contra un cónyuge** *(cláusula de negociación — explicar antes de decidir; condicional)*. Anuncio fijo: "Determinamos si la sociedad tiene algún crédito frente a uno de ustedes." Explica el Art. 1397.3.º CC: si la sociedad pago con dinero común algo que era de cargo de uno solo (la hipoteca de un piso privativo, una deuda personal, una mejora en un bien privativo), la sociedad tiene un crédito contra él, que entra en el activo por su importe **actualizado** al tiempo de la liquidación. Pregunta si concurre algún supuesto y, por cada uno, concepto, importe original, criterio de actualización e importe resultante. Si no hay ninguno, omite el bloque sin dejar rastro.
6. **Pasivo: deudas pendientes a cargo de la sociedad** *(dato objetivo con validación — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Pasamos al pasivo: las deudas pendientes a cargo de la sociedad." Solicita las deudas en bloque mediante `slot_filling_request`: concepto, acreedor y **saldo pendiente certificado a una fecha concreta**. Vista previa en chat, confirmación y `edit_file`.
7. **Pasivo: reintegros y reembolsos a favor de un cónyuge** *(cláusula de negociación — explicar antes de decidir; la sección que más dinero mueve)*. Anuncio fijo: "Corresponde ahora determinar los reintegros que la sociedad deba a cada uno de ustedes." **Esta sección no se omite nunca por silencio del cliente: el cliente no la conoce y no la va a mencionar por su cuenta, de modo que hay que preguntarla activamente.** Explica antes de preguntar, con base en `references/cc-activo-pasivo-y-presuncion.md`, apartado 4: que el artículo 1358 del Código Civil establece que, cuando una masa paga lo que corresponde a la otra, hay que reembolsar el valor satisfecho **por su importe actualizado al tiempo de la liquidación**, no por la cifra nominal de entonces; que funciona en los dos sentidos; que el reintegro no convierte al aportante en propietario de una cuota mayor del bien, sino en acreedor; y que hay que poder acreditarlo documentalmente. Después pregunta expresamente, en turnos separados: a) si alguno de ustedes aportó dinero propio —de una herencia, de una donación o de ahorros anteriores al matrimonio— a la compra, la entrada, la hipoteca o la reforma de un bien común, y con que documentación puede acreditarlo; b) si alguno pago con dinero propio deudas o gastos que eran de cargo de la sociedad (Art. 1364 CC). Por cada reintegro reconocido: concepto, importe original, criterio de actualización pactado e importe resultante. Si el cliente no puede acreditar una aportación, adviértele de que sin justificación documental el reintegro es una pretensión discutible y registra el dato solo si ambos cónyuges lo reconocen expresamente en el convenio.
8. **Liquidación y haber de cada cónyuge** *(dato objetivo calculado — no se pregunta, se muestra)*. Anuncio fijo: "Con el inventario cerrado, procedemos a la liquidación y a la determinación del haber de cada uno." No pidas ninguna cifra nueva: calcula el total del activo, el total del pasivo, el haber líquido y la mitad de cada cónyuge (Arts. 1344 y 1404 CC), aplica las compensaciones del Art. 1403 CC por reintegros y créditos, y muestra la operación completa paso a paso en la vista previa para que el cliente pueda comprobarla. Al escribir el bloque del Art. 1403 en el documento, **suprime los sumandos cuyo importe sea cero en lugar de escribir "0 euros"**: si un cónyuge no tiene reintegros a su favor ni créditos de la sociedad en su contra, se hace constar así en una frase, no con una enumeración de ceros. Explica que **la división por mitad es el resultado legal y no un punto negociable**: si un cónyuge quiere ceder valor al otro, eso es un negocio distinto (una donación) con su propio tratamiento, y debes advertirlo. Si el pasivo supera el activo, aplica la validación correspondiente y trata la contribución al déficit.
9. **Vivienda familiar y préstamo hipotecario** *(cláusula de negociación — explicar antes de decidir; solo si V3 = Sí)*. Anuncio fijo: "Abordamos ahora la vivienda familiar y el préstamo hipotecario que la grava." **Explica PRIMERO, y confirma que el cliente lo ha entendido, antes de escribir cualquier cláusula**, con base en `references/vivienda-hipotecada-y-exceso-adjudicacion.md`: que adjudicar la vivienda a uno de los cónyuges **no libera al otro frente al banco**; que la entidad no firma el convenio, no es parte en el y no queda vinculada por lo que ambos pacten; que si firmaron el préstamo los dos, los dos siguen obligados frente a ella y puede reclamar a cualquiera de los dos con independencia de quién se quede la casa; que lo que si produce el convenio es un efecto interno, la obligación del adjudicatario de pagar y de mantener indemne al otro, con acción de repetición si este acaba pagando (Arts. 1367 y 1401 CC); y que **la única forma de liberar de verdad al otro cónyuge es que la entidad lo acepte mediante una novación subjetiva del préstamo, decisión que corresponde solo a la entidad y que puede denegar.** Solo después pide, en turnos separados: a) dirección, datos registrales y referencia catastral; b) valor atribuido de común acuerdo; c) entidad acreedora y datos de la escritura de préstamo; d) saldo pendiente certificado y su fecha; e) quiénes figuran como prestatarios en la escritura de préstamo; f) a quién se adjudica la vivienda; g) si ya se ha consultado a la entidad la novación subjetiva y cuál fue su respuesta. **Está PROHIBIDO redactar una cláusula que afirme que el cónyuge no adjudicatario queda liberado frente a la entidad.** Usa siempre la estructura del asset: asunción interna, obligación de mantener indemne, compromiso de solicitar la novación y advertencia expresa de que la liberación depende de la entidad.
10. **Adjudicaciones** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Pasamos al reparto: la adjudicación concreta de los bienes a cada uno de ustedes." Explica antes de preguntar: que se procura la igualdad de los lotes (Art. 1410 CC, por remisión a la partición de herencia); que cada cónyuge tiene derecho a que se incluyan con preferencia en su haber sus bienes de uso personal, la explotación económica que gestione efectivamente y el local donde ejerza su profesión (Art. 1406 CC); y **que la preferencia legal sobre la vivienda habitual del Art. 1406.4.º opera solo en caso de fallecimiento del otro cónyuge, no en el divorcio: en un divorcio ningún cónyuge tiene derecho legal preferente a que se le adjudique la vivienda familiar.** No afirmes nunca lo contrario. Advierte también de que la atribución del **uso** de la vivienda es una medida del divorcio (Art. 96 CC), distinta de la adjudicación de la **propiedad** que aquí se decide. Después pide bien por bien, en turnos separados, a quién se adjudica, y ve mostrando el valor acumulado de cada lote frente al haber de cada uno. **Un lote se valora NETO de la deuda pendiente que su titular asume y que grava un bien de ese lote**: el valor que se contrasta con el haber es el de los bienes adjudicados menos esa deuda, no el valor bruto del bien. Adjudicar una vivienda de 240.000 euros con 80.000 euros de hipoteca pendiente que el adjudicatario asume supone un lote de 160.000 euros, no de 240.000. Escribe siempre las dos cifras en el documento —valor de los bienes y valor neto tras deducir la deuda asumida— para que la operación sea verificable, y comprueba que la suma de los valores netos de los dos lotes coincide con la suma de los totales a percibir de la cláusula tercera.
11. **Exceso de adjudicación y compensación** *(cláusula de negociación — explicar antes de decidir; condicional)*. Anuncio fijo: "Comprobamos si el reparto produce un exceso de adjudicación que deba compensarse." Calcula tú mismo si el valor **neto** de un lote —el de los bienes adjudicados menos la deuda pendiente que su titular asume y que los grava— supera el total a percibir por su titular según la cláusula tercera. **Nunca compares el valor bruto de los bienes con el haber: en una vivienda hipotecada eso multiplica el exceso y arruina el reparto.** Si no hay exceso, infórmalo y omite la cláusula sin dejar rastro. Si lo hay: explica el Art. 1407 CC (quien recibe más de su haber abona la diferencia en dinero) y su causa habitual, la indivisibilidad de la vivienda; **advierte de que el exceso puede tener consecuencias fiscales, que su tratamiento depende de la normativa estatal y autonómica aplicable y de si el exceso resulta o no inevitable por la indivisibilidad del bien, y que debe consultarse con un asesor fiscal antes de firmar**; y expón las alternativas del cuadro de `references/vivienda-hipotecada-y-exceso-adjudicacion.md`, apartado 3 (compensación en metálico, asunción de más deuda, adjudicación de otros bienes, venta del inmueble y reparto del precio, o mantener la copropiedad temporalmente, advirtiendo de que esto último solo aplaza el conflicto a una futura división de cosa común). Después pide, en turnos separados: importe de la compensación (calculado por ti, a confirmar por el cliente), forma de pago y medio de pago. **Si el pago se aplaza, advierte expresamente al cónyuge acreedor de que la cláusula de finiquito declara liquidada la sociedad y de que, sin garantía, su único respaldo es una acción de reclamación frente a un obligado que ya ha recibido el bien**, y pregunta si desean pactar alguna garantía (condición resolutoria expresa inscribible sobre el inmueble adjudicado, aval, prenda o vencimiento anticipado por impago de un plazo). Si el cliente la quiere, recógela en la cláusula; si no, déjalo constar y no la inventes. **PROHIBIDO cuantificar el impuesto, citar tipos o exenciones, o afirmar que la operación está exenta.**
12. **Reparto de las deudas pendientes** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Corresponde ahora el reparto interno de las deudas pendientes." Explica, con la misma lógica que en la vivienda, que el reparto pactado rige entre ellos pero **no vincula a los acreedores, que conservan sus créditos frente al cónyuge deudor** (Arts. 1401 y 1402 CC), y que quien pague algo que según el convenio correspondía al otro podrá repetir contra él. Pregunta el reparto deuda por deuda. Si aparece una deuda con la Agencia Tributaria o con la Seguridad Social, aplica el guardrail: detener y escalar.
13. **Gastos e impuestos del convenio** *(cláusula de negociación)*. Anuncio fijo: "Determinamos como se reparten los gastos e impuestos derivados de este convenio." Explica que el pacto no altera las normas imperativas que determinan el sujeto pasivo de cada tributo. Pregunta el reparto (por mitad por defecto).
14. **Eficacia y formalización** *(dato objetivo con explicación)*. Anuncio fijo: "Cerramos determinando como se formalizara el convenio." Según V2 y el contenido del inventario, activa los bloques que correspondan: si el proceso matrimonial está en curso, el sometimiento a aprobación judicial como extremo del convenio regulador (Art. 90.1.e) CC); si es autónomo, la eficacia entre las partes desde la firma; y si el inventario comprende inmuebles, el compromiso de elevación a escritura pública, preguntando el plazo. Si el cliente aún no tiene convenio regulador y su proceso matrimonial está en curso, infórmale de que las demás medidas del divorcio (custodia, alimentos, uso de la vivienda, pensión compensatoria) se documentan en el convenio regulador y ofrece derivación a `divorcio`: esta skill cubre solo la parte patrimonial.
15. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Por último, el lugar y la fecha de la firma." Lugar de firma; fecha del día salvo indicación en contrario.

### Secciones — HOJA JUDICIAL, documento 1: propuesta de inventario (`propuesta-inventario.md`)

1. **Cónyuge solicitante** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Comenzamos por su identificación como parte solicitante." Solicita en bloque mediante `slot_filling_request`: a) nombre completo; b) NIF; c) domicilio. Vista previa en chat, confirmación y `edit_file`.
2. **Cónyuge contrario** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Pasamos a la identificación del otro cónyuge." Solicita en bloque mediante `slot_filling_request`: a) nombre completo; b) NIF; c) domicilio. Vista previa en chat, confirmación y `edit_file`.
3. **Matrimonio y disolución** *(dato objetivo con validación — `slot_filling_request` con confirmación en el chat)*. Igual que la sección 3 de la HOJA CONVENIO.
4. **Activo: bienes gananciales** *(cláusula de negociación — explicar antes de decidir)*. Igual que la sección 4 de la HOJA CONVENIO, con una diferencia esencial: aquí la propuesta se presenta frente a un cónyuge que discute, de modo que por cada partida hay que recoger también **el documento que la justifica** (Art. 808.2, párrafo segundo, LEC) y advertir de las que queden sin justificación.
5. **Activo: bienes enajenados por negocio ilegal o fraudulento** *(cláusula de negociación — condicional)*. Anuncio fijo: "Determinamos si algún bien común fue enajenado de forma irregular y debe reintegrarse a la masa." Explica el Art. 1397.2.º CC: si un bien común fue enajenado mediante negocio ilegal o fraudulento y no se ha recuperado, su valor actualizado se incluye en el activo. Advierte de que esta partida exige documentación de la enajenación y de su valor, y de que **no puede calificarse de fraudulenta la conducta del otro cónyuge sin base documental**. Si el cliente manifiesta indicios de ocultación o distracción de bienes, aplica el guardrail: detener y escalar antes de redactar la partida. Si no concurre el supuesto, omite el bloque sin dejar rastro.
6. **Activo: créditos de la sociedad contra un cónyuge** *(cláusula de negociación)*. Igual que la sección 5 de la HOJA CONVENIO, añadiendo el documento justificativo de cada partida.
7. **Pasivo: deudas pendientes a cargo de la sociedad** *(dato objetivo con validación)*. Igual que la sección 6 de la HOJA CONVENIO, añadiendo el documento justificativo de cada deuda.
8. **Pasivo: reintegros y reembolsos** *(cláusula de negociación — explicar antes de decidir)*. Igual que la sección 7 de la HOJA CONVENIO, con la misma obligación de preguntarla activamente, añadiendo el documento justificativo de cada reintegro. Aquí la exigencia probatoria es mayor: sin acuerdo del otro cónyuge, un reintegro no documentado será rechazado en la comparecencia.
9. **Partidas controvertidas** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Identificamos ahora las partidas que previsiblemente serán discutidas." Explica el Art. 809.2 LEC: si en la comparecencia se suscita controversia sobre la inclusión o exclusión de una partida o sobre su importe, el procedimiento continúa por los trámites del juicio verbal y se resuelve por sentencia. Explica de nuevo la presunción del Art. 1361 CC y, sobre todo, **quién tiene la carga de la prueba**: el cónyuge que sostiene el carácter privativo de un bien debe probarlo, y en defecto de prueba el bien queda en el activo ganancial. Por cada bien discutido pregunta, en turnos separados: descripción, carácter que le atribuye la parte contraria, motivo concreto por el que esta parte lo incluye en el activo, y prueba disponible. Aplica la regla de estilo de `references/estilo-redaccion-escritos.md`: no dar por pacifica la naturaleza de un bien discutido, y expresar el motivo concreto de la calificación, no una fórmula genérica.
10. **Documentos justificativos** *(dato objetivo con validación)*. Anuncio fijo: "Relacionamos los documentos que justifican cada partida del inventario." Recorre las partidas ya recogidas y confirma el documento de cada una, numerándolos correlativamente. Advierte expresamente de las partidas que queden sin documento y de la debilidad que eso supone ante la comparecencia. Recuerda también la consecuencia del Art. 809.1 LEC: **la incomparecencia injustificada de un cónyuge le tiene por conforme con la propuesta del que si comparece**, en ambos sentidos.
11. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos la propuesta con el lugar y la fecha."

### Secciones — HOJA JUDICIAL, documento 2: solicitud de formación de inventario (`solicitud-formacion-inventario.md`)

Al crear este documento, vuelca sin volver a preguntar todos los datos ya recogidos en la propuesta (cónyuges, matrimonio, disolución, bienes discutidos).

1. **Juzgado competente y proceso matrimonial** *(dato objetivo con explicación)*. Anuncio fijo: "Pasamos al escrito judicial: determinamos primero el juzgado competente." Explica el Art. 807 LEC: es competente el Juzgado de Primera Instancia que está conociendo, ha conocido o hubiera tenido la competencia para conocer del proceso de nulidad, separación o divorcio, **sin que sea posible elegir otro fuero ni someterse expresa o tácitamente a un juzgado distinto**. No preguntes en que juzgado desea presentarlo. Pregunta, en turnos separados: a) que juzgado conoció o está conociendo de su proceso matrimonial; b) clase de procedimiento y número de autos; c) según V2, fecha de admisión a trámite de la demanda matrimonial, o fecha de la sentencia y de su firmeza. Activa el bloque condicional del hecho tercero que corresponda a V2. Si V2 = posterior a firmeza, advierte de la posición conservadora sobre el cauce recogida en `references/fuentes-plantillas-validadas.md`, punto 1 de "Verificar manualmente": conviene confirmar el criterio del juzgado antes de presentar.
2. **Falta de acuerdo** *(dato objetivo)*. Anuncio fijo: "Concretamos en que ha consistido la falta de acuerdo." Pregunta brevemente en que puntos no ha sido posible el acuerdo. Aplica la regla de estilo: se describe el desacuerdo patrimonial de forma objetiva, **no se narra el conflicto conyugal ni se formulan reproches**. Redacta el hecho en una o dos frases.
3. **Bienes de carácter discutido** *(dato objetivo, condicional)*. Anuncio fijo: "Trasladamos al escrito los bienes cuyo carácter se discute." Ya resuelto en la propuesta: vuelca la información sin volver a preguntarla y activa el bloque condicional con la invocación del Art. 1361 CC y su carga de la prueba. Si no había bienes discutidos, omite el bloque.
4. **Medidas sobre administración y disposición de los bienes** *(cláusula de negociación — condicional)*. Anuncio fijo: "Valoramos si conviene pedir al Juzgado que resuelva sobre la administración y disposición de los bienes comunes." Explica el Art. 809.1, párrafo cuarto, LEC: el Tribunal resuelve lo procedente sobre administración y disposición de los bienes inventariados el mismo día de la comparecencia o el siguiente. Pregunta si existe riesgo concreto sobre algún bien común (que se venda, se grave o se vacíe una cuenta) y en que consiste. Si no hay riesgo concreto, omite el bloque: **no formules una petición genérica de medidas sin justificación**.
5. **Otrosí de aseguramiento** *(cláusula de negociación — condicional)*. Anuncio fijo: "Valoramos si procede solicitar alguna medida de aseguramiento." Solo si de la sección anterior resulta un riesgo concreto y acreditable. Pregunta la medida que se interesa y su justificación. Si el riesgo es serio o requiere medidas cautelares, escala: la estrategia cautelar excede el alcance de esta skill.
6. **Otrosí de requerimiento de documentación económica** *(cláusula de negociación — condicional)*. Anuncio fijo: "Valoramos si es necesario que el Juzgado requiera documentación a la parte contraria." Pregunta si hay documentación económica necesaria para determinar las partidas que obra en poder del otro cónyuge y a la que esta parte no tiene acceso. Pide la descripción concreta de esa documentación: **rechaza una petición genérica del tipo "toda su documentación bancaria"**, y pide que concrete entidad, periodo y concepto.
7. **Representación procesal** *(dato objetivo — confirmación agrupada por parte)*. Anuncio fijo: "Corresponde identificar la representación procesal." Sub-apartados: a) nombre del procurador; b) nombre del letrado. Confirmación agrupada. Trata abogado y procurador como preceptivos y redacta el fundamento de postulación en consecuencia (ver punto 7 de "Verificar manualmente" en `references/fuentes-plantillas-validadas.md`). Si el cliente pregunta si puede comparecer por sí mismo, indícale que lo confirme con su abogado o en el propio juzgado; **no afirmes que puede hacerlo**. Si aún no están designados, cada uno queda con su propio placeholder del asset, nunca ambos con el mismo marcador genérico.
8. **Documentos, lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con la relación de documentos, el lugar y la fecha." Numera los documentos correlativamente (nº 1 poder, nº 2 certificación de matrimonio, y a continuación los demás en el orden en que se citan en los hechos, incluida la propuesta de inventario y sus justificantes). Lugar de firma; fecha del día salvo indicación en contrario.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: separación estricta entre activo y pasivo, cada partida numerada con su valor y su documento, operaciones de liquidación completas y verificables, precisión terminológica entre disolución y liquidación y entre reintegro y compensación por exceso, HECHOS numerados con una idea por apartado, sin narrar el conflicto conyugal, y SUPLICO ajustado a lo estrictamente pedido.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre el Código Civil y la LEC en el BOE antes de redactar (Fase 2). Sin verificación, no proceder. **Los arts. 807, 808 y 810 LEC están en la redacción de la LO 2/2022 (vigencia 23/03/2022) y su verificación en cada lanzamiento es obligatoria.**
2. Si se detecta una versión posterior a la registrada en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario. No usar una versión desactualizada.
3. **Separación de bienes → DETENER.** En el régimen de separación de bienes no hay masa común y no hay sociedad que liquidar (Arts. 1435 CC y 806 LEC). Explicarlo, informar de que el reparto de bienes en proindiviso es una división de cosa común (Arts. 400 y ss. CC) y no crear documento de liquidación.
4. **Régimen de participación → DETENER.** Se liquida por el Art. 811 LEC, con propuesta de estimación de patrimonio inicial y final de cada cónyuge. Los assets de esta skill no sirven. Advertir y escalar.
5. **Derecho civil propio o foral → DETENER.** Cataluña, Aragon, Navarra, Baleares, País Vasco y Galicia tienen regímenes económicos matrimoniales propios con reglas de composición y liquidación distintas. Verificar la norma autonómica y escalar. Nunca aplicar los Arts. 1344 a 1410 CC a un matrimonio sujeto a derecho civil propio.
6. **La separación de hecho no disuelve la sociedad de gananciales** (Art. 1392 CC). Si no hay demanda matrimonial presentada ni capitulaciones, no hay cauce: informar, derivar a `divorcio` o a capitulaciones y no crear el documento. **En cambio, la disolución ya en curso no es obstáculo:** el Art. 808.1 LEC permite pedir la formación de inventario con la demanda matrimonial ya admitida, antes de que la disolución se produzca, y solo la segunda fase, la solicitud de liquidación del Art. 810.1 LEC, exige que sea firme la resolución que declare disuelto el régimen. Nunca escribir que la sociedad "quedó disuelta" cuando aún no lo está, ni decir al cliente que debe esperar a la sentencia para pedir el inventario.
7. **La adjudicación de un bien hipotecado NO libera al otro cónyuge frente a la entidad acreedora** (Arts. 1367 y 1401 CC). Explicarlo siempre antes de redactar la cláusula y confirmar que el cliente lo ha entendido. **PROHIBIDO redactar una cláusula que afirme esa liberación.** Solo cabe la asunción interna del pago, la obligación de mantener indemne al otro y el compromiso de solicitar de la entidad la novación subjetiva, cuya eficacia depende del consentimiento de la entidad.
8. **El remanente se divide por mitad** (Arts. 1344 y 1404 CC). La mitad es el resultado legal de la división, no un punto negociable. Un reparto desigual sin compensación es un negocio distinto (donación) con su propio tratamiento: advertirlo y no redactarlo como si fuera una liquidación ordinaria.
9. **La presunción de ganancialidad del Art. 1361 CC opera siempre.** Nunca calificar un bien de privativo por la sola afirmación del cliente: preguntar por la documentación que lo acredita y, en su defecto, advertir de que la carga de la prueba le corresponde y de que el bien quedará en el activo común.
10. **Los reintegros del Art. 1358 CC se expresan por su importe actualizado al tiempo de la liquidación**, con el criterio de actualización explícito en el documento. Nunca escribir un reintegro por su valor nominal histórico sin advertirlo, ni inventar un criterio de actualización que las partes no hayan pactado.
11. **La preferencia sobre la vivienda habitual del Art. 1406.4.º CC opera solo en caso de fallecimiento del otro cónyuge**, no en el divorcio. Nunca decirle a un cliente divorciado que la ley le da preferencia sobre la vivienda familiar. La atribución del **uso** de la vivienda es una medida del divorcio (Art. 96 CC), distinta de la adjudicación de la **propiedad**.
12. **Fiscalidad: advertir sin cuantificar.** El exceso de adjudicación puede tener coste fiscal y su tratamiento depende de la normativa estatal y autonómica y de si el exceso es inevitable por la indivisibilidad del bien. **PROHIBIDO citar tipos, exenciones o artículos tributarios, cuantificar el impuesto o afirmar que la operación está exenta.** Remitir siempre a asesor fiscal antes de la firma.
13. **La competencia del Art. 807 LEC no es elegible.** Nunca preguntar en que juzgado desea presentarlo ni admitir sumisión a otro fuero.
14. **Cada partida de la propuesta necesita su documento justificativo** (Art. 808.2 LEC). Advertir expresamente de las partidas sin justificación y no presentarlas como acreditadas.
15. **La fecha de disolución es la fecha de corte del inventario** (Art. 1397.1.º CC). No inventariar bienes adquiridos ni deudas contraídas después de esa fecha.
16. **No estimar valores.** El avalúo lo aportan los cónyuges o un peritaje. La skill calcula la aritmética, pero nunca estima ni inventa el valor de un inmueble, de una empresa, de un vehículo ni el saldo de una deuda: esas partidas conservan su placeholder.
17. Nunca inventar datos, cuantías, fechas, números de protocolo, datos registrales ni jurisprudencia. Los campos no proporcionados quedan como `{{DATO}}` con el nombre propio del placeholder del asset.
18. **Indicios de violencia de género o doméstica → DETENER SIEMPRE y escalar**, conforme al guardrail del plugin. Si el proceso matrimonial se siguió ante un Juzgado de Violencia sobre la Mujer (Art. 807 LEC), concurren por definición esos presupuestos.
19. El documento escrito en disco no contiene ningún comentario HTML. Los bloques condicionales se insertan sin su envoltorio de comentario, y los ordinales y números de documento de los bloques condicionales se resuelven en el momento de insertarlos, sin dejar saltos en la numeración.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar en régimen de separación de bienes: no hay masa común que liquidar (Guardrail 3). Si lo que se quiere es repartir un bien adquirido por ambos en proindiviso, eso es una división de cosa común de los Arts. 400 y siguientes del Código Civil, que esta skill no cubre.
- No usar en régimen de participación: cauce distinto del Art. 811 LEC (Guardrail 4).
- No usar en matrimonios sujetos a derecho civil propio o foral (Guardrail 5).
- No usar para tramitar el divorcio o la separación en sí, ni para las medidas personales (custodia, visitas, alimentos, uso de la vivienda, pensión compensatoria): derivar a `divorcio`. Esta skill cubre exclusivamente la parte patrimonial y es la que debe usarse cuando la liquidación del régimen tiene contenido real; el convenio regulador se limita a incorporarla como uno de sus extremos (Art. 90.1.e) CC).
- No usar para modificar medidas ya acordadas: derivar a `modificacion-medidas` si existe en el marketplace.
- No usar para ejecutar un convenio de liquidación incumplido ni para reclamar una compensación pactada y no pagada: derivar a `ejecucion-titulos`.
- No usar para liquidar la sociedad de gananciales por fallecimiento de un cónyuge dentro de una partición de herencia: derivar a `herencia`, cuyo cuaderno particional incorpora la liquidación previa de gananciales como operación antecedente.
- No usar para valorar una empresa familiar, participaciones sociales o una explotación económica en funcionamiento: escalar.
- No usar cuando haya patrimonio situado en el extranjero: escalar.
- No usar cuando existan deudas con la Agencia Tributaria o con la Tesorería General de la Seguridad Social: escalar.
- No usar cuando haya indicios de que un cónyuge ha ocultado o distraído bienes: escalar.
- No usar para calcular la tributación de la operación ni para planificación fiscal: derivar a asesor fiscal.
- No usar si el usuario pide opinión jurídica sobre la estrategia del reparto o sobre sus posibilidades en el pleito: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
