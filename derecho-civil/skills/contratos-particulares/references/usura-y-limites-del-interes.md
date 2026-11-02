# Interés, Usura y Límites del Pacto

> Material de referencia para la skill `derecho-civil-contratos-particulares`. Régimen del interés en el préstamo entre
> particulares y control de usura. La skill aplica estas reglas al redactar y al explicar al cliente; no forman parte
> literal del output.

---

## 1. Regla capital: sin pacto expreso, no hay intereses

**Art. 1755 CC** (verificado 03/09/2026, sin modificaciones desde 1889):

> "No se deberán intereses sino cuando expresamente se hubiesen pactado."

Consecuencias operativas:

- Un préstamo entre particulares es **gratuito por defecto**. El silencio del contrato no se interpreta a favor del prestamista.
- **El art. 1740 CC** lo confirma: "El simple préstamo puede ser gratuito o con pacto de pagar interés". La onerosidad es la excepción, no la regla.
- No basta una mención genérica ("con el interés que corresponda"). El pacto debe ser **expreso** y determinar el tipo, o al menos ser determinable sin nuevo acuerdo entre las partes (art. 1273 CC, objeto determinable).
- **Art. 1756 CC**: si el prestatario paga intereses que no estaban estipulados, no puede reclamarlos después ni imputarlos al capital. Esto no convierte el préstamo en oneroso hacia el futuro.

### Distinción que la skill debe explicar siempre

Hay **dos intereses distintos** y confundirlos es un error frecuente del cliente:

| | Interés remuneratorio | Interés de demora |
|---|---|---|
| Qué retribuye | El uso del dinero durante el plazo pactado | El retraso del deudor tras el vencimiento |
| Regla por defecto | **No se debe si no se pacta expresamente** (art. 1755 CC) | A falta de pacto, **el interés legal del dinero** (art. 1108 CC) |
| Consecuencia práctica | Un préstamo sin pacto de interés es gratuito durante todo el plazo | Aun siendo gratuito el préstamo, el impago genera interés legal desde la mora |

**Art. 1108 CC** (verificado 03/09/2026): "Si la obligación consistiere en el pago de una cantidad de dinero, y el deudor incurriere en mora, la indemnización de daños y perjuicios, no habiendo pacto en contrario, consistirá en el pago de los intereses convenidos, y a falta de convenio, en el interés legal."

**Art. 1100 CC**: la mora exige requerimiento judicial o extrajudicial del acreedor, **salvo** que la obligación o la ley lo declaren así expresamente (por eso conviene pactar la mora automática al vencimiento) o que la fecha fuera motivo determinante.

---

## 2. El interés legal del dinero es una magnitud variable

**Nunca se escribe una cifra fija en un asset.** El interés legal se fija cada ejercicio en la Ley de Presupuestos Generales del Estado (art. 1 de la Ley 24/1984) y lo recoge el Banco de España.

Estado verificado el 03/09/2026 (detalle en `references/fuentes-plantillas-validadas.md`): la última fijación expresa localizable en el BOE es la **disposición adicional 42.ª de la Ley 31/2022** (PGE 2023), que lo sitúa en el **3,25 %** y literalmente "hasta el 31 de diciembre del año 2023"; no consta aprobada una Ley de Presupuestos para 2026 y el presupuesto está prorrogado.

**Regla de la skill:**

1. Los assets se remiten al "interés legal del dinero vigente en cada momento" y, cuando se necesite la cifra, usan el placeholder `{{TIPO_INTERES_LEGAL_VIGENTE}}`.
2. La cifra se verifica **en cada lanzamiento**, no se hereda de la reference.
3. Si no se puede verificar, se deja el placeholder, se advierte al usuario y se marca como pendiente de verificación manual. **Prohibido dar por vigente una cifra no comprobada.**

---

## 3. Control de usura: la Ley Azcárate

**Ley de 23 de julio de 1908 sobre nulidad de los contratos de préstamos usurarios** (BOE-A-1908-5579). Verificado el 03/09/2026: la API del BOE devuelve `estatus_derogacion = N` y `vigencia_agotada = N`. **Sigue vigente**, sin modificaciones desde su promulgación.

### 3.1 El supuesto de hecho (art. 1)

Es nulo todo contrato de préstamo en que se estipule:

- **(a) un interés notablemente superior al normal del dinero**, **y** manifiestamente desproporcionado con las circunstancias del caso; **o**
- **(b) un interés en condiciones tales que resulte leonino**, habiendo motivos para estimar que fue aceptado por el prestatario **a causa de su situación angustiosa, de su inexperiencia o de lo limitado de sus facultades mentales**.

El mismo artículo declara nulo, además:

- el contrato **en que se suponga recibida mayor cantidad que la verdaderamente entregada** (relevante para el reconocimiento de deuda: ver el apartado 5);
- la **renuncia del fuero propio** hecha por el deudor en esta clase de contratos.

### 3.2 La consecuencia (art. 3) — el punto que el cliente entiende mal

La usura **no rebaja el interés: anula el contrato de préstamo**.

> Art. 3: "Declarada con arreglo a esta ley la nulidad de un contrato, el prestatario estará obligado a entregar tan solo la suma recibida; y si hubiera satisfecho parte de aquella y los intereses vencidos, el prestamista devolverá al prestatario lo que, tomando en cuenta el total de lo percibido, exceda del capital prestado."

Traducido a lo que le pasa al prestamista:

- **Pierde todo el interés**, no solo el exceso sobre lo "razonable".
- El prestatario solo devuelve **el principal efectivamente entregado**.
- Si el prestatario ya había pagado por encima del principal, **el prestamista tiene que devolverle la diferencia**.
- **Art. 8**: la sentencia que declara la nulidad lleva **condena en costas al prestamista**.

Un prestamista suele creer que, como mucho, un juez "le bajaría el interés". Es falso, y la skill debe decírselo con estas palabras antes de que decida el tipo.

### 3.3 Alcance (art. 9): no se elude cambiando el nombre del contrato

> Art. 9: "Lo dispuesto por esta ley se aplicará a **toda operación sustancialmente equivalente a un préstamo de dinero**, cualesquiera que sea la forma que revista el contrato y la garantía que para su cumplimiento se haya ofrecido."

Consecuencia: **no se puede escapar del control de usura** disfrazando el préstamo de reconocimiento de deuda, de compraventa con pacto de recompra, de arras, ni añadiendo una garantía real. La skill nunca ofrece esas construcciones como vía para evitar la Ley Azcárate.

### 3.4 No hay umbral numérico legal

La Ley Azcárate **no fija ningún porcentaje**. Usa conceptos jurídicos indeterminados y remite la apreciación al tribunal:

> Art. 2: "Los Tribunales resolverán en cada caso, formando libremente su convicción en vista de las alegaciones de las partes."

En la práctica, el "interés normal del dinero" se contrasta con los tipos medios que publica el Banco de España para operaciones equivalentes, y la desproporción se valora caso por caso.

**Regla de la skill: prohibido afirmar un umbral numérico como si fuera legal** ("hasta el X % es seguro"). Lo que la skill hace es:

1. Calcular el coste real de la operación tal como el cliente la plantea (incluyendo comisiones, gastos y cualquier cantidad que el prestatario devuelva por encima del principal, no solo el "tipo" nominal).
2. Contrastarlo con el orden de magnitud del interés legal del dinero vigente y del coste normal de operaciones equivalentes.
3. Si la desproporción es evidente, **advertir expresamente antes de redactar**, explicar la consecuencia del art. 3 y ofrecer escalación.
4. Si el cliente insiste, no redactar el pacto sin dejar constancia de la advertencia en el propio documento.

### 3.5 Señales de alarma que obligan a advertir

- El total a devolver duplica o casi duplica el principal en un plazo corto.
- El prestatario está en una situación económica desesperada conocida por el prestamista.
- Hay descuento del interés en el momento de la entrega (se entrega menos de lo que figura como prestado): esto activa directamente el segundo párrafo del art. 1 (suponer recibida mayor cantidad que la entregada).
- Se pactan comisiones, gastos o penalizaciones que, sumadas, elevan el coste efectivo muy por encima del tipo nominal declarado.
- Se pretende que el prestatario renuncie a su fuero: nulo por el propio art. 1.

---

## 4. Interés de demora pactado

El interés de demora **si puede pactarse** por encima del legal (art. 1108 CC, "no habiendo pacto en contrario"), pero:

- Un interés de demora desproporcionado puede ser valorado, junto con el remuneratorio, dentro del juicio global de usura del art. 1 de la Ley Azcárate (art. 9: se atiende a la operación, no a las etiquetas).
- El art. 1154 CC permite al juez **moderar equitativamente la pena** cuando la obligación principal se ha cumplido en parte. Un interés de demora con función penal está expuesto a esa moderación.
- Entre particulares **no se aplica** la Ley 3/2004 de morosidad en operaciones comerciales: esa norma rige entre empresas y con la Administración.

**Posición conservadora de la skill:** ofrecer por defecto el interés legal del dinero incrementado en un número moderado de puntos, explicar que el exceso es un riesgo, y no proponer nunca un múltiplo del interés legal sin advertirlo.

---

## 5. Reconocimiento de deuda y usura

El reconocimiento de deuda **no puede usarse como envoltorio de un préstamo usurario**. Dos razones acumulativas:

1. **Art. 9 de la Ley Azcárate**: la ley se aplica a toda operación sustancialmente equivalente a un préstamo, cualquiera que sea la forma del contrato.
2. **Art. 1 párrafo segundo de la Ley Azcárate**: es nulo el contrato en que se suponga recibida mayor cantidad que la verdaderamente entregada. Reconocer una deuda de 6.000 euros cuando se entregaron 3.000 encaja de lleno en el supuesto.

A esto se suma el régimen de la causa del Código Civil:

- **Art. 1275**: los contratos con causa ilícita **no producen efecto alguno**.
- **Art. 1276**: la expresión de una causa falsa da lugar a la nulidad, salvo que se pruebe que estaban fundados en otra verdadera y licita.
- **Art. 1277**: aunque la causa no se exprese, se presume que existe y es licita mientras el deudor no pruebe lo contrario.

El art. 1277 es la razón por la que un reconocimiento de deuda "abstracto" (sin causa expresada) es válido y coloca la carga de la prueba en el deudor. Pero es también la razón por la que **conviene expresar la causa**: si el deudor logra probar que no había causa o que era ilícita, un reconocimiento abstracto cae entero; uno con causa expresada, veraz y licita, resiste.

**Regla de la skill:** ofrecer siempre la expresión de la causa, explicar por qué conviene, y **rechazar** la petición de redactar un reconocimiento de deuda cuya causa real sea un préstamo con interés desproporcionado, un juego prohibido, o cualquier otra causa ilícita. Ver el guardrail correspondiente en el `SKILL.md`.

---

## 6. Resumen operativo para el punto de negociación `[negociacion]` sobre interés

Lo que la skill explica al cliente **antes** de preguntarle si quiere pactar interés:

1. Si no lo pacta expresamente, el préstamo es gratuito: no habrá intereses (art. 1755 CC).
2. Aunque sea gratuito, si el prestatario no devuelve a tiempo devengará el interés legal del dinero desde la mora (art. 1108 CC), y conviene pactar que la mora se produzca automáticamente al vencimiento sin necesidad de requerimiento (art. 1100 CC).
3. Si decide pactar interés, existe un límite: la Ley de 1908 sigue vigente y declara **nulo** el préstamo con interés notablemente superior al normal y manifiestamente desproporcionado.
4. La consecuencia de la usura **no es una rebaja del interés**: el contrato se anula, el prestatario devuelve solo el principal, el prestamista devuelve lo cobrado de más y carga con las costas (arts. 3 y 8).
5. No hay un porcentaje legal seguro: lo decide el tribunal caso por caso (art. 2). Cuanto más se aleje del coste normal del dinero, mayor es el riesgo.
