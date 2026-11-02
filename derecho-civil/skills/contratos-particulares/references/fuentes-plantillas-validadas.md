# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-contratos-particulares`. Registra las fuentes normativas y las
> plantillas validadas que la skill verifica en cada lanzamiento para aplicar la redacción vigente al documento que redacta.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local, se informa al usuario y se marca el punto como pendiente de verificación manual. **Prohibido dar por vigente lo que no se ha podido verificar.**

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Código Civil (texto consolidado) | BOE-A-1889-4763 | artículos de contratos, préstamo, comodato, compraventa, fianza y prescripción verificados el 03/09/2026 (detalle en la tabla siguiente) | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| Ley de 23 de julio de 1908 sobre nulidad de los contratos de préstamos usurarios (Ley Azcárate) | BOE-A-1908-5579 | **VIGENTE**: la API del BOE devuelve `estatus_derogacion = N` y `vigencia_agotada = N`; última actualización del consolidado 16/12/2025. Texto sin modificaciones desde su promulgación (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-1908-5579 |
| LEC — Ley 1/2000 de Enjuiciamiento Civil (arts. 517 y 520, para la fuerza ejecutiva de la escritura pública) | BOE-A-2000-323 | art. 517.2.4.º en la redacción de la LO 1/2025, efectos 03/04/2025; art. 520 con la conversión a euros del RD 1417/2001 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| Ley 31/2022, de PGE para 2023 (disposición adicional 42.ª, interés legal del dinero) | BOE-A-2022-22128 | última fijación expresa del interés legal del dinero: **3,25 %**, "hasta el 31 de diciembre del año 2023" (bloque `da-42`, verificado 03/09/2026). Ver la advertencia de magnitud variable más abajo | https://www.boe.es/buscar/act.php?id=BOE-A-2022-22128 |

**Endpoint de verificación artículo por artículo (API de legislación consolidada del BOE).** Devuelve todas las versiones históricas del precepto; **la última es la vigente**. Requiere cabecera `Accept: application/xml`:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{numero}
```

Ejemplo: `.../bloque/art1755` para el art. 1755 CC.

**Aviso sobre el formato del identificador de bloque:** no todas las normas usan la misma convención. El Código Civil usa `art{numero}` (`art1755`); la LEC usa `a{numero}` (`a517`); la Ley Azcárate usa `a{numero}` (`a1`, `a3`); las disposiciones adicionales de una ley de presupuestos usan `da-{numero}` (`da-42`). Si un identificador devuelve 404, probar la otra convención antes de darlo por inaccesible.

---

## Artículos del Código Civil verificados el 03/09/2026

| Artículo | Materia | Redacción vigente verificada |
|---|---|---|
| 1088 | Contenido de la obligación | Toda obligación consiste en dar, hacer o no hacer alguna cosa |
| 1091 | Fuerza vinculante | Las obligaciones nacidas de contrato tienen fuerza de ley entre las partes y deben cumplirse a tenor de los mismos |
| 1100 | Mora | Se incurre en mora desde que el acreedor exige judicial o extrajudicialmente el cumplimiento. No hace falta intimación cuando la obligación o la ley lo declaren así expresamente, o cuando la fecha fue motivo determinante |
| 1101 | Indemnización | Responde de daños y perjuicios quien incurre en dolo, negligencia o morosidad |
| 1108 | **Interés por mora en deudas de dinero** | A falta de pacto en contrario, la indemnización consiste en los intereses convenidos y, **a falta de convenio, en el interés legal**. El segundo párrafo ("6 por 100") está desplazado por la fijación anual en la Ley de Presupuestos |
| 1124 | Resolución | Facultad implícita en las obligaciones reciprocas. El perjudicado elige entre exigir el cumplimiento o la resolución, con resarcimiento en ambos casos. El Tribunal decreta la resolución salvo causa justificada para señalar plazo |
| 1157 | Pago | No se entiende pagada una deuda sino cuando se ha entregado completamente la cosa o hecho la prestación |
| 1170 | Especie del pago | El pago de deudas de dinero se hace en la especie pactada. La entrega de pagares o letras solo produce efectos de pago cuando se realizan |
| 1196 | Compensación | Cinco requisitos acumulativos: obligación principal recíproca, deudas homogéneas, ambas vencidas, liquidas y exigibles, y sin retención ni contienda de tercero notificada |
| 1225 | Valor del documento privado | El documento privado reconocido legalmente tiene **el mismo valor que la escritura pública entre los que lo suscribieron y sus causahabientes** |
| 1227 | **Fecha cierta frente a terceros** | La fecha de un documento privado no cuenta frente a terceros sino desde su incorporación o inscripción en un registro público, desde la muerte de cualquiera de los firmantes, o desde su entrega a un funcionario público por razón de su oficio |
| 1255 | **Autonomía de la voluntad** | Las partes pueden establecer los pactos, cláusulas y condiciones que tengan por conveniente, **siempre que no sean contrarios a las leyes, a la moral ni al orden público** |
| 1258 | Perfección e integración | Los contratos se perfeccionan por el mero consentimiento y obligan a lo pactado y a las consecuencias conformes a la buena fe, al uso y a la ley |
| 1261 | Elementos esenciales | No hay contrato sin consentimiento, objeto cierto y causa de la obligación |
| 1274 | Concepto de causa | En los contratos onerosos, la prestación o promesa de la otra parte; en los remuneratorios, el servicio que se remunera; en los de pura beneficencia, la mera liberalidad |
| 1275 | **Causa ilícita** | Los contratos sin causa o con causa ilícita **no producen efecto alguno**. Es ilícita la causa cuando se opone a las leyes o a la moral |
| 1276 | **Causa falsa** | La expresión de una causa falsa da lugar a la nulidad, salvo que se pruebe que estaban fundados en otra verdadera y licita |
| 1277 | Presunción de causa | Aunque la causa no se exprese, se presume que existe y que es licita **mientras el deudor no pruebe lo contrario** |
| 1278 | **Libertad de forma** | Los contratos son obligatorios cualquiera que sea la forma en que se hayan celebrado, siempre que concurran las condiciones esenciales de validez |
| 1279 | **Elevación a la forma exigida** | Si la ley exige escritura u otra forma especial para hacer efectivas las obligaciones, los contratantes **pueden compelerse recíprocamente** a llenar aquella forma desde que hubo consentimiento y demás requisitos de validez |
| 1280 | Contratos que deben constar en documento público | Seis supuestos tasados (derechos reales sobre inmuebles, arrendamientos de inmuebles de seis o más años que perjudiquen a tercero, capitulaciones matrimoniales, cesión de derechos hereditarios, determinados poderes, cesión de acciones de acto en escritura pública). Último párrafo: los demás contratos que excedan de 1.500 pesetas deben hacerse constar por escrito, aunque sea privado. **Última versión: Ley 11/1981 (apartado 3.º)** |
| 1281 | Interpretación | Si los términos son claros, se está al sentido literal; si las palabras contrarian la intención evidente, prevalece esta |
| 1289 | Dudas insalvables | En contrato gratuito, a favor de la menor transmisión de derechos; en oneroso, a favor de la mayor reciprocidad. Si la duda recae sobre el objeto principal, el contrato es nulo |
| 1445 | **Compraventa: concepto** | Uno se obliga a entregar una cosa determinada y el otro a pagar por ella un precio cierto, en dinero o signo que lo represente |
| 1450 | Perfección de la venta | Se perfecciona por el acuerdo sobre cosa y precio, **aunque ni la una ni el otro se hayan entregado** |
| 1461 | Obligaciones del vendedor | Entrega y saneamiento de la cosa vendida |
| 1484 | **Saneamiento por vicios ocultos** | El vendedor responde de los defectos ocultos que hagan la cosa impropia para su uso o disminuyan este de modo que el comprador no la habría adquirido o habría dado menos precio. **No responde de los defectos manifiestos o que estuvieren a la vista**, ni de los ocultos si el comprador es perito que debía conocerlos fácilmente. **Última versión: Ley 17/2021 (bienestar animal), que añade un apartado 2 sobre venta de animales** |
| 1485 | Alcance del saneamiento | El vendedor responde aunque ignorase los vicios. **No rige si se estipulo lo contrario Y el vendedor ignoraba los vicios** (los dos requisitos son acumulativos). Última versión: Ley 17/2021 |
| 1486 | Opciones del comprador | Desistir del contrato con abono de gastos, o rebaja proporcional del precio a juicio de peritos. Si el vendedor conocía los vicios y los oculto, además indemnización de daños si opta por la rescisión |
| 1490 | **Plazo del saneamiento** | Las acciones de saneamiento por vicios ocultos **se extinguen a los seis meses desde la entrega** de la cosa vendida |
| 1500 | Pago del precio | En el tiempo y lugar fijados por el contrato; a falta de pacto, en el tiempo y lugar de la entrega |
| 1501 | Intereses del precio aplazado | El comprador debe intereses entre la entrega y el pago solo en tres casos: si se convino, si la cosa produce fruto o renta, o si está en mora conforme al art. 1100 |
| 1740 | **Concepto de préstamo** | Entrega de cosa **no fungible** para usarla y devolverla = **comodato**; entrega de **dinero u otra cosa fungible** con condición de devolver otro tanto de la misma especie y calidad = **simple préstamo**. **El comodato es esencialmente gratuito. El simple préstamo puede ser gratuito o con pacto de pagar interés** |
| 1741 | Propiedad en el comodato | El comodante conserva la propiedad; el comodatario adquiere el uso pero no los frutos. **Si interviene algún emolumento que haya de pagar quien adquiere el uso, la convención deja de ser comodato** |
| 1743 | Gastos ordinarios | A cargo del comodatario los gastos ordinarios necesarios para el uso y conservación de la cosa |
| 1744 | Uso indebido | Si destina la cosa a uso distinto o la retiene más tiempo del convenido, responde de su pérdida **aunque sobrevenga por caso fortuito** |
| 1745 | Cosa tasada | Si se entregó con tasación y se pierde, responde del precio aun por caso fortuito, salvo pacto expreso de exoneración |
| 1746 | Deterioro por uso | No responde de los deterioros que sobrevengan por el solo efecto del uso y sin culpa suya |
| 1747 | Prohibición de retención | No puede retener la cosa a pretexto de lo que el comodante le deba, aunque sea por expensas |
| 1748 | Pluralidad de comodatarios | Los comodatarios conjuntos responden **solidariamente** |
| 1749 | **Reclamación de la cosa** | El comodante no puede reclamarla sino después de concluido el uso para que la presto. **Si antes tuviere urgente necesidad de ella, podrá reclamar la restitución** |
| 1750 | **Comodato sin plazo ni uso pactado** | Si no se pacto duración ni uso, y este no resulta de la costumbre, **el comodante puede reclamarla a su voluntad** (situación de precario). En caso de duda, la prueba incumbe al comodatario |
| 1751 | Gastos extraordinarios | A cargo del comodante los gastos extraordinarios de conservación, siempre que el comodatario se lo comunique antes de hacerlos, salvo urgencia |
| 1752 | Vicios de la cosa prestada | El comodante que conocía los vicios y no los advirtió responde de los daños causados |
| 1753 | Efecto del simple préstamo | El prestatario **adquiere la propiedad** de lo recibido y debe devolver otro tanto de la misma especie y calidad |
| 1754 | Devolución | Remisión al art. 1170. Si lo prestado es otra cosa fungible, se debe cantidad igual y de la misma especie y calidad, **aunque sufra alteración en su precio** |
| 1755 | **Intereses: regla capital** | "**No se deberán intereses sino cuando expresamente se hubiesen pactado.**" |
| 1756 | Intereses pagados sin pacto | El prestatario que pago intereses no estipulados no puede reclamarlos ni imputarlos al capital |
| 1822 | Fianza | Por la fianza uno se obliga a pagar o cumplir por un tercero en caso de no hacerlo este. Si el fiador se obliga **solidariamente**, se aplica el régimen de la solidaridad |
| 1830 | **Beneficio de excusion** | El fiador no puede ser compelido a pagar sin hacerse antes excusion de todos los bienes del deudor |
| 1831 | Pérdida del beneficio de excusion | No hay excusion si el fiador renuncio expresamente, **si se obligo solidariamente**, en caso de concurso del deudor, o si este no puede ser demandado dentro del Reino |
| 1863 | Prenda | Además de los requisitos del art. 1857, exige **poner la cosa en posesión del acreedor o de un tercero de común acuerdo** (desplazamiento posesorio) |
| 1911 | Responsabilidad patrimonial universal | El deudor responde con todos sus bienes, presentes y futuros |
| 1962 | Prescripción de acciones reales sobre muebles | Seis años desde la pérdida de la posesión, con las excepciones del art. 1955 |
| 1964 | **Prescripción de acciones personales** | Versión vigente (Ley 42/2015): la acción hipotecaria prescribe a los veinte años y **las acciones personales sin plazo especial, a los cinco años** desde que pueda exigirse el cumplimiento. La versión originaria (quince años) está superada: usar siempre la última |
| 1973 | **Interrupción de la prescripción** | Se interrumpe por el ejercicio ante los Tribunales, por reclamación extrajudicial del acreedor y **por cualquier acto de reconocimiento de la deuda por el deudor** |

---

## Ley Azcárate: artículos verificados el 03/09/2026 (BOE-A-1908-5579)

| Artículo | Contenido verificado |
|---|---|
| 1 | "Será **nulo** todo contrato de préstamo en que se estipule un interés notablemente superior al normal del dinero y manifiestamente desproporcionado con las circunstancias del caso o en condiciones tales que resulte aquel leonino, habiendo motivos para estimar que ha sido aceptado por el prestatario a causa de su situación angustiosa, de su inexperiencia o de lo limitado de sus facultades mentales." Segundo párrafo: también es nulo el contrato en que se suponga recibida mayor cantidad que la verdaderamente entregada, y es nula la renuncia del fuero propio hecha por el deudor |
| 2 | Los Tribunales resuelven en cada caso formando libremente su convicción en vista de las alegaciones de las partes |
| 3 | **Consecuencia de la nulidad**: "el prestatario estará obligado a entregar tan solo la suma recibida; y si hubiera satisfecho parte de aquella y los intereses vencidos, el prestamista devolverá al prestatario lo que, tomando en cuenta el total de lo percibido, exceda del capital prestado" |
| 8 | Toda sentencia que declare nulo el préstamo lleva **condena en costas al prestamista** |
| 9 | "Lo dispuesto por esta ley se aplicará a **toda operación sustancialmente equivalente a un préstamo de dinero**, cualesquiera que sea la forma que revista el contrato y la garantía que para su cumplimiento se haya ofrecido" |

Consecuencia operativa para esta skill: la usura **no reduce el interés, anula el contrato**. Ver `references/usura-y-limites-del-interes.md`.

---

## Artículos de la LEC verificados el 03/09/2026 (BOE-A-2000-323)

| Artículo | Materia | Redacción vigente verificada |
|---|---|---|
| 517.2.4.º | Fuerza ejecutiva de la escritura pública | "**La copia de la escritura pública matriz que el interesado solicite que se expida con tal carácter.**" Modificado por la LO 1/2025, efectos 03/04/2025: ya no dice "primera copia" |
| 520 | Cantidad mínima en títulos no judiciales | Solo cabe despachar ejecución por cantidad determinada que **exceda de 300 euros**, en dinero efectivo, moneda extranjera convertible o cosa o especie computable en dinero. El límite puede alcanzarse sumando varios títulos |

---

## Magnitud variable: el interés legal del dinero (NUNCA fijo en el asset)

El interés legal del dinero **cambia cada ejercicio** y se fija en la **Ley de Presupuestos Generales del Estado** de cada año (art. 1 de la Ley 24/1984). El Banco de España lo recoge en su serie histórica de tipos de interés legal.

**Estado verificado el 03/09/2026:**

- La última fijación expresa localizada en el BOE es la de la **Ley 31/2022, de PGE para 2023, disposición adicional cuadragésima segunda** (bloque `da-42` de BOE-A-2022-22128): interés legal **3,25 %** e interés de demora tributario 4,0625 %, ambos **"hasta el 31 de diciembre del año 2023"**.
- **No consta aprobada una Ley de Presupuestos Generales del Estado para 2026**: el presupuesto se encuentra prorrogado. En situación de prórroga la cifra vigente sigue siendo la última fijada, pero **esto no está afirmado literalmente en el texto de una norma consultable**, sino que resulta del régimen de prórroga presupuestaria.

**Regla obligatoria de la skill:** el porcentaje **NO se escribe fijo en ningún asset**. Los assets se remiten al interés legal "vigente en cada momento" mediante placeholder o mediante remisión genérica al art. 1108 CC. Si en un caso concreto hace falta la cifra:

1. Verificarla en el momento en la Ley de Presupuestos Generales del Estado del ejercicio en curso (o en la serie del Banco de España, https://www.bde.es).
2. Si no se puede verificar, **advertir expresamente al usuario** ("no se pudo verificar el interés legal del ejercicio en curso; verifíquelo antes de firmar") y dejar el placeholder sin resolver. Prohibido dar por vigente el 3,25 % sin comprobarlo.

---

## Plantillas: no existe modelo normalizado oficial de contrato entre particulares

Verificado el 03/09/2026: los modelos normalizados publicados por el CGPJ (https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/) son formularios **procesales** (juicio verbal, monitorio, jurisdicción voluntaria, justicia gratuita, denuncia, delito leve, juicio rápido). **No existe modelo oficial de contrato de préstamo, de reconocimiento de deuda, de comodato ni de compraventa de bien mueble**: son contratos privados sujetos a la libertad de forma del art. 1278 CC.

Por tanto los assets de esta skill no reproducen ningún modelo oficial: se construyen sobre el contenido mínimo de validez del art. 1261 CC y sobre el régimen dispositivo de cada tipo contractual.

| Asset | Base normativa de su estructura |
|---|---|
| `assets/contrato-prestamo-particulares.md` | Arts. 1088, 1091, 1100, 1101, 1108, 1124, 1255, 1258, 1261, 1278 a 1281, 1740, 1753 a 1756, 1822, 1830, 1831, 1863, 1911 y 1964 CC; Ley Azcárate arts. 1, 3 y 9; art. 517.2.4.º LEC |
| `assets/reconocimiento-deuda.md` | Arts. 1091, 1100, 1108, 1157, 1196, 1255, 1261, 1274 a 1277, 1278 a 1280, 1911, 1964 y 1973 CC; art. 517.2.4.º LEC |
| `assets/contrato-comodato.md` | Arts. 1255, 1258, 1261, 1740 a 1752 CC |
| `assets/contrato-compraventa-mueble.md` | Arts. 1255, 1258, 1261, 1445, 1450, 1461, 1484 a 1486, 1490, 1500, 1501, 1962 y 1964 CC |

---

## Verificar manualmente (no resuelto por fuente oficial)

1. **Interés legal del dinero del ejercicio en curso.** Ver el apartado anterior. La última fijación expresa verificable en el BOE es de la Ley 31/2022 y se refiere literalmente a 2023. **Marcado como pendiente de verificación manual en cada lanzamiento.**
2. **Umbral cuantitativo de la usura.** La Ley Azcárate **no fija ningún porcentaje**: usa conceptos jurídicos indeterminados ("notablemente superior al normal del dinero", "manifiestamente desproporcionado"). El "interés normal del dinero" se contrasta en la práctica con las estadísticas de tipos medios del Banco de España para operaciones equivalentes, y su apreciación corresponde al Tribunal (art. 2). **La skill nunca afirma un umbral numérico como si fuera legal:** advierte del riesgo y escala. Ver `references/usura-y-limites-del-interes.md`.
3. **Fecha cierta por depósito notarial de documento privado.** El art. 1227 CC enumera tres supuestos tasados. La práctica de legitimar notarialmente las firmas o depositar el documento en poder de notario se dirige a acreditar la fecha, pero su encaje exacto en el art. 1227 depende de la modalidad concreta del acta. **Verificar con el notario** antes de afirmar al cliente que su documento privado tendrá fecha cierta frente a terceros.
4. **Régimen foral y derecho civil autonómico.** Cataluña, Navarra, Aragon, Baleares, Galicia y País Vasco tienen derecho civil propio que puede desplazar reglas del Código Civil en materia de obligaciones y contratos. La skill trabaja por defecto con el Código Civil común: si la vecindad civil de las partes o el lugar de celebración apunta a un territorio foral, **advertir y escalar**.
5. **Redacción literal de los artículos en un documento.** La API del BOE devuelve la versión consolidada vigente, que es la fuente usada aquí. Antes de transcribir literalmente un precepto en un contrato que se vaya a firmar, contrastarlo de nuevo en el BOE.
