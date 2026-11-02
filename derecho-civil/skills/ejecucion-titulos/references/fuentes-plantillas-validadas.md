# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-ejecucion-titulos`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica en cada lanzamiento para aplicar la redacción vigente al documento que redacta.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado), Libro III | BOE-A-2000-323 | última modificación aplicada al Libro III: LO 1/2025, efectos 03/04/2025 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LO 1/2025 de eficiencia del Servicio Público de Justicia | BOE-A-2025-76 | publicada 03/01/2025; art. 5 en vigor 03/04/2025 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |
| TRLC — Real Decreto Legislativo 1/2020, texto refundido de la Ley Concursal | BOE-A-2020-4859 | arts. 142 y 143 en su redacción originaria, vigencia 01/09/2020 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2020-4859 |
| Real Decreto 126/2026, salario mínimo interprofesional para 2026 | BOE-A-2026-3815 | publicado 19/02/2026, efectos desde 01/01/2026 (verificado 31/08/2026) | https://www.boe.es/buscar/doc.php?id=BOE-A-2026-3815 |
| Código Penal — Ley Orgánica 10/1995 (art. 227, impago de pensiones) | BOE-A-1995-25444 | redacción vigente desde 01/10/2004 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444 |

**Endpoint de verificación artículo por artículo (API de legislación consolidada del BOE).** Devuelve todas las versiones históricas del precepto; la última es la vigente. Requiere cabecera `Accept: application/xml`:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a{numero_articulo}
```

Ejemplo: `.../bloque/a517` para el art. 517 LEC.

---

## Artículos de la LEC verificados el 31/08/2026 (Libro III)

| Artículos | Materia | Redacción vigente verificada |
|---|---|---|
| 517 | Títulos que llevan aparejada ejecución | Modificado por la LO 1/2025 (efectos 03/04/2025) en los números 2.º, 4.º, 5.º y 7.º del apartado 2. El 2.º incluye ahora expresamente los acuerdos de mediación y los alcanzados en cualquier otro MASC, elevados a escritura pública. El 4.º ya no dice "primera copia": dice "la copia de la escritura pública matriz que el interesado solicite que se expida con tal carácter". El 5.º es el testimonio notarial del original de la póliza o su copia autorizada, con la certificación del art. 572.2 |
| 518 | Caducidad de la acción ejecutiva | CINCO años desde la firmeza de la sentencia o resolución. Alcanza a sentencia, resolución del tribunal o del LAJ que apruebe transacción o acuerdo, resolución arbitral y acuerdo de mediación. Última modificación: LO 7/2015 (nomenclatura). NO modificado por la LO 1/2025 |
| 519 | Ejecución de consumidores; extensión de efectos en condiciones generales | Reformado por el RDL 6/2023, en vigor 20/03/2024. Fuera del alcance de esta skill (proceso propio de extensión de efectos) |
| 520 | Títulos no judiciales ni arbitrales: cantidad mínima | Solo cabe despachar ejecución por cantidad determinada que EXCEDA de 300 euros, en dinero efectivo, moneda extranjera convertible o cosa o especie computable en dinero. El límite puede alcanzarse sumando varios títulos. Cuantía en euros desde el RD 1417/2001; texto no modificado después |
| 524 | Ejecución provisional: demanda y contenido | Fuera del alcance de esta skill |
| 538 | Partes y sujetos de la ejecución | Solo cabe despachar ejecución frente a quien figure como deudor en el título; frente a quien responda personalmente por disposición legal o por afianzamiento acreditado en documento público; y frente al propietario de bienes especialmente afectos (limitada a esos bienes). El apartado 4 hace responsable de daños y perjuicios al ejecutante que induzca a extender la ejecución a personas o bienes no autorizados |
| 539 | Postulación. Costas y gastos de la ejecución | Modificado por la LO 1/2025 (efectos 03/04/2025). Regla general: abogado y procurador preceptivos para ejecutante y ejecutado, SALVO ejecución de resoluciones dictadas en procesos en que no lo fueran. Reglas específicas de 2.000 euros: ejecución derivada de monitorio SIN oposición, y ejecución derivada de acuerdo de mediación o laudo arbitral. Apartado 2: las costas de la ejecución son a cargo del ejecutado sin necesidad de expresa imposición, aunque el ejecutante las anticipe hasta su liquidación |
| 540 a 544 | Sucesión, deudor solidario y otros sujetos | Verificados 540 (sucesión, con documentos fehacientes) y 542 (deudor solidario: los títulos judiciales obtenidos solo frente a algunos no sirven frente a los demás) |
| 545 | Tribunal competente | Título judicial u homologado: el tribunal que conoció del asunto en primera instancia o que homologo. Laudo o acuerdo de mediación: Juzgado de Primera Instancia del lugar donde se dictó el laudo o se firmo el acuerdo. Demás títulos: arts. 50 y 51, o a elección del ejecutante el del lugar de cumplimiento o el de donde haya bienes embargables, SIN sumisión expresa ni tácita |
| 548 | Plazo de espera | No se despachara ejecución de resoluciones procesales o arbitrales o de acuerdos de mediación dentro de los VEINTE DÍAS posteriores a aquel en que la resolución de condena sea firme, o la resolución de aprobación del convenio o de firma del acuerdo haya sido notificada al ejecutado. Última modificación: Ley 5/2012. NO modificado por la LO 1/2025 |
| 549 | Demanda ejecutiva: contenido | Apartado 1: título; tutela ejecutiva pretendida con la cantidad del art. 575; bienes del ejecutado conocidos y si se estiman suficientes; medidas de localización e investigación del art. 590; personas frente a las que se pide el despacho. Apartado 2: si el título es resolución del LAJ o sentencia del propio tribunal competente para la ejecución, la demanda puede limitarse a solicitar el despacho identificando la resolución. Apartados 3 y 4 (desahucio) reformados por el RDL 6/2023, en vigor 20/03/2024 |
| 550 | Documentos que acompañan a la demanda ejecutiva | Modificado por la LO 1/2025 (efectos 03/04/2025). El número 1.º exige, cuando el título sea un acuerdo de mediación o de otro MASC elevado a escritura pública, acompañar además copia de las actas de la sesión constitutiva y final del procedimiento; si es laudo, el convenio arbitral y la acreditación de su notificación |
| 551 | Orden general de ejecución | Modificado por la LO 1/2025 (efectos 03/04/2025). Consulta previa del LAJ al Registro Público Concursal. El auto debe declarar, en títulos extrajudiciales de contratos con consumidores, que las cláusulas que fundan la ejecución y que determinan la cantidad exigible no son abusivas |
| 552 | Denegación del despacho. Control de oficio de abusividad | Reformado por el RDL 6/2023, en vigor 20/03/2024. Audiencia de quince días a las partes; el pronunciamiento sobre abusividad gana efecto de cosa juzgada |
| 556 y 557 | Oposición a la ejecución | Posición de ejecutado; fuera del alcance de esta skill. Plazo de diez días desde la notificación del auto de despacho |
| 571 | Ámbito de la ejecución dineraria | Se aplica cuando del título resulte, directa o indirectamente, el deber de entregar una cantidad de dinero líquida |
| 572 | Cantidad líquida. Saldo de operaciones | Líquida es toda cantidad determinada expresada en el título con letras, cifras o guarismos; prevalece la expresada con letras. No necesita ser líquida la solicitada por intereses de la ejecución y costas. El apartado 2 admite la ejecución por saldo si se pacto la liquidación unilateral en el título, y exige acreditar la notificación previa al ejecutado y al fiador |
| 573 | Documentos de la demanda por saldo de cuenta | Documento del saldo con extracto de cargos, abonos e intereses; documento fehaciente de haberse liquidado en la forma pactada; documento de la notificación al deudor y al fiador |
| 574 | Intereses variables | Obliga a expresar en la demanda las operaciones de cálculo cuando el interés es variable o hay paridades de moneda |
| 575 | Determinación de la cantidad | Principal + intereses ordinarios y moratorios VENCIDOS + una cantidad provisional para intereses de la ejecución y costas que NO puede superar el 30 % de lo reclamado, salvo justificación excepcional. Apartado 1 bis: en ejecución de vivienda habitual las costas exigibles al ejecutado no pueden superar el 5 % de lo reclamado. Última modificación: Ley 1/2013 |
| 576 | Interés de la mora procesal | Interés legal del dinero incrementado en DOS puntos desde que se dicta la resolución en primera instancia, o el pactado o el legalmente especial. Aplicable también a laudos y acuerdos de mediación |
| 578 | Vencimiento de nuevos plazos | Permite entender ampliada la ejecución por los nuevos vencimientos si lo pide el actor. La ampliación AUTOMÁTICA puede solicitarse ya en la demanda ejecutiva: el ejecutado será advertido al notificarle el auto de despacho, y el ejecutante deberá presentar liquidación final. Redacción originaria de 2000, no modificada |
| 589 | Manifestación de bienes del ejecutado | Se acuerda de oficio SALVO que el ejecutante señale bienes que estime suficientes. Apercibimiento de desobediencia grave y posibles multas coercitivas. El apartado 3 (advertencia concursal / plan de reestructuración) procede de la Ley 16/2022 |
| 590 | Investigación judicial del patrimonio | A instancia del ejecutante que NO pueda designar bienes suficientes. El ejecutante debe indicar las entidades, organismos, registros o personas concretas Y expresar sucintamente las razones por las que estima que disponen de información. El LAJ no reclamará datos que el ejecutante o su procurador puedan obtener por sí mismos |
| 592 | Orden en los embargos | Criterio preferente: mayor facilidad de enajenación y menor onerosidad. Solo si eso resulta imposible o muy difícil se aplica la escala de 9 rangos (dinero y cuentas; créditos y valores a corto; joyas y arte; rentas en dinero; intereses, rentas y frutos; muebles, acciones y participaciones; inmuebles; sueldos, salarios y pensiones; créditos y valores a medio y largo plazo) |
| 605 y 606 | Bienes inembargables | 605: animales de compañía, bienes declarados inalienables, derechos accesorios no alienables, bienes sin contenido patrimonial y los declarados inembargables por ley. El número 1.º sobre animales de compañía procede de la Ley 17/2021. 606: mobiliario y menaje no superfluo, instrumentos de la profesión desproporcionados a la deuda, bienes sacros, cantidades declaradas inembargables por ley o por tratado |
| 607 | Embargo de sueldos y pensiones | Inembargable lo que no exceda del SMI. Escala por tramos adicionales de SMI: 30 %, 50 %, 60 %, 75 % y 90 %. Acumulación de percepciones y de las del cónyuge salvo separación de bienes. Rebaja discrecional del LAJ de 10 a 15 puntos por cargas familiares. Se aplica sobre el líquido tras descuentos públicos. Aplicable también a ingresos de actividades profesionales y mercantiles autónomas |
| 608 | Ejecución por condena a prestación alimenticia | Modificado por la LO 1/2025 (efectos 03/04/2025). El art. 607 NO se aplica cuando se ejecuta condena al pago de alimentos legales, incluidos los pronunciamientos de sentencias de nulidad, separación o divorcio y los decretos o escrituras públicas que formalicen el convenio regulador. Tampoco se aplica a la pensión compensatoria si el ejecutante lo solicita y acredita necesidad económica, previa ponderación. En estos casos el tribunal fija la cantidad embargable |
| 681 | Ejecución sobre bienes hipotecados o pignorados | Proceso especial. Fuera del alcance de esta skill |
| 776 | Ejecución forzosa de los pronunciamientos de medidas (familia) | Reformado por el RDL 6/2023, en vigor 20/03/2024. Se ejecutan con arreglo al Libro III, con cuatro especialidades: 1.ª multas coercitivas del art. 711 por incumplimiento reiterado de pagos, sin perjuicio de hacer efectivas las cantidades debidas; 2.ª obligaciones personalísimas sin sustitución automática por equivalente pecuniario; 3.ª el incumplimiento reiterado del régimen de visitas puede motivar la modificación de guarda y visitas si es acorde con el interés superior del menor; 4.ª los gastos extraordinarios exigen declaración previa al despacho de ejecución, con vista a la contraria y, si se opone en cinco días, comparecencia |
| 816 | Monitorio: incomparecencia del deudor y despacho de la ejecución | Si el deudor no atiende el requerimiento ni comparece, el LAJ dicta decreto poniendo fin al monitorio y da traslado al acreedor para que inste el despacho de ejecución, BASTANDO LA MERA SOLICITUD. Despachada, prosigue conforme a la ejecución de sentencias. Desde el auto de despacho la deuda devenga el interés del art. 576 |
| 264.4.º | Documento del intento de MASC con la demanda | Redacción de la LO 1/2025 (efectos 03/04/2025). Referido a la demanda y la contestación de los procesos declarativos |

---

## MASC: NO es requisito de procedibilidad de la demanda ejecutiva

Verificado el 31/08/2026 en el texto consolidado de la LO 1/2025 (BOE-A-2025-76), **artículo 5.3**, literal:

> "No será preciso acudir a un medio adecuado de solución de controversias para la interposición de una demanda ejecutiva, la solicitud de medidas cautelares previas a la demanda, la solicitud de diligencias preliminares ni para la iniciación de expedientes de jurisdicción voluntaria [...]"

Consecuencia operativa: esta skill **no genera burofax previo ni exige acreditar intento de negociación**, a diferencia de `derecho-civil-reclamacion-cantidad`. El art. 5.2 de la misma ley circunscribe el requisito a los procesos declarativos del Libro II y a los especiales del Libro IV.

---

## Plantillas: no existe modelo normalizado del CGPJ para la ejecución

Verificado el 31/08/2026 en https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/ : los modelos normalizados publicados son los de juicio verbal, proceso monitorio, monitorio de propiedad horizontal, jurisdicción voluntaria (conciliación), asistencia jurídica gratuita, denuncia, juicio por delito leve y juicio rápido. **No hay modelo normalizado de demanda ejecutiva ni de ejecución de títulos judiciales.**

Por tanto los assets de esta skill no reproducen un modelo oficial: se construyen sobre el contenido legalmente exigido por los artículos 549, 550, 572 a 575 y 590 de la LEC y sobre las guías de estilo de redacción judicial (ver `references/estilo-redaccion-escritos.md`).

| Asset | Base normativa de su estructura |
|---|---|
| `assets/demanda-ejecucion-titulo-judicial.md` | Arts. 517.2.1.º y 3.º, 518, 545.1, 548, 549, 550, 575, 576, 589, 590, 592 y 776 LEC |
| `assets/demanda-ejecucion-titulo-no-judicial.md` | Arts. 517.2.2.º y 4.º a 7.º, 520, 545.2 y 3, 549, 550, 551.2.5.º, 572 a 575 LEC |
| `assets/solicitud-embargo-averiguacion-patrimonial.md` | Arts. 589, 590, 592, 605 a 608 y 578 LEC |

---

## Verificar manualmente (no resuelto por fuente oficial)

1. **Plazo de espera del art. 548 en ejecución de pensiones de familia.** La LEC no exceptúa las resoluciones de familia del plazo de veinte días: la única excepción expresa es la del art. 549.4 para los desahucios. Existe jurisprudencia menor de Audiencias Provinciales que considera inaplicable el "plazo de cortesía" a las mensualidades de alimentos ya vencidas e impagadas, pero no es doctrina uniforme ni consta en el texto legal. **Posición conservadora de la skill: computar los veinte días desde la firmeza de la resolución o desde la notificación de la aprobación del convenio.** En la práctica, tratándose de pensiones periódicas de una resolución firme desde hace meses, el plazo ya está agotado. Verificar el criterio del juzgado antes de presentar si la resolución es reciente.
2. **Redacción literal de los artículos en un escrito.** La API del BOE devuelve la versión consolidada vigente, que es la fuente utilizada aquí. Antes de transcribir literalmente un precepto en un escrito que se presente, contrastarlo de nuevo en el BOE.
3. **Tramos concretos del art. 607 en euros.** La escala se expresa en múltiplos del SMI, no en importes fijos: cualquier cálculo en euros depende del SMI del año en curso (para 2026, RD 126/2026). Re-verificar el SMI en cada ejercicio antes de calcular una retención.
4. **Interés legal del dinero del ejercicio en curso.** Se fija cada año en la Ley de Presupuestos Generales del Estado. La skill no lo registra: debe consultarse en el momento de liquidar los intereses del art. 576.
