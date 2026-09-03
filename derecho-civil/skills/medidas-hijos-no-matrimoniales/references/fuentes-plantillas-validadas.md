# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-medidas-hijos-no-matrimoniales`. Registra las
> fuentes normativas y las plantillas validadas que la skill verifica y, si detecta una version
> posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Punto 2 se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local, se advierte expresamente al usuario y el punto queda marcado como pendiente de verificacion manual. **Prohibido dar por vigente lo que no se ha podido verificar.**

---

## Fuentes normativas (BOE) — verificadas el 02/09/2026 contra la API de legislacion consolidada del BOE

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Codigo Civil (Real Decreto de 24 de julio de 1889, texto consolidado) | BOE-A-1889-4763 | consolidado; bloques verificados uno a uno (ver tabla de articulos) | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado; bloques verificados uno a uno (ver tabla de articulos) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LO 1/2025 de eficiencia del Servicio Publico de Justicia (MASC) | BOE-A-2025-76 | 02/01/2025 (requisito de procedibilidad en vigor desde 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |
| LOPJ — Ley Organica 6/1985 del Poder Judicial | BOE-A-1985-12666 | art. 89 en redaccion de la LO 1/2025 (version del bloque: 03/01/2025); el antiguo art. 87 ter consta **(Suprimido)** por el art. 1.26 de la LO 1/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-1985-12666 |
| LO 1/2004 de Medidas de Proteccion Integral contra la Violencia de Genero | BOE-A-2004-21760 | art. 44 (competencia), redaccion vigente | https://www.boe.es/buscar/act.php?id=BOE-A-2004-21760 |

### Articulos verificados bloque a bloque (API de legislacion consolidada, 02/09/2026)

Endpoint utilizado (requiere cabecera `Accept: application/xml`; la redaccion vigente es la ULTIMA `<version>` del bloque):

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{numero}
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a{numero}
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2025-76/texto/bloque/a5
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1985-12666/texto/bloque/aochentaynueve
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1985-12666/texto/bloque/aochentaysieteter
```

**Aviso sobre los identificadores de bloque:** el Codigo Civil usa `art{numero}` y la LEC `a{numero}`, pero la LOPJ identifica sus bloques con el ordinal escrito en letras (`aochentaynueve`, `aochentaysieteter`): `a89` devuelve HTTP 404 y no significa que el articulo no exista.

| Articulo | Contenido verificado | Ultima version del bloque |
|---|---|---|
| CC 92 | Guarda y custodia; 92.1 las obligaciones con los hijos subsisten; 92.2 resolucion motivada en el interes superior del menor; 92.4 ejercicio de la patria potestad por uno solo en beneficio del hijo; 92.5 custodia compartida a peticion de ambos; 92.6 informe del Ministerio Fiscal previo; 92.7 prohibicion de guarda conjunta con violencia; 92.8 compartida excepcional a instancia de una parte | 06/09/2022 (LO 10/2022) |
| CC 93 | El juez determina en todo caso la contribucion de cada progenitor a los alimentos; parrafo 2.º hijos mayores sin ingresos que convivan | 18/10/1990 (Ley 11/1990) |
| CC 94 | Tiempo, modo y lugar de visitas, comunicacion y estancias; audiencia del hijo y del Ministerio Fiscal; limitacion o suspension; NO procede regimen de visitas con proceso penal por violencia ni con indicios fundados de violencia domestica o de genero | 03/06/2021 (Ley 8/2021) |
| CC 96 | Uso de la vivienda familiar. **Redactado literalmente para los conyuges y para los supuestos de nulidad, separacion y divorcio** (96.1 y 96.2 hablan de "conyuge"); 96.3 restriccion de la facultad dispositiva | 03/06/2021 (Ley 8/2021) |
| CC 142 | Concepto de alimentos: sustento, habitacion, vestido, asistencia medica, educacion e instruccion; gastos de embarazo y parto | 19/05/1981 (Ley 11/1981) |
| CC 143 | Obligados reciprocamente: conyuges; ascendientes y descendientes | 19/05/1981 (Ley 11/1981) |
| CC 146 | Cuantia proporcionada al caudal o medios de quien los da y a las necesidades de quien los recibe | 19/05/1981 (Ley 11/1981) |
| CC 148 | La obligacion es exigible desde que se necesitan, pero **no se abonan sino desde la fecha de interposicion de la demanda**; pago por meses anticipados | 19/05/1981 (Ley 11/1981) |
| CC 152 | Causas de cese de la obligacion de dar alimentos | 25/07/1889 (redaccion originaria) |
| CC 154 | Patria potestad como responsabilidad parental; deberes y facultades; 154.3.º **decidir el lugar de residencia habitual del menor solo puede modificarse con el consentimiento de ambos progenitores o autorizacion judicial**; audiencia del hijo con suficiente madurez | 05/06/2021 (LO 8/2021) |
| CC 156 | Ejercicio conjunto de la patria potestad o por uno con el consentimiento del otro; desacuerdo → autoridad judicial atribuye la facultad de decidir, oyendo al hijo si tiene suficiente madurez y en todo caso si es mayor de doce anos; **parrafo final: si los progenitores viven separados, la patria potestad se ejercera por aquel con quien el hijo conviva, salvo que la autoridad judicial, a solicitud fundada del otro, atribuya el ejercicio conjunto o distribuya las funciones** | 03/06/2021 (Ley 8/2021) |
| LEC 748 | Ambito del Titulo I del Libro IV. **748.4.º: "Los que versen exclusivamente sobre guarda y custodia de hijos menores o sobre alimentos reclamados por un progenitor contra el otro en nombre de los hijos menores"** | 03/06/2021 (Ley 8/2021) |
| LEC 749 | 749.2: intervencion **preceptiva** del Ministerio Fiscal en los demas procesos del Titulo I del Libro IV siempre que alguno de los interesados sea menor | 03/06/2021 (Ley 8/2021) |
| LEC 769 | Competencia. **769.3: en los procesos que versen exclusivamente sobre guarda y custodia de hijos menores o sobre alimentos reclamados por un progenitor contra el otro en nombre de los hijos menores, es competente el Juzgado de Primera Instancia del ultimo domicilio comun de los progenitores; si residen en distintos partidos judiciales, a eleccion del demandante, el del domicilio del demandado o el de la residencia del menor.** 769.4: examen de oficio de la competencia y nulidad de los acuerdos de las partes que se opongan | 03/07/2015 (Ley 15/2015) |
| LEC 770 | Procedimiento: tramites del **juicio verbal** con reglas especiales; regla 1.ª documentos economicos; regla 2.ª reconvencion y sus supuestos tasados; regla 3.ª comparecencia personal y presencia obligatoria de abogados; **regla 4.ª: los hijos podran ser oidos cuando tengan menos de doce anos y "debiendo ser oidos en todo caso si hubieran alcanzado dicha edad"** | 20/12/2023 (RDL 6/2023, vigente desde 20/03/2024) |
| LEC 777 | Separacion o divorcio de mutuo acuerdo: escrito con propuesta de convenio y certificaciones; 777.3 ratificacion por separado; **777.5 informe del Ministerio Fiscal sobre los terminos relativos a los hijos menores**; 777.6 sentencia | 03/06/2021 (Ley 8/2021) |
| LEC 264 | 264.4.º: documento que acredite el intento de la actividad negociadora previa o declaracion responsable de su imposibilidad | verificado 02/09/2026 |
| LO 1/2025 art. 5 | Requisito de procedibilidad. **5.2: se exige actividad negociadora previa en todos los declarativos del libro II y en los procesos especiales del libro IV de la LEC, salvo las materias tasadas de las letras a) a h)** — entre las excepciones figuran las medidas del art. 158 CC (letra b) y la filiacion, paternidad y maternidad (letra d), pero **NO** la guarda, custodia y alimentos de hijos menores. 5.3: no es preciso para la demanda ejecutiva, medidas cautelares previas, diligencias preliminares ni jurisdiccion voluntaria, **con excepcion expresa de los expedientes de intervencion judicial en caso de desacuerdo en el ejercicio de la patria potestad** | 02/01/2025 |
| LOPJ 89 | 89.6.a) competencia civil de las Secciones de Violencia sobre la Mujer en las acciones "derivadas de la crisis matrimonial **o de la union de hecho**"; **89.6.b) los que versen exclusivamente sobre guarda y custodia de hijos e hijas menores o sobre alimentos reclamados por un progenitor contra el otro**; 89.6.e) los relativos a las relaciones paternofiliales; 89.7 competencia exclusiva y excluyente concurriendo los cuatro requisitos; **89.9 "En todos estos casos esta vedada la utilizacion de los medios adecuados de solucion de controversias"** | 03/01/2025 (LO 1/2025) |
| LOPJ 87 ter | Consta literalmente **"(Suprimido)"**. Se suprime por el art. 1.26 de la LO 1/2025. **PROHIBIDO citarlo como vigente** | suprimido |

### Ubicacion sistematica verificada (fundamento del cauce procesal)

El bloque `civ-12` de la LEC (`https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/civ-12`) devuelve el rotulo del Capitulo IV del Titulo I del Libro IV: **"De los procesos matrimoniales y de menores"** (arts. 769 a 778). Los procesos del art. 748.4.º LEC —guarda, custodia y alimentos de hijos menores reclamados por un progenitor contra el otro, con independencia de que haya existido o no matrimonio— se sustancian en ese mismo capitulo, del que forman parte los arts. 770 (contencioso) y 777 (mutuo acuerdo). El art. 769.3 LEC es la regla de competencia escrita **especificamente** para estos procesos, lo que confirma que el legislador los situa en este capitulo.

### Puntos marcados como PENDIENTES DE VERIFICACION MANUAL (no darlos por vigentes sin comprobarlos)

| Punto | Estado | Como debe tratarlo la skill |
|---|---|---|
| Aplicacion del **art. 770 LEC** a las medidas paternofiliales no matrimoniales | El art. 770 delimita literalmente su ambito en "las demandas de separacion y divorcio, salvo las previstas en el articulo 777, las de nulidad del matrimonio y las demas que se formulen al amparo del **titulo IV del libro I del Codigo Civil**" (el matrimonio). Las medidas paternofiliales no matrimoniales se fundan en el titulo VII del libro I CC (patria potestad), no en el titulo IV | La skill afirma unicamente lo verificado: que estos procesos estan en el mismo capitulo (art. 748.4.º y art. 769.3 LEC) y que **la practica forense mayoritaria los sustancia por los tramites del juicio verbal del art. 770**. Debe presentarlo como cauce habitual, nunca como remision legal expresa, y advertir de que conviene confirmar el criterio del juzgado competente |
| Aplicacion del **art. 777 LEC** al pacto de relaciones familiares de progenitores no casados | El art. 777 esta redactado para las peticiones de separacion o divorcio de mutuo acuerdo | Igual tratamiento: cauce de aplicacion analogica sostenido por la practica forense para someter el pacto a aprobacion judicial. La intervencion del Ministerio Fiscal, en cambio, si tiene apoyo directo y verificado en el **art. 749.2 LEC** |
| Aplicacion del **art. 96 CC** a la vivienda cuando no hay matrimonio | El art. 96 esta redactado para los conyuges y para la nulidad, separacion y divorcio | La skill NO afirma que el art. 96 se aplique de forma directa. Explica que no hay regimen economico matrimonial que liquidar, que la atribucion del uso depende de la titularidad del inmueble y del interes del menor, y que el criterio del art. 96 se invoca por analogia en beneficio de los hijos menores. Si la vivienda es privativa de un progenitor, ofrece escalacion |
| Normativa civil autonomica | No verificada en este lanzamiento | Cataluna (Libro II del Codigo civil de Cataluna: plan de parentalidad), Aragon, Navarra, Pais Vasco, Baleares y Galicia pueden regular de forma propia la guarda de los hijos y las relaciones familiares tras la ruptura de la convivencia. Si el caso se rige por un derecho civil autonomico, verificar con `web_search` y advertir antes de redactar |
| Ley autonomica de parejas de hecho aplicable | No verificada en este lanzamiento | Solo relevante como prueba de la convivencia y de su cese. No altera el regimen de los hijos. Si el usuario pregunta por efectos patrimoniales del cese de la pareja, es materia distinta: escalar |

---

## Herramienta oficial de referencia — Tablas orientadoras del CGPJ (pension de alimentos)

| Recurso | Detalle |
|---|---|
| Nombre | Tablas orientadoras para determinar las pensiones alimenticias de los hijos en los procesos de familia |
| Organismo | Consejo General del Poder Judicial (CGPJ) |
| URL oficial | https://www.poderjudicial.es/cgpj/es/Servicios/Utilidades/Calculo-de-pensiones-alimenticias/ |
| Estado verificado (02/09/2026) | La pagina responde (HTTP 200), pero el apartado consta literalmente: "Este apartado se encuentra actualmente en proceso de revision y actualizacion" y "No hay informacion disponible". **La calculadora no esta operativa en esta fecha** |
| Caracter | Orientador, NO vinculante: el juez puede apartarse segun las circunstancias (arts. 93, 142 y 146 CC) |

La skill cita estas tablas al explicar la pension de alimentos, siempre como referencia orientadora y nunca como cuantia obligatoria, y **advierte al usuario de que el apartado del CGPJ consta en revision** mientras esa sea la situacion verificada. En cada lanzamiento se re-verifica la URL; si el CGPJ publica la herramienta actualizada, se registra aqui la nueva fecha y se elimina la advertencia.

---

## Plantillas validadas

| Recurso | Detalle |
|---|---|
| Estructura del pacto de relaciones familiares | Contenido material equivalente al del convenio regulador en lo relativo a los hijos: ejercicio de la patria potestad (arts. 154 y 156 CC), guarda y custodia (art. 92 CC), regimen de estancias y comunicacion (art. 94 CC), pension de alimentos con gastos ordinarios y extraordinarios (arts. 93, 142, 146 y 148 CC) y, en su caso, uso de la vivienda en que residen los hijos. **No contiene liquidacion de regimen economico ni pension compensatoria: ambas instituciones son propias del matrimonio** |
| Estructura de la demanda de medidas paternofiliales (contenciosa) | Arts. 748.4.º, 769.3 y 770 LEC: AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / MEDIDAS QUE SE SOLICITAN / SUPLICO / OTROSI (prueba y, en su caso, medidas provisionales), con acreditacion del intento de MASC (art. 264.4.º LEC) e intervencion del Ministerio Fiscal (art. 749.2 LEC) |
| Estructura de la demanda conjunta de mutuo acuerdo | Escrito conjunto acompanando el pacto de relaciones familiares y las certificaciones literales de nacimiento, sometido a ratificacion e informe del Ministerio Fiscal (arts. 749.2 y 777 LEC, este ultimo por el cauce analogico descrito arriba) |
| Orientacion practica | Guias de los Colegios de la Abogacia y del Ministerio de Justicia sobre procesos de familia y redaccion judicial clara |

Los assets `assets/pacto-relaciones-familiares.md` y `assets/demanda-medidas-paternofiliales.md` reflejan esta estructura. En cada lanzamiento, la skill re-verifica los articulos citados en el BOE; si detecta una redaccion posterior, actualiza el asset y las references afectadas antes de redactar.

---

## Guias de estilo de redaccion (consulta)

| Recurso | Uso |
|---|---|
| Guia de redaccion judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminologia y correccion del lenguaje juridico |
| Guia de buenas practicas sobre escritos e informes (ICAB) | Extension razonable del escrito |

Ver `references/estilo-redaccion-escritos.md` para las reglas concretas que la skill aplica al rellenar los assets.
