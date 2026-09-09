---
name: conciliacion-previa
description: >
  Genera los documentos de la vía previa al proceso social: burofax de reclamación extrajudicial de
  cantidades, papeleta de conciliación por despido, por reclamación de cantidad y por impugnación de
  sanción ante el servicio administrativo de mediación, arbitraje y conciliación competente, y acuerdo
  conciliatorio para su elevación al acta. Aplica los artículos 63 a 68 de la **Ley 36/2011 reguladora
  de la Jurisdicción Social**, que exige el intento de conciliación como requisito previo a la demanda en el orden social, y el **texto refundido de la Ley del Estatuto de los Trabajadores aprobado
  por Real Decreto Legislativo 2/2015**, en sus versiones consolidadas vigentes verificadas en el BOE.
  Su primera función es de control: comprueba si el asunto está o no exceptuado del intento de
  conciliación, calcula el plazo de caducidad restante y su suspensión, e identifica el organismo
  territorialmente competente. Metodología: clasificación del objeto y la posición mediante formulario
  interactivo, plan de acción con el cómputo del plazo, creación del documento base en el workspace y
  edición incremental apartado a apartado. NO usar para reclamaciones en materia de Seguridad Social,
  que corresponden a la skill `reclamacion-seguridad-social`, ni para redactar la demanda, que
  corresponde a la skill `demanda-social`.
when_to_use: |
  - El usuario quiere presentar papeleta de conciliación por despido, por cantidades o contra una sanción.
  - El usuario quiere reclamar extrajudicialmente salarios impagados antes de acudir a la vía judicial.
  - El usuario pregunta qué plazo tiene para reclamar y ante qué organismo debe presentar la papeleta.
  - Las partes han alcanzado un acuerdo y quieren documentarlo para el acto de conciliación.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - tipo_documento: burofax de reclamación / papeleta de conciliación / acuerdo conciliatorio
  - objeto_reclamacion: despido / cantidad / sanción / otro
  - posicion_usuario: trabajador o empresa
  - comunidad_autonoma: comunidad autónoma del centro de trabajo, para identificar el organismo competente
  - datos_solicitante: nombre, DNI o NIE, domicilio, teléfono y correo a efectos de notificaciones
  - datos_demandado: razón social, CIF, domicilio y centro de trabajo
  - datos_relacion_laboral: antigüedad, categoría, salario bruto anual con prorrateos, tipo de contrato
  - hechos: relato de los hechos que fundan la reclamación, con fechas
  - fecha_hecho_impugnado: fecha de efectos del despido, de notificación de la sanción o de devengo de la deuda
  - cantidades_reclamadas: desglose por conceptos y periodos, con su total
outputs:
  - papeleta_conciliacion: papeleta completa en markdown, DRAFT, lista para su presentación
  - burofax_reclamacion: carta de reclamación extrajudicial en markdown, DRAFT, para envío por burofax
  - acuerdo_conciliatorio: propuesta de acuerdo en markdown, DRAFT, para su elevación al acta
references:
  - references/fuentes-plantillas-validadas.md
  - references/conciliacion-previa-y-excepciones.md
  - references/plazos-suspension-y-caducidad.md
  - references/contenido-de-la-papeleta.md
  - references/organismos-de-conciliacion.md
assets:
  - assets/template-acuerdo-conciliatorio.md
  - assets/template-burofax-reclamacion-cantidades.md
  - assets/template-papeleta-conciliacion-cantidad.md
  - assets/template-papeleta-conciliacion-despido.md
  - assets/template-papeleta-conciliacion-sancion.md
---

# Generar los Documentos de la Conciliación Previa

> DRAFT — para revisión por un abogado o graduado social colegiado antes de su firma y presentación. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de documento):** `burofax_reclamacion` | `papeleta_despido` | `papeleta_cantidad` | `papeleta_sancion` | `acuerdo_conciliatorio` | `exceptuado_conciliacion`.
- **V2 (Objeto de la reclamación):** `despido` | `cantidad` | `sancion` | `otro`.
- **V3 (Posición del usuario):** `trabajador` | `empresa`.
- **V4 (Ámbito territorial):** comunidad autónoma del centro de trabajo, que determina el organismo competente.
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

### 1.1 Escucha Activa Previa
Si el usuario ya ha identificado inequívocamente el objeto de la reclamación, su posición y el ámbito territorial, registra los vectores en silencio y pasa a la **Fase 2**. En todo caso, **antes de cualquier otra cosa, resuelve el control de procedibilidad del punto 1.3**: es la razón de ser de esta skill.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "objeto_reclamacion",
      "rationale": "Resolver V2: determina si el asunto exige conciliación previa o está exceptuado, y cuál es el plazo aplicable.",
      "question": "¿Sobre qué versa la reclamación?",
      "options": [
        {"id": "despido", "label": "Despido o extinción del contrato por decisión de la empresa"},
        {"id": "cantidad", "label": "Cantidades adeudadas: salarios, pagas, horas extraordinarias, finiquito"},
        {"id": "sancion", "label": "Sanción disciplinaria distinta del despido"},
        {"id": "exceptuado", "label": "Modificación sustancial, movilidad geográfica, vacaciones, conciliación de la vida familiar, o prestaciones de Seguridad Social"},
        {"id": "otro", "label": "Otra materia"}
      ]
    },
    {
      "id": "posicion_usuario",
      "rationale": "Resolver V3: la papeleta la promueve normalmente la persona trabajadora; la empresa puede promoverla en reclamaciones frente a ella.",
      "question": "¿Desde qué posición actúa usted?",
      "options": [
        {"id": "trabajador", "label": "En representación de la persona trabajadora"},
        {"id": "empresa", "label": "En representación de la empresa"}
      ]
    },
    {
      "id": "fase_del_asunto",
      "rationale": "Resolver V1: determina si procede la reclamación extrajudicial previa, la papeleta o la documentación de un acuerdo ya alcanzado.",
      "question": "¿En qué momento se encuentra el asunto?",
      "options": [
        {"id": "reclamacion_extrajudicial", "label": "Aún no se ha reclamado formalmente y se quiere requerir de pago antes de acudir a la vía judicial"},
        {"id": "papeleta", "label": "Procede presentar la papeleta de conciliación"},
        {"id": "acuerdo", "label": "Las partes han alcanzado un acuerdo y quieren documentarlo"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `fase_del_asunto`
- `V2` — `objeto_reclamacion`
- `V3` — `posicion_usuario`
- `V4` — ámbito territorial: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo

### 1.3 Control de Procedibilidad y Enrutamiento (PRIMERA ACCIÓN OBLIGATORIA)

**Comprobación 1 — ¿Está el asunto exceptuado del intento de conciliación?** El artículo 64 de la Ley 36/2011 exceptúa, entre otros, los procesos sobre **Seguridad Social**, **vacaciones**, **movilidad geográfica**, **modificación sustancial de condiciones de trabajo**, **suspensión del contrato y reducción de jornada por causas empresariales**, **derechos de conciliación de la vida personal, familiar y laboral**, materia electoral, impugnación de convenios y **tutela de derechos fundamentales**.

* **Si `[V2 = exceptuado]`, o si de lo relatado resulta que el objeto está exceptuado → Detén la redacción de la papeleta.** Explica en el chat que presentar papeleta en un asunto exceptuado no suspende el plazo de caducidad y puede consumirlo inútilmente, y deriva: a la skill `demanda-social` si procede demanda directa, o a `reclamacion-seguridad-social` si la materia es prestacional. **Verifica siempre la lista vigente del artículo 64 con `web_search` antes de afirmar que un asunto está o no exceptuado.**

**Comprobación 2 — Cómputo del plazo.** Antes de redactar nada, pide la fecha del hecho —efectos del despido, notificación de la sanción, o devengo de la cantidad— y calcula:
- Despido y sanción: **20 días hábiles** de caducidad (artículos 59.3 del Estatuto de los Trabajadores y 103 y 114 de la Ley 36/2011), excluyendo sábados, domingos y festivos.
- Cantidad: **1 año** de prescripción desde que la acción pudo ejercitarse (artículo 59.2 del Estatuto de los Trabajadores).
Comunica en el chat los días consumidos, los restantes y la **fecha límite**. Si el plazo ha vencido, adviértelo con claridad antes de continuar y no lo ocultes en el documento.

**Comprobación 3 — Enrutamiento:**
* **Si `[V1 = reclamacion_extrajudicial]` → Plantilla: `assets/template-burofax-reclamacion-cantidades.md`.** Útil para interrumpir la prescripción y para acreditar la reclamación previa a efectos del requisito de procedibilidad.
* **Si `[V1 = papeleta]` y `[V2 = despido]` → Plantilla: `assets/template-papeleta-conciliacion-despido.md`.**
* **Si `[V1 = papeleta]` y `[V2 = cantidad]` → Plantilla: `assets/template-papeleta-conciliacion-cantidad.md`.**
* **Si `[V1 = papeleta]` y `[V2 = sancion]` → Plantilla: `assets/template-papeleta-conciliacion-sancion.md`.**
* **Si `[V1 = acuerdo]` → Plantilla: `assets/template-acuerdo-conciliatorio.md`.**
* **Si `[V2 = otro]` → DETENER**: identifica la materia y deriva sin crear documento; esta skill cubre despido, cantidad y sanción.
* `V3` no elige plantilla: determina quién figura como solicitante y quién como parte frente a la que se dirige la reclamación, y con ello el sentido de la pretensión.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión consolidada vigente de la Ley 36/2011 en el BOE. **La lista de excepciones del artículo 64 ya se verificó en el control de procedibilidad de la Fase 1.3: no la vuelvas a consultar**, reutiliza el resultado.
3. **Identifica el organismo de conciliación competente** con `web_search` a partir de la comunidad autónoma del centro de trabajo: cada comunidad tiene su propio servicio, con denominación, sede electrónica y modelo propio. Informa del nombre exacto, de la sede electrónica y de si admite presentación telemática.
4. Comprueba si el convenio colectivo o un acuerdo interprofesional del ámbito atribuye la función conciliadora a un **órgano de solución autónoma de conflictos**, en cuyo caso el trámite se cumple ante ese órgano.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Procedencia del trámite:** si el asunto exige conciliación o está exceptuado, con cita del precepto.
2. **Cómputo del plazo:** días consumidos, días restantes y fecha límite, con la advertencia de que la presentación de la papeleta suspende la caducidad y de cómo se reanuda el cómputo.
3. **Organismo competente**, con su denominación exacta y su sede.
4. **Cuantía y conceptos** que se reclamarán, si el objeto es económico.
5. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
6. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:** accede al adjunto y verifica que contenga la identificación completa de ambas partes con domicilios válidos a efectos de citación, la enunciación de los hechos, la pretensión concreta y la fecha. Advierte de las omisiones y propón la redacción válida.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura (`create_file`):** vuelca íntegramente la plantilla acordada en el workspace con nombre en `snake_case.md`, aplicando **Zero-Omission** y dejando los datos pendientes como marcador con su nombre propio de plantilla.
2. **Validación (`read_file`):** comprueba el volcado íntegro.
3. **Confirmación y encadenamiento:** informa de la ruta absoluta y, en la misma respuesta, abre la primera sección de la Fase 4 con su anuncio y su primera solicitud de datos.

---

## FASE 4 — EDICIÓN INCREMENTAL APARTADO A APARTADO

### Protocolo Obligatorio de Edición
```
[slot_filling_request (grupos) / Chat (relato de hechos)] --> [Vista previa en texto plano]
      --> [«¿Confirmamos esta sección?»] --> [edit_file + read_file]
```

- **Datos estructurados agrupados (`slot_filling_request`, MANDATORIO):** solicitante, demandado, relación laboral y desglose de cantidades se piden en bloque.
- **Anuncio de sección visible** al pasar de una sección a la siguiente.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a identificar al solicitante y a la parte frente a la que se dirige la reclamación."
- Sección 2: "Identificadas las partes, corresponde precisar los datos de la relación laboral."
- Sección 3: "Precisada la relación laboral, procede exponer los hechos que fundan la reclamación."
- Sección 4: "Expuestos los hechos, corresponde concretar la pretensión y, en su caso, las cantidades reclamadas."
- Sección 5: "Por último, procede fijar el organismo de presentación y las indicaciones de tramitación."

1. **Partes [dato objetivo, con validación crítica del domicilio].** Solicita en bloque mediante `slot_filling_request`: del solicitante, nombre, DNI o NIE, domicilio, teléfono y correo electrónico a efectos de notificaciones; del demandado, razón social o nombre, CIF o NIF, **domicilio social y domicilio del centro de trabajo**. Advierte de que un domicilio incorrecto impide la citación y frustra el acto: si la empresa tiene varios centros, consígnalos todos. Si el demandado es un grupo de empresas, una contrata o una empresa de trabajo temporal, pregunta expresamente por la **posible responsabilidad solidaria** y dirige la papeleta contra todas las posibles responsables: quien no sea citado en conciliación no podrá ser demandado después sin subsanar el trámite.
2. **Relación laboral [dato objetivo].** Antigüedad, categoría o grupo profesional, tipo de contrato, jornada y salario bruto anual con prorrateo de pagas. Calcula y muestra el salario diario regulador cuando el objeto sea el despido.
3. **Hechos [negociación — el apartado que define el pleito].** Solicita el relato en el chat, ordenado cronológicamente y con fechas. Explica que la papeleta acota el objeto del proceso: la demanda posterior debe ser **sustancialmente coincidente** con ella, y una papeleta escueta o imprecisa limita después la demanda o genera una excepción de variación sustancial. En despido, consigna la fecha de efectos, la modalidad y si hubo carta y su contenido. En sanción, la fecha de notificación, la falta imputada y la sanción impuesta. En cantidad, el periodo, los conceptos y por qué se devengaron.
4. **Pretensión y cantidades [negociación].** Formula la pretensión con precisión: declaración de improcedencia o nulidad del despido con los efectos legales; revocación de la sanción; o condena al abono de la cantidad. Si hay cantidades, presenta el **desglose por conceptos y periodos** en tabla, con el total y con el interés por mora del artículo 29.3 del Estatuto de los Trabajadores cuando proceda. Muestra el cálculo antes de escribirlo.
5. **Presentación y tramitación [dato objetivo].** Consigna el organismo competente identificado, la fecha de presentación prevista y la advertencia sobre la **asistencia obligatoria al acto**: la incomparecencia del solicitante, sin justa causa, determina que se tenga por no presentada la papeleta; la incomparecencia del demandado debidamente citado determina que la conciliación se tenga por intentada sin efecto, con posible imposición de costas si la sentencia posterior coincide esencialmente con la pretensión y se aprecia temeridad. Recuerda llevar al acto la documentación acreditativa y, si se acude con representación, el poder o la designación.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar un apartado existente.
2. Ampliar el relato de hechos o el desglose de cantidades.
3. Añadir codemandados por posible responsabilidad solidaria.
4. Corregir datos identificativos, domicilios o fechas.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Legales Preceptivas de Cierre
- **Carácter DRAFT:** revisión por abogado o graduado social colegiado antes de su presentación.
- **Efecto sobre los plazos:** la presentación de la solicitud **suspende** los plazos de caducidad e **interrumpe** los de prescripción. El cómputo de la caducidad se reanuda al día siguiente de intentada la conciliación o transcurridos quince días hábiles desde su presentación sin que se haya celebrado; y en todo caso, transcurridos treinta días, se tiene por terminado el procedimiento y cumplido el trámite.
- **Cálculo del plazo restante:** recuerda al usuario cuántos días hábiles quedarán tras la conciliación para presentar la demanda, y adviértele de que presentar la papeleta el último día deja un margen mínimo.
- **Asistencia obligatoria:** consecuencias de la incomparecencia de cada parte.
- **Conservar copia sellada** de la papeleta con su fecha de presentación y la certificación del acto de conciliación: son documentos que deben acompañarse a la demanda.
- **Eficacia del acuerdo:** lo acordado en conciliación tiene fuerza ejecutiva entre las partes sin necesidad de ratificación judicial, y se lleva a efecto por el trámite de ejecución de sentencias.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre en el BOE la versión consolidada vigente de la Ley 36/2011 y del Estatuto de los Trabajadores antes de redactar. La **lista de excepciones del artículo 64** se verifica una sola vez, en el control de procedibilidad de la Fase 1.3, y su resultado se reutiliza en el resto de la ejecución.
2. **Control de procedibilidad como primera acción:** si el asunto está exceptuado, no redactar la papeleta. Presentarla en esos casos no suspende el plazo y puede consumirlo.
3. **Cómputo y comunicación del plazo:** calcular y comunicar siempre los días hábiles restantes y la fecha límite antes de redactar. Si el plazo ha vencido, advertirlo con claridad y no ocultarlo.
4. **Días hábiles:** excluir sábados, domingos y festivos nacionales, autonómicos y locales, verificando el calendario laboral de la localidad con `web_search`. El mes de agosto es hábil en el orden social a estos efectos.
5. **Congruencia con la demanda posterior:** la papeleta acota el objeto del proceso. Redactarla con hechos suficientes y pretensión precisa; una papeleta genérica compromete la demanda.
6. **Codemandados:** preguntar siempre por grupos de empresas, contratas, subcontratas, empresas de trabajo temporal y sucesión de empresa, y dirigir la papeleta contra todas las posibles responsables solidarias.
7. **Domicilios de citación:** consignar domicilio social y de centro de trabajo. Un domicilio erróneo frustra el acto y consume el plazo.
8. **Cero invención:** no inventar hechos, fechas, importes ni organismos. Los datos no aportados permanecen como marcador con su nombre propio de plantilla. El nombre exacto del organismo competente se verifica con `web_search`, nunca se escribe de memoria.
9. **Sintaxis de los marcadores (`{{CLAVE: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real: nunca debe quedar rastro de la anotación en el documento escrito. Los marcadores cuyo dato aún no exista se conservan **íntegros, con su clave y su tipo**, para que el cliente y el profesional que revise vean qué falta y de qué naturaleza es. Está PROHIBIDO sustituir la clave propia del marcador por un literal genérico.
