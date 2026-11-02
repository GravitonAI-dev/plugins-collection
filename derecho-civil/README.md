# Derecho Civil

Plugin de GravitonAI para la generación de documentos de derecho civil español, verificando siempre la versión consolidada vigente en el BOE antes de redactar. **19 skills** que cubren reclamación de cantidad y ejecución de títulos, contratos entre particulares, arrendamiento, desahucio, compraventa de inmuebles y propiedad horizontal, familia (divorcio, medidas sobre hijos, modificación de medidas, gananciales y pareja de hecho), sucesiones (herencia y planificación testamentaria), cláusulas abusivas de consumo, responsabilidad civil y medidas de apoyo a personas con discapacidad.

---

## Qué hace

- Elige la vía correcta de reclamación de una deuda (monitorio, juicio verbal u ordinario) y genera la petición o demanda, con opción de burofax previo (Arts. 812-818, 249-250 LEC).
- Ejecuta forzosamente títulos judiciales, no judiciales (escritura, laudo, acuerdo de mediación) y pensiones de familia, incluida la designación de bienes y la investigación patrimonial (Libro III LEC).
- Genera contratos de arrendamiento de vivienda habitual, temporada, local de negocio y habitación, y las comunicaciones asociadas (actualización de renta, no renovación, devolución de fianza), con verificación de zona de mercado tensionado.
- Genera demandas de desahucio (falta de pago con acumulación de rentas, expiración de plazo o precario) y el acuerdo extrajudicial de condonación con entrega de llaves.
- Genera los documentos de comunidad de propietarios: certificación y monitorio especial de cuotas, impugnación de acuerdos de junta y requerimiento de cesación de actividad molesta (LPH).
- Genera el convenio regulador y la demanda de divorcio o separación, de mutuo acuerdo o contenciosa, y la demanda de modificación o extinción de medidas ya fijadas (custodia, alimentos, compensatoria).
- Cubre el ciclo completo de la herencia: aceptación, renuncia, interpelación al heredero silente, cuaderno particional y división judicial.
- Prepara el juicio ordinario civil de principio a fin (admisibilidad, demanda, audiencia previa, prueba y conclusiones).
- Genera la reclamación extrajudicial y la demanda de nulidad de cláusulas abusivas de consumo.
- Reclama daños por responsabilidad civil, incluidos los accidentes con vehículos personales ligeros (patinetes), con seguro obligatorio desde la Ley 5/2025, y responde a la oferta motivada de la aseguradora.
- Genera contratos de arras y de compraventa de vivienda, con advertencia del tanteo y retracto del arrendatario si el inmueble está alquilado.
- Liquida la sociedad de gananciales, con acuerdo o por vía judicial, y fija por primera vez las medidas sobre hijos de progenitores no casados.
- Constituye parejas de hecho y pacta su convivencia o su ruptura, verificando en cada lanzamiento la normativa y el registro de la comunidad autónoma.
- Prepara la minuta del testamento y el checklist de planificación sucesoria (legitimas, mejora, sustituciones, desheredación), solo en derecho común.
- Redacta contratos entre particulares (préstamo, reconocimiento de deuda, comodato, compraventa de mueble) con control de usura.
- Prepara las medidas de apoyo a personas con discapacidad de la Ley 8/2021, tratando la curatela como subsidiaria de la guarda de hecho y de las medidas voluntarias.
- Toda skill verifica en cada lanzamiento la versión vigente de su norma en el BOE antes de redactar y, si detecta cambios, aplica la redacción vigente al documento que genera en el workspace, sin modificar los archivos del plugin. Las magnitudes que cambian solas (baremo de tráfico, IRAV, SMI, interés legal) se consultan en el momento y nunca quedan escritas fijas en la plantilla.

## Qué NO hace

- No revisa contratos ni escritos ya redactados por terceros.
- No cubre arrendamientos de finca rustica, viviendas turísticas, viviendas militares ni porteros/guardas.
- No tramita el depósito de fianza ante el organismo autonómico ni gestiona el pago de impuestos.
- No cubre la ejecución hipotecaria ni la oposición de la parte ejecutada/demandada.
- No da opinión jurídica concreta; el output siempre es un DRAFT para revisión por abogado colegiado.
- No reemplaza la firma ante notario ni la inscripción en el Registro de la Propiedad.

---

## Skills

### `reclamacion-cantidad`

Elige la vía de reclamación de una deuda dineraria (monitorio, verbal u ordinario según documentación, cuantía y oposición) y genera la petición, demanda u oposición correspondiente, con burofax previo.

Invocación: `/derecho-civil:reclamacion-cantidad`

Output: petición de monitorio, burofax, demanda de verbal u ordinario, u oposición al monitorio, en markdown, DRAFT.

### `ejecucion-titulos`

Ejecuta forzosamente un título dinerario: judicial (sentencia, decreto, incluido monitorio firme), no judicial (escritura, laudo, acuerdo de mediación) o de familia (pensiones), y genera por separado el escrito de embargo/investigación patrimonial cuando la ejecución ya está despachada.

Invocación: `/derecho-civil:ejecucion-titulos`

Output: demanda de ejecución de título judicial, no judicial o de familia, o solicitud de embargo/averiguación patrimonial, en markdown, DRAFT.

Que NO hace: no cubre la ejecución hipotecaria, la ejecución provisional ni la oposición del ejecutado.

### `arrendamiento-urbano`

Genera un contrato de arrendamiento urbano (vivienda habitual, temporada, local o habitación) y las comunicaciones asociadas al contrato vigente.

Invocación: `/derecho-civil:arrendamiento-urbano`

Output: contrato de arrendamiento o comunicación (actualización de renta, no renovación, devolución de fianza), en markdown, DRAFT.

### `desahucio`

Genera la demanda de juicio verbal de desahucio (falta de pago con acumulación de rentas, expiración del plazo o precario) o el acuerdo extrajudicial de condonación de rentas a cambio de la entrega de llaves.

Invocación: `/derecho-civil:desahucio`

Output: demanda de desahucio según el supuesto, o acuerdo de condonación, en markdown, DRAFT.

Que NO hace: no cubre la tutela sumaria frente a ocupación ilegal (Art. 250.1.4 LEC), finca rustica ni ejecución hipotecaria; no redacta la oposición del demandado.

### `propiedad-horizontal`

Genera la certificación del acuerdo de liquidación de deuda y la petición de monitorio especial de cuotas de comunidad, la demanda de impugnación de acuerdos de junta y el requerimiento de cesación de actividad molesta.

Invocación: `/derecho-civil:propiedad-horizontal`

Output: certificación + petición de monitorio, demanda de impugnación, o requerimiento de cesación, en markdown, DRAFT.

### `juicio-ordinario`

Prepara de principio a fin un juicio ordinario civil (cuantía superior a 15.000 euros o materia del Art. 249.1 LEC): checklist de admisibilidad, demanda, guion de audiencia previa, proposición de prueba y minuta de conclusiones.

Invocación: `/derecho-civil:juicio-ordinario`

Output: según la fase, checklist de admisibilidad, demanda, guion de audiencia previa, proposición de prueba y/o minuta de conclusiones, en markdown, DRAFT.

### `monitorio`

Genera la petición inicial de proceso monitorio para reclamar una deuda dineraria líquida, vencida y exigible (arts. 812-818 LEC), con opción de burofax de requerimiento previo.

Invocación: `/derecho-civil:monitorio`

Output: petición inicial de monitorio en markdown, DRAFT (y, opcionalmente, burofax de requerimiento previo).

### `divorcio`

Genera el convenio regulador de separación o divorcio de mutuo acuerdo (Art. 90 CC), la demanda conjunta (Art. 777 LEC) o la demanda contenciosa (Art. 770 LEC), y ofrece la vía notarial cuando no hay hijos menores ni dependientes.

Invocación: `/derecho-civil:divorcio`

Output: convenio regulador, demanda de mutuo acuerdo o demanda contenciosa, en markdown, DRAFT.

### `modificacion-medidas`

Genera la demanda de modificación de medidas definitivas ya fijadas (custodia, alimentos, compensatoria, vivienda), consensuada o contenciosa, y la solicitud de extinción de la pensión de alimentos, con filtro previo de viabilidad de la alteración sustancial alegada.

Invocación: `/derecho-civil:modificacion-medidas`

Output: demanda de modificación de medidas o solicitud de extinción de alimentos, en markdown, DRAFT.

Que NO hace: no fija medidas por primera vez; no cubre la ejecución de pensiones impagadas.

### `herencia`

Cubre el ciclo completo de la herencia, para sucesión testada o intestada: aceptación (pura y simple o a beneficio de inventario), renuncia (minuta para escritura notarial, Art. 1008 CC), interpelación notarial al heredero que no se pronuncia (Art. 1005 CC), cuaderno particional (inventario, avalúo, liquidación y adjudicaciones, con respeto de la legítima) y solicitud de división judicial a falta de acuerdo (Arts. 782 y ss. LEC). Advierte del Impuesto de Sucesiones (autonómico) y la plusvalía municipal.

Invocación: `/derecho-civil:herencia`

Output: según el caso, aceptación, renuncia, requerimiento del Art. 1005 CC, cuaderno particional o solicitud de división judicial, en markdown, DRAFT.

### `reclamacion-clausulas-abusivas`

Genera la reclamación extrajudicial y/o la demanda de nulidad de cláusula abusiva con restitución de cantidades, en contratos con consumidores (TRLGDCU, LCGC, Directiva 93/13). Verifica la jurisprudencia reciente del TJUE y del Tribunal Supremo.

Invocación: `/derecho-civil:reclamacion-clausulas-abusivas`

Output: reclamación extrajudicial y/o demanda de nulidad con restitución, en markdown, DRAFT.

### `responsabilidad-civil`

Reclama los daños sufridos por culpa de otro, contractual o extracontractual: accidente de tráfico con vehículo a motor o con vehículo personal ligero (patinete, con seguro obligatorio desde la Ley 5/2025), caída en establecimiento o vía pública, vicio constructivo y negligencia profesional. Aplica un filtro de prescripción bloqueante (un año en la extracontractual, cinco en la contractual) y verifica en cada lanzamiento las cuantías del baremo del ejercicio en curso, que nunca quedan escritas fijas.

Invocación: `/derecho-civil:responsabilidad-civil`

Output: reclamación extrajudicial de daños, demanda de responsabilidad civil o respuesta a la oferta motivada de la aseguradora, en markdown, DRAFT.

### `compraventa-inmueble`

Genera el contrato de arras o señal, el contrato privado de compraventa de vivienda y el requerimiento por incumplimiento. Exige pactar expresamente la clase de arras, porque el silencio juega en contra de quien quiere desistir, y advierte del derecho de tanteo y retracto del arrendatario si el inmueble está alquilado.

Invocación: `/derecho-civil:compraventa-inmueble`

Output: contrato de arras, contrato de compraventa o requerimiento de cumplimiento, en markdown, DRAFT.

### `liquidacion-gananciales`

Liquida la sociedad de gananciales, con acuerdo (convenio) o sin el (solicitud judicial de formación de inventario). Explica la presunción de ganancialidad, los reintegros entre masas y, sobre todo, que adjudicar la vivienda a un cónyuge no libera al otro frente al banco.

Invocación: `/derecho-civil:liquidacion-gananciales`

Output: propuesta de inventario, convenio de liquidación o solicitud de formación de inventario, en markdown, DRAFT.

### `medidas-hijos-no-matrimoniales`

Fija por primera vez la custodia, el régimen de estancias, los alimentos y el uso de la vivienda respecto de hijos de progenitores no casados, de mutuo acuerdo o por vía contenciosa. Comprueba antes que la filiación esté determinada respecto de ambos.

Invocación: `/derecho-civil:medidas-hijos-no-matrimoniales`

Output: pacto de relaciones familiares o demanda de medidas paternofiliales, en markdown, DRAFT.

### `pareja-de-hecho`

Constituye la pareja de hecho, pacta la convivencia o regula la ruptura. Como no existe ley estatal, pregunta la comunidad autónoma y **verifica su normativa y su registro en cada lanzamiento** en lugar de darlos por sabidos. Deja claro que la inscripción no equipara al matrimonio y que el conviviente no hereda sin testamento.

Invocación: `/derecho-civil:pareja-de-hecho`

Output: pacto de convivencia, pacto de ruptura o checklist de inscripción en el registro autonómico, en markdown, DRAFT.

### `testamento-planificacion`

Prepara la minuta del testamento abierto y el checklist de planificación sucesoria: institución de herederos, mejora, legados, sustituciones, usufructo universal al cónyuge con cautela socini y desheredación. Solo derecho común: si la vecindad civil es foral, o el cliente no la conoce con seguridad, detiene y escala.

Invocación: `/derecho-civil:testamento-planificacion`

Output: minuta de testamento abierto para llevar al notario y/o checklist de planificación sucesoria, en markdown, DRAFT.

### `contratos-particulares`

Redacta contratos entre particulares: préstamo de dinero, reconocimiento de deuda, comodato y compraventa de bien mueble. Controla la usura (cuya consecuencia es la nulidad del préstamo, no una rebaja del interés) y explica la diferencia entre documento privado y escritura pública en fecha cierta, fuerza ejecutiva y coste.

Invocación: `/derecho-civil:contratos-particulares`

Output: contrato de préstamo, reconocimiento de deuda, comodato o compraventa de mueble, en markdown, DRAFT.

### `medidas-apoyo-discapacidad`

Prepara las medidas de apoyo de la Ley 8/2021: poder preventivo, autorización judicial puntual dentro de una guarda de hecho, y curatela. La curatela es **subsidiaria**: solo procede cuando no existe otra medida de apoyo suficiente, así que la skill filtra antes de enrutar a ella. Corrige el vocabulario derogado ("incapacitar", "el incapaz") una sola vez y sin reproche.

Invocación: `/derecho-civil:medidas-apoyo-discapacidad`

Output: minuta de poder preventivo, solicitud de autorización judicial en guarda de hecho o demanda de curatela, en markdown, DRAFT.

---

## Alcance del plugin

Este plugin cubre documentos JURÍDICOS de derecho civil (contratos, demandas, reclamaciones). Los TRÁMITES administrativos ante organismos (DGT, Hacienda, Seguridad Social, registros, extranjería) se ubican en el plugin `gestoria`.

---

## Dependencias

### Tools requeridas

| ID | Uso |
|---|---|
| `io.gravitonai.tools.read_document` | Lectura directa de normas en el BOE (verificación normativa) |
| `io.gravitonai.tools.web_search` | Fallback normativo y consulta de normativa autonómica |
| `io.gravitonai.tools.draft_markdown` | Generación del documento desde plantilla |

### Tools opcionales

| ID | Uso |
|---|---|
| `io.gravitonai.tools.escalate_to_attorney` | Escalación a abogado en casos complejos |

### Servidores MCP

Ninguno.

---

## Instalación

```
/plugin marketplace add ./derecho-civil
```

---

## Tuning

- Jurisdicción por defecto: en `CLAUDE.md`, campo "Jurisdicción por defecto".
- Cláusulas adicionales habituales del despacho: agregar en `skills/<skill>/references/` como nuevo archivo de referencia y referenciar desde `SKILL.md`.
- Plantillas personalizadas: editar los assets de la skill correspondiente en `skills/<skill>/assets/`.

---

## Estado de calidad

Las **19 skills** del plugin pasaron un control de calidad ejecutado de verdad, no una revisión del `SKILL.md` sobre el papel: un agente sin contexto previo juega el papel del LLM operativo sobre un caso sintético diseñado para provocar el error más probable de esa skill, con verificación normativa en vivo contra la API del BOE y con `create_file`, `read_file` y `edit_file` reales sobre el documento.

**El proceso encontró defectos reales en las 16 skills sometidas a él.** Ninguno se habría visto leyendo la skill. Los más graves, por familias:

- **Documentos que se contradecían a sí mismos**: un contrato de compraventa obligaba a entregar el piso "libre de arrendatarios" mientras otra cláusula describía un alquiler vigente; una solicitud de apoyos decía "no ha sido posible determinar su voluntad" y dos párrafos después "esta voluntad se ha recabado del siguiente modo".
- **Errores que perjudicaban al cliente**: se declaraba prescrita una reclamación viva por no preguntar antes si la aseguradora se había comunicado; se valoraba un lote de gananciales en bruto en vez de neto de la deuda asumida, casi duplicando la compensación debida.
- **La cláusula central ausente**: en la planificación sucesoria nunca se preguntaba a quién se instituye heredero, y como toda desheredación pasa por esa rama, el caso más delicado era justo el que perdía la cláusula obligatoria.
- **Silencios que se leen como aprobación**: con un interés del 12 % el guardrail de usura no saltaba y la skill no estaba obligada a decir nada.
- **Contenido correcto en el momento equivocado**: la respuesta al malentendido central de las parejas de hecho llegaba diez turnos tarde, cuando el cliente ya estaba decidiendo.

Tres defectos transversales, corregidos en todo el catálogo: placeholders genéricos duplicados que rompían el `edit_file` al perder el `oldString` único; corchetes simples en colisión con los identificadores de privacidad; y un turno muerto tras crear el documento que contradecía la regla del `CLAUDE.md` raíz de encadenar la primera pregunta en la misma respuesta.

El proceso de control de calidad auditó cada flujo conversacional, validando la interacción interactiva, la consulta de assets, la persistencia en disco y el ciclo de edición incremental.

## Herramientas Nativas de Agente (Agent Tools)

El plugin opera exclusivamente con las 9 herramientas nativas del catálogo de agente (agent_tools.json):

1. `read_file`: Inspección y verificación de integridad de documentos creados en el workspace (reservado para casos extremos donde el documento no figure en `# WORKSPACE ACTIVE DOCUMENTS`).
2. `create_file`: Creación del borrador base completo con principio Zero-Omission (`{{DATO_FALTANTE}}`).
3. `edit_file`: Edición incremental y sustitución quirúrgica cláusula a cláusula.
4. `web_search`: Consulta opcional en vivo del texto consolidado de normas y baremos en el BOE.
5. `restricted_human_in_the_loop_request`: Presentación de formularios estructurados de clasificación de vectores en Fase 1 y desambiguación de clientes.
6. `human_in_the_loop_request`: Consulta interactiva abierta en decisiones de diseño o confirmaciones críticas.
7. `slot_filling_request`: Recogida estructurada de parámetros de la transacción o datos residuales faltantes.
8. `search_clients`: Búsqueda primaria y de máxima prioridad para identificar partes y personas en el sistema.
9. `get_client`: Obtención de la ficha completa y detallada de un cliente seleccionado.

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
