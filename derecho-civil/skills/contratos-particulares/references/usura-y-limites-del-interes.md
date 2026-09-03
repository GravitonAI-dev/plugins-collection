# Interes, Usura y Limites del Pacto

> Material de referencia para la skill `derecho-civil-contratos-particulares`. Regimen del interes en el prestamo entre
> particulares y control de usura. La skill aplica estas reglas al redactar y al explicar al cliente; no forman parte
> literal del output.

---

## 1. Regla capital: sin pacto expreso, no hay intereses

**Art. 1755 CC** (verificado 03/09/2026, sin modificaciones desde 1889):

> "No se deberan intereses sino cuando expresamente se hubiesen pactado."

Consecuencias operativas:

- Un prestamo entre particulares es **gratuito por defecto**. El silencio del contrato no se interpreta a favor del prestamista.
- **El art. 1740 CC** lo confirma: "El simple prestamo puede ser gratuito o con pacto de pagar interes". La onerosidad es la excepcion, no la regla.
- No basta una mencion generica ("con el interes que corresponda"). El pacto debe ser **expreso** y determinar el tipo, o al menos ser determinable sin nuevo acuerdo entre las partes (art. 1273 CC, objeto determinable).
- **Art. 1756 CC**: si el prestatario paga intereses que no estaban estipulados, no puede reclamarlos despues ni imputarlos al capital. Esto no convierte el prestamo en oneroso hacia el futuro.

### Distincion que la skill debe explicar siempre

Hay **dos intereses distintos** y confundirlos es un error frecuente del cliente:

| | Interes remuneratorio | Interes de demora |
|---|---|---|
| Que retribuye | El uso del dinero durante el plazo pactado | El retraso del deudor tras el vencimiento |
| Regla por defecto | **No se debe si no se pacta expresamente** (art. 1755 CC) | A falta de pacto, **el interes legal del dinero** (art. 1108 CC) |
| Consecuencia practica | Un prestamo sin pacto de interes es gratuito durante todo el plazo | Aun siendo gratuito el prestamo, el impago genera interes legal desde la mora |

**Art. 1108 CC** (verificado 03/09/2026): "Si la obligacion consistiere en el pago de una cantidad de dinero, y el deudor incurriere en mora, la indemnizacion de daños y perjuicios, no habiendo pacto en contrario, consistira en el pago de los intereses convenidos, y a falta de convenio, en el interes legal."

**Art. 1100 CC**: la mora exige requerimiento judicial o extrajudicial del acreedor, **salvo** que la obligacion o la ley lo declaren asi expresamente (por eso conviene pactar la mora automatica al vencimiento) o que la fecha fuera motivo determinante.

---

## 2. El interes legal del dinero es una magnitud variable

**Nunca se escribe una cifra fija en un asset.** El interes legal se fija cada ejercicio en la Ley de Presupuestos Generales del Estado (art. 1 de la Ley 24/1984) y lo recoge el Banco de España.

Estado verificado el 03/09/2026 (detalle en `references/fuentes-plantillas-validadas.md`): la ultima fijacion expresa localizable en el BOE es la **disposicion adicional 42.ª de la Ley 31/2022** (PGE 2023), que lo situa en el **3,25 %** y literalmente "hasta el 31 de diciembre del año 2023"; no consta aprobada una Ley de Presupuestos para 2026 y el presupuesto esta prorrogado.

**Regla de la skill:**

1. Los assets se remiten al "interes legal del dinero vigente en cada momento" y, cuando se necesite la cifra, usan el placeholder `{{tipo_interes_legal_vigente}}`.
2. La cifra se verifica **en cada lanzamiento**, no se hereda de la reference.
3. Si no se puede verificar, se deja el placeholder, se advierte al usuario y se marca como pendiente de verificacion manual. **Prohibido dar por vigente una cifra no comprobada.**

---

## 3. Control de usura: la Ley Azcarate

**Ley de 23 de julio de 1908 sobre nulidad de los contratos de prestamos usurarios** (BOE-A-1908-5579). Verificado el 03/09/2026: la API del BOE devuelve `estatus_derogacion = N` y `vigencia_agotada = N`. **Sigue vigente**, sin modificaciones desde su promulgacion.

### 3.1 El supuesto de hecho (art. 1)

Es nulo todo contrato de prestamo en que se estipule:

- **(a) un interes notablemente superior al normal del dinero**, **y** manifiestamente desproporcionado con las circunstancias del caso; **o**
- **(b) un interes en condiciones tales que resulte leonino**, habiendo motivos para estimar que fue aceptado por el prestatario **a causa de su situacion angustiosa, de su inexperiencia o de lo limitado de sus facultades mentales**.

El mismo articulo declara nulo, ademas:

- el contrato **en que se suponga recibida mayor cantidad que la verdaderamente entregada** (relevante para el reconocimiento de deuda: ver el apartado 5);
- la **renuncia del fuero propio** hecha por el deudor en esta clase de contratos.

### 3.2 La consecuencia (art. 3) — el punto que el cliente entiende mal

La usura **no rebaja el interes: anula el contrato de prestamo**.

> Art. 3: "Declarada con arreglo a esta ley la nulidad de un contrato, el prestatario estara obligado a entregar tan solo la suma recibida; y si hubiera satisfecho parte de aquella y los intereses vencidos, el prestamista devolvera al prestatario lo que, tomando en cuenta el total de lo percibido, exceda del capital prestado."

Traducido a lo que le pasa al prestamista:

- **Pierde todo el interes**, no solo el exceso sobre lo "razonable".
- El prestatario solo devuelve **el principal efectivamente entregado**.
- Si el prestatario ya habia pagado por encima del principal, **el prestamista tiene que devolverle la diferencia**.
- **Art. 8**: la sentencia que declara la nulidad lleva **condena en costas al prestamista**.

Un prestamista suele creer que, como mucho, un juez "le bajaria el interes". Es falso, y la skill debe decirselo con estas palabras antes de que decida el tipo.

### 3.3 Alcance (art. 9): no se elude cambiando el nombre del contrato

> Art. 9: "Lo dispuesto por esta ley se aplicara a **toda operacion sustancialmente equivalente a un prestamo de dinero**, cualesquiera que sea la forma que revista el contrato y la garantia que para su cumplimiento se haya ofrecido."

Consecuencia: **no se puede escapar del control de usura** disfrazando el prestamo de reconocimiento de deuda, de compraventa con pacto de recompra, de arras, ni añadiendo una garantia real. La skill nunca ofrece esas construcciones como via para evitar la Ley Azcarate.

### 3.4 No hay umbral numerico legal

La Ley Azcarate **no fija ningun porcentaje**. Usa conceptos juridicos indeterminados y remite la apreciacion al tribunal:

> Art. 2: "Los Tribunales resolveran en cada caso, formando libremente su conviccion en vista de las alegaciones de las partes."

En la practica, el "interes normal del dinero" se contrasta con los tipos medios que publica el Banco de España para operaciones equivalentes, y la desproporcion se valora caso por caso.

**Regla de la skill: prohibido afirmar un umbral numerico como si fuera legal** ("hasta el X % es seguro"). Lo que la skill hace es:

1. Calcular el coste real de la operacion tal como el cliente la plantea (incluyendo comisiones, gastos y cualquier cantidad que el prestatario devuelva por encima del principal, no solo el "tipo" nominal).
2. Contrastarlo con el orden de magnitud del interes legal del dinero vigente y del coste normal de operaciones equivalentes.
3. Si la desproporcion es evidente, **advertir expresamente antes de redactar**, explicar la consecuencia del art. 3 y ofrecer escalacion.
4. Si el cliente insiste, no redactar el pacto sin dejar constancia de la advertencia en el propio documento.

### 3.5 Señales de alarma que obligan a advertir

- El total a devolver duplica o casi duplica el principal en un plazo corto.
- El prestatario esta en una situacion economica desesperada conocida por el prestamista.
- Hay descuento del interes en el momento de la entrega (se entrega menos de lo que figura como prestado): esto activa directamente el segundo parrafo del art. 1 (suponer recibida mayor cantidad que la entregada).
- Se pactan comisiones, gastos o penalizaciones que, sumadas, elevan el coste efectivo muy por encima del tipo nominal declarado.
- Se pretende que el prestatario renuncie a su fuero: nulo por el propio art. 1.

---

## 4. Interes de demora pactado

El interes de demora **si puede pactarse** por encima del legal (art. 1108 CC, "no habiendo pacto en contrario"), pero:

- Un interes de demora desproporcionado puede ser valorado, junto con el remuneratorio, dentro del juicio global de usura del art. 1 de la Ley Azcarate (art. 9: se atiende a la operacion, no a las etiquetas).
- El art. 1154 CC permite al juez **moderar equitativamente la pena** cuando la obligacion principal se ha cumplido en parte. Un interes de demora con funcion penal esta expuesto a esa moderacion.
- Entre particulares **no se aplica** la Ley 3/2004 de morosidad en operaciones comerciales: esa norma rige entre empresas y con la Administracion.

**Posicion conservadora de la skill:** ofrecer por defecto el interes legal del dinero incrementado en un numero moderado de puntos, explicar que el exceso es un riesgo, y no proponer nunca un multiplo del interes legal sin advertirlo.

---

## 5. Reconocimiento de deuda y usura

El reconocimiento de deuda **no puede usarse como envoltorio de un prestamo usurario**. Dos razones acumulativas:

1. **Art. 9 de la Ley Azcarate**: la ley se aplica a toda operacion sustancialmente equivalente a un prestamo, cualquiera que sea la forma del contrato.
2. **Art. 1 parrafo segundo de la Ley Azcarate**: es nulo el contrato en que se suponga recibida mayor cantidad que la verdaderamente entregada. Reconocer una deuda de 6.000 euros cuando se entregaron 3.000 encaja de lleno en el supuesto.

A esto se suma el regimen de la causa del Codigo Civil:

- **Art. 1275**: los contratos con causa ilicita **no producen efecto alguno**.
- **Art. 1276**: la expresion de una causa falsa da lugar a la nulidad, salvo que se pruebe que estaban fundados en otra verdadera y licita.
- **Art. 1277**: aunque la causa no se exprese, se presume que existe y es licita mientras el deudor no pruebe lo contrario.

El art. 1277 es la razon por la que un reconocimiento de deuda "abstracto" (sin causa expresada) es valido y coloca la carga de la prueba en el deudor. Pero es tambien la razon por la que **conviene expresar la causa**: si el deudor logra probar que no habia causa o que era ilicita, un reconocimiento abstracto cae entero; uno con causa expresada, veraz y licita, resiste.

**Regla de la skill:** ofrecer siempre la expresion de la causa, explicar por que conviene, y **rechazar** la peticion de redactar un reconocimiento de deuda cuya causa real sea un prestamo con interes desproporcionado, un juego prohibido, o cualquier otra causa ilicita. Ver el guardrail correspondiente en el `SKILL.md`.

---

## 6. Resumen operativo para el punto de negociacion `[negociacion]` sobre interes

Lo que la skill explica al cliente **antes** de preguntarle si quiere pactar interes:

1. Si no lo pacta expresamente, el prestamo es gratuito: no habra intereses (art. 1755 CC).
2. Aunque sea gratuito, si el prestatario no devuelve a tiempo devengara el interes legal del dinero desde la mora (art. 1108 CC), y conviene pactar que la mora se produzca automaticamente al vencimiento sin necesidad de requerimiento (art. 1100 CC).
3. Si decide pactar interes, existe un limite: la Ley de 1908 sigue vigente y declara **nulo** el prestamo con interes notablemente superior al normal y manifiestamente desproporcionado.
4. La consecuencia de la usura **no es una rebaja del interes**: el contrato se anula, el prestatario devuelve solo el principal, el prestamista devuelve lo cobrado de mas y carga con las costas (arts. 3 y 8).
5. No hay un porcentaje legal seguro: lo decide el tribunal caso por caso (art. 2). Cuanto mas se aleje del coste normal del dinero, mayor es el riesgo.
