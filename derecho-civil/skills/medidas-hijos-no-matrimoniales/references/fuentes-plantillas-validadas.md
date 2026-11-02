# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-medidas-hijos-no-matrimoniales`. Registra las
> fuentes normativas y las plantillas validadas que la skill verifica y, si detecta una versión
> posterior, aplica la redacción vigente al documento que redacta en cada lanzamiento.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local, se advierte expresamente al usuario y el punto queda marcado como pendiente de verificación manual. **Prohibido dar por vigente lo que no se ha podido verificar.**

---

## Fuentes normativas (BOE) — verificadas el 02/09/2026 contra la API de legislación consolidada del BOE

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Código Civil (Real Decreto de 24 de julio de 1889, texto consolidado) | BOE-A-1889-4763 | consolidado; bloques verificados uno a uno (ver tabla de artículos) | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado; bloques verificados uno a uno (ver tabla de artículos) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LO 1/2025 de eficiencia del Servicio Público de Justicia (MASC) | BOE-A-2025-76 | 02/01/2025 (requisito de procedibilidad en vigor desde 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |
| LOPJ — Ley Orgánica 6/1985 del Poder Judicial | BOE-A-1985-12666 | art. 89 en redacción de la LO 1/2025 (versión del bloque: 03/01/2025); el antiguo art. 87 ter consta **(Suprimido)** por el art. 1.26 de la LO 1/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-1985-12666 |
| LO 1/2004 de Medidas de Protección Integral contra la Violencia de Género | BOE-A-2004-21760 | art. 44 (competencia), redacción vigente | https://www.boe.es/buscar/act.php?id=BOE-A-2004-21760 |

### Artículos verificados bloque a bloque (API de legislación consolidada, 02/09/2026)

Endpoint utilizado (requiere cabecera `Accept: application/xml`; la redacción vigente es la ÚLTIMA `<version>` del bloque):

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{numero}
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a{numero}
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2025-76/texto/bloque/a5
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1985-12666/texto/bloque/aochentaynueve
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1985-12666/texto/bloque/aochentaysieteter
```

**Aviso sobre los identificadores de bloque:** el Código Civil usa `art{numero}` y la LEC `a{numero}`, pero la LOPJ identifica sus bloques con el ordinal escrito en letras (`aochentaynueve`, `aochentaysieteter`): `a89` devuelve HTTP 404 y no significa que el artículo no exista.

| Artículo | Contenido verificado | Última versión del bloque |
|---|---|---|
| CC 92 | Guarda y custodia; 92.1 las obligaciones con los hijos subsisten; 92.2 resolución motivada en el interés superior del menor; 92.4 ejercicio de la patria potestad por uno solo en beneficio del hijo; 92.5 custodia compartida a petición de ambos; 92.6 informe del Ministerio Fiscal previo; 92.7 prohibición de guarda conjunta con violencia; 92.8 compartida excepcional a instancia de una parte | 06/09/2022 (LO 10/2022) |
| CC 93 | El juez determina en todo caso la contribución de cada progenitor a los alimentos; párrafo 2.º hijos mayores sin ingresos que convivan | 18/10/1990 (Ley 11/1990) |
| CC 94 | Tiempo, modo y lugar de visitas, comunicación y estancias; audiencia del hijo y del Ministerio Fiscal; limitación o suspensión; NO procede régimen de visitas con proceso penal por violencia ni con indicios fundados de violencia doméstica o de género | 03/06/2021 (Ley 8/2021) |
| CC 96 | Uso de la vivienda familiar. **Redactado literalmente para los cónyuges y para los supuestos de nulidad, separación y divorcio** (96.1 y 96.2 hablan de "cónyuge"); 96.3 restricción de la facultad dispositiva | 03/06/2021 (Ley 8/2021) |
| CC 142 | Concepto de alimentos: sustento, habitación, vestido, asistencia médica, educación e instrucción; gastos de embarazo y parto | 19/05/1981 (Ley 11/1981) |
| CC 143 | Obligados recíprocamente: cónyuges; ascendientes y descendientes | 19/05/1981 (Ley 11/1981) |
| CC 146 | Cuantía proporcionada al caudal o medios de quien los da y a las necesidades de quien los recibe | 19/05/1981 (Ley 11/1981) |
| CC 148 | La obligación es exigible desde que se necesitan, pero **no se abonan sino desde la fecha de interposición de la demanda**; pago por meses anticipados | 19/05/1981 (Ley 11/1981) |
| CC 152 | Causas de cese de la obligación de dar alimentos | 25/07/1889 (redacción originaria) |
| CC 154 | Patria potestad como responsabilidad parental; deberes y facultades; 154.3.º **decidir el lugar de residencia habitual del menor solo puede modificarse con el consentimiento de ambos progenitores o autorización judicial**; audiencia del hijo con suficiente madurez | 05/06/2021 (LO 8/2021) |
| CC 156 | Ejercicio conjunto de la patria potestad o por uno con el consentimiento del otro; desacuerdo → autoridad judicial atribuye la facultad de decidir, oyendo al hijo si tiene suficiente madurez y en todo caso si es mayor de doce años; **párrafo final: si los progenitores viven separados, la patria potestad se ejercerá por aquel con quien el hijo conviva, salvo que la autoridad judicial, a solicitud fundada del otro, atribuya el ejercicio conjunto o distribuya las funciones** | 03/06/2021 (Ley 8/2021) |
| LEC 748 | Ámbito del Título I del Libro IV. **748.4.º: "Los que versen exclusivamente sobre guarda y custodia de hijos menores o sobre alimentos reclamados por un progenitor contra el otro en nombre de los hijos menores"** | 03/06/2021 (Ley 8/2021) |
| LEC 749 | 749.2: intervención **preceptiva** del Ministerio Fiscal en los demás procesos del Título I del Libro IV siempre que alguno de los interesados sea menor | 03/06/2021 (Ley 8/2021) |
| LEC 769 | Competencia. **769.3: en los procesos que versen exclusivamente sobre guarda y custodia de hijos menores o sobre alimentos reclamados por un progenitor contra el otro en nombre de los hijos menores, es competente el Juzgado de Primera Instancia del último domicilio común de los progenitores; si residen en distintos partidos judiciales, a elección del demandante, el del domicilio del demandado o el de la residencia del menor.** 769.4: examen de oficio de la competencia y nulidad de los acuerdos de las partes que se opongan | 03/07/2015 (Ley 15/2015) |
| LEC 770 | Procedimiento: trámites del **juicio verbal** con reglas especiales; regla 1.ª documentos económicos; regla 2.ª reconvención y sus supuestos tasados; regla 3.ª comparecencia personal y presencia obligatoria de abogados; **regla 4.ª: los hijos podrán ser oídos cuando tengan menos de doce años y "debiendo ser oídos en todo caso si hubieran alcanzado dicha edad"** | 20/12/2023 (RDL 6/2023, vigente desde 20/03/2024) |
| LEC 777 | Separación o divorcio de mutuo acuerdo: escrito con propuesta de convenio y certificaciones; 777.3 ratificación por separado; **777.5 informe del Ministerio Fiscal sobre los términos relativos a los hijos menores**; 777.6 sentencia | 03/06/2021 (Ley 8/2021) |
| LEC 264 | 264.4.º: documento que acredite el intento de la actividad negociadora previa o declaración responsable de su imposibilidad | verificado 02/09/2026 |
| LO 1/2025 art. 5 | Requisito de procedibilidad. **5.2: se exige actividad negociadora previa en todos los declarativos del libro II y en los procesos especiales del libro IV de la LEC, salvo las materias tasadas de las letras a) a h)** — entre las excepciones figuran las medidas del art. 158 CC (letra b) y la filiación, paternidad y maternidad (letra d), pero **NO** la guarda, custodia y alimentos de hijos menores. 5.3: no es preciso para la demanda ejecutiva, medidas cautelares previas, diligencias preliminares ni jurisdicción voluntaria, **con excepción expresa de los expedientes de intervención judicial en caso de desacuerdo en el ejercicio de la patria potestad** | 02/01/2025 |
| LOPJ 89 | 89.6.a) competencia civil de las Secciones de Violencia sobre la Mujer en las acciones "derivadas de la crisis matrimonial **o de la unión de hecho**"; **89.6.b) los que versen exclusivamente sobre guarda y custodia de hijos e hijas menores o sobre alimentos reclamados por un progenitor contra el otro**; 89.6.e) los relativos a las relaciones paternofiliales; 89.7 competencia exclusiva y excluyente concurriendo los cuatro requisitos; **89.9 "En todos estos casos está vedada la utilización de los medios adecuados de solución de controversias"** | 03/01/2025 (LO 1/2025) |
| LOPJ 87 ter | Consta literalmente **"(Suprimido)"**. Se suprime por el art. 1.26 de la LO 1/2025. **PROHIBIDO citarlo como vigente** | suprimido |

### Ubicación sistemática verificada (fundamento del cauce procesal)

El bloque `civ-12` de la LEC (`https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/civ-12`) devuelve el rotulo del Capítulo IV del Título I del Libro IV: **"De los procesos matrimoniales y de menores"** (arts. 769 a 778). Los procesos del art. 748.4.º LEC —guarda, custodia y alimentos de hijos menores reclamados por un progenitor contra el otro, con independencia de que haya existido o no matrimonio— se sustancian en ese mismo capítulo, del que forman parte los arts. 770 (contencioso) y 777 (mutuo acuerdo). El art. 769.3 LEC es la regla de competencia escrita **específicamente** para estos procesos, lo que confirma que el legislador los sitúa en este capítulo.

### Puntos marcados como PENDIENTES DE VERIFICACIÓN MANUAL (no darlos por vigentes sin comprobarlos)

| Punto | Estado | Cómo debe tratarlo la skill |
|---|---|---|
| Aplicación del **art. 770 LEC** a las medidas paternofiliales no matrimoniales | El art. 770 delimita literalmente su ámbito en "las demandas de separación y divorcio, salvo las previstas en el artículo 777, las de nulidad del matrimonio y las demás que se formulen al amparo del **título IV del libro I del Código Civil**" (el matrimonio). Las medidas paternofiliales no matrimoniales se fundan en el título VII del libro I CC (patria potestad), no en el título IV | La skill afirma únicamente lo verificado: que estos procesos están en el mismo capítulo (art. 748.4.º y art. 769.3 LEC) y que **la práctica forense mayoritaria los sustancia por los trámites del juicio verbal del art. 770**. Debe presentarlo como cauce habitual, nunca como remisión legal expresa, y advertir de que conviene confirmar el criterio del juzgado competente |
| Aplicación del **art. 777 LEC** al pacto de relaciones familiares de progenitores no casados | El art. 777 está redactado para las peticiones de separación o divorcio de mutuo acuerdo | Igual tratamiento: cauce de aplicación analógica sostenido por la práctica forense para someter el pacto a aprobación judicial. La intervención del Ministerio Fiscal, en cambio, si tiene apoyo directo y verificado en el **art. 749.2 LEC** |
| Aplicación del **art. 96 CC** a la vivienda cuando no hay matrimonio | El art. 96 está redactado para los cónyuges y para la nulidad, separación y divorcio | La skill NO afirma que el art. 96 se aplique de forma directa. Explica que no hay régimen económico matrimonial que liquidar, que la atribución del uso depende de la titularidad del inmueble y del interés del menor, y que el criterio del art. 96 se invoca por analogía en beneficio de los hijos menores. Si la vivienda es privativa de un progenitor, ofrece escalación |
| Normativa civil autonómica | No verificada en este lanzamiento | Cataluña (Libro II del Código civil de Cataluña: plan de parentalidad), Aragon, Navarra, País Vasco, Baleares y Galicia pueden regular de forma propia la guarda de los hijos y las relaciones familiares tras la ruptura de la convivencia. Si el caso se rige por un derecho civil autonómico, verificar con `web_search` y advertir antes de redactar |
| Ley autonómica de parejas de hecho aplicable | No verificada en este lanzamiento | Solo relevante como prueba de la convivencia y de su cese. No altera el régimen de los hijos. Si el usuario pregunta por efectos patrimoniales del cese de la pareja, es materia distinta: escalar |

---

## Herramienta oficial de referencia — Tablas orientadoras del CGPJ (pensión de alimentos)

| Recurso | Detalle |
|---|---|
| Nombre | Tablas orientadoras para determinar las pensiones alimenticias de los hijos en los procesos de familia |
| Organismo | Consejo General del Poder Judicial (CGPJ) |
| URL oficial | https://www.poderjudicial.es/cgpj/es/Servicios/Utilidades/Calculo-de-pensiones-alimenticias/ |
| Estado verificado (02/09/2026) | La página responde (HTTP 200), pero el apartado consta literalmente: "Este apartado se encuentra actualmente en proceso de revisión y actualización" y "No hay información disponible". **La calculadora no está operativa en esta fecha** |
| Carácter | Orientador, NO vinculante: el juez puede apartarse según las circunstancias (arts. 93, 142 y 146 CC) |

La skill cita estas tablas al explicar la pensión de alimentos, siempre como referencia orientadora y nunca como cuantía obligatoria, y **advierte al usuario de que el apartado del CGPJ consta en revisión** mientras esa sea la situación verificada. En cada lanzamiento se re-verifica la URL; si el CGPJ publica la herramienta actualizada, se registra aquí la nueva fecha y se elimina la advertencia.

---

## Plantillas validadas

| Recurso | Detalle |
|---|---|
| Estructura del pacto de relaciones familiares | Contenido material equivalente al del convenio regulador en lo relativo a los hijos: ejercicio de la patria potestad (arts. 154 y 156 CC), guarda y custodia (art. 92 CC), régimen de estancias y comunicación (art. 94 CC), pensión de alimentos con gastos ordinarios y extraordinarios (arts. 93, 142, 146 y 148 CC) y, en su caso, uso de la vivienda en que residen los hijos. **No contiene liquidación de régimen económico ni pensión compensatoria: ambas instituciones son propias del matrimonio** |
| Estructura de la demanda de medidas paternofiliales (contenciosa) | Arts. 748.4.º, 769.3 y 770 LEC: AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / MEDIDAS QUE SE SOLICITAN / SUPLICO / OTROSÍ (prueba y, en su caso, medidas provisionales), con acreditación del intento de MASC (art. 264.4.º LEC) e intervención del Ministerio Fiscal (art. 749.2 LEC) |
| Estructura de la demanda conjunta de mutuo acuerdo | Escrito conjunto acompañando el pacto de relaciones familiares y las certificaciones literales de nacimiento, sometido a ratificación e informe del Ministerio Fiscal (arts. 749.2 y 777 LEC, este último por el cauce analógico descrito arriba) |
| Orientación práctica | Guías de los Colegios de la Abogacía y del Ministerio de Justicia sobre procesos de familia y redacción judicial clara |

Los assets `assets/pacto-relaciones-familiares.md` y `assets/demanda-medidas-paternofiliales.md` reflejan esta estructura. En cada lanzamiento, la skill re-verifica los artículos citados en el BOE; si detecta una redacción posterior, actualiza el asset y las references afectadas antes de redactar.

---

## Guías de estilo de redacción (consulta)

| Recurso | Uso |
|---|---|
| Guía de redacción judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminología y corrección del lenguaje jurídico |
| Guía de buenas prácticas sobre escritos e informes (ICAB) | Extensión razonable del escrito |

Ver `references/estilo-redaccion-escritos.md` para las reglas concretas que la skill aplica al rellenar los assets.
