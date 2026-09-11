---
name: derecho-mercantil-constitucion-sociedad
description: >
  Prepara los documentos de constitucion de una sociedad de responsabilidad limitada en Espana
  conforme al **Real Decreto Legislativo 1/2010**, texto refundido de la Ley de Sociedades de Capital
  (LSC), que regula la constitucion, el capital, las aportaciones y el organo de administracion, y al
  **Real Decreto 1784/1996**, Reglamento del Registro Mercantil (RRM), que fija los requisitos de la
  denominacion social y de la inscripcion.


  Genera tres documentos: la solicitud de certificacion negativa de denominacion al Registro Mercantil
  Central, los estatutos sociales completos y la minuta de escritura de constitucion para el notario.


  Trata el capital social minimo de un euro y el regimen especial de reserva y responsabilidad del
  Art. 4.3 LSC introducido por la Ley 18/2022, las aportaciones dinerarias y no dinerarias con la
  responsabilidad solidaria del Art. 73 LSC, la unipersonalidad de los Arts. 12 a 14 LSC, el objeto
  social con su CNAE y las cuatro formas de organizar la administracion del Art. 210 LSC.


  NO usar para sociedades anonimas o cotizadas, para modificaciones estructurales (fusion, escision o
  cesion global), para modificaciones de estatutos de una sociedad ya inscrita, ni para el concurso de
  acreedores.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Ley de Sociedades de Capital](https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544) y
  [Reglamento del Registro Mercantil](https://www.boe.es/buscar/act.php?id=BOE-A-1996-17533).
when_to_use: |
  - El usuario va a crear una sociedad limitada y necesita los estatutos o la minuta de escritura.
  - El usuario necesita solicitar la certificacion negativa de denominacion social al Registro Mercantil Central.
  - El usuario pregunta cuanto capital necesita para constituir una SL o que implica el capital de un euro.
  - El usuario va a aportar bienes o derechos en lugar de dinero al capital y pregunta por su valoracion.
  - El usuario constituye la sociedad como socio unico y pregunta por la unipersonalidad.
  - El usuario pregunta que forma de administracion elegir (administrador unico, solidarios, mancomunados o consejo).
inputs:
  - documento: certificacion de denominacion / estatutos sociales / minuta de escritura (V1)
  - numero_socios: unipersonal / pluripersonal (V2)
  - aportaciones: dinerarias / no dinerarias / mixtas (V3)
  - organo_administracion: administrador unico / solidarios / mancomunados / consejo (V4)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - denominaciones_propuestas: hasta cinco denominaciones sociales por orden de preferencia
  - datos_socios: nombre o razon social, NIF/NIE/CIF, domicilio, estado civil y regimen economico si aplica
  - capital_social: cifra de capital en euros y numero, valor nominal y numeracion de las participaciones
  - reparto_participaciones: participaciones que suscribe cada socio y su desembolso
  - objeto_social: actividades que constituyen el objeto y su codigo CNAE
  - domicilio_social: direccion completa del domicilio social en territorio espanol
  - ejercicio_social: fecha de inicio y cierre del ejercicio social
  - administradores: identidad, cargo, duracion y retribucion del organo de administracion
  - aportaciones_no_dinerarias: descripcion, titulo, valoracion y participaciones que se asignan
outputs:
  - solicitud_certificacion_denominacion: solicitud de certificacion negativa al Registro Mercantil Central, DRAFT
  - estatutos_sociales: estatutos completos de la sociedad limitada por capitulos y articulos, DRAFT
  - minuta_escritura_constitucion: minuta de escritura de constitucion para el notario, DRAFT
  - checklist_tramites: relacion de tramites, organismos, plazos y costes de la constitucion
references:
  - references/lsc-constitucion-sociedad-limitada.md
  - references/tramites-denominacion-notaria-registro.md
  - references/estilo-redaccion-societaria.md
assets:
  - assets/template-solicitud-certificacion-denominacion.md
  - assets/template-estatutos-sociedad-limitada.md
  - assets/template-minuta-escritura-constitucion.md
---

# Constituir una Sociedad de Responsabilidad Limitada (Denominacion, Estatutos y Escritura)

> DRAFT — para revisión por un abogado mercantilista o notario antes de su firma, elevación a público o inscripción. No constituye asesoramiento jurídico vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva y rigurosa a través de un procedimiento estructurado en 5 fases secuenciales para preparar la documentación de constitución de una sociedad de responsabilidad limitada.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `certificacion_denominacion` | `estatutos_sociales` | `escritura_constitucion` | `sociedad_anonima`.
- **V2 (Número de Socios):** `unipersonal` | `pluripersonal`.
- **V3 (Naturaleza de las Aportaciones):** `dinerarias` | `no_dinerarias` | `mixtas`.
- **V4 (Órgano de Administración):** `administrador_unico` | `administradores_solidarios` | `administradores_mancomunados` | `consejo_administracion`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar qué documento se prepara y el encuadre societario.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un abogado mercantilista (de usted), confirmando que vais a preparar la documentación de constitución de su sociedad limitada.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca qué documento necesita, cuántos socios habrá y cómo se administrará la sociedad, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), el número de socios (`V2`) o el órgano de administración (`V4`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar cual de los tres documentos de constitucion se prepara.",
      "question": "¿Qué documento necesita preparar ahora?",
      "options": [
        {"id": "certificacion_denominacion", "label": "Solicitud de certificación de denominación social (primer paso, Registro Mercantil Central)"},
        {"id": "estatutos_sociales", "label": "Estatutos sociales de la sociedad limitada"},
        {"id": "escritura_constitucion", "label": "Minuta completa de escritura de constitución para el notario"},
        {"id": "sociedad_anonima", "label": "Se trata de una sociedad anónima o cotizada"}
      ]
    },
    {
      "id": "numero_socios",
      "rationale": "Resolver V2 para aplicar el regimen de unipersonalidad de los Arts. 12 a 14 LSC.",
      "question": "¿La sociedad se constituye con un socio único o con varios socios?",
      "options": [
        {"id": "unipersonal", "label": "Socio único (sociedad unipersonal)"},
        {"id": "pluripersonal", "label": "Varios socios"}
      ]
    },
    {
      "id": "organo_administracion",
      "rationale": "Resolver V4 para redactar el articulo de administracion conforme al Art. 210 LSC.",
      "question": "¿Cómo se va a organizar la administración de la sociedad?",
      "options": [
        {"id": "administrador_unico", "label": "Administrador único (una sola persona con todas las facultades)"},
        {"id": "administradores_solidarios", "label": "Varios administradores solidarios (cada uno actúa por sí solo)"},
        {"id": "administradores_mancomunados", "label": "Dos administradores mancomunados (deben actuar conjuntamente)"},
        {"id": "consejo_administracion", "label": "Consejo de administración (de tres a doce miembros)"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `numero_socios`
- `V4` — `organo_administracion`
- `V3` — naturaleza de las aportaciones: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo, en la sección de capital social

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = sociedad_anonima`:**
  - **DETENER.** Informar de que la sociedad anónima tiene capital mínimo de 60.000 euros, exige informe de experto independiente para las aportaciones no dinerarias (Art. 67 LSC) y tiene un régimen propio de acciones y de junta que esta skill no cubre. Derivar a abogado mercantilista. No crear documento.
- **Si `V1 = certificacion_denominacion`:**
  - Plantilla del sistema: `assets/template-solicitud-certificacion-denominacion.md`. Proceder a la **Fase 2**.
- **Si `V1 = estatutos_sociales`:**
  - Plantilla del sistema: `assets/template-estatutos-sociedad-limitada.md`. Proceder a la **Fase 2**.
- **Si `V1 = escritura_constitucion`:**
  - Plantilla del sistema: `assets/template-minuta-escritura-constitucion.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina si se incorpora la declaración de unipersonalidad y la mención obligatoria "Sociedad Unipersonal" (Art. 13 LSC).
- `V4` no elige plantilla: determina la redacción del artículo de administración y las facultades del órgano.
- `V3` no elige plantilla: determina si se describe la aportación no dineraria y si se activa la advertencia de responsabilidad solidaria del Art. 73 LSC.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `lsc-constitucion-sociedad-limitada.md`, `tramites-denominacion-notaria-registro.md` y `estilo-redaccion-societaria.md`.
2. Opcionalmente verifica mediante `web_search` la vigencia del régimen de capital del Art. 4 LSC, los aranceles notariales y registrales y el funcionamiento del Registro Mercantil Central. Si detectas modificaciones normativas, aplica la redacción vigente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal y Secuencia de Trámites:**
   - Explicar el orden imperativo: primero la certificación negativa de denominación en el Registro Mercantil Central, después la apertura de cuenta y el desembolso del capital, después la escritura ante notario con los estatutos incorporados, y por último la inscripción en el Registro Mercantil Provincial y el alta censal en la AEAT.
   - Advertir de los plazos: la certificación de denominación caduca a los tres meses para su uso ante notario (la reserva del nombre dura seis), y los administradores deben presentar la escritura a inscripción en el plazo de dos meses (Art. 32 LSC).
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Nombrar por su ruta la plantilla **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
- **Si `origen_plantilla = plantilla_sistema`:** utiliza el asset enrutado y avanza a la **Fase 3**.
- **Si `origen_plantilla = plantilla_usuario`:** toma la plantilla adjunta en `<attached_documents>` o el texto pegado en `<user_message>`, verifica que no contenga cláusulas nulas (en particular cláusulas que hagan prácticamente libre la transmisión voluntaria de participaciones, prohibidas por el Art. 108.1 LSC, o que atribuyan al socio el derecho de separación sin causa), advierte en el chat de la nulidad y propón la redacción válida, y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en el workspace del usuario, con el nombre que corresponda: `solicitud_certificacion_denominacion.md`, `estatutos_sociales.md` o `minuta_escritura_constitucion.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos de la clasificación y de la escucha activa (número de socios, forma de administración, denominaciones propuestas). Todos los datos pendientes permanecen como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves. PROHIBIDO dejar archivos en blanco o con notas resumidas.
2. **Validación de Disco (`read_file`):** ejecuta `read_file` sobre el archivo creado para confirmar su integridad.
3. **Confirmación en Chat:** informa al usuario de la ruta del archivo generado e introduce de inmediato la primera sección de la **Fase 4** sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques. Para cada bloque, ejecuta estrictamente el ciclo interactivo:
```
[Anuncio de la sección + Pregunta] --> [Vista Previa en texto plano] --> [¿Confirmamos esta cláusula?] --> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Anuncio y Pregunta en Chat:** anuncia la sección sustantiva que se aborda con una frase breve en registro jurídico-mercantil (por ejemplo, *"Pasamos ahora a fijar el capital social y el reparto de participaciones"*) y, en el mismo mensaje, formula ya la primera pregunta. No pidas permiso para pasar de sección: informa y continúa.
2. **Búsqueda prioritaria de partes e intervinientes y Regla de Cero Redundancia (`search_clients` / `get_client` — REG-CLI-01 y REG-CLI-02):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** conforme a `REG-CLI-01` de `CLAUDE.md`. Si los datos de una persona ya fueron obtenidos mediante `search_clients` o `get_client`, **queda TERMINANTEMENTE PROHIBIDO volver a pedir dicha información** (nombre, DNI/NIE/CIF, domicilio, contacto, etc.), ya sea en el chat o en `slot_filling_request` (`REG-CLI-02`). Si todos los datos requeridos constan en la ficha del cliente, **NO invoques `slot_filling_request`**: redacta directamente la cláusula, muestra la vista previa en texto plano en el chat y pide confirmación. Solo si faltan campos específicos ausentes en la ficha, invocarás `slot_filling_request` exclusivamente para los datos pendientes.
   - **Datos estructurados no de cliente agrupados (`slot_filling_request`, MANDATORIO):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
3. **Vista Previa (Preview):** muestra el texto redactado en texto plano, sin backticks de código.
4. **Confirmación:** pregunta literalmente: `¿Confirmamos esta cláusula?`.
5. **Persistencia en Disco:** tras la confirmación, aplica `edit_file` con coincidencia exacta y verifica inmediatamente con `read_file`.
6. **Validación de sentido, no solo de formato:** razona si la respuesta tiene sentido. Si la suma de participaciones suscritas no coincide con el capital, si el valor nominal no es divisor exacto del capital o si el objeto social es genérico e inscribible con reparos, dialoga en el chat, señala el motivo y pide aclaración antes de volcarlo.

### Hoja de Ruta de Secciones — RAMA CERTIFICACIÓN DE DENOMINACIÓN:

1. **Solicitante y condición** *(confirmación agrupada)*: nombre y apellidos o razón social, NIF/NIE/CIF, domicilio y correo de notificación; condición de futuro socio fundador o de representante.
2. **Denominaciones propuestas**: hasta cinco denominaciones por orden de preferencia, con la indicación obligatoria de la forma social ("Sociedad de Responsabilidad Limitada" o "S.L."). Advertir de las prohibiciones: identidad con denominación preexistente, uso de términos oficiales o de nombres de personas sin su consentimiento, y de la necesidad de autorización para determinados términos.
3. **Forma de expedición y advertencia de plazos**: soporte electrónico o papel; vigencia de tres meses para el otorgamiento de la escritura y reserva de seis meses a favor del solicitante.

### Hoja de Ruta de Secciones — RAMA ESTATUTOS SOCIALES:

1. **Denominación, objeto y domicilio** *(confirmación agrupada)*: denominación con su forma social, actividades que integran el objeto social con su CNAE, domicilio social y órgano competente para trasladarlo dentro del territorio nacional.
2. **Duración, comienzo de operaciones y ejercicio social**: duración indefinida salvo pacto, fecha de comienzo de las operaciones y fechas de apertura y cierre del ejercicio.
3. **Capital social y participaciones**: cifra del capital, número de participaciones, valor nominal y numeración correlativa. *Condicional capital inferior a 3.000 euros:* consignar el régimen del Art. 4.3 LSC (dotación a reserva legal de al menos el 20% del beneficio hasta que reserva y capital alcancen 3.000 euros, y responsabilidad solidaria de los socios por la diferencia en caso de liquidación con patrimonio insuficiente).
4. **Régimen de transmisión de participaciones**: transmisión libre entre socios, cónyuge, ascendientes, descendientes y sociedades del grupo, y sujeta a consentimiento de la junta en los demás casos (Arts. 107 y 108 LSC), con el procedimiento de comunicación, plazos y determinación del valor razonable. Advertir de la nulidad de las cláusulas que hagan prácticamente libre la transmisión.
5. **Órgano de administración**: modo de organizar la administración conforme a `V4`, duración del cargo (indefinida en la sociedad limitada salvo previsión estatutaria), facultades, régimen de retribución (Art. 217 LSC) y prohibición de competencia.
6. **Junta general**: convocatoria, forma de comunicación, mayorías ordinarias y reforzadas (Arts. 198 a 201 LSC) y régimen de la junta universal.
7. **Prestaciones accesorias, separación y exclusión, y disolución**: solo si el usuario las quiere; en otro caso remisión al régimen legal.

### Hoja de Ruta de Secciones — RAMA MINUTA DE ESCRITURA:

1. **Comparecencia de los socios fundadores** *(confirmación agrupada)*: identidad completa, NIF/NIE/CIF, domicilio, estado civil y régimen económico matrimonial cuando el aportante sea persona física, y representación cuando comparezca una persona jurídica con sus datos registrales.
2. **Voluntad de constituir y denominación**: manifestación de la voluntad de fundar la sociedad, denominación certificada y datos de la certificación del Registro Mercantil Central.
3. **Capital, suscripción y desembolso**: capital suscrito, participaciones asignadas a cada socio y acreditación del desembolso. *Condicional aportaciones dinerarias:* certificación bancaria de ingreso o manifestación de aportación ante el notario. *Condicional aportaciones no dinerarias:* descripción, título y valoración de cada bien o derecho, participaciones que se asignan en contraprestación y advertencia expresa de la responsabilidad solidaria de socios y administradores por la realidad y valoración (Art. 73 LSC), sin que en la sociedad limitada se exija informe de experto independiente.
4. **Estatutos y nombramiento de administradores**: incorporación de los estatutos aprobados, nombramiento del órgano de administración con aceptación del cargo y, en su caso, retribución.
5. **Unipersonalidad y declaraciones finales**: *Condicional `V2 = unipersonal`:* declaración de unipersonalidad para su constancia registral y advertencia del deber de hacer constar la condición en toda la documentación y de la responsabilidad del socio único si la unipersonalidad no se inscribe en el plazo de seis meses (Art. 14 LSC). Solicitud de NIF provisional, exención de la constitución en el impuesto sobre operaciones societarias y apoderamientos para la tramitación.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
El documento de constitución ha sido generado y actualizado en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección (objeto social, capital, participaciones, administración o junta).
2. Añadir cláusulas opcionales (prestaciones accesorias, mayorías reforzadas, separación y exclusión).
3. Cambiar la forma de organizar la administración.
4. Revisar la coherencia global y realizar control de calidad previo a la notaría.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT:** el documento es una minuta preparatoria; debe ser revisada por un abogado mercantilista y por el notario autorizante antes de su otorgamiento.
2. **Forma pública e inscripción:** la constitución exige escritura pública e inscripción en el Registro Mercantil Provincial. La sociedad no adquiere personalidad jurídica de sociedad limitada hasta su inscripción; los administradores deben presentar la escritura a inscripción en el plazo de dos meses y responden solidariamente de los daños por el incumplimiento (Art. 32 LSC).
3. **Capital inferior a 3.000 euros:** recordar la dotación reforzada a reserva legal y la responsabilidad solidaria de los socios hasta 3.000 euros en caso de liquidación con patrimonio insuficiente (Art. 4.3 LSC).
4. **Trámites posteriores y organismos:**
   - Denominación: Registro Mercantil Central (rmc.es).
   - Escritura: notaría de libre elección.
   - Inscripción: Registro Mercantil Provincial del domicilio social.
   - NIF y alta censal: AEAT, modelo 036 (NIF provisional antes de la escritura y definitivo tras la inscripción).
   - Libro registro de socios y legalización de libros: obligatorios desde la constitución (Art. 104 LSC).

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar siempre las referencias antes de citar preceptos, cifras de capital o plazos. Nunca usar el capital mínimo de 3.000 euros como vigente: fue sustituido por el de un euro con el régimen especial del Art. 4.3 LSC.
2. **Cero Invención de Datos:** queda estrictamente prohibido inventar denominaciones, NIF/CIF, cifras de capital, datos registrales o códigos CNAE. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** si se detectan novedades normativas o arancelarias, aplicarlas en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
4. **Límites de Alcance:** no preparar sociedades anónimas o cotizadas, modificaciones estructurales, modificaciones de estatutos de sociedad ya inscrita, aumentos o reducciones de capital, ni operaciones con indicios de insolvencia, que deben derivarse a profesional colegiado.
