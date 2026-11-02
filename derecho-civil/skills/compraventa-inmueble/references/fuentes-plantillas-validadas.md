# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-compraventa-inmueble`. Registra las fuentes normativas y las
> plantillas validadas que la skill verifica en cada lanzamiento para aplicar la redacción vigente al documento que redacta.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa expresamente al usuario de que debe verificarla manualmente antes de firmar.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Código Civil (texto consolidado) — compraventa, saneamiento, resolución y forma | BOE-A-1889-4763 | preceptos de compraventa en redacción originaria de 1889, salvo art. 1484 y 1485 (Ley 17/2021, vigencia 05/01/2022), art. 1280.3 (Ley 11/1981, vigencia 08/06/1981) y art. 1964 (Ley 42/2015, vigencia 07/10/2015). Verificado 02/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| LAU — Ley 29/1994, de Arrendamientos Urbanos, art. 25 (adquisición preferente) | BOE-A-1994-26003 | art. 25 en la redacción del Real Decreto-ley 7/2019, vigencia 06/03/2019 (apartado 7); apartado 8 en la redacción de la Ley 4/2013. Verificado 02/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003 |
| LOE — Ley 38/1999, de Ordenación de la Edificación | BOE-A-1999-21567 | art. 17 y art. 20 en redacción originaria (vigencia 06/05/2000); art. 19 y disposición adicional primera en la redacción de la Ley 20/2015, vigencia 01/01/2016. Verificado 02/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1999-21567 |
| ITPAJD — Real Decreto Legislativo 1/1993, art. 8 (sujeto pasivo) | BOE-A-1993-25359 | art. 8 en redacción originaria, vigencia 21/10/1993. Verificado 02/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1993-25359 |
| TRLRHL — Real Decreto Legislativo 2/2004, art. 106 (sujeto pasivo del IIVTNU) | BOE-A-2004-4214 | art. 106 en la redacción de la Ley 18/2014, vigencia 17/10/2014 (suprimido su apartado 3). Verificado 02/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 |
| LGT — Ley 58/2003, General Tributaria, art. 17 (inalterabilidad de la obligación tributaria) | BOE-A-2003-23186 | art. 17.5 en la redacción del Real Decreto-ley 20/2011, vigencia 01/01/2012 (el antiguo 17.4 se renumero como 17.5). Verificado 02/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 |

**Endpoint de verificación artículo por artículo (API de legislación consolidada del BOE).** Devuelve todas las versiones históricas del precepto; **la última `<version>` del bloque es la vigente**. Requiere cabecera `Accept: application/xml`:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{ID_BOE}/texto/bloque/{bloque}
```

- Código Civil (BOE-A-1889-4763): bloques `artNNNN` — ejemplo `.../bloque/art1454`.
- LAU (BOE-A-1994-26003), LOE (BOE-A-1999-21567), ITPAJD, TRLRHL y LGT: bloques `aNN` — ejemplo `.../bloque/a25`. Las disposiciones adicionales de la LOE usan `daprimera` (no `da1`, que devuelve 404).

---

## Artículos del Código Civil verificados el 02/09/2026

| Artículo | Materia | Redacción vigente verificada |
|---|---|---|
| 1445 | Concepto de compraventa | Un contratante se obliga a entregar una cosa determinada y el otro a pagar por ella un precio cierto, en dinero o signo que lo represente. Redacción originaria de 1889 |
| 1450 | Perfección del contrato | La venta se perfecciona entre comprador y vendedor, y es obligatoria para ambos, si hubieren convenido en la cosa y en el precio, **aunque ni la una ni el otro se hayan entregado**. Redacción originaria de 1889 |
| 1454 | Arras o señal | **Literal íntegro:** "Si hubiesen mediado arras o señal en el contrato de compra y venta, podrá rescindirse el contrato allanándose el comprador a perderlas, o el vendedor a devolverlas duplicadas." Redacción originaria de 1889, vigente sin modificación. **El precepto NO clasifica las arras ni define tipos: solo contempla el desistimiento** (ver `arras-cargas-fiscalidad-y-retracto.md`, apartado 1) |
| 1455 | Gastos de escritura | Los gastos de otorgamiento de escrituras son de cuenta del **vendedor**; los de la primera copia y los demás posteriores a la venta, de cuenta del **comprador**, salvo pacto en contrario. Redacción originaria de 1889 |
| 1461 | Obligación básica del vendedor | Entrega y saneamiento de la cosa objeto de la venta |
| 1462 | Entrega. Traditio instrumental | Se entiende entregada cuando se pone en poder y posesión del comprador. **Cuando la venta se hace mediante escritura pública, el otorgamiento de esta equivale a la entrega**, si de la misma escritura no resultare o se dedujere claramente lo contrario |
| 1465 | Gastos de entrega | Los de entrega, a cargo del vendedor; los de transporte o traslación, del comprador, salvo estipulación especial |
| 1468 | Estado de la cosa y frutos | Se entrega en el estado en que se hallaba al perfeccionarse el contrato. Los frutos pertenecen al comprador desde la perfección |
| 1469 | Cabida del inmueble | Si la venta se hizo con expresión de cabida y a razón de un precio por unidad de medida, el comprador puede exigir todo lo expresado; si no es posible, puede optar entre rebaja proporcional del precio o rescisión, y esta última solo si la disminución **excede de la décima parte** de la cabida atribuida (o si el menor valor excede de la décima parte del precio, cuando la diferencia sea de calidad) |
| 1474 | Contenido del saneamiento | El vendedor responde de: 1.º la posesión legal y pacifica de la cosa vendida; 2.º los vicios o defectos ocultos que tuviere |
| 1475 | Evicción | Se prive al comprador por sentencia firme y en virtud de un derecho anterior a la compra. **El vendedor responde aunque nada se haya expresado en el contrato**, pero los contratantes pueden aumentar, disminuir o suprimir esa obligación legal |
| 1483 | Cargas o servidumbres no aparentes | Si la finca está gravada, sin mencionarlo la escritura, con una carga o servidumbre no aparente de tal naturaleza que deba presumirse que el comprador no la habría adquirido si la hubiera conocido, puede pedir la rescisión o preferir la indemnización. Plazo: **un año desde el otorgamiento de la escritura** para la acción rescisoria o la indemnización; transcurrido, solo indemnización, dentro de otro año desde el descubrimiento |
| 1484 | Vicios ocultos | Apartado 1: el vendedor responde del saneamiento por los defectos ocultos que hagan la cosa impropia para su uso o disminuyan de tal modo ese uso que, de haberlos conocido, el comprador no la habría adquirido o habría dado menos precio. **No responde de los defectos manifiestos o que estuvieren a la vista**, ni de los que no lo estén si el comprador es un perito que por su oficio o profesión debía fácilmente conocerlos. Numerado como apartado 1 y añadido el apartado 2 (animales) por la Ley 17/2021 |
| 1485 | Vicios ignorados por el vendedor | Responde **aunque los ignorase**. No rige cuando se haya estipulado lo contrario **y** el vendedor ignorara los vicios (requisitos acumulativos). Modificado por la Ley 17/2021 |
| 1486 | Opciones del comprador ante el vicio | Desistir del contrato con abono de los gastos pagados, o rebajar una cantidad proporcional del precio a juicio de peritos. Si el vendedor **conocía** los vicios y no los manifesto, el comprador tiene la misma opción y **además indemnización de daños y perjuicios** si opta por la rescisión |
| 1489 | Ventas judiciales | Nunca hay lugar a la responsabilidad por daños y perjuicios; si a todo lo demás |
| 1490 | Plazo de las acciones de saneamiento por vicios | **Se extinguen a los SEIS MESES contados desde la entrega de la cosa vendida.** Redacción originaria de 1889 |
| 1500 | Obligación del comprador | Pagar el precio en el tiempo y lugar fijados por el contrato; si no se fijaron, en el tiempo y lugar de la entrega |
| 1502 | Suspensión del pago por el comprador | Si el comprador es perturbado en la posesión o dominio, o tiene fundado temor de serlo por acción reivindicatoria o hipotecaria, puede suspender el pago del precio hasta que el vendedor haga cesar la perturbación o el peligro, salvo que el vendedor afiance la devolución o se haya estipulado lo contrario |
| 1503 | Resolución a instancia del vendedor | Si el vendedor tiene fundado motivo para temer la pérdida de la cosa inmueble vendida y del precio, puede promover inmediatamente la resolución. Si no existe ese motivo, se aplica el art. 1124 |
| 1504 | Resolución por impago en venta de inmuebles | **Aun cuando se hubiera estipulado que por falta de pago del precio en el tiempo convenido tendrá lugar de pleno derecho la resolución, el comprador podrá pagar, aun después de expirado el término, ínterin no haya sido requerido judicialmente o por acta notarial.** Hecho el requerimiento, el Juez no podrá concederle nuevo término. Redacción originaria de 1889 |
| 1505 | Resolución en bienes muebles | De pleno derecho en interés del vendedor. Fuera del alcance de esta skill (solo inmuebles) |
| 1124 | Resolución de obligaciones reciprocas | El perjudicado puede escoger entre exigir el cumplimiento o la resolución, con resarcimiento de daños e intereses en ambos casos. Puede pedir la resolución aun después de haber optado por el cumplimiento, cuando este resultare imposible. El Tribunal decreta la resolución salvo causas justificadas para señalar plazo |
| 1152 | Cláusula penal | La pena **sustituye** a la indemnización de daños y al abono de intereses en caso de falta de cumplimiento, **si otra cosa no se hubiere pactado** |
| 1255 | Libertad de pactos | Los contratantes pueden establecer los pactos, cláusulas y condiciones que tengan por conveniente, siempre que no sean contrarios a las leyes, a la moral ni al orden público |
| 1279 | Compulsión a la forma | Si la ley exige escritura u otra forma especial para hacer efectivas las obligaciones del contrato, los contratantes **pueden compelerse recíprocamente** a llenar aquella forma desde que hubo consentimiento y demás requisitos de validez |
| 1280.1.º | Forma pública | Deben constar en documento público los actos y contratos que tengan por objeto la creación, transmisión, modificación o extinción de **derechos reales sobre bienes inmuebles**. Última modificación del artículo: Ley 11/1981 (apartado 3, ajeno a este número) |
| 1518 | Reembolso en el retracto | El retrayente debe reembolsar el precio de la venta, los gastos del contrato y cualquier otro pago legítimo hecho para la venta, y los gastos necesarios y útiles hechos en la cosa. **Precepto al que remite expresamente el art. 25.3 LAU** |
| 1875 | Constitución de hipoteca | Es indispensable, para que la hipoteca quede válidamente constituida, que el documento en que se constituya **sea inscrito en el Registro de la Propiedad** |
| 1964.2 | Prescripción de acciones personales | Las acciones personales sin plazo especial prescriben a los **cinco años** desde que pueda exigirse el cumplimiento. Redacción de la Ley 42/2015 |
| 1973 | Interrupción de la prescripción | Se interrumpe por el ejercicio de la acción ante los Tribunales, **por reclamación extrajudicial del acreedor** y por cualquier acto de reconocimiento de la deuda por el deudor. Redacción originaria de 1889 |

---

## LAU art. 25 — Tanteo y retracto del arrendatario (verificado 02/09/2026)

Redacción vigente (última versión del bloque: Real Decreto-ley 7/2019, vigencia 06/03/2019). Contenido operativo:

| Apartado | Regla verificada |
|---|---|
| 25.1 | En caso de venta de la **vivienda arrendada**, el arrendatario tiene derecho de adquisición preferente |
| 25.2 | **Tanteo: treinta días naturales** desde el siguiente a la notificación fehaciente de la decisión de vender, del precio y de las demás condiciones esenciales. Los efectos de esa notificación **caducan a los ciento ochenta días naturales** |
| 25.3 | **Retracto: treinta días naturales** desde el siguiente a la notificación fehaciente que el adquirente debe hacer al arrendatario de las condiciones esenciales de la compraventa, entregando copia de la escritura o documento. Procede cuando **no se hizo la notificación previa, se omitió en ella algún requisito, el precio efectivo resulto inferior o las condiciones menos onerosas**. Se sujeta al art. 1518 CC |
| 25.4 | Preferencia sobre cualquier otro derecho similar, salvo el retracto del condueño o el convencional inscrito antes del arrendamiento |
| 25.5 | **Para inscribir en el Registro de la Propiedad el título de venta de vivienda arrendada hay que justificar que se hicieron las notificaciones.** Si la vivienda no estaba arrendada, el vendedor debe declararlo así en la escritura, **bajo la pena de falsedad en documento público** |
| 25.6 | Si la venta abarca además los accesorios alquilados del art. 3, el arrendatario no puede ejercitar los derechos solo sobre la vivienda |
| 25.7 | **No hay tanteo ni retracto** cuando la vivienda se vende conjuntamente con las restantes viviendas o locales del arrendador que formen parte de un mismo inmueble, ni cuando distintos propietarios venden conjuntamente a un mismo comprador la totalidad de pisos y locales. La legislación de vivienda puede atribuir en esos casos tanteo y retracto sobre la totalidad del inmueble a favor del órgano que designe la Administración competente. **Si en el inmueble solo existiera una vivienda, el arrendatario si tiene tanteo y retracto** |
| 25.8 | **Las partes pueden pactar la renuncia del arrendatario** al derecho de adquisición preferente. Pactada la renuncia, el **arrendador debe comunicar al arrendatario su intención de vender con una antelación mínima de treinta días** a la fecha de formalización del contrato de compraventa |

**Art. 31 LAU** (verificado 02/09/2026, redacción originaria, vigencia 01/01/1995): "Lo dispuesto en el artículo 25 de la presente ley será de aplicación a los arrendamientos que regula este Título" — es decir, **el mismo tanteo y retracto se aplica a los arrendamientos para uso distinto de vivienda** (locales). Consecuencia: el riesgo de retracto no desaparece porque lo arrendado sea un local.

Nota de alcance: la renuncia del 25.8 es un pacto del **contrato de arrendamiento**, no de la compraventa: la skill no la da por buena sin leer ese contrato.

---

## LOE — Obra nueva (verificado 02/09/2026)

| Precepto | Regla verificada |
|---|---|
| art. 17.1 | Plazos de responsabilidad **contados desde la recepción de la obra sin reservas o desde la subsanación de estas**: **diez años** por daños que afecten a cimentación, soportes, vigas, forjados, muros de carga u otros elementos estructurales y comprometan la resistencia mecánica y la estabilidad; **tres años** por vicios de elementos constructivos o instalaciones que incumplan los requisitos de habitabilidad del art. 3.1.c); y **un año** al constructor por vicios de ejecución en elementos de terminación o acabado |
| art. 17.3 | El **promotor responde solidariamente** con los demás agentes ante los adquirentes por los daños materiales por vicios o defectos de construcción |
| art. 17.9 | Estas responsabilidades se entienden **sin perjuicio** de las del vendedor frente al comprador conforme al contrato y a los arts. 1484 y siguientes CC (no se solapan: son vías distintas) |
| art. 19.1 | Garantías de referencia: seguro/caución/garantía financiera de **un año** (acabados; sustituible por retención del 5 % de la ejecución material), **tres años** (habitabilidad) y **diez años** (estructura). Redacción de la Ley 20/2015 |
| art. 19.5 | Capital asegurado mínimo: **5 %** (un año), **30 %** (tres años) y **100 %** (diez años) del coste final de ejecución material, honorarios incluidos |
| art. 20.1 | **No se autorizan ni se inscriben escrituras de declaración de obra nueva** sin acreditar y testimoniar la constitución de las garantías del art. 19 |
| disposición adicional primera, Uno.1 | Quien promueva la construcción de viviendas y pretenda obtener de los adquirentes **entregas de dinero a cuenta** debe: a) **garantizar desde la licencia de edificación** la devolución de las cantidades entregadas más los intereses legales, mediante **seguro de caución o aval solidario** de entidad de crédito, para el caso de que la construcción no se inicie o no llegue a buen fin en el plazo convenido; y b) percibirlas **a través de cuenta especial separada** de cualquier otro fondo del promotor. Redacción de la Ley 20/2015, vigencia 01/01/2016 |
| disposición adicional primera, Tres | El contrato **debe hacer constar expresamente** la obligación de devolución, la referencia al seguro o aval con el nombre de la entidad, y la designación de la entidad de crédito y de la cuenta especial. En el otorgamiento, el promotor entrega al adquirente el documento que acredite la garantía |
| disposición adicional primera, Siete | El incumplimiento de la obligación de constituir garantía da lugar a sanción **de hasta el 25 %** de las cantidades cuya devolución deba asegurarse |

Consecuencia operativa: la venta de **obra nueva sobre plano con entregas a cuenta** exige un aval o seguro de caución individualizado y una cuenta especial. Esta skill **no** redacta ese contrato: escala (ver la tabla de escalación del `SKILL.md`).

---

## Fiscalidad de la transmisión (verificado 02/09/2026)

| Precepto | Regla verificada |
|---|---|
| ITPAJD, art. 8.a) RDLeg 1/1993 | "Estará obligado al pago del Impuesto a título de contribuyente, **y cualesquiera que sean las estipulaciones establecidas por las partes en contrario**: a) En las transmisiones de bienes y derechos de toda clase, **el que los adquiere**" |
| TRLRHL, art. 106.1.b) RDLeg 2/2004 | En las transmisiones de terrenos **a título oneroso**, es sujeto pasivo del IIVTNU (plusvalía municipal) **quien transmite el terreno**. El apartado 2 solo desplaza la condición de sustituto al adquirente cuando el contribuyente sea **persona física no residente en España** |
| LGT, art. 17.5 Ley 58/2003 | "Los elementos de la obligación tributaria **no podrán ser alterados por actos o convenios de los particulares, que no producirán efectos ante la Administración**, sin perjuicio de sus consecuencias jurídico-privadas" |

Consecuencia operativa: un pacto que traslade el ITP al vendedor o la plusvalía al comprador es válido **entre las partes** (acción de reembolso), pero **no** frente a la Administración, que seguirá exigiendo el impuesto al sujeto pasivo legal. La skill lo advierte siempre que se pacte algo distinto del reparto legal.

---

## Plantillas: NO existe modelo oficial de contrato de compraventa

Verificado el 02/09/2026:

- **Consejo General del Notariado** (https://www.notariado.org): publica **guías informativas** para el ciudadano sobre la compra de vivienda y sobre el papel del notario ("¿Qué debería saber antes de adquirir una vivienda?", "Los notarios explican los pasos a seguir en la compraventa de una vivienda y en la solicitud de un préstamo hipotecario"). **No publica un modelo normalizado de contrato privado de compraventa ni de arras.**
- **Colegio de Registradores (CORPME)** (https://www.registradores.org): publica material informativo sobre la inscripción de la compraventa, sobre la nota simple (valor **puramente informativo**, no da fe del contenido de los asientos) y una `Guía de Cargas`. **No publica modelo de contrato.** Confirma expresamente que el documento privado, aunque válido, **no es suficiente para inscribir en el Registro de la Propiedad ni para obtener financiación hipotecaria**: se requiere escritura pública notarial.
- **CGPJ** (https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/): sus modelos normalizados son formularios procesales (verbal, monitorio, jurisdicción voluntaria, justicia gratuita, denuncia, delito leve, juicio rápido). No procede un modelo de contrato: no es un documento judicial.

**Por tanto, los assets de esta skill no reproducen ningún modelo oficial.** Se construyen sobre el contenido legalmente exigido y sobre el contenido cuya omisión genera un riesgo verificado en los preceptos de esta reference:

| Asset | Base normativa de su estructura |
|---|---|
| `assets/contrato-arras.md` | Arts. 1254, 1255, 1445, 1450, **1454**, 1152 y 1124 CC; art. 25 LAU si el inmueble está arrendado; arts. 8 ITPAJD y 106 TRLRHL para el reparto fiscal |
| `assets/contrato-compraventa-vivienda.md` | Arts. 1255, 1445, 1450, 1455, 1461, 1462, 1465, 1468, 1469, 1474, 1475, 1483, 1484 a 1486, 1490, 1500, 1502, 1504, 1124, 1279 y 1280.1.º CC; art. 25 LAU; arts. 17, 19 y 20 LOE si es obra nueva; arts. 8 ITPAJD, 106 TRLRHL y 17.5 LGT |
| `assets/requerimiento-cumplimiento.md` | Arts. **1504**, 1124, 1152, 1279, 1500, 1502 y 1503 CC; art. 1973 CC para la interrupción de la prescripción |

---

## Verificar manualmente (no resuelto por fuente oficial)

1. **Clasificación de las arras en confirmatorias, penales y penitenciales.** **NO es una clasificación legal.** El art. 1454 CC, verificado en su literal íntegro el 02/09/2026, solo contempla el desistimiento (perderlas o devolverlas duplicadas) y no define categoría alguna. La triple calificación es **construcción jurisprudencial**: la skill la explica como tal, nunca como categorías del Código. Del **silencio** del contrato la jurisprudencia tiende a presumir el carácter **confirmatorio** (arras como señal y parte del precio, que NO facultan para desistir), por lo que el asset debe pactar **expresamente** la clase de arras y su consecuencia. Esta skill **no cita sentencias**: si el usuario necesita apoyo jurisprudencial concreto, se escala. Punto de mayor riesgo de la skill.
2. **Derecho civil foral o especial.** Los assets se construyen sobre el **Código Civil común**. Cataluña regula la compraventa en el Llibre sise del Codi civil de Catalunya, con reglas propias en materia de arras, entrega, saneamiento y remedios del comprador; Navarra, Aragon, Baleares, Galicia y País Vasco tienen también derecho civil propio con incidencia posible. **Verificar la vecindad civil y la ley aplicable antes de firmar**; si el caso se rige por derecho foral, escalar.
3. **Tipo de gravamen del ITP.** Lo fija cada Comunidad Autónoma y varía por territorio y por el perfil del adquirente (joven, familia numerosa, discapacidad, vivienda habitual). La skill **no calcula la cuota**: pide el dato o lo deja como placeholder y remite a la normativa autonómica vigente.
4. **Cuota del IIVTNU (plusvalía municipal).** Tras la STC 182/2021 y el Real Decreto-ley 26/2021, la base imponible se determina conforme a los arts. 104.5 y 107 TRLRHL, con coeficientes que se actualizan y con ordenanza municipal propia. La skill **no calcula la cuota**: identifica al sujeto pasivo legal (el vendedor) y remite a la ordenanza del municipio.
5. **Vigencia de la licencia de primera ocupación, cédula de habitabilidad y certificado de eficiencia energética.** Requisitos de origen mayoritariamente autonómico y municipal. La skill los relaciona como documentación a entregar, sin afirmar cuál es obligatorio en el territorio concreto.
6. **Zonas de tanteo y retracto administrativo.** Además del art. 25 LAU, varias leyes autonómicas de vivienda establecen derechos de tanteo y retracto a favor de la Administración en áreas delimitadas o en transmisiones de vivienda protegida. **Verificar la normativa autonómica de vivienda del municipio antes de firmar.**
7. **Redacción literal de los artículos.** La API del BOE devuelve el texto consolidado vigente, que es la fuente usada aquí. Antes de transcribir literalmente un precepto en un documento que se firme o se presente, contrastarlo de nuevo en el BOE.
