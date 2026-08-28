# Derecho Civil

Plugin de GravitonAI para la generacion de documentos de derecho civil espanol, verificando siempre la version consolidada vigente en el BOE: arrendamiento urbano, proceso monitorio, juicio ordinario y desahucios.

---

## Que hace

- Genera contratos de arrendamiento de vivienda habitual entre arrendador y arrendatario.
- Genera contratos de arrendamiento de local de negocio / uso distinto de vivienda.
- Adapta el contrato segun la naturaleza de las partes (persona fisica o juridica).
- Aplica la normativa vigente verificando siempre la ultima version consolidada de la LAU en el BOE antes de redactar.
- Advierte sobre zonas de mercado residencial tensionado y aplica las limitaciones de renta correspondientes (Art. 17.6 y 17.7 LAU, Ley 12/2023).
- Genera clausulas conformes a la LAU e indica cuales son imperativas y cuales dispositivas.
- Genera peticiones de proceso monitorio para reclamar deudas dinerarias (arts. 812-818 LEC), con opcion de burofax de requerimiento previo y variante para rentas de arrendamiento impagadas.
- Genera demandas de desahucio (falta de pago con acumulacion de rentas, expiracion de plazo o precario).
- Prepara el juicio ordinario civil de principio a fin (admisibilidad, demanda, audiencia previa, prueba y conclusiones).

## Que NO hace

- No revisa contratos existentes (para eso, crear una skill `revisar-contrato-arrendamiento`).
- No cubre arrendamientos de finca rustica, viviendas turisticas, viviendas militares ni porteros/guardas.
- No tramita el deposito de fianza ante el organismo autonomico.
- No da opinion juridica concreta; el output siempre es un DRAFT para revision por abogado.
- No reemplaza la firma ante notario ni la inscripcion en el Registro de la Propiedad.

---

## Skills

### `arrendamiento-urbano`

Genera un contrato de arrendamiento urbano completo a partir de los datos recogidos al usuario.

Invocacion: `/derecho-civil:arrendamiento-urbano`

Inputs requeridos:
- Tipo de inmueble (vivienda / local de negocio)
- Datos del arrendador (nombre/razon social, NIF/CIF, domicilio, naturaleza: persona fisica o juridica)
- Datos del arrendatario (nombre/razon social, NIF/CIF, domicilio, naturaleza: persona fisica o juridica)
- Datos del inmueble (direccion completa, referencia catastral, descripcion, comunidad autonoma, municipio)
- Renta mensual pactada
- Duracion pactada (o "minimo legal")
- Fianza (o "segun ley")
- Fecha de inicio del contrato

Output: contrato completo en markdown, DRAFT, listo para revision por abogado.

### `monitorio`

Genera la peticion inicial de proceso monitorio para reclamar una deuda dineraria liquida, vencida y exigible (arts. 812-818 LEC), verificando la version vigente en el BOE. Pregunta al usuario el alcance (solo peticion inicial o tambien burofax de requerimiento previo) y el tipo de deuda (rentas de arrendamiento u otra).

Invocacion: `/derecho-civil:monitorio`

Inputs requeridos:
- Alcance (solo peticion inicial / peticion inicial + burofax previo)
- Tipo de deuda (rentas de arrendamiento / otra)
- Datos del acreedor (nombre/razon social, NIF/CIF, domicilio, naturaleza: persona fisica o juridica)
- Datos del deudor (nombre/razon social, NIF/CIF, domicilio o lugar donde pueda ser hallado)
- Origen de la deuda y documentos que la acreditan
- Cuantia (principal e intereses si proceden) y fecha de vencimiento
- Partido judicial del domicilio del deudor
- Si se ha intentado un MASC (si / no)

Output: peticion inicial de monitorio en markdown, DRAFT (y, opcionalmente, burofax de requerimiento previo).

Que NO hace: no redacta la oposicion del deudor ni la demanda de juicio declarativo; no reclama deudas iliquidas o controvertidas; no reclama a Administraciones Publicas; no tramita el desahucio (para recuperar la posesion, valorar el juicio de desahucio).

### `desahucio`

Genera la demanda de juicio verbal de desahucio de finca urbana en tres supuestos: falta de pago de rentas (con opcion de acumular la reclamacion de rentas debidas), expiracion del plazo contractual y precario. Aplica la LEC (Art. 250.1, 437-440, enervacion del Art. 22.4) y el Art. 27 LAU.

Invocacion: `/derecho-civil:desahucio`

Inputs requeridos: supuesto (falta de pago / expiracion / precario); si se acumula la reclamacion de rentas; datos del arrendador y del arrendatario; datos del inmueble y del contrato; rentas debidas y periodos; si hubo requerimiento previo; comunidad autonoma y municipio.

Output: demanda de desahucio en markdown, DRAFT, segun el supuesto.

Que NO hace: no cubre la tutela sumaria frente a okupacion ilegal (Art. 250.1.4), finca rustica ni ejecucion hipotecaria; no redacta la oposicion del demandado.

### `juicio-ordinario`

Prepara de principio a fin un juicio ordinario civil (cuantia superior a 15.000 euros o materia del Art. 249.1 LEC): intake del caso, checklist de admisibilidad (cuantia, competencia, postulacion, MASC), demanda del Art. 399, guion de audiencia previa (Arts. 414-430), proposicion de prueba (Art. 429) y minuta de conclusiones (Art. 433).

Invocacion: `/derecho-civil:juicio-ordinario`

Inputs requeridos: fase (o ciclo completo); materia y via (por materia o por cuantia); datos del actor y del demandado; hechos; cuantia y su justificacion; documentos y periciales; partido judicial; postulacion (abogado y procurador); si se intento MASC.

Output: segun la fase, checklist de admisibilidad, demanda, guion de audiencia previa, proposicion de prueba y/o minuta de conclusiones, en markdown, DRAFT.

Que NO hace: no cubre asuntos de juicio verbal (por materia o cuantia igual o inferior a 15.000 euros), procesos especiales, ni la contestacion, reconvencion o recursos del demandado.

### `convenio-regulador`

Genera el convenio regulador de separacion o divorcio de mutuo acuerdo (Art. 90 CC) y, para la via judicial, la demanda conjunta (Art. 777 LEC). Determina la via (judicial con Ministerio Fiscal si hay hijos menores o con discapacidad dependientes; notarial o ante Letrado de la Administracion de Justicia si no los hay).

Invocacion: `/derecho-civil:convenio-regulador`

Output: convenio regulador en markdown, DRAFT (y, opcionalmente, demanda de mutuo acuerdo).

### `particion-herencia`

Genera el cuaderno particional o escritura de aceptacion y particion (inventario, avaluo, liquidacion y adjudicaciones, con respeto de la legitima) y el documento de aceptacion de herencia, para sucesion testada o intestada. Advierte del Impuesto de Sucesiones (autonomico) y la plusvalia municipal.

Invocacion: `/derecho-civil:particion-herencia`

Output: cuaderno particional en markdown, DRAFT (y, opcionalmente, aceptacion de herencia).

### `reclamacion-clausulas-abusivas`

Genera la reclamacion extrajudicial y/o la demanda de nulidad de clausula abusiva con restitucion de cantidades, en contratos con consumidores (TRLGDCU, LCGC, Directiva 93/13). Verifica la jurisprudencia reciente del TJUE y del Tribunal Supremo.

Invocacion: `/derecho-civil:reclamacion-clausulas-abusivas`

Output: reclamacion extrajudicial y/o demanda de nulidad con restitucion, en markdown, DRAFT.

---

## Alcance del plugin

Este plugin cubre documentos JURIDICOS de derecho civil (contratos, demandas, reclamaciones). Los TRAMITES administrativos ante organismos (DGT, Hacienda, Seguridad Social, registros, extranjeria) se ubicaran en un futuro plugin `gestoria`.

---

## Dependencias

### Tools requeridas

| ID | Uso |
|---|---|
| `io.gravitonai.tools.read_file` | Lectura y verificación de documentos en el workspace |
| `io.gravitonai.tools.create_file` | Creación inicial de documentos en el workspace |
| `io.gravitonai.tools.edit_file` | Edición incremental de cláusulas y secciones en el workspace |
| `io.gravitonai.tools.web_search` | Verificación normativa en el BOE y consulta autonómica |
| `io.gravitonai.tools.human_in_the_loop_request` | Formulario interactivo con opciones (single/multi-select) y texto libre |
| `io.gravitonai.tools.restricted_human_in_the_loop_request` | Formulario con opciones cerradas para confirmaciones y enrutamiento |
| `io.gravitonai.tools.slot_filling_request` | Formulario de captura de datos en lotes (*batch slot-filling*) con campos de texto libre |

### Servidores MCP

Ninguno.

---

## Instalacion

```
/plugin marketplace add ./derecho-civil
```

---

## Tuning

- Jurisdiccion por defecto: en `CLAUDE.md`, campo "Jurisdiccion por defecto".
- Clausulas adicionales habituales del despacho: agregar en `skills/arrendamiento-urbano/references/` como nuevo archivo de referencia y referenciar desde `SKILL.md`.
- Plantillas personalizadas: editar `skills/arrendamiento-urbano/assets/template-contrato-arrendamiento-vivienda.md` y `template-contrato-arrendamiento-local.md`.
