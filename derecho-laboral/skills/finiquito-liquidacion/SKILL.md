---
name: finiquito-liquidacion
description: >
  Genera los documentos de cierre económico de la relación laboral: recibo de finiquito con la
  propuesta de liquidación de partes proporcionales del artículo 49.2 del texto refundido de la Ley
  del Estatuto de los Trabajadores, hoja de liquidación detallada con el desglose y la fórmula de cada
  concepto, acuerdo de extinción por mutuo acuerdo con indemnización pactada, y carta de baja
  voluntaria con preaviso. Aplica el **Estatuto de los Trabajadores aprobado por Real Decreto
  Legislativo 2/2015**, norma básica que regula la extinción del contrato y la liquidación de las cantidades pendientes, en su versión consolidada vigente verificada en el BOE, y toma del convenio
  colectivo aplicable el número y devengo de las pagas extraordinarias, el régimen de vacaciones y los
  plazos de preaviso. Metodología: clasificación de la causa extintiva mediante formulario
  interactivo, plan de acción con el cálculo desglosado de cada concepto, creación del documento base
  en el workspace y edición incremental concepto a concepto. NO usar para redactar la comunicación
  extintiva en sí, que corresponde a la skill `carta-despido`, ni para reclamar judicialmente las
  cantidades impagadas, que corresponde a las skills `conciliacion-previa` y `demanda-social`.
when_to_use: |
  - El usuario quiere calcular o redactar el finiquito de un trabajador que causa baja.
  - El usuario quiere documentar la liquidación de partes proporcionales de salario, pagas extraordinarias y vacaciones.
  - El usuario quiere formalizar una extinción por mutuo acuerdo con indemnización pactada.
  - El trabajador quiere presentar su baja voluntaria con el preaviso exigible, o revisar un finiquito antes de firmarlo.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - tipo_documento: recibo de finiquito / hoja de liquidación / acuerdo de extinción por mutuo acuerdo / carta de baja voluntaria
  - causa_extincion: despido disciplinario / despido objetivo / fin de contrato temporal / baja voluntaria / mutuo acuerdo / jubilación / no superación del periodo de prueba
  - naturaleza_empleador: persona física o persona jurídica
  - datos_empresa: razón social, CIF, domicilio, código de cuenta de cotización, representante y cargo
  - datos_trabajador: nombre, DNI o NIE, número de afiliación, categoría, antigüedad
  - datos_retributivos: salario base, complementos, número y devengo de pagas extraordinarias, si van prorrateadas
  - fecha_extincion: fecha de efectos de la extinción
  - dias_trabajados_mes: días del mes en curso efectivamente trabajados
  - vacaciones: días devengados, disfrutados y pendientes
  - conceptos_adicionales: horas extraordinarias, comisiones, incentivos, anticipos, preaviso incumplido, bienes a devolver
  - indemnizacion_pactada: importe y concepto, solo en el acuerdo de extinción
outputs:
  - recibo_finiquito: recibo con la liquidación completa en markdown, DRAFT, con espacio de firma y salvedad
  - hoja_liquidacion: desglose detallado por conceptos en markdown, DRAFT, con las fórmulas aplicadas
references:
  - references/fuentes-plantillas-validadas.md
  - references/conceptos-de-la-liquidacion-y-calculo.md
  - references/valor-liberatorio-del-finiquito.md
  - references/extincion-por-voluntad-del-trabajador.md
assets:
  - assets/template-acuerdo-extincion-mutuo-acuerdo.md
  - assets/template-carta-baja-voluntaria.md
  - assets/template-hoja-liquidacion-detallada.md
  - assets/template-recibo-finiquito.md
---

# Generar el Finiquito y la Liquidación

> DRAFT — para revisión por un abogado o graduado social colegiado antes de su firma y entrega. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de documento):** `recibo_finiquito` | `hoja_liquidacion` | `acuerdo_mutuo_acuerdo` | `baja_voluntaria`.
- **V2 (Causa de la extinción):** `despido_disciplinario` | `despido_objetivo` | `fin_temporal` | `baja_voluntaria` | `mutuo_acuerdo` | `jubilacion` | `periodo_prueba`. *(Determina si hay indemnización y si hay derecho a prestación por desempleo.)*
- **V3 (Naturaleza del empleador):** `persona_fisica` | `persona_juridica`.
- **V4 (Posición del usuario):** `empresa` | `trabajador`. *(Determina el tono de la advertencia sobre la firma y las salvedades.)*
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

### 1.1 Escucha Activa Previa
Si el usuario ya ha identificado inequívocamente el documento, la causa extintiva y su propia posición, registra los vectores en silencio y pasa a la **Fase 2**.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "causa_extincion",
      "rationale": "Resolver V2: la causa determina qué conceptos integran la liquidación, si hay indemnización y si hay acceso a la prestación por desempleo.",
      "question": "¿Por qué causa se extingue la relación laboral?",
      "options": [
        {"id": "despido_disciplinario", "label": "Despido disciplinario"},
        {"id": "despido_objetivo", "label": "Despido objetivo por causas del artículo 52"},
        {"id": "fin_temporal", "label": "Finalización de contrato temporal"},
        {"id": "baja_voluntaria", "label": "Baja voluntaria de la persona trabajadora"},
        {"id": "mutuo_acuerdo", "label": "Mutuo acuerdo entre las partes"},
        {"id": "jubilacion", "label": "Jubilación de la persona trabajadora"},
        {"id": "periodo_prueba", "label": "No superación del periodo de prueba"}
      ]
    },
    {
      "id": "tipo_documento",
      "rationale": "Resolver V1: cada documento cumple una función distinta y puede necesitarse más de uno.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "recibo_finiquito", "label": "Recibo de finiquito para su firma"},
        {"id": "hoja_liquidacion", "label": "Hoja de liquidación detallada con el desglose de cada concepto"},
        {"id": "acuerdo_mutuo_acuerdo", "label": "Acuerdo de extinción por mutuo acuerdo con indemnización pactada"},
        {"id": "baja_voluntaria", "label": "Carta de baja voluntaria con preaviso"}
      ]
    },
    {
      "id": "posicion_usuario",
      "rationale": "Resolver V4: determina el enfoque de las advertencias sobre el valor de la firma.",
      "question": "¿Desde qué posición actúa usted?",
      "options": [
        {"id": "empresa", "label": "En representación de la empresa"},
        {"id": "trabajador", "label": "En representación de la persona trabajadora"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `tipo_documento`
- `V2` — `causa_extincion`
- `V4` — `posicion_usuario`
- `V3` — naturaleza del empleador: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo

### 1.3 Enrutamiento de Estado (Routing por Vectores)

* **Si `[V1 = recibo_finiquito]` → Plantilla: `assets/template-recibo-finiquito.md`.** Ofrece generar además la hoja de liquidación detallada: el recibo consigna importes, la hoja explica cómo se han obtenido, y en una reclamación posterior la hoja es la que sostiene la posición de la empresa.
* **Si `[V1 = hoja_liquidacion]` → Plantilla: `assets/template-hoja-liquidacion-detallada.md`.**
* **Si `[V1 = acuerdo_mutuo_acuerdo]` → Plantilla: `assets/template-acuerdo-extincion-mutuo-acuerdo.md`.** **Advertencia obligatoria en el chat:** la extinción por mutuo acuerdo **no da derecho a la prestación por desempleo**, porque no constituye situación legal de desempleo. Si lo que las partes quieren es documentar un despido con indemnización pactada, el documento correcto es otro y el cauce habitual es el acuerdo en conciliación. Explícalo antes de continuar y confirma con el usuario.
* **Si `[V1 = baja_voluntaria]` → Plantilla: `assets/template-carta-baja-voluntaria.md`.** **Advertencia obligatoria:** la baja voluntaria no genera indemnización ni derecho a prestación por desempleo, y el incumplimiento del preaviso del convenio faculta a la empresa para descontar del finiquito los días no preavisados.
* **Si `[V4 = trabajador]` → Enfoque de revisión.** Antes de redactar nada, si el trabajador ya ha recibido un finiquito, ofrece revisarlo concepto a concepto y advierte de que **no debe firmarlo sin la salvedad "no conforme"** si discrepa de algún importe o si no ha podido comprobarlo.
- `V2` no elige plantilla: determina que conceptos integran la liquidacion, si procede indemnizacion y si se hace constar la situacion legal de desempleo.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión consolidada vigente del Estatuto de los Trabajadores en el BOE.
3. **Localiza el convenio colectivo aplicable** y extrae: número de pagas extraordinarias y **periodo de devengo de cada una**, régimen de vacaciones y su devengo, plazo de preaviso en la baja voluntaria, y complementos de devengo superior al mes que deban prorratearse.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje formal que contenga:
1. **Conceptos que integrarán la liquidación** según la causa extintiva y el convenio, enumerados.
2. **Advertencias específicas de la causa:** derecho o no a indemnización, derecho o no a prestación por desempleo, y preaviso exigible.
3. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Menciónala por su denominación formal (sin mostrar rutas internas ni volcar su contenido); si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
4. **Elección de Plantilla Base:** Aplica el protocolo universal de `REG-AST-01` (`CLAUDE.md`), convocando en ese mismo turno el formulario interactivo `restricted_human_in_the_loop_request` para que el usuario elija entre la plantilla del sistema o aportar su propia minuta.

### 2.3 Manejo Determinista de la Elección
Aplica rigurosamente el protocolo de `REG-AST-01` (`CLAUDE.md`): si se selecciona `plantilla_sistema`, carga la plantilla oficial y avanza a la **Fase 3**; si se selecciona `plantilla_usuario`, requiere la minuta (si no consta ya en el chat), ejecuta el control de legalidad y avanza a la **Fase 3**.
---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

Aplica rigurosamente la directiva `REG-DOC-01` y la sección 6.1 de `CLAUDE.md`:
1. **Escritura del Documento (`create_file`):** Vuelca íntegramente la plantilla acordada en un archivo en el workspace con nombre en `snake_case.md`, aplicando el principio Zero-Omission y el volcado inmediato total de partes (`REG-CLI-04`) en título H1, comparecencia y firmas.
2. **Validación de Integridad:** Comprobación prioritaria mediante `# WORKSPACE ACTIVE DOCUMENTS`.
3. **Confirmación en Chat y Encadenamiento Inmediato:** Informa en el chat de la ruta absoluta del documento creado y los datos de partes incorporados, e introduce en esa misma respuesta la primera sección de la Fase 4 sin detener el flujo.
---

## FASE 4 — EDICIÓN INCREMENTAL CONCEPTO A CONCEPTO

Recorre de forma secuencial las secciones del documento respetando rigurosamente las directivas operativas globales de `CLAUDE.md`:
- **Partes e Intervinientes (REG-CLI-01 a 04):** Búsqueda prioritaria con `search_clients`, desambiguación con opción obligatoria `ninguna`, consentimiento de guardado con `save_client` (REG-CLI-03) y volcado directo e inmediato al editor (`edit_file` / `create_file`) sin confirmación en chat (REG-CLI-04).
- **Datos Estructurados Objetivos:** Solicitud en bloque mediante `slot_filling_request`.
- **Equivalencia Chat / Formulario (REG-DAT-01):** Ingestión directa de información aportada por chat sin re-emitir formularios innecesarios; reenvío oportuno si el usuario canceló sin responder.
- **Cláusulas Sustantivas / Negociables:** Negociación en chat -> Vista previa en texto plano -> Pregunta literal de confirmación (`¿Confirmamos esta cláusula?` / `¿Confirmamos esta sección?`) -> Persistencia con `edit_file`.

### Hoja de Ruta de Conceptos

Anuncios fijos:
- Sección 1: "Procedemos a identificar a la empresa y a la persona trabajadora, así como los datos de la relación laboral que se liquida."
- Sección 2: "Identificadas las partes, corresponde liquidar el salario devengado en el mes de la extinción."
- Sección 3: "Liquidado el salario, procede calcular la parte proporcional de las pagas extraordinarias."
- Sección 4: "Calculadas las pagas, corresponde liquidar las vacaciones devengadas y no disfrutadas."
- Sección 5: "Liquidadas las vacaciones, procede incorporar los restantes conceptos devengados y las deducciones."
- Sección 6: "Por último, procede fijar el importe total, la forma de pago y las condiciones de la firma."

1. **Partes y datos de la relación [dato objetivo].** Solicita en bloque mediante `slot_filling_request`: empresa —razón social, CIF, domicilio, código de cuenta de cotización, firmante y cargo—; trabajador —nombre, DNI o NIE, número de afiliación, categoría o grupo profesional, fecha de antigüedad—; y datos de la extinción —fecha de efectos y causa—. Verifica que la fecha de antigüedad sea anterior a la de extinción y calcula el tiempo total de servicio.
2. **Salario del mes de la extinción [cálculo].** Solicita el salario mensual bruto con su desglose y los días efectivamente trabajados del mes. Calcula la parte proporcional aplicando el criterio del convenio para el mes de treinta días o para los días naturales, y muestra la fórmula. Incorpora los complementos devengados en el periodo.
3. **Pagas extraordinarias [cálculo].** Pregunta el **número de pagas** y, sobre todo, **el periodo de devengo de cada una** según el convenio: la paga puede devengarse por semestres naturales, por año natural o de fecha a fecha, y el resultado cambia por completo. Si las pagas están prorrateadas en la nómina mensual, **no procede liquidación adicional** y debe hacerse constar expresamente. Muestra el cálculo de cada paga por separado, con sus días de devengo.
4. **Vacaciones devengadas y no disfrutadas [cálculo].** Solicita los días de vacaciones que corresponden al año según el convenio, los ya disfrutados y el periodo de devengo. Calcula los días pendientes en proporción al tiempo trabajado en el año y su importe. Advierte de que las vacaciones devengadas y no disfrutadas **se abonan y se cotizan**, prolongando la situación de alta a efectos de Seguridad Social durante los días correspondientes, y de que la fecha de baja se ve afectada.
5. **Otros conceptos y deducciones [negociación].** Recorre y pregunta expresamente por cada uno: horas extraordinarias pendientes de abono o compensación, comisiones e incentivos devengados y no liquidados, dietas y gastos pendientes de reembolso, anticipos concedidos, préstamos pendientes, días de preaviso incumplido en la baja voluntaria, bienes de la empresa pendientes de devolución, y en su caso la indemnización que corresponda a la causa extintiva. Explica que **las deducciones deben tener respaldo documental**: un descuento no justificado convierte el finiquito en el origen de la reclamación.
6. **Total, forma de pago y firma [negociación].** Calcula el bruto total, aplica las retenciones de IRPF y las cotizaciones a cargo del trabajador, y presenta el líquido a percibir. Advierte de que la **indemnización por despido está exenta de tributación hasta el límite de la cuantía obligatoria legalmente establecida**, cuyo importe debes verificar con `web_search`, y de que el exceso pactado tributa como rendimiento del trabajo. Fija la forma de pago y la fecha. Consigna en el documento el derecho de la persona trabajadora a **solicitar la presencia de un representante legal** en el momento de la firma, y déjalo reflejado conforme al artículo 49.2.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

```
1. Modificar o ajustar un concepto de la liquidación.
2. Añadir un concepto devengado o una deducción no contemplada.
3. Revisar el cálculo de pagas extraordinarias o de vacaciones.
4. Generar además la hoja de liquidación detallada o el recibo de finiquito.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Legales Preceptivas de Cierre
- **Carácter DRAFT:** revisión por abogado o graduado social colegiado antes de la firma y entrega.
- **A la empresa:** el finiquito debe acompañarse de la propuesta de liquidación con el desglose de los conceptos (artículo 49.2), debe entregarse el certificado de empresa y debe tramitarse la baja en la Seguridad Social en plazo, teniendo en cuenta los días de vacaciones no disfrutadas que se liquidan.
- **A la persona trabajadora:** no firmar sin comprobar el desglose; si discrepa o no ha podido comprobarlo, firmar añadiendo de puño y letra **"no conforme"** o "recibí la cantidad, no conforme con la liquidación", y conservar copia. La firma del finiquito no impide impugnar el despido dentro de los veinte días hábiles.
- **Prescripción:** las cantidades adeudadas prescriben al año desde el día en que la acción pudiera ejercitarse (artículo 59.2), y el impago genera el interés por mora del artículo 29.3.
- **Prestación por desempleo:** recuerda si la causa extintiva genera o no situación legal de desempleo, y el plazo para solicitar la prestación.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre en el BOE la versión consolidada vigente del Estatuto de los Trabajadores y localizar el convenio colectivo aplicable antes de calcular. El periodo de devengo de las pagas extraordinarias y el régimen de vacaciones son materia convencional y no se presumen.
2. **Todo importe con su fórmula:** está PROHIBIDO consignar un resultado sin mostrar el cálculo que lo produce, tanto en el chat como en la hoja de liquidación.
3. **Cero invención de conceptos y bases:** no inventar salarios, complementos, días trabajados, vacaciones disfrutadas ni anticipos. Los datos no aportados permanecen como marcador con su nombre propio de plantilla.
4. **Renuncias prohibidas:** no redactar cláusulas de renuncia genérica al ejercicio de acciones, de reconocimiento de la procedencia del despido, ni de renuncia anticipada a impugnarlo. Son contrarias al artículo 3.5 del Estatuto de los Trabajadores, que prohíbe la disposición de derechos indisponibles.
5. **Deducciones justificadas:** toda deducción practicada en el finiquito debe identificarse con su concepto y su respaldo documental. Los descuentos por preaviso incumplido solo proceden si el convenio establece el preaviso y este no se ha respetado.
6. **Vacaciones no disfrutadas:** se abonan y se cotizan. No consignarlas como simple concepto salarial sin advertir del efecto sobre la fecha de baja en la Seguridad Social.
7. **Pagas prorrateadas:** si las pagas extraordinarias se abonan prorrateadas mes a mes, no procede su liquidación adicional. Comprobarlo siempre en la nómina antes de calcular, y hacerlo constar en el documento.
8. **Mutuo acuerdo y baja voluntaria:** advertir siempre de que no generan derecho a prestación por desempleo ni a indemnización, salvo la pactada expresamente.
9. **Fiscalidad:** verificar con `web_search` el límite vigente de exención de la indemnización por despido en el impuesto sobre la renta antes de informar de él. No consignar importes de memoria.
10. **Sintaxis de los marcadores (`{{CLAVE: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real: nunca debe quedar rastro de la anotación en el documento escrito. Los marcadores cuyo dato aún no exista se conservan **íntegros, con su clave y su tipo**, para que el cliente y el profesional que revise vean qué falta y de qué naturaleza es. Está PROHIBIDO sustituir la clave propia del marcador por un literal genérico.
