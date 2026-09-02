---
name: derecho-civil-medidas-hijos-no-matrimoniales
description: >
  Genera los documentos para FIJAR POR PRIMERA VEZ las medidas relativas a los hijos menores comunes
  de progenitores que no estan ni han estado casados entre si (parejas de hecho registradas, parejas
  no registradas y progenitores que nunca convivieron), en el proceso del articulo 748.4.º de la Ley
  de Enjuiciamiento Civil, en sus dos vias: (1) CON ACUERDO — pacto de relaciones familiares que
  regula el ejercicio de la patria potestad (arts. 154 y 156 CC), la guarda y custodia (art. 92 CC),
  el regimen de estancias, comunicacion y visitas (art. 94 CC), la pension de alimentos (arts. 93,
  142, 146 y 148 CC) y, en su caso, el uso de la vivienda en que residen los hijos, para su
  sometimiento a aprobacion judicial por el cauce del articulo 777 de la LEC; y (2) SIN ACUERDO —
  demanda de medidas paternofiliales por los tramites del juicio verbal del articulo 770 de la LEC,
  con acreditacion del intento de MASC (art. 5 LO 1/2025) e intervencion preceptiva del Ministerio
  Fiscal (art. 749.2 LEC). Verifica la version vigente de las normas en el BOE antes de redactar.
  NO usar entre conyuges (eso es divorcio o separacion), NO usar para modificar medidas ya fijadas,
  NO cubre la determinacion ni la impugnacion de la filiacion, NO cubre la reclamacion de pensiones
  impagadas ni el traslado internacional del menor, y se detiene y escala si existen indicios de
  violencia de genero o domestica.
when_to_use: |
  - Una pareja de hecho con hijos comunes se separa y necesita fijar custodia, estancias y alimentos.
  - Dos progenitores que nunca estuvieron casados no tienen ninguna medida judicial sobre sus hijos
    y quieren regularla, con acuerdo o sin el.
  - El usuario quiere reclamar al otro progenitor la pension de alimentos de un hijo comun cuando no
    hay sentencia ni convenio previo que la fije.
  - El usuario quiere que se le atribuya la guarda y custodia de su hijo, o un regimen de estancias,
    sin que haya habido matrimonio con el otro progenitor.
  - El usuario tiene un acuerdo con el otro progenitor y quiere darle validez y fuerza ejecutiva
    sometiendolo a la aprobacion del Juzgado.
inputs:
  - filiacion: determinada respecto de ambos progenitores / no determinada respecto del otro / se desconoce
  - acuerdo: existe acuerdo con el otro progenitor / no existe acuerdo
  - medidas: guarda y custodia con regimen de estancias / pension de alimentos / ambas
  - vivienda: se solicita la atribucion del uso de la vivienda en que residen los hijos (si / no)
  - convivencia: pareja de hecho inscrita en registro / convivencia sin inscripcion / sin convivencia estable
  - alcance: solo el pacto de relaciones familiares / pacto y demanda conjunta (solo en la via de acuerdo)
  - datos_progenitor_a: nombre, DNI o NIE, domicilio
  - datos_progenitor_b: nombre, DNI o NIE, domicilio
  - datos_hijos: nombre y fecha de nacimiento de cada hijo (unicos datos de menores que se recaban)
  - patria_potestad: decisiones que requeriran el acuerdo de ambos y via de comunicacion entre progenitores
  - custodia_estancias: modalidad de guarda, calendario de estancias, reparto de vacaciones y lugar de entregas
  - pension_alimentos: importe por hijo, dia de pago, cuenta, actualizacion y reparto de gastos extraordinarios
  - vivienda_datos: direccion, titularidad, atribucion del uso y plazo o condicion de cese
  - masc: en la via contenciosa, tipo y fechas del intento de MASC o motivo de imposibilidad
  - documentacion_economica: documentos que acreditan la situacion economica (regla 1.ª del art. 770 LEC)
  - medidas_provisionales: en la via contenciosa, si se interesan
  - partido_judicial: competencia del art. 769.3 LEC
outputs:
  - pacto_relaciones_familiares: pacto de relaciones familiares en markdown, DRAFT
  - demanda_medidas_paternofiliales: demanda conjunta de mutuo acuerdo o demanda contenciosa de medidas
    paternofiliales en markdown, DRAFT (un mismo asset con dos variantes condicionales)
references:
  - references/cc-medidas-hijos-no-matrimoniales.md
  - references/lec-proceso-medidas-paternofiliales.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/pacto-relaciones-familiares.md
  - assets/demanda-medidas-paternofiliales.md
---

# Fijar las Medidas Relativas a los Hijos de Progenitores no Casados

## 0. CONFIRMACION DE CARGA Y ARRANQUE (visible, una sola vez)

Al cargarse esta skill, lo PRIMERO que emites en el chat, antes de cualquier otro texto, es esta linea fija:

**Skill cargada satisfactoriamente.**

A continuacion, en el MISMO mensaje y sin esperar ninguna confirmacion del usuario, ARRANCAS la ejecucion del procedimiento: emite la introduccion fija del Punto 1 y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa. Si el procedimiento arranca con una verificacion normativa interna (Punto 2), ejecutala en silencio y continua hasta la primera pregunta o hasta la Confirmacion visible del Punto 3, segun corresponda.

PROHIBIDO detenerse tras la linea de carga, preguntar si desea empezar, o emitir la linea a solas en un turno propio: la skill queda cargada y en ejecucion en ese mismo turno. La linea se emite una unica vez, al cargar, y no se repite en ningun turno posterior.

Esta linea es, junto con la introduccion fija del Punto 1 y los anuncios de seccion del Punto 5, la UNICA excepcion a la Directiva de Invisibilidad.

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la logica descrita en este documento (la clasificacion de vectores, el enrutamiento, la validacion de presupuestos, la verificacion normativa y la creacion base) es un flujo de ejecucion ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2") o de hojas del arbol.
- Resumenes de validacion con checks (ej. "Filiacion: ✔").
- Fases de instruccion (ej. "Ahora voy a crear el documento", "Pasemos al punto 4").
- Preambulos conversacionales antes de hacer preguntas. Si es tu turno de preguntar, emite unicamente la pregunta exacta — con la unica excepcion de la linea de carga del Punto 0, de la introduccion fija del Punto 1, que solo se usa una vez en el primer turno de toda la conversacion, y de los anuncios de seccion del Punto 5.

## 1. CLASIFICACION DINAMICA (Vectores de Estado)

**Introduccion (solo en el primer turno, una unica vez):** antes de la primera pregunta de clasificacion, y solo la primera vez, anade en el mismo mensaje esta introduccion fija, en el registro formal del plugin (usted, tono de abogado). No afirmes todavia que via ni que documento corresponde: depende de la clasificacion aun no resuelta.

"Vamos a proceder a la preparacion de los documentos necesarios para fijar las medidas relativas a sus hijos. Para ajustarlos correctamente a su caso, es necesario precisar antes algunos datos."

No repitas esta introduccion en turnos posteriores.

Tu primer objetivo es resolver los siguientes vectores de manera SILENCIOSA usando Escucha Activa. Si un vector ya esta resuelto por lo que dijo el usuario, OMITE su pregunta:

- **V1 (Acuerdo con el otro progenitor):** existe acuerdo integro sobre las medidas / no existe acuerdo.
- **V2 (Filiacion — BLOQUEANTE):** la filiacion del hijo consta determinada respecto de AMBOS progenitores / no consta determinada respecto del otro progenitor / el usuario lo desconoce.
- **V3 (Medidas que se piden):** el conjunto completo (guarda y custodia con regimen de estancias y pension de alimentos) / solo la guarda y custodia con su regimen de estancias / solo la pension de alimentos.
- **V3-bis (Uso de la vivienda):** se solicita ademas la atribucion del uso de la vivienda en que residen los hijos / no se solicita.
- **V4 (Convivencia previa y su constancia):** pareja inscrita en un registro de parejas de hecho / convivencia estable sin inscripcion / sin convivencia estable entre los progenitores. **Relevante solo como prueba de la convivencia y de su cese: no altera en nada el regimen de los hijos.**
- **V5 (Alcance — solo si V1 = existe acuerdo):** solo el pacto de relaciones familiares / el pacto y la demanda conjunta para presentarla en el Juzgado.

**Vector de guarda (no se pregunta nunca):** no existe pregunta de clasificacion sobre violencia. Si el relato del usuario revela indicios de violencia de genero o domestica, en cualquier punto del flujo, aplica de inmediato el Guardrail 3 (detener y escalar).

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o mas vectores, TIENES PROHIBIDO inventar la redaccion. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, **en este orden estricto** (omitiendo las que la Escucha Activa ya haya resuelto o las que no apliquen a la rama). El orden empieza por la filiacion porque es el unico presupuesto que puede dejar el caso entero fuera de esta via: preguntar antes cualquier otro dato haria trabajar al usuario en balde.

* **Primera pregunta — V2 (Filiacion):**
  "Respecto de la filiacion de sus hijos:
  1. Estan reconocidos legalmente por ambos progenitores y ambos figuran inscritos en el Registro Civil
  2. El otro progenitor no los ha reconocido y no consta su filiacion
  3. No lo se con seguridad"

  → Si la respuesta es 3, formula esta sub-pregunta de desambiguacion, con este texto exacto: "Puede comprobarlo solicitando la certificacion literal de nacimiento en el Registro Civil, donde figuran ambos progenitores si la filiacion esta determinada. Indiqueme si en el libro de familia o en la certificacion de nacimiento consta el otro progenitor:
  1. Si consta
  2. No consta
  3. No dispongo de ese documento"
  → Respuesta 1 → V2 = determinada, continuar. Respuestas 2 o 3 → **DETENER** conforme al Enrutamiento: no puede darse por determinada una filiacion no acreditada.

* **Segunda pregunta — V1 (Acuerdo):**
  "Respecto del otro progenitor:
  1. Existe acuerdo entre ambos sobre las medidas relativas a los hijos
  2. No existe acuerdo"

* **Tercera pregunta — V3 (Medidas):**
  "Las medidas que necesita fijar son:
  1. El conjunto completo: guarda y custodia, regimen de estancias y pension de alimentos
  2. Solo alguna de ellas"

  → Solo si la respuesta es 2, formula esta sub-pregunta: "La medida que necesita fijar es:
  1. La guarda y custodia con su regimen de estancias
  2. La pension de alimentos"

* **Cuarta pregunta — V3-bis (Vivienda):**
  "Sobre la vivienda en que residen los hijos:
  1. Se solicita tambien que se atribuya su uso
  2. No es necesario pronunciarse sobre ella"

* **Quinta pregunta — V4 (Convivencia):**
  "La relacion entre ambos progenitores fue:
  1. Pareja de hecho inscrita en un registro
  2. Convivencia estable sin inscripcion en ningun registro
  3. Sin convivencia estable"

* **Sexta pregunta — V5 (Alcance, solo si V1 = 1):**
  "Necesita que preparemos:
  1. Solo el pacto de relaciones familiares
  2. El pacto y la demanda conjunta para presentarla en el Juzgado"

*(Si el usuario responde con el numero, interpreta la opcion correspondiente exactamente igual que si hubiera escrito la palabra.)*

**PRINCIPIO: Preguntas simples, no mega-preguntas.** Cada pregunta resuelve un unico punto de decision. No comprimas V3 y V3-bis en una sola pregunta, ni ofrezcas las cuatro medidas posibles en una unica lista: la vivienda se pregunta siempre aparte porque es la decision de regimen mas distinto y la que el cliente peor entiende.

**Alcance de las alternativas numeradas:** son exclusivas de estas preguntas de clasificacion. Las preguntas de relleno del Punto 5 (nombres, domicilios, importes, fechas, calendarios) se formulan en prosa natural y el usuario responde con texto libre.

### Enrutamiento de Estado (Routing)

Una vez resueltos los vectores aplicables, evalua **en este orden**:

- Si **V2 = no consta la filiacion respecto del otro progenitor** (o no ha podido acreditarse) → **DETENER. No crear ningun documento y no pedir ningun otro dato.** Emite el texto fijo del Guardrail 1 y ofrece escalacion. Sin filiacion determinada no existe patria potestad del otro progenitor, ni deber de alimentos exigible frente a el (arts. 143.2.º y 154 CC), ni sujeto pasivo de las medidas: el proceso previo y necesario es el de determinacion de la filiacion (art. 748.2.º LEC), que esta skill no cubre.
- Si en cualquier momento aparecen indicios de violencia de genero o domestica → **DETENER** (Guardrail 3). No crear documento.
- Si **V1 = existe acuerdo** → **HOJA ACUERDO**: `assets/pacto-relaciones-familiares.md`. Si ademas V5 = 2, se genera despues `assets/demanda-medidas-paternofiliales.md` con los bloques condicionales de acuerdo ACTIVADOS y los de contencioso DESACTIVADOS.
- Si **V1 = no existe acuerdo** → **HOJA CONTENCIOSA**: `assets/demanda-medidas-paternofiliales.md` con los bloques condicionales de contencioso ACTIVADOS (intento de MASC, situacion economica de la regla 1.ª del art. 770, apartado de medidas solicitadas, otrosies de prueba y de medidas provisionales) y los de acuerdo DESACTIVADOS. No se genera pacto de relaciones familiares: es propio de la via de acuerdo.
- V3 y V3-bis no eligen asset: activan o desactivan los bloques de custodia y estancias, de alimentos y de vivienda dentro de la hoja ya elegida.
- V4 no elige asset: activa una de las tres variantes del expositivo de convivencia y, solo si V4 = 1, el Documento nº 2 con la certificacion del registro de parejas de hecho.
- Si lo que se pretende es **modificar medidas ya fijadas** en sentencia o en un acuerdo aprobado judicialmente → **DETENER esta via** y derivar a `derecho-civil-modificacion-medidas`, explicando que lo que procede es una demanda de modificacion de medidas y no la fijacion por primera vez.
- Si los progenitores **estan o han estado casados entre si** → **DETENER esta via** y derivar a `derecho-civil-divorcio`.
- Si lo que se reclama son **pensiones ya fijadas e impagadas** → **DETENER esta via** y derivar a `derecho-civil-ejecucion-titulos`.
- Si se pretende la **determinacion o impugnacion de la filiacion**, el **traslado internacional del menor** o medidas de proteccion frente a un **riesgo actual** para el menor → **DETENER** y escalar (ver tabla de Escalacion).

### Validacion de presupuestos (interno, antes del Punto 3)

- **Minoria de edad de los hijos (art. 748.4.º LEC):** el proceso versa sobre hijos MENORES. Si todos los hijos son ya mayores de edad, esta via no procede: los alimentos del hijo mayor se reclaman por el cauce que corresponda y la guarda y custodia carece de objeto. Advertir y escalar. Si hay hijos menores y ademas hijos mayores sin ingresos que convivan, incluir solo a los menores en las medidas y advertir de que los alimentos del mayor tienen fundamento distinto (art. 93, parrafo 2.º, CC) y conviene revision por especialista.
- **Objeto exclusivo (art. 748.4.º LEC):** el proceso debe versar **exclusivamente** sobre guarda, custodia y alimentos de los hijos menores. Si el usuario quiere acumular la division de un inmueble comun, una reclamacion de cantidad entre los progenitores o cualquier pretension patrimonial entre ellos, separarla expresamente: advertir de que no cabe en este procedimiento y ofrecer la via propia o la escalacion. La atribucion del uso de la vivienda en que residen los hijos si se admite en la practica cuando se funda en el interes del menor: se recoge con la advertencia de la seccion correspondiente.
- **Pension compensatoria:** si el usuario la pide, **rechazar la instruccion** y explicar que el art. 97 CC es privativo del matrimonio y no cabe en este procedimiento. No incluirla en ningun documento. Si alega un desequilibrio economico grave derivado de la convivencia, ofrecer escalacion: es una pretension distinta y de fundamento propio.
- **MASC (art. 5.2 LO 1/2025) — solo en la HOJA CONTENCIOSA:** es requisito de procedibilidad. La guarda, la custodia y los alimentos de hijos menores **no** figuran entre las materias exceptuadas de las letras a) a h) del art. 5.2. Verificar si se intento; si no se intento y no concurre imposibilidad, advertir formalmente del riesgo de inadmision antes de continuar. En la HOJA ACUERDO no se pregunta por el MASC: no hay controversia que negociar.
- **Fecha de efectos de los alimentos (art. 148 CC):** los alimentos no se abonan sino desde la interposicion de la demanda. Si el usuario pide mensualidades anteriores, advertirle de que por esta via no se obtienen y no incluir retroactividad en la medida.
- **Cuenta de abono:** si el importe de la pension se fija sin cuenta de abono o sin dia de pago, la medida es dificilmente ejecutable. No cerrar la seccion de alimentos sin ambos datos, o dejarlos con su placeholder propio y advertirlo.
- **Custodia compartida sin acuerdo (art. 92.5 y 92.8 CC):** si V1 = no existe acuerdo y el usuario pide custodia compartida, advertir de que a instancia de una sola parte es excepcional (art. 92.8) y exige informe del Ministerio Fiscal y una fundamentacion en que solo asi se protege el interes del menor. No prometer su concesion.

## 2. VERIFICACION Y AUTO-ACTUALIZACION NORMATIVA (Interno, OBLIGATORIO antes de redactar)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar.

**2.1 — Leer la version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" del Codigo Civil, de la LEC, de la LO 1/2025, de la LOPJ y de la LO 1/2004, asi como el estado registrado de la herramienta del CGPJ.

**2.2 — Consultar la fuente oficial vigente.** La API de legislacion consolidada del BOE devuelve el bloque de un articulo concreto (requiere cabecera `Accept: application/xml`). **La redaccion vigente es la ULTIMA `<version>` del bloque:** si se toma la primera, se cita una redaccion derogada.

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{numero}
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a{numero}
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1985-12666/texto/bloque/{id_ordinal_en_letras}
```

Consultar del Codigo Civil (BOE-A-1889-4763) los bloques `art92`, `art93`, `art94`, `art96`, `art142`, `art143`, `art146`, `art148`, `art152`, `art154` y `art156`; de la LEC (BOE-A-2000-323) los bloques `a748`, `a749`, `a769`, `a770`, `a777` y `a264`; el art. 5 de la LO 1/2025 (BOE-A-2025-76), bloque `a5`. **La LOPJ (BOE-A-1985-12666) NO numera sus bloques con cifras: el art. 89 es el bloque `aochentaynueve` y el suprimido art. 87 ter es `aochentaysieteter`; `a89` devuelve 404.** Consultar ambos: el primero para confirmar los apartados 6, 7 y 9 del art. 89 (competencia de la Seccion de Violencia sobre la Mujer y prohibicion de los MASC) y el segundo para confirmar que sigue constando "(Suprimido)". Verificar ademas la URL de las tablas orientadoras del CGPJ (https://www.poderjudicial.es/cgpj/es/Servicios/Utilidades/Calculo-de-pensiones-alimenticias/) y si el apartado sigue constando en revision.

**2.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar `Write`/`Edit` para:
- Actualizar `references/cc-medidas-hijos-no-matrimoniales.md` y/o `references/lec-proceso-medidas-paternofiliales.md` con la redaccion vigente.
- Actualizar los assets afectados si cambia la estructura legal de los documentos o la cita de un articulo.
- Actualizar la tabla "Version registrada", la tabla de articulos verificados y las fechas de `references/fuentes-plantillas-validadas.md`, incluido el estado verificado de la herramienta del CGPJ.
- Informar brevemente al usuario de la norma y fecha detectadas.

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**2.5 — Fallback si la fuente no es accesible.** Si la lectura falla (error HTTP, timeout):
```
web_search("Codigo Civil articulos 154 156 92 93 94 148 texto consolidado BOE")
web_search("LEC articulo 748 769 770 medidas paternofiliales guarda custodia alimentos texto consolidado BOE")
web_search("tablas orientadoras pensiones alimenticias CGPJ")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente del Codigo Civil y de la Ley de Enjuiciamiento Civil en el BOE. El documento se genera con la version de referencia. Verifique manualmente antes de firmarlo o presentarlo."

**Prohibido dar por vigente lo que no se ha podido verificar.** Los puntos ya registrados como pendientes de verificacion manual en `references/fuentes-plantillas-validadas.md` (aplicacion de los arts. 770, 777 y 96 a supuestos no matrimoniales) se tratan siempre en los terminos alli fijados: cauce habitual o criterio analogico, nunca remision legal expresa.

## 3. CONFIRMACION (visible al usuario)

Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la via y la fuente aplicable.** Textos fijos por hoja:
   - **HOJA ACUERDO:** "A su caso corresponde un pacto de relaciones familiares que regule las medidas relativas a sus hijos comunes, conforme a los articulos 154, 156, 92, 93, 94, 142, 146 y 148 del Codigo Civil, y que se somete a la aprobacion judicial en el proceso previsto en el articulo 748.4.º de la Ley 1/2000, de Enjuiciamiento Civil, por el cauce de su articulo 777. Al existir hijos menores de edad, la intervencion del Ministerio Fiscal es preceptiva y este informara sobre los terminos del pacto que les afecten (articulo 749.2 de la Ley de Enjuiciamiento Civil). Le advierto de que el pacto no queda aprobado por el hecho de firmarse ni de presentarse: hasta que lo apruebe el Juzgado por sentencia carece de fuerza ejecutiva. Puede consultar los textos oficiales en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - **HOJA CONTENCIOSA:** "A su caso corresponde una demanda de medidas paternofiliales en el proceso del articulo 748.4.º de la Ley 1/2000, de Enjuiciamiento Civil, que se sustancia por los tramites del juicio verbal conforme a su articulo 770, siendo competente el Juzgado que determina su articulo 769.3. Las medidas se fundan en los articulos 154, 156, 92, 93, 94, 142, 146 y 148 del Codigo Civil. Al existir hijos menores de edad, la intervencion del Ministerio Fiscal es preceptiva (articulo 749.2 de la Ley de Enjuiciamiento Civil). Debe acreditarse el intento previo de un medio adecuado de solucion de controversias: sin ese requisito la demanda puede ser inadmitida (articulo 5 de la Ley Organica 1/2025 y articulo 264.4.º de la Ley de Enjuiciamiento Civil). Puede consultar los textos oficiales en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763, https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 y https://www.boe.es/buscar/act.php?id=BOE-A-2025-76"
   - **En ambas hojas, anadir:** "Le confirmo que el hecho de que ustedes no hayan estado casados no altera en nada los derechos de sus hijos ni los deberes de ambos progenitores: se fija exactamente lo mismo que se fijaria en un divorcio en cuanto a los hijos. Lo unico que no existe aqui es el vinculo matrimonial y, con el, ni regimen economico matrimonial que liquidar ni pension compensatoria."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio. Si el documento adjuntado contiene clausulas de contenido matrimonial (liquidacion de gananciales, pension compensatoria, cargas del matrimonio), advierteselo expresamente: es sintoma de que se ha reutilizado un convenio regulador de divorcio y esas clausulas no proceden.

## 4. CREACION DEL DOCUMENTO BASE (Cero Vacios)

Inmediatamente tras la Confirmacion (Punto 3), estas OBLIGADO a crear el documento:

1. Utiliza `Read` para leer el documento base decidido (el asset de la hoja, o el que adjunto el usuario).
2. Reemplaza en memoria TODOS los datos que ya poseas (vectores, escucha activa e investigacion: incluida `fecha_verificacion_normativa` del Punto 2) y resuelve los bloques condicionales segun los vectores ya conocidos (V1, V3, V3-bis, V4). Los datos faltantes conservan el nombre propio del placeholder del asset (p. ej. `{{fecha_cese_convivencia}}`, `{{importe_alimentos}}`); no los sustituyas todos por un mismo marcador generico, porque `Edit` necesita un `oldString` unico para localizar cada dato por separado.
3. Resuelve los comentarios HTML: **el documento escrito en disco lleva CERO comentarios `<!-- ... -->`.** Si el bloque procede segun los vectores, se inserta como linea propia sin el envoltorio de comentario, conservando sus placeholders; si no procede o depende de un dato aun desconocido, se omite entero y se insertara en el Punto 5 releyendo el asset.
4. Utiliza `Write` para guardar el archivo en disco, con nombre en `snake_case.md` (ej. `pacto_relaciones_familiares_progenitor_a.md`, `demanda_medidas_paternofiliales_progenitor_a.md`).
5. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. En esa MISMA respuesta, sin turno intermedio y sin preguntar si desea empezar, emite el anuncio fijo de la primera seccion y formula ya su primera pregunta, para que el flujo no se detenga (regla del `CLAUDE.md` raiz, seccion 6.1, punto 5, y coherencia con el Punto 0: la skill esta en ejecucion desde que se carga).

**Orden cuando el alcance incluye pacto y demanda (V5 = 2):** crea y completa PRIMERO el pacto de relaciones familiares (lista 5-A entera). Solo cuando el pacto quede cerrado, crea la demanda conjunta (que se remite al pacto) y completa su lista 5-B, reutilizando sin volver a preguntar todos los datos ya recogidos.

### Resolucion de la numeracion dinamica (OBLIGATORIO, no dejar ningun marcador sin resolver)

Los assets numeran con placeholders todo ordinal que dependa de un bloque condicional, para que la activacion o desactivacion de un bloque no deje saltos en la numeracion. Reglas de resolucion:

- **Pactos del pacto de relaciones familiares** (`{{numero_pacto_patria_potestad}}`, `{{numero_pacto_custodia}}`, `{{numero_pacto_estancias}}`, `{{numero_pacto_alimentos}}`, `{{numero_pacto_vivienda}}`, `{{numero_pacto_sometimiento}}`): se resuelven como el ordinal en letras (PRIMERO, SEGUNDO, TERCERO...) que corresponda a la posicion real de ese pacto **entre los que estan efectivamente presentes en el documento**. La patria potestad es siempre el primero; la custodia y las estancias solo cuentan si V3 las incluye; los alimentos solo si V3 los incluye; la vivienda solo si V3-bis = 1; el sometimiento a aprobacion judicial es siempre el ultimo.
- **Hechos de la demanda** (`{{ordinal_hecho_economica}}`, `{{ordinal_hecho_medidas}}`): PRIMERO, SEGUNDO y TERCERO son fijos y estan siempre presentes; el CUARTO es fijo en cada rama (pacto alcanzado en la HOJA ACUERDO, intento de MASC en la HOJA CONTENCIOSA). Los siguientes se resuelven contando los hechos realmente escritos.
- **Fundamentos de derecho** (`{{ordinal_fundamento_fondo}}`, `{{ordinal_fundamento_interes_menor}}`, `{{ordinal_fundamento_fiscal}}`, `{{ordinal_fundamento_audiencia}}`, `{{ordinal_fundamento_costas}}`): I y II son fijos; el III existe solo en la HOJA CONTENCIOSA (requisito de procedibilidad). En la HOJA ACUERDO, por tanto, el fondo es el III; en la HOJA CONTENCIOSA, el IV. Se resuelven en numeracion romana contando los fundamentos realmente escritos.
- **Documentos** (`{{numero_documento_pacto}}`, `{{numero_documento_masc}}`, `{{numero_documento_economicos}}`): el Documento nº 1 es siempre la certificacion literal de nacimiento; el nº 2 existe solo si V4 = 1 (certificacion del registro de parejas de hecho). Los demas se numeran correlativamente segun los que realmente se acompanen.
- **Medidas solicitadas** (`{{numero_medida_patria_potestad}}`, `{{numero_medida_custodia}}`, `{{numero_medida_estancias}}`, `{{numero_medida_alimentos}}`, `{{numero_medida_vivienda}}`): numeracion arabe correlativa entre las medidas efectivamente solicitadas segun V3 y V3-bis.
- **Advertencia final de violencia** (`{{numero_advertencia_violencia}}`): es siempre la ultima de la lista de advertencias; se resuelve como el numero que le corresponda segun cuantas advertencias condicionales se hayan activado.

Como las secciones del Punto 5 se recorren en el orden fijo de sus listas, al llegar al turno de cada bloque ya se sabe cuantos lo preceden: resuelve el marcador en ese momento y no renumeres lo ya escrito.

## 5. EDICION INCREMENTAL DE SECCIONES

Recorre secuencialmente la lista que corresponda al documento activo (5-A pacto, 5-B demanda conjunta, 5-C demanda contenciosa). Por cada seccion incompleta, aplica el Ciclo de Edicion Incremental Global (Formular Pregunta → Mostrar Vista Previa en texto plano → Pedir Confirmacion → Tras confirmacion, usar `Edit` en disco y verificar con `Read`).

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. No pidas permiso para pasar de seccion: informa y continua. Los anuncios nombran la seccion SUSTANTIVA del documento, nunca la mecanica interna.

**Un dato por turno.** Si un punto agrupa varios datos, pidelos en turnos separados, uno por sub-apartado.

**Confirmacion agrupada por parte (datos identificativos):** los datos puramente identificativos de una misma persona (nombre, documento de identidad y domicilio de un progenitor; nombre y fecha de nacimiento de un hijo) se preguntan igualmente uno por turno, pero SIN vista previa ni `Edit` tras cada uno: acumulalos en memoria. **Solo tras RECIBIR la respuesta al ultimo dato de esa parte —nunca en el mismo turno en que aun se esta preguntando ese ultimo dato— muestra, ya en el turno siguiente, una unica vista previa con todos sus datos juntos y pide una unica confirmacion conjunta antes de aplicar el `Edit` que los vuelca todos a la vez.** Esta excepcion es exclusiva de datos identificativos objetivos.

**Marcas de cada seccion.** Cada punto de las listas esta marcado como *[dato objetivo]* o *[negociacion]*:
- *[dato objetivo]*: se registra el valor, con validacion de sentido.
- *[negociacion]*: implica una decision con consecuencias legales. **PRIMERO explica en el chat, de forma breve y con base en `references/cc-medidas-hijos-no-matrimoniales.md`, el regimen legal por defecto y las consecuencias de cada opcion; DESPUES formula la pregunta.** Confirma que el cliente entiende y esta de acuerdo antes de escribir. Estas secciones se confirman **una por una**, sin agrupacion.

**Validacion de sentido, no solo de formato:** razona si cada respuesta tiene sentido en el contexto. Una fecha de nacimiento futura, un DNI con forma de nombre, una pension de 5 euros al mes o un regimen de estancias imposible de cumplir no se escriben en el documento: senala por que no encaja y pide aclaracion antes de continuar.

**Datos de menores:** de cada hijo se piden **unicamente el nombre y la fecha de nacimiento**. No preguntes ni escribas centro escolar, direccion del menor, datos de salud, ni ningun otro dato del menor, aunque el usuario los ofrezca espontaneamente. Si los ofrece, no los incorpores al documento.

### 5-A. Pacto de relaciones familiares (`pacto-relaciones-familiares.md`)

1. **Progenitores** *[dato objetivo — confirmacion agrupada por parte]*. Anuncio de apertura: "Comenzamos por la identificacion de ambos progenitores." Sub-apartados, uno por turno: (a) nombre completo del primer progenitor; (b) su DNI o NIE; (c) su domicilio actual → confirmacion agrupada del primer progenitor. Anuncio: "Identificado el primer progenitor, pasamos a los datos del otro." (d) nombre completo del segundo progenitor; (e) su DNI o NIE; (f) su domicilio actual → confirmacion agrupada del segundo progenitor.
2. **Hijos comunes** *[dato objetivo — confirmacion agrupada del bloque]*. Anuncio: "Corresponde ahora identificar a los hijos comunes." Por cada hijo, nombre y fecha de nacimiento, un hijo por turno. Solo esos dos datos. Confirmacion agrupada de todos los hijos al terminar.
3. **Convivencia y su cese** *[dato objetivo]*. Anuncio: "Recogemos ahora los datos de la convivencia y de su cese, que se hacen constar unicamente como antecedente." V4 ya esta resuelto: no lo vuelvas a preguntar. Si V4 = 1, en turnos separados: (a) registro de parejas de hecho en que constaba la inscripcion; (b) fecha de la inscripcion; (c) fecha del cese de la convivencia. Si V4 = 2: (a) fecha aproximada de inicio de la convivencia; (b) fecha del cese. Si V4 = 3, la variante del expositivo se resuelve sola: no preguntes nada y pasa a la seccion siguiente.
4. **Patria potestad y su ejercicio** *[negociacion]*. Anuncio: "Pasamos a la primera de las medidas: el ejercicio de la patria potestad." Explica antes de preguntar: la patria potestad corresponde a ambos progenitores por el hecho de la filiacion y su ejercicio conjunto es la regla (art. 156 CC), **con independencia de a quien se atribuya la custodia**: son dos cosas distintas. Advierte del matiz del parrafo final del art. 156 CC: viviendo los progenitores separados, la ley preve que la ejerza aquel con quien el hijo conviva, salvo atribucion judicial del ejercicio conjunto, **por lo que conviene pactarlo expresamente**. Enumera las decisiones que requieren el acuerdo de ambos, y en particular el cambio del lugar de residencia habitual del menor (art. 154.3.º CC), y explica que los desacuerdos se resuelven por la via del art. 156 CC. Despues pregunta, en turnos separados: (a) si desea anadir alguna decision concreta a la lista de las que requeriran acuerdo de ambos; (b) la via de comunicacion que pactan entre progenitores para los asuntos de los hijos.
5. **Guarda y custodia** *[negociacion — solo si V3 incluye custodia]*. Anuncio: "Corresponde ahora determinar la guarda y custodia de los hijos." Explica antes de preguntar: no hay preferencia legal automatica; la compartida requiere el acuerdo de ambos (art. 92.5 CC) y que exista una comunicacion minima entre los progenitores, que el juez valora expresamente (art. 92.6 CC); la exclusiva atribuye la convivencia a un progenitor y el otro conserva la patria potestad y un regimen de estancias (art. 94 CC). El criterio decisivo es el interes superior del menor (art. 92.2 CC), y el vinculo que unio a los progenitores es irrelevante para los derechos del hijo. Despues pregunta la modalidad acordada.
6. **Regimen de estancias, comunicacion y vacaciones** *[negociacion — solo si V3 incluye custodia]*. Anuncio: "Fijada la custodia, corresponde concretar el regimen de estancias y comunicacion." Explica antes de preguntar: la concrecion es lo que evita futuros conflictos y ejecuciones; un regimen "amplio y flexible" garantiza un incidente. Pide dias concretos, horas de inicio y fin, y a quien corresponde cada periodo en los anos pares y en los impares. Despues, en turnos separados: (a) calendario ordinario de estancias; (b) reparto de las vacaciones escolares; (c) lugar de entregas y recogidas y quien recoge y quien entrega; (d) regimen de comunicacion telefonica o telematica con el progenitor con el que el hijo no se encuentre.
7. **Pension de alimentos** *[negociacion — solo si V3 incluye alimentos]*. Anuncio: "Pasamos a la pension de alimentos de los hijos." Explica antes de preguntar: el deber de alimentos deriva de la filiacion y existe igual sin matrimonio (art. 143.2.º CC); la cuantia es proporcionada al caudal o medios de quien los da y a las necesidades de quien los recibe (art. 146 CC), sin tarifa legal; las tablas orientadoras del CGPJ pueden servir de referencia no vinculante (https://www.poderjudicial.es/cgpj/es/Servicios/Utilidades/Calculo-de-pensiones-alimenticias/) **y, mientras el estado verificado en el Punto 2 siga siendo el de revision, adviertelo expresamente para no remitir al cliente a una herramienta que no esta operativa**; la pension cubre los gastos ordinarios y previsibles, mientras los extraordinarios son los imprevisibles y no periodicos, que suelen repartirse al 50 % con comunicacion y justificacion previas y acuerdo previo si no son urgentes; conviene la actualizacion anual para que la pension no se degrade; y **la pension de los hijos menores no es renunciable ni negociable a la baja hasta hacerla irrisoria: un pacto asi es danoso para los hijos y no sera aprobado**. Si la custodia acordada es compartida, usa la variante del asset prevista para ella (contribucion de ambos a un fondo comun o compensacion por la diferencia de ingresos), no la de pago unidireccional. Despues, en turnos separados: (a) importe mensual por hijo, o forma de contribucion si la custodia es compartida; (b) dia de pago y cuenta de abono; (c) criterio de actualizacion anual; (d) porcentaje de reparto de los gastos extraordinarios. Confirmacion propia de cada uno.
8. **Uso de la vivienda en que residen los hijos** *[negociacion — solo si V3-bis = 1]*. Anuncio: "Corresponde ahora la atribucion del uso de la vivienda en que residen los hijos." **Explica antes de preguntar, y hazlo con detalle porque es el punto que mas confunde al cliente:** aqui no hay regimen economico matrimonial que liquidar; el art. 96 CC, que en los divorcios atribuye el uso al progenitor custodio, esta redactado para los conyuges y para los supuestos de nulidad, separacion y divorcio, de modo que **no se aplica de forma directa**. Sin matrimonio, la vivienda se rige por las reglas ordinarias de la propiedad y de los contratos: si es privativa de un progenitor, es suya; si es de ambos en proindiviso, cualquiera puede pedir la division; si es de alquiler, por el contrato. Lo que si opera es el interes del menor, cuya necesidad de habitacion forma parte de los alimentos (art. 142 CC), y por esa via se invoca el criterio del art. 96.1 **por analogia**. Nunca afirmes que el progenitor no titular tiene derecho al uso por el solo hecho de tener la custodia. Si la vivienda es propiedad exclusiva del otro progenitor, advierte expresamente de que la atribucion es una limitacion de la facultad dispositiva del titular, de resultado incierto, y ofrece escalacion antes de redactar la medida; pon sobre la mesa las alternativas: plazo cerrado en lugar de indefinido, compensacion economica al titular, cuantificar la habitacion dentro de la pension, o venta o extincion del condominio si el inmueble es comun. Despues, en turnos separados: (a) direccion de la vivienda; (b) titularidad real; (c) a quien se atribuye el uso; (d) plazo o condicion de cese; (e) reparto de los gastos derivados de la vivienda.
9. **Cierre del pacto** *[dato objetivo]*. Anuncio: "Cerramos el pacto con el lugar y la fecha de firma." Pregunta lugar y fecha de firma. La clausula de sometimiento a la aprobacion judicial se resuelve sola: no la preguntes.

### 5-B. Demanda conjunta de mutuo acuerdo (`demanda-medidas-paternofiliales.md`, solo si V5 = 2)

Al crearla, vuelca sin volver a preguntar todos los datos ya recogidos en 5-A (progenitores, hijos, convivencia, fecha y lugar del pacto). Secciones pendientes:

1. **Juzgado competente** *[dato objetivo con explicacion]*. Anuncio: "Pasamos a la demanda: en primer lugar, el Juzgado competente." Explica la regla del art. 769.3 LEC: es competente el Juzgado de Primera Instancia del ultimo domicilio comun de los progenitores y, si residen en distintos partidos judiciales, a eleccion del demandante, el del domicilio del demandado o el de la residencia del menor; el tribunal lo examina de oficio y no cabe pactar otro fuero (art. 769.4 LEC). Pregunta el partido judicial y el criterio por el que resulta competente. Si nunca existio domicilio comun, adopta la posicion conservadora del de la residencia del menor y explicalo.
2. **Situacion actual de los hijos** *[dato objetivo con validacion]*. Anuncio: "Recogemos brevemente la situacion actual de los hijos." Pregunta con quien conviven los hijos en este momento y desde cuando. **No pidas ni escribas ningun otro dato del menor.**
3. **Representacion procesal** *[dato objetivo — confirmacion agrupada]*. Anuncio: "Corresponde identificar la representacion procesal." (a) nombre del procurador; (b) nombre del letrado → confirmacion agrupada. Si aun no estan designados, cada uno queda con su propio placeholder del asset.
4. **Costas y cierre** *[dato objetivo]*. Anuncio: "Cerramos la demanda con el pronunciamiento sobre costas, el lugar y la fecha." Explica que, presentandose de comun acuerdo, lo habitual es no interesar condena en costas, y pregunta si desea ese pronunciamiento. Despues, lugar y fecha. La relacion de documentos (certificaciones literales de nacimiento, certificacion del registro de parejas de hecho si V4 = 1, pacto firmado) se rellena sola segun la clasificacion: muestrala en la vista previa sin preguntar.

### 5-C. Demanda contenciosa de medidas paternofiliales (`demanda-medidas-paternofiliales.md`)

1. **Progenitor demandante** *[dato objetivo — confirmacion agrupada por parte]*. Anuncio de apertura: "Procedemos a la identificacion de la parte demandante." (a) nombre completo; (b) DNI o NIE; (c) domicilio → confirmacion agrupada.
2. **Progenitor demandado** *[dato objetivo — confirmacion agrupada por parte]*. Anuncio: "Identificada la parte demandante, pasamos a la parte demandada." (d) nombre completo; (e) DNI o NIE; (f) domicilio → confirmacion agrupada. Si se desconoce el domicilio, queda con su propio placeholder y afecta al MASC: se activa la declaracion responsable del art. 264.4.º LEC (ver seccion 4).
3. **Hijos comunes** *[dato objetivo — confirmacion agrupada del bloque]*. Anuncio: "Corresponde identificar a los hijos comunes." Nombre y fecha de nacimiento de cada hijo, uno por turno; solo esos dos datos; confirmacion agrupada. Con la fecha de nacimiento ya conocida, calcula tu mismo si algun hijo ha cumplido doce anos e informa de que en ese caso sera oido en todo caso (regla 4.ª del art. 770 LEC).
4. **Convivencia, cese e intento de solucion extrajudicial** *[dato objetivo con advertencia]*. Anuncio: "Pasamos a los hechos: el cese de la convivencia y el intento de solucion extrajudicial." Primero, segun V4, los datos de la convivencia y su cese (mismos sub-apartados que en 5-A.3). Despues explica el requisito de procedibilidad: el art. 5.2 de la LO 1/2025 exige acreditar el intento previo de un medio adecuado de solucion de controversias en estos procesos, sin que la guarda, la custodia y los alimentos figuren entre las materias exceptuadas, y sin ese requisito la demanda puede ser inadmitida. Aclara que basta la actividad negociadora desarrollada directamente por las partes o entre sus abogados, y que debe existir identidad entre el objeto negociado y el del pleito. Pregunta si se intento (si / no en la misma frase). Si si: tipo de MASC y fechas de inicio y fin, en turnos separados. Si no y se desconoce el domicilio del demandado o concurre otra imposibilidad: activa la declaracion responsable del art. 264.4.º LEC y pregunta el motivo. Si no y no concurre imposibilidad: advierte formalmente del riesgo de inadmision y recomienda intentarlo antes de presentar; si el cliente decide continuar, deja el bloque con su placeholder propio y la advertencia registrada.
5. **Riesgo de reconvencion** *[negociacion — informativo, no genera texto en el documento]*. Anuncio: "Antes de concretar las medidas, debo advertirle de un riesgo del procedimiento." Explica la regla 2.ª, letra d), del art. 770 LEC: la parte demandada puede reconvenir con la contestacion pidiendo medidas que no se han solicitado en la demanda —por ejemplo, la custodia compartida frente a una demanda que solo pide alimentos— y el actor dispone de 10 dias para contestarla. Pregunta si prevee que la otra parte formule esa pretension y, en caso afirmativo, si desea pedir ya en la demanda las medidas correspondientes en lugar de dejar que el debate lo abra la contraparte. Registra la decision para las secciones siguientes; si el cliente amplia las medidas solicitadas, actualiza V3 y activa los bloques correspondientes del asset.
6. **Situacion actual de los hijos** *[dato objetivo con validacion]*. Anuncio: "Recogemos la situacion actual de los hijos." Pregunta con quien conviven en este momento y desde cuando, y si el otro progenitor mantiene contacto y con que frecuencia de hecho. **No pidas ni escribas ningun otro dato del menor.**
7. **Patria potestad** *[negociacion]*. Anuncio: "Pasamos a la primera de las medidas que se solicitaran: el ejercicio de la patria potestad." Misma explicacion que en 5-A.4, con el matiz de que aqui se **solicita** el ejercicio conjunto y la enumeracion de decisiones que requeriran acuerdo de ambos. Pregunta si solicita el ejercicio conjunto y que decisiones desea que se reserven expresamente al acuerdo de ambos.
8. **Guarda, custodia y regimen de estancias solicitados** *[negociacion — solo si V3 incluye custodia]*. Anuncio: "Corresponde concretar la guarda y custodia y el regimen de estancias que se solicitaran." Misma explicacion que en 5-A.5 y 5-A.6, **anadiendo** que en la via contenciosa la custodia compartida a instancia de una sola parte es excepcional y exige informe del Ministerio Fiscal y una fundamentacion en que solo asi se protege adecuadamente el interes del menor (art. 92.8 CC): no prometas su concesion. Despues, en turnos separados: (a) modalidad de custodia que se solicita; (b) calendario de estancias propuesto; (c) reparto de vacaciones; (d) lugar de entregas y recogidas.
9. **Pension de alimentos solicitada** *[negociacion — solo si V3 incluye alimentos]*. Anuncio: "Pasamos a la pension de alimentos que se solicitara." Misma explicacion que en 5-A.7, **anadiendo** el art. 148 CC: los alimentos no se abonan sino desde la fecha de interposicion de la demanda, de modo que no cabe reclamar mensualidades anteriores por esta via y retrasar la presentacion tiene un coste economico. Despues, en turnos separados: (a) importe mensual por hijo que se solicita y su justificacion en los ingresos conocidos del otro progenitor; (b) dia de pago y cuenta de abono; (c) criterio de actualizacion; (d) reparto de gastos extraordinarios.
10. **Uso de la vivienda** *[negociacion — solo si V3-bis = 1]*. Anuncio: "Corresponde ahora la atribucion del uso de la vivienda en que residen los hijos." Misma explicacion completa que en 5-A.8, con la advertencia reforzada si la vivienda es propiedad exclusiva del otro progenitor. Despues, en turnos separados: (a) direccion; (b) titularidad y como se acredita; (c) atribucion que se solicita; (d) plazo o condicion.
11. **Documentacion economica** *[dato objetivo — solo si se solicitan alimentos o el uso de la vivienda]*. Anuncio: "Corresponde relacionar la documentacion economica que se acompanara." Explica la regla 1.ª del art. 770 LEC: **ambas partes** deben aportar los documentos de que dispongan que permitan evaluar la situacion economica (declaraciones tributarias, nominas, certificaciones bancarias, titulos de propiedad o certificaciones registrales). Pregunta, en turnos separados: (a) que documentos aportara; (b) una descripcion breve de sus ingresos y gastos y de los que conozca del otro progenitor.
12. **Medidas provisionales** *[negociacion]*. Anuncio: "Procede decidir si se interesan medidas que rijan mientras se sustancia el procedimiento." Explica: pueden pedirse en la propia demanda para que la custodia, las estancias y los alimentos rijan desde el principio y no solo desde la sentencia, presentandolo en los terminos verificados de la reference (cauce de los arts. 771 y 773 LEC aplicado por analogia a estos procesos, no por remision expresa). **Si el relato revela un riesgo actual para el menor, no lo encajes aqui: existe una via propia y distinta (art. 158 CC) y la posicion correcta es escalar.** Pregunta si se interesan (si / no); si si, se activa el OTROSI SEGUNDO en los mismos terminos de las medidas solicitadas.
13. **Juzgado, prueba, costas, representacion y cierre** *[dato objetivo; representacion con confirmacion agrupada]*. Anuncio: "Cerramos con el Juzgado competente, la prueba, las costas, la representacion procesal y la firma." (a) partido judicial y criterio de competencia (explicar el art. 769.3 LEC como en 5-B.1); (b) prueba adicional para el OTROSI PRIMERO, ademas del interrogatorio de la parte demandada y la documental (testifical, pericial psicosocial); (c) pronunciamiento que se interesa sobre costas; (d) nombre del procurador; (e) nombre del letrado → confirmacion agrupada de la representacion; (f) lugar y fecha.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: terminologia de progenitores y no de conyuges, "pacto de relaciones familiares" y no "convenio regulador", patria potestad distinguida de la guarda y custodia, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, medidas con concrecion ejecutable, pension desglosada y expresada en cifra y en letra, y SUPLICO ajustado a lo estrictamente pedido.

## BUCLE DE REALIMENTACION FINAL

Tras completar la lista del documento activo (y, si V5 = 2, tras completar AMBOS documentos), muestra el siguiente menu y espera instrucciones (aplicando `Edit` segun corresponda):
1. Ajustar una seccion existente.
2. Anadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.

Al cerrar, anade al final estas advertencias (adaptadas a la hoja):
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado colegiado antes de su firma o presentacion.
2. Version del Codigo Civil y de la Ley de Enjuiciamiento Civil verificada: fecha extraida en el Punto 2.
3. Al existir hijos menores, la intervencion del Ministerio Fiscal es preceptiva (articulo 749.2 de la Ley de Enjuiciamiento Civil) y ningun acuerdo danoso para los hijos sera aprobado.
4. La pension de alimentos no se abona sino desde la fecha de interposicion de la demanda (articulo 148 del Codigo Civil).
5. HOJA ACUERDO: el pacto no tiene fuerza ejecutiva hasta su aprobacion judicial; un pacto privado no aprobado exige un proceso declarativo previo para poder exigir su cumplimiento.
6. HOJA CONTENCIOSA: sin acreditar el intento de un medio adecuado de solucion de controversias la demanda puede ser inadmitida (articulo 5 de la Ley Organica 1/2025 y articulo 264.4.º de la Ley de Enjuiciamiento Civil); la parte demandada puede reconvenir pidiendo medidas no solicitadas (regla 2.ª, letra d, del articulo 770 de la Ley de Enjuiciamiento Civil); y los hijos que hayan cumplido doce anos seran oidos en todo caso (regla 4.ª del mismo articulo).

## Guardrails

1. **Filiacion no determinada → DETENER SIEMPRE, antes de pedir cualquier otro dato.** Si la filiacion no consta determinada respecto del otro progenitor, o no ha podido acreditarse, no se crea documento alguno. Texto fijo: "Antes de poder fijar cualquier medida es necesario que la filiacion de su hijo conste determinada respecto de ambos progenitores. Mientras no lo este, no existe patria potestad del otro progenitor, ni deber de alimentos exigible frente a el, ni parte contra la que dirigir estas medidas: el procedimiento previo y necesario es el de determinacion de la filiacion, que es distinto de este y que le corresponde llevar a un especialista. Le derivo para que se lo preparen." Ofrecer escalacion y no continuar el flujo.
2. Verificar siempre el Codigo Civil, la LEC, la LO 1/2025 y la LOPJ en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder. Si se detecta una version posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar.
3. **Violencia de genero o domestica → DETENER SIEMPRE**, en cualquier punto del flujo (clasificacion, verificacion, edicion incremental o conversacion libre), aunque los indicios aparezcan de pasada y aunque el usuario no los presente como un problema. Detener la generacion de inmediato, advertir y escalar via `escalate_to_attorney`: la competencia civil pasa a la Seccion de Violencia sobre la Mujer, que la tiene de forma exclusiva y excluyente concurriendo los requisitos legales, y que conoce expresamente de los procesos sobre guarda y custodia y alimentos y de las acciones derivadas de la crisis de la union de hecho (art. 89, apartados 6.a), 6.b), 6.e) y 7, LOPJ, en redaccion de la LO 1/2025, y art. 44 LO 1/2004); **esta vedada la utilizacion de los medios adecuados de solucion de controversias y de la mediacion (art. 89.9 LOPJ)**, por lo que no se propone ningun MASC ni mediacion; no procede la guarda conjunta (art. 92.7 CC) y no procede regimen de visitas o estancias en los supuestos del art. 94 CC. **PROHIBIDO citar el art. 87 ter LOPJ: fue suprimido por el art. 1.26 de la LO 1/2025.**
4. **La pension de alimentos de los hijos menores no es renunciable ni negociable a la baja hasta hacerla irrisoria.** Si el usuario pide un pacto sin pension, con pension simbolica, o una renuncia a reclamarla, rechazar la instruccion, explicar que es danoso para los hijos y que no sera aprobado, y proponer una alternativa valida. Un pacto que perjudique a los hijos no se escribe en el documento.
5. **De los menores se piden unicamente el nombre y la fecha de nacimiento.** No recabar ni consignar ningun otro dato de un menor (centro escolar, direccion, datos de salud, imagenes), aunque el usuario los aporte espontaneamente.
6. **Ningun pacto ni medida danosa para los hijos.** El interes superior del menor prevalece sobre cualquier acuerdo entre los progenitores (art. 92.2 CC). Un pacto danoso no sera aprobado por el Juzgado, y la skill no lo redacta: advierte y propone alternativa.
7. **La pension compensatoria del art. 97 CC no cabe en esta skill:** es privativa del matrimonio. Tampoco la liquidacion de un regimen economico matrimonial, que no existe, ni las cargas del matrimonio. Si el usuario los pide, explicar por que no procede y, si alega un desequilibrio economico grave derivado de la convivencia, ofrecer escalacion.
8. **No dar por automatica la atribucion del uso de la vivienda al progenitor custodio.** El art. 96 CC esta redactado para los conyuges: sin matrimonio se invoca por analogia y la atribucion depende de la titularidad del inmueble y del interes del menor. Si la vivienda es propiedad exclusiva del otro progenitor, advertir del resultado incierto y ofrecer escalacion antes de redactar la medida.
9. **La patria potestad no se confunde con la guarda y custodia.** Explicar siempre que la primera es de ambos progenitores y su ejercicio conjunto es la regla aunque la custodia sea exclusiva, y que hay decisiones que exigen el acuerdo de ambos, senaladamente el cambio de residencia habitual del menor (art. 154.3.º CC). Advertir del matiz del parrafo final del art. 156 CC y pactar o solicitar el ejercicio conjunto de forma expresa.
10. **En la via contenciosa, el MASC es requisito de procedibilidad** (art. 5.2 LO 1/2025; acreditacion del art. 264.4.º LEC). Advertirlo siempre. Nunca proponer un MASC si concurren indicios de violencia: en ese caso esta vedado (art. 89.9 LOPJ) y el flujo se detiene.
11. **Advertir siempre del riesgo de reconvencion** en la via contenciosa (regla 2.ª, letra d, del art. 770 LEC): quien es demandado puede pedir medidas no solicitadas en la demanda.
12. **No afirmar remisiones legales que no existen.** La aplicacion de los arts. 770 y 777 LEC a estos procesos y la del art. 96 CC a la vivienda se presentan como cauce habitual o criterio analogico, en los terminos registrados en `references/fuentes-plantillas-validadas.md`. Lo verificado con apoyo directo es el art. 748.4.º LEC (ambito), el art. 769.3 LEC (competencia) y el art. 749.2 LEC (Ministerio Fiscal).
13. Nunca inventar datos, importes, fechas, la existencia o identidad de hijos, ni jurisprudencia. Los campos no proporcionados conservan el nombre propio de su placeholder. Nunca afirmar que el pacto esta aprobado: solo lo aprueba el Juzgado por sentencia.
14. Si el impago de alimentos ya fijados alcanza dos meses consecutivos o cuatro no consecutivos, informar de la posible relevancia penal (art. 227 del Codigo Penal) y ofrecer escalacion a especialista en penal. Esta skill no redacta denuncia ni querella, ni ejecuta pensiones impagadas.

## Como NO se usa esta skill

- **No usar para fijar medidas por primera vez entre conyuges** o entre quienes lo han sido: eso es la separacion o el divorcio, con convenio regulador o demanda del art. 770 LEC. Derivar a `derecho-civil-divorcio`.
- **No usar para modificar medidas ya fijadas** en sentencia o en un acuerdo aprobado judicialmente, ni para extinguir una pension ya establecida: derivar a `derecho-civil-modificacion-medidas`.
- **No usar para la determinacion ni la impugnacion de la filiacion** (art. 748.2.º LEC): proceso distinto, en el que el Ministerio Fiscal es siempre parte (art. 749.1 LEC) y que esta exceptuado del requisito de MASC (art. 5.2.d) LO 1/2025). Es presupuesto de esta skill, no su objeto: si falta, detener (Guardrail 1) y escalar.
- **No usar para reclamar alimentos ya fijados e impagados:** eso es ejecucion forzosa. Derivar a `derecho-civil-ejecucion-titulos`.
- **No usar para el traslado internacional del menor** ni para la sustraccion internacional de menores: escalar.
- No usar para pretensiones patrimoniales entre los progenitores (division de un inmueble comun, reclamacion de cantidad, compensacion por la convivencia): el proceso del art. 748.4.º LEC versa **exclusivamente** sobre guarda, custodia y alimentos de los hijos menores. Separar la pretension y derivarla a su via propia o escalar.
- No usar cuando todos los hijos son ya mayores de edad: advertir y escalar.
- No usar cuando existan indicios de violencia de genero o domestica: detener y escalar (Guardrail 3).
- No usar si el usuario pide opinion juridica sobre la estrategia del pleito o sobre un conflicto familiar ya judicializado: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| Indicios de violencia de genero o domestica, actual o pasada, hacia el otro progenitor o hacia los hijos | DETENER SIEMPRE la generacion y escalar via `escalate_to_attorney` (art. 89, apartados 6, 7 y 9, LOPJ; art. 44 LO 1/2004; arts. 92.7 y 94 CC). Vedados los MASC y la mediacion. No citar el art. 87 ter, suprimido |
| Filiacion no determinada respecto del otro progenitor, o no acreditable | DETENER antes de pedir cualquier otro dato y escalar: el proceso previo es el de determinacion de la filiacion (Guardrail 1) |
| Riesgo actual para el menor (desatencion, situacion de peligro, temor a un traslado inminente) | No encajarlo en este flujo: existe la via propia del art. 158 CC, exceptuada del requisito de MASC. Escalar de inmediato |
| Traslado internacional del menor, residencia de un progenitor en el extranjero o riesgo de sustraccion | Escalar: excede el alcance de esta skill |
| Menores con discapacidad o en situacion de especial vulnerabilidad | Advertir de la intervencion reforzada del Ministerio Fiscal y ofrecer escalacion |
| Vivienda propiedad exclusiva del progenitor no custodio y peticion de atribucion de su uso | Advertir del resultado incierto y de que es una limitacion de la facultad dispositiva del titular; ofrecer escalacion antes de redactar la medida |
| Peticion de pension compensatoria o de compensacion economica por la convivencia | Explicar que no cabe en este procedimiento y ofrecer escalacion: pretension distinta y de fundamento propio |
| Custodia compartida solicitada por una sola parte en la via contenciosa | Advertir del caracter excepcional (art. 92.8 CC) y del informe preceptivo del fiscal; ofrecer escalacion si el caso es dudoso |
| Impago de alimentos ya fijados de dos meses consecutivos o cuatro no consecutivos | Informar de la posible relevancia penal (art. 227 CP) y ofrecer escalacion a especialista en penal |
| Caso sujeto a derecho civil autonomico (Cataluna, Aragon, Navarra, Pais Vasco, Baleares, Galicia) | Verificar la norma autonomica con `web_search` (en Cataluna, el plan de parentalidad del Libro II del Codigo civil de Cataluna) y advertir antes de redactar |
| Duda insalvable sobre el interes del menor o sobre la via aplicable | Adoptar la posicion mas conservadora y ofrecer escalacion |
| Litigio conexo ya iniciado, procedimiento penal en curso entre los progenitores o reconvencion ya anunciada | Escalar via `escalate_to_attorney` |
