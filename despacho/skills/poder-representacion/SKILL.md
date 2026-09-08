---
name: poder-representacion
description: >
  Genera los instrumentos de representación con que el despacho actúa por cuenta de su cliente: minuta
  de poder general para pleitos y de poder especial con facultades tasadas para su otorgamiento ante
  notario, solicitud de apoderamiento apud acta ante el letrado de la Administración de Justicia o por
  comparecencia electrónica, designación de representación y defensa en el orden social, y
  autorización de representación en el procedimiento administrativo común. Aplica los artículos 23 a
  26 de la Ley 1/2000 de Enjuiciamiento Civil, los artículos 18 y 21 de la Ley 36/2011 reguladora de
  la Jurisdicción Social y los artículos 5 y 6 de la Ley 39/2015 del Procedimiento Administrativo
  Común de las Administraciones Públicas, en sus versiones consolidadas vigentes verificadas en el
  BOE. Su función crítica es advertir de las facultades que exigen **poder especial** y que un poder
  general no cubre. Metodología: clasificación del ámbito y del alcance mediante formulario
  interactivo, plan de acción con la relación de facultades, creación del documento base en el
  workspace y edición incremental apartado a apartado. NO usar para poderes preventivos ni medidas de
  apoyo a personas con discapacidad, que corresponden a la skill
  `derecho-civil:medidas-apoyo-discapacidad`, ni para poderes mercantiles de representación orgánica
  de sociedades.
when_to_use: |
  - El despacho necesita la minuta de un poder para pleitos para que el cliente lo otorgue ante notario.
  - El cliente va a apoderar por comparecencia ante el letrado de la Administración de Justicia o por vía electrónica.
  - Hay que designar representación y defensa en un procedimiento del orden social.
  - Hay que acreditar la representación del cliente ante una administración pública.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - tipo_instrumento: poder general para pleitos / poder especial / apoderamiento apud acta / designación en el orden social / autorización administrativa
  - ambito: civil, penal y contencioso-administrativo / social / procedimiento administrativo
  - alcance: general con todas las facultades ordinarias / especial con facultades tasadas
  - naturaleza_otorgante: persona física / persona jurídica
  - datos_otorgante: nombre o razón social, documento de identidad o CIF, domicilio, y datos y título del representante orgánico si es persona jurídica
  - datos_apoderados: nombre, número de colegiado y colegio de cada profesional que se apodera
  - facultades_especiales: facultades del artículo 25.2 que el otorgante concede o excluye expresamente
  - datos_procedimiento: órgano, clase de procedimiento y número de autos, si el apoderamiento es para un asunto concreto
outputs:
  - minuta_poder: minuta del poder para su otorgamiento ante notario en markdown, DRAFT
  - escrito_apoderamiento: solicitud de apoderamiento apud acta o designación de representación en markdown, DRAFT
references:
  - references/fuentes-y-normativa-colegial.md
  - references/representacion-procesal-y-postulacion.md
  - references/facultades-del-poder-y-poder-especial.md
  - references/apoderamientos-electronicos-y-registros.md
assets:
  - assets/template-autorizacion-representacion-administrativa.md
  - assets/template-designacion-representacion-social.md
  - assets/template-minuta-poder-especial.md
  - assets/template-minuta-poder-general-pleitos.md
  - assets/template-solicitud-apoderamiento-apud-acta.md
---

# Generar el Instrumento de Representación

> DRAFT — para revisión por el profesional responsable antes de su otorgamiento o presentación. La minuta de poder debe ser revisada y adaptada por el notario autorizante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de instrumento):** `poder_general` | `poder_especial` | `apud_acta` | `designacion_social` | `autorizacion_administrativa`.
- **V2 (Ámbito):** `civil_penal_contencioso` | `social` | `administrativo`. *(Determina la norma aplicable y si es exigible procurador.)*
- **V3 (Naturaleza del otorgante):** `persona_fisica` | `persona_juridica`. *(Si es jurídica, exige acreditar el título del representante orgánico.)*
- **V4 (Alcance):** `general` | `especial_facultades_tasadas`.
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

### 1.1 Escucha Activa Previa
Si el usuario ya ha identificado el instrumento, el ámbito y el alcance, registra los vectores en silencio y pasa a la **Fase 2**.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "ambito",
      "rationale": "Resolver V2: la norma aplicable, la exigencia de procurador y la forma del apoderamiento son distintas en cada orden.",
      "question": "¿En qué ámbito va a actuarse en representación del cliente?",
      "options": [
        {"id": "civil_penal_contencioso", "label": "Jurisdicción civil, penal o contencioso-administrativa"},
        {"id": "social", "label": "Jurisdicción social: Juzgado de lo Social o Sala de lo Social"},
        {"id": "administrativo", "label": "Procedimiento administrativo ante una administración pública"}
      ]
    },
    {
      "id": "tipo_instrumento",
      "rationale": "Resolver V1: la forma del apoderamiento condiciona el documento y el trámite.",
      "question": "¿Cómo va a conferirse la representación?",
      "options": [
        {"id": "poder_general", "label": "Poder general para pleitos otorgado ante notario"},
        {"id": "poder_especial", "label": "Poder especial con facultades tasadas otorgado ante notario"},
        {"id": "apud_acta", "label": "Apoderamiento apud acta: comparecencia ante el letrado de la Administración de Justicia o comparecencia electrónica"},
        {"id": "designacion_social", "label": "Designación de representación y defensa en un procedimiento del orden social"},
        {"id": "autorizacion_administrativa", "label": "Autorización de representación ante una administración pública"}
      ]
    },
    {
      "id": "naturaleza_otorgante",
      "rationale": "Resolver V3: si el otorgante es persona jurídica, hay que acreditar el título y la suficiencia del representante orgánico que apodera.",
      "question": "¿Quién otorga la representación?",
      "options": [
        {"id": "persona_fisica", "label": "Persona física, en su propio nombre y derecho"},
        {"id": "persona_juridica", "label": "Persona jurídica, a través de su representante orgánico"}
      ]
    },
    {
      "id": "alcance",
      "rationale": "Resolver V4: determinadas facultades exigen poder especial y no quedan cubiertas por el poder general.",
      "question": "¿Qué alcance debe tener la representación?",
      "options": [
        {"id": "general", "label": "General: todas las facultades ordinarias para la tramitación del asunto"},
        {"id": "especial_facultades_tasadas", "label": "Especial: solo determinadas facultades, o incluyendo expresamente facultades que exigen poder especial"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `tipo_instrumento`
- `V2` — `ambito`
- `V3` — `naturaleza_otorgante`
- `V4` — `alcance`

### 1.3 Enrutamiento de Estado (Routing por Vectores)

* **Si `[V1 = poder_general]` → Plantilla: `assets/template-minuta-poder-general-pleitos.md`.**
* **Si `[V1 = poder_especial]` o `[V4 = especial_facultades_tasadas]` → Plantilla: `assets/template-minuta-poder-especial.md`.**
* **Si `[V1 = apud_acta]` → Plantilla: `assets/template-solicitud-apoderamiento-apud-acta.md`.** Explica que el apoderamiento apud acta evita el coste del otorgamiento notarial y que puede realizarse por comparecencia personal ante el letrado de la Administración de Justicia o por comparecencia electrónica, e informa de que su constancia se produce en el registro electrónico de apoderamientos judiciales correspondiente. **Verifica el trámite y la sede aplicables con `web_search`** antes de indicárselos al usuario.
* **Si `[V1 = designacion_social]` → Plantilla: `assets/template-designacion-representacion-social.md`.** Explica el régimen propio del orden social: en la instancia las partes pueden comparecer por sí mismas o conferir su representación a abogado, procurador, graduado social colegiado o cualquier persona en el pleno ejercicio de sus derechos civiles, y en los recursos de suplicación y casación la defensa de abogado es preceptiva.
* **Si `[V1 = autorizacion_administrativa]` → Plantilla: `assets/template-autorizacion-representacion-administrativa.md`.** Explica la distinción del artículo 5 de la Ley 39/2015: para los actos y gestiones de **mero trámite** se presume la representación, pero para **formular solicitudes, presentar declaraciones responsables o comunicaciones, interponer recursos, desistir de acciones y renunciar a derechos** debe acreditarse por cualquier medio válido en derecho que deje constancia fidedigna de su existencia.
* **ADVERTENCIA OBLIGATORIA EN TODAS LAS RUTAS — facultades que exigen poder especial.** Antes de continuar, informa en el chat de que el artículo 25.2 de la Ley de Enjuiciamiento Civil exige **poder especial** para la renuncia, la transacción, el desistimiento, el allanamiento, el sometimiento a arbitraje y las manifestaciones que puedan comportar el sobreseimiento del proceso por satisfacción extraprocesal o carencia sobrevenida de objeto, y para ejercitar las facultades que el poderdante hubiera excluido del poder general. Explica la consecuencia práctica: **si el poder no las contiene, el despacho no podrá transigir ni desistir el día de la vista**, que es precisamente el momento en que suelen decidirse los asuntos. Verifica la relación vigente del artículo 25.2 con `web_search` antes de enumerarla.
* **Si `[V3 = persona_juridica]` → Comprobación adicional obligatoria.** El poder debe otorgarlo quien tenga facultades suficientes conforme a los estatutos y a su nombramiento inscrito. Pide los datos del cargo, la fecha del nombramiento y su inscripción, y advierte de que un poder otorgado por quien carece de facultades bastantes es ineficaz y puede provocar la nulidad de las actuaciones. Advierte también de la posible exigencia de **poder mancomunado** cuando la representación orgánica lo sea.
- `V2` no elige plantilla: determina la norma invocada, la exigencia o no de procurador y la forma del apoderamiento propia de ese orden jurisdiccional.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión consolidada vigente de la Ley 1/2000 de Enjuiciamiento Civil —en particular los artículos 23 a 26—, de la Ley 36/2011 y de la Ley 39/2015.
3. Verifica el **trámite y la sede** del apoderamiento electrónico aplicables: registro electrónico de apoderamientos judiciales para el ámbito judicial y registro electrónico de apoderamientos de la administración correspondiente para el administrativo. Sus denominaciones, sedes y requisitos de acceso deben comprobarse, no escribirse de memoria.
4. Comprueba si el ámbito exige **procurador** y, en su caso, informa de que el poder debe otorgarse también a su favor y de que su intervención tiene coste independiente.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Instrumento procedente** y su fundamento, con la forma de otorgamiento y su coste orientativo.
2. **Relación de facultades** que se propone incluir, distinguiendo las ordinarias de las que exigen mención especial.
3. **Advertencia sobre las facultades del artículo 25.2** y sus consecuencias prácticas.
4. **Comprobaciones previas:** título y suficiencia del representante orgánico si el otorgante es persona jurídica, y necesidad de procurador.
5. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
6. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación del origen de la plantilla
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:** accede al adjunto y verifica que identifique correctamente al otorgante y a los apoderados con su número de colegiado, que enumere las facultades, y que contenga o excluya de forma expresa las del artículo 25.2. Advierte de las omisiones.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura (`create_file`):** vuelca íntegramente la plantilla acordada en el workspace con nombre en `snake_case.md`, aplicando **Zero-Omission** y dejando los datos pendientes como marcador con su nombre propio de plantilla.
2. **Validación (`read_file`):** comprueba el volcado íntegro.
3. **Confirmación y encadenamiento:** informa de la ruta absoluta y, en la misma respuesta, abre la primera sección de la Fase 4 con su anuncio y su primera solicitud de datos.

---

## FASE 4 — EDICIÓN INCREMENTAL APARTADO A APARTADO

### Protocolo Obligatorio de Edición
```
[slot_filling_request (grupos) / Chat (facultades)] ──> [Vista previa en texto plano]
      ──> [«¿Confirmamos esta sección?»] ──> [edit_file + read_file]
```

- **Datos estructurados agrupados (`slot_filling_request`, MANDATORIO):** otorgante, representante orgánico y cada apoderado se piden en bloque.
- **Anuncio de sección visible** al pasar de una sección a la siguiente.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a identificar al otorgante y, en su caso, a acreditar el título de su representante."
- Sección 2: "Identificado el otorgante, corresponde identificar a los profesionales que se apoderan."
- Sección 3: "Identificados los apoderados, procede delimitar el ámbito del apoderamiento."
- Sección 4: "Delimitado el ámbito, corresponde relacionar las facultades que se confieren."
- Sección 5: "Por último, procede pronunciarse expresamente sobre las facultades que exigen mención especial y sobre la sustitución y la revocación."

1. **Otorgante [dato objetivo, con validación del título].** Solicita en bloque mediante `slot_filling_request`: nombre o razón social, documento de identidad o CIF, domicilio, estado civil y régimen económico si es relevante para el asunto, y nacionalidad. Si `[V3 = persona_juridica]`, solicita además: denominación completa, datos de constitución e inscripción, nombre y documento del representante orgánico, cargo, fecha de nombramiento, su inscripción registral, y si la representación es solidaria o mancomunada. Advierte de que la suficiencia de facultades la valorará el notario o el letrado de la Administración de Justicia, y de que conviene aportar la documentación acreditativa con antelación.
2. **Apoderados [dato objetivo].** Nombre completo, documento de identidad, **número de colegiado y colegio de adscripción** de cada profesional que se apodera. Pregunta si se apodera también a **procurador** y, en su caso, sus datos. Recomienda apoderar a más de un profesional del despacho para evitar que una baja o una incompatibilidad paralice la actuación.
3. **Ámbito del apoderamiento [negociación].** Pregunta si el poder es para **todos los asuntos** presentes y futuros o **para un asunto concreto**. Si es concreto, identifica órgano, clase de procedimiento, número de autos y objeto. Explica el equilibrio: un poder general ahorra otorgamientos futuros pero confiere una representación amplia; un poder para asunto concreto es más prudente pero obliga a otorgar otro en cada nuevo asunto, con su coste y su demora.
4. **Facultades ordinarias [negociación].** Relaciona las facultades de tramitación: comparecer, formular y contestar demandas y recursos, proponer y practicar prueba, asistir a vistas y comparecencias, solicitar y consentir medidas cautelares, instar y seguir la ejecución, recibir notificaciones, y cuantas actuaciones sean precisas para la tramitación del asunto.
5. **Facultades que exigen mención especial, sustitución y revocación [negociación — el apartado decisivo].**
   - Recorre **una a una** las facultades del artículo 25.2 de la Ley de Enjuiciamiento Civil y pregunta expresamente si el otorgante las concede o las excluye, dejando constancia de la decisión en el documento. Explica antes la consecuencia de cada una: la transacción y el desistimiento son las que se necesitan con más frecuencia y en el momento menos previsible.
   - Añade, si procede, las facultades de **cobro y percepción de cantidades**, con la advertencia de que confieren la disposición de fondos del cliente y de que su régimen de rendición de cuentas debe estar claro.
   - **Sustitución:** pregunta si se autoriza la sustitución del poder a favor de otros profesionales, y con qué límites.
   - **Revocación:** informa de que el poder es revocable en cualquier momento, de que la revocación debe comunicarse al órgano y a los apoderados para ser eficaz frente a ellos, y de que conviene pactar el modo de comunicarla.
   - **Duración:** si el poder es para asunto concreto, su vigencia se agota con él; si es general, conviene valorar la conveniencia de un plazo.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar un apartado existente.
2. Añadir o excluir facultades.
3. Añadir o retirar apoderados.
4. Revisar el ámbito del apoderamiento o su duración.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas de Cierre
- **Carácter DRAFT:** la minuta de poder debe ser revisada y adaptada por el **notario autorizante**, que es quien da forma al instrumento público y valora la capacidad y la suficiencia de facultades. Esta minuta es una propuesta de contenido, no una escritura.
- **Documentación que debe llevarse al otorgamiento:** documento de identidad del otorgante; si es persona jurídica, escritura de constitución y estatutos vigentes, escritura o certificación del nombramiento del cargo con su inscripción, y en su caso certificación registral actualizada.
- **Coste:** el otorgamiento notarial tiene arancel; el apoderamiento apud acta, personal o electrónico, no tiene ese coste. Informar de la alternativa.
- **Aportación al procedimiento:** el poder debe aportarse en la forma que exija el órgano, y la representación acreditarse antes de la primera actuación que la requiera.
- **Facultades del artículo 25.2:** verificar antes de la primera vista que el poder contiene las que puedan necesitarse. Descubrir en la vista que no se puede transigir es un perjuicio real para el cliente.
- **Revocación y cese:** informar al cliente de que puede revocar el poder en cualquier momento, y al despacho de que el cese en la representación debe comunicarse en la forma que proceda.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre en el BOE la versión consolidada vigente de la Ley 1/2000 de Enjuiciamiento Civil, de la Ley 36/2011 y de la Ley 39/2015 antes de redactar, y aplicar la redacción vigente al documento del workspace.
2. **Facultades del artículo 25.2:** advertir siempre, en todas las rutas, de las facultades que exigen poder especial, y pronunciarse expresamente en el documento sobre cada una de ellas. Verificar la relación vigente antes de enumerarla.
3. **Suficiencia de facultades del otorgante:** si el otorgante es persona jurídica, no dar el documento por cerrado sin los datos del cargo, su nombramiento y su inscripción. Un poder otorgado por quien carece de facultades bastantes es ineficaz.
4. **La minuta no es la escritura:** hacer constar siempre que corresponde al notario autorizante la forma del instrumento y la valoración de la capacidad y de la suficiencia de facultades.
5. **Exigencia de procurador:** comprobar si el ámbito la impone y advertir de su coste independiente. No omitir su apoderamiento cuando sea necesario.
6. **Régimen propio del orden social:** no trasladar sin más el esquema civil. En la instancia la representación puede conferirse a abogado, procurador, graduado social colegiado o persona en el pleno ejercicio de sus derechos civiles, y en suplicación y casación la defensa de abogado es preceptiva.
7. **Régimen administrativo:** distinguir los actos de mero trámite, en que la representación se presume, de aquellos en que debe acreditarse por medio que deje constancia fidedigna.
8. **Facultades de cobro:** advertir expresamente de su alcance y del régimen de rendición de cuentas antes de incluirlas.
9. **Cero invención:** no inventar números de colegiado, datos notariales, números de protocolo, datos de inscripción registral, denominaciones de registros electrónicos ni números de autos. Lo no aportado permanece como marcador con su nombre propio de plantilla.
10. **Sintaxis de los marcadores (`{{CLAVE: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real: nunca debe quedar rastro de la anotación en el documento escrito. Los marcadores cuyo dato aún no exista se conservan **íntegros, con su clave y su tipo**, para que el cliente y el profesional que revise vean qué falta y de qué naturaleza es. Está PROHIBIDO sustituir la clave propia del marcador por un literal genérico.
