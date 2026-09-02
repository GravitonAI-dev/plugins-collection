# Catalogo de skills — plugins-collection

> Indice de referencia del marketplace (documentacion humana; no lo lee el orquestador).
> Estado por skill medido contra el estandar oro `derecho-civil/derecho-civil-arrendamiento`.
> Este catalogo vive en `test-local/` como entorno de pruebas del Plugin & Skill Builder.

## Resumen de plugins

| Plugin | Skills | Jurisdiccion | Version |
|---|---|---|---|
| commercial-legal | 1 | EE.UU. | 0.1.0 |
| general-assistant | 1 | agnostica | 0.1.0 |
| derecho-civil | 19 | Espana (CC, LEC, LAU, LPH, LO 1/2025, Ley 8/2021, TRLRCSCVM) | 0.8.0 |
| gestoria | 5 | Espana (AEAT, TGSS, DGT, ISD, extranjeria) | 0.2.1 |
| historical-drafting | 1 | agnostica (historia) | 0.1.0 |
| contrato-alquiler (test-local) | 1 | Espana (LAU) | 0.1.0 |

## Leyenda de estado

- **Completa**: cumple el estandar oro (frontmatter extendido, header DRAFT, auto-verificacion normativa, guardrails, "como NO se usa", escalacion).
- **Parcial**: frontmatter reducido (solo name + description); resto conforme.
- **N/A**: el criterio no aplica (skill no legal o agnostica).

---

## commercial-legal (v0.1.0)
Revision de acuerdos comerciales con triage GREEN/YELLOW/RED y escalacion.

### nda-review
- Proposito: triage de NDAs entrantes con veredicto VERDE/AMARILLO/ROJO y memo estructurado.
- Inputs: texto/path/URL del NDA.
- Outputs: veredicto semaforo, memo, bloque de escalacion (si ROJO).
- Jurisdiccion: EE.UU.
- Assets: nda-triage-output-template.md.
- Estado: **Parcial** (frontmatter reducido).

## general-assistant (v0.1.0)
Asistente de proposito general para consultas con informacion publica o verificacion.

### general-query
- Proposito: atiende una consulta general, decidiendo si invocar web_search.
- Inputs: consulta en lenguaje natural.
- Outputs: respuesta markdown, fuentes, claims [verificar].
- Jurisdiccion: agnostica.
- Assets: answer-output-template.md.
- Estado: **Parcial** (frontmatter reducido; DRAFT/auto-BOE N/A).

## derecho-civil (v0.8.0)
Generacion de documentos de derecho civil espanol verificados en el BOE. Las **16 skills marcadas "QA en vivo"** pasaron un control de calidad ejecutado de verdad, no una revision del `SKILL.md` sobre el papel: un agente sin contexto previo juega el papel del LLM operativo sobre un caso sintetico disenado para provocar el error mas probable de esa skill, con verificacion normativa en vivo contra la API del BOE y con `Write`, `Read` y `Edit` reales sobre el documento. **Encontro defectos reales en las 16.** Detalle por skill, con extractos literales de las conversaciones generadas, en `test-local/tests/test-derecho-civil-<skill>.md`.

### derecho-civil-reclamacion-cantidad  (QA en vivo)
- Proposito: elige la via de reclamacion de una deuda dineraria (monitorio / verbal / ordinario segun documentacion, cuantia y oposicion) y genera peticion, demanda u oposicion.
- Outputs: peticion_monitorio, burofax, demanda_verbal, demanda_ordinario, oposicion_monitorio (DRAFT).
- Jurisdiccion: Espana (LEC, LO 1/2025).
- Assets: 5.
- Estado: **Completa**. QA en vivo: 5 defectos reales corregidos (propagacion de datos confirmados a todas sus apariciones, reutilizacion de contexto ya dado, fecha unica vs. multiples facturas, pregunta obligatoria de consumidor omitida, instruccion de costas inconsistente con el asset de monitorio).

### derecho-civil-ejecucion-titulos  (QA en vivo)
- Proposito: ejecucion forzosa de titulo dinerario judicial, no judicial (escritura/laudo/mediacion) o de familia (pensiones), y escrito de embargo/investigacion patrimonial en ejecucion ya despachada.
- Outputs: demanda_ejecucion_titulo_judicial, demanda_ejecucion_titulo_no_judicial, solicitud_embargo_averiguacion (DRAFT).
- Jurisdiccion: Espana (LEC Libro III, LO 1/2025, TRLC).
- Assets: 3.
- Estado: **Completa**. QA en vivo (por el team-lead): verificacion en vivo contra la API del BOE de los arts. 517/518/539/548/608 LEC (coincidencia literal); 1 correccion de orden en la confirmacion agrupada.

### derecho-civil-arrendamiento  (QA en vivo — ESTANDAR ORO)
- Proposito: contrato de arrendamiento urbano (vivienda habitual, temporada, local o habitacion) y comunicaciones asociadas (actualizacion de renta, no renovacion, devolucion de fianza).
- Inputs: tipo inmueble, naturaleza de las partes, datos de partes/inmueble, condiciones economicas, zona tensionada.
- Outputs: contrato o comunicacion (DRAFT).
- Jurisdiccion: Espana (LAU 29/1994, Ley 12/2023, IRAV).
- Assets: 9 (4 contratos, 3 comunicaciones + los 2 originales).
- Estado: **Completa** (referencia). QA en vivo: 4 defectos corregidos (tabla condicional mal delimitada, guardrail de placeholder generico, encabezamiento sin pregunta asociada) + auditoria ampliada que encontro y corrigio 42 placeholders mas con texto de ayuda embebido en toda la skill.

### derecho-civil-desahucio  (QA en vivo)
- Proposito: demanda de juicio verbal de desahucio (falta de pago, expiracion, precario) — art. 250.1 LEC — y acuerdo extrajudicial de condonacion con entrega de llaves.
- Outputs: demanda_desahucio segun supuesto, o acuerdo_condonacion (DRAFT).
- Jurisdiccion: Espana (LEC, LAU, LO 1/2025, Ley 12/2023).
- Assets: 4 (expiracion-plazo, falta-pago, precario, acuerdo-condonacion).
- Estado: **Completa**. QA en vivo: defecto grave corregido — los 3 assets de demanda carecian de la mencion del Art. 439.6.a/b LEC (destino del inmueble, gran tenedor) que el propio `SKILL.md` marca como causa de inadmision; ademas un hueco de numeracion en el SUPLICO y una instruccion de recogida de datos faltante.

### derecho-civil-propiedad-horizontal  (QA en vivo)
- Proposito: certificacion y monitorio especial de cuotas de comunidad (Art. 21 LPH), impugnacion de acuerdos de junta (Art. 18 LPH) y requerimiento de cesacion de actividad molesta (Art. 7.2 LPH).
- Outputs: certificacion_deuda + peticion_monitorio_lph, demanda_impugnacion, requerimiento_cesacion (DRAFT).
- Jurisdiccion: Espana (LPH, LEC, LO 1/2025).
- Assets: 4.
- Estado: **Completa**. QA en vivo: 2 defectos corregidos (interes legal marcado erroneamente como negociable cuando es automatico por ley; placeholder de referencia catastral sin pregunta asociada).

### derecho-civil-juicio-ordinario
- Proposito: juicio ordinario civil por fases (admisibilidad, demanda 399, audiencia previa, prueba, conclusiones).
- Outputs: 5 documentos (DRAFT).
- Jurisdiccion: Espana (LEC, LO 1/2025, RDL 6/2023).
- Assets: 5.
- Estado: **Completa**.

### derecho-civil-monitorio
- Proposito: peticion inicial de proceso monitorio (arts. 812-818 LEC) con opcion de burofax previo.
- Outputs: peticion_monitorio, burofax_requerimiento (DRAFT).
- Jurisdiccion: Espana (LEC).
- Assets: 3.
- Estado: **Completa**.

### derecho-civil-divorcio  (QA en vivo)
- Proposito: convenio regulador de divorcio/separacion de mutuo acuerdo (art. 90 CC), demanda conjunta (art. 777 LEC) o contenciosa (art. 770 LEC), con via notarial ofrecida cuando no hay hijos menores.
- Outputs: convenio_regulador, demanda_mutuo_acuerdo, demanda_contenciosa (DRAFT).
- Jurisdiccion: Espana (CC, LEC, LO 1/2025, LOPJ).
- Assets: 3.
- Estado: **Completa**. QA en vivo: defecto grave corregido — la clausula de alimentos solo tenia redaccion para custodia exclusiva, forzando a improvisar texto fuera de plantilla con custodia compartida; mas IPC hardcodeado sin placeholder y un placeholder anidado.

### derecho-civil-modificacion-medidas  (QA en vivo)
- Proposito: demanda de modificacion de medidas definitivas (custodia, alimentos, compensatoria, vivienda), consensuada o contenciosa, y solicitud de extincion de alimentos, con filtro previo de viabilidad.
- Outputs: demanda_modificacion_medidas, solicitud_extincion_alimentos (DRAFT).
- Jurisdiccion: Espana (CC, LEC, LO 1/2025, LOPJ).
- Assets: 2.
- Estado: **Completa**. QA en vivo: 2 defectos corregidos (numeracion fija de HECHOS/Documentos que saltaba numeros cuando un bloque condicional no aplicaba, replicado en dos puntos del asset).

### derecho-civil-herencia  (QA en vivo)
- Proposito: ciclo completo de la herencia — aceptacion (pura o a beneficio de inventario), renuncia notarial (Art. 1008 CC), interpelacion al heredero silente (Art. 1005 CC), cuaderno particional (CC, legitima) y division judicial (Arts. 782 y ss. LEC); aviso ISD autonomico.
- Outputs: aceptacion_herencia, renuncia_herencia, requerimiento_1005, cuaderno_particional, solicitud_division_judicial (DRAFT).
- Jurisdiccion: Espana (CC y LEC).
- Assets: 5.
- Estado: **Completa**. QA en vivo: defecto de placeholder generico duplicado corregido (ver seccion de bugs transversales); ademas 2 anidaciones de placeholders rotas detectadas y corregidas en la auditoria posterior.

### derecho-civil-reclamacion-clausulas-abusivas
- Proposito: reclamacion extrajudicial y demanda de nulidad de clausulas abusivas (TRLGDCU, LCGC, Directiva 93/13).
- Outputs: reclamacion_extrajudicial, demanda_nulidad (DRAFT).
- Jurisdiccion: Espana/UE.
- Assets: 2.
- Estado: **Completa**.


### derecho-civil-responsabilidad-civil  (QA en vivo)
- Proposito: reclamacion de danos, contractual o extracontractual (trafico, VMP/patinete, caida, vicio constructivo, negligencia profesional), con filtro de prescripcion bloqueante.
- Outputs: reclamacion_extrajudicial_danos, demanda_responsabilidad_civil, respuesta_oferta_motivada (DRAFT).
- Jurisdiccion: Espana (CC, TRLRCSCVM con la reforma de la Ley 5/2025, LCS).
- Assets: 3.
- Estado: **Completa**. QA en vivo: 5 defectos corregidos, el mas grave declarar prescrita una reclamacion viva por no preguntar antes por la comunicacion de la aseguradora (Art. 7.1 TRLRCSCVM). Las cuantias del baremo se verifican en cada lanzamiento; registrada la pagina estable de la DGSFP porque la URL del PDF lleva el ano y caduca.

### derecho-civil-compraventa-inmueble  (QA en vivo)
- Proposito: contrato de arras, contrato privado de compraventa de vivienda y requerimiento por incumplimiento.
- Outputs: contrato_arras, contrato_compraventa_vivienda, requerimiento_cumplimiento (DRAFT).
- Jurisdiccion: Espana (CC, LAU arts. 25 y 31, LOE).
- Assets: 3.
- Estado: **Completa**. QA en vivo: contrato que se contradecia a si mismo (obligaba a entregar "libre de arrendatarios" describiendo un alquiler vigente) y un bloque condicional que el SKILL prometia y el asset no tenia. La clasificacion de las arras se presenta como jurisprudencial, nunca como categoria legal del Art. 1454.

### derecho-civil-liquidacion-gananciales  (QA en vivo)
- Proposito: liquidacion de la sociedad de gananciales, con acuerdo (convenio) o sin el (formacion judicial de inventario).
- Outputs: propuesta_inventario, convenio_liquidacion, solicitud_formacion_inventario (DRAFT).
- Jurisdiccion: Espana (CC 1344-1410; LEC 806-811, con los arts. 807, 808 y 810 reformados en 2022).
- Assets: 3.
- Estado: **Completa**. QA en vivo: defecto material corregido — el lote se valoraba en bruto en vez de neto de la deuda asumida, casi duplicando la compensacion debida en el escenario mas frecuente.

### derecho-civil-medidas-hijos-no-matrimoniales  (QA en vivo)
- Proposito: primera fijacion de custodia, estancias, alimentos y uso de la vivienda respecto de hijos de progenitores no casados.
- Outputs: pacto_relaciones_familiares, demanda_medidas_paternofiliales (DRAFT).
- Jurisdiccion: Espana (CC 92-96 y 142-156; LEC 748.4, 769.3, 770, 777).
- Assets: 2.
- Estado: **Completa**. QA en vivo: 5 defectos corregidos, entre ellos que el fundamento de la vivienda la atribuia "por la titularidad del inmueble", que era del demandado, en vez de por el interes de la menor. Registrado que los arts. 770 y 777 LEC se cenian al matrimonio y que el apoyo real esta en los arts. 748.4 y 769.3.

### derecho-civil-pareja-de-hecho  (QA en vivo)
- Proposito: constitucion, pacto de convivencia y pacto de ruptura de la pareja de hecho.
- Outputs: pacto_convivencia, pacto_ruptura, checklist_inscripcion_registro (DRAFT).
- Jurisdiccion: Espana (sin ley estatal: 17 regimenes autonomicos, verificados en cada lanzamiento; CC para los pactos; art. 221 LGSS).
- Assets: 3.
- Estado: **Completa**. QA en vivo: 8 defectos corregidos. Destaca una trampa de fuente — los portales autonomicos anuncian equiparacion "en sucesiones" refiriendose al impuesto, no al derecho a heredar — y que la respuesta al malentendido central ("¿quedamos como casados?") llegaba diez turnos tarde.

### derecho-civil-testamento-planificacion  (QA en vivo)
- Proposito: minuta de testamento abierto y checklist de planificacion sucesoria (institucion de herederos, mejora, legados, sustituciones, cautela socini, desheredacion). Solo derecho comun.
- Outputs: minuta_testamento_abierto, checklist_planificacion_sucesoria (DRAFT).
- Jurisdiccion: Espana, derecho comun (CC 662-882, con el art. 808 en redaccion Ley 8/2021). Vecindad foral o desconocida: detiene y escala.
- Assets: 2.
- Estado: **Completa**. QA en vivo: 6 defectos corregidos, el mas grave que en la rama de planificacion nunca se preguntaba a quien se instituye heredero, siendo la clausula obligatoria de la minuta y siendo esa la rama por la que pasa toda desheredacion.

### derecho-civil-contratos-particulares  (QA en vivo)
- Proposito: contratos entre particulares — prestamo, reconocimiento de deuda, comodato y compraventa de bien mueble.
- Outputs: contrato_prestamo, reconocimiento_deuda, contrato_comodato, contrato_compraventa_mueble (DRAFT).
- Jurisdiccion: Espana (CC 1088-1289, 1445-1501, 1740-1757; Ley Azcarate de 1908, verificada vigente).
- Assets: 4.
- Estado: **Completa**. QA en vivo: 5 defectos corregidos. Destaca que con un interes en franja intermedia el guardrail de usura no se disparaba y la skill no estaba obligada a decir nada: ese silencio se lee como aprobacion. Ninguna cifra de interes legal escrita fija (no hay PGE de 2026).

### derecho-civil-medidas-apoyo-discapacidad  (QA en vivo)
- Proposito: medidas de apoyo de la Ley 8/2021 — poder preventivo, autorizacion judicial en guarda de hecho y curatela, esta ultima subsidiaria.
- Outputs: minuta_poder_preventivo, solicitud_autorizacion_guarda_hecho, demanda_curatela (DRAFT).
- Jurisdiccion: Espana (CC 249-298 en redaccion Ley 8/2021; LEC 756-763; LJV).
- Assets: 3.
- Estado: **Completa**. QA en vivo: el SKILL mandaba activar un bloque que no existia en el asset, y el escrito salia diciendo "no ha sido posible determinar su voluntad" e inmediatamente despues "esta voluntad se ha recabado del siguiente modo". Corregido. La correccion terminologica del vocabulario derogado se emite una sola vez y sin reproche.

### Bugs transversales encontrados y corregidos en las 19 skills (01-03/09/2026)

1. **Placeholder generico duplicado**: un `SKILL.md` que instruia sustituir cualquier dato faltante por un token generico repetido (`{{DATO_FALTANTE}}` o `[DATO]`) rompia el `Edit` posterior en cuanto habia dos huecos iguales en el mismo documento (`oldString` deja de ser unico). Corregido: cada dato faltante conserva el nombre propio del placeholder del asset.
2. **Corchete simple en colision con privacidad**: `reclamacion-clausulas-abusivas` usaba `[verificar]`/`[DATO]` visibles en el documento final, en violacion de la regla raiz que prohibe corchetes simples (colision con `[PERSON_1]`). Corregido a `{{VERIFICAR}}` y placeholders con nombre propio.
3. **Placeholders con texto de ayuda embebido**: 176 casos en 9 de las 11 skills (`{{naturaleza: persona fisica / persona juridica}}` en vez de `{{naturaleza}}`), incluidas 2 llaves anidadas rotas en `herencia` y `juicio-ordinario`. Corregidos todos; verificado por grep en cero casos restantes en todo el catalogo.
4. **Turno muerto tras crear el documento**: 12 skills preguntaban "¿desea empezar a completar los datos?" despues del `Write`, contradiciendo la regla del `CLAUDE.md` raiz (seccion 6.1, punto 5) de encadenar la primera pregunta en la misma respuesta, y el Punto 0 de arranque inmediato. Corregido en las 12 y en la guia.
5. **Seccion opcional con placeholder crudo**: "CLAUSULAS ADICIONALES" llegaba al contrato firmado con el placeholder sin resolver cuando el cliente no pedia ninguna. Corregido en los 10 assets afectados envolviendo el bloque completo, cabecera incluida, en el comentario condicional.
6. **Desincronizacion entre `SKILL.md` y asset**: el `SKILL.md` mandaba activar bloques condicionales que el asset no tenia escritos (detectado en `compraventa-inmueble`, `medidas-apoyo-discapacidad` y, en forma de clausula obligatoria ausente, en `testamento-planificacion`). Obliga al agente operacional a improvisar texto fuera de plantilla. Anadida como regla 5 de la seccion 4 de `PLUGIN_AUTHORING_GUIDE.md`.

Las tres reglas quedaron escritas en `PLUGIN_AUTHORING_GUIDE.md` (seccion 2 y seccion 4) para toda skill futura del marketplace.

## gestoria (v0.2.1)
Documentos y solicitudes para tramites administrativos en Espana, verificados en el BOE.

### alta-baja-autonomo
- Proposito: alta/baja censal (036) en AEAT y alta/baja en el RETA.
- Outputs: hojas de datos + checklist (DRAFT).
- Jurisdiccion: Espana (Ley 20/2007, AEAT, SS).
- Assets: 4.
- Estado: **Completa**.

### alta-baja-seguridad-social
- Proposito: altas/bajas en la Seguridad Social (afiliacion TA.1, CCC TA.6, trabajadores, hogar).
- Outputs: hoja_datos_ta + checklist (DRAFT).
- Jurisdiccion: Espana (LGSS, RD 84/1996).
- Assets: 3.
- Estado: **Completa**.

### extranjeria-residencia
- Proposito: solicitud de NIE o autorizacion de residencia (no lucrativa, arraigo, reagrupacion).
- Outputs: hoja_datos_ex + checklist, escrito_solicitud (DRAFT).
- Jurisdiccion: Espana (LOEX, RD 1155/2024).
- Assets: 2.
- Estado: **Completa**.

### liquidacion-impuesto-sucesiones
- Proposito: autoliquidacion del ISD (modelo 650, mortis causa) segun Ley 29/1987 y normativa autonomica.
- Outputs: borrador_650 (cuota [verificar]), checklist (DRAFT).
- Jurisdiccion: Espana (Ley 29/1987 + autonomica).
- Assets: 2.
- Estado: **Completa**.

### transferencia-vehiculo
- Proposito: cambio de titularidad de vehiculo usado ante la DGT y notificacion de venta; aviso ITP.
- Outputs: contrato_compraventa, solicitud_cambio_titularidad, notificacion_venta (DRAFT).
- Jurisdiccion: Espana (RD 2822/1998, DGT).
- Assets: 3.
- Estado: **Completa**.

## historical-drafting (v0.1.0)
Investigacion historica con borradores verificables y trazabilidad de fuentes.

### venezuela-history
- Proposito: resumenes y analisis de historia de Venezuela con citas trazables.
- Outputs: borrador estructurado (hechos, analisis, cronologia, fuentes).
- Jurisdiccion: agnostica.
- Assets: ninguno (por diseno).
- Estado: **Parcial** (frontmatter reducido; DRAFT/auto-BOE N/A).

## contrato-alquiler (test-local, v0.1.0)
Skill de prueba generada con el builder: contrato de alquiler con arbol de decision.

### contrato-alquiler
- Proposito: contrato de alquiler (vivienda o local) navegando un arbol de decision de preguntas textuales que activa los bloques del asset.
- Inputs: respuestas al arbol, datos de partes/inmueble, condiciones economicas.
- Outputs: contrato_alquiler (DRAFT) con los bloques de la rama recorrida.
- Jurisdiccion: Espana (LAU 29/1994).
- Assets: contrato-alquiler.md.
- Estado: **Completa**.

---

## Sintesis del estado

| Estado | Skills |
|---|---|
| Completa | 25 |
| Parcial (frontmatter reducido) | 3 (nda-review, general-query, venezuela-history) |
| Total | 28 |

Todos los assets del marketplace usan la convencion `{{placeholder}}`; no hay datos reales incrustados.
