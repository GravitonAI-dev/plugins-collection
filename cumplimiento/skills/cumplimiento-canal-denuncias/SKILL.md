---
name: cumplimiento-canal-denuncias
description: >
  Prepara el sistema interno de informacion y canal de denuncias que exige la **Ley 2/2023**,
  reguladora de la proteccion de las personas que informen sobre infracciones normativas y de lucha
  contra la corrupcion, que obliga a las empresas de cincuenta o mas personas trabajadoras a
  implantarlo, designar un responsable del sistema y garantizar la ausencia de represalias, con el
  tratamiento de datos sujeto al **Reglamento (UE) 2016/679** general de proteccion de datos.


  Genera tres documentos: la politica del sistema interno de informacion aprobada por el organo de
  administracion, el procedimiento de gestion de las informaciones recibidas con sus plazos y
  garantias, y el acuerdo de designacion del responsable del sistema con sus funciones.


  Comprueba si la empresa esta obligada segun su plantilla y su actividad, computa el plazo de siete
  dias naturales para acusar recibo y el maximo de tres meses de instruccion, articula la admision de
  informaciones anonimas, fija los plazos de conservacion y advierte de la prohibicion de represalias
  con su inversion de la carga de la prueba.


  NO usar cuando ya se ha recibido una informacion y hay una investigacion interna en curso, ni para
  la defensa ante la Autoridad Independiente de Proteccion del Informante, ni para expedientes
  disciplinarios derivados de una denuncia, que exigen direccion letrada.


  Normas aplicadas, en su texto consolidado:
  [Ley 2/2023](https://www.boe.es/buscar/act.php?id=BOE-A-2023-4513) en el BOE, y
  [Reglamento General de Proteccion de Datos](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R0679)
  en el Diario Oficial de la Union Europea.
when_to_use: |
  - La empresa tiene cincuenta o mas personas trabajadoras y no tiene canal de denuncias.
  - El usuario pregunta si su empresa esta obligada a tener un sistema interno de informacion.
  - La empresa necesita la politica del sistema y el procedimiento de gestion de informaciones.
  - La empresa necesita designar formalmente al responsable del sistema interno de informacion.
  - El usuario pregunta si el canal debe admitir denuncias anonimas y como se protege al informante.
  - El usuario pregunta que plazos tiene para responder a una informacion recibida.
inputs:
  - documento: politica del sistema / procedimiento de gestion / designacion del responsable (V1)
  - obligacion: obligada por plantilla o actividad / implantacion voluntaria (V2)
  - gestion_sistema: gestion interna / gestion externalizada en tercero (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_entidad: razon social, CIF, domicilio, actividad y numero de personas trabajadoras
  - organo_administracion: composicion del organo que aprueba y fecha prevista de aprobacion
  - datos_responsable_sistema: identidad, cargo, dependencia jerarquica y medios asignados
  - canales_habilitados: canales de recepcion (escrito, verbal, reunion presencial) y sus direcciones
  - ambito_subjetivo: personas que pueden informar (personal, becarios, candidatos, contratistas, socios)
  - materias_incluidas: infracciones que pueden comunicarse por el sistema
  - proveedor_externo: identidad del tercero que gestiona el sistema, si aplica
  - plazos_y_conservacion: plazos internos de tramitacion y politica de conservacion de la informacion
  - representacion_legal: forma de consulta a la representacion legal de las personas trabajadoras
outputs:
  - politica_sistema_informacion: politica del sistema interno de informacion, DRAFT
  - procedimiento_gestion_informaciones: procedimiento de gestion de informaciones con plazos y garantias, DRAFT
  - designacion_responsable_sistema: acuerdo de designacion del responsable del sistema y sus funciones, DRAFT
  - checklist_implantacion: obligaciones exigibles, plazos y evidencias de implantacion
references:
  - references/ley-2-2023-sistema-interno-informacion.md
  - references/proteccion-informante-y-datos-personales.md
  - references/estilo-redaccion-cumplimiento.md
assets:
  - assets/template-politica-sistema-interno-informacion.md
  - assets/template-procedimiento-gestion-informaciones.md
  - assets/template-designacion-responsable-sistema.md
---

# Sistema Interno de Información y Canal de Denuncias

> DRAFT — para revisión por un abogado o consultor de cumplimiento antes de su aprobación y publicación. No constituye asesoramiento jurídico vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva y rigurosa a través de un procedimiento estructurado en 5 fases secuenciales para implantar el sistema interno de información.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `politica_sistema` | `procedimiento_gestion` | `designacion_responsable` | `investigacion_en_curso`.
- **V2 (Origen de la Obligación):** `obligada` | `voluntaria`.
- **V3 (Gestión del Sistema):** `gestion_interna` | `gestion_externalizada`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar qué documento se prepara y en qué régimen está la empresa.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un consultor de cumplimiento (de usted), confirmando que vais a preparar el sistema interno de información de la empresa.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca qué documento necesita, cuántas personas trabajadoras tiene la empresa y si el sistema se gestionará internamente o con un tercero, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), el origen de la obligación (`V2`) o la forma de gestión (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar cual de los tres documentos del sistema se prepara.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "politica_sistema", "label": "Política del sistema interno de información, para su aprobación"},
        {"id": "procedimiento_gestion", "label": "Procedimiento de gestión de las informaciones recibidas"},
        {"id": "designacion_responsable", "label": "Designación formal del responsable del sistema"},
        {"id": "investigacion_en_curso", "label": "Ya hemos recibido una denuncia y hay que investigarla"}
      ]
    },
    {
      "id": "obligacion",
      "rationale": "Resolver V2: la obligacion legal impone requisitos que la implantacion voluntaria puede modular.",
      "question": "¿La empresa tiene cincuenta o más personas trabajadoras, o pertenece a un sector con obligación específica?",
      "options": [
        {"id": "obligada", "label": "Sí, está obligada"},
        {"id": "voluntaria", "label": "No, lo implanta voluntariamente"}
      ]
    },
    {
      "id": "gestion_sistema",
      "rationale": "Resolver V3: la gestion por tercero exige contrato de encargado y garantias adicionales de independencia.",
      "question": "¿Quién va a gestionar el canal?",
      "options": [
        {"id": "gestion_interna", "label": "Una persona o unidad de la propia empresa"},
        {"id": "gestion_externalizada", "label": "Un proveedor externo especializado"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `obligacion`
- `V3` — `gestion_sistema`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = investigacion_en_curso`:**
  - **DETENER.** Informar de que la instrucción de una información ya recibida exige dirección letrada: hay plazos de tramitación, deber de preservar la identidad del informante, prohibición de represalias con inversión de la carga de la prueba, y riesgo de nulidad de las medidas que se adopten sin garantías. Derivar a abogado especialista en investigaciones internas. No crear documento.
- **Si `V1 = politica_sistema`:**
  - Plantilla del sistema: `assets/template-politica-sistema-interno-informacion.md`. Proceder a la **Fase 2**.
- **Si `V1 = procedimiento_gestion`:**
  - Plantilla del sistema: `assets/template-procedimiento-gestion-informaciones.md`. Proceder a la **Fase 2**.
- **Si `V1 = designacion_responsable`:**
  - Plantilla del sistema: `assets/template-designacion-responsable-sistema.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina si el documento se redacta como cumplimiento de una obligación legal o como compromiso voluntario, y las advertencias sobre régimen sancionador.
- `V3` no elige plantilla: determina si se incorporan las cláusulas de externalización, con el contrato de encargado del tratamiento y las garantías de independencia del tercero.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `ley-2-2023-sistema-interno-informacion.md`, `proteccion-informante-y-datos-personales.md` y `estilo-redaccion-cumplimiento.md`.
2. Opcionalmente verifica mediante `web_search` el estado y los criterios de la Autoridad Independiente de Protección del Informante y la existencia de autoridad autonómica competente. Aplica la redacción vigente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal, Obligación y Riesgo:**
   - Explicar que el sistema interno de información es el **cauce preferente** de la ley y que su ausencia, cuando la empresa está obligada, constituye infracción con multas de cuantía elevada para la persona jurídica.
   - Explicar los tres pilares: **canal** que admita informaciones escritas y verbales y también **anónimas**, **responsable del sistema** designado por el órgano de administración con independencia y medios, y **procedimiento** con plazos (acuse de recibo en siete días naturales y plazo máximo de instrucción de tres meses, ampliable en casos de especial complejidad).
   - Advertir de la **prohibición de represalias** y de que, si el informante acredita indicios, corresponde a la empresa probar que la medida adoptada tuvo causa distinta y justificada.
   - Advertir de que la política debe aprobarse por el órgano de administración, **previa consulta a la representación legal** de las personas trabajadoras, y publicarse de forma accesible.
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

### Hoja de Ruta de Secciones — RAMA POLÍTICA DEL SISTEMA:

1. **Entidad, obligación y ámbito** *(confirmación agrupada)*: razón social, CIF, domicilio, actividad, número de personas trabajadoras, y determinación expresa de si la implantación es obligatoria o voluntaria.
2. **Compromiso del órgano de administración**: declaración de compromiso con la integridad, con la protección del informante y con la tolerancia cero frente a las represalias.
3. **Ámbito subjetivo**: personas que pueden informar, incluyendo personal propio, personas en formación, quienes hayan cesado en la relación, candidatos en procesos de selección, socios, administradores, contratistas y sus trabajadores.
4. **Materias que pueden comunicarse**: infracciones que integran el ámbito material de la ley, y determinación de si la empresa amplía el canal a otras conductas internas.
5. **Canales y garantía de anonimato**: canales habilitados (escrito, verbal y reunión presencial a solicitud), con la garantía expresa de que se admiten **informaciones anónimas** y de que la identidad del informante no se revelará.
6. **Garantías del informante y prohibición de represalias**: enumeración de las conductas prohibidas como represalia y de las medidas de protección, con mención de la inversión de la carga de la prueba.
7. **Responsable del sistema, aprobación y publicación**: identificación del responsable, órgano y fecha de aprobación, constancia de la consulta previa a la representación legal de las personas trabajadoras, y forma de publicación y difusión accesible.

### Hoja de Ruta de Secciones — RAMA PROCEDIMIENTO DE GESTIÓN:

1. **Objeto, responsable y medios** *(confirmación agrupada)*: identificación del responsable del sistema, medios y recursos asignados, y régimen de sustitución.
2. **Recepción y registro**: canales, forma de registro de las informaciones, libro-registro con acceso restringido, y régimen de las informaciones verbales con su transcripción o grabación previo consentimiento.
3. **Acuse de recibo y admisión a trámite**: plazo de **siete días naturales** para el acuse, salvo que pueda comprometer la confidencialidad; criterios de admisión e inadmisión, con motivación y comunicación al informante.
4. **Instrucción**: actuaciones de comprobación, audiencia de la persona afectada con sus derechos (presunción de inocencia, derecho a ser informada de las acciones u omisiones que se le atribuyen, derecho de defensa), y prohibición de revelar la identidad del informante a la persona afectada.
5. **Plazos y resolución**: plazo máximo de **tres meses** desde el acuse de recibo, ampliable en casos de especial complejidad hasta un máximo adicional de tres meses; conclusiones, medidas propuestas, y remisión al Ministerio Fiscal si los hechos pudieran ser constitutivos de delito.
6. **Protección de datos y conservación**: base de licitud del tratamiento, acceso restringido, supresión de los datos que no resulten necesarios, plazo máximo de conservación de la información en el sistema y régimen de conservación fuera de él cuando sea necesario para acreditar el funcionamiento.
7. **Externalización**: *Condicional `V3 = gestion_externalizada`:* identificación del tercero, garantías de independencia y confidencialidad, y contrato de encargado del tratamiento.

### Hoja de Ruta de Secciones — RAMA DESIGNACIÓN DEL RESPONSABLE:

1. **Órgano que designa y entidad** *(confirmación agrupada)*: identificación de la entidad, órgano de administración, fecha del acuerdo y constancia de la consulta previa a la representación legal.
2. **Persona designada y su posición**: identidad, cargo, dependencia jerárquica directa del órgano de administración, y declaración de independencia y ausencia de conflicto de interés.
3. **Funciones**: gestión del sistema, tramitación de las informaciones, comunicación con el informante, propuesta de medidas y elaboración del informe periódico al órgano de administración.
4. **Medios, autonomía y garantías**: medios materiales y personales, autonomía funcional, derecho de acceso a la información necesaria, y garantía de indemnidad de la propia persona designada.
5. **Comunicación a la autoridad y aceptación**: comunicación de la designación a la autoridad independiente competente, aceptación expresa de la persona designada, deber de secreto y régimen de cese y sustitución.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
La documentación del sistema interno de información ha sido generada y actualizada en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección (ámbito, canales, plazos o garantías).
2. Ampliar el ámbito material del canal a otras conductas internas.
3. Preparar el documento complementario del sistema (política, procedimiento o designación).
4. Revisar la coherencia global y realizar control de calidad previo a su aprobación.
5. Dar la documentación por finalizada y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT:** el documento es un borrador preparatorio; debe ser revisado por un profesional antes de su aprobación y publicación.
2. **Aprobación y consulta previa:** la política debe aprobarse por el órgano de administración previa consulta a la representación legal de las personas trabajadoras. Sin esa consulta, la implantación es impugnable.
3. **Publicación y difusión:** el canal debe ser conocido y accesible. Un sistema aprobado y no difundido no cumple, y además impide que la empresa se beneficie de su existencia como prueba de diligencia.
4. **Informaciones anónimas:** el sistema debe permitirlas. Excluirlas es contrario a la ley.
5. **Prohibición de represalias:** cualquier medida desfavorable adoptada en los dos años siguientes a la comunicación se presume represalia, correspondiendo a la empresa acreditar que tuvo causa distinta y justificada. Es el punto de mayor riesgo práctico.
6. **Plazos:** acuse de recibo en siete días naturales y plazo máximo de instrucción de tres meses, ampliable en supuestos de especial complejidad. Superarlos deja al informante habilitado para acudir al canal externo de la autoridad.
7. **Canal externo y protección:** el informante puede acudir directamente a la autoridad independiente competente, y su protección no depende de haber usado antes el canal interno.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias antes de citar plazos, umbrales o importes de sanción. No afirmar que la obligación no aplica sin comprobar plantilla y actividad.
2. **Cero Invención de Datos:** prohibido inventar identidades de responsables, canales, direcciones de correo o composiciones de órganos. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **Prohibido debilitar las garantías:** está prohibido redactar cláusulas que exijan al informante identificarse, que le impongan aportar pruebas como condición de admisión, que permitan revelar su identidad a la persona afectada o que establezcan consecuencias por informar de buena fe.
4. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas o criterios de la autoridad en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
5. **Límites de Alcance:** no instruir investigaciones internas, no redactar expedientes disciplinarios derivados de una información, ni preparar la defensa ante la autoridad, que deben derivarse a letrado.
