# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-ejecucion-titulos`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso de verificacion se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado), Libro III | BOE-A-2000-323 | ultima modificacion aplicada al Libro III: LO 1/2025, efectos 03/04/2025 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LO 1/2025 de eficiencia del Servicio Publico de Justicia | BOE-A-2025-76 | publicada 03/01/2025; art. 5 en vigor 03/04/2025 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |
| TRLC — Real Decreto Legislativo 1/2020, texto refundido de la Ley Concursal | BOE-A-2020-4859 | arts. 142 y 143 en su redaccion originaria, vigencia 01/09/2020 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2020-4859 |
| Real Decreto 126/2026, salario minimo interprofesional para 2026 | BOE-A-2026-3815 | publicado 19/02/2026, efectos desde 01/01/2026 (verificado 31/08/2026) | https://www.boe.es/buscar/doc.php?id=BOE-A-2026-3815 |
| Codigo Penal — Ley Organica 10/1995 (art. 227, impago de pensiones) | BOE-A-1995-25444 | redaccion vigente desde 01/10/2004 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444 |

**Endpoint de verificacion articulo por articulo (API de legislacion consolidada del BOE).** Devuelve todas las versiones historicas del precepto; la ultima es la vigente. Requiere cabecera `Accept: application/xml`:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a{numero_articulo}
```

Ejemplo: `.../bloque/a517` para el art. 517 LEC.

---

## Articulos de la LEC verificados el 31/08/2026 (Libro III)

| Articulos | Materia | Redaccion vigente verificada |
|---|---|---|
| 517 | Titulos que llevan aparejada ejecucion | Modificado por la LO 1/2025 (efectos 03/04/2025) en los numeros 2.º, 4.º, 5.º y 7.º del apartado 2. El 2.º incluye ahora expresamente los acuerdos de mediacion y los alcanzados en cualquier otro MASC, elevados a escritura publica. El 4.º ya no dice "primera copia": dice "la copia de la escritura publica matriz que el interesado solicite que se expida con tal caracter". El 5.º es el testimonio notarial del original de la poliza o su copia autorizada, con la certificacion del art. 572.2 |
| 518 | Caducidad de la accion ejecutiva | CINCO anos desde la firmeza de la sentencia o resolucion. Alcanza a sentencia, resolucion del tribunal o del LAJ que apruebe transaccion o acuerdo, resolucion arbitral y acuerdo de mediacion. Ultima modificacion: LO 7/2015 (nomenclatura). NO modificado por la LO 1/2025 |
| 519 | Ejecucion de consumidores; extension de efectos en condiciones generales | Reformado por el RDL 6/2023, en vigor 20/03/2024. Fuera del alcance de esta skill (proceso propio de extension de efectos) |
| 520 | Titulos no judiciales ni arbitrales: cantidad minima | Solo cabe despachar ejecucion por cantidad determinada que EXCEDA de 300 euros, en dinero efectivo, moneda extranjera convertible o cosa o especie computable en dinero. El limite puede alcanzarse sumando varios titulos. Cuantia en euros desde el RD 1417/2001; texto no modificado despues |
| 524 | Ejecucion provisional: demanda y contenido | Fuera del alcance de esta skill |
| 538 | Partes y sujetos de la ejecucion | Solo cabe despachar ejecucion frente a quien figure como deudor en el titulo; frente a quien responda personalmente por disposicion legal o por afianzamiento acreditado en documento publico; y frente al propietario de bienes especialmente afectos (limitada a esos bienes). El apartado 4 hace responsable de danos y perjuicios al ejecutante que induzca a extender la ejecucion a personas o bienes no autorizados |
| 539 | Postulacion. Costas y gastos de la ejecucion | Modificado por la LO 1/2025 (efectos 03/04/2025). Regla general: abogado y procurador preceptivos para ejecutante y ejecutado, SALVO ejecucion de resoluciones dictadas en procesos en que no lo fueran. Reglas especificas de 2.000 euros: ejecucion derivada de monitorio SIN oposicion, y ejecucion derivada de acuerdo de mediacion o laudo arbitral. Apartado 2: las costas de la ejecucion son a cargo del ejecutado sin necesidad de expresa imposicion, aunque el ejecutante las anticipe hasta su liquidacion |
| 540 a 544 | Sucesion, deudor solidario y otros sujetos | Verificados 540 (sucesion, con documentos fehacientes) y 542 (deudor solidario: los titulos judiciales obtenidos solo frente a algunos no sirven frente a los demas) |
| 545 | Tribunal competente | Titulo judicial u homologado: el tribunal que conocio del asunto en primera instancia o que homologo. Laudo o acuerdo de mediacion: Juzgado de Primera Instancia del lugar donde se dicto el laudo o se firmo el acuerdo. Demas titulos: arts. 50 y 51, o a eleccion del ejecutante el del lugar de cumplimiento o el de donde haya bienes embargables, SIN sumision expresa ni tacita |
| 548 | Plazo de espera | No se despachara ejecucion de resoluciones procesales o arbitrales o de acuerdos de mediacion dentro de los VEINTE DIAS posteriores a aquel en que la resolucion de condena sea firme, o la resolucion de aprobacion del convenio o de firma del acuerdo haya sido notificada al ejecutado. Ultima modificacion: Ley 5/2012. NO modificado por la LO 1/2025 |
| 549 | Demanda ejecutiva: contenido | Apartado 1: titulo; tutela ejecutiva pretendida con la cantidad del art. 575; bienes del ejecutado conocidos y si se estiman suficientes; medidas de localizacion e investigacion del art. 590; personas frente a las que se pide el despacho. Apartado 2: si el titulo es resolucion del LAJ o sentencia del propio tribunal competente para la ejecucion, la demanda puede limitarse a solicitar el despacho identificando la resolucion. Apartados 3 y 4 (desahucio) reformados por el RDL 6/2023, en vigor 20/03/2024 |
| 550 | Documentos que acompanan a la demanda ejecutiva | Modificado por la LO 1/2025 (efectos 03/04/2025). El numero 1.º exige, cuando el titulo sea un acuerdo de mediacion o de otro MASC elevado a escritura publica, acompanar ademas copia de las actas de la sesion constitutiva y final del procedimiento; si es laudo, el convenio arbitral y la acreditacion de su notificacion |
| 551 | Orden general de ejecucion | Modificado por la LO 1/2025 (efectos 03/04/2025). Consulta previa del LAJ al Registro Publico Concursal. El auto debe declarar, en titulos extrajudiciales de contratos con consumidores, que las clausulas que fundan la ejecucion y que determinan la cantidad exigible no son abusivas |
| 552 | Denegacion del despacho. Control de oficio de abusividad | Reformado por el RDL 6/2023, en vigor 20/03/2024. Audiencia de quince dias a las partes; el pronunciamiento sobre abusividad gana efecto de cosa juzgada |
| 556 y 557 | Oposicion a la ejecucion | Posicion de ejecutado; fuera del alcance de esta skill. Plazo de diez dias desde la notificacion del auto de despacho |
| 571 | Ambito de la ejecucion dineraria | Se aplica cuando del titulo resulte, directa o indirectamente, el deber de entregar una cantidad de dinero liquida |
| 572 | Cantidad liquida. Saldo de operaciones | Liquida es toda cantidad determinada expresada en el titulo con letras, cifras o guarismos; prevalece la expresada con letras. No necesita ser liquida la solicitada por intereses de la ejecucion y costas. El apartado 2 admite la ejecucion por saldo si se pacto la liquidacion unilateral en el titulo, y exige acreditar la notificacion previa al ejecutado y al fiador |
| 573 | Documentos de la demanda por saldo de cuenta | Documento del saldo con extracto de cargos, abonos e intereses; documento fehaciente de haberse liquidado en la forma pactada; documento de la notificacion al deudor y al fiador |
| 574 | Intereses variables | Obliga a expresar en la demanda las operaciones de calculo cuando el interes es variable o hay paridades de moneda |
| 575 | Determinacion de la cantidad | Principal + intereses ordinarios y moratorios VENCIDOS + una cantidad provisional para intereses de la ejecucion y costas que NO puede superar el 30 % de lo reclamado, salvo justificacion excepcional. Apartado 1 bis: en ejecucion de vivienda habitual las costas exigibles al ejecutado no pueden superar el 5 % de lo reclamado. Ultima modificacion: Ley 1/2013 |
| 576 | Interes de la mora procesal | Interes legal del dinero incrementado en DOS puntos desde que se dicta la resolucion en primera instancia, o el pactado o el legalmente especial. Aplicable tambien a laudos y acuerdos de mediacion |
| 578 | Vencimiento de nuevos plazos | Permite entender ampliada la ejecucion por los nuevos vencimientos si lo pide el actor. La ampliacion AUTOMATICA puede solicitarse ya en la demanda ejecutiva: el ejecutado sera advertido al notificarle el auto de despacho, y el ejecutante debera presentar liquidacion final. Redaccion originaria de 2000, no modificada |
| 589 | Manifestacion de bienes del ejecutado | Se acuerda de oficio SALVO que el ejecutante senale bienes que estime suficientes. Apercibimiento de desobediencia grave y posibles multas coercitivas. El apartado 3 (advertencia concursal / plan de reestructuracion) procede de la Ley 16/2022 |
| 590 | Investigacion judicial del patrimonio | A instancia del ejecutante que NO pueda designar bienes suficientes. El ejecutante debe indicar las entidades, organismos, registros o personas concretas Y expresar sucintamente las razones por las que estima que disponen de informacion. El LAJ no reclamara datos que el ejecutante o su procurador puedan obtener por si mismos |
| 592 | Orden en los embargos | Criterio preferente: mayor facilidad de enajenacion y menor onerosidad. Solo si eso resulta imposible o muy dificil se aplica la escala de 9 rangos (dinero y cuentas; creditos y valores a corto; joyas y arte; rentas en dinero; intereses, rentas y frutos; muebles, acciones y participaciones; inmuebles; sueldos, salarios y pensiones; creditos y valores a medio y largo plazo) |
| 605 y 606 | Bienes inembargables | 605: animales de compania, bienes declarados inalienables, derechos accesorios no alienables, bienes sin contenido patrimonial y los declarados inembargables por ley. El numero 1.º sobre animales de compania procede de la Ley 17/2021. 606: mobiliario y menaje no superfluo, instrumentos de la profesion desproporcionados a la deuda, bienes sacros, cantidades declaradas inembargables por ley o por tratado |
| 607 | Embargo de sueldos y pensiones | Inembargable lo que no exceda del SMI. Escala por tramos adicionales de SMI: 30 %, 50 %, 60 %, 75 % y 90 %. Acumulacion de percepciones y de las del conyuge salvo separacion de bienes. Rebaja discrecional del LAJ de 10 a 15 puntos por cargas familiares. Se aplica sobre el liquido tras descuentos publicos. Aplicable tambien a ingresos de actividades profesionales y mercantiles autonomas |
| 608 | Ejecucion por condena a prestacion alimenticia | Modificado por la LO 1/2025 (efectos 03/04/2025). El art. 607 NO se aplica cuando se ejecuta condena al pago de alimentos legales, incluidos los pronunciamientos de sentencias de nulidad, separacion o divorcio y los decretos o escrituras publicas que formalicen el convenio regulador. Tampoco se aplica a la pension compensatoria si el ejecutante lo solicita y acredita necesidad economica, previa ponderacion. En estos casos el tribunal fija la cantidad embargable |
| 681 | Ejecucion sobre bienes hipotecados o pignorados | Proceso especial. Fuera del alcance de esta skill |
| 776 | Ejecucion forzosa de los pronunciamientos de medidas (familia) | Reformado por el RDL 6/2023, en vigor 20/03/2024. Se ejecutan con arreglo al Libro III, con cuatro especialidades: 1.ª multas coercitivas del art. 711 por incumplimiento reiterado de pagos, sin perjuicio de hacer efectivas las cantidades debidas; 2.ª obligaciones personalisimas sin sustitucion automatica por equivalente pecuniario; 3.ª el incumplimiento reiterado del regimen de visitas puede motivar la modificacion de guarda y visitas si es acorde con el interes superior del menor; 4.ª los gastos extraordinarios exigen declaracion previa al despacho de ejecucion, con vista a la contraria y, si se opone en cinco dias, comparecencia |
| 816 | Monitorio: incomparecencia del deudor y despacho de la ejecucion | Si el deudor no atiende el requerimiento ni comparece, el LAJ dicta decreto poniendo fin al monitorio y da traslado al acreedor para que inste el despacho de ejecucion, BASTANDO LA MERA SOLICITUD. Despachada, prosigue conforme a la ejecucion de sentencias. Desde el auto de despacho la deuda devenga el interes del art. 576 |
| 264.4.º | Documento del intento de MASC con la demanda | Redaccion de la LO 1/2025 (efectos 03/04/2025). Referido a la demanda y la contestacion de los procesos declarativos |

---

## MASC: NO es requisito de procedibilidad de la demanda ejecutiva

Verificado el 31/08/2026 en el texto consolidado de la LO 1/2025 (BOE-A-2025-76), **articulo 5.3**, literal:

> "No sera preciso acudir a un medio adecuado de solucion de controversias para la interposicion de una demanda ejecutiva, la solicitud de medidas cautelares previas a la demanda, la solicitud de diligencias preliminares ni para la iniciacion de expedientes de jurisdiccion voluntaria [...]"

Consecuencia operativa: esta skill **no genera burofax previo ni exige acreditar intento de negociacion**, a diferencia de `derecho-civil-reclamacion-cantidad`. El art. 5.2 de la misma ley circunscribe el requisito a los procesos declarativos del Libro II y a los especiales del Libro IV.

---

## Plantillas: no existe modelo normalizado del CGPJ para la ejecucion

Verificado el 31/08/2026 en https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/ : los modelos normalizados publicados son los de juicio verbal, proceso monitorio, monitorio de propiedad horizontal, jurisdiccion voluntaria (conciliacion), asistencia juridica gratuita, denuncia, juicio por delito leve y juicio rapido. **No hay modelo normalizado de demanda ejecutiva ni de ejecucion de titulos judiciales.**

Por tanto los assets de esta skill no reproducen un modelo oficial: se construyen sobre el contenido legalmente exigido por los articulos 549, 550, 572 a 575 y 590 de la LEC y sobre las guias de estilo de redaccion judicial (ver `references/estilo-redaccion-escritos.md`).

| Asset | Base normativa de su estructura |
|---|---|
| `assets/demanda-ejecucion-titulo-judicial.md` | Arts. 517.2.1.º y 3.º, 518, 545.1, 548, 549, 550, 575, 576, 589, 590, 592 y 776 LEC |
| `assets/demanda-ejecucion-titulo-no-judicial.md` | Arts. 517.2.2.º y 4.º a 7.º, 520, 545.2 y 3, 549, 550, 551.2.5.º, 572 a 575 LEC |
| `assets/solicitud-embargo-averiguacion-patrimonial.md` | Arts. 589, 590, 592, 605 a 608 y 578 LEC |

---

## Verificar manualmente (no resuelto por fuente oficial)

1. **Plazo de espera del art. 548 en ejecucion de pensiones de familia.** La LEC no exceptua las resoluciones de familia del plazo de veinte dias: la unica excepcion expresa es la del art. 549.4 para los desahucios. Existe jurisprudencia menor de Audiencias Provinciales que considera inaplicable el "plazo de cortesia" a las mensualidades de alimentos ya vencidas e impagadas, pero no es doctrina uniforme ni consta en el texto legal. **Posicion conservadora de la skill: computar los veinte dias desde la firmeza de la resolucion o desde la notificacion de la aprobacion del convenio.** En la practica, tratandose de pensiones periodicas de una resolucion firme desde hace meses, el plazo ya esta agotado. Verificar el criterio del juzgado antes de presentar si la resolucion es reciente.
2. **Redaccion literal de los articulos en un escrito.** La API del BOE devuelve la version consolidada vigente, que es la fuente utilizada aqui. Antes de transcribir literalmente un precepto en un escrito que se presente, contrastarlo de nuevo en el BOE.
3. **Tramos concretos del art. 607 en euros.** La escala se expresa en multiplos del SMI, no en importes fijos: cualquier calculo en euros depende del SMI del ano en curso (para 2026, RD 126/2026). Re-verificar el SMI en cada ejercicio antes de calcular una retencion.
4. **Interes legal del dinero del ejercicio en curso.** Se fija cada ano en la Ley de Presupuestos Generales del Estado. La skill no lo registra: debe consultarse en el momento de liquidar los intereses del art. 576.
