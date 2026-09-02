# Derecho Civil

Plugin de GravitonAI para la generacion de documentos de derecho civil espanol, verificando siempre la version consolidada vigente en el BOE antes de redactar. Cubre reclamacion de cantidad (monitorio/verbal/ordinario), ejecucion de titulos, arrendamiento, desahucio, propiedad horizontal, divorcio y modificacion de medidas, herencia, y clausulas abusivas de consumo.

---

## Que hace

- Elige la via correcta de reclamacion de una deuda (monitorio, juicio verbal u ordinario) y genera la peticion o demanda, con opcion de burofax previo (Arts. 812-818, 249-250 LEC).
- Ejecuta forzosamente titulos judiciales, no judiciales (escritura, laudo, acuerdo de mediacion) y pensiones de familia, incluida la designacion de bienes y la investigacion patrimonial (Libro III LEC).
- Genera contratos de arrendamiento de vivienda habitual, temporada, local de negocio y habitacion, y las comunicaciones asociadas (actualizacion de renta, no renovacion, devolucion de fianza), con verificacion de zona de mercado tensionado.
- Genera demandas de desahucio (falta de pago con acumulacion de rentas, expiracion de plazo o precario) y el acuerdo extrajudicial de condonacion con entrega de llaves.
- Genera los documentos de comunidad de propietarios: certificacion y monitorio especial de cuotas, impugnacion de acuerdos de junta y requerimiento de cesacion de actividad molesta (LPH).
- Genera el convenio regulador y la demanda de divorcio o separacion, de mutuo acuerdo o contenciosa, y la demanda de modificacion o extincion de medidas ya fijadas (custodia, alimentos, compensatoria).
- Cubre el ciclo completo de la herencia: aceptacion, renuncia, interpelacion al heredero silente, cuaderno particional y division judicial.
- Prepara el juicio ordinario civil de principio a fin (admisibilidad, demanda, audiencia previa, prueba y conclusiones).
- Genera la reclamacion extrajudicial y la demanda de nulidad de clausulas abusivas de consumo.
- Toda skill se auto-actualiza en cada lanzamiento: verifica la version vigente de su norma en el BOE antes de redactar y reescribe sus propias references/assets si detecta cambios.

## Que NO hace

- No revisa contratos ni escritos ya redactados por terceros.
- No cubre arrendamientos de finca rustica, viviendas turisticas, viviendas militares ni porteros/guardas.
- No tramita el deposito de fianza ante el organismo autonomico ni gestiona el pago de impuestos.
- No cubre la ejecucion hipotecaria ni la oposicion de la parte ejecutada/demandada.
- No da opinion juridica concreta; el output siempre es un DRAFT para revision por abogado colegiado.
- No reemplaza la firma ante notario ni la inscripcion en el Registro de la Propiedad.

---

## Skills

### `derecho-civil-reclamacion-cantidad`

Elige la via de reclamacion de una deuda dineraria (monitorio, verbal u ordinario segun documentacion, cuantia y oposicion) y genera la peticion, demanda u oposicion correspondiente, con burofax previo.

Invocacion: `/derecho-civil:derecho-civil-reclamacion-cantidad`

Output: peticion de monitorio, burofax, demanda de verbal u ordinario, u oposicion al monitorio, en markdown, DRAFT.

### `derecho-civil-ejecucion-titulos`

Ejecuta forzosamente un titulo dinerario: judicial (sentencia, decreto, incluido monitorio firme), no judicial (escritura, laudo, acuerdo de mediacion) o de familia (pensiones), y genera por separado el escrito de embargo/investigacion patrimonial cuando la ejecucion ya esta despachada.

Invocacion: `/derecho-civil:derecho-civil-ejecucion-titulos`

Output: demanda de ejecucion de titulo judicial, no judicial o de familia, o solicitud de embargo/averiguacion patrimonial, en markdown, DRAFT.

Que NO hace: no cubre la ejecucion hipotecaria, la ejecucion provisional ni la oposicion del ejecutado.

### `derecho-civil-arrendamiento`

Genera un contrato de arrendamiento urbano (vivienda habitual, temporada, local o habitacion) y las comunicaciones asociadas al contrato vigente.

Invocacion: `/derecho-civil:derecho-civil-arrendamiento`

Output: contrato de arrendamiento o comunicacion (actualizacion de renta, no renovacion, devolucion de fianza), en markdown, DRAFT.

### `derecho-civil-desahucio`

Genera la demanda de juicio verbal de desahucio (falta de pago con acumulacion de rentas, expiracion del plazo o precario) o el acuerdo extrajudicial de condonacion de rentas a cambio de la entrega de llaves.

Invocacion: `/derecho-civil:derecho-civil-desahucio`

Output: demanda de desahucio segun el supuesto, o acuerdo de condonacion, en markdown, DRAFT.

Que NO hace: no cubre la tutela sumaria frente a ocupacion ilegal (Art. 250.1.4 LEC), finca rustica ni ejecucion hipotecaria; no redacta la oposicion del demandado.

### `derecho-civil-propiedad-horizontal`

Genera la certificacion del acuerdo de liquidacion de deuda y la peticion de monitorio especial de cuotas de comunidad, la demanda de impugnacion de acuerdos de junta y el requerimiento de cesacion de actividad molesta.

Invocacion: `/derecho-civil:derecho-civil-propiedad-horizontal`

Output: certificacion + peticion de monitorio, demanda de impugnacion, o requerimiento de cesacion, en markdown, DRAFT.

### `derecho-civil-juicio-ordinario`

Prepara de principio a fin un juicio ordinario civil (cuantia superior a 15.000 euros o materia del Art. 249.1 LEC): checklist de admisibilidad, demanda, guion de audiencia previa, proposicion de prueba y minuta de conclusiones.

Invocacion: `/derecho-civil:derecho-civil-juicio-ordinario`

Output: segun la fase, checklist de admisibilidad, demanda, guion de audiencia previa, proposicion de prueba y/o minuta de conclusiones, en markdown, DRAFT.

### `derecho-civil-monitorio`

Genera la peticion inicial de proceso monitorio para reclamar una deuda dineraria liquida, vencida y exigible (arts. 812-818 LEC), con opcion de burofax de requerimiento previo.

Invocacion: `/derecho-civil:derecho-civil-monitorio`

Output: peticion inicial de monitorio en markdown, DRAFT (y, opcionalmente, burofax de requerimiento previo).

### `derecho-civil-divorcio`

Genera el convenio regulador de separacion o divorcio de mutuo acuerdo (Art. 90 CC), la demanda conjunta (Art. 777 LEC) o la demanda contenciosa (Art. 770 LEC), y ofrece la via notarial cuando no hay hijos menores ni dependientes.

Invocacion: `/derecho-civil:derecho-civil-divorcio`

Output: convenio regulador, demanda de mutuo acuerdo o demanda contenciosa, en markdown, DRAFT.

### `derecho-civil-modificacion-medidas`

Genera la demanda de modificacion de medidas definitivas ya fijadas (custodia, alimentos, compensatoria, vivienda), consensuada o contenciosa, y la solicitud de extincion de la pension de alimentos, con filtro previo de viabilidad de la alteracion sustancial alegada.

Invocacion: `/derecho-civil:derecho-civil-modificacion-medidas`

Output: demanda de modificacion de medidas o solicitud de extincion de alimentos, en markdown, DRAFT.

Que NO hace: no fija medidas por primera vez; no cubre la ejecucion de pensiones impagadas.

### `derecho-civil-herencia`

Cubre el ciclo completo de la herencia, para sucesion testada o intestada: aceptacion (pura y simple o a beneficio de inventario), renuncia (minuta para escritura notarial, Art. 1008 CC), interpelacion notarial al heredero que no se pronuncia (Art. 1005 CC), cuaderno particional (inventario, avaluo, liquidacion y adjudicaciones, con respeto de la legitima) y solicitud de division judicial a falta de acuerdo (Arts. 782 y ss. LEC). Advierte del Impuesto de Sucesiones (autonomico) y la plusvalia municipal.

Invocacion: `/derecho-civil:derecho-civil-herencia`

Output: segun el caso, aceptacion, renuncia, requerimiento del Art. 1005 CC, cuaderno particional o solicitud de division judicial, en markdown, DRAFT.

### `derecho-civil-reclamacion-clausulas-abusivas`

Genera la reclamacion extrajudicial y/o la demanda de nulidad de clausula abusiva con restitucion de cantidades, en contratos con consumidores (TRLGDCU, LCGC, Directiva 93/13). Verifica la jurisprudencia reciente del TJUE y del Tribunal Supremo.

Invocacion: `/derecho-civil:derecho-civil-reclamacion-clausulas-abusivas`

Output: reclamacion extrajudicial y/o demanda de nulidad con restitucion, en markdown, DRAFT.

---

## Alcance del plugin

Este plugin cubre documentos JURIDICOS de derecho civil (contratos, demandas, reclamaciones). Los TRAMITES administrativos ante organismos (DGT, Hacienda, Seguridad Social, registros, extranjeria) se ubican en el plugin `gestoria`.

---

## Dependencias

### Tools requeridas

| ID | Uso |
|---|---|
| `io.gravitonai.tools.read_document` | Lectura directa de normas en el BOE (verificacion normativa) |
| `io.gravitonai.tools.web_search` | Fallback normativo y consulta de normativa autonomica |
| `io.gravitonai.tools.draft_markdown` | Generacion del documento desde plantilla |

### Tools opcionales

| ID | Uso |
|---|---|
| `io.gravitonai.tools.escalate_to_attorney` | Escalacion a abogado en casos complejos |

### Servidores MCP

Ninguno.

---

## Instalacion

```
/plugin marketplace add ./derecho-civil
```

---

## Tuning

<!-- EDITAR PARA TU EQUIPO: personalizar segun la practica del despacho -->

- Jurisdiccion por defecto: en `CLAUDE.md`, campo "Jurisdiccion por defecto".
- Clausulas adicionales habituales del despacho: agregar en `skills/<skill>/references/` como nuevo archivo de referencia y referenciar desde `SKILL.md`.
- Plantillas personalizadas: editar los assets de la skill correspondiente en `skills/<skill>/assets/`.

---

## Estado de calidad

Las 8 skills creadas o ampliadas en la ultima iteracion (`derecho-civil-reclamacion-cantidad`, `derecho-civil-arrendamiento`, `derecho-civil-divorcio`, `derecho-civil-herencia`, `derecho-civil-desahucio`, `derecho-civil-propiedad-horizontal`, `derecho-civil-modificacion-medidas`, `derecho-civil-ejecucion-titulos`) pasaron un control de calidad en vivo: ejecucion real del procedimiento (no solo revision del `SKILL.md`), verificacion normativa contra el BOE en vivo, y generacion real de documentos con `Write`/`Read`/`Edit`. El proceso encontro y corrigio defectos reales en las 8 skills (ver `test-local/tests/test-derecho-civil-*.md`, seccion "Verificacion en vivo + calidad LLM" de cada una) y tres bugs transversales ya corregidos en las 11 skills del plugin: placeholders genericos duplicados que rompian `Edit`, placeholders con corchete simple en colision con los identificadores de privacidad, y placeholders con texto de ayuda embebido en las llaves. Detalle en `test-local/CATALOGO.md`.
