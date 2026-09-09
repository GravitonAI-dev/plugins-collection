---
name: demanda-social
description: >
  Genera la demanda ante el Juzgado de lo Social en las modalidades procesales de mayor uso: despido
  con pretensión de improcedencia o de nulidad, reclamación de cantidad, impugnación de sanción,
  movilidad geográfica y modificación sustancial de condiciones de trabajo del artículo 138, y tutela
  de derechos fundamentales y libertades públicas. Aplica la **Ley 36/2011 reguladora de la Jurisdicción
  Social**, que regula el proceso ante los juzgados y tribunales del orden social y los requisitos de la demanda, y el **texto refundido de la Ley del Estatuto de los Trabajadores aprobado por Real Decreto
  Legislativo 2/2015**, en sus versiones consolidadas vigentes verificadas en el BOE. Comprueba antes de
  redactar la competencia objetiva y territorial, la postulación, el agotamiento de la vía previa y el
  plazo de caducidad o prescripción restante, y construye la demanda con los requisitos del artículo
  80 y, en el despido, los adicionales del artículo 104. Metodología: clasificación de la modalidad
  procesal mediante formulario interactivo, plan de acción con el cómputo de plazos y el mapa de
  codemandados, creación del documento base en el workspace y edición incremental hecho a hecho. NO
  usar para procesos colectivos, conflicto colectivo, impugnación de convenios, materia electoral,
  despido colectivo ni prestaciones de Seguridad Social, que tienen modalidad y trámites propios.
when_to_use: |
  - El usuario quiere presentar demanda por despido, por cantidades, contra una sanción o contra una modificación de condiciones.
  - El usuario ha celebrado ya el acto de conciliación sin avenencia y quiere continuar en vía judicial.
  - El usuario quiere demandar por vulneración de derechos fundamentales en el ámbito laboral.
  - El usuario pregunta ante qué juzgado debe demandar, con qué plazo y con qué requisitos.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - modalidad_procesal: despido / cantidad / sanción / movilidad y modificación sustancial / tutela de derechos fundamentales
  - calificacion_pretendida: improcedencia o nulidad, solo en despido
  - posicion_usuario: trabajador demandante o empresa demandante
  - responsabilidad: individual o solidaria, con identificación de todas las codemandadas
  - datos_demandante: nombre, DNI o NIE, domicilio, y datos del letrado o graduado social que le representa
  - datos_demandados: razón social, CIF, domicilio social y de centro de trabajo de cada demandada
  - datos_relacion_laboral: antigüedad, categoría, salario, tiempo y forma de pago, lugar y características del trabajo
  - condicion_representativa: si el trabajador ostenta o ha ostentado en el año anterior la condición de representante legal o sindical, y si está afiliado a un sindicato
  - hechos: relato cronológico y numerado de los hechos que fundan la pretensión
  - via_previa: fecha de presentación de la papeleta y del acto de conciliación, con su resultado
  - cantidades: desglose por conceptos y periodos, con su total
  - prueba: documental, testifical, pericial e interrogatorio que se propondrá, y prueba en poder de la contraria
outputs:
  - demanda_social: demanda completa en markdown, DRAFT, con encabezamiento, hechos, fundamentos, otrosíes y súplica
references:
  - references/fuentes-plantillas-validadas.md
  - references/requisitos-de-la-demanda.md
  - references/modalidades-procesales-y-plazos.md
  - references/competencia-postulacion-y-recursos.md
  - references/prueba-y-carga-probatoria.md
assets:
  - assets/template-demanda-despido.md
  - assets/template-demanda-impugnacion-sancion.md
  - assets/template-demanda-modificacion-sustancial.md
  - assets/template-demanda-reclamacion-cantidad.md
  - assets/template-demanda-tutela-derechos-fundamentales.md
---

# Generar la Demanda ante el Juzgado de lo Social

> DRAFT — para revisión por un abogado o graduado social colegiado antes de su firma y presentación. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Modalidad procesal):** `despido` | `cantidad` | `sancion` | `modificacion_art138` | `tutela_derechos_fundamentales` | `fuera_de_alcance`.
- **V2 (Calificación pretendida):** `improcedencia` | `nulidad` | `no_aplica`.
- **V3 (Posición del usuario):** `trabajador_demandante` | `empresa_demandante`.
- **V4 (Régimen de responsabilidad):** `individual` | `solidaria`. *(Determina el mapa de codemandados y la llamada al Fondo de Garantía Salarial.)*
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

### 1.1 Escucha Activa Previa
Si el usuario ya ha identificado inequívocamente la modalidad, la pretensión y las partes, registra los vectores en silencio y pasa a la **Fase 2**. En todo caso, **antes de redactar, ejecuta el control de admisibilidad del punto 1.3**.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "modalidad_procesal",
      "rationale": "Resolver V1: cada modalidad tiene requisitos de demanda, plazo, vía previa y régimen de recursos distintos.",
      "question": "¿Cuál es el objeto de la demanda?",
      "options": [
        {"id": "despido", "label": "Impugnación de un despido o de una extinción por decisión de la empresa"},
        {"id": "cantidad", "label": "Reclamación de cantidades adeudadas"},
        {"id": "sancion", "label": "Impugnación de una sanción disciplinaria"},
        {"id": "modificacion_art138", "label": "Movilidad geográfica o modificación sustancial de condiciones de trabajo"},
        {"id": "tutela_derechos_fundamentales", "label": "Vulneración de derechos fundamentales: discriminación, garantía de indemnidad, acoso, libertad sindical"},
        {"id": "fuera_de_alcance", "label": "Prestaciones de Seguridad Social, conflicto colectivo, despido colectivo, materia electoral u otra"}
      ]
    },
    {
      "id": "calificacion_pretendida",
      "rationale": "Resolver V2: la nulidad exige hechos indiciarios y cambia los efectos de la sentencia y la carga de la prueba.",
      "question": "En caso de despido, ¿qué calificación se pretende?",
      "options": [
        {"id": "improcedencia", "label": "Improcedencia: la causa no existe o no está acreditada, o la carta es defectuosa"},
        {"id": "nulidad", "label": "Nulidad: móvil discriminatorio, represalia, o supuesto objetivo de protección"},
        {"id": "no_aplica", "label": "No se trata de un despido"}
      ]
    },
    {
      "id": "responsabilidad",
      "rationale": "Resolver V4: quien no fue citado en conciliación y no se demanda no podrá ser condenado.",
      "question": "¿Concurre alguna circunstancia que genere responsabilidad de más de una empresa?",
      "options": [
        {"id": "individual", "label": "No: una sola empresa empleadora"},
        {"id": "solidaria", "label": "Sí: empresa de trabajo temporal, contrata o subcontrata, grupo de empresas, sucesión de empresa o cesión ilegal"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `modalidad_procesal`
- `V2` — `calificacion_pretendida`
- `V4` — `responsabilidad`
- `V3` — posición del usuario: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo

### 1.3 Control de Admisibilidad y Enrutamiento (PRIMERA ACCIÓN OBLIGATORIA)

Antes de redactar, resuelve y comunica en el chat estos cinco extremos:

**1. Vía previa.** ¿Exigía el asunto conciliación previa, y se ha celebrado? Si la exigía y no consta el intento, **detén la redacción** y deriva a la skill `conciliacion-previa`: la demanda sin certificación no se admite. Si el asunto está exceptuado del trámite (movilidad, modificación sustancial, vacaciones, tutela de derechos fundamentales, Seguridad Social), hazlo constar expresamente en la demanda con cita del artículo 64 de la Ley 36/2011.

**2. Plazo.** Calcula los días hábiles restantes teniendo en cuenta la suspensión producida por la papeleta y su reanudación, y comunica la **fecha límite**. Si el plazo ha vencido, adviértelo con claridad antes de continuar.

**3. Competencia.** Juzgado de lo Social del **lugar de prestación de los servicios** o del **domicilio del demandado**, a elección del demandante. Explica el criterio y pide al usuario que elija, señalando el partido judicial concreto.

**4. Postulación.** Explica que en la instancia las partes pueden comparecer por sí mismas o conferir su representación a abogado, procurador o graduado social colegiado, y que en los recursos de suplicación y casación la defensa de abogado es preceptiva. Si el trabajador litiga por sí mismo, la demanda debe designar domicilio a efectos de notificaciones.

**5. Codemandados.** Si `[V4 = solidaria]`, enumera con el usuario todas las posibles responsables y **comprueba que todas fueron citadas en conciliación**. Advierte de que quien no fue citado no puede ser demandado sin subsanar el trámite. Valora la llamada al **Fondo de Garantía Salarial** cuando haya indicios de insolvencia o concurso.

**Enrutamiento:**
* **Si `[V1 = fuera_de_alcance]` → Detener.** Explica que la modalidad procesal es distinta y deriva: a `reclamacion-seguridad-social` en materia prestacional, o al profesional competente en procesos colectivos. **No crees documento.**
* **Si `[V1 = despido]` → Plantilla: `assets/template-demanda-despido.md`.** Es la única modalidad con **requisitos adicionales de contenido** (artículo 104 de la Ley 36/2011), que deben cumplirse todos.
* **Si `[V1 = cantidad]` → Plantilla: `assets/template-demanda-reclamacion-cantidad.md`.**
* **Si `[V1 = sancion]` → Plantilla: `assets/template-demanda-impugnacion-sancion.md`.**
* **Si `[V1 = modificacion_art138]` → Plantilla: `assets/template-demanda-modificacion-sustancial.md`.** Recuerda que es proceso urgente y de tramitación preferente, exceptuado de conciliación previa, con plazo de caducidad de veinte días hábiles.
* **Si `[V1 = tutela_derechos_fundamentales]` → Plantilla: `assets/template-demanda-tutela-derechos-fundamentales.md`.** Advierte de que la demanda debe expresar con claridad los **hechos constitutivos de la vulneración** y la cuantía de la indemnización pretendida con las bases de su cálculo, y de que el Ministerio Fiscal será siempre parte.
- `V2` no elige plantilla: determina si la demanda pide la improcedencia o la nulidad, y con ello el bloque de hechos indiciarios, la inversion de la carga de la prueba y los efectos que se solicitan en el suplico.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión consolidada vigente de la Ley 36/2011 y del Estatuto de los Trabajadores en el BOE.
3. Verifica el **calendario laboral** del partido judicial para el cómputo de días hábiles.
4. Si la pretensión depende de doctrina jurisprudencial, verifica su estado actual con `web_search` en el CENDOJ antes de citarla. **No cites sentencias que no hayas verificado en esta sesión.**

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Modalidad procesal y su régimen:** plazo, vía previa, tramitación y recursos.
2. **Juzgado competente** propuesto, con el criterio aplicado.
3. **Cómputo del plazo** con la fecha límite.
4. **Mapa de partes demandadas** y su fundamento de responsabilidad.
5. **Estructura de la demanda** que se va a construir y prueba que conviene ir preparando.
6. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
7. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:** accede al adjunto y verifica los requisitos del artículo 80 y, en despido, los del artículo 104. Advierte de las omisiones —que darían lugar a requerimiento de subsanación en cuatro días— y propón la redacción válida.

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
[slot_filling_request (grupos) / Chat (relato y estrategia)] --> [Vista previa en texto plano]
      --> [«¿Confirmamos esta sección?»] --> [edit_file en el editor]
```

- **Datos estructurados agrupados (`slot_filling_request`, MANDATORIO):** demandante, cada demandada, relación laboral y desglose de cantidades se piden en bloque.
- **Anuncio de sección visible** al pasar de una sección a la siguiente.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a fijar el encabezamiento de la demanda y la identificación del demandante y de las partes demandadas."
- Sección 2: "Identificadas las partes, corresponde consignar los datos de la relación laboral exigidos por la ley procesal."
- Sección 3: "Consignada la relación laboral, procede exponer los hechos de forma numerada y cronológica."
- Sección 4: "Expuestos los hechos, corresponde acreditar el agotamiento de la vía previa y el cumplimiento del plazo."
- Sección 5: "Cumplida la vía previa, procede desarrollar los fundamentos de derecho."
- Sección 6: "Desarrollados los fundamentos, corresponde proponer la prueba mediante los otrosíes."
- Sección 7: "Por último, procede formular la súplica con las pretensiones concretas."

1. **Encabezamiento y partes [dato objetivo].** Solicita en bloque mediante `slot_filling_request`: órgano al que se dirige, con el partido judicial elegido; del demandante, nombre, DNI o NIE, domicilio y, en su caso, letrado o graduado social con su número de colegiado y domicilio a efectos de notificaciones; de **cada** demandada, razón social, CIF, domicilio social y de centro de trabajo. Si `[V4 = solidaria]`, incluye a todas y consigna en el propio encabezamiento el título de responsabilidad de cada una.
2. **Datos de la relación laboral [dato objetivo, requisito de admisión en despido].** En la modalidad de despido son **requisitos adicionales de la demanda** (artículo 104 de la Ley 36/2011) y deben constar todos: antigüedad, categoría profesional, salario, tiempo y forma de pago, lugar de trabajo, características particulares del trabajo, fecha de efectividad del despido, forma en que se produjo, hechos alegados por el empresario en la carta, si el trabajador ostenta o ha ostentado en el año anterior la condición de representante legal o sindical, y si está afiliado a un sindicato en el caso de que se alegue la improcedencia por no haberse dado audiencia previa a los delegados sindicales. Recórrelos uno a uno y no des por cerrada la sección hasta tenerlos todos.
3. **Hechos [negociación — el núcleo del escrito].** Construye el relato **numerado y cronológico**, un hecho por ordinal, con fecha, sujeto y conducta. Reglas de redacción que debes aplicar y explicar:
   - Cada hecho debe ser susceptible de prueba y estar respaldado por un documento, un testigo o una pericial que se propondrá después.
   - En despido, transcribe o resume con fidelidad **los hechos imputados en la carta**: la empresa no podrá alegar otros, y el proceso se librará sobre ellos.
   - Si se pretende la **nulidad**, los hechos deben construir el **panorama indiciario**: el ejercicio previo de un derecho o la situación protegida, el conocimiento por la empresa, la proximidad temporal con la medida, y cualquier trato diferenciado. Sin indicios no se desplaza la carga de la prueba.
   - Separa los hechos de las valoraciones: las valoraciones van a los fundamentos.
   - No incluyas hechos que no puedas probar: cada hecho no acreditado resta credibilidad al conjunto.
4. **Vía previa y plazo [dato objetivo].** Consigna la fecha de presentación de la papeleta, la del acto de conciliación y su resultado, con la certificación que se acompaña. Si el asunto está exceptuado, hazlo constar con cita del artículo 64. Deja expresado el cómputo del plazo y su cumplimiento.
5. **Fundamentos de derecho [negociación].** Estructura en cuatro bloques: competencia y procedimiento; legitimación de las partes, con el fundamento de la responsabilidad solidaria si la hay; fondo del asunto, con los preceptos aplicables; y costas e intereses. **Cita solo normas verificadas**; si invocas jurisprudencia, verifícala en esta misma sesión con `web_search` en el CENDOJ y cítala con su órgano, fecha y número de recurso. Si no la puedes verificar, no la cites.
6. **Otrosíes y prueba [negociación].** Propón mediante otrosíes: documental que se acompaña; documental en poder de la contraria, con **requerimiento expreso** de aportación —nóminas, registros de jornada, contratos, expediente personal, correos—; interrogatorio del representante legal de la demandada; testifical con identificación de los testigos y solicitud de citación judicial si procede; y pericial si es necesaria. Advierte de que el **registro de jornada** es la prueba decisiva en las reclamaciones de horas extraordinarias y de que su ausencia perjudica a la empresa. Añade los otrosíes de designación de domicilio a efectos de notificaciones y, si procede, de solicitud de beneficio de justicia gratuita.
7. **Súplica [negociación].** Formula las pretensiones con precisión y en el orden correcto: la principal, las subsidiarias y las accesorias. En despido: nulidad con readmisión y salarios de tramitación como principal si se sostiene, improcedencia con sus efectos como subsidiaria, y las cantidades adeudadas. En cantidad: condena al principal más el interés por mora del artículo 29.3 del Estatuto de los Trabajadores. En sanción: revocación con reposición de derechos y reintegro de lo descontado. En tutela: declaración de la vulneración, cese inmediato, reposición y la **indemnización por daños con sus bases de cálculo**, que debe expresarse en la demanda.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar un apartado existente.
2. Ampliar el relato de hechos o el panorama indiciario.
3. Añadir codemandados, prueba u otrosíes.
4. Revisar la súplica y el orden de las pretensiones.
5. Dar la demanda por finalizada y cerrar la sesión.
```

### Advertencias Legales Preceptivas de Cierre
- **Carácter DRAFT:** revisión por abogado o graduado social colegiado antes de su firma y presentación.
- **Documentos que deben acompañarse:** certificación del acto de conciliación o de su intento, o justificación de estar exceptuado; carta de despido o de sanción; contrato y nóminas; poder o designación de representación; y copia de la demanda y de los documentos para cada demandada.
- **Presentación:** verificar la vía de presentación aplicable —sede judicial electrónica o registro— y conservar el justificante con su fecha, que acredita el cumplimiento del plazo.
- **Subsanación:** si la demanda adolece de defectos u omisiones, el letrado de la Administración de Justicia advertirá a la parte para que los subsane en el plazo legalmente previsto, con archivo si no se subsanan. Revisar los requisitos antes de presentar evita ese trance con el plazo consumido.
- **Justicia gratuita:** las personas trabajadoras y las beneficiarias de la Seguridad Social tienen reconocido el derecho a la asistencia jurídica gratuita en el orden social en los términos legalmente previstos. Verificar el alcance vigente antes de informar.
- **Recursos:** advertir de que no toda sentencia es recurrible en suplicación, señaladamente por razón de la cuantía o en impugnación de sanciones que no sean muy graves. Verificar el régimen vigente del artículo 191 antes de informar.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre en el BOE la versión consolidada vigente de la Ley 36/2011 y del Estatuto de los Trabajadores antes de redactar, y aplicar la redacción vigente al documento del workspace.
2. **Control de admisibilidad antes de redactar:** vía previa, plazo, competencia, postulación y codemandados. Redactar una demanda inadmisible con el plazo corriendo es el peor resultado posible.
3. **Requisitos del artículo 80 y, en despido, del artículo 104:** deben cumplirse todos. No dar la demanda por cerrada con un requisito pendiente; los datos que falten permanecen como marcador visible.
4. **Congruencia con la papeleta:** la demanda debe ser sustancialmente coincidente con la conciliación previa. No introducir pretensiones ni fundamentos fácticos esencialmente nuevos.
5. **Hechos probables:** no consignar hechos que el cliente no pueda acreditar. Cada hecho debe tener su medio de prueba propuesto en los otrosíes.
6. **Nulidad e indicios:** no formular pretensión de nulidad sin un panorama indiciario construido con hechos concretos. Una nulidad alegada sin indicios debilita la demanda y no desplaza la carga de la prueba.
7. **Cita de jurisprudencia:** prohibido citar sentencias, doctrina o números de recurso que no se hayan verificado en esta misma sesión mediante `web_search` en una fuente oficial. Ante la duda, no citar.
8. **Cero invención:** no inventar hechos, fechas, importes, juzgados, números de expediente ni nombres de testigos. Los datos no aportados permanecen como marcador con su nombre propio de plantilla.
9. **Cuantía y recursos:** no afirmar que una sentencia será o no recurrible sin verificar el umbral y las exclusiones vigentes del artículo 191.
10. **Sintaxis de los marcadores (`{{CLAVE: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real: nunca debe quedar rastro de la anotación en el documento escrito. Los marcadores cuyo dato aún no exista se conservan **íntegros, con su clave y su tipo**, para que el cliente y el profesional que revise vean qué falta y de qué naturaleza es. Está PROHIBIDO sustituir la clave propia del marcador por un literal genérico.
