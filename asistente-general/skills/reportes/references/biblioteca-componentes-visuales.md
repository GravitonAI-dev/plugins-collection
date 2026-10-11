# Biblioteca de componentes visuales

Todo lo que se inserta en un reporte usa los tokens de `:root` de la base (`--superficie`, `--borde`, `--acento`, `--c1` a `--c6`, escala `--e1` a `--e6`). Por eso hereda el tema claro, el oscuro, el sobrio y la impresion sin tocar nada. Las clases y los identificadores estan en espanol y **no se renombran**: lo que cambia de idioma es el texto visible.

---

## Parte I. Como se declara un grafico

Los graficos **no se dibujan a mano ni se calculan coordenadas**. Se declaran en dos sitios con el mismo nombre:

1. **El hueco**, donde debe aparecer: `<figure class="grafico" data-grafico="evolucion"></figure>`. El minigrafico de un indicador usa `<div class="tendencia" data-grafico="tendencia"></div>`.
2. **Los datos**, dentro del bloque `<script type="application/json" id="datos-reporte">` de la base, en `graficos.evolucion`.

El motor de la base dibuja el SVG, calcula escalas, ejes y porcentajes, rellena la descripcion accesible, anade debajo la tabla de datos desplegable con descarga en CSV, escribe la linea de fuente del grafico y compone el pie de fuentes del documento. Si un grafico tiene un error de datos, en su lugar aparece un recuadro rojo que dice que falta; nunca un grafico equivocado.

### Estructura del bloque de datos

```json
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "ine": {"nombre": "INE, Estadistica de nacimientos", "url": "https://www.ine.es/...", "consulta": "2026-10-11"},
    "cliente": {"nombre": "Mayor de clientes aportado por el cliente", "consulta": "2026-09-18"}
  },
  "cifras": {
    "principal": {"de": "evolucion", "calculo": "ultimo", "unidad": "eur"}
  },
  "graficos": {
    "evolucion": {"tipo": "linea", "unidad": "eur", "fuente": "cliente", "etiquetas": [], "series": []}
  },
  "textos": {}
}
```

- **`idioma`** y **`moneda`** fijan el formato de cifras y fechas (miles con punto en espanol, siempre, tambien con cuatro cifras).
- **`fuentes`**: cada fuente con `nombre`, `url` si viene de internet y `consulta` en formato `AAAA-MM-DD` (la fecha real de la consulta en la sesion, nunca inventada). Los graficos las citan por su clave.
- **`cifras`**: cifras sueltas del texto. Cada una es `{"valor": 1234, "unidad": "eur"}` o un calculo sobre un grafico: `{"de": "grafico", "calculo": "suma", "serie": 0, "unidad": "eur"}`. Calculos: `suma`, `media`, `maximo`, `minimo`, `primero`, `ultimo`, `cuenta`, `variacion` (porcentaje entre el primero y el ultimo) y `porcentaje` (peso de `"elemento": "rotulo"` sobre el total). En el HTML se escriben con `<span data-cifra="principal"></span>`.
- **`textos`**: solo si el documento no esta en espanol ni en ingles, para traducir los rotulos del motor (`datos`, `csv`, `fuente`, `fuentes`, `consulta`, `otros`, `hoy`, `total`, `concepto`, `valor`, `acumulado`, `porcentaje`, `inicio`, `fin`, `restantes`, `maximo`, `ok`, `aviso`, `riesgo`, `error`).

### Campos comunes a todos los graficos

| Campo | Uso |
| :--- | :--- |
| `tipo` | Obligatorio. Uno de los tipos de la Parte II |
| `resumen` | La frase que lee un lector de pantalla: el dato principal resumido. Obligatorio en la practica |
| `fuente` | Clave de `fuentes`. En linea y columnas puede ir por serie (`series[].fuente`) |
| `unidad` | `eur`, `pct`, `num`, `entero` o cualquier texto (`"dias"`, `"asuntos"`), que se anade detras de la cifra |
| `color` | En elementos, series o porciones: `1` a `6` (serie `--c1` a `--c6`) o `ok`, `aviso`, `riesgo`. Sirve para mantener el mismo color para la misma parte en todos los graficos |
| `tabla` | `false` para no anadir la tabla de datos desplegable |

Los valores que falten se escriben `null`: la linea se interrumpe y la columna no se pinta. Nunca se inventa un punto para cerrar una serie.

---

## Parte II. Los tipos

### `barras` — barras horizontales

La forma mas robusta para comparar partidas.

```json
{"tipo": "barras", "unidad": "eur", "fuente": "cliente",
 "elementos": [{"rotulo": "Factura 2025/118", "valor": 18400}, {"rotulo": "Factura 2025/131", "valor": 11250}]}
```

Se ordenan de mayor a menor salvo `"orden": "original"`, que se usa cuando el orden cronologico es el que informa.

### `columnas` — barras verticales, una o varias series

```json
{"tipo": "columnas", "unidad": "eur", "etiquetas": ["1T", "2T", "3T", "4T"],
 "series": [{"nombre": "2025", "valores": [12000, 16000, 9000, 14000]}, {"nombre": "2026", "valores": [14000, 18500, 11000, null]}]}
```

Con mas de ocho categorias se usan `barras`: las etiquetas dejan de leerse. `"valores": false` quita las cifras encima de las columnas.

### `apiladas` — composicion de cada periodo

Mismo formato que `columnas`. Encima de cada columna aparece el total. Con `"cien": true` cada columna se normaliza al cien por cien: **solo cuando importa la proporcion**, nunca el volumen, porque una columna de 200 euros y otra de 200.000 se verian identicas. No admite negativos.

### `linea` — evolucion, con area, banda, anotaciones y destacados

```json
{"tipo": "linea", "unidad": "eur", "etiquetas": ["Ene", "Feb", "Mar"],
 "series": [{"nombre": "Principal", "valores": [12400, 21800, 28900]}, {"nombre": "Cobrado", "valores": [0, 2100, 2100]}],
 "umbral": {"desde": 0, "hasta": 15000, "rotulo": "Umbral de riesgo asumido"},
 "anotaciones": [{"indice": 1, "texto": "Reconocimiento de deuda"}],
 "destacar": ["maximo", "ultimo"]}
```

- La primera serie lleva area degradada (`"area": false` la quita); las demas van con trazo discontinuo y sin area, para no taparse.
- `umbral` dibuja una franja por debajo de las series (un limite legal, un pacto, un objetivo) y su rotulo entra en la leyenda.
- `anotaciones` marca con una linea vertical un hecho de contexto en el punto `indice` (base cero).
- `destacar` escribe la cifra en `maximo`, `minimo`, `primero` o `ultimo`. Por serie: `series[].destacar`.
- El eje empieza en cero y su tope es la cifra redonda inmediatamente superior. No admite negativos.

### `chispa` — minigrafico de tendencia dentro de un indicador

```json
{"tipo": "chispa", "valores": [12400, 21800, 28900, 36200, 42180.5], "etiquetas": ["Enero", "Septiembre"], "resumen": "Al alza de enero a septiembre"}
```

Muestra **forma**, no magnitud: no lleva ejes ni cifras, y su escala si arranca en el minimo. Con `etiquetas` el motor escribe la nota «Enero – Septiembre: +240 %»; `nota` la sustituye por un texto propio.

### `medidor` — semicirculo para un porcentaje de algo

```json
{"tipo": "medidor", "valor": 7, "maximo": 10, "unidad": "dias", "cifra": "70 %", "rotulo": "del plazo de diez dias consumido", "tramos": [60, 85]}
```

Sin `unidad`, la cifra central es el porcentaje de `valor` sobre `maximo` y el extremo dice «100 %»; con `unidad`, la cifra es el valor con su unidad y el extremo, el maximo (o la `cifra` que se indique). Si el valor supera el maximo, el arco se llena y la cifra muestra el valor real, nunca el recortado. El color va por tramos: hasta el primer porcentaje `--ok`, hasta el segundo `--aviso`, por encima `--riesgo`. Solo para valores que son un porcentaje de un maximo conocido: plazo consumido, avance, nivel de riesgo. `rotulo` va debajo, en HTML, porque dentro del SVG un texto largo se recorta.

### `cascada` — como se llega a un total

```json
{"tipo": "cascada", "unidad": "eur",
 "pasos": [{"rotulo": "Principal", "valor": 42180.5}, {"rotulo": "Intereses", "valor": 1947.32}, {"rotulo": "Pagos", "valor": -5600}],
 "total": {"rotulo": "A reclamar"}}
```

El total lo calcula el motor: nunca se escribe. Un valor negativo baja la columna y se pinta en `--riesgo`. Solo conceptos que suman al total.

### `matriz` — riesgo e impacto

```json
{"tipo": "matriz", "filas": ["Alta", "Media", "Baja"], "columnas": ["Bajo", "Medio", "Alto"],
 "eje_filas": "Probabilidad", "eje_columnas": "Impacto",
 "elementos": [{"nombre": "Prescripcion de la accion", "fila": "Alta", "columna": "Alto"}],
 "zonas": {"ok": "Asumir", "aviso": "Vigilar", "riesgo": "Actuar ya"}}
```

De dos a cuatro niveles por eje: mas niveles no dan precision, solo ruido. `filas` van de arriba abajo (la mas grave primero) y `columnas` de izquierda a derecha (la mas grave al final). Cada elemento es un circulo numerado en su celda y su nombre va en la lista de debajo. La zona de cada celda se calcula sola y lleva escrito que hacer.

### `plazos` — varios plazos en un calendario comun con la marca de hoy

```json
{"tipo": "plazos", "hoy": "2026-09-24",
 "plazos": [{"rotulo": "Plazo del burofax", "inicio": "2026-09-17", "fin": "2026-09-27"}]}
```

Fechas en `AAAA-MM-DD`. Todos los plazos comparten escala, que es lo unico que da sentido a la linea de hoy. El motor colorea: vencido en gris, en curso en `--aviso`, futuro con la serie. Cada barra lleva su fecha de vencimiento. La tabla de datos anade los dias que quedan.

### `anillo` y `tarta` — peso de cada parte sobre el total

```json
{"tipo": "anillo", "unidad": "eur",
 "porciones": [{"rotulo": "Principal", "valor": 12000}, {"rotulo": "Intereses", "valor": 1450}, {"rotulo": "Costas", "valor": 800}],
 "centro": {"rotulo": "total"}}
```

Maximo seis porciones: a partir de ahi el motor agrupa las menores en «Otros». Los porcentajes de la leyenda los calcula el motor. El anillo pone el total en el centro (o `centro.cifra`); la tarta no tiene centro. Para tres o cuatro partes es preferible el anillo; para comparar partidas entre si, siempre `barras`.

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

Modificadores: `es-ok`, `es-atencion`, `es-riesgo`. Maximo cuatro por fila. Si la cifra sale de un grafico, se escribe `<p class="cifra" data-cifra="clave"></p>` y se declara en `cifras`; si no, va como texto. La clase `aparece` anade la animacion escalonada de entrada, que se desactiva sola en impresion y para quien pide movimiento reducido.

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

Presente en la maqueta de herramienta interactiva (`maquetas-reportes.md`). Cada punto es un `input type="checkbox"` con su `label`; la barra y el contador se actualizan solos. Para anadir puntos basta replicar el `li`: el script cuenta los elementos existentes, no un numero fijo.

### Panel de entrada y recalculo

Estructura, script y contrato de `calcular` en la maqueta `herramienta_interactiva` de `maquetas-reportes.md`. Los valores introducidos se vuelcan siempre con `textContent`, nunca con `innerHTML`.

### Figura con fotografia

Cuando una foto aporta de verdad (portada de un informe, evidencia de un caso), se incrusta como `data:` URI conforme a las reglas de `anatomia-documento-visual.md` (JPEG comprimido, menos de 30 KB, licencia que permita el uso). Estilos con tokens, a anadir junto al resto del CSS:

```css
figure{margin:var(--e4) 0 0}
figure img{display:block;width:100%;max-width:520px;height:auto;border-radius:var(--radio-s);border:1px solid var(--borde)}
figcaption{font-size:.78rem;color:var(--apagado);margin-top:var(--e2);max-width:520px}
```

```html
<figure>
  <img src="data:image/jpeg;base64,..." alt="Descripcion literal de lo que se ve en la foto.">
  <figcaption>Pie que conecta la foto con el dato. Foto: Autor, "Titulo", origen, licencia (URL).</figcaption>
</figure>
```

El `alt` describe la imagen; el `figcaption` la acredita **siempre** (autor, titulo, origen, licencia con URL), tambien cuando la licencia no lo exige.

### Pie del reporte

Lo trae la base: la lista de fuentes la compone el motor a partir de `fuentes` y solo se rellena `{{PIE_AVISO_LEGAL}}`. No se anade otro pie.
