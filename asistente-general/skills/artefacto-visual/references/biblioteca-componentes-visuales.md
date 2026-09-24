# Biblioteca de componentes visuales

Bloques listos para insertar en cualquiera de las tres plantillas. Todos usan los tokens ya declarados en `:root` (`--superficie`, `--borde`, `--acento`, `--c1` a `--c6`, escala `--e1` a `--e6`), de modo que heredan el tema claro, el oscuro y los estilos de impresion sin tocar nada. Las clases y los identificadores estan en espanol y **no se renombran**: lo que cambia de idioma es el texto visible.

---

## Parte I. Sistema de coordenadas comun

Los graficos cartesianos comparten un mismo lienzo para que todos los calculos sean iguales:

```
viewBox = "0 0 700 300"
area de dibujo:  x de 64 a 664   (600 de ancho)
                 y de 44 a 244   (200 de alto, con el cero en y = 244)
lineas de rejilla: y = 44, 94, 144, 194, 244
```

```
y(valor)   = 244 - valor / maximo_eje * 200
x(indice)  = 64 + indice / (n - 1) * 600          para lineas
banda      = 600 / n                              para barras
centro(i)  = 64 + banda * (i + 0,5)
```

El `maximo_eje` se redondea **hacia arriba** a una cifra legible: si el maximo real es 8.640, el eje va a 10.000. Las etiquetas del eje vertical, de arriba abajo, valen `maximo_eje`, `0,75 x maximo_eje`, `0,5 x maximo_eje`, `0,25 x maximo_eje` y `0`. El eje arranca **siempre** en cero.

Reglas que acompanan a todos los graficos:

- `role="img"` y `aria-label` con el dato resumido en una frase.
- Colores tomados de la serie `--c1` a `--c6`, en orden y **coherentes entre graficos del mismo artefacto**: si la parte actora es `--c1` en el primero, lo es en todos.
- Coordenadas con un decimal como maximo.
- Nunca se inventa un punto para cerrar una serie: un hueco interrumpe la linea.

---

## Parte II. Las diez formas

### 1. Barras horizontales comparativas (CSS, sin SVG)

La forma mas robusta para comparar partidas: solo exige el porcentaje respecto al valor mayor.

```html
<ul class="barras">
  <li>
    <p class="fila"><span>Factura 2025/118</span><span class="valor">18.400,00 EUR</span></p>
    <div class="pista" role="img" aria-label="Factura 2025/118: 18.400,00 euros"><span style="width:100%"></span></div>
  </li>
  <li>
    <p class="fila"><span>Factura 2025/131</span><span class="valor">11.250,00 EUR</span></p>
    <div class="pista" role="img" aria-label="Factura 2025/131: 11.250,00 euros"><span style="width:61.1%"></span></div>
  </li>
</ul>
```

`porcentaje = valor / valor_maximo * 100`, con un decimal. Cada `li` toma automaticamente el siguiente color de la serie. Se ordenan de mayor a menor salvo que el orden cronologico sea el que informa.

### 2. Barras verticales

```
banda  = 600 / n
ancho  = banda * 0,56
x(i)   = 64 + banda * (i + 0,5) - ancho / 2
alto(v)= v / maximo_eje * 200
y(v)   = 244 - alto(v)
```

```html
<svg viewBox="0 0 700 300" role="img" aria-label="Importe reclamado por trimestre">
  <line class="rejilla" x1="64" y1="44" x2="664" y2="44"></line>
  <line class="rejilla" x1="64" y1="144" x2="664" y2="144"></line>
  <line class="rejilla" x1="64" y1="244" x2="664" y2="244"></line>
  <text class="eje" x="56" y="48" text-anchor="end">20.000</text>
  <text class="eje" x="56" y="248" text-anchor="end">0</text>
  <rect x="97.6" y="124" width="84" height="120" fill="var(--c1)" rx="3"></rect>
  <rect x="247.6" y="84" width="84" height="160" fill="var(--c1)" rx="3"></rect>
  <text class="eje" x="139.6" y="264" text-anchor="middle">1T</text>
  <text class="eje" x="289.6" y="264" text-anchor="middle">2T</text>
</svg>
```

Con mas de ocho categorias, se pasa a barras horizontales: las etiquetas verticales dejan de leerse.

### 3. Barras apiladas y apiladas al cien por cien

Cada segmento arranca donde acaba el anterior:

```
acumulado(0) = 0
y_segmento(k) = 244 - (acumulado(k) + valor(k)) / maximo_eje * 200
alto_segmento(k) = valor(k) / maximo_eje * 200
acumulado(k+1) = acumulado(k) + valor(k)
```

En la variante al cien por cien, `maximo_eje = total de la columna` y cada valor se convierte antes en porcentaje. **Solo se usa cuando importa la proporcion, nunca cuando importa el volumen absoluto**: al normalizar, una columna de 200 euros y otra de 200.000 se ven identicas.

### 4. Linea con area degradada

El degradado se declara una vez en `<defs>` y la plantilla de panel ya lo trae con el identificador `degradado-area`:

```html
<defs>
  <linearGradient id="degradado-area" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="var(--c1)" stop-opacity=".34"></stop>
    <stop offset="100%" stop-color="var(--c1)" stop-opacity="0"></stop>
  </linearGradient>
</defs>
<polygon class="area-1" points="64,190.4 214,152.8 364,124.4 514,95.2 664,71.3 664,244 64,244"></polygon>
<polyline class="serie-1" points="64,190.4 214,152.8 364,124.4 514,95.2 664,71.3"></polyline>
<circle class="punto-1" cx="214" cy="152.8" r="3.6"></circle>
```

El poligono del area son **los mismos puntos de la linea mas los dos vertices de la base**: `664,244` y `64,244`, en ese orden. La segunda serie usa `class="serie-2"` (trazo discontinuo) y no lleva area.

### 5. Banda de objetivo o umbral

Franja horizontal que situa la serie frente a un limite legal, un pacto o un objetivo:

```
y_banda   = 244 - limite_superior / maximo_eje * 200
alto_banda= (limite_superior - limite_inferior) / maximo_eje * 200
```

```html
<rect class="banda" x="64" y="104" width="600" height="40"></rect>
```

Se dibuja **antes** que la rejilla y que las series, para que quede por debajo. Su significado se explica en la leyenda.

### 6. Minigrafico de tendencia dentro del indicador

Cabe en la tarjeta del indicador y no necesita ejes:

```
x(i) = 1 + i / (n - 1) * 118
y(v) = 30 - (v - minimo) / (maximo - minimo) * 28
```

```html
<div class="tendencia">
  <svg class="chispa" viewBox="0 0 120 32" preserveAspectRatio="none" role="img" aria-label="Tendencia de los ultimos seis meses: al alza">
    <polygon class="chispa-area" points="1,28 24.6,24 48.2,18 71.8,13 95.4,9 119,4 119,32 1,32"></polygon>
    <polyline class="chispa-linea" points="1,28 24.6,24 48.2,18 71.8,13 95.4,9 119,4"></polyline>
    <circle class="chispa-punto" cx="119" cy="4" r="2.4"></circle>
  </svg>
  <p class="tendencia-nota">Enero a septiembre: +240%</p>
</div>
```

Tres cosas lo convierten en un grafico y no en una raya suelta: el **area** bajo la linea, que le da suelo; el **punto final**, que dice hacia donde se lee; y el **pie de una linea**, que dice de que periodo habla y cuanto ha variado. Sin ellos, quien lo mira ve una diagonal sin explicacion en medio de una tarjeta.

El poligono del area son los puntos de la linea mas los dos vertices del suelo, `119,32` y `1,32`. La linea lleva `vector-effect="non-scaling-stroke"` porque el `preserveAspectRatio="none"` estira el lienzo al ancho de la tarjeta y, sin eso, el trazo se deformaria.

Aqui la escala si puede arrancar en el minimo de la serie, porque el minigrafico muestra **forma**, no magnitud, y nunca lleva cifras en los ejes.

### 7. Medidor semicircular

> **Cuidado con el color:** una regla CSS gana siempre al atributo `stroke` escrito en la etiqueta. Si el color del arco se decide por dato (verde, ambar o rojo segun el tramo), la regla `.medidor .arco` **no** debe fijar `stroke`; solo el grosor y el remate. Lo mismo ocurre con `transform` en el anillo.

Arco de media circunferencia para porcentajes de avance, consumo de plazo o nivel de riesgo.

```
Plantilla de panel:        radio 90  ->  longitud del arco = pi x 90 = 282,7
Plantilla interactiva:     radio 70  ->  longitud del arco = pi x 70 = 219,9

arco  = porcentaje / 100 * longitud
resto = longitud - arco
```

```html
<svg class="medidor" viewBox="0 0 240 150" role="img" aria-label="Plazo consumido: 68 por ciento">
  <path class="pista-arco" d="M 30 125 A 90 90 0 0 1 210 125"></path>
  <path class="arco" d="M 30 125 A 90 90 0 0 1 210 125" stroke="var(--aviso)" stroke-dasharray="192.2 90.5"></path>
  <text x="120" y="112" text-anchor="middle" font-size="34" font-weight="670">68%</text>
</svg>
```

Color por tramo: hasta el 60 por ciento `var(--ok)`, hasta el 85 `var(--aviso)`, por encima `var(--riesgo)`.

### 8. Cascada de descomposicion

Explica como se llega a un total: principal, intereses, costas y suma. Lienzo de la plantilla de panel: `viewBox="0 0 460 280"`, base en `y = 240`, alto util 200.

```
maximo   = total final
alto(k)  = |valor_final(k) - valor_inicial(k)| / maximo * 200
y(k)     = 240 - mayor(valor_inicial(k), valor_final(k)) / maximo * 200
etiqueta = y(k) - 6
```

La primera columna arranca en cero y la ultima es el total, que tambien arranca en cero y se pinta con `var(--acento-fuerte)`. Los conectores discontinuos unen el techo de cada columna con el arranque de la siguiente. Con saldos negativos, la columna baja: `valor_final < valor_inicial` y se colorea con `var(--riesgo)`.

### 9. Matriz de riesgo e impacto

Cruza dos ejes cualitativos de tres o cuatro niveles. Mas niveles no aportan precision, solo ruido.

```html
<svg viewBox="0 0 420 300" role="img" aria-label="Matriz de riesgo: dos contingencias en probabilidad alta e impacto alto">
  <rect x="90" y="30" width="100" height="70" fill="var(--aviso)" opacity=".18"></rect>
  <rect x="190" y="30" width="100" height="70" fill="var(--riesgo)" opacity=".22"></rect>
  <text class="eje" x="140" y="70" text-anchor="middle">Vigilar</text>
  <text class="eje" x="240" y="70" text-anchor="middle">Actuar ya</text>
  <text class="eje" x="80" y="70" text-anchor="end">Probabilidad alta</text>
  <text class="eje" x="140" y="290" text-anchor="middle">Impacto medio</text>
  <circle cx="240" cy="62" r="7" fill="var(--c4)"></circle>
</svg>
```

Cada contingencia es un circulo **numerado** dentro de su celda, y los nombres van en una `ul class="leyenda"` debajo del grafico: escribir el rotulo al lado del circulo desborda la tarjeta en cuanto el texto crece. El color de fondo de la celda indica la zona (`--ok`, `--aviso`, `--riesgo` con opacidad baja) y el texto de la celda dice que hacer.

### 10. Diagrama de plazos con marca de hoy

Varios plazos sobre **una misma escala de calendario**, con una linea vertical en la fecha actual. Es la unica forma honesta de comparar plazos entre si: si cada barra tuviera su propia escala, la linea de hoy no significaria nada.

```
x(fecha) = x0 + (fecha - inicio) / (fin - inicio) * ancho
```

Con `x0 = 150` y `ancho = 520` queda sitio para los rotulos a la izquierda. Cada fila baja 38 px; la barra mide 18 px de alto con `rx="4"`.

```html
<svg viewBox="0 0 700 210" role="img" aria-label="El requerimiento vence el 27 de septiembre y la contestacion corre hasta el 13 de noviembre">
  <text class="eje" x="140" y="57" text-anchor="end">Requerimiento</text>
  <rect x="218.8" y="44" width="43.0" height="18" rx="4" fill="var(--aviso)"></rect>
  <text class="eje" x="148.9" y="24" text-anchor="middle" fill="var(--riesgo)">hoy</text>
  <line x1="248.9" y1="30" x2="248.9" y2="196" stroke="var(--riesgo)" stroke-width="2" stroke-dasharray="4 3"></line>
  <line class="rejilla" x1="150" y1="182" x2="670" y2="182"></line>
  <text class="eje" x="150" y="198">1 sep</text>
</svg>
```

El plazo en curso se pinta con `var(--aviso)`; los futuros, con la serie categorica. Todo plazo lleva su fecha de vencimiento, en el rotulo o en el eje: una barra sin fecha no sirve para calcular.

**Variante corta (una sola barra por plazo, sin calendario comun):** la pista de la seccion 1 con el ancho igual a la parte consumida, `dias_transcurridos / dias_totales * 100`, y `var(--riesgo)` por encima del 80 por ciento. Sirve para un unico plazo dentro de una tarjeta de indicador, nunca para comparar varios.

### 11. Anillo de reparto

Radio 62 en la plantilla de panel, luego `C = 2 x pi x 62 = 389,6`.

```
arco(i)          = porcentaje(i) / 100 * 389,6
resto(i)         = 389,6 - arco(i)
desplazamiento(i)= -(suma de los arcos anteriores)
```

```html
<g transform="translate(115,95) rotate(-90)">
  <circle class="base" cx="0" cy="0" r="62"></circle>
  <circle cx="0" cy="0" r="62" stroke="var(--c1)" stroke-dasharray="101.3 288.3" stroke-dashoffset="0"></circle>
  <circle cx="0" cy="0" r="62" stroke="var(--c2)" stroke-dasharray="148.0 241.6" stroke-dashoffset="-101.3"></circle>
</g>
```

La rotacion va en el atributo `transform` del grupo, **nunca** en una regla CSS: una `transform` en CSS sustituye al atributo y descoloca el anillo. Maximo cuatro porciones.

---

## Parte III. Componentes de contenido

### Fila de indicadores

```html
<div class="indicadores">
  <div class="indicador aparece es-riesgo">
    <p class="rotulo">Importe reclamado</p>
    <p class="cifra">14.250,00 EUR</p>
    <p class="detalle">Principal mas intereses al 31/12/2026</p>
  </div>
</div>
```

Modificadores: `es-ok`, `es-atencion`, `es-riesgo`. Maximo cuatro por fila. La clase `aparece` anade la animacion escalonada de entrada, que se desactiva sola en impresion y para quien pide movimiento reducido.

### Aviso destacado

```html
<div class="aviso riesgo">
  <span class="titulo">Plazo de caducidad</span>
  La accion de despido caduca a los veinte dias habiles desde la fecha de efectos.
</div>
```

Variantes: sin clase (informativo), `favorable`, `riesgo`. Uno cada varias secciones: si todo esta destacado, nada lo esta.

### Cronologia de hitos

```html
<ol class="cronologia">
  <li>
    <span class="fecha">12 de marzo de 2026</span>
    <span class="hito">Requerimiento extrajudicial</span><br>
    Burofax con acuse de recibo remitido al domicilio social.
  </li>
</ol>
```

Orden cronologico ascendente y fecha cierta o `{{FECHA_PENDIENTE}}`; nunca una fecha estimada presentada como real.

### Tabla comparativa

```html
<div class="tabla">
  <table>
    <caption>Comparativa de vias de reclamacion</caption>
    <thead>
      <tr><th>Via</th><th class="cifra">Coste</th><th class="cifra">Plazo</th><th>Viabilidad</th></tr>
    </thead>
    <tbody>
      <tr><td>Monitorio</td><td class="cifra">Sin costas iniciales</td><td class="cifra">2 a 4 meses</td><td><span class="distintivo ok">Alta</span></td></tr>
    </tbody>
    <tfoot>
      <tr><td>Total</td><td class="cifra">42.180,50</td><td class="cifra"></td><td></td></tr>
    </tfoot>
  </table>
</div>
```

Las columnas numericas llevan `class="cifra"`. Los distintivos admiten `ok`, `atencion` y `riesgo`. En impresion, el `thead` se repite en cada pagina.

### Lista de verificacion con progreso

Presente en la plantilla interactiva. Cada punto es un `input type="checkbox"` con su `label`; la barra y el contador se actualizan solos. Para anadir puntos basta replicar el `li`: el script cuenta los elementos existentes, no un numero fijo.

### Panel de entrada y recalculo

Tres funciones separadas:

- `leer()` recoge los valores del formulario y devuelve un objeto.
- `calcular(d)` recibe ese objeto y devuelve `{ resultado1, resultado2, resultado3, medidor, desglose: [{concepto, importe, detalle}] }`. Es el unico bloque que cambia de un artefacto a otro. `medidor` es un porcentaje de 0 a 100 que mueve el arco; `detalle` es texto ya formateado. La fila de totales suma la columna de importes; la tercera solo muestra total si el calculo devuelve ademas `totalDetalle`, porque sumar dias o porcentajes carece de sentido.
- `pintar(r)` vuelca el resultado con `textContent`, nunca con `innerHTML`.

Formato espanol siempre mediante `Intl.NumberFormat("es-ES", ...)`.

Ejemplo de bloque de calculo para intereses de demora:

```js
var base = d.campo1;
var tipo = d.campo2 / 100;
var dias = d.campo3;
var recargo = d.campo4 === "comercial" ? base * 0.4 / 100 * dias / 365 : 0;
var intereses = base * tipo * dias / 365;
var total = base + intereses + recargo;
return {
  resultado1: total,
  resultado2: intereses + recargo,
  resultado3: dias,
  medidor: total ? (intereses + recargo) * 100 / total : 0,
  desglose: [
    { concepto: "Principal reclamado", importe: base, detalle: "--" },
    { concepto: "Intereses al tipo aplicado", importe: intereses, detalle: dias + " dias" },
    { concepto: "Recargo por morosidad comercial", importe: recargo, detalle: dias + " dias" }
  ]
};
```

### Pie del artefacto

```html
<footer class="pie">
  <p>Fuentes: documentacion aportada por el cliente el 12/03/2026 y calculo propio.</p>
  <p>Documento de trabajo. No sustituye al asesoramiento de un profesional colegiado.</p>
</footer>
```
