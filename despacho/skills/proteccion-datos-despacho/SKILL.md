---
name: proteccion-datos-despacho
description: >
  Genera el paquete de cumplimiento en protección de datos que el propio despacho profesional necesita:
  registro de actividades de tratamiento, contrato de encargado de tratamiento con proveedores o con
  clientes, cláusula informativa para clientes y para terceros afectados, compromiso de
  confidencialidad del personal y colaboradores, y registro de brechas de seguridad con su análisis de
  riesgo. Aplica el **Reglamento (UE) 2016/679**, norma europea de protección de datos de aplicación directa, y la **Ley Orgánica 3/2018 de Protección de Datos
  Personales y garantía de los derechos digitales**, que la adapta y completa en el ordenamiento español, en sus versiones consolidadas vigentes verificadas
  en el BOE y en el Diario Oficial de la Unión Europea. Atiende a las dos particularidades del
  despacho como responsable: el **secreto profesional**, que modula el ejercicio de los derechos de
  los interesados y el acceso de terceros, y el tratamiento habitual de **categorías especiales de
  datos** y de datos relativos a condenas e infracciones penales que los asuntos comportan.
  Metodología: clasificación del documento y del rol del despacho mediante formulario interactivo,
  plan de acción con la identificación de bases jurídicas, creación del documento base en el workspace
  y edición incremental apartado a apartado. NO diseña el sistema de cumplimiento completo del
  despacho ni sustituye la evaluación de impacto ni el asesoramiento de un delegado de protección de
  datos.
when_to_use: |
  - El despacho necesita elaborar o actualizar su registro de actividades de tratamiento.
  - Hay que formalizar un contrato de encargado de tratamiento con un proveedor o con un cliente.
  - Hay que redactar la cláusula informativa para clientes o para terceros cuyos datos se tratan en un asunto.
  - Se ha producido una brecha de seguridad y hay que documentarla y valorar su notificación.
  - Hay que formalizar el compromiso de confidencialidad del personal o de un colaborador externo.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - tipo_documento: registro de actividades / contrato de encargado / cláusula informativa / compromiso de confidencialidad / registro de brecha
  - rol_despacho: responsable del tratamiento / encargado del tratamiento por cuenta de un cliente
  - datos_despacho: denominación, NIF, domicilio, contacto de protección de datos y, si existe, delegado de protección de datos
  - actividades_tratamiento: relación de tratamientos, con su finalidad, base jurídica, categorías de datos e interesados
  - destinatarios_y_encargados: proveedores, colaboradores y terceros a los que se comunican o ceden datos
  - transferencias_internacionales: existencia, destino y garantías aplicables
  - medidas_seguridad: medidas técnicas y organizativas implantadas
  - datos_brecha: naturaleza, momento de detección, datos e interesados afectados, causa y medidas adoptadas
outputs:
  - documento_cumplimiento: registro de actividades, contrato de encargado, cláusula informativa, compromiso de confidencialidad o registro de brecha, en markdown, DRAFT
references:
  - references/fuentes-y-normativa-proteccion-datos.md
  - references/rol-del-despacho-responsable-o-encargado.md
  - references/registro-de-actividades-y-bases-juridicas.md
  - references/secreto-profesional-y-derechos-de-los-interesados.md
  - references/brechas-de-seguridad-y-notificacion.md
assets:
  - assets/template-clausula-informativa-clientes.md
  - assets/template-compromiso-confidencialidad-personal.md
  - assets/template-contrato-encargado-tratamiento.md
  - assets/template-registro-actividades-tratamiento.md
  - assets/template-registro-brechas-seguridad.md
---

# Generar la Documentación de Protección de Datos del Despacho

> DRAFT — para revisión por el profesional responsable o por el delegado de protección de datos antes de su uso. No constituye dictamen de cumplimiento ni sustituye la evaluación de impacto cuando resulte exigible.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de documento):** `registro_actividades` | `contrato_encargado` | `clausula_informativa` | `compromiso_confidencialidad` | `registro_brecha`.
- **V2 (Rol del despacho):** `responsable` | `encargado`. *(Determina las obligaciones y el contenido del documento.)*
- **V3 (Colectivo de interesados):** `clientes` | `terceros_del_asunto` | `personal` | `proveedores`.
- **V4 (Urgencia):** `ordinaria` | `brecha_en_curso`. *(La brecha activa un protocolo con plazos de horas.)*
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

### 1.1 Escucha Activa Previa y Parada por Urgencia

**Antes de cualquier otra cosa:** si el usuario describe una **brecha de seguridad en curso** —acceso no autorizado, pérdida o robo de dispositivos o documentación, envío de información a destinatario equivocado, cifrado por programa malicioso, publicación indebida—, aplica el protocolo del punto 1.4 **de inmediato**: la notificación a la autoridad de control tiene un plazo contado en horas, y lo primero es el reloj.

En otro caso, si el usuario ya ha identificado el documento, el rol del despacho y el colectivo afectado, registra los vectores en silencio y pasa a la **Fase 2**.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "tipo_documento",
      "rationale": "Resolver V1: cada documento cumple una obligación distinta del Reglamento.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "registro_actividades", "label": "Registro de actividades de tratamiento del despacho"},
        {"id": "contrato_encargado", "label": "Contrato de encargado de tratamiento con un proveedor o con un cliente"},
        {"id": "clausula_informativa", "label": "Cláusula informativa para clientes o para terceros del asunto"},
        {"id": "compromiso_confidencialidad", "label": "Compromiso de confidencialidad del personal o de un colaborador externo"},
        {"id": "registro_brecha", "label": "Registro y análisis de una brecha de seguridad"}
      ]
    },
    {
      "id": "rol_despacho",
      "rationale": "Resolver V2: el despacho es normalmente responsable del tratamiento, pero en determinados encargos actúa como encargado por cuenta del cliente, y las obligaciones cambian.",
      "question": "¿En qué posición actúa el despacho respecto de los datos de que se trata?",
      "options": [
        {"id": "responsable", "label": "Decide las finalidades y los medios del tratamiento: datos de sus clientes, de los asuntos y de su personal"},
        {"id": "encargado", "label": "Trata datos por cuenta y siguiendo instrucciones de un cliente, para una finalidad que este determina"},
        {"id": "no_claro", "label": "No está claro y hay que determinarlo"}
      ]
    },
    {
      "id": "colectivo_interesados",
      "rationale": "Resolver V3: la base jurídica y el deber de información difieren según el colectivo, y en los terceros del asunto la información puede modularse.",
      "question": "¿De quién son los datos que se tratan?",
      "options": [
        {"id": "clientes", "label": "Clientes del despacho y sus representantes"},
        {"id": "terceros_del_asunto", "label": "Contrapartes, testigos, familiares y otros terceros cuyos datos aparecen en los asuntos"},
        {"id": "personal", "label": "Personal del despacho, colaboradores y candidatos"},
        {"id": "proveedores", "label": "Proveedores y prestadores de servicios"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `tipo_documento`
- `V2` — `rol_despacho`
- `V3` — `colectivo_interesados`
- `V4` — urgencia: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo

### 1.3 Determinación del Rol y Enrutamiento

**Comprobación 1 — Resuelve el rol si no está claro.** El despacho es **responsable** cuando decide las finalidades y los medios del tratamiento: los datos de sus clientes, los de los asuntos que dirige, los de su personal. Es **encargado** cuando trata datos por cuenta de un cliente y siguiendo sus instrucciones, para una finalidad que el cliente determina: por ejemplo, cuando gestiona en su nombre un canal de comunicaciones internas, administra una base de datos del cliente o presta un servicio externalizado de gestión.

Advierte de que la calificación **no la elige el despacho**: depende de quién decide sobre el tratamiento, y determinarla mal invalida todo el documento. En la dirección técnica de un asunto, el despacho actúa como responsable respecto de los datos que trata para desempeñarla, aunque los datos procedan del cliente.

**Comprobación 2 — Enrutamiento:**
* **Si `[V1 = registro_actividades]` → Plantilla: `assets/template-registro-actividades-tratamiento.md`.** Advierte de que el despacho debe llevar registro de actividades: aunque el Reglamento exime a determinadas organizaciones por su tamaño, la excepción no alcanza a quien trata datos de forma no ocasional o trata categorías especiales de datos, circunstancias que concurren de ordinario en un despacho. **Verifica el alcance de la excepción en el texto vigente.**
* **Si `[V1 = contrato_encargado]` → Plantilla: `assets/template-contrato-encargado-tratamiento.md`.** Pregunta en qué posición está el despacho: si contrata a un proveedor que accederá a datos, el despacho es responsable y el proveedor encargado; si el despacho presta el servicio, es encargado y el cliente responsable. El documento cambia de dirección.
* **Si `[V1 = clausula_informativa]` → Plantilla: `assets/template-clausula-informativa-clientes.md`.** Si `[V3 = terceros_del_asunto]`, advierte de que el deber de información respecto de datos no obtenidos del propio interesado tiene un régimen y unas excepciones propias, y de que su cumplimiento puede modularse cuando comprometería el secreto profesional o la finalidad del asunto. **Verifica el régimen y las excepciones aplicables antes de concluir.**
* **Si `[V1 = compromiso_confidencialidad]` → Plantilla: `assets/template-compromiso-confidencialidad-personal.md`.**
* **Si `[V1 = registro_brecha]` → Plantilla: `assets/template-registro-brechas-seguridad.md`,** con el protocolo del punto 1.4.

**Comprobación 3 — Advertencia transversal sobre categorías especiales.** En un despacho, el tratamiento de **categorías especiales de datos** —salud, afiliación sindical, convicciones, orientación sexual, datos biométricos— y de **datos relativos a condenas e infracciones penales** no es excepcional: es cotidiano. Advierte de que estos tratamientos exigen una base jurídica reforzada y medidas de seguridad acordes, y **verifica con `web_search` los preceptos aplicables** —tanto del Reglamento como de la Ley Orgánica 3/2018, que contiene una previsión específica sobre el tratamiento por abogados y procuradores de datos relativos a condenas e infracciones penales— antes de consignar una base jurídica en el documento.
- `V2` no elige plantilla: determina si el despacho figura como responsable o como encargado del tratamiento, y con ello las obligaciones que se recogen en el documento.

### 1.4 Protocolo ante Brecha de Seguridad (PARADA POR URGENCIA)

Si hay una brecha en curso, y **antes de redactar nada**:

1. **Informa del plazo.** La notificación a la autoridad de control debe realizarse **sin dilación indebida** y, cuando sea posible, dentro del plazo máximo que el Reglamento establece desde que se tuvo constancia de la brecha, plazo contado en **horas**. **Verifícalo con `web_search`** y comunica la fecha y hora límite calculadas.
2. **Indica las acciones inmediatas**, por orden: contener la brecha; preservar las evidencias y los registros técnicos; identificar qué datos y qué interesados están afectados; y valorar el riesgo para sus derechos y libertades.
3. **Explica el doble umbral:** la notificación a la autoridad procede salvo que sea improbable que la brecha suponga un riesgo para los derechos y libertades; la comunicación a los interesados procede cuando el riesgo sea **alto**. Son dos decisiones distintas con umbrales distintos.
4. **Advierte de que toda brecha se documenta**, se notifique o no. El registro interno es obligatorio y es lo que acredita la diligencia del despacho.
5. **Advierte de la dimensión de secreto profesional:** una brecha en un despacho afecta con frecuencia a información amparada por el secreto, lo que agrava el riesgo para los interesados y puede tener consecuencias deontológicas propias. Recomienda valorar la comunicación al colegio de adscripción y a la aseguradora de responsabilidad civil.
6. **Deriva** al delegado de protección de datos si existe, o a especialista, para la decisión sobre la notificación.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión vigente del Reglamento (UE) 2016/679 y de la Ley Orgánica 3/2018, y en particular: el contenido mínimo del registro de actividades, el contenido mínimo del contrato de encargado, el contenido del deber de información, el plazo de notificación de brechas, los supuestos de designación obligatoria de delegado de protección de datos y los de evaluación de impacto.
3. Verifica si existen **guías vigentes de la autoridad de control** aplicables, y si el colegio de adscripción ha dictado criterios propios.
4. Verifica los preceptos aplicables al tratamiento de **categorías especiales** y de **datos relativos a condenas e infracciones penales** por abogados y procuradores.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Rol del despacho** determinado y razonado.
2. **Obligación que el documento cumple** y su fundamento.
3. **Bases jurídicas** que se van a emplear para cada finalidad, y advertencia sobre las categorías especiales.
4. **Interacción con el secreto profesional**, cuando el documento la tenga.
5. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
6. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:** accede al adjunto y aplica el **guardrail de defectos frecuentes**: consentimiento invocado como base jurídica donde la base real es el contrato o la obligación legal; ausencia de plazos de conservación concretos; contrato de encargado sin el contenido mínimo exigido; cláusula informativa que remite a un documento inexistente; ausencia de mención de las transferencias internacionales cuando los proveedores están fuera del Espacio Económico Europeo; y omisión del tratamiento de categorías especiales. Advierte de cada defecto y propón la redacción válida.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura (`create_file`):** vuelca íntegramente la plantilla acordada en el workspace con nombre en `snake_case.md`, aplicando **Zero-Omission** y dejando los datos pendientes como marcador con su nombre propio de plantilla.
2. **Validación (`read_file`):** comprueba el volcado íntegro.
3. **Confirmación y encadenamiento:** informa de la ruta absoluta y, en la misma respuesta, abre la primera sección de la Fase 4 con su anuncio y su primera solicitud de datos.

---

## FASE 4 — EDICIÓN INCREMENTAL APARTADO A APARTADO

### Protocolo Obligatorio de Edición
```
[slot_filling_request (grupos) / Chat (bases jurídicas y riesgo)] --> [Vista previa en texto plano]
      --> [«¿Confirmamos esta sección?»] --> [edit_file + read_file]
```

- **Datos estructurados agrupados (`slot_filling_request`, MANDATORIO):** datos del despacho, del proveedor o cliente, y de cada actividad de tratamiento se piden en bloque.
- **Anuncio de sección visible** al pasar de una sección a la siguiente.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a identificar al despacho como responsable del tratamiento y su punto de contacto."
- Sección 2: "Identificado el responsable, corresponde inventariar las actividades de tratamiento."
- Sección 3: "Inventariadas las actividades, procede asignar a cada una su base jurídica y su plazo de conservación."
- Sección 4: "Asignadas las bases jurídicas, corresponde relacionar los destinatarios, encargados y transferencias internacionales."
- Sección 5: "Relacionados los destinatarios, procede documentar las medidas técnicas y organizativas de seguridad."
- Sección 6: "Por último, procede fijar el régimen de derechos de los interesados y su interacción con el secreto profesional."

1. **Responsable y contacto [dato objetivo].** Solicita en bloque mediante `slot_filling_request`: denominación, NIF, domicilio, dirección de contacto en materia de protección de datos, y si existe delegado de protección de datos, sus datos y la comunicación de su designación a la autoridad de control. Si no existe, valora con el usuario si concurre algún supuesto de designación obligatoria y **verifícalo en el texto vigente**.
2. **Inventario de actividades [negociación — el trabajo real].** Recorre con el usuario las actividades típicas de un despacho y no des por cerrada ninguna sin su finalidad y sus interesados: gestión de clientes y facturación; dirección y tramitación de asuntos, incluidos los datos de terceros que los asuntos comportan; gestión de recursos humanos y nóminas; selección de personal; diligencia debida en prevención del blanqueo, como actividad **diferenciada**; videovigilancia, si existe; control de accesos; gestión de proveedores; comunicaciones comerciales y boletines; sitio web, formularios y cookies; y archivo y custodia documental. Advierte de que el registro incompleto es el defecto más frecuente, y de que la actividad de diligencia debida no puede confundirse con la gestión ordinaria de clientes porque su base jurídica, su finalidad y su plazo son distintos.
3. **Bases jurídicas y conservación [negociación — donde se cometen los errores].** Para cada actividad, asigna base jurídica y plazo. Explica la regla que evita el error más común: **el consentimiento no es la base por defecto**. La relación con el cliente se funda en la **ejecución del contrato** y en el **cumplimiento de obligaciones legales**; los datos de terceros del asunto, en el **interés legítimo** o en el cumplimiento de una obligación legal según el caso; el personal, en el contrato y la obligación legal; la diligencia debida, en la **obligación legal**. El consentimiento queda para lo que es realmente voluntario, señaladamente las comunicaciones comerciales. Y advierte: si la base es el contrato o la ley, **pedir consentimiento es un error** que confunde al interesado y permite que lo retire para algo que no depende de su voluntad. Fija plazos de conservación **concretos**, con su fundamento, y menciona el bloqueo de los datos cuando la normativa lo prevea.
4. **Destinatarios, encargados y transferencias [dato objetivo].** Relaciona destinatarios de cesiones y comunicaciones —órganos judiciales, administraciones, contrapartes en lo que el asunto exija, colegio profesional, aseguradora— y encargados de tratamiento: asesoría, informática, servicios en la nube, gestión documental, destrucción de documentación, servicio de correo electrónico. Pregunta expresamente por **transferencias internacionales**: si algún proveedor está fuera del Espacio Económico Europeo, identifica el destino y la garantía aplicable, y **verifica el régimen y las garantías vigentes** antes de consignarlas. Advierte de que un servicio en la nube de proveedor no europeo es una transferencia internacional aunque el despacho no lo perciba así.
5. **Medidas de seguridad [negociación].** Documenta las medidas técnicas y organizativas realmente implantadas, no las deseables: control de acceso a la información con perfiles; cifrado de dispositivos portátiles y de copias de seguridad; copias de seguridad con verificación periódica de su restauración; política de contraseñas y doble factor; actualización de sistemas; gestión de dispositivos personales; destrucción segura de documentación en papel; armarios y archivos con cierre; control de visitas; formación del personal; y procedimiento de gestión de brechas. Advierte de que consignar medidas que no existen empeora la posición del despacho ante una brecha.
6. **Derechos de los interesados y secreto profesional [negociación — la particularidad del despacho].** Fija el procedimiento de atención de los derechos de acceso, rectificación, supresión, limitación, oposición y portabilidad: canal, plazo de respuesta y verificación de la identidad del solicitante. Y aborda la particularidad: cuando el solicitante es la **contraparte** de un asunto y pide acceso a los datos que el despacho trata sobre ella, el **secreto profesional** y el derecho de defensa del cliente modulan la respuesta. **Verifica con `web_search` el régimen aplicable y las limitaciones previstas** antes de fijar el criterio, y advierte de que estas solicitudes no se contestan de forma automática ni se ignoran: se analizan y se responden motivadamente, con asesoramiento si es preciso.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar un apartado existente.
2. Añadir una actividad de tratamiento no inventariada.
3. Revisar las bases jurídicas o los plazos de conservación.
4. Completar los encargados de tratamiento o las transferencias internacionales.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas de Cierre
- **Carácter DRAFT:** revisión por el profesional responsable o por el delegado de protección de datos antes de su uso.
- **El registro de actividades es un documento vivo:** debe actualizarse cuando cambien las actividades, los proveedores o los plazos. Fijar una revisión periódica.
- **Contratos de encargado con todos los proveedores** que accedan a datos: es la omisión que la autoridad de control detecta con más facilidad, y afecta también a proveedores que el despacho no percibe como tales, como el servicio de correo electrónico o el de destrucción de papel.
- **Evaluación de impacto:** verificar si alguna actividad la exige, señaladamente por el tratamiento a gran escala de categorías especiales de datos. Si procede, requiere trabajo específico que esta skill no realiza.
- **Delegado de protección de datos:** verificar si concurre algún supuesto de designación obligatoria. Si se designa, debe comunicarse a la autoridad de control.
- **Formación del personal** y constancia documental de su realización.
- **Secreto profesional:** el deber es propio y anterior, y no queda absorbido por la normativa de protección de datos. Los dos regímenes conviven y el más protector prevalece.
- **Este documento no es un dictamen de cumplimiento.** El diseño del sistema completo del despacho exige asesoramiento especializado.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre la versión vigente del Reglamento (UE) 2016/679 y de la Ley Orgánica 3/2018 antes de redactar, y aplicar la redacción vigente al documento del workspace. **Ningún plazo, contenido mínimo ni supuesto de obligación se escribe de memoria.**
2. **Determinación correcta del rol:** responsable o encargado no es una elección del despacho, depende de quién decide sobre el tratamiento. Determinarlo mal invalida el documento entero.
3. **El consentimiento no es la base jurídica por defecto:** está PROHIBIDO invocarlo donde la base real es la ejecución del contrato, el cumplimiento de una obligación legal o el interés legítimo. Es el error más frecuente y el más perjudicial, porque permite al interesado retirar un consentimiento del que el tratamiento no dependía.
4. **Plazos de conservación concretos:** no admitir formulaciones como "el tiempo necesario". Cada actividad lleva su plazo con su fundamento.
5. **Categorías especiales y datos penales:** advertir siempre de su presencia en la actividad del despacho y verificar los preceptos aplicables, incluida la previsión específica de la Ley Orgánica 3/2018 sobre el tratamiento por abogados y procuradores de datos relativos a condenas e infracciones penales.
6. **Contenido mínimo del contrato de encargado:** verificar el listado vigente y no dar el contrato por cerrado sin cumplirlo íntegramente.
7. **Transferencias internacionales:** preguntar siempre por ellas, y verificar el régimen y las garantías vigentes antes de consignarlas. Un servicio en la nube de proveedor no europeo es una transferencia internacional.
8. **Brechas de seguridad:** el plazo se cuenta en horas. Comunicar la fecha y hora límite, distinguir el umbral de notificación a la autoridad del de comunicación a los interesados, y documentar toda brecha aunque no se notifique.
9. **Medidas de seguridad reales:** prohibido consignar medidas que no estén implantadas. Un registro que declara cifrado inexistente agrava la posición del despacho ante una brecha.
10. **Secreto profesional:** no redactar procedimientos de atención de derechos que comprometan el secreto profesional o el derecho de defensa del cliente. Ante una solicitud de la contraparte, analizar y responder motivadamente, con asesoramiento si es preciso.
11. **Cero invención:** no inventar proveedores, medidas, plazos, garantías de transferencia, datos del delegado de protección de datos ni números de registro. Lo no aportado permanece como marcador con su nombre propio de plantilla.
12. **Sintaxis de los marcadores (`{{CLAVE: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real: nunca debe quedar rastro de la anotación en el documento escrito. Los marcadores cuyo dato aún no exista se conservan **íntegros, con su clave y su tipo**, para que el cliente y el profesional que revise vean qué falta y de qué naturaleza es. Está PROHIBIDO sustituir la clave propia del marcador por un literal genérico.
