# Procedimiento Judicial de Liquidacion del Regimen Economico Matrimonial (arts. 806 a 811 LEC)

> Material de referencia para la skill `derecho-civil-liquidacion-gananciales`. Recoge el contenido de la LEC
> verificado en el BOE (BOE-A-2000-323) el 02/09/2026.
> **Los arts. 807, 808 y 810 estan en la redaccion de la LO 2/2022, de 21 de marzo (BOE-A-2022-4516), en vigor
> desde el 23/03/2022.** Redaccion reciente: verificar estos tres bloques en cada lanzamiento de la skill.
> Fuente y versiones registradas en `references/fuentes-plantillas-validadas.md`.

---

## 1. Ambito: el procedimiento es SUBSIDIARIO del acuerdo (art. 806 LEC)

**Literal verificado:**

> "La liquidacion de cualquier regimen economico matrimonial que, por capitulaciones matrimoniales o por disposicion legal, determine la existencia de una masa comun de bienes y derechos sujeta a determinadas cargas y obligaciones se llevara a cabo, **en defecto de acuerdo entre los conyuges**, con arreglo a lo dispuesto en el presente capitulo y a las normas civiles que resulten aplicables."

Dos consecuencias que gobiernan el arbol de decision de la skill:

1. **"En defecto de acuerdo".** Si los conyuges se ponen de acuerdo, no hay procedimiento: la liquidacion se documenta en convenio (elevado a escritura publica si hay inmuebles, para su inscripcion en el Registro de la Propiedad) o se integra en el convenio regulador del divorcio (art. 90.1.e) CC). El procedimiento de los arts. 807 a 810 es el cauce para cuando no hay acuerdo. De ahi que el vector del acuerdo sea el que enruta el asset.
2. **"Masa comun de bienes y derechos sujeta a cargas".** Es el presupuesto material del procedimiento. **Un regimen de separacion de bienes no determina ninguna masa comun**: no hay nada que inventariar ni que liquidar, y este capitulo no le es aplicable. Si hay bienes adquiridos por ambos en proindiviso, eso es una comunidad ordinaria y su reparto es una division de cosa comun (arts. 400 y ss. CC), no una liquidacion de regimen.

---

## 2. Competencia (art. 807 LEC, redaccion LO 2/2022)

**Literal verificado:**

> "Sera competente para conocer del procedimiento de liquidacion el Juzgado de Primera Instancia **o Juzgado de Violencia sobre la Mujer** que este conociendo, o haya conocido o hubiera tenido la competencia para conocer del proceso de nulidad, separacion o divorcio, o aquel ante el que se sigan o se hayan seguido las actuaciones sobre disolucion del regimen economico matrimonial por alguna de las causas previstas en la legislacion civil."

Claves:

- **Competencia funcional, no territorial elegible.** No hay eleccion de fuero ni sumision posible: el juzgado es el del proceso matrimonial. La skill nunca pregunta al cliente "en que juzgado quiere presentarlo": pregunta que juzgado conocio o esta conociendo de su divorcio.
- Las tres modalidades cubren los tres momentos: el que **esta conociendo** (proceso en curso), el que **ha conocido** (sentencia ya dictada) y el que **hubiera tenido la competencia** (supuestos en que no llego a tramitarse el proceso matrimonial ante ese juzgado).
- La mencion del **Juzgado de Violencia sobre la Mujer** es la aportacion de la LO 2/2022. Si el proceso matrimonial se siguio ante un Juzgado de Violencia sobre la Mujer, ese es el competente para la liquidacion. En esos casos concurren, por definicion, los presupuestos del Guardrail de violencia del plugin: la skill detiene y escala.

---

## 3. Fase primera: solicitud y formacion de inventario (arts. 808 y 809 LEC)

### 3.1 La solicitud (art. 808 LEC, apartado 1 en redaccion LO 2/2022)

**Literal verificado:**

> "1. Admitida la demanda de nulidad, separacion o divorcio, o iniciado el proceso en que se haya demandado la disolucion del regimen economico matrimonial, cualquiera de los conyuges **o sus herederos**, podra solicitar la formacion de inventario.
> 2. La solicitud a que se refiere el apartado anterior debera acompanarse de **una propuesta en la que, con la debida separacion, se haran constar las diferentes partidas que deban incluirse en el inventario** con arreglo a la legislacion civil.
> A la solicitud se acompanaran tambien **los documentos que justifiquen las diferentes partidas incluidas en la propuesta**."

Contenido legalmente exigido, que es la base del asset `solicitud-formacion-inventario.md` y de `propuesta-inventario.md`:

| Exigencia | Consecuencia en el documento |
|---|---|
| Legitimacion: cualquiera de los conyuges **o sus herederos** (novedad LO 2/2022) | El solicitante puede ser un heredero de un conyuge fallecido; el asset debe admitir esa variante |
| Presupuesto temporal: demanda matrimonial **admitida**, o proceso de disolucion **iniciado** | El escrito debe expresar el numero de autos y el estado del proceso matrimonial |
| **Propuesta con la debida separacion de partidas** | La propuesta no es una lista corrida de bienes: separa activo y pasivo y, dentro de cada uno, las partidas de los arts. 1397 y 1398 CC |
| Partidas **con arreglo a la legislacion civil** | Las partidas se corresponden con las de los arts. 1397 y 1398 CC, no con categorias inventadas |
| **Documentos justificativos de cada partida** | Cada partida numerada de la propuesta lleva su documento; una partida sin documento es una debilidad procesal que hay que advertir al cliente |

**Clave que se pasa por alto con frecuencia: el inventario se puede pedir ANTES de la disolucion.** El presupuesto del apartado 1 es la **admision a tramite** de la demanda matrimonial, no la firmeza de la sentencia. Es decir: con el divorcio todavia en tramite, y por tanto con la sociedad de gananciales aun no disuelta (Art. 1392 CC), cualquiera de los conyuges ya puede solicitar la formacion de inventario. Lo que si exige que sea firme la resolucion que declare disuelto el regimen es la **segunda fase**, la solicitud de liquidacion del Art. 810.1 LEC. Consecuencias para la skill: (a) no decirle nunca al cliente que debe esperar a la sentencia para pedir el inventario; (b) no redactar en el escrito que la sociedad "quedo disuelta" cuando aun no lo esta, sino que quedara disuelta al ponerse termino al proceso; y (c) fijar en ese caso una fecha de referencia del inventario, no una fecha de corte definitiva, porque el activo lo determina el momento de la disolucion (Art. 1397.1.º CC).

**Nota sobre el caso del divorcio ya firme:** el apartado 1 contempla literalmente la demanda matrimonial admitida y el proceso de disolucion iniciado, **no menciona expresamente el supuesto de sentencia de divorcio ya firme**. Que ese caso se tramita por el mismo cauce se desprende del art. 807 (juzgado que "haya conocido") y del art. 810.1 ("una vez firme la resolucion que declare disuelto el regimen"). Ver el punto 1 del apartado "Verificar manualmente" de `references/fuentes-plantillas-validadas.md`: posicion conservadora, y advertir al cliente de que conviene confirmar el criterio del juzgado.

### 3.2 La formacion del inventario (art. 809 LEC)

- El Letrado de la Administracion de Justicia senala dia y hora **en el plazo maximo de diez dias** y cita a ambos conyuges.
- En el acto se forma el inventario **sujetandose a la legislacion civil del regimen de que se trate**.
- **Incomparecencia injustificada de un conyuge: se le tiene por conforme con la propuesta de inventario del que comparecio.** Consecuencia practica de primer orden que hay que explicar al cliente: no acudir a esa comparecencia equivale a aceptar el inventario del otro. Y, en el otro sentido, es la razon por la que la propuesta debe estar bien construida desde el principio.
- Si hay acuerdo en el acto, se consigna en acta y se da por concluido. El mismo dia o el siguiente el Tribunal resuelve sobre **administracion y disposicion de los bienes inventariados**.
- **Apartado 2 — inventario contradictorio:** si se suscita controversia sobre la inclusion o exclusion de algun concepto, o sobre el importe de cualquier partida, se cita a vista y **se continua por los tramites del juicio verbal**. La **sentencia** resuelve todas las cuestiones, aprueba el inventario y dispone lo procedente sobre administracion y disposicion de los bienes comunes.

Aqui es donde se resuelve judicialmente la discusion sobre si un bien es privativo o ganancial, y donde opera la presuncion del art. 1361 CC con su carga de la prueba.

---

## 4. Fase segunda: solicitud de liquidacion (art. 810 LEC, redaccion LO 2/2022)

**Contenido verificado:**

1. **Presupuesto:** concluido el inventario y, en su caso, **una vez firme la resolucion que declare disuelto el regimen**, cualquiera de los conyuges o, de haber fallecido, sus herederos, podran solicitar la liquidacion.
2. **Contenido de la propuesta de liquidacion:** debe incluir **el pago de las indemnizaciones y reintegros debidos a cada conyuge y la division del remanente en la proporcion que corresponda**, teniendo en cuenta, en la formacion de los lotes, **las preferencias que establezcan las normas civiles aplicables** (arts. 1403, 1404, 1406 y 1407 CC).
3. **Comparecencia:** el LAJ senala, **dentro del plazo maximo de diez dias**, dia y hora para que los conyuges o sus herederos comparezcan al objeto de alcanzar acuerdo y, en su defecto, designar contador y, en su caso, peritos.
4. **Incomparecencia injustificada:** se tiene al ausente por conforme con la propuesta de liquidacion del compareciente. El acuerdo se consigna en acta y **se lleva a efecto conforme a los dos primeros apartados del art. 788 LEC**.
5. **Sin acuerdo:** se procede por diligencia al **nombramiento de contador y, en su caso, peritos, conforme al art. 784 LEC**, continuando la tramitacion con arreglo a los **arts. 785 y siguientes** (los de la division judicial de patrimonios).

**Estructura en dos fases: el dato que hay que explicar siempre al cliente.** El procedimiento no es un pleito, son dos: primero se fija QUE hay (inventario, con su posible juicio verbal y sentencia) y solo despues se reparte (liquidacion, con su posible contador, peritos y oposicion). Cada fase tiene sus comparecencias, sus plazos y su posible contradiccion. Los plazos de diez dias del texto legal son los de senalamiento por el LAJ, no la duracion del procedimiento: en la practica cada fase se mide en meses. Esta es la razon de fondo por la que casi siempre conviene intentar el acuerdo antes: el resultado negociado se obtiene en semanas y el judicial puede tardar anos, con dos fases, posibles recursos y el coste de contador y peritos a cargo de la masa.

---

## 5. Regimen de participacion (art. 811 LEC): cauce distinto

**Contenido verificado:**

1. **No puede solicitarse la liquidacion hasta que sea firme** la resolucion que declare disuelto el regimen (a diferencia del inventario de gananciales, que puede pedirse con la demanda matrimonial ya admitida).
2. La propuesta debe incluir **una estimacion del patrimonio inicial y final de cada conyuge**, expresando la cantidad resultante a pagar por el conyuge que haya experimentado un mayor incremento patrimonial.
3. Comparecencia senalada por el LAJ en plazo maximo de diez dias para alcanzar acuerdo.
4. Incomparecencia injustificada: conformidad con la propuesta del compareciente.
5. Sin acuerdo: vista por los tramites del **juicio verbal** y sentencia que determina los patrimonios inicial y final de cada conyuge, la cantidad que deba satisfacer el de mayor incremento y **la forma en que haya de hacerse el pago**.

**Diferencia estructural:** en el regimen de participacion (arts. 1411 y ss. CC) **no hay masa comun que inventariar**. Cada conyuge tiene su propio patrimonio y lo que se liquida es un **derecho de credito** a participar en las ganancias del otro. No hay activo y pasivo de una sociedad, no hay adjudicacion de lotes, no hay division por mitad de un remanente: hay una comparacion de patrimonio inicial y final de cada uno y un pago compensatorio. **Los assets de esta skill, construidos sobre los arts. 1397 a 1410 CC, no sirven para el art. 811 LEC.** Si el regimen es de participacion, la skill detiene y escala.

---

## 6. Cuadro resumen de cauces

| Situacion | Cauce | Documento |
|---|---|---|
| Gananciales, **con acuerdo** | Convenio de liquidacion (art. 806 LEC a contrario); escritura publica si hay inmuebles; o clausula del convenio regulador (art. 90.1.e) CC) | `assets/convenio-liquidacion-gananciales.md` |
| Gananciales, **sin acuerdo** | Arts. 807 a 810 LEC: solicitud de formacion de inventario con su propuesta y, en su caso, posterior solicitud de liquidacion | `assets/solicitud-formacion-inventario.md` + `assets/propuesta-inventario.md` |
| **Participacion** | Art. 811 LEC: propuesta con estimacion de patrimonio inicial y final | Fuera de alcance: detener y escalar |
| **Separacion de bienes** | No hay masa comun (art. 806 LEC): nada que liquidar. Si hay bienes en proindiviso, division de cosa comun (arts. 400 y ss. CC) | Fuera de alcance: detener y explicar |
| Regimen de **derecho civil propio** (foral) | Norma autonomica aplicable | Fuera de alcance: verificar y escalar |
