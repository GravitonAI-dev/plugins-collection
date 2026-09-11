---
name: cumplimiento-igualdad-y-acoso
description: >
  Prepara la documentacion de igualdad y prevencion del acoso que la ley exige a una empresa conforme
  a la **Ley Organica 3/2007** para la igualdad efectiva de mujeres y hombres, que obliga a toda
  empresa a adoptar medidas frente al acoso sexual y por razon de sexo y a las de cincuenta o mas
  personas trabajadoras a tener plan de igualdad, y a su desarrollo reglamentario en materia de planes
  de igualdad y de igualdad retributiva, que impone el registro retributivo a todas las empresas y la
  auditoria retributiva a las que tienen plan.


  Genera tres documentos: el protocolo de prevencion y actuacion frente al acoso sexual, por razon de
  sexo y por razon de orientacion e identidad, el plan de igualdad con su diagnostico y su comision
  negociadora, y el registro retributivo con la estructura de la auditoria retributiva.


  Comprueba que obligaciones son exigibles segun la plantilla (el protocolo de acoso y el registro
  retributivo lo son sin umbral; el plan de igualdad y la auditoria retributiva a partir de cincuenta
  personas), articula la negociacion con la representacion legal, advierte del plazo de vigencia y de
  la inscripcion registral del plan, y del deber de actuacion inmediata del empresario ante una
  denuncia.


  NO usar cuando exista un caso de acoso actual o una denuncia ya presentada, que exige actuacion
  inmediata y direccion letrada, ni para expedientes disciplinarios, ni para la defensa ante la
  inspeccion de trabajo o ante una demanda por discriminacion.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Ley Organica 3/2007 para la igualdad efectiva de mujeres y hombres](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6115).
when_to_use: |
  - La empresa no tiene protocolo de acoso y quiere implantarlo.
  - La empresa ha alcanzado cincuenta personas trabajadoras y debe negociar un plan de igualdad.
  - La empresa necesita el registro retributivo o la auditoria retributiva.
  - El usuario pregunta que obligaciones de igualdad tiene segun el tamano de su plantilla.
  - El usuario pregunta como se calcula la brecha salarial y cuando hay que justificarla.
  - El usuario pregunta si debe tener medidas y protocolo frente al acoso de personas LGTBI.
inputs:
  - documento: protocolo de acoso / plan de igualdad / registro retributivo (V1)
  - plantilla: menos de cincuenta personas / cincuenta o mas personas (V2)
  - representacion_legal: con representacion legal / sin representacion legal (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_entidad: razon social, CIF, domicilio, actividad, convenio colectivo aplicable y centros de trabajo
  - datos_plantilla: numero de personas trabajadoras por sexo, grupo profesional, puesto y tipo de contrato
  - representacion: composicion de la representacion legal y sindicatos con legitimacion
  - datos_retributivos: retribuciones por grupo, puesto y sexo, con salario base, complementos y percepciones extrasalariales
  - sistema_valoracion: sistema de valoracion de puestos de trabajo utilizado o previsto
  - responsables_protocolo: personas o comision instructora del protocolo y sus suplentes
  - canales_denuncia: canales de comunicacion de situaciones de acoso y su acceso
  - medidas_prevencion: acciones de formacion, informacion y evaluacion de riesgos psicosociales
  - vigencia_y_seguimiento: vigencia prevista, comision de seguimiento y periodicidad de evaluacion
outputs:
  - protocolo_acoso: protocolo de prevencion y actuacion frente al acoso, DRAFT
  - plan_igualdad: plan de igualdad con diagnostico, medidas e indicadores, DRAFT
  - registro_retributivo: registro retributivo y estructura de la auditoria retributiva, DRAFT
  - checklist_obligaciones: obligaciones exigibles segun plantilla, con plazos, negociacion y registro
references:
  - references/igualdad-plan-protocolo-y-umbrales.md
  - references/registro-y-auditoria-retributiva.md
  - references/estilo-redaccion-cumplimiento.md
assets:
  - assets/template-protocolo-acoso.md
  - assets/template-plan-igualdad.md
  - assets/template-registro-retributivo.md
---

# Igualdad y Prevención del Acoso en la Empresa (Protocolo, Plan y Registro Retributivo)

> DRAFT — para revisión por un abogado o consultor de cumplimiento antes de su aprobación y publicación. No constituye asesoramiento jurídico vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva y rigurosa a través de un procedimiento estructurado en 5 fases secuenciales para preparar la documentación de igualdad y prevención del acoso.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `protocolo_acoso` | `plan_igualdad` | `registro_retributivo` | `caso_acoso_activo`.
- **V2 (Plantilla):** `menos_de_cincuenta` | `cincuenta_o_mas`.
- **V3 (Representación Legal):** `con_representacion` | `sin_representacion`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar qué documento se prepara y qué obligaciones son exigibles.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un consultor de cumplimiento (de usted), confirmando que vais a preparar la documentación de igualdad y prevención del acoso de la empresa.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca qué documento necesita, cuántas personas trabajadoras tiene y si hay representación legal, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), la plantilla (`V2`) o la existencia de representación legal (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar cual de los tres documentos de igualdad se prepara.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "protocolo_acoso", "label": "Protocolo de prevención y actuación frente al acoso"},
        {"id": "plan_igualdad", "label": "Plan de igualdad con su diagnóstico"},
        {"id": "registro_retributivo", "label": "Registro retributivo o auditoría retributiva"},
        {"id": "caso_acoso_activo", "label": "Hay una situación o denuncia de acoso ahora mismo"}
      ]
    },
    {
      "id": "plantilla",
      "rationale": "Resolver V2: el plan de igualdad y la auditoria retributiva se exigen a partir de cincuenta personas trabajadoras.",
      "question": "¿Cuántas personas trabajadoras tiene la empresa, contando todos sus centros de trabajo?",
      "options": [
        {"id": "menos_de_cincuenta", "label": "Menos de cincuenta"},
        {"id": "cincuenta_o_mas", "label": "Cincuenta o más"}
      ]
    },
    {
      "id": "representacion_legal",
      "rationale": "Resolver V3: la negociacion del plan y del protocolo cambia segun exista o no representacion legal.",
      "question": "¿Existe representación legal de las personas trabajadoras (delegados de personal o comité de empresa)?",
      "options": [
        {"id": "con_representacion", "label": "Sí, hay representación legal"},
        {"id": "sin_representacion", "label": "No hay representación legal"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `plantilla`
- `V3` — `representacion_legal`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = caso_acoso_activo`:**
  - **DETENER.** Informar de que ante una situación o denuncia de acoso actual nace el deber de actuación inmediata del empresario: adoptar medidas cautelares de protección de la persona afectada, activar la instrucción con garantías y preservar la prueba, con riesgo de responsabilidad si no se actúa. Derivar a letrado especialista y, en su caso, a la inspección de trabajo o a la vía penal. No crear documento genérico.
- **Si `V1 = protocolo_acoso`:**
  - Plantilla del sistema: `assets/template-protocolo-acoso.md`. Proceder a la **Fase 2**.
- **Si `V1 = plan_igualdad`:**
  - Plantilla del sistema: `assets/template-plan-igualdad.md`. Proceder a la **Fase 2**.
- **Si `V1 = registro_retributivo`:**
  - Plantilla del sistema: `assets/template-registro-retributivo.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina qué obligaciones se declaran exigibles y si procede la auditoría retributiva y las medidas planificadas frente al acoso de personas LGTBI.
- `V3` no elige plantilla: determina cómo se constituye la comisión negociadora y si intervienen los sindicatos más representativos.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `igualdad-plan-protocolo-y-umbrales.md`, `registro-y-auditoria-retributiva.md` y `estilo-redaccion-cumplimiento.md`.
2. Verifica **obligatoriamente** el **convenio colectivo aplicable**, que puede imponer un protocolo propio, un procedimiento concreto o mejoras, y mediante `web_search` el estado del registro de planes de igualdad y de la normativa de igualdad de trato de las personas LGTBI y su reglamento de desarrollo. Aplica la redacción vigente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal, Umbrales y Riesgo:**
   - Explicar con claridad qué obligación depende del tamaño y cuál no: el **protocolo frente al acoso sexual y por razón de sexo** y el **registro retributivo** se exigen a **todas** las empresas, sin umbral; el **plan de igualdad** y la **auditoría retributiva** a partir de **cincuenta** personas trabajadoras.
   - Advertir de que las empresas de más de cincuenta personas trabajadoras deben además contar con medidas planificadas y un protocolo de actuación frente al acoso y la violencia contra las personas LGTBI, conforme a la normativa de igualdad de trato y a su reglamento de desarrollo.
   - Explicar que el plan de igualdad debe **negociarse** con la representación legal, tiene **vigencia máxima de cuatro años** y debe **inscribirse** en el registro de convenios y acuerdos colectivos: sin inscripción no se tiene por cumplida la obligación.
   - Advertir del riesgo: sanción de la inspección de trabajo, pérdida de acceso a contratación pública y subvenciones, e inversión de la carga de la prueba en los litigios por discriminación.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Nombrar por su ruta la plantilla **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
- **Si `origen_plantilla = plantilla_sistema`:** utiliza el asset enrutado y avanza a la **Fase 3**.
- **Si `origen_plantilla = plantilla_usuario`:** toma la plantilla adjunta en `<attached_documents>` o el texto pegado en `<user_message>`, verifica que no exija a la víctima aportar pruebas, que no imponga la confrontación directa con la persona denunciada, que no prevea plazos irrazonables y que no atribuya la instrucción a quien pueda estar implicado, advierte en el chat y propón la redacción válida, y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en el workspace del usuario, con el nombre `protocolo_acoso.md`, `plan_igualdad.md` o `registro_retributivo.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos de la clasificación y de la escucha activa, incluidas la fecha del sistema y las obligaciones exigibles según la plantilla. Todos los datos pendientes permanecen como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves. PROHIBIDO dejar archivos en blanco o con notas resumidas.
2. **Validación de Disco (`read_file`):** ejecuta `read_file` sobre el archivo creado para confirmar su integridad.
3. **Confirmación en Chat:** informa al usuario de la ruta del archivo generado e introduce de inmediato la primera sección de la **Fase 4** sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques. Para cada bloque, ejecuta estrictamente el ciclo interactivo:
```
[Anuncio de la sección + Pregunta] --> [Vista Previa en texto plano] --> [¿Confirmamos esta sección?] --> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Anuncio y Pregunta en Chat:** anuncia la sección sustantiva con una frase breve en registro técnico-normativo (por ejemplo, *"Pasamos ahora al procedimiento de actuación ante una denuncia"*) y, en el mismo mensaje, formula ya la primera pregunta. No pidas permiso para pasar de sección: informa y continúa.
2. **Búsqueda prioritaria, Cero Redundancia y Guardado de Nuevos Clientes (`search_clients` / `get_client` / `save_client` — REG-CLI-01, REG-CLI-02 y REG-CLI-03):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** conforme a `REG-CLI-01`. Si los datos ya constan en el sistema, **queda TERMINANTEMENTE PROHIBIDO volver a pedirlos** (`REG-CLI-02`) y se omite `slot_filling_request`. Si se especifican datos de una persona nueva (por formulario o chat), **pregunta al usuario mediante formulario (`restricted_human_in_the_loop_request`) si desea guardarla como nuevo cliente** (`REG-CLI-03`). En caso afirmativo, invoca `save_client` con los campos disponibles. Luego de esto (o si es negativo), continúa con el flujo normal de redacción y confirmación de la skill.
   - **Datos estructurados no de cliente agrupados (`slot_filling_request`, MANDATORIO):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
3. **Vista Previa (Preview):** muestra el texto redactado en texto plano, sin backticks de código.
4. **Confirmación:** pregunta literalmente: `¿Confirmamos esta sección?`.
5. **Persistencia en Disco:** tras la confirmación, aplica `edit_file` con coincidencia exacta y verifica inmediatamente con `read_file`.
6. **Validación de sentido, no solo de formato:** comprueba que la suma de la plantilla por sexo y grupo coincide con el total declarado, que las obligaciones declaradas se corresponden con el umbral, que la instrucción del protocolo no recae en quien puede estar implicado y que los datos retributivos permiten calcular la brecha. Si los datos aportados no permiten el cálculo, **dilo antes de volcarlos**.

### Hoja de Ruta de Secciones — RAMA PROTOCOLO DE ACOSO:

1. **Entidad, convenio y ámbito** *(confirmación agrupada)*: razón social, CIF, actividad, convenio colectivo aplicable, centros de trabajo y número de personas trabajadoras; ámbito personal del protocolo, incluyendo personal propio, en formación, de empresas contratistas que compartan centro y personal externo.
2. **Declaración de principios y definiciones**: compromiso de tolerancia cero, y definición precisa de acoso sexual, acoso por razón de sexo, acoso discriminatorio y acoso laboral, con ejemplos de conductas, distinguiendo el acoso del conflicto laboral ordinario.
3. **Medidas de prevención**: formación e información, evaluación de los riesgos psicosociales, difusión del protocolo y compromiso de los mandos.
4. **Canales de comunicación y garantías**: canales para comunicar la situación, posibilidad de que la comunicación la formule un tercero, garantía de confidencialidad, prohibición de represalias y protección de la persona denunciante y de los testigos.
5. **Procedimiento de actuación**: comisión o persona instructora con sus suplentes, plazos breves y tasados, procedimiento informal y formal, práctica de actuaciones con audiencia, prohibición de la confrontación directa entre denunciante y denunciado, y medidas cautelares de protección desde la recepción.
6. **Resolución, medidas y seguimiento**: informe de conclusiones, medidas disciplinarias conforme al convenio, medidas de reparación y apoyo a la víctima, cierre del expediente, registro y seguimiento posterior.
7. **Personas LGTBI**: *Condicional `V2 = cincuenta_o_mas`:* incorporación de las medidas planificadas y del protocolo de actuación frente al acoso y la violencia contra las personas LGTBI exigidos por la normativa de igualdad de trato y su reglamento.
8. **Aprobación, negociación y publicación**: forma de negociación o consulta con la representación legal, fecha de aprobación, publicación y difusión, y periodicidad de revisión.

### Hoja de Ruta de Secciones — RAMA PLAN DE IGUALDAD:

1. **Ámbito, partes y comisión negociadora** *(confirmación agrupada)*: identificación de la empresa, centros afectados, convenio aplicable, y composición de la comisión negociadora. *Condicional `V3 = sin_representacion`:* constitución de la comisión con los sindicatos más representativos y los representativos del sector, en los términos reglamentarios.
2. **Diagnóstico de situación**: datos desagregados por sexo de plantilla, ingreso y selección, clasificación profesional, formación, promoción, condiciones de trabajo, ejercicio corresponsable de los derechos de conciliación, infrarrepresentación femenina, retribuciones y prevención del acoso.
3. **Auditoría retributiva**: *Condicional `V2 = cincuenta_o_mas`:* valoración de puestos de trabajo con criterios objetivos, análisis de la brecha por grupos y puestos de igual valor, y justificación o plan de corrección de las diferencias detectadas.
4. **Objetivos y medidas**: objetivos cuantitativos y cualitativos, medidas concretas por materia, con persona responsable, plazo, recursos e indicadores de seguimiento.
5. **Calendario, vigencia y seguimiento**: calendario de implantación, vigencia (máximo cuatro años), comisión de seguimiento, periodicidad de evaluación y régimen de revisión anticipada.
6. **Firma, registro e inscripción**: firma de las partes, procedimiento de inscripción en el registro de convenios y acuerdos colectivos, y advertencia de que sin inscripción la obligación no se tiene por cumplida.

### Hoja de Ruta de Secciones — RAMA REGISTRO RETRIBUTIVO:

1. **Entidad, periodo y ámbito** *(confirmación agrupada)*: identificación de la empresa, periodo de referencia (habitualmente el año natural), centros incluidos y convenio aplicable.
2. **Estructura del registro**: desglose por **grupo profesional, categoría, nivel y puesto**, separando por sexo, y distinguiendo **salario base**, **complementos salariales** y **percepciones extrasalariales**.
3. **Valores estadísticos**: media aritmética y mediana de cada concepto, por sexo y por agrupación, tal como exige la norma.
4. **Cálculo de la brecha y justificación**: diferencia porcentual entre las retribuciones medias de mujeres y hombres, en total y por conceptos. *Condicional brecha relevante:* justificación objetiva y motivada de la diferencia o, en su defecto, plan de corrección.
5. **Acceso y consulta**: derecho de acceso de las personas trabajadoras a través de la representación legal, y régimen de acceso cuando no exista representación.
6. **Auditoría retributiva**: *Condicional `V2 = cincuenta_o_mas`:* remisión al sistema de valoración de puestos y a la auditoría, con su plan de actuación.
7. **Conservación, actualización y protección de datos**: periodicidad de actualización, plazo de conservación y advertencia de que el registro se elabora con datos agregados, sin identificar individualmente a las personas trabajadoras.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
La documentación de igualdad ha sido generada y actualizada en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección (definiciones, procedimiento, medidas o datos).
2. Añadir las medidas y el protocolo frente al acoso y la violencia contra las personas LGTBI.
3. Preparar el documento complementario (protocolo, plan o registro retributivo).
4. Revisar la coherencia global y realizar control de calidad previo a la negociación.
5. Dar la documentación por finalizada y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT:** el documento es un borrador preparatorio; debe ser revisado por un profesional y, cuando la ley lo exige, **negociado** con la representación legal antes de su aprobación.
2. **Obligaciones sin umbral:** el protocolo frente al acoso sexual y por razón de sexo y el registro retributivo son exigibles a **todas** las empresas, con independencia de su tamaño. Es el error más frecuente en pymes.
3. **Negociación e inscripción del plan:** el plan de igualdad se negocia con la representación legal, tiene vigencia máxima de cuatro años y debe inscribirse en el registro de convenios y acuerdos colectivos. Un plan redactado unilateralmente y sin inscribir no cumple.
4. **Deber de actuación inmediata:** ante una comunicación de acoso, la empresa debe actuar sin demora, con medidas cautelares de protección. La pasividad genera responsabilidad propia de la empresa, distinta de la del acosador.
5. **Inversión de la carga de la prueba:** en los litigios por discriminación o acoso, si la persona aporta indicios, corresponde a la empresa acreditar la justificación objetiva y razonable de su actuación. La documentación implantada y aplicada es la prueba principal de la empresa.
6. **Consecuencias añadidas del incumplimiento:** más allá de la sanción, el incumplimiento afecta al acceso a la contratación pública y a subvenciones, y puede determinar la nulidad de decisiones empresariales.
7. **Convenio colectivo:** debe comprobarse siempre, porque puede imponer un protocolo o un procedimiento propio, plazos más breves o mejoras que prevalecen.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias y el convenio aplicable antes de citar umbrales, plazos o contenidos obligatorios. No afirmar que una obligación no aplica sin comprobar la plantilla real de todos los centros.
2. **Cero Invención de Datos:** prohibido inventar composiciones de plantilla, cifras retributivas, brechas, identidades de la comisión o datos del convenio. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **Protección de la víctima como prioridad:** está prohibido redactar procedimientos que exijan a la víctima aportar pruebas, que impongan careos con la persona denunciada, que le exijan mantener el contacto o que subordinen la actuación de la empresa a la presentación de una denuncia formal.
4. **No maquillar el diagnóstico:** está prohibido redactar un diagnóstico o un registro con datos distintos de los reales, o justificar una brecha con motivos que no consten acreditados.
5. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas o del convenio en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
6. **Límites de Alcance:** no instruir casos de acoso, no redactar expedientes disciplinarios, ni preparar la defensa ante la inspección de trabajo o ante demandas por discriminación, que deben derivarse a letrado.
