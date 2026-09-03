# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-pareja-de-hecho`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso de verificacion se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Regla especial de la normativa autonomica (NUNCA se da por sabida)

**No existe ley estatal de parejas de hecho ni registro estatal.** La constitucion de la pareja, sus requisitos, el caracter constitutivo o meramente declarativo de la inscripcion y los efectos civiles, sucesorios y fiscales dependen enteramente de la ley de cada comunidad autonoma (17 regulaciones distintas, mas los registros municipales). El Codigo Civil **no** regula la pareja de hecho.

Consecuencia operativa, sin excepciones:

1. La comunidad autonoma es un **vector obligatorio** del arbol de decision en todas las ramas de la skill.
2. La normativa autonomica y su registro **se verifican con `web_search` en CADA lanzamiento**, contra el boletin oficial de la comunidad autonoma o el texto consolidado del BOE de esa ley autonomica y contra la sede electronica del registro. **Esta reference NO almacena los requisitos de las 17 comunidades**: hacerlo invitaria a citarlos de memoria y quedarian obsoletos sin aviso.
3. La fecha de la verificacion se hace constar en el documento generado (`{{fecha_verificacion_normativa_autonomica}}`) junto con la denominacion exacta de la ley y el enlace consultado.
4. **Si la verificacion falla**, la skill lo dice expresamente, no afirma ningun requisito autonomico y marca el punto como pendiente de comprobacion en el propio documento. Prohibido rellenar el hueco con conocimiento previo del modelo.

| Fuente | Que se verifica | Cuando |
|---|---|---|
| Ley autonomica de parejas de hecho / uniones o parejas estables de la comunidad indicada por el usuario | Denominacion exacta y vigencia; requisitos de constitucion (edad, tiempo previo de convivencia, empadronamiento, vecindad civil o administrativa); caracter constitutivo o declarativo de la inscripcion; efectos que la ley atribuye; preceptos anulados por el Tribunal Constitucional | Cada lanzamiento |
| Sede electronica del registro autonomico (y, en su caso, municipal) de parejas de hecho | Denominacion oficial del registro, documentacion exigida, forma de solicitud, tasa y plazos | Cada lanzamiento |

---

## Fuentes normativas estatales (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Codigo Civil | BOE-A-1889-4763 | arts. 1255, 1258, 1261, 1274, 1275 y 1902 en redaccion originaria de 1889; art. 1323 en redaccion de la Ley 13/2005 (vigente 03/07/2005); art. 1438 en redaccion de la Ley 11/1981 (vigente 08/06/1981); arts. 392 a 400 y 406 en redaccion originaria, art. 401 modificado por la Ley 49/1960 y art. 404 por la Ley 17/2021 (vigente 05/01/2022) — verificado 03/09/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| LGSS — Real Decreto Legislativo 8/2015, texto refundido de la Ley General de la Seguridad Social (art. 221, pension de viudedad de la pareja de hecho) | BOE-A-2015-11724 | redaccion de la Ley 21/2021, de 28 de diciembre, vigente desde 01/01/2022 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| TRLRCSCVM — Real Decreto Legislativo 8/2004 (baremo de accidentes de circulacion), arts. 36 y 62, en la redaccion dada por la **Ley 35/2015** | BOE-A-2004-18911 (redaccion: BOE-A-2015-10197) | redaccion de la Ley 35/2015, vigente desde 01/01/2016 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2004-18911 |
| Ley 11/2001, de Uniones de Hecho de la Comunidad de Madrid *(ejemplo de ley autonomica; NO extrapolable a otras comunidades)* | BOE-A-2002-4374 | texto consolidado con ultima actualizacion publicada el 26/12/2024, vigente desde 27/12/2024 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2002-4374 |

**Endpoint de verificacion articulo por articulo (API de legislacion consolidada del BOE).** Devuelve todas las versiones historicas del precepto; la ultima es la vigente. Requiere cabecera `Accept: application/xml`:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{numero_articulo}
```

**Aviso de formato de identificador de bloque:** el Codigo Civil usa `art1255`; la LGSS y el TRLRCSCVM usan `a221` y `a36`. Si un identificador devuelve 404, probar la otra convencion antes de dar la fuente por inaccesible.

---

## Articulos verificados el 03/09/2026

| Precepto | Materia | Redaccion vigente verificada |
|---|---|---|
| CC 1255 | Autonomia de la voluntad | "Los contratantes pueden establecer los pactos, clausulas y condiciones que tengan por conveniente, siempre que no sean contrarios a las leyes, a la moral ni al orden publico." **Es la base juridica del pacto de convivencia y del pacto de ruptura**: no hay norma estatal que regule el contenido economico de la pareja de hecho, y son las partes quienes lo fijan |
| CC 1258 | Perfeccion del contrato | Los contratos se perfeccionan por el mero consentimiento y obligan tambien a las consecuencias conformes a la buena fe, al uso y a la ley |
| CC 1261, 1274 y 1275 | Requisitos del contrato y causa | 1261: consentimiento, objeto cierto y causa. 1274: en los contratos onerosos la causa es la prestacion o promesa de la otra parte; en los remuneratorios, el servicio que se remunera. 1275: los contratos sin causa o con causa ilicita no producen efecto alguno. **Relevante para blindar la compensacion pactada: hay que expresar su causa** |
| CC 1323 | Contratacion entre conyuges | "Los conyuges podran transmitirse por cualquier titulo bienes y derechos y celebrar entre si toda clase de contratos" (Ley 13/2005). **Se refiere solo a conyuges.** Entre convivientes no casados la libertad de contratar no necesita este precepto: deriva directamente del art. 1255. Citarlo como base directa del pacto seria impreciso |
| CC 1438 | Compensacion por trabajo domestico | "Los conyuges contribuiran al sostenimiento de las cargas del matrimonio. A falta de convenio lo haran proporcionalmente a sus respectivos recursos economicos. El trabajo para la casa sera computado como contribucion a las cargas y dara derecho a obtener una compensacion que el Juez senalara, a falta de acuerdo, a la extincion del regimen de separacion" (Ley 11/1981). **Es una norma del REGIMEN DE SEPARACION DE BIENES DEL MATRIMONIO.** Su aplicacion analogica a la pareja de hecho es jurisprudencial y discutida: ver el apartado de jurisprudencia. Prohibido presentarla como derecho automatico del conviviente |
| CC 392 a 406 | Comunidad de bienes | 392: hay comunidad cuando la propiedad pertenece pro indiviso a varias personas; a falta de contratos o disposiciones especiales rige este titulo. 393: el concurso en beneficios y cargas es proporcional a las cuotas, **que se presumen iguales mientras no se pruebe lo contrario**. 394: uso conforme al destino sin perjudicar a los demas. 395: derecho a obligar a contribuir a los gastos de conservacion. 398: acuerdos por mayoria de intereses para la administracion. 399: cada condueno tiene la plena propiedad de su parte y puede enajenarla. 400: nadie esta obligado a permanecer en la comunidad y puede pedir la division en cualquier tiempo; **es valido el pacto de indivision por tiempo determinado no superior a diez anos, prorrogable**. 401: no cabe exigir la division si la cosa resulta inservible. 404: si la cosa es esencialmente indivisible y no hay acuerdo de adjudicacion con indemnizacion, se vende y se reparte el precio (parrafos sobre animales de compania anadidos por la Ley 17/2021). 406: a la division se aplican las reglas de la division de la herencia |
| CC 1902 | Responsabilidad extracontractual | Quien por accion u omision causa dano a otro, interviniendo culpa o negligencia, esta obligado a repararlo. Via residual y de dificil exito en la ruptura de pareja: exige culpa o negligencia y dano acreditado, no basta la ruptura |
| LGSS 221 | Pension de viudedad de la pareja de hecho | Redaccion de la Ley 21/2021 (vigente 01/01/2022). Requisitos acumulativos, **distintos de los del registro autonomico**: (a) cumplir los requisitos del art. 219; (b) pareja constituida con analoga relacion de afectividad a la conyugal, sin impedimento para contraer matrimonio, sin vinculo matrimonial ni otra pareja de hecho; (c) **convivencia estable y notoria acreditada por certificado de empadronamiento, ininterrumpida no inferior a CINCO anos**, salvo que existan hijos en comun, en cuyo caso basta acreditar la constitucion de la pareja; (d) la existencia de la pareja se acredita por **certificacion de inscripcion en un registro autonomico o municipal, o por documento publico**, y tanto la inscripcion como el documento publico deben tener **una antelacion minima de DOS anos** respecto del fallecimiento. El apartado 3 regula el supuesto de pareja ya extinguida en vida (exige ser acreedor de pension compensatoria fijada judicialmente o en convenio o pacto en documento publico), con regla propia para victimas de violencia de genero |
| TRLRCSCVM 36.2 y 62 | Baremo de accidentes de circulacion (Ley 35/2015) | Art. 36.2: "se considera que sufre el mismo perjuicio resarcible que el conyuge viudo el miembro superstite de una pareja de hecho estable constituida mediante inscripcion en un registro o documento publico o que haya convivido un minimo de un ano inmediatamente anterior al fallecimiento o un periodo inferior si tiene un hijo en comun". Art. 62: en caso de muerte hay cinco categorias autonomas de perjudicados, la primera de ellas el conyuge viudo. **Es uno de los pocos ambitos estatales en que la pareja de hecho esta expresamente equiparada, y con requisitos propios mas laxos que los de la viudedad** |

---

## Jurisprudencia verificada en esta sesion (03/09/2026)

Verificada a traves de publicaciones oficiales del BOE. **Ninguna otra sentencia puede citarse sin verificarla en el lanzamiento.**

| Resolucion | Fuente oficial consultada | Criterio verificado |
|---|---|---|
| STC 81/2013, de 11 de abril | Referencia BOE-A-2013-4901, recogida en las notas de vigencia del texto consolidado de la Ley 11/2001 de la Comunidad de Madrid (https://www.boe.es/buscar/act.php?id=BOE-A-2002-4374) | Declara inconstitucionales y nulos los articulos 4 y 5 de la Ley 11/2001 de Uniones de Hecho de la Comunidad de Madrid (pactos de convivencia y su inscripcion), por invadir la competencia estatal en materia de legislacion civil |
| STC 93/2013, de 23 de abril | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2013-5436 | Declara la nulidad de diversos preceptos de la Ley Foral 6/2000 de Navarra. Criterio nuclear: **no puede imponerse a una pareja estable un regimen juridico por el mero hecho de la convivencia, sin una manifestacion de voluntad de someterse a el** (art. 10.1 CE, libre desarrollo de la personalidad) |
| STS de 12 de septiembre de 2005 (Sala Primera, ponente Sierra Gil de la Cuesta) | Biblioteca Juridica del BOE, "Comentarios a las sentencias de unificacion de doctrina civil y mercantil": https://www.boe.es/biblioteca_juridica/comentarios_sentencias_unificacion_doctrina_civil_y_mercantil/abrir_pdf.php?id=COM-D-2005-1 | "Debe huirse de la aplicacion por analogia legis de normas propias del matrimonio en materia de ruptura de la pareja". Admite en cambio la analogia iuris y, por su cauce, el **enriquecimiento injusto**, entendido tambien como no disminucion del patrimonio y como perdida de expectativas por dedicacion al beneficio del otro |
| STS 17/2018, de 15 de enero (Sala Primera, ponente Parra Lucan; Roj STS 37/2018, ECLI:ES:TS:2018:37) | Biblioteca Juridica del BOE: https://www.boe.es/biblioteca_juridica/comentarios_sentencias_unificacion_doctrina_civil_y_mercantil/abrir_pdf.php?id=COM-D-2018-22 | "No cabe aplicar por analogia legis las normas del matrimonio a los supuestos de ruptura de la convivencia more uxorio o union de hecho, pero no descarta que pueda recurrirse, **en defecto de pacto**, a principios generales, como el del enriquecimiento injusto". En el caso concreto **rechaza** la compensacion por no concurrir sus requisitos |

**Lectura operativa de estas cuatro resoluciones, que sostiene el diseno de la skill:**

1. Nadie queda sometido a un regimen economico por convivir (STC 93/2013). Sin pacto no hay regimen.
2. Las normas del matrimonio no se aplican por analogia legis a la pareja de hecho (STS 2005 y STS 17/2018). El art. 1438 CC no es un derecho del conviviente.
3. Cabe una compensacion por la via del enriquecimiento injusto, **en defecto de pacto**, y solo si se prueban sus requisitos: es una via de resultado incierto, nunca automatica (STS 17/2018 la rechaza en el caso enjuiciado).
4. Por eso el **pacto** es el instrumento central de esta skill: es la unica via que da certeza a los convivientes.

---

## Plantillas: no existe modelo oficial

Verificado el 03/09/2026: no existe modelo normalizado del CGPJ ni formulario estatal de pacto de convivencia o de pacto de ruptura de pareja de hecho, por la sencilla razon de que no hay norma estatal que regule la institucion. Los registros autonomicos publican solicitudes de inscripcion propias, que no son plantillas de pacto.

Los assets de esta skill no reproducen por tanto ningun modelo oficial: se construyen sobre la autonomia de la voluntad del art. 1255 CC, sobre las reglas de la comunidad de bienes de los arts. 392 y siguientes y sobre los requisitos generales del contrato de los arts. 1261 y siguientes.

| Asset | Base normativa de su estructura |
|---|---|
| `assets/pacto-convivencia.md` | Arts. 1255, 1258, 1261, 1274, 1275, 392 a 400 y 406 CC, mas la ley autonomica verificada en el lanzamiento |
| `assets/pacto-ruptura-pareja-hecho.md` | Arts. 1255, 1258, 1261, 1274, 1275, 392 a 406 y 1902 CC, mas la ley autonomica verificada en el lanzamiento |
| `assets/checklist-inscripcion-registro.md` | Ley autonomica y registro verificados en el lanzamiento; art. 221 LGSS; arts. 36.2 y 62 TRLRCSCVM |

---

## Verificar manualmente (no resuelto por fuente oficial)

1. **Los requisitos de las 17 leyes autonomicas.** No se registran aqui deliberadamente. Se verifican en cada lanzamiento contra el boletin oficial autonomico y la sede del registro. Cualquier requisito que la skill no haya podido verificar en el lanzamiento debe quedar en el documento como pendiente y advertido al cliente, nunca completado de memoria.
2. **Estado actual de la doctrina del Tribunal Supremo sobre la compensacion en la ruptura.** Las dos sentencias registradas arriba (2005 y 2018) estan verificadas, pero la jurisprudencia posterior no se ha comprobado en esta sesion. Antes de apoyar una reclamacion en ellas, contrastar en el CENDOJ (https://www.poderjudicial.es/search/) si el criterio se mantiene. La skill enuncia el criterio como criterio jurisprudencial, nunca como derecho cierto del cliente.
3. **Aplicacion analogica del art. 1438 CC a la pareja de hecho.** Discutida y dependiente del caso. No afirmarla.
4. **Efectos sucesorios y fiscales autonomicos.** Varian por comunidad (derechos sucesorios del conviviente en los derechos civiles forales, reducciones del Impuesto de Sucesiones y Donaciones, tributacion de las adjudicaciones en la liquidacion). No afirmarlos sin verificar la normativa de la comunidad concreta y, en materia fiscal, derivar a asesoramiento tributario.
5. **Registros municipales.** Algunas comunidades admiten o exigen inscripcion municipal, con efectos distintos de los del registro autonomico. Comprobar cual corresponde al domicilio concreto.
6. **Parejas con elemento internacional o con miembros de distinta vecindad civil.** La ley aplicable puede no ser la de la comunidad de residencia. Escalar.
