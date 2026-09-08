---
name: prevencion-blanqueo
description: >
  Genera la documentación de cumplimiento que el despacho debe conservar cuando actúa como sujeto
  obligado por la Ley 10/2010 de prevención del blanqueo de capitales y de la financiación del
  terrorismo: ficha de identificación formal del cliente, declaración de titularidad real, lista de
  comprobación de diligencia debida por expediente, e informe interno de examen especial de una
  operación. Aplica la Ley 10/2010 y su reglamento de desarrollo, en sus versiones consolidadas
  vigentes verificadas en el BOE. Su primera función es de delimitación: determina si la actuación
  concreta entra en el ámbito de sujeción del profesional y si opera la exención legal relativa a la
  información recibida en el marco de la determinación de la posición jurídica del cliente o de su
  defensa o representación. Metodología: clasificación de la actuación y del nivel de riesgo mediante
  formulario interactivo, plan de acción con las medidas exigibles, creación del documento base en el
  workspace y edición incremental apartado a apartado. NO genera la comunicación por indicio al
  órgano competente, que se formaliza en los modelos oficiales por el representante del sujeto
  obligado y exige asesoramiento especializado: ante indicios, esta skill detiene el proceso y deriva.
when_to_use: |
  - El despacho acepta un encargo que entra en el ámbito de la normativa de prevención del blanqueo y debe documentar la identificación del cliente.
  - Hay que recabar y documentar la titularidad real de una persona jurídica cliente.
  - El despacho quiere revisar el cumplimiento de la diligencia debida de un expediente concreto.
  - Ha aparecido una operación que exige examen especial y hay que documentar el análisis interno.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - tipo_documento: ficha de identificación / declaración de titularidad real / lista de comprobación de diligencia debida / informe interno de examen especial
  - actuacion_profesional: descripción de la actuación encargada, a efectos de determinar la sujeción
  - opera_exencion: si la información se recibe en el marco de la determinación de la posición jurídica o de la defensa o representación en un proceso
  - nivel_riesgo: simplificado / normal / reforzado
  - naturaleza_cliente: persona física / persona jurídica / entidad sin personalidad jurídica o estructura análoga
  - datos_cliente: identificación formal completa conforme a documento fehaciente
  - titularidad_real: personas físicas que poseen o controlan la persona jurídica y su porcentaje o medio de control
  - origen_de_fondos: información sobre el origen de los fondos y del patrimonio, cuando resulte exigible
  - proposito_relacion: propósito e índole prevista de la relación de negocios y actividad del cliente
outputs:
  - ficha_identificacion: ficha de identificación formal en markdown, DRAFT, para su conservación en el expediente
  - documentacion_diligencia_debida: declaración de titularidad real, lista de comprobación o informe de examen especial en markdown, DRAFT
references:
  - references/fuentes-y-normativa-blanqueo.md
  - references/sujecion-del-profesional-y-exencion-legal.md
  - references/diligencia-debida-y-titularidad-real.md
  - references/abstencion-comunicacion-y-prohibicion-de-revelacion.md
  - references/conservacion-y-control-interno.md
assets:
  - assets/checklist-diligencia-debida.md
  - assets/template-declaracion-titularidad-real.md
  - assets/template-ficha-identificacion-cliente.md
  - assets/template-informe-examen-especial-interno.md
---

# Generar la Documentación de Diligencia Debida

> DRAFT — para revisión por el profesional responsable o por el responsable de cumplimiento del despacho antes de su uso y conservación. No constituye asesoramiento en materia de cumplimiento normativo ni dictamen vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de documento):** `ficha_identificacion` | `titularidad_real` | `checklist_diligencia` | `examen_especial` | `fuera_de_ambito`.
- **V2 (Sujeción de la actuación):** `sujeta` | `no_sujeta` | `sujeta_con_exencion`. *(Vector determinante: se resuelve antes que ningún otro.)*
- **V3 (Naturaleza del cliente):** `persona_fisica` | `persona_juridica` | `entidad_sin_personalidad`.
- **V4 (Nivel de riesgo):** `simplificado` | `normal` | `reforzado`.
- **V5 (Origen plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

### 1.1 Escucha Activa Previa y Parada de Seguridad

**Antes de cualquier otra cosa, aplica esta parada:** si el usuario describe hechos que sugieren indicios de blanqueo de capitales o de financiación del terrorismo —operaciones sin sentido económico o profesional aparente, fraccionamiento artificioso, uso de efectivo desproporcionado, interposición de estructuras opacas, negativa injustificada a identificar al titular real, o cualquier otra circunstancia que el usuario califique como sospechosa—, **detén la generación de documentos** y aplica el protocolo del punto 1.4.

En otro caso, si el usuario ya ha identificado la actuación, la naturaleza del cliente y el nivel de riesgo, registra los vectores en silencio y pasa a la **Fase 2**.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "actuacion_profesional",
      "rationale": "Resolver V2: la sujeción del profesional no es general, depende de la actuación concreta que se le encarga.",
      "question": "¿Cuál es la actuación profesional encargada?",
      "options": [
        {"id": "operacion_inmobiliaria_o_societaria", "label": "Concepción, realización o asesoramiento de operaciones de compraventa de inmuebles o de entidades, gestión de fondos, valores u otros activos, o creación, funcionamiento o gestión de sociedades, fideicomisos o estructuras análogas"},
        {"id": "actuacion_por_cuenta_en_operacion", "label": "Actuación por cuenta del cliente en una operación financiera o inmobiliaria"},
        {"id": "defensa_o_posicion_juridica", "label": "Determinación de la posición jurídica del cliente, o defensa o representación en un proceso judicial o administrativo, incluido el asesoramiento sobre su incoación o sobre cómo evitarlo"},
        {"id": "otra_actuacion", "label": "Otra actuación profesional distinta de las anteriores"}
      ]
    },
    {
      "id": "naturaleza_cliente",
      "rationale": "Resolver V3: la identificación del titular real solo procede respecto de personas jurídicas y estructuras análogas.",
      "question": "¿Quién es el cliente?",
      "options": [
        {"id": "persona_fisica", "label": "Persona física, actuando por sí misma"},
        {"id": "persona_juridica", "label": "Sociedad, asociación, fundación u otra persona jurídica"},
        {"id": "entidad_sin_personalidad", "label": "Entidad sin personalidad jurídica, patrimonio separado o estructura análoga a un fideicomiso"}
      ]
    },
    {
      "id": "factores_de_riesgo",
      "rationale": "Resolver V4: determina si procede diligencia debida simplificada, normal o reforzada.",
      "question": "¿Concurre alguno de estos factores en el cliente o en la operación?",
      "options": [
        {"id": "reforzado", "label": "Persona con responsabilidad pública, relación a distancia sin presencia física, jurisdicción de riesgo, estructura de titularidad compleja u opaca, o uso significativo de efectivo"},
        {"id": "normal", "label": "Ninguno de los anteriores: cliente y operación ordinarios"},
        {"id": "simplificado", "label": "Cliente o producto de los expresamente contemplados para la aplicación de medidas simplificadas"}
      ]
    }
  ]
}
```

### 1.3 Delimitación de la Sujeción y de la Exención (PRIMERA ACCIÓN SUSTANTIVA)

**Comprobación 1 — ¿Está la actuación sujeta?** La sujeción del abogado, procurador u otro profesional independiente **no es general**: depende de la actuación concreta. El artículo 2.1 de la Ley 10/2010 la delimita por referencia a la participación en la concepción, realización o asesoramiento de determinadas operaciones, o a la actuación por cuenta del cliente en operaciones financieras o inmobiliarias. **Verifica la redacción vigente del precepto con `web_search` antes de pronunciarte sobre la sujeción.**

* **Si la actuación no está comprendida → `[V2 = no_sujeta]`.** Informa de que la actuación queda fuera del ámbito de sujeción y de que, por tanto, no nacen las obligaciones de diligencia debida de esta normativa. Ofrece, no obstante, documentar la identificación del cliente como buena práctica del despacho. **No presentes como obligatorio lo que no lo es.**

**Comprobación 2 — ¿Opera la exención legal?** El artículo 22 de la Ley 10/2010 exime a los abogados de determinadas obligaciones —señaladamente las relativas a la abstención de ejecución, a la comunicación por indicio y a la colaboración— respecto de la información que reciban de o sobre un cliente **en el marco de la determinación de su posición jurídica, o en el desempeño de las funciones de defensa o representación en procesos judiciales o administrativos, incluido el asesoramiento sobre la incoación o la forma de evitar un proceso**, con independencia de si la información se obtuvo antes, durante o después de tales procesos.

* **Si la actuación es de defensa o de determinación de la posición jurídica → `[V2 = sujeta_con_exencion]`.** **Verifica el alcance exacto de la exención en el texto vigente con `web_search` antes de afirmar nada.** El error en este punto tiene consecuencias graves en ambas direcciones: aplicar la exención donde no procede incumple la ley; no aplicarla donde procede vulnera el secreto profesional y el derecho de defensa del cliente. Ante cualquier duda, **deriva al responsable de cumplimiento del despacho o a especialista**, y no redactes comunicación alguna.
* Advierte en todo caso de que la exención no elimina las obligaciones de identificación y de conservación documental, y de que el **deber de secreto profesional** subsiste con arreglo a la legislación vigente.

**Comprobación 3 — Enrutamiento:**
* **Si `[V1 = ficha_identificacion]` → Plantilla: `assets/template-ficha-identificacion-cliente.md`.**
* **Si `[V1 = titularidad_real]` → Plantilla: `assets/template-declaracion-titularidad-real.md`.** Solo procede si `[V3]` no es persona física.
* **Si `[V1 = checklist_diligencia]` → Asset: `assets/checklist-diligencia-debida.md`.**
* **Si `[V1 = examen_especial]` → Plantilla: `assets/template-informe-examen-especial-interno.md`,** con el protocolo del punto 1.4.

### 1.4 Protocolo ante Indicios (PARADA OBLIGATORIA)

Si aparecen indicios de blanqueo de capitales o de financiación del terrorismo:

1. **No redactes ninguna comunicación al órgano competente.** La comunicación por indicio se formaliza en los **modelos oficiales**, la efectúa el **representante del sujeto obligado** ante el organismo competente, y exige asesoramiento especializado. Esta skill no la genera.
2. **Informa de la prohibición de revelación.** El sujeto obligado y sus directivos y empleados **no pueden revelar al cliente ni a terceros** que se ha comunicado o que se está examinando una operación, ni que se ha iniciado o se pueda iniciar un análisis. Adviértelo con claridad: es una prohibición legal con consecuencias sancionadoras, y afecta también a lo que se escriba en documentos que el cliente pueda ver.
3. **Informa del deber de abstención**, en los términos y con las excepciones que la ley establezca, y **verifica su alcance vigente** antes de describirlo.
4. **Deriva** al responsable de cumplimiento del despacho, al órgano de control interno si existe, o a especialista en la materia.
5. **Lo único que puedes generar es el informe interno de examen especial**, documento de uso estrictamente interno, que sirve para documentar el análisis y la decisión adoptada, y que **nunca se entrega al cliente**. Hazlo constar en el propio documento.
6. Recuerda que el examen especial debe **documentarse por escrito** y conservarse, con independencia de cuál sea su conclusión.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión consolidada vigente de la Ley 10/2010 y de su reglamento de desarrollo en el BOE, y en particular: el precepto que delimita la sujeción de los profesionales, el alcance de la exención, el umbral de participación que determina la titularidad real, los supuestos de diligencia simplificada y reforzada, y el plazo de conservación documental.
3. Verifica si existen **guías o comunicados vigentes** del organismo competente o del Consejo General de la Abogacía Española aplicables a la actuación, y las obligaciones específicas del colegio de adscripción.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Conclusión sobre la sujeción** de la actuación y, en su caso, sobre la exención, con el precepto verificado.
2. **Medidas de diligencia debida exigibles** según el nivel de riesgo, enumeradas.
3. **Documentación que hay que recabar del cliente**, con indicación de lo que falta.
4. **Advertencia sobre el momento:** la identificación formal debe practicarse **con carácter previo** al establecimiento de la relación de negocios o a la ejecución de la operación, en los términos que la ley establezca. Verifícalo.
5. **Propuesta de plantilla oficial del sistema.**
6. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación de V5 (Origen Plantilla)
* **Si `[V5 = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[V5 = plantilla_usuario]`:** accede al adjunto y verifica que contenga la identificación formal por documento fehaciente, la titularidad real cuando proceda, el propósito de la relación, la información sobre el origen de los fondos cuando resulte exigible, y la fecha y firma. Advierte de las omisiones y de si el documento contiene información que no deba figurar en un documento accesible al cliente.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura (`create_file`):** vuelca íntegramente la plantilla acordada en el workspace con nombre en `snake_case.md`, aplicando **Zero-Omission** y dejando los datos pendientes como marcador con su nombre propio de plantilla.
2. **Validación (`read_file`):** comprueba el volcado íntegro.
3. **Confirmación y encadenamiento:** informa de la ruta absoluta y, en la misma respuesta, abre la primera sección de la Fase 4 con su anuncio y su primera solicitud de datos.

---

## FASE 4 — EDICIÓN INCREMENTAL APARTADO A APARTADO

### Protocolo Obligatorio de Edición
```
[slot_filling_request (grupos) / Chat (análisis de riesgo)] ──> [Vista previa en texto plano]
      ──> [«¿Confirmamos esta sección?»] ──> [edit_file + read_file]
```

- **Datos estructurados agrupados (`slot_filling_request`, MANDATORIO):** identificación del cliente, del representante y de cada titular real se piden en bloque.
- **Anuncio de sección visible** al pasar de una sección a la siguiente.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a la identificación formal del cliente mediante documento fehaciente."
- Sección 2: "Practicada la identificación formal, corresponde determinar la titularidad real."
- Sección 3: "Determinada la titularidad real, procede documentar el propósito y la índole de la relación."
- Sección 4: "Documentado el propósito, corresponde valorar el nivel de riesgo y las medidas aplicables."
- Sección 5: "Por último, procede fijar el régimen de seguimiento, conservación y responsable del expediente."

1. **Identificación formal [dato objetivo].** Solicita en bloque mediante `slot_filling_request`: nombre completo o denominación social, tipo y número de documento fehaciente de identificación, fecha de validez del documento, nacionalidad, fecha y lugar de nacimiento o de constitución, domicilio, actividad profesional o empresarial, y datos del representante que actúa con su documento y título de representación. **La identificación se practica mediante documento fehaciente**, y debe conservarse copia en los términos que la ley establezca: pide al usuario que confirme que dispone de ella.
2. **Titularidad real [dato objetivo, con validación].** Solo si `[V3]` no es persona física. Solicita la identidad de las personas físicas que en último término posean o controlen la persona jurídica, con su porcentaje de participación o su medio de control, y la estructura de propiedad completa cuando haya niveles intermedios. **Verifica con `web_search` el umbral de participación vigente** que determina la titularidad real antes de aplicarlo. Si no existe persona física que reúna el criterio, se considerarán titulares reales quienes la normativa determine, extremo que también debe verificarse. Advierte de que la negativa del cliente a facilitar la titularidad real, o la imposibilidad de determinarla, tiene consecuencias sobre la posibilidad de establecer la relación.
3. **Propósito e índole de la relación [dato objetivo].** Actividad real del cliente, finalidad de la operación encargada, importe y naturaleza previstos, procedencia y destino de los fondos cuando resulte exigible, y coherencia entre la operación y el perfil del cliente. Explica que este apartado no es burocrático: es el que permite después advertir una operación incoherente con el perfil.
4. **Valoración del riesgo y medidas aplicables [negociación].** Recorre los factores de riesgo y documenta la valoración razonada: cliente, producto o servicio, canal de contratación y ubicación geográfica. Determina el nivel resultante y enumera las medidas aplicables. **Si `[V4 = reforzado]`**, indica las medidas adicionales exigibles —entre ellas, según los casos, la obtención de información adicional sobre el origen de los fondos y del patrimonio, la autorización de un nivel directivo y el seguimiento intensificado— y **verifica su relación vigente** antes de enumerarlas.
5. **Seguimiento, conservación y responsable [dato objetivo].** Periodicidad de la revisión del expediente y de la actualización de los datos; **plazo de conservación** de la documentación, que debes verificar en el texto vigente; soporte y medidas de seguridad de la conservación; y **profesional responsable** del expediente en el despacho. Recuerda que la documentación de diligencia debida se conserva con separación y con acceso restringido, y que su tratamiento está sujeto a la normativa de protección de datos.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar un apartado existente.
2. Completar la estructura de titularidad real o la información sobre el origen de los fondos.
3. Revisar la valoración de riesgo y las medidas aplicables.
4. Generar además la lista de comprobación del expediente.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas de Cierre
- **Carácter DRAFT:** revisión por el profesional responsable o por el responsable de cumplimiento antes de su uso y conservación.
- **Momento de la identificación:** debe practicarse con carácter previo al establecimiento de la relación de negocios o a la ejecución de la operación, en los términos legalmente previstos.
- **Imposibilidad de completar la diligencia debida:** si el cliente no facilita la información exigible, la ley prevé la abstención de establecer la relación o de ejecutar la operación, y en su caso la terminación de la relación. Verificar el régimen vigente y consultar al responsable de cumplimiento.
- **Conservación:** durante el plazo legalmente establecido, con las medidas de seguridad aplicables. Verificar el plazo vigente.
- **Prohibición de revelación:** los documentos de examen especial y las actuaciones de análisis **no se comunican al cliente ni a terceros**.
- **Protección de datos:** la documentación de diligencia debida contiene datos personales y su tratamiento debe reflejarse en el registro de actividades del despacho, con base jurídica en el cumplimiento de una obligación legal. Ofrecer la skill `proteccion-datos-despacho`.
- **Formación y control interno:** las obligaciones de control interno, manual de prevención, designación de representante y formación tienen su propio régimen, con particularidades según el tamaño del sujeto obligado. Verificarlo y consultar a especialista.
- **Este documento no es un dictamen de cumplimiento.** El despacho debe contar con asesoramiento especializado para el diseño de su sistema de prevención.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre en el BOE la versión consolidada vigente de la Ley 10/2010 y de su reglamento antes de redactar, y aplicar la redacción vigente al documento del workspace. **Ningún umbral, plazo ni relación de medidas se escribe de memoria.**
2. **Delimitación de la sujeción antes de todo:** la sujeción del profesional no es general, depende de la actuación concreta. **PROHIBIDO** presentar como obligatorias medidas que no lo son para la actuación de que se trate, y prohibido omitirlas cuando sí lo son.
3. **Exención legal:** verificar su alcance en el texto vigente antes de aplicarla o descartarla. Ante duda, derivar al responsable de cumplimiento o a especialista, y no redactar comunicación alguna.
4. **Ante indicios, parada obligatoria.** Esta skill **no genera la comunicación por indicio** al órgano competente: se formaliza en modelos oficiales, la efectúa el representante del sujeto obligado y exige asesoramiento especializado.
5. **Prohibición de revelación:** advertir siempre de que no puede revelarse al cliente ni a terceros que se ha comunicado o se está examinando una operación. Los documentos internos de examen especial no se entregan al cliente, y así debe constar en ellos.
6. **Secreto profesional:** el deber subsiste con arreglo a la legislación vigente y debe respetarse en la redacción de todos los documentos de esta skill.
7. **Cero invención de identidades y estructuras:** no inventar titulares reales, porcentajes de participación, orígenes de fondos, números de documento ni datos registrales. Lo no aportado permanece como marcador con su nombre propio de plantilla, y se indica al usuario qué documentación debe obtener.
8. **Cero asesoramiento de evasión:** está ESTRICTAMENTE PROHIBIDO sugerir formas de eludir las obligaciones de diligencia debida, de fraccionar operaciones, de opacar la titularidad real o de evitar la sujeción. Si la petición del usuario apunta en esa dirección, rechazarla, explicar la obligación legal y ofrecer el camino de cumplimiento.
9. **No es un dictamen de cumplimiento:** hacer constar siempre que el diseño del sistema de prevención del despacho exige asesoramiento especializado.
10. **Sintaxis de los marcadores (`{{clave: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real: nunca debe quedar rastro de la anotación en el documento escrito. Los marcadores cuyo dato aún no exista se conservan **íntegros, con su clave y su tipo**, para que el cliente y el profesional que revise vean qué falta y de qué naturaleza es. Está PROHIBIDO sustituir la clave propia del marcador por un literal genérico.
