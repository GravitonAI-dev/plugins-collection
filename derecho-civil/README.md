# Derecho Civil

Plugin de GravitonAI para la generacion de documentos de derecho civil espanol, verificando siempre la version consolidada vigente en el BOE antes de redactar. **19 skills** que cubren reclamacion de cantidad y ejecucion de titulos, contratos entre particulares, arrendamiento, desahucio, compraventa de inmuebles y propiedad horizontal, familia (divorcio, medidas sobre hijos, modificacion de medidas, gananciales y pareja de hecho), sucesiones (herencia y planificacion testamentaria), clausulas abusivas de consumo, responsabilidad civil y medidas de apoyo a personas con discapacidad.

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
- Reclama danos por responsabilidad civil, incluidos los accidentes con vehiculos personales ligeros (patinetes), con seguro obligatorio desde la Ley 5/2025, y responde a la oferta motivada de la aseguradora.
- Genera contratos de arras y de compraventa de vivienda, con advertencia del tanteo y retracto del arrendatario si el inmueble esta alquilado.
- Liquida la sociedad de gananciales, con acuerdo o por via judicial, y fija por primera vez las medidas sobre hijos de progenitores no casados.
- Constituye parejas de hecho y pacta su convivencia o su ruptura, verificando en cada lanzamiento la normativa y el registro de la comunidad autonoma.
- Prepara la minuta del testamento y el checklist de planificacion sucesoria (legitimas, mejora, sustituciones, desheredacion), solo en derecho comun.
- Redacta contratos entre particulares (prestamo, reconocimiento de deuda, comodato, compraventa de mueble) con control de usura.
- Prepara las medidas de apoyo a personas con discapacidad de la Ley 8/2021, tratando la curatela como subsidiaria de la guarda de hecho y de las medidas voluntarias.
- Toda skill se auto-actualiza en cada lanzamiento: verifica la version vigente de su norma en el BOE antes de redactar y reescribe sus propias references/assets si detecta cambios. Las magnitudes que cambian solas (baremo de trafico, IRAV, SMI, interes legal) se consultan en el momento y nunca quedan escritas fijas en la plantilla.

## Que NO hace

- No revisa contratos ni escritos ya redactados por terceros.
- No cubre arrendamientos de finca rustica, viviendas turisticas, viviendas militares ni porteros/guardas.
- No tramita el deposito de fianza ante el organismo autonomico ni gestiona el pago de impuestos.
- No cubre la ejecucion hipotecaria ni la oposicion de la parte ejecutada/demandada.
- No da opinion juridica concreta; el output siempre es un DRAFT para revision por abogado colegiado.
- No reemplaza la firma ante notario ni la inscripcion en el Registro de la Propiedad.

---

## Skills

### `reclamacion-cantidad`

Elige la via de reclamacion de una deuda dineraria (monitorio, verbal u ordinario segun documentacion, cuantia y oposicion) y genera la peticion, demanda u oposicion correspondiente, con burofax previo.

Invocacion: `/derecho-civil:reclamacion-cantidad`

Output: peticion de monitorio, burofax, demanda de verbal u ordinario, u oposicion al monitorio, en markdown, DRAFT.

### `ejecucion-titulos`

Ejecuta forzosamente un titulo dinerario: judicial (sentencia, decreto, incluido monitorio firme), no judicial (escritura, laudo, acuerdo de mediacion) o de familia (pensiones), y genera por separado el escrito de embargo/investigacion patrimonial cuando la ejecucion ya esta despachada.

Invocacion: `/derecho-civil:ejecucion-titulos`

Output: demanda de ejecucion de titulo judicial, no judicial o de familia, o solicitud de embargo/averiguacion patrimonial, en markdown, DRAFT.

Que NO hace: no cubre la ejecucion hipotecaria, la ejecucion provisional ni la oposicion del ejecutado.

### `arrendamiento-urbano`

Genera un contrato de arrendamiento urbano (vivienda habitual, temporada, local o habitacion) y las comunicaciones asociadas al contrato vigente.

Invocacion: `/derecho-civil:arrendamiento-urbano`

Output: contrato de arrendamiento o comunicacion (actualizacion de renta, no renovacion, devolucion de fianza), en markdown, DRAFT.

### `desahucio`

Genera la demanda de juicio verbal de desahucio (falta de pago con acumulacion de rentas, expiracion del plazo o precario) o el acuerdo extrajudicial de condonacion de rentas a cambio de la entrega de llaves.

Invocacion: `/derecho-civil:desahucio`

Output: demanda de desahucio segun el supuesto, o acuerdo de condonacion, en markdown, DRAFT.

Que NO hace: no cubre la tutela sumaria frente a ocupacion ilegal (Art. 250.1.4 LEC), finca rustica ni ejecucion hipotecaria; no redacta la oposicion del demandado.

### `propiedad-horizontal`

Genera la certificacion del acuerdo de liquidacion de deuda y la peticion de monitorio especial de cuotas de comunidad, la demanda de impugnacion de acuerdos de junta y el requerimiento de cesacion de actividad molesta.

Invocacion: `/derecho-civil:propiedad-horizontal`

Output: certificacion + peticion de monitorio, demanda de impugnacion, o requerimiento de cesacion, en markdown, DRAFT.

### `juicio-ordinario`

Prepara de principio a fin un juicio ordinario civil (cuantia superior a 15.000 euros o materia del Art. 249.1 LEC): checklist de admisibilidad, demanda, guion de audiencia previa, proposicion de prueba y minuta de conclusiones.

Invocacion: `/derecho-civil:juicio-ordinario`

Output: segun la fase, checklist de admisibilidad, demanda, guion de audiencia previa, proposicion de prueba y/o minuta de conclusiones, en markdown, DRAFT.

### `monitorio`

Genera la peticion inicial de proceso monitorio para reclamar una deuda dineraria liquida, vencida y exigible (arts. 812-818 LEC), con opcion de burofax de requerimiento previo.

Invocacion: `/derecho-civil:monitorio`

Output: peticion inicial de monitorio en markdown, DRAFT (y, opcionalmente, burofax de requerimiento previo).

### `divorcio`

Genera el convenio regulador de separacion o divorcio de mutuo acuerdo (Art. 90 CC), la demanda conjunta (Art. 777 LEC) o la demanda contenciosa (Art. 770 LEC), y ofrece la via notarial cuando no hay hijos menores ni dependientes.

Invocacion: `/derecho-civil:divorcio`

Output: convenio regulador, demanda de mutuo acuerdo o demanda contenciosa, en markdown, DRAFT.

### `modificacion-medidas`

Genera la demanda de modificacion de medidas definitivas ya fijadas (custodia, alimentos, compensatoria, vivienda), consensuada o contenciosa, y la solicitud de extincion de la pension de alimentos, con filtro previo de viabilidad de la alteracion sustancial alegada.

Invocacion: `/derecho-civil:modificacion-medidas`

Output: demanda de modificacion de medidas o solicitud de extincion de alimentos, en markdown, DRAFT.

Que NO hace: no fija medidas por primera vez; no cubre la ejecucion de pensiones impagadas.

### `herencia`

Cubre el ciclo completo de la herencia, para sucesion testada o intestada: aceptacion (pura y simple o a beneficio de inventario), renuncia (minuta para escritura notarial, Art. 1008 CC), interpelacion notarial al heredero que no se pronuncia (Art. 1005 CC), cuaderno particional (inventario, avaluo, liquidacion y adjudicaciones, con respeto de la legitima) y solicitud de division judicial a falta de acuerdo (Arts. 782 y ss. LEC). Advierte del Impuesto de Sucesiones (autonomico) y la plusvalia municipal.

Invocacion: `/derecho-civil:herencia`

Output: segun el caso, aceptacion, renuncia, requerimiento del Art. 1005 CC, cuaderno particional o solicitud de division judicial, en markdown, DRAFT.

### `reclamacion-clausulas-abusivas`

Genera la reclamacion extrajudicial y/o la demanda de nulidad de clausula abusiva con restitucion de cantidades, en contratos con consumidores (TRLGDCU, LCGC, Directiva 93/13). Verifica la jurisprudencia reciente del TJUE y del Tribunal Supremo.

Invocacion: `/derecho-civil:reclamacion-clausulas-abusivas`

Output: reclamacion extrajudicial y/o demanda de nulidad con restitucion, en markdown, DRAFT.

### `responsabilidad-civil`

Reclama los danos sufridos por culpa de otro, contractual o extracontractual: accidente de trafico con vehiculo a motor o con vehiculo personal ligero (patinete, con seguro obligatorio desde la Ley 5/2025), caida en establecimiento o via publica, vicio constructivo y negligencia profesional. Aplica un filtro de prescripcion bloqueante (un ano en la extracontractual, cinco en la contractual) y verifica en cada lanzamiento las cuantias del baremo del ejercicio en curso, que nunca quedan escritas fijas.

Invocacion: `/derecho-civil:responsabilidad-civil`

Output: reclamacion extrajudicial de danos, demanda de responsabilidad civil o respuesta a la oferta motivada de la aseguradora, en markdown, DRAFT.

### `compraventa-inmueble`

Genera el contrato de arras o senal, el contrato privado de compraventa de vivienda y el requerimiento por incumplimiento. Exige pactar expresamente la clase de arras, porque el silencio juega en contra de quien quiere desistir, y advierte del derecho de tanteo y retracto del arrendatario si el inmueble esta alquilado.

Invocacion: `/derecho-civil:compraventa-inmueble`

Output: contrato de arras, contrato de compraventa o requerimiento de cumplimiento, en markdown, DRAFT.

### `liquidacion-gananciales`

Liquida la sociedad de gananciales, con acuerdo (convenio) o sin el (solicitud judicial de formacion de inventario). Explica la presuncion de ganancialidad, los reintegros entre masas y, sobre todo, que adjudicar la vivienda a un conyuge no libera al otro frente al banco.

Invocacion: `/derecho-civil:liquidacion-gananciales`

Output: propuesta de inventario, convenio de liquidacion o solicitud de formacion de inventario, en markdown, DRAFT.

### `medidas-hijos-no-matrimoniales`

Fija por primera vez la custodia, el regimen de estancias, los alimentos y el uso de la vivienda respecto de hijos de progenitores no casados, de mutuo acuerdo o por via contenciosa. Comprueba antes que la filiacion este determinada respecto de ambos.

Invocacion: `/derecho-civil:medidas-hijos-no-matrimoniales`

Output: pacto de relaciones familiares o demanda de medidas paternofiliales, en markdown, DRAFT.

### `pareja-de-hecho`

Constituye la pareja de hecho, pacta la convivencia o regula la ruptura. Como no existe ley estatal, pregunta la comunidad autonoma y **verifica su normativa y su registro en cada lanzamiento** en lugar de darlos por sabidos. Deja claro que la inscripcion no equipara al matrimonio y que el conviviente no hereda sin testamento.

Invocacion: `/derecho-civil:pareja-de-hecho`

Output: pacto de convivencia, pacto de ruptura o checklist de inscripcion en el registro autonomico, en markdown, DRAFT.

### `testamento-planificacion`

Prepara la minuta del testamento abierto y el checklist de planificacion sucesoria: institucion de herederos, mejora, legados, sustituciones, usufructo universal al conyuge con cautela socini y desheredacion. Solo derecho comun: si la vecindad civil es foral, o el cliente no la conoce con seguridad, detiene y escala.

Invocacion: `/derecho-civil:testamento-planificacion`

Output: minuta de testamento abierto para llevar al notario y/o checklist de planificacion sucesoria, en markdown, DRAFT.

### `contratos-particulares`

Redacta contratos entre particulares: prestamo de dinero, reconocimiento de deuda, comodato y compraventa de bien mueble. Controla la usura (cuya consecuencia es la nulidad del prestamo, no una rebaja del interes) y explica la diferencia entre documento privado y escritura publica en fecha cierta, fuerza ejecutiva y coste.

Invocacion: `/derecho-civil:contratos-particulares`

Output: contrato de prestamo, reconocimiento de deuda, comodato o compraventa de mueble, en markdown, DRAFT.

### `medidas-apoyo-discapacidad`

Prepara las medidas de apoyo de la Ley 8/2021: poder preventivo, autorizacion judicial puntual dentro de una guarda de hecho, y curatela. La curatela es **subsidiaria**: solo procede cuando no existe otra medida de apoyo suficiente, asi que la skill filtra antes de enrutar a ella. Corrige el vocabulario derogado ("incapacitar", "el incapaz") una sola vez y sin reproche.

Invocacion: `/derecho-civil:medidas-apoyo-discapacidad`

Output: minuta de poder preventivo, solicitud de autorizacion judicial en guarda de hecho o demanda de curatela, en markdown, DRAFT.

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

- Jurisdiccion por defecto: en `CLAUDE.md`, campo "Jurisdiccion por defecto".
- Clausulas adicionales habituales del despacho: agregar en `skills/<skill>/references/` como nuevo archivo de referencia y referenciar desde `SKILL.md`.
- Plantillas personalizadas: editar los assets de la skill correspondiente en `skills/<skill>/assets/`.

---

## Estado de calidad

Las **19 skills** del plugin pasaron un control de calidad ejecutado de verdad, no una revision del `SKILL.md` sobre el papel: un agente sin contexto previo juega el papel del LLM operativo sobre un caso sintetico disenado para provocar el error mas probable de esa skill, con verificacion normativa en vivo contra la API del BOE y con `Write`, `Read` y `Edit` reales sobre el documento.

**El proceso encontro defectos reales en las 16 skills sometidas a el.** Ninguno se habria visto leyendo la skill. Los mas graves, por familias:

- **Documentos que se contradecian a si mismos**: un contrato de compraventa obligaba a entregar el piso "libre de arrendatarios" mientras otra clausula describia un alquiler vigente; una solicitud de apoyos decia "no ha sido posible determinar su voluntad" y dos parrafos despues "esta voluntad se ha recabado del siguiente modo".
- **Errores que perjudicaban al cliente**: se declaraba prescrita una reclamacion viva por no preguntar antes si la aseguradora se habia comunicado; se valoraba un lote de gananciales en bruto en vez de neto de la deuda asumida, casi duplicando la compensacion debida.
- **La clausula central ausente**: en la planificacion sucesoria nunca se preguntaba a quien se instituye heredero, y como toda desheredacion pasa por esa rama, el caso mas delicado era justo el que perdia la clausula obligatoria.
- **Silencios que se leen como aprobacion**: con un interes del 12 % el guardrail de usura no saltaba y la skill no estaba obligada a decir nada.
- **Contenido correcto en el momento equivocado**: la respuesta al malentendido central de las parejas de hecho llegaba diez turnos tarde, cuando el cliente ya estaba decidiendo.

Tres defectos transversales, corregidos en todo el catalogo: placeholders genericos duplicados que rompian el `Edit` al perder el `oldString` unico; corchetes simples en colision con los identificadores de privacidad; y un turno muerto tras crear el documento que contradecia la regla del `CLAUDE.md` raiz de encadenar la primera pregunta en la misma respuesta.

El proceso de control de calidad auditó cada flujo conversacional, validando la interacción interactiva, la consulta de assets, la persistencia en disco y el ciclo de edición incremental.

## Herramientas Nativas de Agente (Agent Tools)

El plugin opera exclusivamente con las 7 herramientas nativas del catálogo de agente (agent_tools.json):

1. `read_file`: Inspección y verificación de integridad de documentos creados en el workspace.
2. `create_file`: Creación del borrador base completo con principio Zero-Omission (`{{DATO_FALTANTE}}`).
3. `edit_file`: Edición incremental y sustitución quirúrgica cláusula a cláusula.
4. `web_search`: Consulta opcional en vivo del texto consolidado de normas y baremos en el BOE.
5. `restricted_human_in_the_loop_request`: Presentación de formularios estructurados de clasificación de vectores en Fase 1.
6. `human_in_the_loop_request`: Consulta interactiva abierta en decisiones de diseño o confirmaciones críticas.
7. `slot_filling_request`: Recogida estructurada de parámetros complementarios.

---

## Instalación y Uso

Para instalar el plugin en GravitonAI:

```bash
/plugin marketplace add ./derecho-civil
```

Invocación directa de cualquier skill mediante comando de barra:
```bash
/derecho-civil:<nombre-skill>
```
