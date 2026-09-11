---
name: derecho-civil-extincion-condominio
description: >
  Genera los documentos para deshacer una copropiedad sobre un inmueble conforme al **Codigo Civil**,
  que regula la comunidad de bienes y el derecho de todo comunero a pedir en cualquier momento la
  division de la cosa comun (Arts. 392 a 406), y a la **Ley 1/2000 de Enjuiciamiento Civil**, que fija
  el cauce judicial cuando no hay acuerdo.


  Genera tres documentos: el requerimiento previo a los demas comuneros con propuesta de adjudicacion
  y valoracion, la minuta de escritura de extincion de condominio para el notario con su compensacion
  en metalico y el reparto de gastos, y la demanda de division de la cosa comun cuando el acuerdo
  resulta imposible.


  Trata el caso mas frecuente en la practica, la pareja no casada que compro a medias, con la
  subrogacion o cancelacion del prestamo hipotecario pendiente, la indivisibilidad del inmueble y sus
  consecuencias, la valoracion y la compensacion entre comuneros, la liquidacion de los gastos
  soportados por uno solo, y la tributacion mas favorable de la extincion frente a la compraventa.


  NO usar para la liquidacion del regimen economico matrimonial, que corresponde a la skill de
  liquidacion de gananciales, ni para la particion de una herencia con varios herederos, que
  corresponde a la skill de herencia, ni para la division de patrimonios empresariales.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Codigo Civil](https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763) y
  [Ley 1/2000 de Enjuiciamiento Civil](https://www.boe.es/buscar/act.php?id=BOE-A-2000-323).
when_to_use: |
  - Una pareja no casada se separa y quiere deshacer la copropiedad de la vivienda que compro a medias.
  - Varios copropietarios de un inmueble quieren que uno se quede con el y compense a los demas.
  - Un comunero quiere salir de la copropiedad y los demas no acceden.
  - El usuario pregunta como se reparte la hipoteca pendiente al extinguir el condominio.
  - El usuario pregunta que impuesto se paga al extinguir un condominio y si sale mas barato que vender.
  - El usuario ha pagado solo la hipoteca o los gastos del inmueble comun y quiere que se le compense.
inputs:
  - documento: requerimiento previo / escritura de extincion de condominio / demanda de division (V1)
  - acuerdo: hay acuerdo entre comuneros / no hay acuerdo (V2)
  - hipoteca: con prestamo hipotecario pendiente / sin carga hipotecaria (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_comuneros: nombre, NIF/NIE, domicilio, estado civil y cuota de participacion de cada comunero
  - datos_inmueble: direccion, referencia catastral, superficie, datos registrales y anejos
  - titulo_adquisicion: titulo por el que se adquirio la copropiedad, fecha y notario
  - valoracion: valor atribuido al inmueble y forma de determinarlo, con tasacion si existe
  - adjudicacion: comunero al que se adjudica el inmueble y compensacion en metalico a los demas
  - hipoteca_pendiente: entidad, numero de prestamo, capital pendiente y titulares
  - gastos_soportados: pagos de hipoteca, IBI, comunidad, seguros y obras soportados por cada comunero
  - uso_del_inmueble: quien ha usado el inmueble y desde cuando, y si se reclama compensacion por el uso
  - fiscalidad: reparto de impuestos, notaria y registro entre los comuneros
outputs:
  - requerimiento_extincion_condominio: requerimiento previo a los comuneros con propuesta y valoracion, DRAFT
  - minuta_escritura_extincion: minuta de escritura de extincion de condominio para el notario, DRAFT
  - demanda_division_cosa_comun: demanda de division de la cosa comun, DRAFT
  - checklist_tramites: tramites, tributacion, cancelacion de cargas e inscripcion registral
references:
  - references/cc-comunidad-de-bienes-y-division.md
  - references/hipoteca-valoracion-y-fiscalidad-de-la-extincion.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/template-requerimiento-extincion-condominio.md
  - assets/template-minuta-escritura-extincion-condominio.md
  - assets/template-demanda-division-cosa-comun.md
---

# Extinción de Condominio y División de la Cosa Común

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para deshacer una copropiedad.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `requerimiento_previo` | `escritura_extincion` | `demanda_division` | `regimen_matrimonial`.
- **V2 (Acuerdo):** `con_acuerdo` | `sin_acuerdo`.
- **V3 (Carga Hipotecaria):** `con_hipoteca` | `sin_hipoteca`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar si hay acuerdo y qué documento procede.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un abogado de despacho (de usted), confirmando que vais a preparar la extinción de la copropiedad del inmueble.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca si hay acuerdo entre los copropietarios, qué documento necesita y si queda hipoteca pendiente, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), la existencia de acuerdo (`V2`) o la carga hipotecaria (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar si se prepara la via extrajudicial, la escritura o la demanda.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "requerimiento_previo", "label": "Requerimiento a los demás copropietarios, con propuesta de reparto"},
        {"id": "escritura_extincion", "label": "Minuta de escritura de extinción de condominio para el notario"},
        {"id": "demanda_division", "label": "Demanda judicial de división de la cosa común"},
        {"id": "regimen_matrimonial", "label": "Estamos casados y hay que liquidar el régimen económico matrimonial"}
      ]
    },
    {
      "id": "acuerdo",
      "rationale": "Resolver V2: con acuerdo la via es notarial; sin acuerdo hay que agotar el requerimiento y el medio adecuado de solucion de controversias antes de demandar.",
      "question": "¿Hay acuerdo entre todos los copropietarios sobre quién se queda el inmueble y por cuánto?",
      "options": [
        {"id": "con_acuerdo", "label": "Sí, hay acuerdo"},
        {"id": "sin_acuerdo", "label": "No hay acuerdo, o no contestan"}
      ]
    },
    {
      "id": "hipoteca",
      "rationale": "Resolver V3: la hipoteca pendiente exige tratar la subrogacion o cancelacion y el consentimiento de la entidad.",
      "question": "¿Queda préstamo hipotecario pendiente sobre el inmueble?",
      "options": [
        {"id": "con_hipoteca", "label": "Sí, queda hipoteca por pagar"},
        {"id": "sin_hipoteca", "label": "No, está libre de cargas"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `acuerdo`
- `V3` — `hipoteca`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = regimen_matrimonial`:**
  - **DETENER.** Informar de que la disolución del régimen económico matrimonial tiene un cauce propio, con inventario, avalúo y liquidación conjunta de todos los bienes y deudas del régimen, y que no debe confundirse con la extinción de un condominio ordinario. Derivar a la skill de liquidación de gananciales del plugin de derecho civil. No crear documento.
- **Si `V1 = requerimiento_previo`:**
  - Plantilla del sistema: `assets/template-requerimiento-extincion-condominio.md`. Proceder a la **Fase 2**.
- **Si `V1 = escritura_extincion`:**
  - Plantilla del sistema: `assets/template-minuta-escritura-extincion-condominio.md`. Proceder a la **Fase 2**.
- **Si `V1 = demanda_division`:**
  - Plantilla del sistema: `assets/template-demanda-division-cosa-comun.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina el tono del requerimiento, la advertencia sobre el medio adecuado de solución de controversias previo a la demanda y las alternativas que se ofrecen.
- `V3` no elige plantilla: determina si se incorporan las cláusulas de subrogación o cancelación del préstamo y la advertencia sobre el consentimiento de la entidad acreedora.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `cc-comunidad-de-bienes-y-division.md`, `hipoteca-valoracion-y-fiscalidad-de-la-extincion.md` y `estilo-redaccion-escritos.md`.
2. Verifica mediante `web_search`, cuando el caso lo requiera, el tipo vigente del impuesto de actos jurídicos documentados en la comunidad autónoma competente, así como la vigencia de la exigencia de intento previo de solución extrajudicial antes de demandar. Aplica la redacción vigente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal y Consecuencias Económicas:**
   - Explicar la regla capital: **ningún comunero está obligado a permanecer en la comunidad** y cualquiera puede pedir en cualquier momento la división de la cosa común. La copropiedad no se puede imponer indefinidamente.
   - Explicar que si el inmueble es **indivisible** (lo habitual en una vivienda), la división se materializa adjudicándolo a un comunero con compensación en metálico a los demás o, en su defecto, vendiéndolo en pública subasta con reparto del precio.
   - Explicar la **ventaja fiscal** de la extinción de condominio bien planteada frente a una compraventa de cuota: cuando la adjudicación es la consecuencia necesaria de la indivisibilidad y se compensa en metálico, tributa por actos jurídicos documentados sobre el valor de la parte adjudicada y no por transmisiones patrimoniales, con un coste sensiblemente inferior.
   - *Condicional `V3 = con_hipoteca`:* advertir de que la extinción de condominio **no libera** al comunero saliente frente al banco: la deuda solo se traslada con la **subrogación** aceptada expresamente por la entidad, o cancelando el préstamo.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Nombrar por su ruta la plantilla **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
- **Si `origen_plantilla = plantilla_sistema`:** utiliza el asset enrutado y avanza a la **Fase 3**.
- **Si `origen_plantilla = plantilla_usuario`:** toma la plantilla adjunta en `<attached_documents>` o el texto pegado en `<user_message>`, verifica que no contenga renuncias indefinidas al derecho a pedir la división (solo válido el pacto de indivisión por plazo limitado), que la compensación no encubra una donación no querida y que no dé por liberado al comunero saliente frente a la entidad acreedora sin subrogación, advierte en el chat y propón la redacción válida, y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en el workspace del usuario, con el nombre `requerimiento_extincion_condominio.md`, `minuta_escritura_extincion_condominio.md` o `demanda_division_cosa_comun.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos de la clasificación y de la escucha activa, incluida la fecha del sistema. Todos los datos pendientes permanecen como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves. PROHIBIDO dejar archivos en blanco o con notas resumidas.
2. **Validación de Disco (`read_file`):** ejecuta `read_file` sobre el archivo creado para confirmar su integridad.
3. **Confirmación en Chat:** informa al usuario de la ruta del archivo generado e introduce de inmediato la primera sección de la **Fase 4** sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques. Para cada bloque, ejecuta estrictamente el ciclo interactivo:
```
[Anuncio de la sección + Pregunta] --> [Vista Previa en texto plano] --> [¿Confirmamos esta cláusula?] --> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Anuncio y Pregunta en Chat:** anuncia la sección sustantiva con una frase breve en registro jurídico (por ejemplo, *"Pasamos ahora a la valoración del inmueble y a la compensación entre comuneros"*) y, en el mismo mensaje, formula ya la primera pregunta. No pidas permiso para pasar de sección: informa y continúa.
2. **Petición de datos en bloque:** para cualquier grupo de datos objetivos o identificativos (datos de los comuneros, datos del inmueble y registrales, datos del préstamo, importes de gastos soportados), **NO preguntes dato por dato en el chat**. Invoca `slot_filling_request` agrupando todos los campos del bloque de una sola vez. Los datos de un mismo comunero se confirman todos juntos al final del bloque, no uno a uno.
3. **Vista Previa (Preview):** muestra el texto redactado en texto plano, sin backticks de código.
4. **Confirmación:** pregunta literalmente: `¿Confirmamos esta cláusula?`.
5. **Persistencia en Disco:** tras la confirmación, aplica `edit_file` con coincidencia exacta y verifica inmediatamente con `read_file`.
6. **Validación de sentido, no solo de formato:** comprueba que las cuotas de participación suman la unidad, que la compensación en metálico se corresponde con el valor atribuido y con las cuotas, que el capital hipotecario pendiente es coherente con lo que se asume, y que la referencia catastral tiene veinte caracteres. Si las cuotas no cuadran o la compensación es notoriamente inferior al valor de la cuota, **dilo antes de volcarlo**, porque puede constituir donación con consecuencias fiscales.

### Hoja de Ruta de Secciones — RAMA REQUERIMIENTO PREVIO:

1. **Comuneros y cuotas** *(confirmación agrupada)*: identidad completa, NIF, domicilio y cuota de cada comunero, con el título por el que adquirieron.
2. **Inmueble y situación registral**: dirección, referencia catastral, superficie, datos registrales, anejos y cargas inscritas.
3. **Situación actual de la comunidad**: quién usa el inmueble y desde cuándo, quién atiende los pagos, y estado del préstamo hipotecario si existe.
4. **Propuesta de extinción**: valoración del inmueble con su fundamento, comunero al que se propone la adjudicación, compensación en metálico y forma de pago, y tratamiento del préstamo pendiente.
5. **Liquidación de gastos y uso**: gastos de hipoteca, IBI, comunidad, seguros y obras soportados por cada comunero, con la compensación que se reclama; y, en su caso, compensación por el uso exclusivo del inmueble.
6. **Plazo, advertencia y cierre**: plazo que se concede para aceptar, ofrecimiento de mediación o del medio adecuado de solución de controversias que corresponda, y advertencia de que, en su defecto, se ejercitará la acción de división con las costas y gastos que ello genere.

### Hoja de Ruta de Secciones — RAMA ESCRITURA DE EXTINCIÓN:

1. **Comparecencia de los comuneros** *(confirmación agrupada)*: identidad completa, NIF, domicilio, estado civil y régimen económico cuando afecte, y cuota de cada uno.
2. **Descripción del inmueble y título**: descripción registral completa, referencia catastral, cargas, y título de adquisición de la copropiedad con su fecha y notario.
3. **Valoración y adjudicación**: valor atribuido al inmueble, adjudicación íntegra al comunero que corresponda por razón de la indivisibilidad, y determinación del exceso de adjudicación.
4. **Compensación en metálico**: importe que recibe cada comunero saliente, medio de pago y momento, con carta de pago si se satisface en el acto.
5. **Préstamo hipotecario**: *Condicional `V3 = con_hipoteca`:* subrogación del adjudicatario en el préstamo con constancia del consentimiento de la entidad, o cancelación con los fondos que se indiquen, y advertencia expresa de que sin consentimiento de la entidad el comunero saliente sigue obligado frente a ella.
6. **Gastos, impuestos y liquidación de cuentas**: reparto de notaría, gestoría, registro e impuestos, y liquidación de los gastos del inmueble soportados por cada comunero hasta la fecha.
7. **Manifestaciones finales, inscripción y apoderamientos**: manifestación sobre el estado posesorio y de deudas de comunidad, solicitud de inscripción, y facultades para la liquidación de impuestos y la subsanación de defectos.

### Hoja de Ruta de Secciones — RAMA DEMANDA DE DIVISIÓN:

1. **Partes, postulación y competencia** *(confirmación agrupada)*: demandante y demandados con sus datos, procurador y abogado, juzgado competente por razón del lugar del inmueble, y cuantía del procedimiento.
2. **Intento previo de solución y su acreditación**: constancia del requerimiento previo y del intento de solución extrajudicial exigido con carácter general antes de demandar, con la documentación que lo acredita.
3. **Hechos**: adquisición de la copropiedad y título, cuotas, situación del inmueble, uso, pagos soportados, gestiones realizadas para la división y negativa o silencio de los demandados.
4. **Fundamentos de derecho**: derecho de todo comunero a pedir la división en cualquier momento, indivisibilidad del inmueble y consecuencia legal (adjudicación con compensación o venta en pública subasta con reparto del precio), y liquidación de los gastos comunes.
5. **Petición**: declaración de la extinción de la comunidad, adjudicación al comunero que corresponda con compensación o, subsidiariamente, venta en pública subasta con admisión de licitadores extraños y reparto del precio conforme a las cuotas; liquidación de los gastos soportados; y costas.
6. **Prueba, cuantía y documentos**: proposición de prueba documental y pericial de valoración, determinación de la cuantía, y relación de documentos que se acompañan.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
El documento ha sido generado y actualizado en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección (valoración, compensación, hipoteca o gastos).
2. Añadir la liquidación de los gastos soportados por un comunero.
3. Preparar el documento siguiente del itinerario (del requerimiento a la escritura, o a la demanda).
4. Revisar la coherencia global y realizar control de calidad previo a la notaría o al juzgado.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT:** el documento es un borrador preparatorio; debe ser revisado por un abogado colegiado y, en su caso, por el notario autorizante.
2. **Nadie está obligado a permanecer en la comunidad:** el derecho a pedir la división es imprescriptible mientras dure la comunidad. Solo es válido el pacto de conservar la cosa indivisa por un **plazo limitado**.
3. **La hipoteca no se reparte con la escritura:** el comunero saliente sigue obligado frente al banco salvo subrogación expresamente consentida por la entidad o cancelación del préstamo. Es el error más costoso en la práctica.
4. **Fiscalidad:** la extinción de condominio por indivisibilidad con compensación en metálico tributa por actos jurídicos documentados y no por transmisiones patrimoniales, lo que la hace sensiblemente más barata que una compraventa de cuota. Si la compensación no se ajusta al valor de la cuota, puede apreciarse donación o exceso de adjudicación sujeto a tributación distinta.
5. **Plusvalía municipal:** la extinción de condominio sin exceso de adjudicación oneroso no suele generar sujeción, pero debe comprobarse con el ayuntamiento y con la naturaleza concreta de la adjudicación.
6. **Vía judicial como último recurso:** la subasta pública suele obtener un precio inferior al de mercado y genera costes. Conviene agotar el acuerdo y dejar acreditado el intento.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias antes de citar preceptos, tipos impositivos o plazos. No afirmar el tratamiento fiscal sin comprobar la comunidad autónoma competente.
2. **Cero Invención de Datos:** prohibido inventar referencias catastrales, datos registrales, valoraciones, capital hipotecario pendiente o importes de gastos. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas o fiscales en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
4. **Límites de Alcance:** no liquidar regímenes económicos matrimoniales, no partir herencias, no dividir patrimonios empresariales ni preparar la ejecución de la subasta, que corresponden a otras skills o a profesional competente.
