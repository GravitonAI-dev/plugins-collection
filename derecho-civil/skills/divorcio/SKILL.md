---
name: divorcio
description: >
  Genera los documentos de la separacion o el divorcio en Espana, en sus tres vias: (1) MUTUO ACUERDO
  judicial — convenio regulador conforme al articulo 90 del Codigo Civil y, si se desea, demanda
  conjunta del articulo 777 de la LEC (con intervencion del Ministerio Fiscal si hay hijos menores o
  mayores con discapacidad dependientes); (2) MUTUO ACUERDO notarial o ante el Letrado de la
  Administracion de Justicia — convenio regulador para su otorgamiento en escritura publica (arts. 82
  y 87 CC y art. 54 Ley del Notariado; solo sin hijos menores ni dependientes); y (3) CONTENCIOSO —
  demanda de separacion o divorcio del articulo 770 de la LEC con las medidas definitivas de los
  articulos 91 a 97 del Codigo Civil y acreditacion del intento de MASC (LO 1/2025). Verifica la
  version vigente de las normas en el BOE antes de redactar. NO usar para nulidad matrimonial,
  modificacion de medidas ya acordadas, ejecucion de convenios incumplidos, parejas de hecho, ni
  cuando existan indicios de violencia de genero o domestica (en ese caso se detiene y escala).
when_to_use: |
  - El usuario quiere divorciarse o separarse, de mutuo acuerdo o sin acuerdo con su conyuge.
  - El usuario pide un convenio regulador, una demanda de divorcio o separacion (de mutuo acuerdo o
    contenciosa), o pregunta por la via notarial del divorcio.
  - El usuario necesita pactar o solicitar custodia, visitas, pension de alimentos, uso de la
    vivienda o pension compensatoria dentro de una ruptura matrimonial.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - modalidad: mutuo acuerdo / contencioso
  - tipo_ruptura: divorcio / separacion
  - hijos: existencia de hijos menores no emancipados o mayores con discapacidad dependientes (si / no)
  - via: judicial / notarial (solo mutuo acuerdo sin hijos menores ni dependientes)
  - alcance: solo convenio regulador / convenio + demanda de mutuo acuerdo (solo via judicial de mutuo acuerdo)
  - datos_conyuges: nombre, DNI, domicilio de cada conyuge
  - datos_hijos: nombre y fecha de nacimiento de cada hijo, si los hay
  - datos_matrimonio: fecha y lugar de celebracion, registro civil, regimen economico
  - custodia_visitas: modalidad de guarda (exclusiva / compartida) y regimen de estancias
  - pension_alimentos: importe, dia de pago, cuenta, actualizacion y gastos extraordinarios
  - vivienda_familiar: direccion, titularidad y atribucion del uso
  - liquidacion_regimen: reparto de bienes y deudas comunes, si procede
  - pension_compensatoria: si hay desequilibrio, importe, duracion y forma; o renuncia
  - masc: en contencioso, tipo y fechas del intento de MASC o motivo de imposibilidad
  - medidas_provisionales: en contencioso, si se interesan (art. 773 LEC)
  - partido_judicial: competencia (art. 769 LEC), en las vias judiciales
outputs:
  - convenio_regulador: convenio regulador de separacion o divorcio en markdown, DRAFT
  - demanda_mutuo_acuerdo: opcional, demanda conjunta del Art. 777 LEC en markdown, DRAFT
  - demanda_contenciosa: demanda de separacion o divorcio del Art. 770 LEC en markdown, DRAFT
references:
  - references/cc-convenio-regulador-art90.md
  - references/cc-divorcio-separacion-art81-87.md
  - references/cc-medidas-custodia-alimentos-arts92-97.md
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/lec-proceso-contencioso-arts770-774.md
  - references/lec-proceso-mutuo-acuerdo-art777.md
assets:
  - assets/template-convenio-regulador.md
  - assets/template-demanda-divorcio-contencioso.md
  - assets/template-demanda-divorcio-mutuo-acuerdo.md
---

# Generar Convenio Regulador y Demandas de Separacion o Divorcio

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

Para garantizar un enrutamiento determinista y el cumplimiento normativo riguroso, el asistente resuelve y mantiene internamente en memoria los vectores de estado de la operación (V1 a V4) y el origen de la plantilla (V5).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`, `V4`, `V5`) y los resúmenes de validación con marcas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

Tu primer objetivo es clasificar con precisión la naturaleza del caso y fijar los vectores deterministas de estado.

### 1.1 Escucha Activa Previa
Antes de abrir formularios interactivos o hacer preguntas, analiza el mensaje inicial del usuario y la documentación aportada:
- Si el mensaje ya especifica inequívocamente los vectores de la operación, asígnalos de forma inmediata y silenciosa en memoria y pasa a la **Fase 2**.
- Si restan vectores por definir, no formules preguntas abiertas en turnos sucesivos: presenta el formulario estructurado interactivo mediante la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Presenta al usuario las opciones estructuradas para resolver los vectores pendientes:
```json
{
  "type": "object",
  "properties": {
    "modalidad_divorcio": {
      "type": "string",
      "description": "Modalidad de tramitaci\u00f3n (V1)",
      "enum": [
        "mutuo_acuerdo_judicial",
        "mutuo_acuerdo_notarial",
        "contencioso"
      ]
    },
    "tipo_ruptura": {
      "type": "string",
      "description": "Tipo de disoluci\u00f3n (V2)",
      "enum": [
        "divorcio",
        "separacion"
      ]
    },
    "hijos_menores": {
      "type": "string",
      "description": "Existencia de hijos (V3)",
      "enum": [
        "con_hijos_menores",
        "con_hijos_mayores",
        "sin_hijos"
      ]
    },
    "vivienda_y_patrimonio": {
      "type": "string",
      "description": "Uso de la vivienda y liquidaci\u00f3n patrimonial (V4)",
      "enum": [
        "atribucion_vivienda",
        "sin_atribucion_exclusiva"
      ]
    }
  },
  "required": [
    "modalidad_divorcio",
    "tipo_ruptura"
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores necesarios, evalua:
- Si [V1 = Contencioso] -> Plantilla a usar: `assets/template-demanda-divorcio-contencioso.md`. V4 y V5 no aplican. No se genera convenio regulador (es propio del mutuo acuerdo).
- Si [V1 = Mutuo acuerdo] y [V3 = Si] -> Via judicial obligatoria con Ministerio Fiscal. Resolver V5. Plantillas: `assets/template-convenio-regulador.md` y, si V5 = 2, ademas `assets/template-demanda-divorcio-mutuo-acuerdo.md`.
- Si [V1 = Mutuo acuerdo] y [V3 = No] y [V4 = Notarial] -> Plantilla a usar: `assets/template-convenio-regulador.md` (la escritura la otorga el notario; no se genera demanda). V5 no aplica.
- Si [V1 = Mutuo acuerdo] y [V3 = No] y [V4 = Judicial] -> Resolver V5. Plantillas: `assets/template-convenio-regulador.md` y, si V5 = 2, ademas `assets/template-demanda-divorcio-mutuo-acuerdo.md`.
- Si en cualquier momento hay indicios de violencia de genero o domestica -> Deten el proceso (Guardrail 3). No crees documento.

---

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 81 a 97 del Código Civil (separación, divorcio, medidas paternofiliales, pensión de alimentos y pensión compensatoria), y Arts. 769, 770 y 777 de la Ley de Enjuiciamiento Civil (LEC).
2. **Orientación Legal del Caso:**
A diferencia de los Puntos 1 y 2, esta seccion **es visible** para el usuario. Tras completar la verificacion normativa (Punto 2), en un unico mensaje:

**3.1 — Informa la norma aplicable y las consecuencias de la ruta.** Con registro formal (usted, tono de abogado), indica que ley y que articulos concretos aplican al caso ya clasificado, con la version vigente verificada, e incluye SIEMPRE el enlace al BOE consultado. Ademas, segun la ruta:
- Con hijos menores o dependientes (mutuo acuerdo): informar de que la via es judicial y de que el Ministerio Fiscal informara sobre las medidas que afecten a los hijos (Ley 1/2000, de Enjuiciamiento Civil, articulo 777.5).
- Via notarial: informar de que la escritura se otorga ante el notario del ultimo domicilio comun o del domicilio de cualquiera de los solicitantes, con asistencia letrada preceptiva (Ley del Notariado, articulo 54), y de que los hijos mayores sin ingresos que convivan en el domicilio deberan consentir las medidas que les afecten (Codigo Civil, articulo 82).
- Contencioso: informar del requisito de acreditar el intento previo de un medio adecuado de solucion de controversias (Ley Organica 1/2025, articulo 5) y de la posibilidad de solicitar medidas provisionales (Ley de Enjuiciamiento Civil, articulos 771 y 773).

Ejemplo (ruta mutuo acuerdo judicial con hijos): "Al presente caso le resulta de aplicacion el Codigo Civil, en concreto los articulos 81 y 86 (divorcio de mutuo acuerdo y plazo de tres meses) y 90 (contenido del convenio regulador), y la Ley 1/2000, de Enjuiciamiento Civil, articulo 777, en su version consolidada vigente verificada hoy. Al existir hijos menores, la via es judicial y el Ministerio Fiscal informara sobre las medidas que les afecten. Puede consultar los textos oficiales en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"

**3.2 — Ofrece la plantilla o pide el documento propio.** En el mismo mensaje, informa de que se dispone de una plantilla del sistema, revisada por nuestros abogados y colaboradores, basada en esa normativa, y pregunta cual usar como base (alternativas numeradas):

"¿Que documento desea utilizar como base?
1. La plantilla del sistema, revisada por nuestros abogados y colaboradores
2. Adjuntar su propio documento"

**3.3 — Enrutamiento segun la respuesta:**
- Si elige la plantilla del sistema -> continuar con el Punto 4 usando el asset o assets del Punto 1.
- Si elige adjuntar su propio documento -> pedirle que lo adjunte o pegue su contenido, leerlo con `Read`, y usarlo como documento base en el Punto 4 en lugar del asset. Se le siguen aplicando los mismos guardrails (interes del menor, extremos del Art. 90, alimentos no renunciables, MASC en contencioso): si el documento adjuntado los incumple, adviertelo antes de continuar.

---
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-convenio-regulador.md`).
4. **Pregunta Explícita al Usuario (Vía Chat):** Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación de V5 (Origen Plantilla) y Manejo de la Elección
* **Si `[V5 = plantilla_sistema]` (El usuario acepta la plantilla propuesta):**
  Toma el texto íntegro de la plantilla correspondiente directamente desde el catálogo del prompt y procede de inmediato a la **Fase 3**.
* **Si `[V5 = plantilla_usuario]` (El usuario aporta su propia minuta adjuntando un documento o pegando texto):**
  1. Accede al contenido del adjunto desde `<attached_documents>` o el mensaje del usuario.
  2. **Guardrail de Verificación Legal:** Analiza el texto aportado. Si contiene cláusulas nulas, contrarias a normas imperativas o de imposible cumplimiento, adviértelo expresamente en el chat y propón la redacción legalmente válida.
  3. Adopta la minuta revisada como base y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en un archivo en el workspace con nombre en `snake_case.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos e inserta `{{DATO_FALTANTE}}` para aquellos que deban resolverse durante la redacción.
   - PROHIBIDO dejar archivos en blanco, crear resúmenes o esquemas provisionales.
2. **Validación de Integridad (`read_file`):**
   - Ejecuta inmediatamente `read_file` sobre el archivo recién creado para comprobar que el volcado es íntegro y que el archivo existe en disco.
3. **Confirmación en Chat y Encadenamiento Inmediato:**
   - Informa al usuario de la ruta absoluta del documento creado.
   - En esa **misma respuesta**, introduce la primera sección/cláusula de la **Fase 4** y formula ya su primera pregunta, sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

### Protocolo Obligatorio de Edición
Para cada cláusula o bloque temático del documento, ejecuta estrictamente el siguiente ciclo interactivo:
```
[Pregunta al Usuario] ──> [Vista Previa en texto plano] ──> [¿Confirmamos?] ──> [edit_file + read_file]
```
1. **Pregunta en Chat:** Solicita los datos específicos de la sección.
2. **Vista Previa:** Muestra el texto exacto redactado en texto plano en el chat.
3. **Confirmación:** Consulta al usuario si está conforme o desea algún ajuste.
4. **Persistencia en Disco:** Una vez confirmado, ejecuta `edit_file` con `old_string` y `new_string` exactos, y verifica con `read_file`.

### Hoja de Ruta de Secciones y Cláusulas Condicionales

Recorre secuencialmente la lista que corresponda al documento activo (5-A convenio, 5-B demanda de mutuo acuerdo, 5-C demanda contenciosa). Por cada seccion incompleta, aplica el Ciclo de Edicion Incremental del sistema global (Formular Pregunta -> Mostrar Vista Previa en texto plano -> Pedir Confirmacion -> Tras confirmacion, usar `Edit` en disco). Estas son preguntas de relleno de datos: se piden en prosa natural y el cliente responde con texto libre; solo cuando una pregunta tenga un numero pequeno y cerrado de respuestas (ej. gananciales / separacion de bienes) se ofrecen esas opciones en la misma frase. **Un dato por turno**, salvo la confirmacion agrupada descrita abajo. **Validacion de sentido, no solo de formato:** razona si cada respuesta tiene sentido en el contexto (una fecha de matrimonio futura, un DNI con forma de nombre o un importe absurdo no se escriben en el documento: senala por que no encaja y pide aclaracion).

**Confirmacion agrupada por persona (datos identificativos):** los datos puramente identificativos de una misma persona (nombre, DNI, domicilio de un conyuge; nombre y fecha de nacimiento de un hijo) se preguntan igualmente uno por turno, pero SIN vista previa ni `Edit` tras cada dato: acumulalos en memoria y, al completar el ultimo dato de esa persona, muestra una unica vista previa con todos sus datos juntos, pide una unica confirmacion conjunta ("¿Confirmamos estos datos?") y aplica entonces un solo `Edit`. Esta excepcion NO se aplica a las clausulas de negociacion, que se confirman una por una.

**Dialogo y acuerdo en las clausulas de negociacion:** las secciones marcadas como (NEGOCIACION) implican una decision con consecuencias legales. En ellas NO te limites a registrar el valor que de el cliente: primero explica en el chat, de forma breve y con base en `references/cc-medidas-custodia-alimentos-arts92-97.md`, el regimen legal por defecto y las consecuencias de cada opcion, y solo despues formula la pregunta. Confirma que el cliente entiende y esta de acuerdo antes de escribir. Nunca registres un pacto danoso para los hijos o gravemente perjudicial para un conyuge (Art. 90.2 CC): advierte y propon alternativa.

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion y antes de la primera pregunta de la siguiente, anade en el mismo mensaje el anuncio fijo de esa seccion (tono de abogado) y, a continuacion, la pregunta. No pidas permiso para pasar de seccion. Los anuncios nombran la seccion SUSTANTIVA del documento, nunca la mecanica interna.

### 5-A. Convenio regulador (`convenio-regulador.md`)

Los marcadores `{{numero_clausula_...}}` (vivienda, liquidacion, compensatoria, cargas, aprobacion) se resuelven como el ordinal en letras (CUARTA, QUINTA...) que corresponda a la posicion real de esa clausula entre las que estan efectivamente presentes en el documento en ese momento: cuenta solo las clausulas numeradas ya escritas por encima (custodia/visitas/alimentos solo cuentan si V3 = Si; la de animales de compania solo si existen). Como las secciones se recorren en el orden fijo de esta lista, al llegar al turno de cada clausula ya se sabe cuantas la preceden: resuelvela en ese momento, sin dejar el marcador sin resolver ni renumerar clausulas ya escritas.

Anuncios fijos y secciones:

1. **Conyuges (dato objetivo, confirmacion agrupada por conyuge).** Anuncio de apertura: "Procedemos a la identificacion de ambos conyuges." Sub-apartados, uno por turno: (a) nombre completo del primer conyuge; (b) su DNI o NIE; (c) su domicilio actual -> confirmacion agrupada del primer conyuge; (d) nombre completo del segundo conyuge; (e) su DNI o NIE; (f) su domicilio actual -> confirmacion agrupada del segundo conyuge.
2. **Matrimonio (dato objetivo).** Anuncio: "Identificados los conyuges, pasamos a los datos del matrimonio." (a) fecha y lugar de celebracion; (b) registro civil de inscripcion; (c) regimen economico (gananciales / separacion de bienes — opciones cerradas en la misma frase; si el matrimonio se rige por derecho foral, aplicar la fila correspondiente de Escalacion).
3. **Hijos (solo si V3 = Si; dato objetivo, confirmacion agrupada del bloque).** Anuncio: "Corresponde ahora identificar a los hijos comunes." Por cada hijo, nombre y fecha de nacimiento (un hijo por turno). Con menores, pide SOLO los datos imprescindibles para el convenio; no recabes datos adicionales de menores. Confirmacion agrupada de todos los hijos al terminar.
4. **Cuidado de los hijos: custodia y visitas (solo si V3 = Si; NEGOCIACION).** Anuncio: "Pasamos a la primera de las medidas: la guarda y custodia de los hijos y el regimen de estancias." Explica antes de preguntar: patria potestad normalmente conjunta; custodia compartida (exige acuerdo de ambos, Art. 92.5 CC) frente a exclusiva con regimen de visitas para el otro progenitor (Art. 94 CC: contenido habitual — fines de semana alternos, tardes entre semana, mitad de vacaciones); el criterio rector es el interes superior del menor y el Ministerio Fiscal informara. Despues pregunta la modalidad y, en turno aparte, el detalle del regimen de estancias y el lugar de entregas y recogidas.
5. **Pension de alimentos (solo si V3 = Si; NEGOCIACION).** Anuncio: "Fijada la custodia, corresponde determinar la pension de alimentos de los hijos." Explica antes de preguntar: concepto y proporcionalidad (Arts. 93, 142 y 146 CC), la referencia orientadora de las tablas del CGPJ (https://www.poderjudicial.es/cgpj/es/Servicios/Utilidades/Calculo-de-pensiones-alimenticias/ — orientadoras, no vinculantes), y que una pension inexistente o irrisoria no seria aprobada (Art. 90.2 CC). El asset tiene una variante de esta clausula para custodia exclusiva (un progenitor paga al otro) y otra para custodia compartida (fondo comun o compensacion por la diferencia de ingresos): usa la que corresponda segun lo ya resuelto en el punto 4. Despues, en turnos separados: importe mensual por hijo (o compensacion, si la custodia es compartida); dia de pago y cuenta; actualizacion (IPC por defecto); reparto de gastos extraordinarios (50 % por defecto).
6. **Animales de compania (NEGOCIACION, condicional).** Anuncio: "Procede determinar, si los hay, el destino de los animales de compania." Pregunta si existen (si / no en la misma frase). Si no existen, omite la clausula sin dejar rastro. Si existen, explica el Art. 90.1.b) bis CC (destino, reparto de tiempos y cargas segun el bienestar del animal) e inserta una clausula adicional numerada, siguiendo el estilo del asset, con el pacto alcanzado.
7. **Vivienda familiar (NEGOCIACION).** Anuncio: "Corresponde ahora la atribucion del uso de la vivienda familiar." Explica antes de preguntar el regimen por defecto del Art. 96 CC: con hijos menores, el uso corresponde a estos y al conyuge en cuya compania queden hasta su mayoria de edad; sin hijos, cabe atribuirlo temporalmente al conyuge no titular si su interes es el mas necesitado de proteccion. Despues, en turnos separados: direccion; titularidad (comun / privativa / arrendada); a quien se atribuye el uso y por que plazo o condicion.
8. **Liquidacion del regimen economico (NEGOCIACION).** Anuncio: "Pasamos a la liquidacion del regimen economico del matrimonio." Segun el regimen del punto 2: en gananciales, preguntar si liquidan en el propio convenio (relacion de bienes y deudas y su adjudicacion) o lo aplazan; en separacion de bienes, preguntar si existen bienes en proindiviso y su reparto. Si el patrimonio es complejo, aplicar el Guardrail 10 antes de redactar.
9. **Pension compensatoria (NEGOCIACION).** Anuncio: "Corresponde ahora valorar la pension compensatoria." Explica antes de preguntar: no es automatica — solo procede si la ruptura produce desequilibrio economico a uno de los conyuges (Art. 97 CC); puede ser temporal, indefinida o prestacion unica; si ninguno la reclama, se hace constar la renuncia reciproca. Despues pregunta si existe desequilibrio y, en su caso, en turnos separados: beneficiario e importe; duracion y forma de pago.
10. **Cargas y gastos comunes (NEGOCIACION).** Anuncio: "Por ultimo, el reparto de las cargas y gastos comunes pendientes." Preguntar el reparto de deudas y cargas comunes (por mitad por defecto).
11. **Cierre del convenio (dato objetivo).** Anuncio: "Cerramos el convenio con el lugar y la fecha de firma." Preguntar lugar y fecha de firma. La clausula de eficacia se resuelve sola con la via ya clasificada (judicial: sometimiento a aprobacion del Juzgado; notarial/LAJ: otorgamiento en escritura o decreto), sin preguntar.

### 5-B. Demanda de mutuo acuerdo (`demanda-divorcio-mutuo-acuerdo.md`, solo si V5 = 2)

Al crearla, vuelca sin volver a preguntar todos los datos ya recogidos en 5-A (conyuges, matrimonio, hijos). Secciones pendientes:

1. **Juzgado competente (dato objetivo).** Anuncio: "Pasamos a la demanda: primero, el Juzgado competente." Explica que es competente el Juzgado de Primera Instancia del ultimo domicilio comun o el del domicilio de cualquiera de los solicitantes (Art. 769.2 LEC) y pregunta el partido judicial.
2. **Representacion procesal (dato objetivo, confirmacion agrupada).** Anuncio: "Corresponde identificar la representacion procesal." (a) nombre del procurador; (b) nombre del letrado -> confirmacion agrupada. Si aun no estan designados, cada uno queda con su propio placeholder del asset (p. ej. `{{nombre_procurador}}`, `{{nombre_letrado}}`), nunca ambos como el mismo `{{DATO_FALTANTE}}`.
3. **Cierre (dato objetivo).** Anuncio: "Cerramos la demanda con el lugar y la fecha." Preguntar lugar y fecha. La relacion de documentos (certificacion de matrimonio, certificaciones de nacimiento si hay hijos, convenio firmado) se rellena sola segun la clasificacion; muestrala en la vista previa sin preguntar.

### 5-C. Demanda contenciosa (`demanda-divorcio-contencioso.md`)

1. **Conyuge demandante (dato objetivo, confirmacion agrupada).** Anuncio de apertura: "Procedemos a la identificacion de la parte demandante." (a) nombre completo; (b) DNI o NIE; (c) domicilio -> confirmacion agrupada.
2. **Conyuge demandado (dato objetivo, confirmacion agrupada).** Anuncio: "Identificada la parte demandante, pasamos a la parte demandada." (d) nombre completo; (e) DNI o NIE; (f) domicilio (si se desconoce, queda con su propio placeholder de domicilio del asset, no el generico `{{DATO_FALTANTE}}`, y afecta al MASC: ver seccion 5) -> confirmacion agrupada.
3. **Matrimonio (dato objetivo).** Anuncio: "Pasamos a los datos del matrimonio." (a) fecha y lugar de celebracion; (b) registro civil; (c) regimen economico (gananciales / separacion de bienes).
4. **Hijos (solo si V3 = Si; dato objetivo, confirmacion agrupada del bloque).** Anuncio: "Corresponde identificar a los hijos comunes." Nombre y fecha de nacimiento de cada hijo, uno por turno; solo lo imprescindible; confirmacion agrupada.
5. **Cese de la convivencia e intento de MASC (dato objetivo con advertencia).** Anuncio: "Pasamos a los hechos: el cese de la convivencia y el intento de solucion extrajudicial." Primero pregunta, en un turno, la fecha y circunstancias del cese (sin exigir causa: no es necesaria). Despues explica el requisito de procedibilidad (Art. 5 LO 1/2025: sin acreditar el intento de MASC la demanda puede ser inadmitida) y pregunta si se intento (si / no en la misma frase). Si si: tipo de MASC y fechas de inicio y fin, en turnos separados. Si no y se desconoce el domicilio del demandado: activar la declaracion responsable del Art. 264.4.º LEC. Si no y no concurre imposibilidad: advertir formalmente del riesgo de inadmision y recomendar intentar un MASC antes de presentar; si el cliente decide continuar, dejar el bloque con el placeholder propio de MASC del asset (no el generico `{{DATO_FALTANTE}}`) con la advertencia registrada.
6. **Medidas sobre los hijos (solo si V3 = Si; NEGOCIACION).** Anuncio: "Corresponde ahora concretar las medidas que se solicitaran respecto de los hijos." Explica antes de preguntar (con base en `references/cc-medidas-custodia-alimentos-arts92-97.md`): custodia exclusiva frente a compartida (en contencioso, la compartida a instancia de una sola parte es excepcional, Art. 92.8 CC), regimen de visitas habitual, y pension de alimentos con la referencia de las tablas del CGPJ. Despues, en turnos separados: custodia solicitada; regimen de estancias propuesto; alimentos solicitados (importe, pago, actualizacion, gastos extraordinarios).
7. **Vivienda y pension compensatoria (NEGOCIACION).** Anuncio: "Pasamos al uso de la vivienda familiar y, en su caso, a la pension compensatoria." Explica el Art. 96 CC (regimen por defecto) y el Art. 97 CC (la compensatoria no es automatica: exige desequilibrio). Despues, en turnos separados: direccion de la vivienda y atribucion que se solicita; si se solicita pension compensatoria y, en su caso, importe y duracion. Si hay animales de compania (preguntar si / no), anadir la medida de su destino.
8. **Cargas del matrimonio (NEGOCIACION).** Anuncio: "Corresponde el reparto de las cargas del matrimonio." Preguntar la contribucion que se solicita a las cargas y deudas comunes.
9. **Medidas provisionales (NEGOCIACION).** Anuncio: "Procede decidir si se interesan medidas provisionales durante el proceso." Explica: pueden pedirse en la propia demanda (Art. 773 LEC) para que rijan custodia, alimentos, vivienda y cargas mientras se tramita el pleito. Pregunta si se interesan (si / no). Si si, se activa el OTROSI SEGUNDO en los mismos terminos de las medidas definitivas.
10. **Documentacion economica (dato objetivo, solo si hay medidas patrimoniales).** Anuncio: "Corresponde relacionar la documentacion economica que se acompanara." Explica la regla 1.ª del Art. 770 LEC y pregunta que documentos aportara (declaraciones tributarias, nominas, certificaciones bancarias, titulos de propiedad).
11. **Juzgado, representacion y cierre (dato objetivo; representacion con confirmacion agrupada).** Anuncio: "Cerramos con el Juzgado competente, la representacion procesal y la firma." (a) partido judicial (explicar Art. 769.1 LEC: domicilio conyugal; si residen en partidos distintos, ultimo domicilio del matrimonio o residencia del demandado, a eleccion); (b) nombre del procurador; (c) nombre del letrado -> confirmacion agrupada de la representacion; (d) prueba adicional para el OTROSI PRIMERO (testifical, pericial; si no hay, se deja la documental y el interrogatorio); (e) lugar y fecha.

---

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones del documento, presenta al usuario un menú interactivo:
```
1. Modificar o ajustar una cláusula o sección existente.
2. Añadir una estipulación o pacto adicional a medida.
3. Eliminar contenido opcional o corregir datos de partes/fincas.
4. Revisar la coherencia global y realizar control de calidad final.
5. Dar el documento por finalizado y cerrar la sesión.
```
### Advertencias Legales Preceptivas de Cierre:
Al dar por finalizado el documento, emite siempre las siguientes advertencias:
- **Carácter DRAFT:** El documento generado es un borrador profesional que debe ser revisado por un abogado colegiado antes de su firma o presentación procesal.
- **Obligaciones Fiscales y Plazos:** Recuerda los plazos de liquidación de tributos (ITP/AJD o Plusvalía municipal en 30 días hábiles) cuando proceda.
- **Elevación a Instrumento Público:** Recuerda que para la inscripción en el Registro de la Propiedad o Mercantil, o para su ejecución forzosa directa, es necesario el otorgamiento ante Notario público.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre el Codigo Civil y la LEC en el BOE antes de redactar. Sin verificacion, no proceder.
2. Verificar siempre la versión consolidada vigente de la norma en el BOE antes de redactar. Si se detectan cambios normativos, aplicar la redacción vigente en el documento a generar en el workspace sin usar versiones desactualizadas.
3. **Violencia de genero o domestica → DETENER SIEMPRE.** Si en cualquier momento del flujo (clasificacion, edicion incremental o conversacion libre) aparecen indicios de violencia de genero o domestica entre los conyuges o hacia los hijos, detener la generacion de inmediato, advertir y escalar via derivación formal: la competencia pasa a la Seccion de Violencia sobre la Mujer (Art. 89.6 y 89.7 LOPJ, redaccion LO 1/2025; Art. 44 LO 1/2004), esta vedada la utilizacion de los MASC y de la mediacion (Art. 89.9 LOPJ), no procede la custodia compartida (Art. 92.7 CC) y este flujo no es aplicable. No citar el antiguo Art. 87 ter LOPJ: fue suprimido por la LO 1/2025.
4. El mutuo acuerdo exige la conformidad de ambos conyuges y el transcurso de tres meses desde el matrimonio (Arts. 81 y 86 CC; la excepcion por riesgo del Art. 81 no se tramita por esta via: escalar). Si no hay acuerdo, la via es la contenciosa, que esta skill tambien cubre.
5. Con hijos menores no emancipados o hijos mayores con discapacidad y medidas de apoyo atribuidas a sus progenitores, el mutuo acuerdo es SIEMPRE judicial, con intervencion del Ministerio Fiscal (Arts. 81 CC y 777.5 LEC). No proponer nunca la via notarial en ese caso. Los asuntos con menores se tratan con especial cautela: el interes superior del menor prevalece sobre cualquier pacto y ningun acuerdo danoso para los hijos sera aprobado (Art. 90.2 CC).
6. Sin hijos menores ni dependientes, informar de que cabe la via notarial o ante el Letrado de la Administracion de Justicia (Arts. 82 y 87 CC; Art. 54 Ley del Notariado): mas agil, con asistencia letrada preceptiva y ante el notario del ultimo domicilio comun o del domicilio o residencia de cualquiera de los solicitantes.
7. En el contencioso, advertir del requisito de procedibilidad: acreditar el intento previo de un MASC (Art. 5 LO 1/2025 y Art. 264.4.º LEC); sin el, la demanda puede ser inadmitida. La pension de alimentos de los hijos menores no es renunciable ni negociable a la baja hasta ser irrisoria.
8. El convenio debe cubrir todos los extremos aplicables del Art. 90.1 CC (incluido el destino de los animales de compania si los hay). Los no aplicables se omiten con mencion breve de que no proceden; no dejar clausulas vacias.
9. Los datos faltantes conservan el nombre propio del placeholder del asset (p. ej. `{{fecha_cese_convivencia}}`, `{{domicilio_conyuge_demandado}}`); usa el marcador generico `{{DATO_FALTANTE}}` solo para un hueco suelto dentro de una frase ya redactada que no tenga placeholder propio. Nunca generes dos `{{DATO_FALTANTE}}` en el mismo documento: al repetirse el mismo texto literal, `Edit` ya no puede localizar uno sin el otro por `oldString` unico. Nunca inventar datos, importes, fechas, la existencia o identidad de hijos, ni jurisprudencia. Nunca afirmar que el convenio esta aprobado: solo lo aprueba el juez por sentencia, el LAJ por decreto o se formaliza ante notario.
10. Si el regimen economico es complejo (empresas, inmuebles en varios paises, deudas relevantes), advertir de la conveniencia de asesoramiento especializado y ofrecer escalacion antes de redactar la liquidacion.
