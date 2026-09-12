---
name: reclamacion-seguridad-social
description: >
  Genera los escritos de impugnación de resoluciones en materia de prestaciones de Seguridad Social:
  reclamación administrativa previa ante la entidad gestora, escrito de disconformidad con el alta
  médica, solicitud de revisión del grado de incapacidad permanente y demanda ante el Juzgado de lo
  Social una vez agotada la vía previa. Aplica la **Ley General de la Seguridad Social aprobada por Real
  Decreto Legislativo 8/2015**, que regula las prestaciones del sistema y los requisitos para acceder a ellas, y los artículos 71 y 140 a 147 de la **Ley 36/2011 reguladora de la
  Jurisdicción Social**, que regula la reclamación previa y el proceso en materia de prestaciones, en sus versiones consolidadas vigentes verificadas en el BOE. Su función
  crítica es de control de plazos y de vía: en esta materia la conciliación previa está exceptuada
  pero la reclamación administrativa previa es requisito inexcusable, y los plazos son breves y de
  caducidad. Metodología: clasificación de la materia y la entidad gestora mediante formulario
  interactivo, plan de acción con el cómputo de plazos, creación del documento base en el workspace y
  edición incremental apartado a apartado. NO usar para actos de encuadramiento, afiliación,
  cotización y recaudación frente a la Tesorería General de la Seguridad Social, que siguen la vía
  administrativa común y el orden contencioso-administrativo, ni para la tramitación inicial de altas
  y bajas, que corresponde al plugin `gestoria`.
when_to_use: |
  - El usuario ha recibido una resolución del Instituto Nacional de la Seguridad Social, del Servicio Público de Empleo Estatal o de una mutua y quiere impugnarla.
  - El usuario quiere reclamar un grado superior de incapacidad permanente o su revisión.
  - El usuario está en desacuerdo con un alta médica y quiere manifestar su disconformidad.
  - El usuario quiere demandar en materia de prestaciones tras agotar la reclamación previa.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - tipo_tramite: reclamación previa / disconformidad con alta médica / solicitud de revisión de grado / demanda
  - materia: incapacidad temporal / incapacidad permanente / lesiones permanentes no invalidantes / jubilación / viudedad y orfandad / nacimiento y cuidado / desempleo / reintegro de gastos / recargo de prestaciones
  - entidad_gestora: Instituto Nacional de la Seguridad Social / Instituto Social de la Marina / Servicio Público de Empleo Estatal / mutua colaboradora con la Seguridad Social
  - posicion_usuario: beneficiario o empresa
  - datos_interesado: nombre, DNI o NIE, número de afiliación, domicilio, teléfono y correo
  - datos_resolucion: órgano, fecha de la resolución, fecha de notificación, número de expediente y contenido
  - datos_profesionales: profesión habitual, categoría, antigüedad, régimen de encuadramiento y bases de cotización
  - cuadro_clinico: dolencias, limitaciones funcionales e informes médicos disponibles con su fecha y facultativo
  - fundamentos: motivos de la impugnación
outputs:
  - reclamacion_previa: escrito de reclamación administrativa previa en markdown, DRAFT, listo para su presentación
  - demanda_seguridad_social: demanda ante el Juzgado de lo Social en markdown, DRAFT
references:
  - references/fuentes-plantillas-validadas.md
  - references/reclamacion-previa-y-plazos.md
  - references/grados-de-incapacidad-permanente.md
  - references/alta-medica-y-disconformidad.md
  - references/prueba-medica-y-expediente.md
assets:
  - assets/template-demanda-seguridad-social.md
  - assets/template-escrito-disconformidad-alta-medica.md
  - assets/template-reclamacion-previa-prestaciones.md
  - assets/template-solicitud-revision-grado-incapacidad.md
---

# Generar los Escritos de Impugnación en Materia de Seguridad Social

> DRAFT — para revisión por un abogado o graduado social colegiado antes de su firma y presentación. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de trámite):** `reclamacion_previa` | `disconformidad_alta` | `revision_grado` | `demanda` | `fuera_de_alcance`.
- **V2 (Materia prestacional):** `incapacidad_temporal` | `incapacidad_permanente` | `lesiones_permanentes` | `jubilacion` | `muerte_y_supervivencia` | `nacimiento_y_cuidado` | `desempleo` | `reintegro_gastos` | `recargo_prestaciones`.
- **V3 (Entidad gestora o colaboradora):** `inss` | `ism` | `sepe` | `mutua`. *(Determina el órgano destinatario y el procedimiento aplicable.)*
- **V4 (Posición del usuario):** `beneficiario` | `empresa`.
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

### 1.1 Escucha Activa Previa
Si el usuario ya ha identificado inequívocamente la materia, la entidad y el trámite, registra los vectores en silencio y pasa a la **Fase 2**. En todo caso, **la primera acción sustantiva es el control de plazo y de vía del punto 1.3**: en esta materia los plazos son de treinta días y de caducidad, y el asunto se pierde por el calendario antes que por el fondo.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "tipo_tramite",
      "rationale": "Resolver V1: la vía previa administrativa es requisito inexcusable para demandar, y el alta médica tiene un procedimiento propio con plazos de días.",
      "question": "¿En qué situación se encuentra el asunto?",
      "options": [
        {"id": "reclamacion_previa", "label": "Se ha recibido una resolución y hay que impugnarla en vía administrativa"},
        {"id": "disconformidad_alta", "label": "Se ha recibido un alta médica y se quiere manifestar disconformidad"},
        {"id": "revision_grado", "label": "Se quiere solicitar la revisión de un grado de incapacidad ya reconocido"},
        {"id": "demanda", "label": "Ya se ha resuelto o ha transcurrido el plazo de la reclamación previa y procede demandar"},
        {"id": "fuera_de_alcance", "label": "Se trata de afiliación, cotización, recaudación o una sanción administrativa"}
      ]
    },
    {
      "id": "materia",
      "rationale": "Resolver V2: cada prestación tiene requisitos, base reguladora y controversia típica distintos.",
      "question": "¿Sobre qué prestación versa el asunto?",
      "options": [
        {"id": "incapacidad_permanente", "label": "Incapacidad permanente: denegación, grado insuficiente o revisión"},
        {"id": "incapacidad_temporal", "label": "Incapacidad temporal: alta médica, denegación o determinación de la contingencia"},
        {"id": "prestacion_economica", "label": "Jubilación, viudedad, orfandad, nacimiento y cuidado, u otra prestación económica"},
        {"id": "desempleo", "label": "Desempleo: denegación, extinción, suspensión o reclamación de prestaciones indebidas"},
        {"id": "otra", "label": "Reintegro de gastos, recargo de prestaciones, o lesiones permanentes no invalidantes"}
      ]
    },
    {
      "id": "entidad_gestora",
      "rationale": "Resolver V3: el escrito se dirige al órgano que dictó la resolución, y el procedimiento varía según la entidad.",
      "question": "¿Qué entidad ha dictado la resolución?",
      "options": [
        {"id": "inss", "label": "Instituto Nacional de la Seguridad Social"},
        {"id": "sepe", "label": "Servicio Público de Empleo Estatal"},
        {"id": "mutua", "label": "Mutua colaboradora con la Seguridad Social"},
        {"id": "ism", "label": "Instituto Social de la Marina u otra entidad"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `tipo_tramite`
- `V2` — `materia`
- `V3` — `entidad_gestora`
- `V4` — posición del usuario: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo

### 1.3 Control de Plazo y de Vía (PRIMERA ACCIÓN OBLIGATORIA)

**Comprobación 1 — Pide la fecha de notificación de la resolución.** No la fecha de la resolución: la de su **notificación**, que es la que abre el plazo. Si el usuario no la conoce con certeza, pídele que compruebe el acuse de recibo o el justificante de la notificación electrónica.

**Comprobación 2 — Calcula y comunica el plazo.**
- **Reclamación previa:** el plazo es de **treinta días** desde la notificación de la resolución (artículo 71.2 de la Ley 36/2011).
- **Demanda tras la reclamación previa:** **treinta días** desde la notificación de la resolución de la reclamación previa o desde que deba entenderse denegada por silencio.
- **Silencio administrativo:** transcurrido el plazo legalmente previsto sin resolución expresa, la reclamación previa se entiende **denegada por silencio**, y desde ese momento se abre el plazo para demandar.
- **Disconformidad con el alta médica:** el plazo se cuenta en **días naturales** y es muy breve. Verifícalo en el texto vigente antes de comunicarlo y adviértelo con urgencia.

**Verifica con `web_search` los plazos exactos y el plazo de resolución de la entidad en el texto vigente antes de comunicarlos.** Son cifras que han variado y de las que depende el asunto.

**Comprobación 3 — Comprueba la vía.**
- La **conciliación previa está exceptuada** en materia de Seguridad Social (artículo 64 de la Ley 36/2011): no hay que presentar papeleta, y hacerlo no suspende ningún plazo.
- La **reclamación administrativa previa es requisito inexcusable** para formular demanda (artículo 71). Sin ella, la demanda no se admite.
- Si el usuario quiere demandar y **no consta reclamación previa**, detén la redacción de la demanda y redacta primero la reclamación previa, si el plazo lo permite.

**Comprobación 4 — Enrutamiento:**
* **Si `[V1 = fuera_de_alcance]` → Detener.** Los actos de encuadramiento, afiliación, cotización, recaudación y las sanciones administrativas siguen la vía administrativa común y, en su caso, el orden contencioso-administrativo. Deriva al profesional competente. **No crees documento.**
* **Si `[V1 = reclamacion_previa]` → Plantilla: `assets/template-reclamacion-previa-prestaciones.md`.**
* **Si `[V1 = disconformidad_alta]` → Plantilla: `assets/template-escrito-disconformidad-alta-medica.md`.** Advierte del plazo brevísimo y de que la disconformidad debe presentarse en el plazo y ante el órgano correctos, o el alta despliega todos sus efectos.
* **Si `[V1 = revision_grado]` → Plantilla: `assets/template-solicitud-revision-grado-incapacidad.md`.** Comprueba que haya transcurrido el plazo de revisión fijado en la resolución de reconocimiento o que concurra agravación o mejoría acreditada.
* **Si `[V1 = demanda]` → Plantilla: `assets/template-demanda-seguridad-social.md`.** Exige la resolución de la reclamación previa o la acreditación de su desestimación presunta.
- `V2` no elige plantilla: determina los requisitos, la base reguladora y la controversia tipica que se argumentan en el escrito.
- `V3` no elige plantilla: determina el organo destinatario, que es el que dicto la resolucion, y las particularidades de tramitacion de esa entidad.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión consolidada vigente de la Ley General de la Seguridad Social y de la Ley 36/2011 en el BOE.
3. **Verifica los criterios vigentes de calificación de la incapacidad permanente:** la definición de los grados ha sido objeto de reformas y de un régimen transitorio, de modo que el precepto formalmente vigente puede remitir a la regulación anterior. No expliques los grados sin haberlo comprobado.
4. Verifica las **magnitudes del ejercicio en curso** que puedan condicionar la prestación: salario mínimo interprofesional, indicador público de renta de efectos múltiples, bases máximas y mínimas de cotización, porcentajes aplicables y topes de pensión.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Vía y trámite procedentes**, con la advertencia de que la conciliación no procede y de que la reclamación previa es requisito para demandar.
2. **Cómputo del plazo** con la fecha límite, y advertencia expresa si el margen es escaso.
3. **Órgano destinatario** exacto y forma de presentación, incluida la sede electrónica cuando exista.
4. **Motivos de impugnación** que se van a articular y **prueba médica o documental** que conviene reunir, con indicación de lo que falta.
5. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
6. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:** accede al adjunto y verifica que identifique al interesado con su número de afiliación, la resolución impugnada con su expediente y fecha de notificación, los motivos y la pretensión. Advierte de las omisiones y propón la redacción válida.

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
[slot_filling_request (grupos) / Chat (cuadro clínico y motivos)] --> [Vista previa en texto plano]
      --> [«¿Confirmamos esta sección?»] --> [edit_file en el editor]
```

- **Búsqueda prioritaria, Cero Redundancia y Guardado de Nuevos Clientes (`search_clients` / `get_client` / `save_client` — REG-CLI-01, REG-CLI-02 y REG-CLI-03):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** conforme a `REG-CLI-01`. Si los datos ya constan en el sistema, **queda TERMINANTEMENTE PROHIBIDO volver a pedirlos** (`REG-CLI-02`) y se omite `slot_filling_request`. Si se especifican datos de una persona nueva (por formulario o chat), **DEBES invocar INMEDIATAMENTE `restricted_human_in_the_loop_request`** para preguntar al usuario si desea guardarla como nuevo cliente (`REG-CLI-03`), quedando **TERMINANTEMENTE PROHIBIDO emitir la vista previa de la cláusula o decir 'le preguntaré después' antes de resolver el guardado**. En caso afirmativo, invoca `save_client` con los campos disponibles. Solo tras resolver el guardado (o si el usuario lo rechaza), continúa con el flujo normal de vista previa y confirmación de la cláusula.

- **Grupos de datos estructurados no de cliente (MANDATORIO con `slot_filling_request`):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
- **Campos omitidos o negativa expresa (No insistencia):** Si el usuario pide explícitamente no aportar determinados campos de información, pásalos por alto de inmediato sin insistir en pedirlos ni presionar. Rellena la plantilla con los datos disponibles, conserva los no aportados como marcadores pendientes ({{NOMBRE_CAMPO}} o {{DATO_FALTANTE}}) e indica en la confirmación cuáles faltan antes de continuar con la siguiente sección.
- **Anuncio de sección visible** al pasar de una sección a la siguiente.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a identificar al interesado y el expediente administrativo de referencia."
- Sección 2: "Identificado el expediente, corresponde precisar el contenido de la resolución que se impugna y la fecha de su notificación."
- Sección 3: "Precisada la resolución, procede describir la profesión habitual y las condiciones reales del puesto."
- Sección 4: "Descrita la profesión, corresponde exponer el cuadro clínico y las limitaciones funcionales acreditadas."
- Sección 5: "Expuesto el cuadro clínico, procede desarrollar los motivos de la impugnación."
- Sección 6: "Por último, procede formular la pretensión y relacionar la documentación que se acompaña."

1. **Interesado y expediente [dato objetivo].** Solicita en bloque mediante `slot_filling_request`: nombre y apellidos, DNI o NIE, **número de afiliación a la Seguridad Social**, domicilio, teléfono y correo electrónico; y número de expediente, órgano y provincia de la dirección provincial. El número de afiliación y el de expediente son imprescindibles: sin ellos el escrito no se vincula al procedimiento.
2. **Resolución impugnada [dato objetivo, con validación del plazo].** Fecha de la resolución, **fecha de notificación**, contenido de la parte dispositiva y motivación que la entidad haya expresado, incluido el dictamen del equipo de valoración de incapacidades si consta. Recalcula y confirma el plazo con la fecha de notificación definitiva.
3. **Profesión habitual y condiciones del puesto [negociación — decisivo en incapacidad].** Solicita profesión habitual, categoría, antigüedad, y una **descripción real de las tareas**: esfuerzos, posturas mantenidas, manipulación de cargas, bipedestación, exposición a riesgos, ritmo, turnos y requerimientos cognitivos. Explica por qué importa: la incapacidad permanente total se define por relación con la **profesión habitual**, de modo que las mismas dolencias pueden dar lugar a grados distintos según el puesto. Un escrito que no describe el puesto con precisión pierde su mejor argumento.
4. **Cuadro clínico y limitaciones [dato objetivo, con inventario de prueba].** Solicita el listado de dolencias con su diagnóstico, los informes médicos disponibles con su fecha, facultativo y servicio, las pruebas objetivas practicadas, los tratamientos seguidos y las **limitaciones funcionales** resultantes. Distingue con claridad diagnóstico de limitación: lo que decide el grado no es la etiqueta diagnóstica sino la limitación funcional acreditada. Señala qué informes faltan y recomienda obtenerlos antes de presentar. **No inventes ni interpretes datos clínicos**: transcribe lo que digan los informes.
5. **Motivos de la impugnación [negociación].** Articula los motivos que correspondan a la materia: error en la valoración de las limitaciones funcionales; no consideración de dolencias acreditadas; inadecuación del grado reconocido a la profesión habitual; error en la determinación de la **contingencia**, común o profesional, con su relevancia sobre la base reguladora y los requisitos; error en el cálculo de la base reguladora o del porcentaje; error en el periodo de carencia; falta de motivación; o incongruencia con el dictamen médico. Cita solo preceptos verificados.
6. **Pretensión y documentación [negociación].** Formula la pretensión concreta: reconocimiento del grado que se solicita con su porcentaje y efectos económicos, determinación de la contingencia, o rectificación de la base reguladora, con la fecha de efectos pretendida. Relaciona numerada la documentación que se acompaña y solicita expresamente la **aportación del expediente administrativo completo**, incluido el historial clínico y los dictámenes médicos, que es la fuente esencial de la impugnación.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar un apartado existente.
2. Ampliar el cuadro clínico o incorporar nuevos informes médicos.
3. Precisar la descripción de la profesión habitual y sus requerimientos.
4. Revisar los motivos de impugnación y la pretensión.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Legales Preceptivas de Cierre
- **Carácter DRAFT:** revisión por abogado o graduado social colegiado antes de su firma y presentación.
- **Plazo:** recordar la fecha límite calculada y que el plazo es de caducidad. Presentar por registro con **justificante fechado** o por la sede electrónica de la entidad, conservando el acuse.
- **Silencio administrativo:** si la entidad no resuelve en plazo, la reclamación se entiende denegada y se abre el plazo para demandar. Anotar la fecha en que se produce el silencio para no perder el plazo judicial esperando una respuesta que puede no llegar.
- **Conciliación no aplicable:** en esta materia no hay que presentar papeleta, y presentarla no suspende ningún plazo.
- **Prueba médica:** los informes de especialista con pruebas objetivas y descripción de limitaciones funcionales son la prueba decisiva. Un informe que solo consigna diagnósticos, sin limitaciones, tiene poco valor. Valorar un informe pericial de valoración del daño corporal cuando el asunto lo justifique.
- **Compatibilidad y efectos:** advertir de las reglas de compatibilidad de cada grado con el trabajo, de la revisión periódica del grado reconocido, y del efecto de la reincorporación al trabajo sobre la prestación.
- **Justicia gratuita:** las personas beneficiarias del sistema de la Seguridad Social tienen reconocido el derecho a la asistencia jurídica gratuita en el orden social en los términos legalmente previstos. Verificar el alcance vigente antes de informar.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre en el BOE la versión consolidada vigente de la Ley General de la Seguridad Social y de la Ley 36/2011 antes de redactar, y aplicar la redacción vigente al documento del workspace.
2. **Control de plazo como primera acción**, calculado desde la **fecha de notificación**. Los plazos exactos se verifican con `web_search` una sola vez, en el control de la Fase 1.3, y su resultado se reutiliza: son breves, de caducidad, y han variado con las reformas.
3. **Reclamación previa inexcusable:** no redactar demanda sin acreditar el agotamiento de la vía previa administrativa, expresa o por silencio.
4. **Conciliación exceptuada:** no derivar a la skill `conciliacion-previa` ni redactar papeleta en esta materia.
5. **Grados de incapacidad:** no explicar ni invocar la definición de los grados sin verificar el precepto vigente y su régimen transitorio. La regulación formalmente en vigor puede remitir a la anterior.
6. **Cero invención clínica:** está PROHIBIDO inventar, deducir o interpretar diagnósticos, pruebas, limitaciones funcionales o valoraciones médicas. Solo se consigna lo que conste en informes aportados, con su fecha y facultativo. Lo que falte permanece como marcador y se indica al usuario qué informe debe obtener.
7. **Cero invención de magnitudes:** bases reguladoras, porcentajes, topes de pensión, salario mínimo interprofesional e indicador público de renta de efectos múltiples se verifican con `web_search` en la normativa del ejercicio. No se escriben de memoria.
8. **Profesión habitual:** no redactar una impugnación de grado sin una descripción real y detallada de las tareas del puesto. Es el argumento central y su omisión debilita el escrito.
9. **Cita de jurisprudencia:** prohibido citar sentencias o doctrina no verificadas en esta misma sesión mediante `web_search` en una fuente oficial.
10. **Solicitud del expediente:** pedir siempre la aportación del expediente administrativo completo con el historial clínico y los dictámenes, tanto en la reclamación previa como en la demanda.
11. **Sintaxis de los marcadores (`{{CLAVE: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real: nunca debe quedar rastro de la anotación en el documento escrito. Los marcadores cuyo dato aún no exista se conservan **íntegros, con su clave y su tipo**, para que el cliente y el profesional que revise vean qué falta y de qué naturaleza es. Está PROHIBIDO sustituir la clave propia del marcador por un literal genérico.
