# Test de ejecucion — skill `derecho-civil-arrendamiento` (arbol ampliado)

Ejecucion manual del arbol de decision sobre tres escenarios. Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento, el relleno del asset y el disparo de preguntas.

## Verificacion normativa (Punto 2)

- Fuentes: BOE — LAU (BOE-A-1994-26003, consolidada 25/05/2023), Ley 12/2023 (BOE-A-2023-12203, consolidada 28/02/2026), Resolucion INE del IRAV (BOE-A-2024-26685, vigente desde 01/01/2025), Codigo Civil (BOE-A-1889-4763).
- Verificadas online el 31/08/2026 (ver `references/fuentes-plantillas-validadas.md` de la skill). En estos tests se usan esas versiones.
- `fecha_verificacion_lau` = 25/05/2023 (Ley 12/2023).

---

## Test 1 — Vivienda habitual en zona tensionada

Peticion inicial simulada: "Quiero un contrato de alquiler de un piso en Barcelona para un inquilino que vivira alli de forma permanente. El casero es un particular."

### Recorrido del arbol
```
V0 -> contrato (escucha activa: "contrato de alquiler")      sin pregunta
V2 -> vivienda (escucha activa: "piso")                       sin pregunta
V5 -> vivienda completa                                       PREGUNTA (alcance)
V1 -> permanente (escucha activa: "de forma permanente")      sin pregunta
V6 -> "no lo se"                                              PREGUNTA (zona tensionada)
V3 -> persona fisica (escucha activa: "un particular")        sin pregunta
V4 -> persona fisica                                          PREGUNTA (naturaleza arrendatario)
HOJA -> assets/contrato-arrendamiento-vivienda.md
```
Ruta: `V0-contrato -> V2-vivienda -> V5-completa -> V1-permanente -> V6-no-lo-se -> V3-fisica -> V4-fisica -> HOJA vivienda`
Bloques activados: `vivienda habitual`, `zona_tensionada` (resuelto en seccion 5.A.1: el agente verifica con web_search que Barcelona esta en zona declarada de mercado residencial tensionado por la Generalitat y lo informa en la vista previa, sin pedir el dato al cliente).

### Disparo de preguntas
- Una pregunta por turno: solo se formularon V5, V6 y V4 (3 turnos); V0, V2, V1 y V3 se resolvieron por escucha activa de la peticion inicial y NO se re-preguntaron. OK.
- V6 admite "No lo se" y no bloquea: la resolucion se difiere a la verificacion oficial de la seccion 1. OK.
- Introduccion fija solo en el primer turno, antes de la pregunta de V5. OK.
- Seccion 2 (partes): 6 turnos (a-f), un dato por turno, con UNA sola confirmacion agrupada por parte ("¿Confirmamos estos datos del arrendador?") tras el apartado c, y otra tras el f. Sin vistas previas intermedias dato a dato. OK.

### Validaciones
- Duracion pactada 5 anos >= minimo 5 (arrendador persona fisica, Art. 9.1 LAU): OK.
- Zona tensionada confirmada -> clausula TERCERA incorpora la prorroga extraordinaria (Art. 10.3 LAU), clausula CUARTA incorpora el limite de renta (Art. 17.6 LAU: no superar la ultima renta del contrato anterior) y se anade la advertencia final adicional. OK.
- Actualizacion: clausula QUINTA con tope IRAV (INE, Resolucion 18/12/2024), no IPC. OK.
- Fianza 1 mensualidad >= minimo vivienda (1): OK.

### Extracto sintetico del documento generado
```
CONTRATO DE ARRENDAMIENTO DE VIVIENDA — ARRENDADOR A / ARRENDATARIO A
> DRAFT — para revision por un abogado antes de su firma.
> Version de la LAU verificada en el BOE: 25/05/2023

ARRENDADOR: ARRENDADOR A — NIF 00000000-T — Calle Ejemplo 1, Barcelona — persona fisica
ARRENDATARIO: ARRENDATARIO A — NIF 11111111-H — Calle Ejemplo 2, Barcelona — persona fisica

TERCERA — Duracion: 5 anos desde 01/10/2026. Preaviso de no renovacion: 4 meses
  arrendador / 2 meses arrendatario (Art. 10.1 LAU).
  CLAUSULA ESPECIAL — ZONA DE MERCADO RESIDENCIAL TENSIONADO: prorroga extraordinaria
  del Art. 10.3 LAU a solicitud del ARRENDATARIO.
CUARTA — Renta: 950 euros/mes. La renta cumple los limites del Art. 17.6 LAU
  (ultima renta del contrato anterior: 950 euros/mes).
QUINTA — Actualizacion: IRAV (INE), Art. 18 LAU y Resolucion de 18/12/2024.
SEXTA — Fianza: 950 euros (1 mensualidad, Art. 36.1 LAU).
> Advertencia adicional: el inmueble se ubica en zona de mercado residencial tensionado.
```
Filtrado de ramas: el documento NO contiene bloques de `local` (actividad, licencias, Art. 34), `temporada` (causa de temporada, extincion sin prorroga) ni `habitacion` (zonas comunes, convivencia). Cero comentarios HTML en el documento escrito.

Resultado: **PASA**.

---

## Test 2 — Vivienda por temporada (6 meses por trabajo)

Peticion inicial simulada: "Necesito un contrato para alquilar mi apartamento 6 meses a un ingeniero desplazado por obra. El vive en Sevilla y vuelve alli al terminar."

### Recorrido del arbol
```
V0 -> contrato                                                sin pregunta
V2 -> vivienda ("apartamento")                                sin pregunta
V5 -> vivienda completa                                       PREGUNTA (alcance)
V1 -> temporal ("6 meses... desplazado por obra")             sin pregunta
V1-b -> temporada (causa laboral, no turistico)               sin pregunta (inequivoco)
V6 -> NO APLICA (solo vivienda habitual)                      no se pregunta
V3 -> persona fisica ("mi apartamento")                       sin pregunta
V4 -> persona fisica ("un ingeniero")                         sin pregunta
HOJA -> assets/contrato-arrendamiento-temporada.md
```
Ruta: `V0-contrato -> V2-vivienda -> V5-completa -> V1-temporal -> V1b-temporada -> V3-fisica -> V4-fisica -> HOJA temporada`
Bloques activados: `temporada` (Art. 3.2 LAU, uso distinto de vivienda). Cambio clave respecto a la version anterior de la skill: la rama temporada YA NO detiene el proceso — genera contrato con su propio asset.

### Disparo de preguntas
- Solo se formulo V5 (1 turno): el resto se resolvio por escucha activa. No se re-pregunto ningun dato ya aportado (duracion 6 meses y causa laboral quedan registrados para las secciones 3 y 4). OK.
- V6 (zona tensionada) NO se dispara en temporada: los limites de renta del Art. 17.6 no aplican a uso distinto de vivienda. OK.
- Seccion 3 (objeto): la causa de temporada se valida como real y acreditable (trabajo por obra, con residencia habitual en Sevilla) — Guardrail 8 no se activa. OK.

### Validaciones
- Sin plazos minimos ni prorrogas del Titulo II: duracion pactada 6 meses con fecha cierta de fin. OK.
- Fianza: 2 mensualidades (Art. 36.1 LAU, uso distinto). Una fianza de 1 mensualidad se habria rechazado. OK.
- Domicilio habitual del arrendatario (Sevilla) distinto de la vivienda arrendada: coherente con la causa. OK.

### Extracto sintetico del documento generado
```
CONTRATO DE ARRENDAMIENTO DE VIVIENDA POR TEMPORADA — ARRENDADOR B / ARRENDATARIO B
> DRAFT — para revision por un abogado antes de su firma.
> Version de la LAU verificada en el BOE: 25/05/2023

EXPONE II: ... UNICAMENTE por razon de temporada, por la siguiente causa:
  trabajo temporal (obra), manteniendo su residencia habitual en Calle Ejemplo 3, Sevilla.
EXPONE III: arrendamiento para uso distinto del de vivienda, Art. 3.2 LAU, Titulo III.
TERCERA — Duracion: del 01/10/2026 al 31/03/2027. Al vencimiento el contrato queda
  extinguido sin prorroga (no aplican los Arts. 9 y 10 LAU).
QUINTA — Fianza: 1.600 euros (2 mensualidades, Art. 36.1 LAU).
NOVENA — Resolucion: causa de resolucion destinar la vivienda a residencia permanente.
```
Filtrado de ramas: el documento NO contiene bloques de `vivienda habitual` — sin plazos minimos 5/7 anos, sin prorroga del Art. 10, sin clausula IRAV de actualizacion anual, sin limites de zona tensionada, sin derecho de adquisicion preferente del Art. 25. Tampoco bloques de `local` ni `habitacion`. Cero comentarios HTML en el documento escrito.

Resultado: **PASA**.

---

## Test 3 — Comunicacion de no renovacion remitida por el arrendador

Peticion inicial simulada: "Soy el propietario y quiero avisar a mi inquilina de que no le renuevo el contrato de vivienda, que vence el 15 de enero de 2027."

### Recorrido del arbol
```
V0 -> comunicacion ("avisar... no le renuevo")                sin pregunta
V7 -> no renovacion                                           sin pregunta
V8 -> arrendador ("soy el propietario")                       sin pregunta
V6 -> "no" (respuesta del cliente)                            PREGUNTA (zona tensionada)
V2/V5/V1/V3/V4 -> NO APLICAN (no es contrato nuevo)           no se preguntan
HOJA -> assets/comunicacion-no-renovacion.md
```
Ruta: `V0-comunicacion -> V7-no-renovacion -> V8-arrendador -> V6-no -> HOJA no-renovacion`
Bloques activados: `preaviso arrendador (4 meses)`. Bloque `zona tensionada (Art. 10.3)` desactivado tras contraste con fuente oficial en la seccion 3.

### Disparo de preguntas
- Solo se formulo V6 (1 turno). El tipo de inmueble, alcance, finalidad y naturalezas NO se preguntan en la rama comunicacion: el flujo salta directo a las secciones de 5.B. OK.
- La fecha de vencimiento (15/01/2027) aportada en la peticion inicial NO se re-pregunta en la seccion 5.B.3: queda registrada por escucha activa. OK.
- Seccion 5.B.2: datos de remitente y destinatario un dato por turno con confirmacion agrupada por parte; la condicion (arrendador/arrendatario) no se re-pregunta porque V8 ya la resolvio. OK.

### Validacion del plazo de preaviso (Art. 10.1 LAU) — verificacion critica del escenario
- Remitente: ARRENDADOR -> preaviso minimo 4 meses.
- Fecha de emision prevista: 31/08/2026. Vencimiento: 15/01/2027. Antelacion: 4 meses y 15 dias >= 4 meses. **Preaviso valido.** El asset inserta el bloque del arrendador ("antelacion no inferior a cuatro meses") y omite el del arrendatario (2 meses).
- Contraprueba (rama de advertencia): con vencimiento 15/11/2026 la antelacion seria de 2 meses y 15 dias < 4 meses -> la skill advierte de comunicacion extemporanea y de la prorroga anual (Guardrail 9) antes de redactar. Comportamiento verificado en la instruccion 5.B.3.

### Extracto sintetico del documento generado
```
COMUNICACION DE NO RENOVACION DEL CONTRATO DE ARRENDAMIENTO — ARRENDADOR C a ARRENDATARIA C
> DRAFT — para revision por un abogado antes de su envio.

REMITENTE (ARRENDADOR): ARRENDADOR C — NIF 00000000-T — Calle Ejemplo 4, Ciudad
DESTINATARIO (ARRENDATARIO): ARRENDATARIA C — Calle Ejemplo 5, Ciudad

... le comunico ... mi voluntad de NO RENOVAR el referido contrato a su vencimiento,
de conformidad con el articulo 10.1 de la Ley 29/1994 ...
La presente comunicacion se remite con una antelacion no inferior a cuatro meses
respecto de la fecha de vencimiento indicada (15/01/2027) ...
> Advertencia: envio recomendado por burofax con certificacion de texto y acuse de recibo.
```
Filtrado de ramas: el documento NO contiene el parrafo de preaviso del arrendatario (2 meses), NO contiene el bloque de zona tensionada (V6 = no, contrastado), y NO contiene clausulas de contrato (partes/objeto/duracion/renta). Cero comentarios HTML en el documento escrito.

Resultado: **PASA**.

---

## Resumen del test

| Test | Ruta | Asset cargado | Bloques activados | Validaciones clave | Resultado |
|---|---|---|---|---|---|
| 1 | contrato / vivienda / completa / permanente / tensionada | contrato-arrendamiento-vivienda.md | vivienda, zona_tensionada | duracion 5/7, Art. 17.6, IRAV, fianza 1 | PASA |
| 2 | contrato / vivienda / completa / temporal / temporada | contrato-arrendamiento-temporada.md | temporada (Art. 3.2) | causa real, sin Titulo II, fianza 2 | PASA |
| 3 | comunicacion / no renovacion / arrendador | comunicacion-no-renovacion.md | preaviso 4 meses | Art. 10.1 (4 meses), sin bloque 2 meses | PASA |

Conclusion: el arbol ampliado enruta correctamente las 7 hojas, activa solo los bloques de la rama recorrida, no re-pregunta datos resueltos por escucha activa y aplica las validaciones legales (LAU, Ley 12/2023, IRAV, CC). Pendiente en produccion: verificacion en vivo del BOE y del valor del IRAV en cada lanzamiento (Punto 2 de la skill).

---

## Revision UX

Hallazgos detectados durante el diseno y la ejecucion de los tests, y ajustes ya aplicados a la skill/assets:

1. **Comentario HTML colgante en las advertencias del asset de vivienda.** La advertencia 3 era `> 3. <!-- Si zona tensionada: ... -->`: si la condicion no se cumplia, el documento escrito quedaba con un "3." vacio y la numeracion rota (basura visible en el render de la GUI). **Ajuste aplicado:** la advertencia condicional se movio a un comentario de linea propia con instruccion de insercion como advertencia numerada adicional; la lista fija quedo renumerada 1-4.
2. **Comentario HTML incrustado a mitad de frase (clausula SEGUNDA de vivienda).** `...del ARRENDATARIO <!-- y de las siguientes personas: {{personas_convivientes}} -->, de conformidad...` dejaba, al omitirse, un espacio doble antes de la coma, y al aplicarse era ambiguo (la regla global inserta los bloques como linea propia). **Ajuste aplicado:** convertido en comentario condicional de parrafo propio.
3. **Clausula de actualizacion desactualizada (IPC -> IRAV).** La QUINTA de vivienda seguia usando IGC/IPC como tope, derogado en la practica para contratos desde el 26/05/2023 por la Resolucion INE del IRAV (vigente desde 01/01/2025). Habria generado contratos con un tope ilegal. **Ajuste aplicado:** clausula QUINTA reescrita con el IRAV y el Art. 18.2 (exigibilidad desde el mes siguiente); referencias y guardrails actualizados.
4. **Pregunta de finalidad innecesaria en la rama local.** El arbol anterior preguntaba "uso permanente o temporal" tambien para locales y detenia el proceso si era temporal; un local es siempre uso distinto de vivienda y su duracion es de libre pacto. **Ajuste aplicado:** la rama local enruta directa al asset sin V1 (una pregunta menos y desaparece un rechazo erroneo).
5. **"No lo se" como respuesta valida en zona tensionada.** Exigir si/no al cliente sobre un dato publico bloqueaba el flujo. **Ajuste aplicado:** V6 ofrece "No lo se" y difiere la resolucion a la verificacion oficial que el agente hace por si mismo con el municipio (seccion 5.A.1); si el cliente contesta si/no, la fuente oficial prevalece en caso de contradiccion.
6. **Preguntas de clasificacion suprimidas cuando solo hay una respuesta posible.** En habitacion el arrendatario es siempre persona fisica (V4 no se pregunta) y en devolucion de fianza el remitente es siempre el arrendatario (V8 no se pregunta). Evita turnos vacios de contenido.
7. **Limite del Art. 36.5 LAU ausente en garantias adicionales.** El comentario condicional de garantia adicional del asset de vivienda no recogia el tope de 2 mensualidades en contratos de hasta 5/7 anos. **Ajuste aplicado:** el bloque insertable declara el cumplimiento del limite y la seccion 5.A.7 obliga a explicarlo antes de pactar (clausula de negociacion).
8. **Validaciones de fechas en comunicaciones como paso obligatorio, no opcional.** El preaviso del Art. 10.1 y el mes del Art. 36.4 son los dos errores mas costosos para el cliente (prorroga no deseada / requerimiento prematuro). **Ajuste aplicado:** guardrails 9 y 10 + validacion explicita en 5.B.3 con advertencia de extemporaneidad.

Sin hallazgos pendientes: los 8 ajustes estan aplicados en `SKILL.md`, los assets y las references de la skill.

---

## Seguimiento al hallazgo B.1 (placeholders no desnudos)

El agente de QA en vivo corrigio los 9 casos de `contrato-arrendamiento-vivienda.md` y senalo 38 casos mas sin corregir en los otros 6 assets de la skill. Verificados y corregidos los 42 restantes (`comunicacion-no-renovacion.md`, `comunicacion-actualizacion-renta.md`, `contrato-arrendamiento-local.md`, `contrato-arrendamiento-habitacion.md`, `contrato-arrendamiento-temporada.md`, `requerimiento-devolucion-fianza.md`) con un script que extrae `{{nombre: texto de ayuda}}` -> `{{nombre}}`, preservando el nombre del placeholder. Verificado por grep: cero placeholders con texto de ayuda interno en toda la skill. Confirmado ademas que el `SKILL.md` (guardrails 7 y 10, y las secciones marcadas [negociacion]) ya explica los valores por defecto legales (fianza minima, indices, plazos) que antes vivian dentro de las llaves, por lo que no se pierde informacion sustantiva al desnudar los placeholders.

## Verificacion en vivo + calidad LLM

Ejecucion real (no simulada sobre el papel): un agente sin contexto previo de la skill se puso en el rol del LLM operativo gobernado por `SKILL.md`, sostuvo una conversacion completa haciendo tambien de cliente sintetico, y aplico `Write`/`Read`/`Edit` de verdad sobre `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/arrendamiento-qa-prueba.md`. Peticion inicial: *"Quiero alquilar mi piso en Barcelona como vivienda habitual a una familia. La renta seria 900 euros al mes. No se si Barcelona esta en zona tensionada."* Datos sinteticos: Arrendador A / NIF 00000000-T, Arrendatario A / NIF 11111111-H.

### Extractos literales de la conversacion

Introduccion fija + primera pregunta de clasificacion (turno 1, unica vez):
```
Vamos a proceder a la elaboración de su documento de arrendamiento. Para ajustarlo
correctamente a su caso, es necesario precisar antes algunos datos.

El arrendador es:
1. Persona física
2. Empresa (persona jurídica)
```

Confirmacion visible (Punto 3), con la norma aplicable y el enlace al BOE, tras resolver V3/V4 en silencio:
```
Al presente caso le resulta de aplicación la Ley 29/1994, de Arrendamientos Urbanos
(LAU), en concreto los artículos 2 y 9 (vivienda habitual y duración), 17 a 20 (renta
y gastos) y 36 (fianza), en su versión consolidada vigente desde el 25 de mayo de 2023
(Ley 12/2023). Dado que el inmueble se encuentra en Barcelona, cabe además la
aplicación de la Ley 12/2023 y de los artículos 10.3, 17.6 y 17.7 de la LAU, relativos
a las zonas de mercado residencial tensionado; este extremo se verificará y le
informaré del resultado al fijar la ubicación del inmueble. Puede consultar el texto
oficial en el BOE en el siguiente enlace: https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003

¿Qué documento desea utilizar como base?
1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
2. Adjuntar su propio documento
```

Apertura de la seccion 1 con verificacion real de zona tensionada (`web_search` efectivo, no simulado — Resolucion de 14/03/2024, BOE-A-2024-5214) y clausula lista para confirmar:
```
Procedemos a determinar la ubicación del inmueble, a los efectos de verificar su
posible sujeción a los límites de renta en zona de mercado residencial tensionado.

He verificado la declaración de zona de mercado residencial tensionado publicada en
el Boletín Oficial del Estado: Barcelona figura entre los municipios de Cataluña
declarados zona de mercado residencial tensionado por Resolución de 14 de marzo de
2024 de la Secretaría de Estado de Vivienda y Agenda Urbana (BOE-A-2024-5214), con
una vigencia de tres años desde su publicación.

La cláusula quedaría así:

El inmueble se ubica en Barcelona, Comunidad Autónoma de Cataluña. Al encontrarse en
zona de mercado residencial tensionado conforme a la Ley 12/2023, el contrato
incorporará el límite de renta del artículo 17.6 de la LAU y la posibilidad de
prórroga extraordinaria del artículo 10.3 de la LAU a solicitud del arrendatario.

¿Confirmamos esta cláusula?
```

Cláusula de duración con la explicación del mínimo legal antes de pedir la decisión (negociación, no registro mecánico):
```
Determinado el objeto, corresponde fijar la duración del arrendamiento.

Al ser usted arrendador persona física, la ley establece una duración mínima de 5
años: si pacta un plazo inferior, el contrato se prorrogará obligatoriamente año a
año hasta alcanzarlo, salvo que usted desee acogerse directamente a ese mínimo legal.
¿Qué duración desea pactar: un número concreto de años o el mínimo legal de 5 años?
```

Cláusula de renta con el matiz del Art. 17.6 (sin contrato anterior, el límite no aplica — validación de sentido jurídico, no solo de dato):
```
Al no existir un contrato de arrendamiento anterior sobre esta vivienda en los
últimos cinco años, no resulta de aplicación el límite del artículo 17.6 de la LAU,
que solo opera cuando hay una renta anterior de referencia. Tampoco resulta de
aplicación el límite del índice de precios de referencia del artículo 17.7,
reservado a los grandes tenedores (más de cinco inmuebles urbanos de uso
residencial en esta zona tensionada, según la declaración vigente), condición que
no concurre en usted según los datos aportados.
```

Cláusula de actualización — IRAV, la más delicada (explicación del tope legal antes de la decisión):
```
Establecida la renta, corresponde determinar su índice de actualización.

En los contratos de arrendamiento de vivienda habitual celebrados desde el 26 de
mayo de 2023, la ley no permite pactar un incremento anual de la renta superior a
la variación del Índice de Referencia para la Actualización de los Arrendamientos
de Vivienda (IRAV), que publica mensualmente el Instituto Nacional de Estadística
en desarrollo de la Ley 12/2023; no cabe pactar el IPC ni ningún otro índice que
pueda superarlo. ¿Desea que la actualización se realice conforme al IRAV, que es el
límite legal, o prefiere fijar un índice distinto siempre que no exceda ese límite?
```

Documento final (fragmento real tras los `Edit`, ruta `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/arrendamiento-qa-prueba.md`):
```
CLAUSULA ESPECIAL — ZONA DE MERCADO RESIDENCIAL TENSIONADO. El inmueble se ubica en
Barcelona, declarado zona de mercado residencial tensionado conforme a la Resolucion
de 14 de marzo de 2024 de la Secretaria de Estado de Vivienda y Agenda Urbana
(BOE-A-2024-5214), dictada al amparo del articulo 18 de la Ley 12/2023. La prorroga
extraordinaria prevista en el articulo 10.3 de la LAU sera de aplicacion a solicitud
del ARRENDATARIO.
...
Al no existir un contrato de arrendamiento anterior sobre esta misma vivienda en los
ultimos cinco años, no resulta de aplicacion el limite de renta del articulo 17.6 de
la LAU, que opera unicamente cuando existe una renta anterior de referencia.
```

### A) Calidad de la respuesta del LLM

- **Tono formal, "usted", sin coloquialismos:** se sostiene en las 27 respuestas generadas. Verbos precisos ("indíqueme", "confirmamos") en vez de "dime/pon". Ningun "vale/genial/perfecto".
- **Claridad de las clausulas de negociacion:** buena. Antes de cada decision del cliente (duracion, renta en zona tensionada, actualizacion, fianza) se explico el regimen legal por defecto, tal como exige la seccion "Diálogo y acuerdo" del `SKILL.md`. El caso de la renta sin contrato anterior obligo a razonar mas alla de un simple "aplica/no aplica" — el agente tuvo que distinguir el Art. 17.6 (renta de referencia anterior) del 17.7 (gran tenedor), algo que el `SKILL.md` no explicita pero que se dedujo correctamente de las references (`fuentes-plantillas-validadas.md`).
- **Directiva de invisibilidad:** respetada. Nunca se menciono "V3", "V6", "vector", "fase" ni "ahora voy a".
- **Cero invenciones:** la cita de la Resolucion de zona tensionada (BOE-A-2024-5214, 14/03/2024) proviene de una busqueda `web_search` real ejecutada durante esta prueba, no de memoria. El unico punto delicado es el organismo de deposito de fianza: el agente escribio "el organismo autonomico competente de Cataluña" y "el plazo legalmente establecido" en vez de nombrar la Agencia de l'Habitatge de Catalunya y el plazo de 2 meses, precisamente para NO inventar un dato no verificado en esta sesion — correcto por cautela, pero expone que el `SKILL.md` nunca instruye verificar ese dato con `web_search` (a diferencia de la zona tensionada, que si lo exige explicitamente en 5.A.1). Ver hallazgo 4 abajo.
- **Preguntas de clasificacion simples:** V3 y V4 se formularon con el texto exacto del arbol, opciones numeradas, sin duplicar informacion ya conocida (V0/V2/V5/V1/V6 no se re-preguntaron porque la peticion inicial ya los resolvia).

### B) El asset visto desde el LLM que lo rellena

- **Placeholders ambiguos encontrados y corregidos (hallazgo 1, critico):** nueve placeholders de `contrato-arrendamiento-vivienda.md` no eran "desnudos" — llevaban texto de ayuda dentro de las llaves, ej. `{{naturaleza_arrendador: persona fisica / persona juridica}}`, `{{indice_actualizacion: IRAV / otro indice pactado}}`, `{{organismo_deposito_fianza: nombre del organismo autonomico competente}}`. Esto viola la convencion "placeholders desnudos" de `PLUGIN_AUTHORING_GUIDE.md` §4.1: si ese campo llega a quedar sin resolver al cerrar el documento, el cliente veria el texto de ayuda interno tal cual en su editor rich-text — el mismo incidente que ya motivo la convencion. **Corregido:** los 9 placeholders se dejaron desnudos (`{{naturaleza_arrendador}}`, etc.). El mismo patron existe tambien, sin corregir todavia, en el resto de assets de esta skill (`contrato-arrendamiento-temporada.md`: 14 casos, `contrato-arrendamiento-local.md`: 10, `contrato-arrendamiento-habitacion.md`: 9, `comunicacion-actualizacion-renta.md`: 4, `comunicacion-no-renovacion.md`: 3, `requerimiento-devolucion-fianza.md`: 2) — pendiente de una pasada de limpieza equivalente.
- **Bloque condicional confuso de resolver (hallazgo 2, corregido):** en el ANEXO I de inventario, el comentario `<!-- Si la vivienda se arrienda amueblada, incluir inventario detallado -->` solo envolvia esa frase — la tabla de `{{elemento_1}}/{{estado_1}}` que venia justo debajo NO estaba dentro del comentario, asi que se imprimia siempre, amueblada o no. Se detecto al redactar el documento de prueba (vivienda sin datos de inventario) y aparecia una tabla vacia con placeholders sueltos. **Corregido:** la tabla completa se movio dentro del comentario condicional, para que se omita entera cuando no aplica.
- **Placeholder generico que rompe la precision del `Edit` (hallazgo 3, corregido en `SKILL.md`):** el guardrail 11 ordenaba literalmente "marcar todos los campos a rellenar con `{{DATO_FALTANTE}}`", que contradice el propio diseno del asset (placeholders con nombre propio) y, tomado al pie de la letra, generaria decenas de placeholders identicos en el mismo documento — el `oldString` de un `Edit` posterior no podria dirigirse a un campo concreto sin arrastrar los demas. Se reformulo el guardrail para exigir el nombre propio de la plantilla y prohibir explicitamente el literal generico.
- **Dato objetivo nunca preguntado (hallazgo 4, corregido en `SKILL.md`):** el encabezamiento del contrato ("En {{municipio}}, a {{fecha_contrato}}") no correspondia a ningun apartado de la seccion 5.A — ninguna de las 9 secciones pedia el lugar/fecha de firma, a diferencia de las comunicaciones (5.B.4 si lo hace). Sin ese apartado, esos dos campos quedarian sin resolver para siempre en todo contrato. Se anadio una instruccion en la seccion 4 (Duracion) para fijarlos junto con la fecha de inicio.
- **Dato sin ruta de verificacion (hallazgo 5, no corregido, pendiente):** `{{organismo_deposito_fianza}}` y `{{plazo_deposito}}` (clausula SEXTA) dependen de la comunidad autonoma del inmueble (en Cataluña, Agencia de l'Habitatge de Catalunya, plazo de 2 meses; en Madrid, IVIMA, plazo distinto) pero la seccion 5.A.7 no exige verificarlos con `web_search` como si exige para la zona tensionada en 5.A.1. Sin esa instruccion, el agente queda entre inventar el organismo (prohibido) o dejarlo generico ("el organismo autonomico competente") indefinidamente. Recomendacion para una proxima iteracion: anadir a 5.A.7 una verificacion equivalente a la de 5.A.1.
- **¿Suena a contrato real o a plantilla mal encajada?** Leido de corrido, el documento final suena a contrato real: las clausulas de zona tensionada y de ausencia de renta anterior se integran como parrafos propios sin residuos de sintaxis de plantilla. La unica aspereza es la referencia catastral, que queda correctamente como `{{referencia_catastral}}` (el cliente no la tenia a mano) — eso es el comportamiento correcto de la Regla 11, no un defecto.

### Correcciones aplicadas en esta sesion

1. `assets/contrato-arrendamiento-vivienda.md`: 9 placeholders con texto de ayuda incrustado convertidos a placeholders desnudos.
2. `assets/contrato-arrendamiento-vivienda.md`: tabla de inventario de mobiliario movida dentro de su comentario condicional (antes se imprimia siempre).
3. `SKILL.md` guardrail 11: aclarado para exigir el nombre propio del placeholder y prohibir el literal generico `{{DATO_FALTANTE}}` que rompia la precision del `Edit`.
4. `SKILL.md` seccion 5.A.4 (Duracion): añadida la instruccion, ausente hasta ahora, de fijar el lugar y la fecha de firma del encabezamiento del contrato.

Pendiente para una proxima iteracion (no corregido en esta sesion, fuera del alcance quirurgico de este test): replicar la limpieza de placeholders desnudos en los otros 6 assets de la skill (38 casos mas), y anadir a 5.A.7 una verificacion por `web_search` del organismo y plazo de deposito de fianza segun la comunidad autonoma.

Resultado: **PASA con reservas** — el arbol de clasificacion, el tono y las clausulas de negociacion funcionan correctamente en ejecucion real; se encontraron y corrigieron 4 defectos reales de la plantilla/skill, y queda 1 hallazgo documentado sin corregir por alcance.
