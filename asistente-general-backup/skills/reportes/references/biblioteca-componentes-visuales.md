# Biblioteca de componentes visuales

Todo lo que se inserta en un artefacto usa los tokens de `:root` de la base (`--superficie`, `--borde`, `--acento`, `--c1` a `--c6`, escala `--e1` a `--e6`). Por eso hereda cualquier tema (`temas-visuales.md`), su versión oscura y la impresión sin tocar nada. Las clases y los identificadores están en español y **no se renombran**: lo que cambia de idioma es el texto visible.

---

## Parte I. Como se declara un gráfico

Los gráficos **no se dibujan a mano ni se calculan coordenadas**. Se declaran en dos sitios con el mismo nombre:

1. **El hueco**, donde debe aparecer: `<figure class="grafico" data-grafico="evolucion"></figure>`. El minigráfico de un indicador usa `<div class="tendencia" data-grafico="tendencia"></div>`.
2. **Los datos**, dentro del bloque `<script type="application/json" id="datos-reporte">` de la base, en `graficos.evolucion`.

El motor de la base dibuja el SVG, calcula escalas, ejes y porcentajes, rellena la descripción accesible, añade debajo la tabla de datos desplegable con descarga en CSV, escribe la línea de fuente del gráfico y compone el pie de fuentes del documento. Si un gráfico tiene un error de datos, en su lugar aparece un recuadro rojo que dice qué falta; nunca un gráfico equivocado.

### Estructura del bloque de datos

```json
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "ine": {"nombre": "INE, Estadística de nacimientos", "url": "https://www.ine.es/...", "consulta": "2026-10-11"},
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

- **`idioma`** y **`moneda`** fijan el formato de cifras y fechas (miles con punto en español, siempre, también con cuatro cifras).
- **`fuentes`**: cada fuente con `nombre`, `url` si viene de internet y `consulta` en formato `AAAA-MM-DD` (la fecha real de la consulta en la sesión, nunca inventada). Los gráficos las citan por su clave.
- **`cifras`**: cifras sueltas del texto. Cada una es `{"valor": 1234, "unidad": "eur"}`, una operación entre otras dos cifras (o números) —`{"operacion": "porcentaje", "a": "cobrado", "b": "facturado", "unidad": "pct"}`, con `suma`, `diferencia`, `producto`, `cociente` o `porcentaje` (a sobre b por cien); el 30 % de una cifra es `producto` por 0.3— o un cálculo sobre un gráfico: `{"de": "grafico", "calculo": "suma", "serie": 0, "unidad": "eur"}`. Cálculos: `suma`, `media`, `maximo`, `minimo`, `primero`, `ultimo`, `cuenta`, `variacion` (porcentaje entre el primero y el último) y `porcentaje` (peso de `"elemento": "rotulo"` sobre el total). En el HTML se escriben con `<span data-cifra="principal"></span>`; en las diapositivas, con `{cifra:principal}` dentro del texto. `"decimales": 0` quita los decimales (una cifra grande de portada); por defecto los importes llevan dos. **Toda cifra que se obtiene de otras (un porcentaje de cumplimiento, una diferencia con el objetivo, un total) se declara así y nunca se calcula a mano.**
- **`fuentes[].consulta`** es la fecha en que se obtuvieron los datos: la de la consulta en internet, la de exportación que indique el usuario o, si no indica ninguna, la fecha de la conversación.
- **`marca`** (colores, logo y pie del despacho): va en el motor de la base, contrato en `modulos-motor.md`. **Plazos en días hábiles** (`dias_habiles`, `vencimiento`): módulo opcional, contrato en el mismo documento.
- **`textos`**: solo si el documento no está en español ni en inglés, para traducir los rótulos que escribe el motor; las claves son las de `TEXTOS_BASE` en el script de la base (y las de `TX` en el módulo de diagramas).

### Campos comunes a todos los gráficos

| Campo | Uso |
| :--- | :--- |
| `tipo` | Obligatorio. Uno de los tipos de la Parte II |
| `resumen` | La frase que lee un lector de pantalla: el dato principal resumido. Obligatorio en la práctica |
| `fuente` | Clave de `fuentes`, o lista de claves si el gráfico combina dos fuentes (`["cierre", "plan"]`). En línea y columnas puede ir por serie (`series[].fuente`) |
| `unidad` | `eur`, `pct`, `num`, `entero` o cualquier texto (`"dias"`, `"asuntos"`), que se añade detrás de la cifra |
| `color` | En elementos, series o porciones: `1` a `6` (serie `--c1` a `--c6`) o `ok`, `aviso`, `riesgo`. Sirve para mantener el mismo color para la misma parte en todos los gráficos |
| `tabla` | `false` para no añadir la tabla de datos desplegable |

Los valores que falten se escriben `null`: la línea se interrumpe y la columna no se pinta. Nunca se inventa un punto para cerrar una serie.

**Valores calculados dentro de un gráfico:** cualquier valor numérico de un gráfico o de un módulo (también los `valores` del mapa o los puntos de una dispersión) puede ser `"@clave"`, que el motor sustituye por la cifra `clave` de `cifras`. Así una cascada de la propuesta a la liquidación definitiva usa `"valor": "@baja_cuota"` con `baja_cuota` declarada como `{"operacion": "diferencia", "a": "cuota_definitiva", "b": "cuota_propuesta"}`, y ningún importe se escribe dos veces ni se resta a mano. Una cifra calculada sobre un gráfico ignora los valores de ese gráfico que sean referencias.

---

## Parte II. Los tipos

### `barras` — barras horizontales

La forma más robusta para comparar partidas.

```json
{"tipo": "barras", "unidad": "eur", "fuente": "cliente",
 "elementos": [{"rotulo": "Factura 2025/118", "valor": 18400}, {"rotulo": "Factura 2025/131", "valor": 11250}]}
```

Se ordenan de mayor a menor salvo `"orden": "original"`, que se usa cuando el orden cronológico es el que informa.

### `columnas` — barras verticales, una o varias series

```json
{"tipo": "columnas", "unidad": "eur", "etiquetas": ["1T", "2T", "3T", "4T"],
 "series": [{"nombre": "2025", "valores": [12000, 16000, 9000, 14000]}, {"nombre": "2026", "valores": [14000, 18500, 11000, null]}]}
```

Con más de ocho categorías se usan `barras`: las etiquetas dejan de leerse. `"valores": false` quita las cifras encima de las columnas.

### `apiladas` — composición de cada periodo

Mismo formato que `columnas`. Encima de cada columna aparece el total. Con `"cien": true` cada columna se normaliza al cien por cien: **solo cuando importa la proporción**, nunca el volumen, porque una columna de 200 euros y otra de 200.000 se verían idénticas. No admite negativos.

### `linea` — evolución, con área, banda, anotaciones y destacados

```json
{"tipo": "linea", "unidad": "eur", "etiquetas": ["Ene", "Feb", "Mar"],
 "series": [{"nombre": "Principal", "valores": [12400, 21800, 28900]}, {"nombre": "Cobrado", "valores": [0, 2100, 2100]}],
 "umbral": {"desde": 0, "hasta": 15000, "rotulo": "Umbral de riesgo asumido"},
 "anotaciones": [{"indice": 1, "texto": "Reconocimiento de deuda"}],
 "destacar": ["maximo", "ultimo"]}
```

- La primera serie lleva área degradada (`"area": false` la quita); las demás van con trazo discontinuo y sin área, para no taparse.
- `umbral` dibuja una franja por debajo de las series (un límite legal, un pacto, un objetivo) y su rotulo entra en la leyenda. Es verde por defecto (la zona correcta); `"color": "riesgo"` la marca como zona a evitar.
- `anotaciones` marca con una línea vertical un hecho de contexto en el punto `indice` (base cero).
- `destacar` escribe la cifra en `maximo`, `minimo`, `primero` o `ultimo`. Por serie: `series[].destacar`.
- El eje empieza en cero y su tope es la cifra redonda inmediatamente superior. No admite negativos.

### `chispa` — minigráfico de tendencia dentro de un indicador

```json
{"tipo": "chispa", "valores": [12400, 21800, 28900, 36200, 42180.5], "etiquetas": ["Enero", "Septiembre"], "resumen": "Al alza de enero a septiembre"}
```

Muestra **forma**, no magnitud: no lleva ejes ni cifras, y su escala sí arranca en el mínimo. Con `etiquetas` el motor escribe la nota «Enero – Septiembre: +240 %»; `nota` la sustituye por un texto propio.

### `medidor` — semicírculo para un porcentaje de algo

```json
{"tipo": "medidor", "valor": 7, "maximo": 10, "unidad": "dias", "cifra": "70 %", "rotulo": "del plazo de diez días consumido", "tramos": [60, 85]}
```

Sin `unidad`, la cifra central es el porcentaje de `valor` sobre `maximo` y el extremo dice «100 %»; con `unidad`, la cifra es el valor con su unidad y el extremo, el máximo (o la `cifra` que se indique). Si el valor supera el máximo, el arco se llena y la cifra muestra el valor real, nunca el recortado. El color va por tramos: hasta el primer porcentaje `--ok`, hasta el segundo `--aviso`, por encima `--riesgo`. Solo para valores que son un porcentaje de un máximo conocido: plazo consumido, avance, nivel de riesgo. `rotulo` va debajo, en HTML, porque dentro del SVG un texto largo se recorta.

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
 "elementos": [{"nombre": "Prescripción de la acción", "fila": "Alta", "columna": "Alto"}],
 "zonas": {"ok": "Asumir", "aviso": "Vigilar", "riesgo": "Actuar ya"}}
```

De dos a cuatro niveles por eje: más niveles no dan precisión, solo ruido. `filas` van de arriba abajo (la más grave primero) y `columnas` de izquierda a derecha (la más grave al final). Cada elemento es un circulo numerado en su celda y su nombre va en la lista de debajo. La zona de cada celda se calcula sola y lleva escrito que hacer.

### `plazos` — varios plazos en un calendario común con la marca de hoy

```json
{"tipo": "plazos", "hoy": "2026-09-24",
 "plazos": [{"rotulo": "Plazo del burofax", "inicio": "2026-09-17", "fin": "2026-09-27"}]}
```

Fechas en `AAAA-MM-DD`. Una fase abierta, sin fin conocido, se declara sin `fin`: llega hasta hoy y se rotula «en curso». Una fecha prevista y no notificada lleva `"aproximada": true`: barra con borde discontinuo y «≈» delante de la fecha. Todos los plazos comparten escala, que es lo único que da sentido a la línea de hoy. El motor colorea: vencido en gris, en curso en `--aviso`, futuro con la serie. Cada barra lleva su fecha de vencimiento. La tabla de datos añade los días que quedan.

### `anillo` y `tarta` — peso de cada parte sobre el total

```json
{"tipo": "anillo", "unidad": "eur",
 "porciones": [{"rotulo": "Principal", "valor": 12000}, {"rotulo": "Intereses", "valor": 1450}, {"rotulo": "Costas", "valor": 800}],
 "centro": {"rotulo": "total"}}
```

Máximo seis porciones: a partir de ahí el motor agrupa las menores en «Otros». Los porcentajes de la leyenda los calcula el motor. El anillo pone el total en el centro (o `centro.cifra`); la tarta no tiene centro. Para tres o cuatro partes es preferible el anillo; para comparar partidas entre sí, siempre `barras`.

### `bala` — real frente a objetivo

```json
{"tipo": "bala", "unidad": "eur",
 "elementos": [{"rotulo": "Facturación", "valor": 82000, "objetivo": 100000, "tramos": [60000, 90000, 120000]}]}
```

Una fila por elemento: la barra fina es el valor, la marca vertical el objetivo y los tramos de fondo (opcionales) la valoración cualitativa, de malo a bueno. La tabla de datos añade el porcentaje de cumplimiento. Mejor que varios medidores cuando hay varios objetivos que comparar.

### `divergentes` — saldos con signo alrededor de cero

```json
{"tipo": "divergentes", "unidad": "eur", "nombres": {"positivo": "Cobros", "negativo": "Pagos"},
 "elementos": [{"rotulo": "Enero", "valor": 12000}, {"rotulo": "Febrero", "valor": -8000}]}
```

Los positivos van a la derecha en `--ok` y los negativos a la izquierda en `--riesgo`; `colores` (`{"positivo": 1, "negativo": 2}`) los cambia cuando el signo no es bueno ni malo (a favor y en contra de una tesis). La escala es simétrica.

### `diagrama` — cajas y flechas

Procesos, flujos, organigramas, estructuras societarias, relaciones entre partes y quién hace que. Va en un módulo aparte: contrato de datos y código en `modulos-motor.md`.

### Tipos de los módulos opcionales

Se declaran igual que los anteriores (hueco `data-grafico` y datos en `graficos`), pero su código no va en la base: se copia el módulo correspondiente de `modulos-motor.md` después del motor, solo en los artefactos que los usan. Contrato de datos de cada uno en esa referencia.

| Módulo | Tipos | Para que |
| :--- | :--- | :--- |
| `avanzados` | `dispersion`, `histograma`, `radar`, `embudo`, `treemap`, `pendiente`, `halteras`, `piramide`, `calendario`, `pictograma` | Relaciones entre magnitudes, reparto de muchos valores, perfiles, etapas, muchas partidas, cambio entre dos momentos, dos grupos enfrentados, días de actividad, una proporción en figuras |
| `analiticos` | `area_apilada`, `pareto`, `escalones`, `cajas`, `tornado`, `rango`, `mapa_calor`, `sankey`, `anillos`, `puntuacion` | Composición en el tiempo, concentración (80/20), valores que rigen a tramos, distribución por grupos, sensibilidad, posición en una horquilla legal, dos dimensiones, flujos, avance de varios objetivos, notas en escala corta |
| `seguimiento` | `progreso`, `semaforos`, `linea_tiempo` | Avance por fase, estado de cada punto de control, hitos sobre una escala real de fechas |
| `diagramas` | `diagrama` (capas, árbol, radial, carriles) | Procesos, organigramas, relaciones, quién hace que |
| `mapa` (+ `mapa_ccaa` o `mapa_provincias`) | `mapa` | Dónde se concentra algo en España |
| `qr`, `iconos` | `qr`, iconos en línea | Llevar al lector en papel a una fuente; iconos en indicadores |

### Cifras con variación

Una cifra de `cifras` con `"signo": true` se muestra con su signo y una flecha (▲ +4,2 % o ▼ -4,2 %), en verde si es favorable y en rojo si no. Por defecto subir es bueno; `"mejor": "bajar"` lo invierte (morosidad, plazos, costes) y `"mejor": "neutro"` muestra el signo sin color (más asuntos abiertos no es bueno ni malo). Variación entre el primer y el último valor de un gráfico: `{"de": "evolucion", "calculo": "variacion", "unidad": "pct", "signo": true}`; diferencia en unidades: `"calculo": "diferencia"`.

### Familias: gráficos que se cambian entre si

El usuario puede cambiar la forma de un gráfico desde el visor de la app, sin la IA, pero solo por otro tipo que lea **exactamente los mismos datos**: no se convierte nada. Estas son las familias del catálogo `catalogo-reporte` de la base; un tipo que no está en ninguna no se puede cambiar así (se pide en el chat).

| Familia | Datos que comparten | Tipos |
| :--- | :--- | :--- |
| `series` | `etiquetas` y `series: [{nombre, valores}]` | `columnas`, `apiladas`, `linea`, `area_apilada`, `escalones` |
| `partidas` | `elementos: [{rotulo, valor}]`, magnitudes que se comparan | `barras`, `pareto`, `divergentes`, `treemap` |
| `porciones` | `porciones: [{rotulo, valor}]` | `anillo`, `tarta` |
| `avance` | `elementos: [{rotulo, valor, maximo}]`, avance sobre un máximo | `progreso`, `anillos` |

Los campos propios de un tipo (`umbral` de la línea, `cien` de las apiladas, `nombres` de las divergentes) se conservan y los demás tipos los ignoran. `bala` y `puntuacion` también llevan `elementos`, pero su valor significa otra cosa (frente a un objetivo, una nota en una escala): quedan fuera. Al elegir, la app avisa si un tipo no conviene con estos datos (una tarta con más de seis porciones, un pareto con menos de tres partidas, unas divergentes sin negativos, unas columnas con más de doce categorías) o si no se puede dibujar. Las alternativas que ofrece son las cargadas en el motor: los tipos de módulo solo aparecen si su módulo va copiado: `area_apilada`, `escalones`, `pareto` y `anillos` (analíticos), `treemap` (avanzados) y `progreso` (seguimiento).

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

Modificadores: `es-ok`, `es-atencion`, `es-riesgo`. Máximo cuatro por fila. Si la cifra sale de un gráfico, se escribe `<p class="cifra" data-cifra="clave"></p>` y se declara en `cifras`; si no, va como texto. La clase `aparece` añade la animación escalonada de entrada, que se desactiva sola en impresión y para quien pide movimiento reducido.

### Aviso destacado

```html
<div class="aviso riesgo">
  <span class="titulo">Plazo de caducidad</span>
  La accion de despido caduca a los veinte dias habiles desde la fecha de efectos.
</div>
```

Variantes: sin clase (informativo), `favorable`, `riesgo`. Uno cada varias secciones: si todo está destacado, nada lo está.

### Cronología de hitos

```html
<ol class="cronologia">
  <li>
    <span class="fecha">12 de marzo de 2026</span>
    <span class="hito">Requerimiento extrajudicial</span><br>
    Burofax con acuse de recibo remitido al domicilio social.
  </li>
</ol>
```

Orden cronológico ascendente y fecha cierta o `{{FECHA_PENDIENTE}}`; nunca una fecha estimada presentada como real.

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

Las columnas numéricas llevan `class="cifra"`. Los distintivos admiten `ok`, `atencion` y `riesgo`. En impresión, el `thead` se repite en cada página.

### Lista de verificación con progreso

Presente en la maqueta de herramienta interactiva (`maquetas-reportes.md`). Cada punto es un `input type="checkbox"` con su `label`; la barra y el contador se actualizan solos. Para añadir puntos basta replicar el `li`: el script cuenta los elementos existentes, no un número fijo.

### Panel de entrada y recálculo

Estructura, script y contrato de `calcular` en la maqueta `herramienta_interactiva` de `maquetas-reportes.md`. Los valores introducidos se vuelcan siempre con `textContent`, nunca con `innerHTML`.

### Figura con fotografía

Cuando una foto aporta de verdad (portada de un informe, evidencia de un caso), se incrusta como `data:` URI conforme a las reglas de `anatomia-artefacto.md` (JPEG comprimido, menos de 30 KB, licencia que permita el uso). Estilos con tokens, a añadir junto al resto del CSS:

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

El `alt` describe la imagen; el `figcaption` la acredita **siempre** (autor, título, origen, licencia con URL), también cuando la licencia no lo exige.

### Tabla de jurisprudencia

Para fundamentar con resoluciones, siempre verificadas en la sesión en el CENDOJ u otra fuente oficial (si no se pueden verificar, no entran):

```html
<div class="tabla">
  <table>
    <caption>Resoluciones que sostienen la reclamacion</caption>
    <thead><tr><th>Tribunal y fecha</th><th>Referencia</th><th>Que dice</th><th>Relevancia</th></tr></thead>
    <tbody>
      <tr><td>{{TRIBUNAL}}, {{FECHA}}</td><td>{{ROJ_O_ECLI}}</td><td>{{DOCTRINA_EN_UNA_FRASE}}</td><td><span class="distintivo ok">Directa</span></td></tr>
    </tbody>
  </table>
</div>
```

La referencia es la oficial (Roj o ECLI) y la URL de cada resolución va en `fuentes`, que la recoge el pie. Relevancia: `ok` directa, `atencion` por analogía, `riesgo` en contra. Si se quiere que el lector en papel llegue a la resolución, un QR con su URL.

### Pie del artefacto

Lo trae la base: la lista de fuentes la compone el motor a partir de `fuentes` y solo se rellena `{{PIE_AVISO_LEGAL}}`. No se añade otro pie.
