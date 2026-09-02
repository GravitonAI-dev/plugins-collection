# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-modificacion-medidas`. Registra las fuentes
> normativas y las plantillas validadas que la skill verifica y, si detecta una version posterior,
> ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Punto 2 se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE) — verificadas el 31/08/2026 contra la API de legislacion consolidada del BOE

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Codigo Civil (Real Decreto de 24 de julio de 1889, texto consolidado) | BOE-A-1889-4763 | consolidado; art. 90 en redaccion Ley 17/2021 (16/12/2021), art. 91 en redaccion Ley 17/2021, art. 93 en redaccion Ley 11/1990, art. 100 en redaccion Ley 15/2015, arts. 101, 142, 146 y 148 en redaccion Ley 11/1981, art. 152 en redaccion original de 1889 | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado; art. 775 en redaccion Ley 8/2021 (vigente desde 03/09/2021), art. 776 en redaccion RDL 6/2023 (vigente desde 20/03/2024), art. 770 en redaccion RDL 6/2023 (juicio verbal, vigente desde 20/03/2024), art. 264.4.º anadido por LO 1/2025 (vigente desde 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LO 1/2025 de eficiencia del Servicio Publico de Justicia (MASC) | BOE-A-2025-76 | 02/01/2025 (requisito de procedibilidad del art. 5 en vigor desde 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |
| LOPJ — Ley Organica 6/1985 del Poder Judicial | BOE-A-1985-12666 | art. 89 en redaccion de la LO 1/2025 (Secciones de Violencia sobre la Mujer); el antiguo art. 87 ter esta SUPRIMIDO | https://www.boe.es/buscar/act.php?id=BOE-A-1985-12666 |
| LO 1/2004 de Medidas de Proteccion Integral contra la Violencia de Genero | BOE-A-2004-21760 | art. 44 (competencia), redaccion original vigente | https://www.boe.es/buscar/act.php?id=BOE-A-2004-21760 |
| Ley 15/2015 de la Jurisdiccion Voluntaria | BOE-A-2015-7391 | 02/07/2015 (suavizo el art. 90.3 CC y el art. 100 CC; introdujo la modificacion por nuevo convenio ante LAJ o notario) | https://www.boe.es/buscar/act.php?id=BOE-A-2015-7391 |

---

## Redaccion vigente verificada de los articulos nucleares

### Codigo Civil

- **Art. 90.3** (redaccion Ley 15/2015, con parrafo de animales anadido por Ley 17/2021): *"Las medidas que el juez adopte en defecto de acuerdo o las convenidas por los conyuges judicialmente, podran ser modificadas judicialmente o por nuevo convenio aprobado por el juez, cuando asi lo aconsejen las nuevas necesidades de los hijos o el cambio de las circunstancias de los conyuges. Asimismo, podra modificarse el convenio o solicitarse modificacion de las medidas sobre los animales de compania si se hubieran alterado gravemente sus circunstancias. Las medidas que hubieran sido convenidas ante el letrado de la Administracion de Justicia o en escritura publica podran ser modificadas por un nuevo acuerdo, sujeto a los mismos requisitos exigidos en este Codigo."*

  **VERIFICADO — matiz relevante:** la Ley 15/2015 SUAVIZO este apartado. La redaccion anterior exigia que "se alteren sustancialmente las circunstancias"; la vigente se limita a "las nuevas necesidades de los hijos o el cambio de las circunstancias de los conyuges". **No obstante, la formula estricta sigue viva en el art. 91 in fine CC y en el art. 775.1 LEC**, que es la norma procesal que rige la accion: no se puede afirmar que el requisito de sustancialidad haya desaparecido. La skill enuncia el criterio como "alteracion sustancial" por ser el que impone el art. 775.1 LEC, y cita el art. 90.3 CC como base sustantiva.

- **Art. 91 in fine** (redaccion Ley 17/2021): tras enumerar las medidas que la sentencia determina en defecto de acuerdo, cierra: *"Estas medidas podran ser modificadas cuando se alteren sustancialmente las circunstancias."*
- **Art. 93** (parrafo 1.º, Ley 30/1981; parrafo 2.º anadido por Ley 11/1990): el juez determina en todo caso la contribucion de cada progenitor a los alimentos y adopta las medidas para asegurar su efectividad y su **acomodacion a las circunstancias economicas y necesidades de los hijos en cada momento**. Parrafo 2.º: *"Si convivieran en el domicilio familiar hijos mayores de edad o emancipados que carecieran de ingresos propios, el Juez, en la misma resolucion, fijara los alimentos que sean debidos conforme a los articulos 142 y siguientes de este Codigo."*
- **Art. 100** (redaccion Ley 15/2015): *"Fijada la pension y las bases de su actualizacion en la sentencia de separacion o de divorcio, solo podra ser modificada por alteraciones en la fortuna de uno u otro conyuge que asi lo aconsejen. La pension y las bases de actualizacion fijadas en el convenio regulador formalizado ante el Secretario judicial o Notario podran modificarse mediante nuevo convenio, sujeto a los mismos requisitos exigidos en este Codigo."* (La Ley 15/2015 suprimio aqui el adjetivo "sustanciales" que figuraba en la redaccion de 1981.)
- **Art. 101** (redaccion Ley 30/1981): *"El derecho a la pension se extingue por el cese de la causa que lo motivo, por contraer el acreedor nuevo matrimonio o por vivir maritalmente con otra persona. El derecho a la pension no se extingue por el solo hecho de la muerte del deudor. No obstante, los herederos de este podran solicitar del Juez la reduccion o supresion de aquella, si el caudal hereditario no pudiera satisfacer las necesidades de la deuda o afectara a sus derechos en la legitima."*
- **Art. 142**: alimentos = sustento, habitacion, vestido y asistencia medica. *"Los alimentos comprenden tambien la educacion e instruccion del alimentista mientras sea menor de edad y aun despues cuando no haya terminado su formacion por causa que no le sea imputable."*
- **Art. 146**: la cuantia sera proporcionada al caudal o medios de quien los da y a las necesidades de quien los recibe.
- **Art. 148** (parrafo 1.º): *"La obligacion de dar alimentos sera exigible desde que los necesitare, para subsistir, la persona que tenga derecho a percibirlos, pero no se abonaran sino desde la fecha en que se interponga la demanda."* Base legal de la regla de no retroactividad.
- **Art. 152**: cesa la obligacion de dar alimentos: **1.º** muerte del alimentista; **2.º** cuando la fortuna del obligado se hubiere reducido hasta el punto de no poder satisfacerlos sin desatender sus propias necesidades y las de su familia; **3.º** *"cuando el alimentista pueda ejercer un oficio, profesion o industria, o haya adquirido un destino o mejorado de fortuna, de suerte que no le sea necesaria la pension alimenticia para su subsistencia"*; **4.º** cuando el alimentista hubiese cometido alguna falta de las que dan lugar a la desheredacion; **5.º** cuando el alimentista sea descendiente del obligado y su necesidad provenga de mala conducta o falta de aplicacion al trabajo, mientras subsista esa causa.

### LEC

- **Art. 775 — Modificacion de las medidas definitivas** (ap. 1 en redaccion Ley 8/2021, vigente desde 03/09/2021):
  - **775.1:** *"El Ministerio Fiscal, habiendo hijos menores o hijos con discapacidad con medidas de apoyo atribuidas a sus progenitores y, en todo caso, los conyuges, podran solicitar del Tribunal que acordo las medidas definitivas, la modificacion de las medidas convenidas por los conyuges o de las adoptadas en defecto de acuerdo, siempre que hayan variado sustancialmente las circunstancias tenidas en cuenta al aprobarlas o acordarlas."*
  - **775.2:** *"Estas peticiones se tramitaran conforme a lo dispuesto en el articulo 770. No obstante, si la peticion se hiciera por ambos conyuges de comun acuerdo o por uno con el consentimiento del otro y acompanando propuesta de convenio regulador, regira el procedimiento establecido en el articulo 777."*
  - **775.3:** *"Las partes podran solicitar, en la demanda o en la contestacion, la modificacion provisional de las medidas definitivas concedidas en un pleito anterior. Esta peticion se sustanciara con arreglo a lo previsto en el articulo 773."*
- **Art. 776 — Ejecucion forzosa de los pronunciamientos de medidas** (redaccion RDL 6/2023, vigente desde 20/03/2024): 1.ª multas coercitivas por el LAJ al que incumple reiteradamente pagos (art. 711 LEC); 2.ª obligaciones no pecuniarias personalisimas; **3.ª** *"El incumplimiento reiterado de las obligaciones derivadas del regimen de visitas, tanto por parte del progenitor guardador como del no guardador, podra dar lugar a la modificacion por el Tribunal del regimen de guarda y visitas siempre y cuando sea acorde con la evaluacion del interes superior del menor realizada previamente."*; 4.ª declaracion previa de gasto extraordinario antes del despacho de ejecucion.

  **Delimitacion:** el art. 776 es EJECUCION, no modificacion. El impago de pensiones se reclama por la via ejecutiva del art. 776, no por esta skill. La unica pasarela es la regla 3.ª, que permite pedir la modificacion del regimen de guarda y visitas ante incumplimientos reiterados de ese regimen.
- **Art. 770** (redaccion RDL 6/2023, vigente desde 20/03/2024): el contencioso de familia se sustancia **por los tramites del juicio verbal** con reglas especiales. Regla **1.ª**: si se solicitan medidas de caracter patrimonial, **ambas partes** deben aportar los documentos que permitan evaluar la situacion economica (declaraciones tributarias, nominas, certificaciones bancarias, titulos de propiedad o certificaciones registrales) y **acreditar, de existir, la resolucion judicial o acuerdo en virtud del cual corresponde el uso de la vivienda familiar**. Regla **2.ª**: la **reconvencion** se propone con la contestacion (el actor dispone de 10 dias para contestarla) y solo se admite en cuatro supuestos, entre ellos la letra **d)** *"cuando el conyuge demandado pretenda la adopcion de medidas definitivas, que no hubieran sido solicitadas en la demanda, y sobre las que el tribunal no deba pronunciarse de oficio"* — base del riesgo de reconvencion que la skill advierte. Regla **4.ª**: audiencia de los hijos (obligatoria a partir de doce anos). Regla **5.ª**: en cualquier momento cabe reconducir al art. 777. Regla **7.ª**: suspension de comun acuerdo para mediacion (art. 19.4 LEC).
- **Art. 769** (redaccion Ley 15/2015): competencia territorial general en los procesos del capitulo. **769.3:** en los procesos que versen exclusivamente sobre guarda y custodia de hijos menores o sobre alimentos reclamados por un progenitor contra el otro en nombre de los hijos menores, es competente el Juzgado del ultimo domicilio comun de los progenitores; si residen en partidos distintos, a eleccion del demandante, el del domicilio del demandado o el de la residencia del menor. **769.4:** el tribunal examina de oficio su competencia y son nulos los acuerdos de las partes que se opongan a este articulo.

  **Regla aplicable en esta skill:** el art. 775.1 LEC atribuye la peticion al **Tribunal que acordo las medidas definitivas**. Es la regla especifica y prevalece; el art. 769 se cita como marco general. Si el menor ha trasladado su residencia a otro partido judicial, la competencia puede discutirse: verificar antes de presentar y, en caso de duda, escalar.
- **Art. 264.4.º** (anadido por LO 1/2025, vigente desde 03/04/2025): con la demanda debe presentarse *"el documento que acredite haberse intentado la actividad negociadora previa a la via judicial cuando la ley exija dicho intento como requisito de procedibilidad, o declaracion responsable de la parte de la imposibilidad de llevar a cabo la actividad negociadora previa a la via judicial por desconocer el domicilio de la parte demandada o el medio por el que puede ser requerido."*
- **Art. 749.2**: intervencion preceptiva del Ministerio Fiscal cuando hay menores o personas con discapacidad.
- **Art. 773**: tramitacion de las medidas provisionales, a la que remite el art. 775.3 para la modificacion provisional.

### LO 1/2025 — requisito de procedibilidad (MASC)

- **Art. 5.1:** en el orden civil, con caracter general, para que la demanda sea admisible es requisito de procedibilidad acudir previamente a un MASC, y **debe existir identidad entre el objeto de la negociacion y el objeto del litigio**. Se cumple con mediacion, conciliacion, opinion neutral de experto independiente, oferta vinculante confidencial, Derecho colaborativo o **actividad negociadora desarrollada directamente por las partes o entre sus abogados bajo sus directrices y con su conformidad**.
- **Art. 5.2:** se exige en todos los procesos declarativos del libro II y en los **procesos especiales del libro IV** de la LEC, con ocho excepciones tasadas: derechos fundamentales; medidas del art. 158 CC; medidas de apoyo a personas con discapacidad; filiacion, paternidad y maternidad; tutela sumaria de tenencia o posesion; demolicion por ruina; ingreso de menores en centros, entrada en domicilio para ejecucion de medidas de proteccion y restitucion en sustraccion internacional; juicio cambiario.

  **VERIFICADO:** la modificacion de medidas del art. 775 LEC es un proceso especial del libro IV y **NO figura entre las excepciones del art. 5.2**. Por tanto, en la via contenciosa hay que acreditar el intento de MASC. La excepcion practica es la violencia de genero, donde el art. 89.9 LOPJ veda expresamente los MASC.

### LOPJ — art. 89 (redaccion LO 1/2025)

- **89.6:** las Secciones de Violencia sobre la Mujer pueden conocer en el orden civil, entre otros, de: **a)** los relativos al matrimonio y a su regimen economico y *"los que tengan por objeto la adopcion o modificacion de medidas de trascendencia familiar"*; **b)** los que versen exclusivamente sobre guarda y custodia de hijos menores o sobre alimentos reclamados por un progenitor contra el otro en nombre de los hijos menores; **c)** *"los relativos a modificacion de medidas adoptadas en los procesos que versen sobre las materias previstas en las letras anteriores"*.
- **89.7:** competencia **exclusiva y excluyente** cuando concurren los cuatro requisitos (materia del ap. 6, victima de violencia de genero o sexual, parte imputada, y actuaciones penales o orden de proteccion iniciadas).
- **89.9:** *"En todos estos casos esta vedada la utilizacion de los medios adecuados de solucion de controversias."*
- El antiguo **art. 87 ter LOPJ fue SUPRIMIDO** por la LO 1/2025 (la consulta a la API del BOE devuelve el bloque solo como historico). **No citarlo como vigente:** citar art. 89 LOPJ en relacion con el art. 44 LO 1/2004.

---

## Requisitos de la alteracion sustancial — cautela de citas

La doctrina consolidada exige que el cambio sea **sustancial, sobrevenido, acreditado, no imputable a quien lo alega y con vocacion de permanencia**. Esta formulacion se enuncia en la skill como **criterio general con base legal en los arts. 775.1 LEC, 90.3 y 91 in fine CC**, NUNCA atribuida a una sentencia concreta. **Prohibido citar resoluciones del Tribunal Supremo o de Audiencias Provinciales sin haberlas verificado en CENDOJ en la misma sesion.** Ver `references/requisitos-alteracion-sustancial.md`.

---

## Herramienta oficial de referencia — Tablas orientadoras del CGPJ (pension de alimentos)

| Recurso | Detalle |
|---|---|
| Nombre | Tablas orientadoras para determinar las pensiones alimenticias de los hijos en los procesos de familia |
| Organismo | Consejo General del Poder Judicial (CGPJ) |
| URL oficial | https://www.poderjudicial.es/cgpj/es/Servicios/Utilidades/Calculo-de-pensiones-alimenticias/ |
| Estado verificado (31/08/2026) | La pagina responde pero el apartado consta "en proceso de revision y actualizacion" |
| Caracter | Orientador, NO vinculante (arts. 93, 142 y 146 CC) |

La skill cita estas tablas al justificar un nuevo importe de alimentos, siempre como referencia orientadora. En cada lanzamiento, re-verificar la URL.

---

## Plantillas validadas

| Recurso | Detalle |
|---|---|
| Estructura de la demanda de modificacion de medidas | Arts. 775.1 y 775.2 LEC en relacion con el art. 770 LEC (contenciosa, juicio verbal) o el art. 777 LEC (mutuo acuerdo, con propuesta de nuevo convenio): AL JUZGADO / HECHOS (medidas vigentes, alteracion sustancial, MASC) / FUNDAMENTOS DE DERECHO / SUPLICO con la medida nueva concreta / OTROSI de prueba y, en su caso, de modificacion provisional (art. 775.3 LEC) |
| Estructura de la solicitud de extincion de la pension de alimentos | Misma estructura procesal (art. 775 LEC) con pretension de extincion fundada en los arts. 152.3.º y 142 CC y, en su caso, en la perdida del presupuesto del art. 93.2 CC |
| Requerimiento extrajudicial previo | Bloque condicional: burofax o comunicacion fehaciente al otro progenitor, que sirve simultaneamente de intento de MASC (art. 5.1 LO 1/2025, negociacion directa) si se documenta como tal |
| Orientacion practica | Guias de los Colegios de la Abogacia y del Ministerio de Justicia sobre procesos de familia |

Los assets `assets/demanda-modificacion-medidas.md` y `assets/solicitud-extincion-pension-alimentos.md` reflejan esta estructura. En cada lanzamiento, la skill re-verifica los articulos citados en el BOE; si detecta una redaccion posterior, actualiza el asset y las references afectadas.

---

## Verificacion de normativa autonomica

El derecho civil foral (Cataluna, Aragon, Navarra, Pais Vasco, Baleares, Galicia) puede regular de forma propia la guarda y custodia, los alimentos o la vivienda familiar, y por tanto tambien su modificacion. Si las medidas de origen se dictaron bajo derecho foral, verificar con `web_search` la norma autonomica vigente antes de redactar y advertir al usuario.
