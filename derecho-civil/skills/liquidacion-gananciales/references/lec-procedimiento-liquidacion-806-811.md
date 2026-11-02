# Procedimiento Judicial de Liquidación del Régimen Económico Matrimonial (arts. 806 a 811 LEC)

> Material de referencia para la skill `derecho-civil-liquidacion-gananciales`. Recoge el contenido de la LEC
> verificado en el BOE (BOE-A-2000-323) el 02/09/2026.
> **Los arts. 807, 808 y 810 están en la redacción de la LO 2/2022, de 21 de marzo (BOE-A-2022-4516), en vigor
> desde el 23/03/2022.** Redacción reciente: verificar estos tres bloques en cada lanzamiento de la skill.
> Fuente y versiones registradas en `references/fuentes-plantillas-validadas.md`.

---

## 1. Ámbito: el procedimiento es SUBSIDIARIO del acuerdo (art. 806 LEC)

**Literal verificado:**

> "La liquidación de cualquier régimen económico matrimonial que, por capitulaciones matrimoniales o por disposición legal, determine la existencia de una masa común de bienes y derechos sujeta a determinadas cargas y obligaciones se llevará a cabo, **en defecto de acuerdo entre los cónyuges**, con arreglo a lo dispuesto en el presente capítulo y a las normas civiles que resulten aplicables."

Dos consecuencias que gobiernan el árbol de decisión de la skill:

1. **"En defecto de acuerdo".** Si los cónyuges se ponen de acuerdo, no hay procedimiento: la liquidación se documenta en convenio (elevado a escritura pública si hay inmuebles, para su inscripción en el Registro de la Propiedad) o se integra en el convenio regulador del divorcio (art. 90.1.e) CC). El procedimiento de los arts. 807 a 810 es el cauce para cuando no hay acuerdo. De ahí que el vector del acuerdo sea el que enruta el asset.
2. **"Masa común de bienes y derechos sujeta a cargas".** Es el presupuesto material del procedimiento. **Un régimen de separación de bienes no determina ninguna masa común**: no hay nada que inventariar ni que liquidar, y este capítulo no le es aplicable. Si hay bienes adquiridos por ambos en proindiviso, eso es una comunidad ordinaria y su reparto es una división de cosa común (arts. 400 y ss. CC), no una liquidación de régimen.

---

## 2. Competencia (art. 807 LEC, redacción LO 2/2022)

**Literal verificado:**

> "Será competente para conocer del procedimiento de liquidación el Juzgado de Primera Instancia **o Juzgado de Violencia sobre la Mujer** que esté conociendo, o haya conocido o hubiera tenido la competencia para conocer del proceso de nulidad, separación o divorcio, o aquel ante el que se sigan o se hayan seguido las actuaciones sobre disolución del régimen económico matrimonial por alguna de las causas previstas en la legislación civil."

Claves:

- **Competencia funcional, no territorial elegible.** No hay elección de fuero ni sumisión posible: el juzgado es el del proceso matrimonial. La skill nunca pregunta al cliente "en que juzgado quiere presentarlo": pregunta qué juzgado conoció o está conociendo de su divorcio.
- Las tres modalidades cubren los tres momentos: el que **está conociendo** (proceso en curso), el que **ha conocido** (sentencia ya dictada) y el que **hubiera tenido la competencia** (supuestos en que no llego a tramitarse el proceso matrimonial ante ese juzgado).
- La mención del **Juzgado de Violencia sobre la Mujer** es la aportación de la LO 2/2022. Si el proceso matrimonial se siguió ante un Juzgado de Violencia sobre la Mujer, ese es el competente para la liquidación. En esos casos concurren, por definición, los presupuestos del Guardrail de violencia del plugin: la skill detiene y escala.

---

## 3. Fase primera: solicitud y formación de inventario (arts. 808 y 809 LEC)

### 3.1 La solicitud (art. 808 LEC, apartado 1 en redacción LO 2/2022)

**Literal verificado:**

> "1. Admitida la demanda de nulidad, separación o divorcio, o iniciado el proceso en que se haya demandado la disolución del régimen económico matrimonial, cualquiera de los cónyuges **o sus herederos**, podrá solicitar la formación de inventario.
> 2. La solicitud a que se refiere el apartado anterior deberá acompañarse de **una propuesta en la que, con la debida separación, se harán constar las diferentes partidas que deban incluirse en el inventario** con arreglo a la legislación civil.
> A la solicitud se acompañarán también **los documentos que justifiquen las diferentes partidas incluidas en la propuesta**."

Contenido legalmente exigido, que es la base del asset `solicitud-formacion-inventario.md` y de `propuesta-inventario.md`:

| Exigencia | Consecuencia en el documento |
|---|---|
| Legitimación: cualquiera de los cónyuges **o sus herederos** (novedad LO 2/2022) | El solicitante puede ser un heredero de un cónyuge fallecido; el asset debe admitir esa variante |
| Presupuesto temporal: demanda matrimonial **admitida**, o proceso de disolución **iniciado** | El escrito debe expresar el número de autos y el estado del proceso matrimonial |
| **Propuesta con la debida separación de partidas** | La propuesta no es una lista corrida de bienes: separa activo y pasivo y, dentro de cada uno, las partidas de los arts. 1397 y 1398 CC |
| Partidas **con arreglo a la legislación civil** | Las partidas se corresponden con las de los arts. 1397 y 1398 CC, no con categorías inventadas |
| **Documentos justificativos de cada partida** | Cada partida numerada de la propuesta lleva su documento; una partida sin documento es una debilidad procesal que hay que advertir al cliente |

**Clave que se pasa por alto con frecuencia: el inventario se puede pedir ANTES de la disolución.** El presupuesto del apartado 1 es la **admisión a trámite** de la demanda matrimonial, no la firmeza de la sentencia. Es decir: con el divorcio todavía en trámite, y por tanto con la sociedad de gananciales aún no disuelta (Art. 1392 CC), cualquiera de los cónyuges ya puede solicitar la formación de inventario. Lo que si exige que sea firme la resolución que declare disuelto el régimen es la **segunda fase**, la solicitud de liquidación del Art. 810.1 LEC. Consecuencias para la skill: (a) no decirle nunca al cliente que debe esperar a la sentencia para pedir el inventario; (b) no redactar en el escrito que la sociedad "quedó disuelta" cuando aún no lo está, sino que quedará disuelta al ponerse término al proceso; y (c) fijar en ese caso una fecha de referencia del inventario, no una fecha de corte definitiva, porque el activo lo determina el momento de la disolución (Art. 1397.1.º CC).

**Nota sobre el caso del divorcio ya firme:** el apartado 1 contempla literalmente la demanda matrimonial admitida y el proceso de disolución iniciado, **no menciona expresamente el supuesto de sentencia de divorcio ya firme**. Que ese caso se tramita por el mismo cauce se desprende del art. 807 (juzgado que "haya conocido") y del art. 810.1 ("una vez firme la resolución que declare disuelto el régimen"). Ver el punto 1 del apartado "Verificar manualmente" de `references/fuentes-plantillas-validadas.md`: posición conservadora, y advertir al cliente de que conviene confirmar el criterio del juzgado.

### 3.2 La formación del inventario (art. 809 LEC)

- El Letrado de la Administración de Justicia señala día y hora **en el plazo máximo de diez días** y cita a ambos cónyuges.
- En el acto se forma el inventario **sujetándose a la legislación civil del régimen de que se trate**.
- **Incomparecencia injustificada de un cónyuge: se le tiene por conforme con la propuesta de inventario del que compareció.** Consecuencia práctica de primer orden que hay que explicar al cliente: no acudir a esa comparecencia equivale a aceptar el inventario del otro. Y, en el otro sentido, es la razón por la que la propuesta debe estar bien construida desde el principio.
- Si hay acuerdo en el acto, se consigna en acta y se da por concluido. El mismo día o el siguiente el Tribunal resuelve sobre **administración y disposición de los bienes inventariados**.
- **Apartado 2 — inventario contradictorio:** si se suscita controversia sobre la inclusión o exclusión de algún concepto, o sobre el importe de cualquier partida, se cita a vista y **se continúa por los trámites del juicio verbal**. La **sentencia** resuelve todas las cuestiones, aprueba el inventario y dispone lo procedente sobre administración y disposición de los bienes comunes.

Aquí es donde se resuelve judicialmente la discusión sobre si un bien es privativo o ganancial, y donde opera la presunción del art. 1361 CC con su carga de la prueba.

---

## 4. Fase segunda: solicitud de liquidación (art. 810 LEC, redacción LO 2/2022)

**Contenido verificado:**

1. **Presupuesto:** concluido el inventario y, en su caso, **una vez firme la resolución que declare disuelto el régimen**, cualquiera de los cónyuges o, de haber fallecido, sus herederos, podrán solicitar la liquidación.
2. **Contenido de la propuesta de liquidación:** debe incluir **el pago de las indemnizaciones y reintegros debidos a cada cónyuge y la división del remanente en la proporción que corresponda**, teniendo en cuenta, en la formación de los lotes, **las preferencias que establezcan las normas civiles aplicables** (arts. 1403, 1404, 1406 y 1407 CC).
3. **Comparecencia:** el LAJ señala, **dentro del plazo máximo de diez días**, día y hora para que los cónyuges o sus herederos comparezcan al objeto de alcanzar acuerdo y, en su defecto, designar contador y, en su caso, peritos.
4. **Incomparecencia injustificada:** se tiene al ausente por conforme con la propuesta de liquidación del compareciente. El acuerdo se consigna en acta y **se lleva a efecto conforme a los dos primeros apartados del art. 788 LEC**.
5. **Sin acuerdo:** se procede por diligencia al **nombramiento de contador y, en su caso, peritos, conforme al art. 784 LEC**, continuando la tramitación con arreglo a los **arts. 785 y siguientes** (los de la división judicial de patrimonios).

**Estructura en dos fases: el dato que hay que explicar siempre al cliente.** El procedimiento no es un pleito, son dos: primero se fija QUÉ hay (inventario, con su posible juicio verbal y sentencia) y solo después se reparte (liquidación, con su posible contador, peritos y oposición). Cada fase tiene sus comparecencias, sus plazos y su posible contradicción. Los plazos de diez días del texto legal son los de señalamiento por el LAJ, no la duración del procedimiento: en la práctica cada fase se mide en meses. Esta es la razón de fondo por la que casi siempre conviene intentar el acuerdo antes: el resultado negociado se obtiene en semanas y el judicial puede tardar años, con dos fases, posibles recursos y el coste de contador y peritos a cargo de la masa.

---

## 5. Régimen de participación (art. 811 LEC): cauce distinto

**Contenido verificado:**

1. **No puede solicitarse la liquidación hasta que sea firme** la resolución que declare disuelto el régimen (a diferencia del inventario de gananciales, que puede pedirse con la demanda matrimonial ya admitida).
2. La propuesta debe incluir **una estimación del patrimonio inicial y final de cada cónyuge**, expresando la cantidad resultante a pagar por el cónyuge que haya experimentado un mayor incremento patrimonial.
3. Comparecencia señalada por el LAJ en plazo máximo de diez días para alcanzar acuerdo.
4. Incomparecencia injustificada: conformidad con la propuesta del compareciente.
5. Sin acuerdo: vista por los trámites del **juicio verbal** y sentencia que determina los patrimonios inicial y final de cada cónyuge, la cantidad que deba satisfacer el de mayor incremento y **la forma en que haya de hacerse el pago**.

**Diferencia estructural:** en el régimen de participación (arts. 1411 y ss. CC) **no hay masa común que inventariar**. Cada cónyuge tiene su propio patrimonio y lo que se liquida es un **derecho de crédito** a participar en las ganancias del otro. No hay activo y pasivo de una sociedad, no hay adjudicación de lotes, no hay división por mitad de un remanente: hay una comparación de patrimonio inicial y final de cada uno y un pago compensatorio. **Los assets de esta skill, construidos sobre los arts. 1397 a 1410 CC, no sirven para el art. 811 LEC.** Si el régimen es de participación, la skill detiene y escala.

---

## 6. Cuadro resumen de cauces

| Situación | Cauce | Documento |
|---|---|---|
| Gananciales, **con acuerdo** | Convenio de liquidación (art. 806 LEC a contrario); escritura pública si hay inmuebles; o cláusula del convenio regulador (art. 90.1.e) CC) | `assets/convenio-liquidacion-gananciales.md` |
| Gananciales, **sin acuerdo** | Arts. 807 a 810 LEC: solicitud de formación de inventario con su propuesta y, en su caso, posterior solicitud de liquidación | `assets/solicitud-formacion-inventario.md` + `assets/propuesta-inventario.md` |
| **Participación** | Art. 811 LEC: propuesta con estimación de patrimonio inicial y final | Fuera de alcance: detener y escalar |
| **Separación de bienes** | No hay masa común (art. 806 LEC): nada que liquidar. Si hay bienes en proindiviso, división de cosa común (arts. 400 y ss. CC) | Fuera de alcance: detener y explicar |
| Régimen de **derecho civil propio** (foral) | Norma autonómica aplicable | Fuera de alcance: verificar y escalar |
