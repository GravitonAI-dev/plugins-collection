---
name: sancion-disciplinaria
description: >
  Genera los documentos del ejercicio de la potestad disciplinaria del empresario distinta del
  despido: carta de amonestación, carta de sanción por falta grave o muy grave con o sin suspensión
  de empleo y sueldo, pliego de cargos de apertura de expediente contradictorio y resolución del
  expediente. Aplica los artículos 58 y 60.2 del texto refundido de la Ley del Estatuto de los
  Trabajadores aprobado por Real Decreto Legislativo 2/2015 y los artículos 114 y 115 de la Ley
  36/2011 reguladora de la Jurisdicción Social, en sus versiones consolidadas vigentes verificadas en
  el BOE, y toma la tipificación y graduación de faltas y el cuadro de sanciones del convenio
  colectivo aplicable, sin el cual no se redacta ninguna sanción. Metodología: clasificación de la
  gravedad y de las garantías del trabajador mediante formulario interactivo, plan de acción con
  cómputo de prescripción, creación del documento base en el workspace y edición incremental apartado
  a apartado. NO usar para despido disciplinario, que corresponde a la skill `carta-despido`, ni para
  sanciones a personal estatutario o funcionario, sujetos a régimen administrativo propio.
when_to_use: |
  - El usuario quiere sancionar a un trabajador por una falta laboral sin llegar al despido.
  - El usuario quiere redactar una amonestación escrita o una suspensión de empleo y sueldo.
  - El usuario debe abrir expediente contradictorio a un representante legal de los trabajadores o delegado sindical.
  - El usuario pregunta qué sanción corresponde a una conducta según el convenio colectivo aplicable.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - tipo_documento: amonestación / sanción con suspensión de empleo y sueldo / pliego de cargos / resolución de expediente
  - gravedad_falta: leve / grave / muy grave, conforme al convenio colectivo
  - garantias_trabajador: representante legal o sindical / situación de especial protección / ninguna
  - naturaleza_empleador: persona física o persona jurídica
  - datos_empresa: razón social, CIF, domicilio, representante y cargo
  - datos_trabajador: nombre, DNI o NIE, domicilio, categoría, antigüedad
  - convenio_colectivo: denominación, ámbito, código y artículos del régimen disciplinario
  - hechos_imputados: relato concreto, fechado e individualizado de la conducta sancionada
  - fecha_conocimiento: fecha en que la empresa tuvo conocimiento del hecho, a efectos de prescripción
  - sancion_impuesta: tipo, duración y fechas de efectos
outputs:
  - documento_disciplinario: comunicación o escrito completo en markdown, DRAFT, con acuse de recibo
references:
  - references/fuentes-plantillas-validadas.md
  - references/regimen-disciplinario-y-prescripcion.md
  - references/expediente-contradictorio-y-garantias.md
  - references/impugnacion-de-sanciones.md
assets:
  - assets/template-carta-amonestacion.md
  - assets/template-carta-sancion-suspension-empleo-sueldo.md
  - assets/template-pliego-cargos-expediente-contradictorio.md
  - assets/template-resolucion-expediente-contradictorio.md
---

# Generar el Documento de Sanción Disciplinaria

> DRAFT — para revisión por un abogado o graduado social colegiado antes de su firma y entrega. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de documento):** `amonestacion` | `sancion_suspension` | `pliego_cargos` | `resolucion_expediente` | `fuera_de_alcance`.
- **V2 (Gravedad de la falta):** `leve` | `grave` | `muy_grave`, conforme a la tipificación del convenio colectivo.
- **V3 (Naturaleza del empleador):** `persona_fisica` | `persona_juridica`.
- **V4 (Garantías reforzadas del trabajador):** `representante_legal` | `especial_proteccion` | `ninguna`.
- **V5 (Origen plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

### 1.1 Escucha Activa Previa
Si el usuario ya ha identificado inequívocamente la conducta, la sanción pretendida y la condición del trabajador, registra los vectores en silencio y pasa a la **Fase 2**. En otro caso, presenta el formulario estructurado.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "tipo_documento",
      "rationale": "Resolver V1: cada documento responde a un momento distinto del procedimiento disciplinario.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "amonestacion", "label": "Amonestación escrita, sin suspensión de empleo y sueldo"},
        {"id": "sancion_suspension", "label": "Sanción con suspensión de empleo y sueldo"},
        {"id": "pliego_cargos", "label": "Apertura de expediente contradictorio (pliego de cargos)"},
        {"id": "resolucion_expediente", "label": "Resolución de un expediente contradictorio ya instruido"},
        {"id": "fuera_de_alcance", "label": "Despido disciplinario del trabajador"}
      ]
    },
    {
      "id": "garantias_trabajador",
      "rationale": "Resolver V4: determina si el expediente contradictorio es preceptivo y si hay riesgo cualificado de nulidad.",
      "question": "¿Concurre en el trabajador alguna de estas circunstancias?",
      "options": [
        {"id": "representante_legal", "label": "Es representante legal de los trabajadores, delegado sindical o delegado de prevención"},
        {"id": "especial_proteccion", "label": "Ha reclamado o denunciado recientemente, está en situación protegida o hay indicios de trato discriminatorio"},
        {"id": "ninguna", "label": "Ninguna de las anteriores"}
      ]
    },
    {
      "id": "naturaleza_empleador",
      "rationale": "Resolver V3: fija la estructura de comparecencia y la firma del documento.",
      "question": "¿Quién es el empleador?",
      "options": [
        {"id": "persona_juridica", "label": "Empresa, sociedad o entidad (persona jurídica)"},
        {"id": "persona_fisica", "label": "Empresario individual o particular (persona física)"}
      ]
    }
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)

* **Si `[V1 = fuera_de_alcance]` → Deriva a la skill `carta-despido`,** que cubre el despido disciplinario con sus requisitos propios. No crees documento aquí.
* **Si `[V4 = representante_legal]` → El expediente contradictorio es preceptivo** (artículo 68.a del Estatuto de los Trabajadores para representantes legales, y artículo 10.3 de la Ley Orgánica 11/1985 de Libertad Sindical para delegados sindicales), y lo es para toda falta grave o muy grave, no solo para el despido. Fuerza la ruta `pliego_cargos` antes de cualquier sanción y explícalo en el chat.
* **Si `[V4 = especial_proteccion]` → Advertencia obligatoria:** explica que una sanción impuesta como represalia por una reclamación previa vulnera la garantía de indemnidad y sería nula, y que basta con que el trabajador aporte indicios para que la carga de justificar la medida se desplace a la empresa (artículo 181.2 de la Ley 36/2011). Continúa solo si el usuario lo confirma.
* **Si `[V1 = amonestacion]` → Plantilla: `assets/template-carta-amonestacion.md`.** Propia de faltas leves. Aunque el artículo 58.2 solo exige forma escrita para las faltas graves y muy graves, redáctala siempre por escrito: sin constancia no hay antecedente disciplinario utilizable después.
* **Si `[V1 = sancion_suspension]` → Plantilla: `assets/template-carta-sancion-suspension-empleo-sueldo.md`.** Verifica en el convenio la duración máxima de suspensión prevista para la gravedad de la falta.
* **Si `[V1 = pliego_cargos]` → Plantilla: `assets/template-pliego-cargos-expediente-contradictorio.md`.**
* **Si `[V1 = resolucion_expediente]` → Plantilla: `assets/template-resolucion-expediente-contradictorio.md`.** Exige que consten el pliego de cargos, la fecha de su entrega y el pliego de descargos o la constancia de que no se presentó.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. **Localiza el convenio colectivo aplicable con `web_search`** en REGCON o en el boletín oficial correspondiente y extrae de él: el cuadro de faltas y su graduación, el cuadro de sanciones aplicables a cada gravedad, la duración máxima de la suspensión de empleo y sueldo, y las exigencias procedimentales adicionales. **Sin convenio identificado no se redacta la sanción:** si no se localiza, adviértelo y redacta con el mínimo legal dejando constancia de la verificación pendiente.
3. Verifica la versión consolidada vigente del Estatuto de los Trabajadores en el BOE.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Marco legal y convencional:** artículos legales y del convenio, con el cuadro de faltas y sanciones aplicable a la conducta descrita.
2. **Cómputo de la prescripción de la falta** conforme al artículo 60.2, con la fecha límite resultante y la advertencia expresa si el plazo está próximo a vencer o ya ha vencido.
3. **Proporcionalidad de la sanción propuesta:** explica que la sanción debe corresponderse con la gravedad tipificada y que una sanción desproporcionada será revocada o reducida en juicio (artículo 115 de la Ley 36/2011).
4. **Propuesta de plantilla oficial del sistema.**
5. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación de V5 (Origen Plantilla)
* **Si `[V5 = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[V5 = plantilla_usuario]`:** accede al adjunto, verifica que contenga fecha, hechos concretos y la sanción impuesta con su duración, advierte de los defectos detectados y de las sanciones prohibidas por el artículo 58.3, y adopta la minuta revisada.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura (`create_file`):** vuelca íntegramente la plantilla acordada en el workspace con nombre en `snake_case.md`, aplicando **Zero-Omission** y dejando los datos pendientes como marcador con su nombre propio de plantilla.
2. **Validación (`read_file`):** comprueba el volcado íntegro.
3. **Confirmación y encadenamiento:** informa de la ruta absoluta y, en la misma respuesta, abre la primera sección de la Fase 4 con su anuncio y su primera solicitud de datos.

---

## FASE 4 — EDICIÓN INCREMENTAL APARTADO A APARTADO

### Protocolo Obligatorio de Edición
```
[slot_filling_request (grupos) / Chat (negociación)] ──> [Vista previa en texto plano]
      ──> [«¿Confirmamos esta sección?»] ──> [edit_file + read_file]
```

- **Datos estructurados agrupados (`slot_filling_request`, MANDATORIO):** empresa, trabajador y relación laboral se solicitan en bloque, nunca dato a dato en turnos sucesivos.
- **Confirmación obligatoria en el chat** antes de todo `edit_file`, con verificación posterior mediante `read_file`.
- **Anuncio de sección visible** al pasar de una sección a la siguiente, en el mismo mensaje que la primera solicitud, sin pedir permiso aparte.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a identificar a la empresa y al trabajador, así como el convenio colectivo de aplicación."
- Sección 2: "Identificadas las partes, corresponde concretar los hechos objeto de reproche disciplinario."
- Sección 3: "Concretados los hechos, procede su calificación conforme al convenio colectivo."
- Sección 4: "Calificada la falta, corresponde determinar la sanción y su fecha de efectos."
- Sección 5: "Por último, procede fijar la fórmula de entrega y acuse de recibo."

1. **Partes y convenio [dato objetivo].** Solicita en bloque mediante `slot_filling_request`: razón social o nombre del empleador, CIF o NIF, domicilio, nombre, NIF y cargo del firmante si V3 es persona jurídica; nombre del trabajador, DNI o NIE, domicilio, categoría o grupo profesional, y fecha de antigüedad. Pide la denominación del convenio y, si el usuario no la conoce, verifícala tú mismo con `web_search`.
2. **Hechos [negociación — el apartado decisivo].** Solicita el relato en el chat y exige para cada hecho fecha o periodo concreto, lugar, conducta descrita objetivamente sin adjetivos valorativos, personas afectadas y medios de acreditación disponibles. Rechaza las fórmulas genéricas explicando que la sanción se revisa judicialmente sobre los hechos escritos y solo sobre ellos. Pregunta expresamente por la **fecha en que la empresa tuvo conocimiento del hecho** y calcula la prescripción del artículo 60.2: 10 días para las leves, 20 para las graves y 60 para las muy graves desde ese conocimiento, y 6 meses desde la comisión en todo caso. Advierte de cualquier hecho prescrito y no lo imputes.
3. **Calificación [negociación].** Encaja la conducta en el artículo del convenio que la tipifica, citando su número y su texto, y fija la gravedad. Si el convenio no tipifica la conducta, adviértelo: la potestad disciplinaria no permite crear faltas no previstas. Comprueba el principio *non bis in idem*: un mismo hecho no puede sancionarse dos veces, y una sanción ya impuesta no puede agravarse después.
4. **Sanción y efectos [negociación].** Determina la sanción dentro del cuadro del convenio para esa gravedad y su duración. Comprueba las **sanciones prohibidas** del artículo 58.3: no cabe imponer sanciones que consistan en reducción de la duración de las vacaciones, en otra minoración de los derechos al descanso, ni multa de haber. Fija las fechas de inicio y fin de la suspensión de empleo y sueldo, si procede, y advierte de que durante ella el trabajador permanece en alta con obligación de cotizar. Explica la proporcionalidad exigible y el alcance de la revisión judicial del artículo 115 de la Ley 36/2011.
5. **Entrega y acuse de recibo [dato objetivo].** Fija la entrega en mano con firma de recibí, con la alternativa de burofax si el trabajador se niega o no acude, y la constancia ante dos testigos de la negativa a firmar. Recuerda la obligación de comunicar a la representación legal de los trabajadores las sanciones por faltas graves y muy graves cuando el convenio o el artículo 64.4.c del Estatuto de los Trabajadores así lo prevean, y advierte del plazo de **20 días hábiles** de que dispone el trabajador para impugnar la sanción.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar un apartado existente.
2. Precisar hechos o añadir medios de acreditación.
3. Revisar la calificación o la proporcionalidad de la sanción.
4. Corregir datos identificativos o fechas.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Legales Preceptivas de Cierre
- **Carácter DRAFT:** revisión por abogado o graduado social colegiado antes de la firma y entrega.
- **Plazo de impugnación:** 20 días hábiles desde la notificación, con conciliación previa (artículo 114 de la Ley 36/2011).
- **Conservación de la prueba:** el acuse de recibo y los medios de acreditación de los hechos son la única base admisible de la defensa en juicio.
- **Efecto de antecedente:** la sanción firme queda como antecedente disciplinario a efectos de reincidencia durante el plazo que fije el convenio; transcurrido ese plazo debe considerarse cancelada.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre en el BOE la versión consolidada vigente del Estatuto de los Trabajadores y de la Ley 36/2011, y localizar el convenio colectivo en su registro oficial, antes de redactar. Aplicar la redacción vigente al documento del workspace sin usar versiones desactualizadas.
2. **Sin convenio no hay tipificación:** la potestad disciplinaria se ejerce conforme a la graduación de faltas y sanciones establecida en las disposiciones legales o en el convenio colectivo aplicable (artículo 58.1). No inventar faltas ni sanciones no previstas.
3. **Forma escrita (artículo 58.2):** la sanción de faltas graves y muy graves requiere comunicación escrita al trabajador haciendo constar la fecha y los hechos que la motivan.
4. **Sanciones prohibidas (artículo 58.3):** no cabe imponer sanciones que consistan en reducción de la duración de las vacaciones u otra minoración de los derechos al descanso, ni multa de haber. Rechazar la redacción si el usuario lo solicita, citando el precepto.
5. **Prescripción de faltas (artículo 60.2):** leves 10 días, graves 20 días, muy graves 60 días desde que la empresa tuvo conocimiento, y 6 meses desde su comisión en todo caso. Calcular y advertir siempre.
6. **Expediente contradictorio:** preceptivo para representantes legales de los trabajadores y delegados sindicales, para toda falta grave o muy grave, y siempre que el convenio lo exija. Su omisión determina la nulidad de la sanción.
7. **Non bis in idem:** un mismo hecho no puede sancionarse dos veces ni agravarse una sanción ya impuesta y notificada.
8. **Proporcionalidad:** la sanción debe ajustarse a la gravedad tipificada. El juzgado puede revocarla o autorizar la imposición de una sanción adecuada a la falta de menor gravedad que resulte probada (artículo 115 de la Ley 36/2011).
9. **Cero invención:** no inventar hechos, fechas, antecedentes disciplinarios, artículos de convenio ni jurisprudencia. Los datos no aportados permanecen como marcador con su nombre propio de plantilla.
