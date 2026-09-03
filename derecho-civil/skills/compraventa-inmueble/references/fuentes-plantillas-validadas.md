# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-compraventa-inmueble`. Registra las fuentes normativas y las
> plantillas validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso de verificacion se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa expresamente al usuario de que debe verificarla manualmente antes de firmar.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Codigo Civil (texto consolidado) — compraventa, saneamiento, resolucion y forma | BOE-A-1889-4763 | preceptos de compraventa en redaccion originaria de 1889, salvo art. 1484 y 1485 (Ley 17/2021, vigencia 05/01/2022), art. 1280.3 (Ley 11/1981, vigencia 08/06/1981) y art. 1964 (Ley 42/2015, vigencia 07/10/2015). Verificado 02/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| LAU — Ley 29/1994, de Arrendamientos Urbanos, art. 25 (adquisicion preferente) | BOE-A-1994-26003 | art. 25 en la redaccion del Real Decreto-ley 7/2019, vigencia 06/03/2019 (apartado 7); apartado 8 en la redaccion de la Ley 4/2013. Verificado 02/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003 |
| LOE — Ley 38/1999, de Ordenacion de la Edificacion | BOE-A-1999-21567 | art. 17 y art. 20 en redaccion originaria (vigencia 06/05/2000); art. 19 y disposicion adicional primera en la redaccion de la Ley 20/2015, vigencia 01/01/2016. Verificado 02/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1999-21567 |
| ITPAJD — Real Decreto Legislativo 1/1993, art. 8 (sujeto pasivo) | BOE-A-1993-25359 | art. 8 en redaccion originaria, vigencia 21/10/1993. Verificado 02/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1993-25359 |
| TRLRHL — Real Decreto Legislativo 2/2004, art. 106 (sujeto pasivo del IIVTNU) | BOE-A-2004-4214 | art. 106 en la redaccion de la Ley 18/2014, vigencia 17/10/2014 (suprimido su apartado 3). Verificado 02/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 |
| LGT — Ley 58/2003, General Tributaria, art. 17 (inalterabilidad de la obligacion tributaria) | BOE-A-2003-23186 | art. 17.5 en la redaccion del Real Decreto-ley 20/2011, vigencia 01/01/2012 (el antiguo 17.4 se renumero como 17.5). Verificado 02/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 |

**Endpoint de verificacion articulo por articulo (API de legislacion consolidada del BOE).** Devuelve todas las versiones historicas del precepto; **la ultima `<version>` del bloque es la vigente**. Requiere cabecera `Accept: application/xml`:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{ID_BOE}/texto/bloque/{bloque}
```

- Codigo Civil (BOE-A-1889-4763): bloques `artNNNN` — ejemplo `.../bloque/art1454`.
- LAU (BOE-A-1994-26003), LOE (BOE-A-1999-21567), ITPAJD, TRLRHL y LGT: bloques `aNN` — ejemplo `.../bloque/a25`. Las disposiciones adicionales de la LOE usan `daprimera` (no `da1`, que devuelve 404).

---

## Articulos del Codigo Civil verificados el 02/09/2026

| Articulo | Materia | Redaccion vigente verificada |
|---|---|---|
| 1445 | Concepto de compraventa | Un contratante se obliga a entregar una cosa determinada y el otro a pagar por ella un precio cierto, en dinero o signo que lo represente. Redaccion originaria de 1889 |
| 1450 | Perfeccion del contrato | La venta se perfecciona entre comprador y vendedor, y es obligatoria para ambos, si hubieren convenido en la cosa y en el precio, **aunque ni la una ni el otro se hayan entregado**. Redaccion originaria de 1889 |
| 1454 | Arras o senal | **Literal integro:** "Si hubiesen mediado arras o senal en el contrato de compra y venta, podra rescindirse el contrato allanandose el comprador a perderlas, o el vendedor a devolverlas duplicadas." Redaccion originaria de 1889, vigente sin modificacion. **El precepto NO clasifica las arras ni define tipos: solo contempla el desistimiento** (ver `arras-cargas-fiscalidad-y-retracto.md`, apartado 1) |
| 1455 | Gastos de escritura | Los gastos de otorgamiento de escrituras son de cuenta del **vendedor**; los de la primera copia y los demas posteriores a la venta, de cuenta del **comprador**, salvo pacto en contrario. Redaccion originaria de 1889 |
| 1461 | Obligacion basica del vendedor | Entrega y saneamiento de la cosa objeto de la venta |
| 1462 | Entrega. Traditio instrumental | Se entiende entregada cuando se pone en poder y posesion del comprador. **Cuando la venta se hace mediante escritura publica, el otorgamiento de esta equivale a la entrega**, si de la misma escritura no resultare o se dedujere claramente lo contrario |
| 1465 | Gastos de entrega | Los de entrega, a cargo del vendedor; los de transporte o traslacion, del comprador, salvo estipulacion especial |
| 1468 | Estado de la cosa y frutos | Se entrega en el estado en que se hallaba al perfeccionarse el contrato. Los frutos pertenecen al comprador desde la perfeccion |
| 1469 | Cabida del inmueble | Si la venta se hizo con expresion de cabida y a razon de un precio por unidad de medida, el comprador puede exigir todo lo expresado; si no es posible, puede optar entre rebaja proporcional del precio o rescision, y esta ultima solo si la disminucion **excede de la decima parte** de la cabida atribuida (o si el menor valor excede de la decima parte del precio, cuando la diferencia sea de calidad) |
| 1474 | Contenido del saneamiento | El vendedor responde de: 1.º la posesion legal y pacifica de la cosa vendida; 2.º los vicios o defectos ocultos que tuviere |
| 1475 | Eviccion | Se prive al comprador por sentencia firme y en virtud de un derecho anterior a la compra. **El vendedor responde aunque nada se haya expresado en el contrato**, pero los contratantes pueden aumentar, disminuir o suprimir esa obligacion legal |
| 1483 | Cargas o servidumbres no aparentes | Si la finca esta gravada, sin mencionarlo la escritura, con una carga o servidumbre no aparente de tal naturaleza que deba presumirse que el comprador no la habria adquirido si la hubiera conocido, puede pedir la rescision o preferir la indemnizacion. Plazo: **un ano desde el otorgamiento de la escritura** para la accion rescisoria o la indemnizacion; transcurrido, solo indemnizacion, dentro de otro ano desde el descubrimiento |
| 1484 | Vicios ocultos | Apartado 1: el vendedor responde del saneamiento por los defectos ocultos que hagan la cosa impropia para su uso o disminuyan de tal modo ese uso que, de haberlos conocido, el comprador no la habria adquirido o habria dado menos precio. **No responde de los defectos manifiestos o que estuvieren a la vista**, ni de los que no lo esten si el comprador es un perito que por su oficio o profesion debia facilmente conocerlos. Numerado como apartado 1 y anadido el apartado 2 (animales) por la Ley 17/2021 |
| 1485 | Vicios ignorados por el vendedor | Responde **aunque los ignorase**. No rige cuando se haya estipulado lo contrario **y** el vendedor ignorara los vicios (requisitos acumulativos). Modificado por la Ley 17/2021 |
| 1486 | Opciones del comprador ante el vicio | Desistir del contrato con abono de los gastos pagados, o rebajar una cantidad proporcional del precio a juicio de peritos. Si el vendedor **conocia** los vicios y no los manifesto, el comprador tiene la misma opcion y **ademas indemnizacion de danos y perjuicios** si opta por la rescision |
| 1489 | Ventas judiciales | Nunca hay lugar a la responsabilidad por danos y perjuicios; si a todo lo demas |
| 1490 | Plazo de las acciones de saneamiento por vicios | **Se extinguen a los SEIS MESES contados desde la entrega de la cosa vendida.** Redaccion originaria de 1889 |
| 1500 | Obligacion del comprador | Pagar el precio en el tiempo y lugar fijados por el contrato; si no se fijaron, en el tiempo y lugar de la entrega |
| 1502 | Suspension del pago por el comprador | Si el comprador es perturbado en la posesion o dominio, o tiene fundado temor de serlo por accion reivindicatoria o hipotecaria, puede suspender el pago del precio hasta que el vendedor haga cesar la perturbacion o el peligro, salvo que el vendedor afiance la devolucion o se haya estipulado lo contrario |
| 1503 | Resolucion a instancia del vendedor | Si el vendedor tiene fundado motivo para temer la perdida de la cosa inmueble vendida y del precio, puede promover inmediatamente la resolucion. Si no existe ese motivo, se aplica el art. 1124 |
| 1504 | Resolucion por impago en venta de inmuebles | **Aun cuando se hubiera estipulado que por falta de pago del precio en el tiempo convenido tendra lugar de pleno derecho la resolucion, el comprador podra pagar, aun despues de expirado el termino, interin no haya sido requerido judicialmente o por acta notarial.** Hecho el requerimiento, el Juez no podra concederle nuevo termino. Redaccion originaria de 1889 |
| 1505 | Resolucion en bienes muebles | De pleno derecho en interes del vendedor. Fuera del alcance de esta skill (solo inmuebles) |
| 1124 | Resolucion de obligaciones reciprocas | El perjudicado puede escoger entre exigir el cumplimiento o la resolucion, con resarcimiento de danos e intereses en ambos casos. Puede pedir la resolucion aun despues de haber optado por el cumplimiento, cuando este resultare imposible. El Tribunal decreta la resolucion salvo causas justificadas para senalar plazo |
| 1152 | Clausula penal | La pena **sustituye** a la indemnizacion de danos y al abono de intereses en caso de falta de cumplimiento, **si otra cosa no se hubiere pactado** |
| 1255 | Libertad de pactos | Los contratantes pueden establecer los pactos, clausulas y condiciones que tengan por conveniente, siempre que no sean contrarios a las leyes, a la moral ni al orden publico |
| 1279 | Compulsion a la forma | Si la ley exige escritura u otra forma especial para hacer efectivas las obligaciones del contrato, los contratantes **pueden compelerse reciprocamente** a llenar aquella forma desde que hubo consentimiento y demas requisitos de validez |
| 1280.1.º | Forma publica | Deben constar en documento publico los actos y contratos que tengan por objeto la creacion, transmision, modificacion o extincion de **derechos reales sobre bienes inmuebles**. Ultima modificacion del articulo: Ley 11/1981 (apartado 3, ajeno a este numero) |
| 1518 | Reembolso en el retracto | El retrayente debe reembolsar el precio de la venta, los gastos del contrato y cualquier otro pago legitimo hecho para la venta, y los gastos necesarios y utiles hechos en la cosa. **Precepto al que remite expresamente el art. 25.3 LAU** |
| 1875 | Constitucion de hipoteca | Es indispensable, para que la hipoteca quede validamente constituida, que el documento en que se constituya **sea inscrito en el Registro de la Propiedad** |
| 1964.2 | Prescripcion de acciones personales | Las acciones personales sin plazo especial prescriben a los **cinco anos** desde que pueda exigirse el cumplimiento. Redaccion de la Ley 42/2015 |
| 1973 | Interrupcion de la prescripcion | Se interrumpe por el ejercicio de la accion ante los Tribunales, **por reclamacion extrajudicial del acreedor** y por cualquier acto de reconocimiento de la deuda por el deudor. Redaccion originaria de 1889 |

---

## LAU art. 25 — Tanteo y retracto del arrendatario (verificado 02/09/2026)

Redaccion vigente (ultima version del bloque: Real Decreto-ley 7/2019, vigencia 06/03/2019). Contenido operativo:

| Apartado | Regla verificada |
|---|---|
| 25.1 | En caso de venta de la **vivienda arrendada**, el arrendatario tiene derecho de adquisicion preferente |
| 25.2 | **Tanteo: treinta dias naturales** desde el siguiente a la notificacion fehaciente de la decision de vender, del precio y de las demas condiciones esenciales. Los efectos de esa notificacion **caducan a los ciento ochenta dias naturales** |
| 25.3 | **Retracto: treinta dias naturales** desde el siguiente a la notificacion fehaciente que el adquirente debe hacer al arrendatario de las condiciones esenciales de la compraventa, entregando copia de la escritura o documento. Procede cuando **no se hizo la notificacion previa, se omitio en ella algun requisito, el precio efectivo resulto inferior o las condiciones menos onerosas**. Se sujeta al art. 1518 CC |
| 25.4 | Preferencia sobre cualquier otro derecho similar, salvo el retracto del condueno o el convencional inscrito antes del arrendamiento |
| 25.5 | **Para inscribir en el Registro de la Propiedad el titulo de venta de vivienda arrendada hay que justificar que se hicieron las notificaciones.** Si la vivienda no estaba arrendada, el vendedor debe declararlo asi en la escritura, **bajo la pena de falsedad en documento publico** |
| 25.6 | Si la venta abarca ademas los accesorios alquilados del art. 3, el arrendatario no puede ejercitar los derechos solo sobre la vivienda |
| 25.7 | **No hay tanteo ni retracto** cuando la vivienda se vende conjuntamente con las restantes viviendas o locales del arrendador que formen parte de un mismo inmueble, ni cuando distintos propietarios venden conjuntamente a un mismo comprador la totalidad de pisos y locales. La legislacion de vivienda puede atribuir en esos casos tanteo y retracto sobre la totalidad del inmueble a favor del organo que designe la Administracion competente. **Si en el inmueble solo existiera una vivienda, el arrendatario si tiene tanteo y retracto** |
| 25.8 | **Las partes pueden pactar la renuncia del arrendatario** al derecho de adquisicion preferente. Pactada la renuncia, el **arrendador debe comunicar al arrendatario su intencion de vender con una antelacion minima de treinta dias** a la fecha de formalizacion del contrato de compraventa |

**Art. 31 LAU** (verificado 02/09/2026, redaccion originaria, vigencia 01/01/1995): "Lo dispuesto en el articulo 25 de la presente ley sera de aplicacion a los arrendamientos que regula este Titulo" — es decir, **el mismo tanteo y retracto se aplica a los arrendamientos para uso distinto de vivienda** (locales). Consecuencia: el riesgo de retracto no desaparece porque lo arrendado sea un local.

Nota de alcance: la renuncia del 25.8 es un pacto del **contrato de arrendamiento**, no de la compraventa: la skill no la da por buena sin leer ese contrato.

---

## LOE — Obra nueva (verificado 02/09/2026)

| Precepto | Regla verificada |
|---|---|
| art. 17.1 | Plazos de responsabilidad **contados desde la recepcion de la obra sin reservas o desde la subsanacion de estas**: **diez anos** por danos que afecten a cimentacion, soportes, vigas, forjados, muros de carga u otros elementos estructurales y comprometan la resistencia mecanica y la estabilidad; **tres anos** por vicios de elementos constructivos o instalaciones que incumplan los requisitos de habitabilidad del art. 3.1.c); y **un ano** al constructor por vicios de ejecucion en elementos de terminacion o acabado |
| art. 17.3 | El **promotor responde solidariamente** con los demas agentes ante los adquirentes por los danos materiales por vicios o defectos de construccion |
| art. 17.9 | Estas responsabilidades se entienden **sin perjuicio** de las del vendedor frente al comprador conforme al contrato y a los arts. 1484 y siguientes CC (no se solapan: son vias distintas) |
| art. 19.1 | Garantias de referencia: seguro/caucion/garantia financiera de **un ano** (acabados; sustituible por retencion del 5 % de la ejecucion material), **tres anos** (habitabilidad) y **diez anos** (estructura). Redaccion de la Ley 20/2015 |
| art. 19.5 | Capital asegurado minimo: **5 %** (un ano), **30 %** (tres anos) y **100 %** (diez anos) del coste final de ejecucion material, honorarios incluidos |
| art. 20.1 | **No se autorizan ni se inscriben escrituras de declaracion de obra nueva** sin acreditar y testimoniar la constitucion de las garantias del art. 19 |
| disposicion adicional primera, Uno.1 | Quien promueva la construccion de viviendas y pretenda obtener de los adquirentes **entregas de dinero a cuenta** debe: a) **garantizar desde la licencia de edificacion** la devolucion de las cantidades entregadas mas los intereses legales, mediante **seguro de caucion o aval solidario** de entidad de credito, para el caso de que la construccion no se inicie o no llegue a buen fin en el plazo convenido; y b) percibirlas **a traves de cuenta especial separada** de cualquier otro fondo del promotor. Redaccion de la Ley 20/2015, vigencia 01/01/2016 |
| disposicion adicional primera, Tres | El contrato **debe hacer constar expresamente** la obligacion de devolucion, la referencia al seguro o aval con el nombre de la entidad, y la designacion de la entidad de credito y de la cuenta especial. En el otorgamiento, el promotor entrega al adquirente el documento que acredite la garantia |
| disposicion adicional primera, Siete | El incumplimiento de la obligacion de constituir garantia da lugar a sancion **de hasta el 25 %** de las cantidades cuya devolucion deba asegurarse |

Consecuencia operativa: la venta de **obra nueva sobre plano con entregas a cuenta** exige un aval o seguro de caucion individualizado y una cuenta especial. Esta skill **no** redacta ese contrato: escala (ver la tabla de escalacion del `SKILL.md`).

---

## Fiscalidad de la transmision (verificado 02/09/2026)

| Precepto | Regla verificada |
|---|---|
| ITPAJD, art. 8.a) RDLeg 1/1993 | "Estara obligado al pago del Impuesto a titulo de contribuyente, **y cualesquiera que sean las estipulaciones establecidas por las partes en contrario**: a) En las transmisiones de bienes y derechos de toda clase, **el que los adquiere**" |
| TRLRHL, art. 106.1.b) RDLeg 2/2004 | En las transmisiones de terrenos **a titulo oneroso**, es sujeto pasivo del IIVTNU (plusvalia municipal) **quien transmite el terreno**. El apartado 2 solo desplaza la condicion de sustituto al adquirente cuando el contribuyente sea **persona fisica no residente en Espana** |
| LGT, art. 17.5 Ley 58/2003 | "Los elementos de la obligacion tributaria **no podran ser alterados por actos o convenios de los particulares, que no produciran efectos ante la Administracion**, sin perjuicio de sus consecuencias juridico-privadas" |

Consecuencia operativa: un pacto que traslade el ITP al vendedor o la plusvalia al comprador es valido **entre las partes** (accion de reembolso), pero **no** frente a la Administracion, que seguira exigiendo el impuesto al sujeto pasivo legal. La skill lo advierte siempre que se pacte algo distinto del reparto legal.

---

## Plantillas: NO existe modelo oficial de contrato de compraventa

Verificado el 02/09/2026:

- **Consejo General del Notariado** (https://www.notariado.org): publica **guias informativas** para el ciudadano sobre la compra de vivienda y sobre el papel del notario ("¿Que deberia saber antes de adquirir una vivienda?", "Los notarios explican los pasos a seguir en la compraventa de una vivienda y en la solicitud de un prestamo hipotecario"). **No publica un modelo normalizado de contrato privado de compraventa ni de arras.**
- **Colegio de Registradores (CORPME)** (https://www.registradores.org): publica material informativo sobre la inscripcion de la compraventa, sobre la nota simple (valor **puramente informativo**, no da fe del contenido de los asientos) y una `Guia de Cargas`. **No publica modelo de contrato.** Confirma expresamente que el documento privado, aunque valido, **no es suficiente para inscribir en el Registro de la Propiedad ni para obtener financiacion hipotecaria**: se requiere escritura publica notarial.
- **CGPJ** (https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/): sus modelos normalizados son formularios procesales (verbal, monitorio, jurisdiccion voluntaria, justicia gratuita, denuncia, delito leve, juicio rapido). No procede un modelo de contrato: no es un documento judicial.

**Por tanto, los assets de esta skill no reproducen ningun modelo oficial.** Se construyen sobre el contenido legalmente exigido y sobre el contenido cuya omision genera un riesgo verificado en los preceptos de esta reference:

| Asset | Base normativa de su estructura |
|---|---|
| `assets/contrato-arras.md` | Arts. 1254, 1255, 1445, 1450, **1454**, 1152 y 1124 CC; art. 25 LAU si el inmueble esta arrendado; arts. 8 ITPAJD y 106 TRLRHL para el reparto fiscal |
| `assets/contrato-compraventa-vivienda.md` | Arts. 1255, 1445, 1450, 1455, 1461, 1462, 1465, 1468, 1469, 1474, 1475, 1483, 1484 a 1486, 1490, 1500, 1502, 1504, 1124, 1279 y 1280.1.º CC; art. 25 LAU; arts. 17, 19 y 20 LOE si es obra nueva; arts. 8 ITPAJD, 106 TRLRHL y 17.5 LGT |
| `assets/requerimiento-cumplimiento.md` | Arts. **1504**, 1124, 1152, 1279, 1500, 1502 y 1503 CC; art. 1973 CC para la interrupcion de la prescripcion |

---

## Verificar manualmente (no resuelto por fuente oficial)

1. **Clasificacion de las arras en confirmatorias, penales y penitenciales.** **NO es una clasificacion legal.** El art. 1454 CC, verificado en su literal integro el 02/09/2026, solo contempla el desistimiento (perderlas o devolverlas duplicadas) y no define categoria alguna. La triple calificacion es **construccion jurisprudencial**: la skill la explica como tal, nunca como categorias del Codigo. Del **silencio** del contrato la jurisprudencia tiende a presumir el caracter **confirmatorio** (arras como senal y parte del precio, que NO facultan para desistir), por lo que el asset debe pactar **expresamente** la clase de arras y su consecuencia. Esta skill **no cita sentencias**: si el usuario necesita apoyo jurisprudencial concreto, se escala. Punto de mayor riesgo de la skill.
2. **Derecho civil foral o especial.** Los assets se construyen sobre el **Codigo Civil comun**. Cataluna regula la compraventa en el Llibre sise del Codi civil de Catalunya, con reglas propias en materia de arras, entrega, saneamiento y remedios del comprador; Navarra, Aragon, Baleares, Galicia y Pais Vasco tienen tambien derecho civil propio con incidencia posible. **Verificar la vecindad civil y la ley aplicable antes de firmar**; si el caso se rige por derecho foral, escalar.
3. **Tipo de gravamen del ITP.** Lo fija cada Comunidad Autonoma y varia por territorio y por el perfil del adquirente (joven, familia numerosa, discapacidad, vivienda habitual). La skill **no calcula la cuota**: pide el dato o lo deja como placeholder y remite a la normativa autonomica vigente.
4. **Cuota del IIVTNU (plusvalia municipal).** Tras la STC 182/2021 y el Real Decreto-ley 26/2021, la base imponible se determina conforme a los arts. 104.5 y 107 TRLRHL, con coeficientes que se actualizan y con ordenanza municipal propia. La skill **no calcula la cuota**: identifica al sujeto pasivo legal (el vendedor) y remite a la ordenanza del municipio.
5. **Vigencia de la licencia de primera ocupacion, cedula de habitabilidad y certificado de eficiencia energetica.** Requisitos de origen mayoritariamente autonomico y municipal. La skill los relaciona como documentacion a entregar, sin afirmar cual es obligatorio en el territorio concreto.
6. **Zonas de tanteo y retracto administrativo.** Ademas del art. 25 LAU, varias leyes autonomicas de vivienda establecen derechos de tanteo y retracto a favor de la Administracion en areas delimitadas o en transmisiones de vivienda protegida. **Verificar la normativa autonomica de vivienda del municipio antes de firmar.**
7. **Redaccion literal de los articulos.** La API del BOE devuelve el texto consolidado vigente, que es la fuente usada aqui. Antes de transcribir literalmente un precepto en un documento que se firme o se presente, contrastarlo de nuevo en el BOE.
