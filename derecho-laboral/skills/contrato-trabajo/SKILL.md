---
name: contrato-trabajo
description: >
  Genera el contrato de trabajo y sus anexos en las modalidades vigentes tras la reforma del Real
  Decreto-ley 32/2021: indefinido ordinario, fijo-discontinuo, temporal por circunstancias de la
  producción, temporal por sustitución de persona trabajadora, formativo en alternancia y formativo
  para la obtención de práctica profesional, a jornada completa o parcial, con el acuerdo de trabajo a
  distancia de la Ley 10/2021 cuando proceda. Aplica el texto refundido de la Ley del Estatuto de los
  Trabajadores aprobado por Real Decreto Legislativo 2/2015, en su versión consolidada vigente
  verificada en el BOE, y toma del convenio colectivo aplicable la clasificación profesional, las
  tablas salariales, la jornada anual, el periodo de prueba y las duraciones máximas de los contratos
  temporales. Metodología: clasificación de la modalidad y la jornada mediante formulario interactivo,
  plan de acción con la validación de la causa de temporalidad, creación del documento base en el
  workspace y edición incremental cláusula a cláusula. NO usar para relaciones laborales especiales
  (alta dirección, empleados de hogar, artistas, deportistas profesionales, representantes de
  comercio, penados, discapacidad en centros especiales de empleo), ni para contratos mercantiles de
  prestación de servicios o de agencia, ni para el contrato de relevo y jubilación parcial.
when_to_use: |
  - El usuario quiere redactar o formalizar un contrato de trabajo para una nueva incorporación.
  - El usuario pregunta qué modalidad contractual corresponde a una necesidad concreta de la empresa.
  - El usuario quiere formalizar un acuerdo de trabajo a distancia o teletrabajo.
  - El usuario quiere revisar o adaptar un contrato existente a la normativa vigente.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - modalidad_contractual: indefinido / fijo-discontinuo / temporal por circunstancias de la producción / temporal por sustitución / formativo en alternancia / formativo para práctica profesional
  - tipo_jornada: completa o parcial, con el número de horas y su distribución
  - modalidad_presencial: presencial / híbrida / a distancia, con el porcentaje de jornada
  - naturaleza_empleador: persona física o persona jurídica
  - datos_empresa: razón social, CIF, domicilio, código de cuenta de cotización, actividad, representante y cargo
  - datos_trabajador: nombre, DNI o NIE, número de afiliación, domicilio, titulación y fecha de nacimiento
  - convenio_colectivo: denominación, ámbito, código, grupo profesional y nivel retributivo
  - causa_temporalidad: acreditación concreta de la circunstancia de la producción o de la sustitución
  - condiciones_economicas: salario base, complementos, pagas extraordinarias y periodicidad
  - condiciones_temporales: fecha de inicio, duración, periodo de prueba, jornada anual y vacaciones
  - pactos_opcionales: confidencialidad, no concurrencia, permanencia, exclusividad, uso de medios
outputs:
  - contrato_trabajo: contrato completo en markdown, DRAFT, con las cláusulas del régimen legal y convencional aplicable
  - acuerdo_trabajo_distancia: anexo de trabajo a distancia en markdown, DRAFT, cuando proceda
references:
  - references/fuentes-plantillas-validadas.md
  - references/modalidades-contractuales-art15-y-16.md
  - references/contenido-minimo-y-pactos.md
  - references/trabajo-a-distancia-ley10-2021.md
  - references/formalizacion-registro-y-comunicacion.md
assets:
  - assets/template-acuerdo-trabajo-a-distancia.md
  - assets/template-contrato-fijo-discontinuo.md
  - assets/template-contrato-formativo.md
  - assets/template-contrato-indefinido.md
  - assets/template-contrato-temporal-circunstancias-produccion.md
  - assets/template-contrato-temporal-sustitucion.md
---

# Generar el Contrato de Trabajo

> DRAFT — para revisión por un abogado o graduado social colegiado antes de su firma y formalización. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Modalidad contractual):** `indefinido` | `fijo_discontinuo` | `temporal_produccion` | `temporal_sustitucion` | `formativo_alternancia` | `formativo_practica` | `fuera_de_alcance`.
- **V2 (Jornada):** `completa` | `parcial`.
- **V3 (Naturaleza del empleador):** `persona_fisica` | `persona_juridica`.
- **V4 (Modalidad de prestación):** `presencial` | `hibrida` | `a_distancia`. *(Determina si nace el acuerdo de la Ley 10/2021.)*
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

### 1.1 Escucha Activa Previa
Si el usuario ya ha identificado inequívocamente la modalidad, la jornada y el régimen de prestación, registra los vectores en silencio y pasa a la **Fase 2**. La modalidad no se presume: si el usuario describe una necesidad sin nombrar la modalidad, la resuelves tú preguntando por la necesidad, no por el nombre del contrato.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "necesidad_contractual",
      "rationale": "Resolver V1: la modalidad se determina por la necesidad real, no por la preferencia de la empresa. La contratación temporal es excepcional y causal.",
      "question": "¿A qué necesidad responde la contratación?",
      "options": [
        {"id": "indefinido", "label": "Actividad ordinaria y permanente de la empresa, sin término previsto"},
        {"id": "fijo_discontinuo", "label": "Trabajo estacional, de temporada, o de prestación intermitente y previsible"},
        {"id": "temporal_produccion", "label": "Incremento ocasional e imprevisible de la actividad, u oscilación puntual de la demanda"},
        {"id": "temporal_sustitucion", "label": "Sustitución de una persona con derecho a reserva de puesto, o cobertura durante un proceso de selección"},
        {"id": "formativo_alternancia", "label": "Compatibilizar el trabajo con una formación reglada o de certificado de profesionalidad"},
        {"id": "formativo_practica", "label": "Práctica profesional de quien ha terminado sus estudios recientemente"},
        {"id": "fuera_de_alcance", "label": "Alta dirección, empleo del hogar, artistas, deportistas, contrato de relevo u otra relación especial"}
      ]
    },
    {
      "id": "tipo_jornada",
      "rationale": "Resolver V2: el contrato a tiempo parcial exige forma escrita con distribución horaria detallada y régimen propio de horas complementarias.",
      "question": "¿Qué jornada se pacta?",
      "options": [
        {"id": "completa", "label": "Jornada completa según convenio"},
        {"id": "parcial", "label": "Jornada parcial"}
      ]
    },
    {
      "id": "modalidad_prestacion",
      "rationale": "Resolver V4: a partir del 30 por ciento de la jornada a distancia en un periodo de referencia de tres meses nace el acuerdo escrito de la Ley 10/2021.",
      "question": "¿Dónde se prestarán los servicios?",
      "options": [
        {"id": "presencial", "label": "Íntegramente en el centro de trabajo"},
        {"id": "hibrida", "label": "Modalidad mixta, con parte de la jornada a distancia"},
        {"id": "a_distancia", "label": "Íntegramente o mayoritariamente a distancia"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `necesidad_contractual`
- `V2` — `tipo_jornada`
- `V4` — `modalidad_prestacion`
- `V3` — naturaleza del empleador: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo

### 1.3 Enrutamiento de Estado (Routing por Vectores)

* **Si `[V1 = fuera_de_alcance]` → Detener proceso.** Explica que las relaciones laborales especiales del artículo 2 del Estatuto de los Trabajadores y el contrato de relevo tienen regulación propia con contenido contractual distinto. Ofrece la derivación. **No crees documento.**
* **Si `[V1 = indefinido]` → Plantilla: `assets/template-contrato-indefinido.md`.** Es la modalidad por defecto: el contrato de trabajo se presume concertado por tiempo indefinido (artículo 15.1).
* **Si `[V1 = fijo_discontinuo]` → Plantilla: `assets/template-contrato-fijo-discontinuo.md`.** Verifica que la actividad sea de naturaleza estacional o de temporada, o de prestación intermitente con periodos de ejecución ciertos, determinados o indeterminados. El contrato debe reflejar la duración estimada de la actividad, la forma y el orden de llamamiento, y la jornada estimada y su distribución horaria.
* **Si `[V1 = temporal_produccion]` → Plantilla: `assets/template-contrato-temporal-circunstancias-produccion.md`.** Exige y valida la **causa concreta**: incremento ocasional e imprevisible de la actividad, u oscilación que, aun tratándose de la actividad normal, genera un desajuste temporal entre el empleo disponible y el existente. Duración máxima de seis meses, ampliable hasta un año por convenio colectivo sectorial. Comprueba el encadenamiento del artículo 15.5.
* **Si `[V1 = temporal_sustitucion]` → Plantilla: `assets/template-contrato-temporal-sustitucion.md`.** Debe identificarse a la **persona sustituida** y la causa de la sustitución. En la cobertura temporal de un puesto durante un proceso de selección o promoción, la duración máxima es de tres meses.
* **Si `[V1 = formativo_alternancia]` o `[V1 = formativo_practica]` → Plantilla: `assets/template-contrato-formativo.md`.** Verifica los requisitos propios de cada submodalidad: la existencia de acuerdo con el centro formativo y de plan formativo individual en la alternancia, y en la práctica profesional que no hayan transcurrido más de tres años (cinco en caso de discapacidad) desde la terminación de los estudios.
* **Si `[V4 = hibrida]` o `[V4 = a_distancia]` → Documento adicional obligatorio:** además del contrato, genera el `assets/template-acuerdo-trabajo-a-distancia.md`. Explica en el chat que el acuerdo debe formalizarse **por escrito**, que el trabajo a distancia es **voluntario y reversible**, y que no puede imponerse por la vía del artículo 41. Advierte de que el porcentaje del 30 por ciento de la jornada en un periodo de referencia de tres meses es el que determina la aplicación de la Ley 10/2021, y verifícalo en el texto vigente.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión consolidada vigente del Estatuto de los Trabajadores en el BOE.
3. **Localiza el convenio colectivo aplicable** y extrae de él: clasificación profesional y grupos, tablas salariales vigentes del año en curso, jornada anual, distribución irregular, periodo de prueba, duración máxima ampliada del contrato por circunstancias de la producción, y complementos obligatorios.
4. Verifica el **salario mínimo interprofesional vigente** con `web_search` antes de fijar cualquier retribución, y comprueba que el salario pactado no queda por debajo ni del salario mínimo ni de la tabla del convenio para ese grupo y nivel.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Modalidad procedente y su fundamento legal**, explicando por qué la necesidad descrita encaja en ella y, si el usuario pretendía otra, por qué no procede.
2. **Marco convencional:** convenio identificado, grupo profesional y salario de tabla aplicable.
3. **Duración, periodo de prueba y límites** aplicables a la modalidad.
4. **Obligaciones de formalización:** comunicación del contenido del contrato al servicio público de empleo y entrega de copia básica a la representación legal de los trabajadores, con sus plazos.
5. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
6. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación del origen de la plantilla
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:** accede al adjunto y aplica el **guardrail de cláusulas nulas**: renuncia anticipada de derechos, salario inferior al convenio o al salario mínimo, periodo de prueba superior al máximo, cláusula de temporalidad sin causa, pacto de no concurrencia sin compensación económica, cláusula de disponibilidad horaria absoluta, o renuncia al registro de jornada. Advierte expresamente de la nulidad de cada una y propón la redacción válida antes de adoptar la minuta.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura (`create_file`):** vuelca íntegramente la plantilla acordada en el workspace con nombre en `snake_case.md`, aplicando **Zero-Omission** y dejando los datos pendientes como marcador con su nombre propio de plantilla. Si V4 exige el acuerdo de trabajo a distancia, crea también ese segundo archivo e infórmalo.
2. **Validación (`read_file`):** comprueba el volcado íntegro de cada archivo creado.
3. **Confirmación y encadenamiento:** informa de la ruta absoluta y, en la misma respuesta, abre la primera sección de la Fase 4 con su anuncio y su primera solicitud de datos.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA

### Protocolo Obligatorio de Edición
```
[slot_filling_request (grupos) / Chat (negociación)] --> [Vista previa en texto plano]
      --> [«¿Confirmamos esta cláusula?»] --> [edit_file + read_file]
```

- **Datos estructurados agrupados (`slot_filling_request`, MANDATORIO):** empresa, trabajador, condiciones económicas y jornada se solicitan en bloque, nunca dato a dato.
- **Anuncio de sección visible** al pasar de una cláusula a la siguiente, en el mismo mensaje que la primera solicitud.
- **Diálogo en las cláusulas de negociación:** no te limites a registrar el dato. En jornada, salario, periodo de prueba, duración y pactos opcionales, explica antes el mínimo legal o convencional aplicable y la consecuencia de apartarse de él, y confirma que el cliente lo entiende.

### Hoja de Ruta de Cláusulas

Anuncios fijos:
- Cláusula 1: "Procedemos a identificar a las partes contratantes y el convenio colectivo de aplicación."
- Cláusula 2: "Identificadas las partes, corresponde determinar el objeto del contrato y el puesto de trabajo."
- Cláusula 3: "Determinado el objeto, procede fijar la modalidad, la duración y, en su caso, la causa de temporalidad."
- Cláusula 4: "Fijada la duración, corresponde establecer la jornada y su distribución."
- Cláusula 5: "Establecida la jornada, procede determinar la retribución."
- Cláusula 6: "Determinada la retribución, corresponde fijar el periodo de prueba y las vacaciones."
- Cláusula 7: "Por último, procede recoger los pactos adicionales que las partes deseen incorporar."

1. **Partes y convenio [dato objetivo].** Solicita en bloque mediante `slot_filling_request`: de la empresa, razón social o nombre, CIF o NIF, domicilio, código de cuenta de cotización, actividad y centro de trabajo, y firmante con su NIF y cargo si V3 es persona jurídica; del trabajador, nombre, DNI o NIE, número de afiliación a la Seguridad Social, domicilio, fecha de nacimiento y titulación. Verifica que el trabajador tenga la edad legal para contratar (artículo 6) y, si es menor de dieciocho años, advierte de las prohibiciones de trabajo nocturno, horas extraordinarias y actividades insalubres o peligrosas. Localiza el convenio con `web_search` si el usuario no lo conoce.
2. **Objeto y puesto [dato objetivo].** Grupo profesional del convenio, nivel retributivo, denominación del puesto y descripción de funciones. Explica que el **grupo profesional**, y no la categoría, es la unidad de clasificación y la que delimita la movilidad funcional ordinaria: una descripción de funciones excesivamente estrecha limita a la empresa, y una excesivamente amplia puede resultar inaplicable.
3. **Modalidad, duración y causa [negociación — el apartado decisivo en los temporales].**
   - *Indefinido:* fecha de inicio, sin término.
   - *Fijo-discontinuo:* duración estimada de la actividad, **forma y orden de llamamiento** conforme al convenio, y jornada estimada con su distribución horaria orientativa. Explica que el llamamiento debe realizarse por escrito y que su incumplimiento habilita al trabajador para reclamar por despido.
   - *Temporal por circunstancias de la producción:* exige y transcribe la **causa concreta** con los datos que la sustenten. Fija la duración dentro del máximo de seis meses, o del ampliado por convenio sectorial hasta un año. Advierte de que solo cabe una prórroga, hasta el máximo, si se concertó por duración inferior. Comprueba el **encadenamiento del artículo 15.5** preguntando por contratos anteriores del mismo trabajador o en el mismo puesto en los últimos veinticuatro meses, y advierte si la contratación determinaría la adquisición de la condición de fijo.
   - *Temporal por sustitución:* identifica a la persona sustituida, la causa de la reserva de puesto y la duración prevista, que se extiende mientras subsista el derecho a la reserva.
   - *Formativo:* duración dentro de los límites de la submodalidad y referencia al plan formativo o al acuerdo con el centro de formación.
4. **Jornada y distribución [negociación].** Jornada anual y semanal según convenio, horario, distribución y descansos. Si V2 es parcial, es **obligatorio** consignar el número de horas ordinarias al día, a la semana, al mes o al año y su distribución; sin esa consignación el contrato se presume a jornada completa. Explica el régimen de **horas complementarias**: solo caben si se pactan expresamente, con preaviso, y dentro del porcentaje legal o convencional, y no caben horas extraordinarias en el contrato a tiempo parcial salvo fuerza mayor. Informa siempre de la obligación empresarial de **registro diario de jornada** del artículo 34.9.
5. **Retribución [negociación].** Salario base, complementos, número de pagas extraordinarias y si van prorrateadas, periodicidad y medio de pago. **Verifica que el importe no sea inferior al salario de tabla del convenio para ese grupo y nivel, ni al salario mínimo interprofesional vigente**, que debes comprobar con `web_search`. Muestra el cálculo del salario bruto anual resultante. Advierte de que un salario inferior al convenio es nulo en la diferencia y genera reclamación de cantidad con recargo por mora.
6. **Periodo de prueba y vacaciones [negociación].** Periodo de prueba dentro del máximo del convenio o, en su defecto, del artículo 14.1. Advierte de que **es nulo el pacto cuando el trabajador ya haya desempeñado las mismas funciones con anterioridad en la empresa**, bajo cualquier modalidad de contratación. En contratos temporales de duración no superior a seis meses, el periodo de prueba no puede exceder de un mes salvo lo dispuesto en convenio. Vacaciones: mínimo de treinta días naturales anuales, o la mejora del convenio.
7. **Pactos adicionales [negociación].** Ofrece y explica, sin imponer: confidencialidad, propiedad intelectual e industrial de los desarrollos, uso de medios y equipos de la empresa, política de protección de datos e información al trabajador, y los pactos con requisitos propios que exigen advertencia expresa:
   - **Pacto de no concurrencia postcontractual (artículo 21.2):** duración máxima de dos años para técnicos y de seis meses para los demás trabajadores; exige que el empresario tenga un efectivo interés industrial o comercial y que se satisfaga al trabajador una **compensación económica adecuada**. Sin compensación, el pacto es nulo.
   - **Pacto de permanencia (artículo 21.4):** solo cuando el trabajador haya recibido una especialización profesional con cargo al empresario para poner en marcha proyectos determinados o realizar un trabajo específico; duración máxima de dos años, por escrito, con derecho del empresario a indemnización de daños en caso de abandono.
   - **Pacto de plena dedicación (artículo 21.1 y 21.3):** exige compensación económica expresa y es renunciable por el trabajador con preaviso de treinta días, perdiendo la compensación.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar una cláusula existente.
2. Añadir un pacto adicional a medida.
3. Revisar la modalidad, la duración o la causa de temporalidad.
4. Corregir datos identificativos, jornada o importes.
5. Dar el contrato por finalizado y cerrar la sesión.
```

### Advertencias Legales Preceptivas de Cierre
- **Carácter DRAFT:** revisión por abogado o graduado social colegiado antes de la firma.
- **Alta previa en la Seguridad Social:** el alta debe solicitarse **con anterioridad al inicio de la prestación de servicios**. Recuérdalo siempre.
- **Comunicación al servicio público de empleo:** el contenido del contrato debe comunicarse en el plazo de los diez días hábiles siguientes a su concertación.
- **Copia básica a la representación legal de los trabajadores** en el plazo de diez días, cuando exista representación.
- **Entrega de copia al trabajador** e información sobre los elementos esenciales del contrato.
- **Registro de jornada:** obligación diaria desde el primer día, conservando los registros durante cuatro años.
- **Prevención de riesgos laborales:** evaluación del puesto, formación e información al trabajador y, en su caso, reconocimiento médico previo, antes del inicio efectivo.
- **Protección de datos:** información al trabajador sobre el tratamiento de sus datos personales.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre en el BOE la versión consolidada vigente del Estatuto de los Trabajadores, el convenio colectivo aplicable y el salario mínimo interprofesional vigente antes de fijar condiciones. Aplicar la redacción vigente al documento del workspace.
2. **Presunción de indefinido (artículo 15.1):** el contrato de trabajo se presume concertado por tiempo indefinido. La temporalidad es excepcional y causal. **PROHIBIDO** redactar un contrato temporal sin causa concreta expresada, o con una causa genérica que se limite a reproducir el texto legal.
3. **Duraciones máximas:** seis meses en el contrato por circunstancias de la producción, ampliables hasta un año por convenio sectorial; tres meses en la cobertura temporal durante un proceso de selección. No redactar duraciones superiores.
4. **Encadenamiento (artículo 15.5):** comprobar siempre los contratos previos del trabajador y del puesto en los últimos veinticuatro meses, y advertir de la adquisición de la condición de fijo cuando concurran los presupuestos legales.
5. **Salario:** nunca inferior al convenio ni al salario mínimo interprofesional. Rechazar la redacción si el usuario lo solicita, citando el precepto y proponiendo el importe válido.
6. **Contrato a tiempo parcial:** consignación obligatoria del número de horas ordinarias y su distribución; sin ella el contrato se presume a jornada completa. Prohibidas las horas extraordinarias salvo fuerza mayor.
7. **Periodo de prueba:** dentro del máximo convencional o legal; nulo si el trabajador ya desempeñó las mismas funciones en la empresa.
8. **Pactos con requisitos propios:** no concurrencia postcontractual sin compensación económica adecuada, permanencia sin especialización a cargo del empresario, o plena dedicación sin compensación expresa, son **nulos**. Advertirlo y no redactarlos sin sus requisitos.
9. **Trabajo a distancia:** voluntario y reversible, con acuerdo escrito. No puede imponerse unilateralmente ni por la vía del artículo 41, y su negativa no es causa de despido ni de modificación de condiciones.
10. **Cero invención:** no inventar convenios, artículos, tablas salariales, importes de salario mínimo ni datos de las partes. Los datos no aportados permanecen como marcador con su nombre propio de plantilla.
11. **Sintaxis de los marcadores (`{{CLAVE: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real: nunca debe quedar rastro de la anotación en el documento escrito. Los marcadores cuyo dato aún no exista se conservan **íntegros, con su clave y su tipo**, para que el cliente y el profesional que revise vean qué falta y de qué naturaleza es. Está PROHIBIDO sustituir la clave propia del marcador por un literal genérico.
