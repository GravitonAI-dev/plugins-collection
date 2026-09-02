# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-contratos-particulares`. Registra las fuentes normativas y las
> plantillas validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso de verificacion se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local, se informa al usuario y se marca el punto como pendiente de verificacion manual. **Prohibido dar por vigente lo que no se ha podido verificar.**

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Codigo Civil (texto consolidado) | BOE-A-1889-4763 | articulos de contratos, prestamo, comodato, compraventa, fianza y prescripcion verificados el 03/09/2026 (detalle en la tabla siguiente) | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| Ley de 23 de julio de 1908 sobre nulidad de los contratos de prestamos usurarios (Ley Azcarate) | BOE-A-1908-5579 | **VIGENTE**: la API del BOE devuelve `estatus_derogacion = N` y `vigencia_agotada = N`; ultima actualizacion del consolidado 16/12/2025. Texto sin modificaciones desde su promulgacion (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-1908-5579 |
| LEC — Ley 1/2000 de Enjuiciamiento Civil (arts. 517 y 520, para la fuerza ejecutiva de la escritura publica) | BOE-A-2000-323 | art. 517.2.4.º en la redaccion de la LO 1/2025, efectos 03/04/2025; art. 520 con la conversion a euros del RD 1417/2001 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| Ley 31/2022, de PGE para 2023 (disposicion adicional 42.ª, interes legal del dinero) | BOE-A-2022-22128 | ultima fijacion expresa del interes legal del dinero: **3,25 %**, "hasta el 31 de diciembre del año 2023" (bloque `da-42`, verificado 03/09/2026). Ver la advertencia de magnitud variable mas abajo | https://www.boe.es/buscar/act.php?id=BOE-A-2022-22128 |

**Endpoint de verificacion articulo por articulo (API de legislacion consolidada del BOE).** Devuelve todas las versiones historicas del precepto; **la ultima es la vigente**. Requiere cabecera `Accept: application/xml`:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{numero}
```

Ejemplo: `.../bloque/art1755` para el art. 1755 CC.

**Aviso sobre el formato del identificador de bloque:** no todas las normas usan la misma convencion. El Codigo Civil usa `art{numero}` (`art1755`); la LEC usa `a{numero}` (`a517`); la Ley Azcarate usa `a{numero}` (`a1`, `a3`); las disposiciones adicionales de una ley de presupuestos usan `da-{numero}` (`da-42`). Si un identificador devuelve 404, probar la otra convencion antes de darlo por inaccesible.

---

## Articulos del Codigo Civil verificados el 03/09/2026

| Articulo | Materia | Redaccion vigente verificada |
|---|---|---|
| 1088 | Contenido de la obligacion | Toda obligacion consiste en dar, hacer o no hacer alguna cosa |
| 1091 | Fuerza vinculante | Las obligaciones nacidas de contrato tienen fuerza de ley entre las partes y deben cumplirse a tenor de los mismos |
| 1100 | Mora | Se incurre en mora desde que el acreedor exige judicial o extrajudicialmente el cumplimiento. No hace falta intimacion cuando la obligacion o la ley lo declaren asi expresamente, o cuando la fecha fue motivo determinante |
| 1101 | Indemnizacion | Responde de daños y perjuicios quien incurre en dolo, negligencia o morosidad |
| 1108 | **Interes por mora en deudas de dinero** | A falta de pacto en contrario, la indemnizacion consiste en los intereses convenidos y, **a falta de convenio, en el interes legal**. El segundo parrafo ("6 por 100") esta desplazado por la fijacion anual en la Ley de Presupuestos |
| 1124 | Resolucion | Facultad implicita en las obligaciones reciprocas. El perjudicado elige entre exigir el cumplimiento o la resolucion, con resarcimiento en ambos casos. El Tribunal decreta la resolucion salvo causa justificada para señalar plazo |
| 1157 | Pago | No se entiende pagada una deuda sino cuando se ha entregado completamente la cosa o hecho la prestacion |
| 1170 | Especie del pago | El pago de deudas de dinero se hace en la especie pactada. La entrega de pagares o letras solo produce efectos de pago cuando se realizan |
| 1196 | Compensacion | Cinco requisitos acumulativos: obligacion principal reciproca, deudas homogeneas, ambas vencidas, liquidas y exigibles, y sin retencion ni contienda de tercero notificada |
| 1225 | Valor del documento privado | El documento privado reconocido legalmente tiene **el mismo valor que la escritura publica entre los que lo suscribieron y sus causahabientes** |
| 1227 | **Fecha cierta frente a terceros** | La fecha de un documento privado no cuenta frente a terceros sino desde su incorporacion o inscripcion en un registro publico, desde la muerte de cualquiera de los firmantes, o desde su entrega a un funcionario publico por razon de su oficio |
| 1255 | **Autonomia de la voluntad** | Las partes pueden establecer los pactos, clausulas y condiciones que tengan por conveniente, **siempre que no sean contrarios a las leyes, a la moral ni al orden publico** |
| 1258 | Perfeccion e integracion | Los contratos se perfeccionan por el mero consentimiento y obligan a lo pactado y a las consecuencias conformes a la buena fe, al uso y a la ley |
| 1261 | Elementos esenciales | No hay contrato sin consentimiento, objeto cierto y causa de la obligacion |
| 1274 | Concepto de causa | En los contratos onerosos, la prestacion o promesa de la otra parte; en los remuneratorios, el servicio que se remunera; en los de pura beneficencia, la mera liberalidad |
| 1275 | **Causa ilicita** | Los contratos sin causa o con causa ilicita **no producen efecto alguno**. Es ilicita la causa cuando se opone a las leyes o a la moral |
| 1276 | **Causa falsa** | La expresion de una causa falsa da lugar a la nulidad, salvo que se pruebe que estaban fundados en otra verdadera y licita |
| 1277 | Presuncion de causa | Aunque la causa no se exprese, se presume que existe y que es licita **mientras el deudor no pruebe lo contrario** |
| 1278 | **Libertad de forma** | Los contratos son obligatorios cualquiera que sea la forma en que se hayan celebrado, siempre que concurran las condiciones esenciales de validez |
| 1279 | **Elevacion a la forma exigida** | Si la ley exige escritura u otra forma especial para hacer efectivas las obligaciones, los contratantes **pueden compelerse reciprocamente** a llenar aquella forma desde que hubo consentimiento y demas requisitos de validez |
| 1280 | Contratos que deben constar en documento publico | Seis supuestos tasados (derechos reales sobre inmuebles, arrendamientos de inmuebles de seis o mas años que perjudiquen a tercero, capitulaciones matrimoniales, cesion de derechos hereditarios, determinados poderes, cesion de acciones de acto en escritura publica). Ultimo parrafo: los demas contratos que excedan de 1.500 pesetas deben hacerse constar por escrito, aunque sea privado. **Ultima version: Ley 11/1981 (apartado 3.º)** |
| 1281 | Interpretacion | Si los terminos son claros, se esta al sentido literal; si las palabras contrarian la intencion evidente, prevalece esta |
| 1289 | Dudas insalvables | En contrato gratuito, a favor de la menor transmision de derechos; en oneroso, a favor de la mayor reciprocidad. Si la duda recae sobre el objeto principal, el contrato es nulo |
| 1445 | **Compraventa: concepto** | Uno se obliga a entregar una cosa determinada y el otro a pagar por ella un precio cierto, en dinero o signo que lo represente |
| 1450 | Perfeccion de la venta | Se perfecciona por el acuerdo sobre cosa y precio, **aunque ni la una ni el otro se hayan entregado** |
| 1461 | Obligaciones del vendedor | Entrega y saneamiento de la cosa vendida |
| 1484 | **Saneamiento por vicios ocultos** | El vendedor responde de los defectos ocultos que hagan la cosa impropia para su uso o disminuyan este de modo que el comprador no la habria adquirido o habria dado menos precio. **No responde de los defectos manifiestos o que estuvieren a la vista**, ni de los ocultos si el comprador es perito que debia conocerlos facilmente. **Ultima version: Ley 17/2021 (bienestar animal), que añade un apartado 2 sobre venta de animales** |
| 1485 | Alcance del saneamiento | El vendedor responde aunque ignorase los vicios. **No rige si se estipulo lo contrario Y el vendedor ignoraba los vicios** (los dos requisitos son acumulativos). Ultima version: Ley 17/2021 |
| 1486 | Opciones del comprador | Desistir del contrato con abono de gastos, o rebaja proporcional del precio a juicio de peritos. Si el vendedor conocia los vicios y los oculto, ademas indemnizacion de daños si opta por la rescision |
| 1490 | **Plazo del saneamiento** | Las acciones de saneamiento por vicios ocultos **se extinguen a los seis meses desde la entrega** de la cosa vendida |
| 1500 | Pago del precio | En el tiempo y lugar fijados por el contrato; a falta de pacto, en el tiempo y lugar de la entrega |
| 1501 | Intereses del precio aplazado | El comprador debe intereses entre la entrega y el pago solo en tres casos: si se convino, si la cosa produce fruto o renta, o si esta en mora conforme al art. 1100 |
| 1740 | **Concepto de prestamo** | Entrega de cosa **no fungible** para usarla y devolverla = **comodato**; entrega de **dinero u otra cosa fungible** con condicion de devolver otro tanto de la misma especie y calidad = **simple prestamo**. **El comodato es esencialmente gratuito. El simple prestamo puede ser gratuito o con pacto de pagar interes** |
| 1741 | Propiedad en el comodato | El comodante conserva la propiedad; el comodatario adquiere el uso pero no los frutos. **Si interviene algun emolumento que haya de pagar quien adquiere el uso, la convencion deja de ser comodato** |
| 1743 | Gastos ordinarios | A cargo del comodatario los gastos ordinarios necesarios para el uso y conservacion de la cosa |
| 1744 | Uso indebido | Si destina la cosa a uso distinto o la retiene mas tiempo del convenido, responde de su perdida **aunque sobrevenga por caso fortuito** |
| 1745 | Cosa tasada | Si se entrego con tasacion y se pierde, responde del precio aun por caso fortuito, salvo pacto expreso de exoneracion |
| 1746 | Deterioro por uso | No responde de los deterioros que sobrevengan por el solo efecto del uso y sin culpa suya |
| 1747 | Prohibicion de retencion | No puede retener la cosa a pretexto de lo que el comodante le deba, aunque sea por expensas |
| 1748 | Pluralidad de comodatarios | Los comodatarios conjuntos responden **solidariamente** |
| 1749 | **Reclamacion de la cosa** | El comodante no puede reclamarla sino despues de concluido el uso para que la presto. **Si antes tuviere urgente necesidad de ella, podra reclamar la restitucion** |
| 1750 | **Comodato sin plazo ni uso pactado** | Si no se pacto duracion ni uso, y este no resulta de la costumbre, **el comodante puede reclamarla a su voluntad** (situacion de precario). En caso de duda, la prueba incumbe al comodatario |
| 1751 | Gastos extraordinarios | A cargo del comodante los gastos extraordinarios de conservacion, siempre que el comodatario se lo comunique antes de hacerlos, salvo urgencia |
| 1752 | Vicios de la cosa prestada | El comodante que conocia los vicios y no los advirtio responde de los daños causados |
| 1753 | Efecto del simple prestamo | El prestatario **adquiere la propiedad** de lo recibido y debe devolver otro tanto de la misma especie y calidad |
| 1754 | Devolucion | Remision al art. 1170. Si lo prestado es otra cosa fungible, se debe cantidad igual y de la misma especie y calidad, **aunque sufra alteracion en su precio** |
| 1755 | **Intereses: regla capital** | "**No se deberan intereses sino cuando expresamente se hubiesen pactado.**" |
| 1756 | Intereses pagados sin pacto | El prestatario que pago intereses no estipulados no puede reclamarlos ni imputarlos al capital |
| 1822 | Fianza | Por la fianza uno se obliga a pagar o cumplir por un tercero en caso de no hacerlo este. Si el fiador se obliga **solidariamente**, se aplica el regimen de la solidaridad |
| 1830 | **Beneficio de excusion** | El fiador no puede ser compelido a pagar sin hacerse antes excusion de todos los bienes del deudor |
| 1831 | Perdida del beneficio de excusion | No hay excusion si el fiador renuncio expresamente, **si se obligo solidariamente**, en caso de concurso del deudor, o si este no puede ser demandado dentro del Reino |
| 1863 | Prenda | Ademas de los requisitos del art. 1857, exige **poner la cosa en posesion del acreedor o de un tercero de comun acuerdo** (desplazamiento posesorio) |
| 1911 | Responsabilidad patrimonial universal | El deudor responde con todos sus bienes, presentes y futuros |
| 1962 | Prescripcion de acciones reales sobre muebles | Seis años desde la perdida de la posesion, con las excepciones del art. 1955 |
| 1964 | **Prescripcion de acciones personales** | Version vigente (Ley 42/2015): la accion hipotecaria prescribe a los veinte años y **las acciones personales sin plazo especial, a los cinco años** desde que pueda exigirse el cumplimiento. La version originaria (quince años) esta superada: usar siempre la ultima |
| 1973 | **Interrupcion de la prescripcion** | Se interrumpe por el ejercicio ante los Tribunales, por reclamacion extrajudicial del acreedor y **por cualquier acto de reconocimiento de la deuda por el deudor** |

---

## Ley Azcarate: articulos verificados el 03/09/2026 (BOE-A-1908-5579)

| Articulo | Contenido verificado |
|---|---|
| 1 | "Sera **nulo** todo contrato de prestamo en que se estipule un interes notablemente superior al normal del dinero y manifiestamente desproporcionado con las circunstancias del caso o en condiciones tales que resulte aquel leonino, habiendo motivos para estimar que ha sido aceptado por el prestatario a causa de su situacion angustiosa, de su inexperiencia o de lo limitado de sus facultades mentales." Segundo parrafo: tambien es nulo el contrato en que se suponga recibida mayor cantidad que la verdaderamente entregada, y es nula la renuncia del fuero propio hecha por el deudor |
| 2 | Los Tribunales resuelven en cada caso formando libremente su conviccion en vista de las alegaciones de las partes |
| 3 | **Consecuencia de la nulidad**: "el prestatario estara obligado a entregar tan solo la suma recibida; y si hubiera satisfecho parte de aquella y los intereses vencidos, el prestamista devolvera al prestatario lo que, tomando en cuenta el total de lo percibido, exceda del capital prestado" |
| 8 | Toda sentencia que declare nulo el prestamo lleva **condena en costas al prestamista** |
| 9 | "Lo dispuesto por esta ley se aplicara a **toda operacion sustancialmente equivalente a un prestamo de dinero**, cualesquiera que sea la forma que revista el contrato y la garantia que para su cumplimiento se haya ofrecido" |

Consecuencia operativa para esta skill: la usura **no reduce el interes, anula el contrato**. Ver `references/usura-y-limites-del-interes.md`.

---

## Articulos de la LEC verificados el 03/09/2026 (BOE-A-2000-323)

| Articulo | Materia | Redaccion vigente verificada |
|---|---|---|
| 517.2.4.º | Fuerza ejecutiva de la escritura publica | "**La copia de la escritura publica matriz que el interesado solicite que se expida con tal caracter.**" Modificado por la LO 1/2025, efectos 03/04/2025: ya no dice "primera copia" |
| 520 | Cantidad minima en titulos no judiciales | Solo cabe despachar ejecucion por cantidad determinada que **exceda de 300 euros**, en dinero efectivo, moneda extranjera convertible o cosa o especie computable en dinero. El limite puede alcanzarse sumando varios titulos |

---

## Magnitud variable: el interes legal del dinero (NUNCA fijo en el asset)

El interes legal del dinero **cambia cada ejercicio** y se fija en la **Ley de Presupuestos Generales del Estado** de cada año (art. 1 de la Ley 24/1984). El Banco de España lo recoge en su serie historica de tipos de interes legal.

**Estado verificado el 03/09/2026:**

- La ultima fijacion expresa localizada en el BOE es la de la **Ley 31/2022, de PGE para 2023, disposicion adicional cuadragesima segunda** (bloque `da-42` de BOE-A-2022-22128): interes legal **3,25 %** e interes de demora tributario 4,0625 %, ambos **"hasta el 31 de diciembre del año 2023"**.
- **No consta aprobada una Ley de Presupuestos Generales del Estado para 2026**: el presupuesto se encuentra prorrogado. En situacion de prorroga la cifra vigente sigue siendo la ultima fijada, pero **esto no esta afirmado literalmente en el texto de una norma consultable**, sino que resulta del regimen de prorroga presupuestaria.

**Regla obligatoria de la skill:** el porcentaje **NO se escribe fijo en ningun asset**. Los assets se remiten al interes legal "vigente en cada momento" mediante placeholder o mediante remision generica al art. 1108 CC. Si en un caso concreto hace falta la cifra:

1. Verificarla en el momento en la Ley de Presupuestos Generales del Estado del ejercicio en curso (o en la serie del Banco de España, https://www.bde.es).
2. Si no se puede verificar, **advertir expresamente al usuario** ("no se pudo verificar el interes legal del ejercicio en curso; verifiquelo antes de firmar") y dejar el placeholder sin resolver. Prohibido dar por vigente el 3,25 % sin comprobarlo.

---

## Plantillas: no existe modelo normalizado oficial de contrato entre particulares

Verificado el 03/09/2026: los modelos normalizados publicados por el CGPJ (https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/) son formularios **procesales** (juicio verbal, monitorio, jurisdiccion voluntaria, justicia gratuita, denuncia, delito leve, juicio rapido). **No existe modelo oficial de contrato de prestamo, de reconocimiento de deuda, de comodato ni de compraventa de bien mueble**: son contratos privados sujetos a la libertad de forma del art. 1278 CC.

Por tanto los assets de esta skill no reproducen ningun modelo oficial: se construyen sobre el contenido minimo de validez del art. 1261 CC y sobre el regimen dispositivo de cada tipo contractual.

| Asset | Base normativa de su estructura |
|---|---|
| `assets/contrato-prestamo-particulares.md` | Arts. 1088, 1091, 1100, 1101, 1108, 1124, 1255, 1258, 1261, 1278 a 1281, 1740, 1753 a 1756, 1822, 1830, 1831, 1863, 1911 y 1964 CC; Ley Azcarate arts. 1, 3 y 9; art. 517.2.4.º LEC |
| `assets/reconocimiento-deuda.md` | Arts. 1091, 1100, 1108, 1157, 1196, 1255, 1261, 1274 a 1277, 1278 a 1280, 1911, 1964 y 1973 CC; art. 517.2.4.º LEC |
| `assets/contrato-comodato.md` | Arts. 1255, 1258, 1261, 1740 a 1752 CC |
| `assets/contrato-compraventa-mueble.md` | Arts. 1255, 1258, 1261, 1445, 1450, 1461, 1484 a 1486, 1490, 1500, 1501, 1962 y 1964 CC |

---

## Verificar manualmente (no resuelto por fuente oficial)

1. **Interes legal del dinero del ejercicio en curso.** Ver el apartado anterior. La ultima fijacion expresa verificable en el BOE es de la Ley 31/2022 y se refiere literalmente a 2023. **Marcado como pendiente de verificacion manual en cada lanzamiento.**
2. **Umbral cuantitativo de la usura.** La Ley Azcarate **no fija ningun porcentaje**: usa conceptos juridicos indeterminados ("notablemente superior al normal del dinero", "manifiestamente desproporcionado"). El "interes normal del dinero" se contrasta en la practica con las estadisticas de tipos medios del Banco de España para operaciones equivalentes, y su apreciacion corresponde al Tribunal (art. 2). **La skill nunca afirma un umbral numerico como si fuera legal:** advierte del riesgo y escala. Ver `references/usura-y-limites-del-interes.md`.
3. **Fecha cierta por deposito notarial de documento privado.** El art. 1227 CC enumera tres supuestos tasados. La practica de legitimar notarialmente las firmas o depositar el documento en poder de notario se dirige a acreditar la fecha, pero su encaje exacto en el art. 1227 depende de la modalidad concreta del acta. **Verificar con el notario** antes de afirmar al cliente que su documento privado tendra fecha cierta frente a terceros.
4. **Regimen foral y derecho civil autonomico.** Cataluña, Navarra, Aragon, Baleares, Galicia y Pais Vasco tienen derecho civil propio que puede desplazar reglas del Codigo Civil en materia de obligaciones y contratos. La skill trabaja por defecto con el Codigo Civil comun: si la vecindad civil de las partes o el lugar de celebracion apunta a un territorio foral, **advertir y escalar**.
5. **Redaccion literal de los articulos en un documento.** La API del BOE devuelve la version consolidada vigente, que es la fuente usada aqui. Antes de transcribir literalmente un precepto en un contrato que se vaya a firmar, contrastarlo de nuevo en el BOE.
