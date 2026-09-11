---
name: modificacion-condiciones
description: >
  Genera los documentos de alteración unilateral de las condiciones de trabajo por decisión
  empresarial y las respuestas del trabajador a esa alteración: comunicación de modificación
  sustancial de condiciones de trabajo (artículo 41 del texto refundido de la Ley del Estatuto de los
  Trabajadores), comunicación de traslado o desplazamiento con cambio de residencia (artículo 40),
  comunicación de movilidad funcional (artículo 39) y escrito del trabajador optando por la extinción
  indemnizada o anunciando la impugnación. Aplica el **Estatuto de los Trabajadores aprobado por Real
  Decreto Legislativo 2/2015**, norma básica que regula la movilidad funcional y geográfica y la modificación sustancial de condiciones, y los artículos 138 y siguientes de la **Ley 36/2011 reguladora de la
  Jurisdicción Social**, que regula la impugnación judicial de esas medidas, en sus versiones consolidadas vigentes verificadas en el BOE, y contrasta el
  convenio colectivo aplicable, que puede mejorar los preavisos y las compensaciones. Metodología:
  clasificación de la medida y de su alcance individual o colectivo mediante formulario interactivo,
  plan de acción con cómputo de preavisos y plazos de caducidad, creación del documento base en el
  workspace y edición incremental apartado a apartado. NO usar para modificaciones de alcance
  colectivo que superen los umbrales del artículo 41.2, que exigen periodo de consultas, ni para la
  inaplicación del convenio colectivo del artículo 82.3, ni para la suspensión o reducción de jornada
  del artículo 47.
when_to_use: |
  - La empresa quiere modificar la jornada, el horario, el régimen de turnos, el sistema de remuneración o las funciones de un trabajador.
  - La empresa quiere trasladar o desplazar a un trabajador a un centro que exige cambio de residencia.
  - La empresa quiere encomendar funciones distintas de las del grupo profesional del trabajador.
  - El trabajador ha recibido una comunicación de modificación y quiere optar por la extinción indemnizada o impugnarla.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - tipo_medida: modificación sustancial / traslado o desplazamiento / movilidad funcional / respuesta del trabajador
  - materia_afectada: jornada, horario y distribución, turnos, sistema de remuneración y cuantía salarial, sistema de trabajo y rendimiento, o funciones
  - alcance: individual o colectivo, con el número de trabajadores afectados en los últimos 90 días
  - causa_empresarial: acreditación de las razones económicas, técnicas, organizativas o de producción
  - naturaleza_empleador: persona física o persona jurídica
  - datos_empresa: razón social, CIF, domicilio, representante y cargo
  - datos_trabajador: nombre, DNI o NIE, domicilio, categoría, antigüedad, salario
  - condiciones_actuales: condición vigente antes de la modificación, con su origen contractual o convencional
  - condiciones_nuevas: condición que se implanta y fecha de efectos
  - convenio_colectivo: denominación, ámbito y código
outputs:
  - documento_modificacion: comunicación o escrito completo en markdown, DRAFT, con acuse de recibo
references:
  - references/fuentes-plantillas-validadas.md
  - references/art41-modificacion-sustancial.md
  - references/art40-movilidad-geografica.md
  - references/art39-movilidad-funcional.md
  - references/opciones-del-trabajador-y-plazos.md
assets:
  - assets/template-comunicacion-modificacion-sustancial-art41.md
  - assets/template-comunicacion-movilidad-funcional-art39.md
  - assets/template-comunicacion-traslado-art40.md
  - assets/template-escrito-trabajador-opcion-extincion.md
---

# Generar el Documento de Modificación de Condiciones de Trabajo

> DRAFT — para revisión por un abogado o graduado social colegiado antes de su firma y entrega. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de medida):** `mscd_art41` | `traslado_art40` | `movilidad_funcional_art39` | `respuesta_trabajador` | `fuera_de_alcance`.
- **V2 (Materia afectada):** `jornada` | `horario_distribucion` | `turnos` | `remuneracion` | `sistema_trabajo_rendimiento` | `funciones`. *(Determina si nace el derecho de rescisión indemnizada.)*
- **V3 (Alcance):** `individual` | `colectivo_bajo_umbral` | `colectivo_sobre_umbral`.
- **V4 (Posición del usuario):** `empresa` | `trabajador`.
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

### 1.1 Escucha Activa Previa
Si el usuario ya ha identificado inequívocamente la medida, la materia afectada, el número de afectados y su propia posición, registra los vectores en silencio y pasa a la **Fase 2**.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "tipo_medida",
      "rationale": "Resolver V1: cada precepto tiene preaviso, causa y consecuencias indemnizatorias distintos.",
      "question": "¿Qué medida se pretende adoptar o se ha recibido?",
      "options": [
        {"id": "mscd_art41", "label": "Cambio de jornada, horario, turnos, sistema de remuneración, cuantía salarial o funciones"},
        {"id": "traslado_art40", "label": "Traslado o desplazamiento a otro centro que exige cambio de residencia"},
        {"id": "movilidad_funcional_art39", "label": "Encomienda de funciones distintas dentro o fuera del grupo profesional, sin cambio de centro"},
        {"id": "respuesta_trabajador", "label": "El trabajador ha recibido una comunicación y quiere responder"},
        {"id": "fuera_de_alcance", "label": "Inaplicación del convenio, suspensión de contratos o reducción de jornada"}
      ]
    },
    {
      "id": "alcance",
      "rationale": "Resolver V3: superado el umbral, el procedimiento exige periodo de consultas y queda fuera del alcance de esta skill.",
      "question": "¿A cuántos trabajadores afecta la medida en los últimos noventa días?",
      "options": [
        {"id": "individual", "label": "Solo a este trabajador"},
        {"id": "colectivo_bajo_umbral", "label": "A varios, pero por debajo de los umbrales legales (menos de 10 en empresas de menos de 100; menos del 10 por ciento en empresas de 100 a 300; menos de 30 en empresas de 300 o más)"},
        {"id": "colectivo_sobre_umbral", "label": "A un número igual o superior a esos umbrales"}
      ]
    },
    {
      "id": "posicion_usuario",
      "rationale": "Resolver V4: determina si se redacta la comunicación empresarial o la respuesta del trabajador.",
      "question": "¿Desde qué posición actúa usted?",
      "options": [
        {"id": "empresa", "label": "En representación de la empresa"},
        {"id": "trabajador", "label": "En representación del trabajador"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `tipo_medida`
- `V3` — `alcance`
- `V4` — `posicion_usuario`
- `V2` — no se pregunta en el formulario: se deriva durante el propio enrutamiento a partir de la norma aplicable y de los hechos que relate el usuario

### 1.3 Enrutamiento de Estado (Routing por Vectores)

* **Si `[V1 = fuera_de_alcance]` → Detener proceso.** La medida solicitada no es ninguna de las tres que cubre esta skill: identifica la figura y deriva sin crear documento.
* **Si `[V3 = colectivo_sobre_umbral]` → Detener proceso.** Explica en el chat que la medida exige un **periodo de consultas** con la representación de los trabajadores (artículo 41.4), o el procedimiento de inaplicación del convenio del artículo 82.3, con trámites, plazos y documentación propios que exceden de esta skill. Ofrece la derivación al profesional competente. **No crees documento.**
* **Si `[V3 = colectivo_bajo_umbral]` → Advertencia obligatoria antes de continuar:** el cómputo del umbral se hace en periodos sucesivos de noventa días, y superarlo mediante medidas individuales sucesivas determina la **nulidad** de las modificaciones en fraude de ley. Pide el número exacto de afectados en los noventa días anteriores y déjalo consignado.
* **Si `[V1 = mscd_art41]` → Plantilla: `assets/template-comunicacion-modificacion-sustancial-art41.md`.** Resuelve V2 identificando la letra del artículo 41.1. Preaviso: **15 días** de antelación a la fecha de efectividad, con notificación simultánea al trabajador y a sus representantes legales.
* **Si `[V1 = traslado_art40]` → Plantilla: `assets/template-comunicacion-traslado-art40.md`.** Preaviso: **30 días** de antelación a la fecha de efectividad en el traslado. Distingue el traslado (definitivo, o desplazamiento superior a doce meses en un periodo de tres años) del desplazamiento temporal, con preaviso de cinco días laborables si excede de tres meses.
* **Si `[V1 = movilidad_funcional_art39]` → Plantilla: `assets/template-comunicacion-movilidad-funcional-art39.md`.** Distingue la movilidad **dentro del grupo profesional**, que no exige causa ni preaviso, de la que excede del grupo, que exige razones técnicas u organizativas y se limita al tiempo imprescindible. Si la encomienda de funciones excede de los límites del artículo 39, la medida se reconduce al artículo 41 y cambia de ruta.
* **Si `[V1 = respuesta_trabajador]` → Plantilla: `assets/template-escrito-trabajador-opcion-extincion.md`.** Determina primero qué comunicación ha recibido, en qué fecha y qué materia afecta, porque de ello depende que exista o no derecho de rescisión indemnizada.
- `V4` no elige plantilla por si solo: determina si se redacta la comunicacion de la empresa o el escrito de respuesta del trabajador sobre la plantilla enrutada.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión consolidada vigente del Estatuto de los Trabajadores en el BOE.
3. Localiza el convenio colectivo aplicable y comprueba si mejora los preavisos, las compensaciones por traslado o las garantías de jornada y horario. El convenio puede establecer preavisos superiores y compensaciones económicas propias, que prevalecen sobre el mínimo legal.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Marco legal aplicable:** precepto, materia afectada y efectos, explicando qué opciones abre la medida al trabajador.
2. **Calendario de la operación:** fecha de la comunicación, preaviso exigible y fecha de efectividad más temprana posible. Advierte de que una fecha de efectos anterior al vencimiento del preaviso vicia la medida.
3. **Plazos que se abren al trabajador:** 20 días hábiles de caducidad para impugnar (artículo 138 de la Ley 36/2011), y el plazo para optar por la extinción indemnizada cuando proceda.
4. **Cálculo económico preliminar desglosado** de la indemnización por rescisión, cuando la materia afectada la genere.
5. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
6. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:** accede al adjunto y verifica que exprese la causa, la condición anterior y la nueva, la fecha de efectos y el preaviso. Si omite la causa o fija efectos inmediatos, adviértelo y propón la redacción válida.

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
[slot_filling_request (grupos) / Chat (negociación)] --> [Vista previa en texto plano]
      --> [«¿Confirmamos esta sección?»] --> [edit_file en el editor]
```

- **Búsqueda prioritaria, Cero Redundancia y Guardado de Nuevos Clientes (`search_clients` / `get_client` / `save_client` — REG-CLI-01, REG-CLI-02 y REG-CLI-03):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** conforme a `REG-CLI-01`. Si los datos ya constan en el sistema, **queda TERMINANTEMENTE PROHIBIDO volver a pedirlos** (`REG-CLI-02`) y se omite `slot_filling_request`. Si se especifican datos de una persona nueva (por formulario o chat), **pregunta al usuario mediante formulario (`restricted_human_in_the_loop_request`) si desea guardarla como nuevo cliente** (`REG-CLI-03`). En caso afirmativo, invoca `save_client` con los campos disponibles. Luego de esto (o si es negativo), continúa con el flujo normal de redacción y confirmación de la skill.

- **Grupos de datos estructurados no de cliente (MANDATORIO con `slot_filling_request`):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
- **Campos omitidos o negativa expresa (No insistencia):** Si el usuario pide explícitamente no aportar determinados campos de información, pásalos por alto de inmediato sin insistir en pedirlos ni presionar. Rellena la plantilla con los datos disponibles, conserva los no aportados como marcadores pendientes ({{NOMBRE_CAMPO}} o {{DATO_FALTANTE}}) e indica en la confirmación cuáles faltan antes de continuar con la siguiente sección.
- **Anuncio de sección visible** al pasar de una sección a la siguiente, en el mismo mensaje que la primera solicitud.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a identificar a la empresa y al trabajador, así como el convenio colectivo de aplicación."
- Sección 2: "Identificadas las partes, corresponde precisar la condición de trabajo vigente que se pretende modificar."
- Sección 3: "Precisada la condición vigente, procede exponer la causa empresarial que justifica la medida."
- Sección 4: "Expuesta la causa, corresponde concretar la nueva condición y su fecha de efectos."
- Sección 5: "Determinada la nueva condición, procede informar de las opciones y compensaciones que asisten al trabajador."
- Sección 6: "Por último, procede fijar la fórmula de entrega y las comunicaciones a la representación de los trabajadores."

1. **Partes y convenio [dato objetivo].** Solicita en bloque mediante `slot_filling_request` los datos de empresa —razón social, CIF, domicilio, centro de trabajo, firmante y cargo— y de trabajador —nombre, DNI o NIE, domicilio, categoría o grupo profesional, fecha de antigüedad, jornada y salario bruto anual—. Verifica el convenio con `web_search` si el usuario no lo conoce.
2. **Condición vigente [dato objetivo, con validación de origen].** Concreta con exactitud la condición actual y, sobre todo, **de dónde procede**: contrato individual, convenio colectivo, acuerdo colectivo o condición más beneficiosa consolidada. Es determinante: el artículo 41 permite modificar condiciones reconocidas en contrato, en acuerdo o pacto colectivo, o disfrutadas por decisión unilateral de efectos colectivos, pero **las condiciones fijadas en convenio colectivo estatutario solo pueden inaplicarse por el cauce del artículo 82.3**, no por el del artículo 41. Si la condición procede de convenio estatutario, adviértelo y detén la redacción.
3. **Causa empresarial [negociación — el apartado decisivo].** Solicita la acreditación de las razones económicas, técnicas, organizativas o de producción y su **conexión con la medida concreta**. Explica que la causa debe estar relacionada con la competitividad, la productividad o la organización técnica o del trabajo en la empresa, y que la comunicación debe expresarla con detalle suficiente para permitir la defensa. Rechaza las fórmulas genéricas: una causa enunciada sin datos convierte la medida en injustificada.
4. **Nueva condición y fecha de efectos [negociación].** Concreta la nueva condición con el mismo detalle que la anterior, de modo que la comparación sea inmediata. Calcula la fecha de efectos más temprana admisible según el preaviso aplicable —15 días en el artículo 41, 30 días en el traslado del artículo 40, 5 días laborables en desplazamientos superiores a tres meses— y advierte de que anticiparla vicia la medida. Comprueba el preaviso que fije el convenio, que puede ser superior.
5. **Opciones del trabajador y compensaciones [negociación].** Informa expresamente en el propio documento de las opciones que asisten al trabajador:
   - *Artículo 41:* si resulta perjudicado por la modificación en las materias de jornada, horario y distribución del tiempo, régimen de turnos, sistema de remuneración y cuantía salarial, o funciones, tiene derecho a rescindir su contrato con indemnización de **20 días de salario por año de servicio, prorrateándose por meses los periodos inferiores al año, con el máximo de nueve meses**. La modificación del sistema de trabajo y rendimiento no genera ese derecho.
   - *Artículo 40 (traslado):* opción entre aceptar el traslado percibiendo **compensación por gastos** propios y de los familiares a su cargo en los términos convenidos, o extinguir el contrato con indemnización de **20 días de salario por año de servicio, con el máximo de doce mensualidades**.
   - *Artículo 39:* la retribución es la correspondiente a las funciones efectivamente realizadas, salvo en la encomienda de funciones inferiores, en la que se mantiene la retribución de origen.
   Muestra el cálculo desglosado con su fórmula antes de escribirlo.
6. **Entrega y comunicación a la representación [dato objetivo].** Fija la entrega en mano con firma de recibí o burofax, y consigna la **notificación simultánea a los representantes legales de los trabajadores**, exigida por los artículos 40.1 y 41.3. Advierte del plazo de 20 días hábiles de caducidad para impugnar y de que la impugnación no exime al trabajador de cumplir la medida mientras no recaiga resolución.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar un apartado existente.
2. Precisar la causa empresarial o su acreditación.
3. Revisar el preaviso, la fecha de efectos o las compensaciones.
4. Corregir datos identificativos o importes.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Legales Preceptivas de Cierre
- **Carácter DRAFT:** revisión por abogado o graduado social colegiado antes de la firma y entrega.
- **Plazo de impugnación:** 20 días hábiles desde la notificación, sin necesidad de conciliación previa en el proceso del artículo 138 de la Ley 36/2011. Verificar este extremo antes de informar de él.
- **Extinción indemnizada:** el ejercicio del derecho de rescisión es incompatible con la impugnación de la medida; el trabajador debe elegir, y conviene asesorarle antes de que lo haga.
- **Fraude por acumulación:** si en los noventa días siguientes se adoptan nuevas medidas de la misma naturaleza que superen los umbrales sin periodo de consultas, todas ellas serán nulas.
- **Extinción por voluntad del trabajador:** cuando la modificación redunde en menoscabo de la dignidad del trabajador, este puede solicitar la extinción del contrato con la indemnización del despido improcedente (artículo 50.1.a).

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre en el BOE la versión consolidada vigente del Estatuto de los Trabajadores y de la Ley 36/2011, y el convenio colectivo aplicable, antes de redactar. Aplicar la redacción vigente al documento del workspace.
2. **Causa expresada y acreditable:** está PROHIBIDO redactar una comunicación de modificación sin expresar la causa económica, técnica, organizativa o de producción con datos concretos. La causa genérica convierte la medida en injustificada.
3. **Preavisos mínimos:** 15 días en la modificación sustancial individual (artículo 41.3), 30 días en el traslado (artículo 40.1), 5 días laborables en desplazamientos superiores a tres meses (artículo 40.6). El convenio puede ampliarlos, nunca reducirlos.
4. **Notificación a la representación legal de los trabajadores:** simultánea a la del trabajador, en los artículos 40 y 41. Su omisión es un defecto de la medida.
5. **Umbrales del artículo 41.2:** superados en periodos de noventa días, el cauce es el colectivo con periodo de consultas. No redactar comunicaciones individuales sucesivas que eludan el umbral.
6. **Condiciones de convenio estatutario:** no pueden modificarse por el artículo 41. Su inaplicación exige el procedimiento del artículo 82.3. Detener y advertir si la condición procede de convenio.
7. **Derecho de rescisión indemnizada:** informar siempre de él en el propio documento cuando la materia afectada lo genere, con su módulo y su tope. Omitirlo no lo extingue y agrava la posición de la empresa.
8. **Movilidad funcional:** dentro del grupo profesional no requiere causa; fuera de él exige razones técnicas u organizativas y se limita al tiempo imprescindible, sin menoscabo de la dignidad ni perjuicio de la formación y promoción profesional. Nunca redactar una encomienda indefinida de funciones inferiores.
9. **Cero invención:** no inventar causas, datos económicos, cifras de producción ni artículos de convenio. Los datos no aportados permanecen como marcador con su nombre propio de plantilla.
10. **Sintaxis de los marcadores (`{{CLAVE: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real: nunca debe quedar rastro de la anotación en el documento escrito. Los marcadores cuyo dato aún no exista se conservan **íntegros, con su clave y su tipo**, para que el cliente y el profesional que revise vean qué falta y de qué naturaleza es. Está PROHIBIDO sustituir la clave propia del marcador por un literal genérico.
