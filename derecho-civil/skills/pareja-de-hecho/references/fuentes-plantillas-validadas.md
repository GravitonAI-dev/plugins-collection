# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-pareja-de-hecho`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica en cada lanzamiento para aplicar la redacción vigente al documento que redacta.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa al usuario.

---

## Regla especial de la normativa autonómica (NUNCA se da por sabida)

**No existe ley estatal de parejas de hecho ni registro estatal.** La constitución de la pareja, sus requisitos, el carácter constitutivo o meramente declarativo de la inscripción y los efectos civiles, sucesorios y fiscales dependen enteramente de la ley de cada comunidad autónoma (17 regulaciones distintas, más los registros municipales). El Código Civil **no** regula la pareja de hecho.

Consecuencia operativa, sin excepciones:

1. La comunidad autónoma es un **vector obligatorio** del árbol de decisión en todas las ramas de la skill.
2. La normativa autonómica y su registro **se verifican con `web_search` en CADA lanzamiento**, contra el boletín oficial de la comunidad autónoma o el texto consolidado del BOE de esa ley autonómica y contra la sede electrónica del registro. **Esta reference NO almacena los requisitos de las 17 comunidades**: hacerlo invitaría a citarlos de memoria y quedarían obsoletos sin aviso.
3. La fecha de la verificación se hace constar en el documento generado (`{{FECHA_VERIFICACION_NORMATIVA_AUTONOMICA}}`) junto con la denominación exacta de la ley y el enlace consultado.
4. **Si la verificación falla**, la skill lo dice expresamente, no afirma ningún requisito autonómico y marca el punto como pendiente de comprobación en el propio documento. Prohibido rellenar el hueco con conocimiento previo del modelo.

| Fuente | Qué se verifica | Cuándo |
|---|---|---|
| Ley autonómica de parejas de hecho / uniones o parejas estables de la comunidad indicada por el usuario | Denominación exacta y vigencia; requisitos de constitución (edad, tiempo previo de convivencia, empadronamiento, vecindad civil o administrativa); carácter constitutivo o declarativo de la inscripción; efectos que la ley atribuye; preceptos anulados por el Tribunal Constitucional | Cada lanzamiento |
| Sede electrónica del registro autonómico (y, en su caso, municipal) de parejas de hecho | Denominación oficial del registro, documentación exigida, forma de solicitud, tasa y plazos | Cada lanzamiento |

---

## Fuentes normativas estatales (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Código Civil | BOE-A-1889-4763 | arts. 1255, 1258, 1261, 1274, 1275 y 1902 en redacción originaria de 1889; art. 1323 en redacción de la Ley 13/2005 (vigente 03/07/2005); art. 1438 en redacción de la Ley 11/1981 (vigente 08/06/1981); arts. 392 a 400 y 406 en redacción originaria, art. 401 modificado por la Ley 49/1960 y art. 404 por la Ley 17/2021 (vigente 05/01/2022) — verificado 03/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| LGSS — Real Decreto Legislativo 8/2015, texto refundido de la Ley General de la Seguridad Social (art. 221, pensión de viudedad de la pareja de hecho) | BOE-A-2015-11724 | redacción de la Ley 21/2021, de 28 de diciembre, vigente desde 01/01/2022 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| TRLRCSCVM — Real Decreto Legislativo 8/2004 (baremo de accidentes de circulación), arts. 36 y 62, en la redacción dada por la **Ley 35/2015** | BOE-A-2004-18911 (redacción: BOE-A-2015-10197) | redacción de la Ley 35/2015, vigente desde 01/01/2016 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2004-18911 |
| Ley 11/2001, de Uniones de Hecho de la Comunidad de Madrid *(ejemplo de ley autonómica; NO extrapolable a otras comunidades)* | BOE-A-2002-4374 | texto consolidado con última actualización publicada el 26/12/2024, vigente desde 27/12/2024 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2002-4374 |

**Endpoint de verificación artículo por artículo (API de legislación consolidada del BOE).** Devuelve todas las versiones históricas del precepto; la última es la vigente. Requiere cabecera `Accept: application/xml`:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{numero_articulo}
```

**Aviso de formato de identificador de bloque:** el Código Civil usa `art1255`; la LGSS y el TRLRCSCVM usan `a221` y `a36`. Si un identificador devuelve 404, probar la otra convención antes de dar la fuente por inaccesible.

---

## Artículos verificados el 03/09/2026

| Precepto | Materia | Redacción vigente verificada |
|---|---|---|
| CC 1255 | Autonomía de la voluntad | "Los contratantes pueden establecer los pactos, cláusulas y condiciones que tengan por conveniente, siempre que no sean contrarios a las leyes, a la moral ni al orden público." **Es la base jurídica del pacto de convivencia y del pacto de ruptura**: no hay norma estatal que regule el contenido económico de la pareja de hecho, y son las partes quienes lo fijan |
| CC 1258 | Perfección del contrato | Los contratos se perfeccionan por el mero consentimiento y obligan también a las consecuencias conformes a la buena fe, al uso y a la ley |
| CC 1261, 1274 y 1275 | Requisitos del contrato y causa | 1261: consentimiento, objeto cierto y causa. 1274: en los contratos onerosos la causa es la prestación o promesa de la otra parte; en los remuneratorios, el servicio que se remunera. 1275: los contratos sin causa o con causa ilícita no producen efecto alguno. **Relevante para blindar la compensación pactada: hay que expresar su causa** |
| CC 1323 | Contratación entre cónyuges | "Los cónyuges podrán transmitirse por cualquier título bienes y derechos y celebrar entre si toda clase de contratos" (Ley 13/2005). **Se refiere solo a cónyuges.** Entre convivientes no casados la libertad de contratar no necesita este precepto: deriva directamente del art. 1255. Citarlo como base directa del pacto sería impreciso |
| CC 1438 | Compensación por trabajo doméstico | "Los cónyuges contribuirán al sostenimiento de las cargas del matrimonio. A falta de convenio lo harán proporcionalmente a sus respectivos recursos económicos. El trabajo para la casa será computado como contribución a las cargas y dará derecho a obtener una compensación que el Juez señalará, a falta de acuerdo, a la extinción del régimen de separación" (Ley 11/1981). **Es una norma del RÉGIMEN DE SEPARACIÓN DE BIENES DEL MATRIMONIO.** Su aplicación analógica a la pareja de hecho es jurisprudencial y discutida: ver el apartado de jurisprudencia. Prohibido presentarla como derecho automático del conviviente |
| CC 392 a 406 | Comunidad de bienes | 392: hay comunidad cuando la propiedad pertenece pro indiviso a varias personas; a falta de contratos o disposiciones especiales rige este título. 393: el concurso en beneficios y cargas es proporcional a las cuotas, **que se presumen iguales mientras no se pruebe lo contrario**. 394: uso conforme al destino sin perjudicar a los demás. 395: derecho a obligar a contribuir a los gastos de conservación. 398: acuerdos por mayoría de intereses para la administración. 399: cada condueño tiene la plena propiedad de su parte y puede enajenarla. 400: nadie está obligado a permanecer en la comunidad y puede pedir la división en cualquier tiempo; **es válido el pacto de indivisión por tiempo determinado no superior a diez años, prorrogable**. 401: no cabe exigir la división si la cosa resulta inservible. 404: si la cosa es esencialmente indivisible y no hay acuerdo de adjudicación con indemnización, se vende y se reparte el precio (párrafos sobre animales de compañía añadidos por la Ley 17/2021). 406: a la división se aplican las reglas de la división de la herencia |
| CC 1902 | Responsabilidad extracontractual | Quien por acción u omisión causa daño a otro, interviniendo culpa o negligencia, está obligado a repararlo. Vía residual y de difícil éxito en la ruptura de pareja: exige culpa o negligencia y daño acreditado, no basta la ruptura |
| LGSS 221 | Pensión de viudedad de la pareja de hecho | Redacción de la Ley 21/2021 (vigente 01/01/2022). Requisitos acumulativos, **distintos de los del registro autonómico**: (a) cumplir los requisitos del art. 219; (b) pareja constituida con análoga relación de afectividad a la conyugal, sin impedimento para contraer matrimonio, sin vínculo matrimonial ni otra pareja de hecho; (c) **convivencia estable y notoria acreditada por certificado de empadronamiento, ininterrumpida no inferior a CINCO años**, salvo que existan hijos en común, en cuyo caso basta acreditar la constitución de la pareja; (d) la existencia de la pareja se acredita por **certificación de inscripción en un registro autonómico o municipal, o por documento público**, y tanto la inscripción como el documento público deben tener **una antelación mínima de DOS años** respecto del fallecimiento. El apartado 3 regula el supuesto de pareja ya extinguida en vida (exige ser acreedor de pensión compensatoria fijada judicialmente o en convenio o pacto en documento público), con regla propia para víctimas de violencia de género |
| TRLRCSCVM 36.2 y 62 | Baremo de accidentes de circulación (Ley 35/2015) | Art. 36.2: "se considera que sufre el mismo perjuicio resarcible que el cónyuge viudo el miembro supérstite de una pareja de hecho estable constituida mediante inscripción en un registro o documento público o que haya convivido un mínimo de un año inmediatamente anterior al fallecimiento o un periodo inferior si tiene un hijo en común". Art. 62: en caso de muerte hay cinco categorías autónomas de perjudicados, la primera de ellas el cónyuge viudo. **Es uno de los pocos ámbitos estatales en que la pareja de hecho está expresamente equiparada, y con requisitos propios más laxos que los de la viudedad** |

---

## Jurisprudencia verificada en esta sesión (03/09/2026)

Verificada a través de publicaciones oficiales del BOE. **Ninguna otra sentencia puede citarse sin verificarla en el lanzamiento.**

| Resolución | Fuente oficial consultada | Criterio verificado |
|---|---|---|
| STC 81/2013, de 11 de abril | Referencia BOE-A-2013-4901, recogida en las notas de vigencia del texto consolidado de la Ley 11/2001 de la Comunidad de Madrid (https://www.boe.es/buscar/act.php?id=BOE-A-2002-4374) | Declara inconstitucionales y nulos los artículos 4 y 5 de la Ley 11/2001 de Uniones de Hecho de la Comunidad de Madrid (pactos de convivencia y su inscripción), por invadir la competencia estatal en materia de legislación civil |
| STC 93/2013, de 23 de abril | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2013-5436 | Declara la nulidad de diversos preceptos de la Ley Foral 6/2000 de Navarra. Criterio nuclear: **no puede imponerse a una pareja estable un régimen jurídico por el mero hecho de la convivencia, sin una manifestación de voluntad de someterse a el** (art. 10.1 CE, libre desarrollo de la personalidad) |
| STS de 12 de septiembre de 2005 (Sala Primera, ponente Sierra Gil de la Cuesta) | Biblioteca Jurídica del BOE, "Comentarios a las sentencias de unificación de doctrina civil y mercantil": https://www.boe.es/biblioteca_juridica/comentarios_sentencias_unificacion_doctrina_civil_y_mercantil/abrir_pdf.php?id=COM-D-2005-1 | "Debe huirse de la aplicación por analogía legis de normas propias del matrimonio en materia de ruptura de la pareja". Admite en cambio la analogía iuris y, por su cauce, el **enriquecimiento injusto**, entendido también como no disminución del patrimonio y como pérdida de expectativas por dedicación al beneficio del otro |
| STS 17/2018, de 15 de enero (Sala Primera, ponente Parra Lucan; Roj STS 37/2018, ECLI:ES:TS:2018:37) | Biblioteca Jurídica del BOE: https://www.boe.es/biblioteca_juridica/comentarios_sentencias_unificacion_doctrina_civil_y_mercantil/abrir_pdf.php?id=COM-D-2018-22 | "No cabe aplicar por analogía legis las normas del matrimonio a los supuestos de ruptura de la convivencia more uxorio o unión de hecho, pero no descarta que pueda recurrirse, **en defecto de pacto**, a principios generales, como el del enriquecimiento injusto". En el caso concreto **rechaza** la compensación por no concurrir sus requisitos |

**Lectura operativa de estas cuatro resoluciones, que sostiene el diseño de la skill:**

1. Nadie queda sometido a un régimen económico por convivir (STC 93/2013). Sin pacto no hay régimen.
2. Las normas del matrimonio no se aplican por analogía legis a la pareja de hecho (STS 2005 y STS 17/2018). El art. 1438 CC no es un derecho del conviviente.
3. Cabe una compensación por la vía del enriquecimiento injusto, **en defecto de pacto**, y solo si se prueban sus requisitos: es una vía de resultado incierto, nunca automática (STS 17/2018 la rechaza en el caso enjuiciado).
4. Por eso el **pacto** es el instrumento central de esta skill: es la única vía que da certeza a los convivientes.

---

## Plantillas: no existe modelo oficial

Verificado el 03/09/2026: no existe modelo normalizado del CGPJ ni formulario estatal de pacto de convivencia o de pacto de ruptura de pareja de hecho, por la sencilla razón de que no hay norma estatal que regule la institución. Los registros autonómicos publican solicitudes de inscripción propias, que no son plantillas de pacto.

Los assets de esta skill no reproducen por tanto ningún modelo oficial: se construyen sobre la autonomía de la voluntad del art. 1255 CC, sobre las reglas de la comunidad de bienes de los arts. 392 y siguientes y sobre los requisitos generales del contrato de los arts. 1261 y siguientes.

| Asset | Base normativa de su estructura |
|---|---|
| `assets/pacto-convivencia.md` | Arts. 1255, 1258, 1261, 1274, 1275, 392 a 400 y 406 CC, más la ley autonómica verificada en el lanzamiento |
| `assets/pacto-ruptura-pareja-hecho.md` | Arts. 1255, 1258, 1261, 1274, 1275, 392 a 406 y 1902 CC, más la ley autonómica verificada en el lanzamiento |
| `assets/checklist-inscripcion-registro.md` | Ley autonómica y registro verificados en el lanzamiento; art. 221 LGSS; arts. 36.2 y 62 TRLRCSCVM |

---

## Verificar manualmente (no resuelto por fuente oficial)

1. **Los requisitos de las 17 leyes autonómicas.** No se registran aquí deliberadamente. Se verifican en cada lanzamiento contra el boletín oficial autonómico y la sede del registro. Cualquier requisito que la skill no haya podido verificar en el lanzamiento debe quedar en el documento como pendiente y advertido al cliente, nunca completado de memoria.
2. **Estado actual de la doctrina del Tribunal Supremo sobre la compensación en la ruptura.** Las dos sentencias registradas arriba (2005 y 2018) están verificadas, pero la jurisprudencia posterior no se ha comprobado en esta sesión. Antes de apoyar una reclamación en ellas, contrastar en el CENDOJ (https://www.poderjudicial.es/search/) si el criterio se mantiene. La skill enuncia el criterio como criterio jurisprudencial, nunca como derecho cierto del cliente.
3. **Aplicación analógica del art. 1438 CC a la pareja de hecho.** Discutida y dependiente del caso. No afirmarla.
4. **Efectos sucesorios y fiscales autonómicos.** Varían por comunidad (derechos sucesorios del conviviente en los derechos civiles forales, reducciones del Impuesto de Sucesiones y Donaciones, tributación de las adjudicaciones en la liquidación). No afirmarlos sin verificar la normativa de la comunidad concreta y, en materia fiscal, derivar a asesoramiento tributario.
5. **Registros municipales.** Algunas comunidades admiten o exigen inscripción municipal, con efectos distintos de los del registro autonómico. Comprobar cuál corresponde al domicilio concreto.
6. **Parejas con elemento internacional o con miembros de distinta vecindad civil.** La ley aplicable puede no ser la de la comunidad de residencia. Escalar.
