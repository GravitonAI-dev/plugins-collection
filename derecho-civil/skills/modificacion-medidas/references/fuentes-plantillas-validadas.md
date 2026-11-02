# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-modificacion-medidas`. Registra las fuentes
> normativas y las plantillas validadas que la skill verifica y, si detecta una versión posterior,
> aplica la redacción vigente al documento que redacta en cada lanzamiento.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa al usuario.

---

## Fuentes normativas (BOE) — verificadas el 31/08/2026 contra la API de legislación consolidada del BOE

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Código Civil (Real Decreto de 24 de julio de 1889, texto consolidado) | BOE-A-1889-4763 | consolidado; art. 90 en redacción Ley 17/2021 (16/12/2021), art. 91 en redacción Ley 17/2021, art. 93 en redacción Ley 11/1990, art. 100 en redacción Ley 15/2015, arts. 101, 142, 146 y 148 en redacción Ley 11/1981, art. 152 en redacción original de 1889 | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado; art. 775 en redacción Ley 8/2021 (vigente desde 03/09/2021), art. 776 en redacción RDL 6/2023 (vigente desde 20/03/2024), art. 770 en redacción RDL 6/2023 (juicio verbal, vigente desde 20/03/2024), art. 264.4.º añadido por LO 1/2025 (vigente desde 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LO 1/2025 de eficiencia del Servicio Público de Justicia (MASC) | BOE-A-2025-76 | 02/01/2025 (requisito de procedibilidad del art. 5 en vigor desde 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |
| LOPJ — Ley Orgánica 6/1985 del Poder Judicial | BOE-A-1985-12666 | art. 89 en redacción de la LO 1/2025 (Secciones de Violencia sobre la Mujer); el antiguo art. 87 ter está SUPRIMIDO | https://www.boe.es/buscar/act.php?id=BOE-A-1985-12666 |
| LO 1/2004 de Medidas de Protección Integral contra la Violencia de Género | BOE-A-2004-21760 | art. 44 (competencia), redacción original vigente | https://www.boe.es/buscar/act.php?id=BOE-A-2004-21760 |
| Ley 15/2015 de la Jurisdicción Voluntaria | BOE-A-2015-7391 | 02/07/2015 (suavizo el art. 90.3 CC y el art. 100 CC; introdujo la modificación por nuevo convenio ante LAJ o notario) | https://www.boe.es/buscar/act.php?id=BOE-A-2015-7391 |

---

## Redacción vigente verificada de los artículos nucleares

### Código Civil

- **Art. 90.3** (redacción Ley 15/2015, con párrafo de animales añadido por Ley 17/2021): *"Las medidas que el juez adopte en defecto de acuerdo o las convenidas por los cónyuges judicialmente, podrán ser modificadas judicialmente o por nuevo convenio aprobado por el juez, cuando así lo aconsejen las nuevas necesidades de los hijos o el cambio de las circunstancias de los cónyuges. Asimismo, podrá modificarse el convenio o solicitarse modificación de las medidas sobre los animales de compañía si se hubieran alterado gravemente sus circunstancias. Las medidas que hubieran sido convenidas ante el letrado de la Administración de Justicia o en escritura pública podrán ser modificadas por un nuevo acuerdo, sujeto a los mismos requisitos exigidos en este Código."*

  **VERIFICADO — matiz relevante:** la Ley 15/2015 SUAVIZO este apartado. La redacción anterior exigía que "se alteren sustancialmente las circunstancias"; la vigente se limita a "las nuevas necesidades de los hijos o el cambio de las circunstancias de los cónyuges". **No obstante, la fórmula estricta sigue viva en el art. 91 in fine CC y en el art. 775.1 LEC**, que es la norma procesal que rige la acción: no se puede afirmar que el requisito de sustancialidad haya desaparecido. La skill enuncia el criterio como "alteración sustancial" por ser el que impone el art. 775.1 LEC, y cita el art. 90.3 CC como base sustantiva.

- **Art. 91 in fine** (redacción Ley 17/2021): tras enumerar las medidas que la sentencia determina en defecto de acuerdo, cierra: *"Estas medidas podrán ser modificadas cuando se alteren sustancialmente las circunstancias."*
- **Art. 93** (párrafo 1.º, Ley 30/1981; párrafo 2.º añadido por Ley 11/1990): el juez determina en todo caso la contribución de cada progenitor a los alimentos y adopta las medidas para asegurar su efectividad y su **acomodación a las circunstancias económicas y necesidades de los hijos en cada momento**. Párrafo 2.º: *"Si convivieran en el domicilio familiar hijos mayores de edad o emancipados que carecieran de ingresos propios, el Juez, en la misma resolución, fijara los alimentos que sean debidos conforme a los artículos 142 y siguientes de este Código."*
- **Art. 100** (redacción Ley 15/2015): *"Fijada la pensión y las bases de su actualización en la sentencia de separación o de divorcio, solo podrá ser modificada por alteraciones en la fortuna de uno u otro cónyuge que así lo aconsejen. La pensión y las bases de actualización fijadas en el convenio regulador formalizado ante el Secretario judicial o Notario podrán modificarse mediante nuevo convenio, sujeto a los mismos requisitos exigidos en este Código."* (La Ley 15/2015 suprimió aquí el adjetivo "sustanciales" que figuraba en la redacción de 1981.)
- **Art. 101** (redacción Ley 30/1981): *"El derecho a la pensión se extingue por el cese de la causa que lo motivo, por contraer el acreedor nuevo matrimonio o por vivir maritalmente con otra persona. El derecho a la pensión no se extingue por el solo hecho de la muerte del deudor. No obstante, los herederos de este podrán solicitar del Juez la reducción o supresión de aquella, si el caudal hereditario no pudiera satisfacer las necesidades de la deuda o afectara a sus derechos en la legítima."*
- **Art. 142**: alimentos = sustento, habitación, vestido y asistencia médica. *"Los alimentos comprenden también la educación e instrucción del alimentista mientras sea menor de edad y aun después cuando no haya terminado su formación por causa que no le sea imputable."*
- **Art. 146**: la cuantía será proporcionada al caudal o medios de quien los da y a las necesidades de quien los recibe.
- **Art. 148** (párrafo 1.º): *"La obligación de dar alimentos será exigible desde que los necesitare, para subsistir, la persona que tenga derecho a percibirlos, pero no se abonaran sino desde la fecha en que se interponga la demanda."* Base legal de la regla de no retroactividad.
- **Art. 152**: cesa la obligación de dar alimentos: **1.º** muerte del alimentista; **2.º** cuando la fortuna del obligado se hubiere reducido hasta el punto de no poder satisfacerlos sin desatender sus propias necesidades y las de su familia; **3.º** *"cuando el alimentista pueda ejercer un oficio, profesión o industria, o haya adquirido un destino o mejorado de fortuna, de suerte que no le sea necesaria la pensión alimenticia para su subsistencia"*; **4.º** cuando el alimentista hubiese cometido alguna falta de las que dan lugar a la desheredación; **5.º** cuando el alimentista sea descendiente del obligado y su necesidad provenga de mala conducta o falta de aplicación al trabajo, mientras subsista esa causa.

### LEC

- **Art. 775 — Modificación de las medidas definitivas** (ap. 1 en redacción Ley 8/2021, vigente desde 03/09/2021):
  - **775.1:** *"El Ministerio Fiscal, habiendo hijos menores o hijos con discapacidad con medidas de apoyo atribuidas a sus progenitores y, en todo caso, los cónyuges, podrán solicitar del Tribunal que acordó las medidas definitivas, la modificación de las medidas convenidas por los cónyuges o de las adoptadas en defecto de acuerdo, siempre que hayan variado sustancialmente las circunstancias tenidas en cuenta al aprobarlas o acordarlas."*
  - **775.2:** *"Estas peticiones se tramitaran conforme a lo dispuesto en el artículo 770. No obstante, si la petición se hiciera por ambos cónyuges de común acuerdo o por uno con el consentimiento del otro y acompañando propuesta de convenio regulador, regirá el procedimiento establecido en el artículo 777."*
  - **775.3:** *"Las partes podrán solicitar, en la demanda o en la contestación, la modificación provisional de las medidas definitivas concedidas en un pleito anterior. Esta petición se sustanciara con arreglo a lo previsto en el artículo 773."*
- **Art. 776 — Ejecución forzosa de los pronunciamientos de medidas** (redacción RDL 6/2023, vigente desde 20/03/2024): 1.ª multas coercitivas por el LAJ al que incumple reiteradamente pagos (art. 711 LEC); 2.ª obligaciones no pecuniarias personalísimas; **3.ª** *"El incumplimiento reiterado de las obligaciones derivadas del régimen de visitas, tanto por parte del progenitor guardador como del no guardador, podrá dar lugar a la modificación por el Tribunal del régimen de guarda y visitas siempre y cuando sea acorde con la evaluación del interés superior del menor realizada previamente."*; 4.ª declaración previa de gasto extraordinario antes del despacho de ejecución.

  **Delimitación:** el art. 776 es EJECUCIÓN, no modificación. El impago de pensiones se reclama por la vía ejecutiva del art. 776, no por esta skill. La única pasarela es la regla 3.ª, que permite pedir la modificación del régimen de guarda y visitas ante incumplimientos reiterados de ese régimen.
- **Art. 770** (redacción RDL 6/2023, vigente desde 20/03/2024): el contencioso de familia se sustancia **por los trámites del juicio verbal** con reglas especiales. Regla **1.ª**: si se solicitan medidas de carácter patrimonial, **ambas partes** deben aportar los documentos que permitan evaluar la situación económica (declaraciones tributarias, nóminas, certificaciones bancarias, títulos de propiedad o certificaciones registrales) y **acreditar, de existir, la resolución judicial o acuerdo en virtud del cual corresponde el uso de la vivienda familiar**. Regla **2.ª**: la **reconvención** se propone con la contestación (el actor dispone de 10 días para contestarla) y solo se admite en cuatro supuestos, entre ellos la letra **d)** *"cuando el cónyuge demandado pretenda la adopción de medidas definitivas, que no hubieran sido solicitadas en la demanda, y sobre las que el tribunal no deba pronunciarse de oficio"* — base del riesgo de reconvención que la skill advierte. Regla **4.ª**: audiencia de los hijos (obligatoria a partir de doce años). Regla **5.ª**: en cualquier momento cabe reconducir al art. 777. Regla **7.ª**: suspensión de común acuerdo para mediación (art. 19.4 LEC).
- **Art. 769** (redacción Ley 15/2015): competencia territorial general en los procesos del capítulo. **769.3:** en los procesos que versen exclusivamente sobre guarda y custodia de hijos menores o sobre alimentos reclamados por un progenitor contra el otro en nombre de los hijos menores, es competente el Juzgado del último domicilio común de los progenitores; si residen en partidos distintos, a elección del demandante, el del domicilio del demandado o el de la residencia del menor. **769.4:** el tribunal examina de oficio su competencia y son nulos los acuerdos de las partes que se opongan a este artículo.

  **Regla aplicable en esta skill:** el art. 775.1 LEC atribuye la petición al **Tribunal que acordó las medidas definitivas**. Es la regla específica y prevalece; el art. 769 se cita como marco general. Si el menor ha trasladado su residencia a otro partido judicial, la competencia puede discutirse: verificar antes de presentar y, en caso de duda, escalar.
- **Art. 264.4.º** (añadido por LO 1/2025, vigente desde 03/04/2025): con la demanda debe presentarse *"el documento que acredite haberse intentado la actividad negociadora previa a la vía judicial cuando la ley exija dicho intento como requisito de procedibilidad, o declaración responsable de la parte de la imposibilidad de llevar a cabo la actividad negociadora previa a la vía judicial por desconocer el domicilio de la parte demandada o el medio por el que puede ser requerido."*
- **Art. 749.2**: intervención preceptiva del Ministerio Fiscal cuando hay menores o personas con discapacidad.
- **Art. 773**: tramitación de las medidas provisionales, a la que remite el art. 775.3 para la modificación provisional.

### LO 1/2025 — requisito de procedibilidad (MASC)

- **Art. 5.1:** en el orden civil, con carácter general, para que la demanda sea admisible es requisito de procedibilidad acudir previamente a un MASC, y **debe existir identidad entre el objeto de la negociación y el objeto del litigio**. Se cumple con mediación, conciliación, opinión neutral de experto independiente, oferta vinculante confidencial, Derecho colaborativo o **actividad negociadora desarrollada directamente por las partes o entre sus abogados bajo sus directrices y con su conformidad**.
- **Art. 5.2:** se exige en todos los procesos declarativos del libro II y en los **procesos especiales del libro IV** de la LEC, con ocho excepciones tasadas: derechos fundamentales; medidas del art. 158 CC; medidas de apoyo a personas con discapacidad; filiación, paternidad y maternidad; tutela sumaria de tenencia o posesión; demolición por ruina; ingreso de menores en centros, entrada en domicilio para ejecución de medidas de protección y restitución en sustracción internacional; juicio cambiario.

  **VERIFICADO:** la modificación de medidas del art. 775 LEC es un proceso especial del libro IV y **NO figura entre las excepciones del art. 5.2**. Por tanto, en la vía contenciosa hay que acreditar el intento de MASC. La excepción práctica es la violencia de género, donde el art. 89.9 LOPJ veda expresamente los MASC.

### LOPJ — art. 89 (redacción LO 1/2025)

- **89.6:** las Secciones de Violencia sobre la Mujer pueden conocer en el orden civil, entre otros, de: **a)** los relativos al matrimonio y a su régimen económico y *"los que tengan por objeto la adopción o modificación de medidas de trascendencia familiar"*; **b)** los que versen exclusivamente sobre guarda y custodia de hijos menores o sobre alimentos reclamados por un progenitor contra el otro en nombre de los hijos menores; **c)** *"los relativos a modificación de medidas adoptadas en los procesos que versen sobre las materias previstas en las letras anteriores"*.
- **89.7:** competencia **exclusiva y excluyente** cuando concurren los cuatro requisitos (materia del ap. 6, víctima de violencia de género o sexual, parte imputada, y actuaciones penales o orden de protección iniciadas).
- **89.9:** *"En todos estos casos está vedada la utilización de los medios adecuados de solución de controversias."*
- El antiguo **art. 87 ter LOPJ fue SUPRIMIDO** por la LO 1/2025 (la consulta a la API del BOE devuelve el bloque solo como histórico). **No citarlo como vigente:** citar art. 89 LOPJ en relación con el art. 44 LO 1/2004.

---

## Requisitos de la alteración sustancial — cautela de citas

La doctrina consolidada exige que el cambio sea **sustancial, sobrevenido, acreditado, no imputable a quien lo alega y con vocación de permanencia**. Esta formulación se enuncia en la skill como **criterio general con base legal en los arts. 775.1 LEC, 90.3 y 91 in fine CC**, NUNCA atribuida a una sentencia concreta. **Prohibido citar resoluciones del Tribunal Supremo o de Audiencias Provinciales sin haberlas verificado en CENDOJ en la misma sesión.** Ver `references/requisitos-alteracion-sustancial.md`.

---

## Herramienta oficial de referencia — Tablas orientadoras del CGPJ (pensión de alimentos)

| Recurso | Detalle |
|---|---|
| Nombre | Tablas orientadoras para determinar las pensiones alimenticias de los hijos en los procesos de familia |
| Organismo | Consejo General del Poder Judicial (CGPJ) |
| URL oficial | https://www.poderjudicial.es/cgpj/es/Servicios/Utilidades/Calculo-de-pensiones-alimenticias/ |
| Estado verificado (31/08/2026) | La página responde pero el apartado consta "en proceso de revisión y actualización" |
| Carácter | Orientador, NO vinculante (arts. 93, 142 y 146 CC) |

La skill cita estas tablas al justificar un nuevo importe de alimentos, siempre como referencia orientadora. En cada lanzamiento, re-verificar la URL.

---

## Plantillas validadas

| Recurso | Detalle |
|---|---|
| Estructura de la demanda de modificación de medidas | Arts. 775.1 y 775.2 LEC en relación con el art. 770 LEC (contenciosa, juicio verbal) o el art. 777 LEC (mutuo acuerdo, con propuesta de nuevo convenio): AL JUZGADO / HECHOS (medidas vigentes, alteración sustancial, MASC) / FUNDAMENTOS DE DERECHO / SUPLICO con la medida nueva concreta / OTROSÍ de prueba y, en su caso, de modificación provisional (art. 775.3 LEC) |
| Estructura de la solicitud de extinción de la pensión de alimentos | Misma estructura procesal (art. 775 LEC) con pretensión de extinción fundada en los arts. 152.3.º y 142 CC y, en su caso, en la pérdida del presupuesto del art. 93.2 CC |
| Requerimiento extrajudicial previo | Bloque condicional: burofax o comunicación fehaciente al otro progenitor, que sirve simultáneamente de intento de MASC (art. 5.1 LO 1/2025, negociación directa) si se documenta como tal |
| Orientación práctica | Guías de los Colegios de la Abogacía y del Ministerio de Justicia sobre procesos de familia |

Los assets `assets/demanda-modificacion-medidas.md` y `assets/solicitud-extincion-pension-alimentos.md` reflejan esta estructura. En cada lanzamiento, la skill re-verifica los artículos citados en el BOE; si detecta una redacción posterior, actualiza el asset y las references afectadas.

---

## Verificación de normativa autonómica

El derecho civil foral (Cataluña, Aragon, Navarra, País Vasco, Baleares, Galicia) puede regular de forma propia la guarda y custodia, los alimentos o la vivienda familiar, y por tanto también su modificación. Si las medidas de origen se dictaron bajo derecho foral, verificar con `web_search` la norma autonómica vigente antes de redactar y advertir al usuario.
