---
name: derecho-mercantil-pacto-socios
description: >
  Redacta el pacto de socios (pacto parasocial) de una sociedad limitada espanola al amparo del
  **Codigo Civil** (Arts. 1091, 1255 y 1258), que consagra la libertad de pactos y su fuerza
  obligatoria entre las partes, y del **Real Decreto Legislativo 1/2010**, texto refundido de la Ley
  de Sociedades de Capital (Art. 29 LSC), que declara los pactos reservados no oponibles a la
  sociedad.


  Genera dos documentos: el pacto entre socios fundadores (permanencia y devengo progresivo de
  participaciones, dedicacion, no competencia, propiedad intelectual, mayorias reforzadas y regimen de
  salida) y el pacto de entrada de inversor (aportacion y valoracion, derechos de informacion y veto,
  antidilucion, arrastre y acompanamiento, preferencia en liquidacion).


  Explica que clausulas necesitan trasladarse a estatutos para ganar eficacia frente a la sociedad y
  frente a terceros, y advierte de los limites de validez de la permanencia, de la no competencia y de
  la clausula penal.


  NO usar para sociedades cotizadas, para protocolos de sociedad anonima con acciones sindicadas, para
  conflictos societarios ya abiertos ni para la modificacion de estatutos, que exige escritura publica
  e inscripcion.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Codigo Civil](https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763) y
  [Ley de Sociedades de Capital](https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544).
when_to_use: |
  - Varios socios crean una sociedad y quieren regular entre ellos lo que los estatutos no pueden o no conviene publicar.
  - Un inversor va a entrar en el capital y exige derechos de veto, informacion, antidilucion o arrastre.
  - Los socios quieren pactar permanencia, dedicacion exclusiva o no competencia entre ellos.
  - El usuario pregunta que pasa si un socio se marcha pronto o deja de trabajar en el proyecto.
  - El usuario pregunta la diferencia entre pacto de socios y estatutos, o si el pacto obliga a la sociedad.
  - El usuario quiere fijar como se decide en caso de bloqueo o empate entre socios.
inputs:
  - documento: pacto de fundadores / pacto de entrada de inversor (V1)
  - alcance_firmantes: todos los socios / solo algunos socios (V2)
  - permanencia: con permanencia y devengo progresivo / sin permanencia (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_sociedad: denominacion, domicilio, CIF y datos registrales de la sociedad
  - datos_socios: nombre o razon social, NIF/NIE/CIF, domicilio y participaciones de cada firmante
  - reparto_capital: participaciones y porcentaje de cada socio antes y despues de la operacion
  - aportacion_inversor: importe, valoracion pre y post money y forma de desembolso
  - materias_reservadas: decisiones que exigiran mayoria reforzada o veto del inversor
  - permanencia_plazos: plazo de permanencia, calendario de devengo y consecuencias de la salida
  - no_competencia: ambito material, territorial y temporal de la prohibicion de competir
  - clausula_penal: importe o formula de la penalizacion por incumplimiento
  - regimen_salida: arrastre, acompanamiento, derecho de adquisicion preferente y valoracion
outputs:
  - pacto_socios_fundadores: pacto entre socios fundadores completo por estipulaciones, DRAFT
  - pacto_entrada_inversor: pacto de socios con entrada de inversor completo por estipulaciones, DRAFT
  - cuadro_estatutos_vs_pacto: relacion de clausulas que conviene trasladar a estatutos y por que
references:
  - references/lsc-pactos-parasociales.md
  - references/limites-permanencia-competencia-penal.md
  - references/estilo-redaccion-societaria.md
assets:
  - assets/template-pacto-socios-fundadores.md
  - assets/template-pacto-entrada-inversor.md
---

# Redactar el Pacto de Socios (Pacto Parasocial)

> DRAFT — para revisión por un abogado mercantilista o notario antes de su firma, elevación a público o inscripción. No constituye asesoramiento jurídico vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva y rigurosa a través de un procedimiento estructurado en 5 fases secuenciales para redactar un pacto parasocial.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `pacto_fundadores` | `pacto_entrada_inversor` | `sociedad_cotizada`.
- **V2 (Alcance de los Firmantes):** `todos_los_socios` | `solo_algunos_socios`.
- **V3 (Permanencia):** `con_permanencia` | `sin_permanencia`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar qué pacto se redacta y quién lo firma.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un abogado mercantilista (de usted), confirmando que vais a preparar el pacto de socios y advirtiendo en una línea de que el pacto obliga a quienes lo firman pero, por sí solo, no es oponible a la sociedad.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca si se trata de un pacto entre fundadores o de la entrada de un inversor, quién firma y si habrá permanencia, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), el alcance de los firmantes (`V2`) o la permanencia (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar si el pacto es entre fundadores o de entrada de inversor.",
      "question": "¿Qué situación quiere regular el pacto?",
      "options": [
        {"id": "pacto_fundadores", "label": "Acuerdo entre los socios fundadores del proyecto"},
        {"id": "pacto_entrada_inversor", "label": "Entrada de un inversor en el capital de la sociedad"},
        {"id": "sociedad_cotizada", "label": "Se trata de una sociedad cotizada o de acciones sindicadas de una anónima"}
      ]
    },
    {
      "id": "alcance_firmantes",
      "rationale": "Resolver V2: el pacto omnilateral (todos los socios) tiene mayor eficacia practica que el parcial.",
      "question": "¿Van a firmar el pacto todos los socios de la sociedad, o solo algunos?",
      "options": [
        {"id": "todos_los_socios", "label": "Todos los socios (pacto omnilateral)"},
        {"id": "solo_algunos_socios", "label": "Solo algunos socios"}
      ]
    },
    {
      "id": "permanencia",
      "rationale": "Resolver V3 para incluir o no el compromiso de permanencia y el devengo progresivo.",
      "question": "¿Quiere que los socios queden comprometidos a permanecer un tiempo mínimo, con devengo progresivo de sus participaciones si se marchan antes?",
      "options": [
        {"id": "con_permanencia", "label": "Sí: permanencia mínima con devengo progresivo y penalización"},
        {"id": "sin_permanencia", "label": "No: cada socio conserva sus participaciones sin compromiso de permanencia"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `alcance_firmantes`
- `V3` — `permanencia`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = sociedad_cotizada`:**
  - **DETENER.** Informar de que los pactos parasociales de sociedades cotizadas están sujetos a deberes de comunicación y publicidad ante la Comisión Nacional del Mercado de Valores y al régimen propio de la legislación del mercado de valores, que esta skill no cubre. Derivar a abogado especialista en mercado de valores. No crear documento.
- **Si `V1 = pacto_fundadores`:**
  - Plantilla del sistema: `assets/template-pacto-socios-fundadores.md`. Proceder a la **Fase 2**.
- **Si `V1 = pacto_entrada_inversor`:**
  - Plantilla del sistema: `assets/template-pacto-entrada-inversor.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina la redacción de la estipulación de eficacia y oponibilidad, y la advertencia sobre el alcance del pacto frente a la sociedad.
- `V3` no elige plantilla: determina si se incorporan las estipulaciones de permanencia, devengo progresivo y cláusula penal, o si se suprimen.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `lsc-pactos-parasociales.md`, `limites-permanencia-competencia-penal.md` y `estilo-redaccion-societaria.md`.
2. Opcionalmente verifica mediante `web_search` la doctrina reciente sobre oponibilidad de pactos omnilaterales y sobre moderación judicial de cláusulas penales. Aplica la redacción vigente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal y Eficacia del Pacto:**
   - Explicar que el pacto obliga a quienes lo firman con fuerza de ley entre las partes, pero que el Art. 29 LSC declara los pactos reservados **no oponibles a la sociedad**: si un socio vota en junta incumpliendo el pacto, el voto vale y lo que nace es una indemnización por incumplimiento.
   - Explicar la consecuencia práctica: las cláusulas que deban desplegar eficacia frente a la sociedad o frente a terceros adquirentes (restricciones a la transmisión, mayorías reforzadas, prestaciones accesorias) conviene **trasladarlas a estatutos** mediante escritura pública e inscripción.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Mencionar por su denominación formal la plantilla (sin mostrar rutas internas ni volcar su contenido) **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Elección de Plantilla Base:** Aplica el protocolo universal de `REG-AST-01` (`CLAUDE.md`), convocando en ese mismo turno el formulario interactivo `restricted_human_in_the_loop_request` para que el usuario elija entre la plantilla del sistema o aportar su propia minuta.

### 2.3 Manejo Determinista de la Elección
Aplica rigurosamente el protocolo de `REG-AST-01` (`CLAUDE.md`): si se selecciona `plantilla_sistema`, carga la plantilla oficial y avanza a la **Fase 3**; si se selecciona `plantilla_usuario`, requiere la minuta (si no consta ya en el chat), ejecuta el control de legalidad y avanza a la **Fase 3**.
---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

Aplica rigurosamente la directiva `REG-DOC-01` y la sección 6.1 de `CLAUDE.md`:
1. **Escritura del Documento (`create_file`):** Vuelca íntegramente la plantilla acordada en un archivo en el workspace con nombre en `snake_case.md`, aplicando el principio Zero-Omission y el volcado inmediato total de partes (`REG-CLI-04`) en título H1, comparecencia y firmas.
2. **Validación de Integridad:** Comprobación prioritaria mediante `# WORKSPACE ACTIVE DOCUMENTS`.
3. **Confirmación en Chat y Encadenamiento Inmediato:** Informa en el chat de la ruta absoluta del documento creado y los datos de partes incorporados, e introduce en esa misma respuesta la primera sección de la Fase 4 sin detener el flujo.
---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial las secciones del documento respetando rigurosamente las directivas operativas globales de `CLAUDE.md`:
- **Partes e Intervinientes (REG-CLI-01 a 04):** Búsqueda prioritaria con `search_clients`, desambiguación con opción obligatoria `ninguna`, consentimiento de guardado con `save_client` (REG-CLI-03) y volcado directo e inmediato al editor (`edit_file` / `create_file`) sin confirmación en chat (REG-CLI-04).
- **Datos Estructurados Objetivos:** Solicitud en bloque mediante `slot_filling_request`.
- **Equivalencia Chat / Formulario (REG-DAT-01):** Ingestión directa de información aportada por chat sin re-emitir formularios innecesarios; reenvío oportuno si el usuario canceló sin responder.
- **Cláusulas Sustantivas / Negociables:** Negociación en chat -> Vista previa en texto plano -> Pregunta literal de confirmación (`¿Confirmamos esta cláusula?` / `¿Confirmamos esta sección?`) -> Persistencia con `edit_file`.

### Hoja de Ruta de Secciones — RAMA PACTO DE FUNDADORES:

1. **Partes y sociedad** *(confirmación agrupada)*: identidad completa de cada socio firmante, participaciones y porcentaje que ostenta, y datos de la sociedad afectada.
2. **Objeto del pacto y relación con los estatutos**: finalidad, carácter parasocial, y advertencia expresa de no oponibilidad a la sociedad con indicación de qué cláusulas se llevarán a estatutos.
3. **Dedicación y régimen de exclusividad**: dedicación exigida a cada socio, compatibilidad con otras actividades y consecuencias del incumplimiento.
4. **Permanencia y devengo progresivo**: *Condicional `V3 = con_permanencia`:* plazo de permanencia, calendario de devengo de participaciones, distinción entre salida justificada y no justificada, y precio de las participaciones no devengadas.
5. **No competencia y no captación**: ámbito material, territorial y temporal de la prohibición durante la relación y tras la salida; prohibición de captar clientes, proveedores y empleados.
6. **Propiedad intelectual e industrial y confidencialidad**: cesión a la sociedad de los desarrollos realizados para el proyecto y deber de secreto con su duración.
7. **Gobierno y materias reservadas**: composición del órgano de administración, materias que exigirán mayoría reforzada y mecanismo de desbloqueo en caso de empate.
8. **Régimen de transmisión y salida**: derecho de adquisición preferente, acompañamiento, arrastre y método de valoración de las participaciones.
9. **Incumplimiento, duración y ley aplicable**: cláusula penal con su importe o fórmula, duración del pacto, sumisión a mediación previa y fuero.

### Hoja de Ruta de Secciones — RAMA ENTRADA DE INVERSOR:

1. **Partes, sociedad y situación previa** *(confirmación agrupada)*: identidad de socios actuales e inversor, participaciones y porcentajes antes de la operación.
2. **Operación de entrada**: importe de la aportación, valoración antes y después de la operación, número de participaciones que se crean o transmiten, prima de emisión y forma y calendario de desembolso.
3. **Compromisos de la sociedad y destino de los fondos**: aplicación de los fondos, hitos y consecuencias de su incumplimiento.
4. **Derechos de información y de veto**: información periódica que recibirá el inversor y lista cerrada de materias reservadas sujetas a su consentimiento.
5. **Órgano de administración y asistencia a la junta**: derecho a designar consejero u observador y reglas de convocatoria.
6. **Antidilución y derecho de suscripción preferente**: protección frente a rondas a valoración inferior y régimen de suscripción en futuros aumentos.
7. **Salida: arrastre, acompañamiento y preferencia en liquidación**: derecho de arrastre con sus umbrales, derecho de acompañamiento, preferencia en el reparto en caso de venta o liquidación y su cuantificación.
8. **Permanencia de los fundadores**: *Condicional `V3 = con_permanencia`:* compromiso de permanencia de los socios fundadores, devengo progresivo y consecuencias de la salida anticipada.
9. **Manifestaciones y garantías, incumplimiento y ley aplicable**: manifestaciones sobre la titularidad y situación de la sociedad, consecuencias de su inexactitud, cláusula penal, duración, mediación previa y fuero.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
El pacto de socios ha sido generado y actualizado en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una estipulación (permanencia, no competencia, materias reservadas o salida).
2. Añadir o suprimir el compromiso de permanencia y su devengo progresivo.
3. Revisar qué cláusulas conviene trasladar a los estatutos y preparar ese cuadro.
4. Revisar la coherencia global y realizar control de calidad previo a la firma.
5. Dar el pacto por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT:** el pacto es un borrador preparatorio; debe ser revisado por un abogado mercantilista antes de su firma.
2. **No oponibilidad a la sociedad (Art. 29 LSC):** el pacto vincula únicamente a quienes lo firman. Un acuerdo social adoptado contra el pacto no es nulo por esa sola razón; la consecuencia es la indemnización o la cláusula penal entre los firmantes.
3. **Cláusulas que conviene llevar a estatutos:** restricciones a la transmisión de participaciones, mayorías reforzadas, prestaciones accesorias y causas estatutarias de separación y exclusión, mediante acuerdo de junta, escritura pública e inscripción en el Registro Mercantil.
4. **Límites de validez:** la permanencia sin plazo, la no competencia sin delimitación material, territorial y temporal, y la cláusula penal desproporcionada son susceptibles de nulidad o de moderación judicial. La prohibición estatutaria de transmitir solo es válida con derecho de separación o por plazo máximo de cinco años.
5. **Fecha y prueba:** conviene dotar al pacto de fecha fehaciente, mediante firma electrónica cualificada o legitimación notarial de firmas, para evitar discusiones probatorias.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias antes de citar preceptos o doctrina. No atribuir al pacto efectos frente a la sociedad que la ley le niega.
2. **Cero Invención de Datos:** prohibido inventar denominaciones, CIF, datos registrales, porcentajes, valoraciones o importes. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas o doctrinales en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
4. **Límites de Alcance:** no redactar pactos de sociedades cotizadas, no intervenir en conflictos societarios ya abiertos (impugnación de acuerdos, acciones de responsabilidad), ni preparar la modificación de estatutos, que exige escritura pública e inscripción y se aborda con la skill de constitución y vida societaria correspondiente.
