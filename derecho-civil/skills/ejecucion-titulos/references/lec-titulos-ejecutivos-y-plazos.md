# Titulos Ejecutivos, Plazos y Postulacion (LEC, Libro III)

> Material de referencia interno de la skill `derecho-civil-ejecucion-titulos`. Resume el regimen verificado en el BOE el
> 31/08/2026 (texto consolidado BOE-A-2000-323) que gobierna el arbol de decision. No es texto visible al usuario.
> Fuente y fechas de verificacion: `references/fuentes-plantillas-validadas.md`.

---

## 1. Que es un titulo ejecutivo (art. 517.2 LEC)

La accion ejecutiva debe fundarse en un titulo que lleve aparejada ejecucion. Solo la llevan los del art. 517.2:

| Nº | Titulo | Clasificacion de la skill |
|---|---|---|
| 1.º | La sentencia de condena firme | JUDICIAL |
| 2.º | Los laudos o resoluciones arbitrales y los acuerdos de mediacion elevados a escritura publica, asi como los acuerdos alcanzados en cualquier otro medio adecuado de solucion de controversias igualmente elevados a escritura publica | NO JUDICIAL |
| 3.º | Las resoluciones judiciales que aprueben u homologuen transacciones judiciales y acuerdos logrados en el proceso | JUDICIAL |
| 4.º | La copia de la escritura publica matriz que el interesado solicite que se expida con tal caracter | NO JUDICIAL |
| 5.º | El testimonio notarial del original de la poliza conservada en el Libro-Registro, o su copia autorizada, con la certificacion del art. 572.2 | NO JUDICIAL |
| 6.º | Titulos al portador o nominativos que representen obligaciones vencidas, y sus cupones vencidos | NO JUDICIAL |
| 7.º | Certificados no caducados de los registros contables de valores representados por anotaciones en cuenta | NO JUDICIAL |
| 8.º | El auto que fija la cantidad maxima reclamable por indemnizacion en procesos penales por hechos cubiertos por el seguro obligatorio de vehiculos | JUDICIAL (con especialidad de oposicion, art. 556.3) |
| 9.º | Las demas resoluciones procesales y documentos que por disposicion legal lleven aparejada ejecucion | Segun su naturaleza |

**Los numeros 2.º, 4.º, 5.º y 7.º fueron modificados por la LO 1/2025, con efectos de 3 de abril de 2025.** Dos consecuencias practicas:

- El 4.º ya no habla de "primera copia" ni de segunda copia con mandamiento judicial: basta **la copia de la escritura publica matriz que el interesado solicite que se expida con tal caracter**. Redactar el escrito con la formula antigua es un error.
- El 2.º incorpora expresamente, junto a los acuerdos de mediacion, los acuerdos de **cualquier otro MASC** elevados a escritura publica.

### El decreto que pone fin a un monitorio sin oposicion (art. 816 LEC)

Si el deudor requerido en un proceso monitorio no paga ni comparece, el Letrado de la Administracion de Justicia dicta decreto dando por terminado el monitorio y **da traslado al acreedor para que inste el despacho de ejecucion, bastando para ello con la mera solicitud**. Despachada la ejecucion, prosigue conforme a lo previsto para las sentencias judiciales. Desde el auto de despacho la deuda devenga el interes del art. 576.

Clasificacion de la skill: **JUDICIAL**, con dos particularidades — la demanda puede limitarse a la solicitud de despacho (art. 549.2), y la postulacion sigue la regla especifica del art. 539.1 (abogado y procurador solo si la cantidad excede de 2.000 euros).

### El convenio regulador y las medidas de familia

Los pronunciamientos sobre medidas se ejecutan con arreglo al Libro III con las especialidades del art. 776 (ver `references/especialidades-familia-776.md`). El titulo puede ser la sentencia, el decreto de aprobacion del convenio o la escritura publica que lo formalice (asi lo presupone el art. 608 al enumerar "decretos o escrituras publicas que formalicen el convenio regulador").

---

## 2. Caducidad de la accion ejecutiva (art. 518 LEC)

> La accion ejecutiva fundada en sentencia, en resolucion del tribunal o del Letrado de la Administracion de Justicia que apruebe una transaccion judicial o un acuerdo alcanzado en el proceso, en resolucion arbitral o en acuerdo de mediacion **caducara si no se interpone la correspondiente demanda ejecutiva dentro de los cinco anos siguientes a la firmeza** de la sentencia o resolucion.

Puntos operativos:

- El plazo es de **caducidad**, no de prescripcion: no se interrumpe por reclamaciones extrajudiciales.
- El dies a quo es la **firmeza**, no la fecha de la resolucion.
- Alcanza a los titulos judiciales y asimilados y a los laudos y acuerdos de mediacion. **NO alcanza a la escritura publica notarial**, cuya accion se rige por los plazos de prescripcion de la obligacion documentada (art. 1964 del Codigo Civil para las personales sin plazo especial).
- En pensiones periodicas de familia, cada mensualidad tiene su propio vencimiento; el titulo no caduca por el transcurso de cinco anos desde la sentencia si se ejecutan mensualidades posteriores, pero **si es determinante para las mensualidades mas antiguas**. Ante la duda concreta, escalar.
- Si el plazo esta agotado: **detener, advertir y no redactar la demanda**. La caducidad es ademas motivo de oposicion del ejecutado (art. 556.1, parrafo segundo).

---

## 3. Plazo de espera de veinte dias (art. 548 LEC)

> No se despachara ejecucion de resoluciones procesales o arbitrales o de acuerdos de mediacion, dentro de los **veinte dias posteriores** a aquel en que la resolucion de condena sea firme, o la resolucion de aprobacion del convenio o de firma del acuerdo haya sido notificada al ejecutado.

- Se aplica a titulos judiciales, laudos y acuerdos de mediacion. **NO se aplica a las escrituras publicas notariales ni a los demas titulos no judiciales del art. 520**: esos pueden ejecutarse desde el vencimiento de la obligacion.
- Unica excepcion expresa en la ley: **art. 549.4**, ejecucion de condenas de desahucio por falta de pago o por expiracion del plazo.
- **Familia:** la ley no exceptua las resoluciones de familia. Ver la nota "verificar manualmente" en `references/fuentes-plantillas-validadas.md`: la skill mantiene la posicion conservadora de computar los veinte dias, advirtiendo de que existe jurisprudencia menor en contra para mensualidades ya vencidas.
- Efecto de presentar antes de tiempo: el juzgado no despachara la ejecucion todavia. No caduca nada, pero se pierde tiempo y puede generar costas inutiles.

---

## 4. Requisitos del titulo NO judicial (art. 520 LEC)

Para los titulos de los numeros 4.º, 5.º, 6.º y 7.º del art. 517.2 **solo podra despacharse ejecucion por cantidad determinada que exceda de 300 euros**:

1. En dinero efectivo.
2. En moneda extranjera convertible, si la obligacion de pago en esa moneda esta autorizada o permitida legalmente.
3. En cosa o especie computable en dinero.

El limite puede alcanzarse **sumando varios titulos ejecutivos** de los mismos numeros (art. 520.2).

Ademas la cantidad debe ser **liquida** (art. 572.1): determinada y expresada en el titulo con letras, cifras o guarismos comprensibles. Si hay discordancia entre expresiones, prevalece la escrita con letras. No necesita ser liquida la cantidad que se pida para intereses de la ejecucion y costas.

### Ejecucion por saldo de operaciones (arts. 572.2, 573 y 574)

Cabe cuando el titulo es escritura publica o poliza intervenida **y en el propio titulo se pacto** que la cantidad exigible sera la resultante de la liquidacion practicada por el acreedor en la forma convenida. Requisitos acumulativos:

- Acreditar la **notificacion previa** al ejecutado y al fiador, si lo hay, de la cantidad exigible resultante de la liquidacion (art. 572.2, parrafo segundo).
- Acompanar a la demanda (art. 573.1): documento del saldo con el extracto de partidas de cargo, abono e intereses; documento fehaciente de haberse liquidado en la forma pactada; y documento de la notificacion al deudor y al fiador.
- Si el interes es **variable** o hay paridades de moneda, expresar en la demanda las operaciones de calculo (art. 574).
- Si el acreedor duda de alguna partida, puede pedir el despacho por la cantidad indubitada y reservar el resto para el declarativo (art. 573.3).

---

## 5. Tribunal competente (art. 545 LEC)

| Titulo | Tribunal competente |
|---|---|
| Resolucion judicial, resolucion del LAJ con caracter de titulo ejecutivo, transaccion o acuerdo homologado judicialmente | El tribunal que conocio del asunto **en primera instancia**, o el que homologo o aprobo la transaccion o acuerdo (545.1) |
| Laudo arbitral o acuerdo de mediacion | Juzgado de Primera Instancia del **lugar en que se dicto el laudo o se firmo el acuerdo** (545.2) |
| Demas titulos (escritura publica, poliza, titulos al portador, certificados) | Juzgado de Primera Instancia del lugar que corresponda por los arts. 50 y 51; **a eleccion del ejecutante**, tambien el del lugar de cumplimiento de la obligacion segun el titulo, o el de cualquier lugar donde haya bienes embargables del ejecutado (545.3) |

**En ningun caso son aplicables las reglas de sumision expresa o tacita** en el supuesto del 545.3. Si hay varios ejecutados, es competente el tribunal que lo sea respecto de cualquiera de ellos, a eleccion del ejecutante.

---

## 6. Postulacion (art. 539.1 LEC, redaccion de la LO 1/2025)

Regla general: **ejecutante y ejecutado deben estar dirigidos por letrado y representados por procurador**, salvo que se trate de la ejecucion de resoluciones dictadas en procesos en que no fuera preceptiva la intervencion de esos profesionales.

Dos reglas especificas de 2.000 euros:

- **Ejecucion derivada de proceso monitorio en que no hubo oposicion:** abogado y procurador solo si la cantidad por la que se despache ejecucion es **superior a 2.000 euros**.
- **Ejecucion derivada de acuerdo de mediacion o laudo arbitral:** misma regla, superior a 2.000 euros.

Consecuencia practica del arbol: para saber si son preceptivos en la ejecucion de una sentencia hay que mirar el proceso de origen. Si la sentencia se dicto en un juicio verbal de cuantia no superior a 2.000 euros, donde no eran preceptivos (arts. 23.2.1.º y 31.2.1.º), tampoco lo son en su ejecucion.

### Costas y gastos de la ejecucion (art. 539.2)

Las costas del proceso de ejecucion **son a cargo del ejecutado sin necesidad de expresa imposicion**, salvo las actuaciones para las que la ley prevea pronunciamiento expreso sobre costas y las que se realicen a instancia del ejecutado o de otros sujetos. Hasta su liquidacion, el ejecutante debe ir anticipando los gastos que se produzcan.

---

## 7. Contenido y documentos de la demanda ejecutiva (arts. 549 y 550)

**Art. 549.1 — contenido:**

1. El titulo en que se funda el ejecutante.
2. La tutela ejecutiva que se pretende, precisando la cantidad conforme al art. 575.
3. Los bienes del ejecutado susceptibles de embargo de los que se tenga conocimiento y, en su caso, si se consideran suficientes.
4. En su caso, las medidas de localizacion e investigacion que se interesen al amparo del art. 590.
5. Las personas frente a las que se pretende el despacho, con sus circunstancias identificativas, por aparecer en el titulo como deudores o por estar sujetas conforme a los arts. 538 a 544.

**Art. 549.2 — demanda sucinta:** si el titulo es una resolucion del LAJ o una sentencia o resolucion dictada por el tribunal competente para conocer de la ejecucion, la demanda **puede limitarse a solicitar que se despache la ejecucion**, identificando la resolucion. La skill no explota esta simplificacion al maximo: mantiene un escrito completo pero breve, porque el desglose del art. 575 y la designacion de bienes siguen siendo necesarios.

**Art. 550.1 — documentos:**

1. El titulo ejecutivo, **salvo que la ejecucion se funde en sentencia, decreto, acuerdo o transaccion que conste en los autos**. Si es laudo, ademas el convenio arbitral y la acreditacion de su notificacion a las partes. Si es acuerdo de mediacion o de otro MASC elevado a escritura publica, ademas **copia de las actas de la sesion constitutiva y final** del procedimiento (redaccion de la LO 1/2025).
2. La certificacion del registro electronico de apoderamientos judiciales o la referencia a su numero, cuando no conste ya en las actuaciones.
3. Los documentos que acrediten precios o cotizaciones para computar en dinero deudas no dinerarias, salvo datos oficiales o de publico conocimiento.
4. Los demas documentos que la ley exija.

---

## 8. La cantidad por la que se despacha (arts. 575 y 576)

**Art. 575.1.** La ejecucion se despacha por:

```
principal
+ intereses ordinarios y moratorios YA VENCIDOS
+ cantidad provisional para intereses de la ejecucion y costas
```

La cantidad provisional **no puede superar el 30 % de lo que se reclame en la demanda ejecutiva**, sin perjuicio de la posterior liquidacion. Excepcionalmente puede excederse si el ejecutante justifica que, atendida la previsible duracion de la ejecucion y el tipo de interes aplicable, ese limite se quedara corto.

**Art. 575.1 bis.** En ejecucion de **vivienda habitual**, las costas exigibles al ejecutado no pueden superar el **5 %** de lo reclamado en la demanda ejecutiva.

**Art. 575.2.** El tribunal no puede denegar el despacho porque entienda que la cantidad debida es distinta de la fijada por el ejecutante; queda a salvo la pluspeticion que alegue el ejecutado.

**Art. 575.3.** **No se despachara ejecucion si la demanda no expresa los calculos** de los articulos anteriores o no acompana los documentos exigidos. De ahi la regla de estilo: desglosar siempre.

**Art. 576 — mora procesal.** Desde que se dicta en primera instancia, toda sentencia o resolucion que condene al pago de cantidad liquida devenga en favor del acreedor un interes anual igual al **interes legal del dinero incrementado en dos puntos**, o el que corresponda por pacto o por disposicion especial. Se aplica a resoluciones judiciales de cualquier orden, laudos y acuerdos de mediacion.

**Art. 578 — ampliacion por nuevos vencimientos.** Si vence algun plazo de la misma obligacion despues de despachada la ejecucion, esta se entiende ampliada por el importe de los nuevos vencimientos de principal e intereses si lo pide el actor, sin retrotraer el procedimiento. **La ampliacion automatica puede solicitarse ya en la demanda ejecutiva**: entonces el ejecutado es advertido al notificarle el auto de despacho de que la ejecucion se ampliara automaticamente si no consigna en cada vencimiento, y el ejecutante debera presentar una liquidacion final. Es la herramienta natural de las pensiones periodicas.

---

## 9. Sujetos frente a los que cabe despachar (arts. 538 a 544)

Solo cabe despachar ejecucion, a instancia de quien aparezca como acreedor en el titulo, frente a (art. 538.2):

1. Quien aparezca como **deudor en el mismo titulo**.
2. Quien, sin figurar como deudor en el titulo, **responda personalmente de la deuda por disposicion legal o en virtud de afianzamiento acreditado mediante documento publico**.
3. Quien, sin figurar como deudor, sea **propietario de bienes especialmente afectos** al pago, si la afeccion deriva de la ley o se acredita con documento fehaciente. La ejecucion se concreta a esos bienes.

**Art. 538.4:** el ejecutante que induzca al tribunal a extender la ejecucion frente a personas o bienes que el titulo o la ley no autorizan **responde de los danos y perjuicios**. De ahi el guardrail de la skill.

**Art. 540 — sucesion:** cabe a favor o frente al sucesor acreditado con documentos fehacientes; si no lo estan, hay traslado y comparecencia previa.

**Art. 542 — deudor solidario:** los titulos ejecutivos **judiciales** obtenidos solo frente a algunos deudores solidarios **no sirven de titulo frente a los que no fueron parte**. En titulos extrajudiciales solo cabe frente al deudor solidario que figure en ellos o en otro documento que acredite la solidaridad y lleve aparejada ejecucion. Si en el titulo aparecen varios deudores solidarios, puede pedirse el despacho por el importe total frente a uno, varios o todos.

---

## 10. Control de oficio de clausulas abusivas (arts. 551.2.5.º y 552)

Cuando la ejecucion se funda en un **titulo extrajudicial** derivado de un contrato entre empresario o profesional y consumidor:

- El auto de despacho debe expresar que las clausulas que fundan la ejecucion y que determinan la cantidad exigible **no son abusivas** (art. 551.2.5.º, redaccion de la LO 1/2025), y advertir al deudor de que puede oponerse a esa valoracion y de que si no lo hace en tiempo y forma no podra impugnarla despues (art. 551.4).
- Si el tribunal aprecia posible abusividad, da audiencia de quince dias a las partes y resuelve en cinco dias habiles conforme al art. 561.1.3.ª. Firme el auto, el pronunciamiento sobre abusividad **tiene eficacia de cosa juzgada** (art. 552.4).
- La abusividad es tambien motivo de oposicion del ejecutado (art. 557.1.7.ª).

Consecuencia para la skill: en la hoja NO JUDICIAL con consumidor, informar de este control antes de cerrar la cuantia y, si la clausula que determina el importe es potencialmente abusiva (intereses moratorios desproporcionados, vencimiento anticipado, comisiones), advertir y ofrecer revision por especialista.

---

## 11. Concurso del ejecutado (arts. 142 y 143 TRLC)

- **Art. 142 TRLC:** desde la declaracion de concurso **no podran iniciarse** ejecuciones singulares, judiciales o extrajudiciales, ni apremios administrativos, contra los bienes o derechos de la masa activa.
- **Art. 143.1 TRLC:** las ejecuciones en tramitacion **quedan en suspenso** desde la declaracion de concurso, y son **nulas** cuantas actuaciones se hubieran realizado desde ese momento.

Ademas, el art. 551.1 LEC obliga al Letrado de la Administracion de Justicia a **consultar el Registro Publico Concursal** con caracter previo al despacho.

Consecuencia para la skill: si consta o se sospecha concurso del ejecutado, **detener** y derivar a concursal. No preparar la demanda.
