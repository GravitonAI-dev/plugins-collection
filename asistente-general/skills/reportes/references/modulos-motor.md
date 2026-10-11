# Modulos opcionales del motor

Algunos tipos de grafico pesan demasiado para ir en todos los reportes. Viven aqui como **modulos**: un `<script>` que se copia integro, sin modificarlo, **justo despues del script del motor** (antes de `</body>` y antes del script de la maqueta, si la maqueta tiene uno) y solo en los reportes que usan ese tipo. El modulo registra su tipo en el motor y, a partir de ahi, se declara en `datos-reporte` como cualquier otro grafico.

Si un reporte declara un tipo de modulo pero no copia el modulo, el grafico muestra el recuadro rojo «tipo desconocido».

---

## Diagramas con conectores (`diagrama`)

Cajas unidas por flechas: procesos, flujos de un procedimiento, cadenas de hechos, organigramas, estructuras societarias, relaciones entre partes y quien hace que. El modelo **no coloca nada**: declara los nodos y las conexiones, y el modulo calcula la disposicion, ajusta el texto de cada caja en varias lineas y traza las flechas con su rotulo.

```json
{"tipo": "diagrama", "disposicion": "capas", "direccion": "horizontal", "fuente": "cliente",
 "nodos": [
   {"id": "contrato", "texto": "Contrato de suministro", "forma": "inicio"},
   {"id": "impago", "texto": "Impago de siete facturas", "grupo": 3},
   {"id": "pago", "texto": "¿Paga en el plazo del requerimiento?", "forma": "decision"},
   {"id": "fin", "texto": "Archivo del expediente", "forma": "inicio", "grupo": 2},
   {"id": "monitorio", "texto": "Peticion de monitorio", "grupo": 1}
 ],
 "conexiones": [
   {"de": "contrato", "a": "impago"},
   {"de": "impago", "a": "pago", "texto": "burofax"},
   {"de": "pago", "a": "fin", "texto": "si"},
   {"de": "pago", "a": "monitorio", "texto": "no", "estilo": "destacada"}
 ],
 "grupos": {"1": "Via judicial", "2": "Cierre", "3": "Hechos"}}
```

| Campo | Uso |
| :--- | :--- |
| `disposicion` | `capas` (flujos y procesos, por defecto), `arbol` (organigramas, estructuras societarias, de arriba abajo), `radial` (un nodo central y sus relaciones) o `carriles` (quien hace que: una franja por actor) |
| `direccion` | En `capas`: `horizontal` o `vertical`. Si no se indica, el modulo elige: hasta cinco pasos encadenados en horizontal y, a partir de ahi, en vertical |
| `nodos[].forma` | `caja` (por defecto), `inicio` (inicio o fin, con extremos redondos), `decision` (rombo) o `nota` (borde discontinuo) |
| `nodos[].grupo` | Color de la serie, `1` a `6` o `ok`, `aviso`, `riesgo`. `grupos` da el nombre de cada grupo para la leyenda |
| `nodos[].carril` | En `carriles`, el actor al que pertenece; `carriles` fija el orden de las franjas |
| `centro` | En `radial`, el id del nodo central (por defecto, el primero) |
| `conexiones[].texto` | Rotulo corto de la flecha: «si», «no», «20 dias», «burofax» |
| `conexiones[].estilo` | `discontinua` (relacion indirecta o eventual) o `destacada` (el camino que importa) |

Reglas:

- **Solo los pasos que ha descrito el usuario o que constan en el expediente.** Si el flujo queda incompleto (falta que pasa cuando si paga, por ejemplo), se pregunta en el chat; no se completa con pasos supuestos.
- **Colores de grupo:** la serie `1` a `6` para distinguir fases o actores; `ok`, `aviso` y `riesgo` solo cuando el nodo es un resultado bueno, dudoso o malo (cobro, archivo, sancion).
- **Maximo 24 nodos.** Un diagrama mayor no se lee: se divide en dos o se resume.
- Texto de cada caja corto, en una o dos lineas. Los detalles van en el texto del reporte, no dentro de la caja.
- Una conexion que vuelve atras (un ciclo) se dibuja por fuera, curvada. Si hay muchas, el proceso esta mal descrito o necesita otra forma.
- El diagrama va en una tarjeta `ancho-total` si tiene mas de tres pasos en horizontal. En una diapositiva caben a lo ancho hasta cinco pasos; con mas, el modulo lo pasa a vertical o conviene dividirlo en dos diapositivas.

```js modulo=diagramas
<script>
/* Modulo de diagramas con conectores para el motor de reportes. Se copia integro,
   despues del motor, solo en los reportes con algun grafico de tipo diagrama. */
(function(){
"use strict";
var R = Reportes, svg = R.svg, r1 = R.r1, CAR = 6.7, LINEA = 15;
var TX = Object.assign(/^en/.test(document.documentElement.lang) ? {desde: "From", hacia: "To", rotulo: "Label"} : {desde: "Desde", hacia: "Hacia", rotulo: "Rotulo"}, R.T);
var LETRA_NODO = {"font-size": 12, fill: "var(--texto)", "font-weight": 560}, LETRA_CONEXION = {"font-size": 10.5, fill: "var(--apagado)", "font-weight": 600};
function trocear(texto, max) {
  var lineas = [], actual = "";
  String(texto).split(/\s+/).forEach(function (p) {
    if (actual && (actual + " " + p).length > max) { lineas.push(actual); actual = p; }
    else actual = actual ? actual + " " + p : p;
  });
  if (actual) lineas.push(actual);
  return lineas;
}
function medir(n, estrecho) {
  var decision = n.forma === "decision";
  n.lineas = trocear(n.texto, estrecho ? (decision ? 12 : 14) : decision ? 16 : 22);
  var largo = Math.max.apply(null, n.lineas.map(function (l) { return l.length; }));
  n.w = Math.max(84, Math.min(196, largo * CAR + 28));
  n.h = n.lineas.length * LINEA + 20;
  if (decision) { n.w = r1(n.w * 1.4); n.h = r1(n.h * 1.6); }
}
/* Marca las conexiones que cierran un ciclo para no seguirlas al calcular capas. */
function marcarCiclos(nodos, conexiones) {
  var estado = {}, salen = {};
  nodos.forEach(function (n) { salen[n.id] = []; });
  conexiones.forEach(function (c) { salen[c.de].push(c); });
  function visitar(id) {
    estado[id] = 1;
    salen[id].forEach(function (c) { if (estado[c.a] === 1) c.atras = true; else if (!estado[c.a]) visitar(c.a); });
    estado[id] = 2;
  }
  nodos.forEach(function (n) { if (!estado[n.id]) visitar(n.id); });
}
/* Capa de cada nodo: el camino mas largo desde un origen. */
function capas(nodos, conexiones, porId) {
  nodos.forEach(function (n) { n.capa = 0; });
  for (var k = 0; k < nodos.length; k++) {
    var cambio = false;
    conexiones.forEach(function (c) { if (!c.atras && porId[c.a].capa < porId[c.de].capa + 1) { porId[c.a].capa = porId[c.de].capa + 1; cambio = true; } });
    if (!cambio) break;
  }
  var grupos = [];
  nodos.forEach(function (n) { (grupos[n.capa] = grupos[n.capa] || []).push(n); });
  /* Dos pasadas de baricentro para reducir cruces. */
  for (var pasada = 0; pasada < 2; pasada++) {
    grupos.forEach(function (capa, i) {
      if (!i) return;
      capa.forEach(function (n) {
        var padres = conexiones.filter(function (c) { return c.a === n.id && !c.atras; }).map(function (c) { return grupos[porId[c.de].capa].indexOf(porId[c.de]); });
        n.orden = padres.length ? padres.reduce(function (s, v) { return s + v; }, 0) / padres.length : capa.indexOf(n);
      });
      capa.sort(function (a, b) { return a.orden - b.orden; });
    });
  }
  return grupos;
}
function colocarCapas(grupos, vertical) {
  var hueco = !vertical && grupos.length > 4 ? 40 : 64, sep = 20, pos = 0;
  var grosor = grupos.map(function (capa) { return Math.max.apply(null, capa.map(function (n) { return vertical ? n.h : n.w; })); });
  var largo = grupos.map(function (capa) { return capa.reduce(function (s, n) { return s + (vertical ? n.w : n.h) + sep; }, -sep); });
  var mayor = Math.max.apply(null, largo);
  grupos.forEach(function (capa, i) {
    var c = (mayor - largo[i]) / 2;
    capa.forEach(function (n) {
      var tam = vertical ? n.w : n.h;
      if (vertical) { n.x = c + tam / 2; n.y = pos + grosor[i] / 2; } else { n.x = pos + grosor[i] / 2; n.y = c + tam / 2; }
      c += tam + sep;
    });
    pos += grosor[i] + hueco;
  });
}
function colocarArbol(nodos, conexiones, porId) {
  var hijos = {}, padre = {}, cursor = 0, sep = 22;
  nodos.forEach(function (n) { hijos[n.id] = []; });
  conexiones.forEach(function (c) { if (!c.atras && !padre[c.a]) { padre[c.a] = c.de; hijos[c.de].push(porId[c.a]); } });
  var filas = {};
  function profundidad(n, d) { n.capa = d; filas[d] = Math.max(filas[d] || 0, n.h); hijos[n.id].forEach(function (h) { profundidad(h, d + 1); }); }
  /* Cada subarbol ocupa lo que el mayor de su caja o de sus hijos: un padre ancho con un
     solo hijo estrecho no invade a sus vecinos. */
  function ancho(n) {
    var hs = hijos[n.id], suma = hs.reduce(function (s, h) { return s + ancho(h); }, 0) + sep * Math.max(0, hs.length - 1);
    return (n.span = Math.max(n.w, suma));
  }
  function colocar(n, izq) {
    var hs = hijos[n.id], ocupado = hs.reduce(function (s, h) { return s + h.span; }, 0) + sep * Math.max(0, hs.length - 1), x = izq + (n.span - ocupado) / 2;
    hs.forEach(function (h) { colocar(h, x); x += h.span + sep; });
    n.x = izq + n.span / 2;
  }
  nodos.filter(function (n) { return !padre[n.id]; }).forEach(function (raiz) { profundidad(raiz, 0); ancho(raiz); colocar(raiz, cursor); cursor += raiz.span + sep * 2; });
  var y = 0, alturas = [];
  Object.keys(filas).sort(function (a, b) { return a - b; }).forEach(function (d) { alturas[d] = y + filas[d] / 2; y += filas[d] + 56; });
  nodos.forEach(function (n) { n.y = alturas[n.capa]; });
}
function colocarRadial(nodos, centro) {
  var resto = nodos.filter(function (n) { return n !== centro; });
  var mw = Math.max.apply(null, resto.map(function (n) { return n.w; })), mh = Math.max.apply(null, resto.map(function (n) { return n.h; }));
  /* Elipse que deja libre la caja central y crece con el numero de nodos. */
  var crece = Math.max(1, resto.length / 6), rx = (centro.w / 2 + mw / 2 + 56) * crece, ry = (centro.h / 2 + mh / 2 + 48) * crece;
  centro.x = 0; centro.y = 0;
  resto.forEach(function (n, i) {
    var a = -Math.PI / 2 + i * 2 * Math.PI / resto.length;
    n.x = r1(Math.cos(a) * rx); n.y = r1(Math.sin(a) * ry);
  });
}
function colocarCarriles(g, nodos, conexiones, porId) {
  capas(nodos, conexiones, porId);
  var carriles = g.carriles || nodos.map(function (n) { return n.carril; }).filter(function (c, i, a) { return c && a.indexOf(c) === i; });
  var ancho = [], alto = [], y = 0;
  nodos.forEach(function (n) {
    n.fila = Math.max(0, carriles.indexOf(n.carril));
    ancho[n.capa] = Math.max(ancho[n.capa] || 0, n.w);
  });
  var x = 120, xs = [];
  ancho.forEach(function (w, i) { xs[i] = x + w / 2; x += w + 56; });
  carriles.forEach(function (c, f) {
    var aqui = nodos.filter(function (n) { return n.fila === f; }), pila = {};
    var h = 0;
    aqui.forEach(function (n) { var k = pila[n.capa] || 0; n.sub = k; pila[n.capa] = k + 1; h = Math.max(h, (k + 1) * (n.h + 14)); });
    aqui.forEach(function (n) { n.x = xs[n.capa]; n.y = y + 18 + n.sub * (n.h + 14) + n.h / 2; });
    alto[f] = [y, Math.max(h, 40) + 22];
    y += alto[f][1];
  });
  return {carriles: carriles, franjas: alto, ancho: x};
}
/* Punto del borde de una caja en la direccion de otro punto. */
function borde(n, hacia) {
  var dx = hacia.x - n.x, dy = hacia.y - n.y;
  if (!dx && !dy) return {x: n.x, y: n.y};
  var e = Math.min(Math.abs(dx) ? n.w / 2 / Math.abs(dx) : Infinity, Math.abs(dy) ? n.h / 2 / Math.abs(dy) : Infinity);
  return {x: r1(n.x + dx * e), y: r1(n.y + dy * e)};
}
R.tipos.diagrama = function (fig, g, id) {
  var nodos = (g.nodos || []).map(function (n) { return Object.assign({}, n); }), porId = {};
  if (!nodos.length) throw new Error("faltan nodos");
  if (nodos.length > 24) throw new Error("mas de 24 nodos: divide el diagrama en dos");
  nodos.forEach(function (n) { if (!n.id || porId[n.id]) throw new Error("cada nodo necesita un id unico"); porId[n.id] = n; medir(n); });
  var conexiones = (g.conexiones || []).map(function (c) {
    if (!porId[c.de] || !porId[c.a]) throw new Error("la conexion " + c.de + " -> " + c.a + " une un nodo que no existe");
    return Object.assign({}, c);
  });
  marcarCiclos(nodos, conexiones);
  var disp = g.disposicion || "capas", vertical = disp === "arbol", carril = null;
  if (disp === "arbol") colocarArbol(nodos, conexiones, porId);
  else if (disp === "radial") { colocarRadial(nodos, porId[g.centro] || nodos[0]); }
  else if (disp === "carriles") carril = colocarCarriles(g, nodos, conexiones, porId);
  else {
    var grupos = capas(nodos, conexiones, porId);
    /* Sin direccion indicada, un flujo de mas de cinco pasos va en vertical: en horizontal no se leeria. */
    vertical = g.direccion ? g.direccion === "vertical" : grupos.length > 5;
    /* En horizontal con muchos pasos, cajas mas estrechas para que el flujo quepa a lo ancho. */
    if (!vertical && grupos.length > 4) nodos.forEach(function (n) { medir(n, true); });
    colocarCapas(grupos, vertical);
  }
  var x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
  nodos.forEach(function (n) { x0 = Math.min(x0, n.x - n.w / 2 - 18); y0 = Math.min(y0, n.y - n.h / 2 - 18); x1 = Math.max(x1, n.x + n.w / 2 + 18); y1 = Math.max(y1, n.y + n.h / 2 + 18); });
  if (carril) { x0 = 0; y0 = 0; y1 = Math.max(y1, carril.franjas.reduce(function (s, f) { return s + f[1]; }, 0)); }
  if (conexiones.some(function (c) { return c.atras; })) y1 += 44;
  var ancho = r1(x1 - x0), alto = r1(y1 - y0);
  var s = R.lienzo(fig, ancho, alto, g.resumen || "");
  s.setAttribute("viewBox", r1(x0) + " " + r1(y0) + " " + ancho + " " + alto);
  s.setAttribute("width", r1(ancho * R.escala(fig)));  /* tamano natural: solo se reduce si no cabe */
  var defs = svg("defs", {}, s), flecha = svg("marker", {id: "flecha-" + id, viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 9, markerHeight: 9, markerUnits: "userSpaceOnUse", orient: "auto-start-reverse"}, defs);
  svg("path", {d: "M0,0 L10,5 L0,10 z", fill: "var(--apagado)"}, flecha);
  if (carril) carril.carriles.forEach(function (nombre, f) {
    var fr = carril.franjas[f];
    svg("rect", {x: 0, y: fr[0], width: ancho, height: fr[1], fill: f % 2 ? "var(--superficie)" : "var(--superficie-2)"}, s);
    svg("text", Object.assign({x: 10, y: fr[0] + fr[1] / 2 + 4}, LETRA_NODO), s, R.recortar(nombre, 14));
  });
  conexiones.forEach(function (c) {
    var a = porId[c.de], b = porId[c.a], d, m;
    if (c.atras) {
      var yb = Math.max(a.y + a.h / 2, b.y + b.h / 2) + 34;
      d = "M " + a.x + " " + (a.y + a.h / 2) + " C " + a.x + " " + yb + ", " + b.x + " " + yb + ", " + b.x + " " + (b.y + b.h / 2);
      m = {x: (a.x + b.x) / 2, y: yb - 8};
    } else if (disp === "radial") {
      var p = borde(a, b), q = borde(b, a);
      d = "M " + p.x + " " + p.y + " L " + q.x + " " + q.y;
      m = {x: (p.x + q.x) / 2, y: (p.y + q.y) / 2};
    } else if (vertical) {
      var ya = a.y + a.h / 2, yb2 = b.y - b.h / 2, ym = (ya + yb2) / 2;
      d = "M " + a.x + " " + ya + " C " + a.x + " " + ym + ", " + b.x + " " + ym + ", " + b.x + " " + yb2;
      m = {x: (a.x + b.x) / 2, y: ym};
    } else {
      var xa = a.x + a.w / 2, xb = b.x - b.w / 2, xm = (xa + xb) / 2;
      d = "M " + xa + " " + a.y + " C " + xm + " " + a.y + ", " + xm + " " + b.y + ", " + xb + " " + b.y;
      m = {x: xm, y: (a.y + b.y) / 2};
    }
    var destacada = c.estilo === "destacada";
    svg("path", {d: d, fill: "none", stroke: destacada ? "var(--acento)" : "var(--apagado)", "stroke-width": destacada ? 2.4 : 1.5,
      "stroke-dasharray": c.estilo === "discontinua" ? "5 4" : null, "marker-end": "url(#flecha-" + id + ")"}, s);
    if (c.texto) {
      var w = String(c.texto).length * 6.2 + 12;
      svg("rect", {x: r1(m.x - w / 2), y: r1(m.y - 9), width: r1(w), height: 18, rx: 9, fill: "var(--superficie)", stroke: "var(--borde)"}, s);
      svg("text", Object.assign({x: r1(m.x), y: r1(m.y + 4), "text-anchor": "middle"}, LETRA_CONEXION), s, c.texto);
    }
  });
  nodos.forEach(function (n, i) {
    /* grupo puede venir como numero o como texto ("2"): se normaliza igual que en la leyenda. */
    var c = n.grupo === undefined ? "var(--acento)" : R.color(isNaN(n.grupo) ? n.grupo : +n.grupo, 0), grupo = svg("g", {}, s), x = r1(n.x - n.w / 2), y = r1(n.y - n.h / 2);
    var comun = {fill: c, "fill-opacity": ".12", stroke: c, "stroke-width": 1.6};
    if (n.forma === "decision") svg("polygon", Object.assign({points: [n.x + "," + y, (x + n.w) + "," + n.y, n.x + "," + (y + n.h), x + "," + n.y].join(" ")}, comun), grupo);
    else svg("rect", Object.assign({x: x, y: y, width: n.w, height: n.h, rx: n.forma === "inicio" ? n.h / 2 : n.forma === "nota" ? 3 : 8,
      "stroke-dasharray": n.forma === "nota" ? "4 3" : null}, comun), grupo);
    var t = svg("text", Object.assign({x: n.x, y: r1(n.y - (n.lineas.length - 1) * LINEA / 2 + 4), "text-anchor": "middle"}, LETRA_NODO), grupo);
    n.lineas.forEach(function (l, k) { svg("tspan", {x: n.x, dy: k ? LINEA : 0}, t, l); });
    R.consejo(grupo, n.texto);
  });
  if (g.grupos) R.leyenda(fig, Object.keys(g.grupos).map(function (k) { return {color: R.color(isNaN(k) ? k : +k, 0), texto: g.grupos[k]}; }));
  return {cabecera: [TX.desde, TX.hacia, TX.rotulo], filas: conexiones.map(function (c) { return [porId[c.de].texto, porId[c.a].texto, c.texto || "\u2014"]; })};
};
R.tipos.diagrama.fijo = true;  /* su tamano sale de su contenido: no se recalcula al cambiar el ancho */
})();
</script>
```


---

## Graficos avanzados (`dispersion`, `histograma`, `radar`, `embudo`, `treemap`, `pendiente`, `halteras`, `piramide`, `calendario`, `pictograma`)

Formas menos frecuentes que las del motor de la base. Un solo modulo para todas: se copia si el reporte usa cualquiera de ellas.

| Tipo | Pregunta que responde | Datos |
| :--- | :--- | :--- |
| `dispersion` | ¿Hay relacion entre dos magnitudes? Con `tamano`, una tercera (burbujas) | `puntos: [{rotulo, x, y, tamano}]`, `eje_x: {nombre, unidad}`, `eje_y: {nombre, unidad}`, `nombre_tamano`, `unidad_tamano` |
| `histograma` | ¿Como se reparten muchos valores sueltos? (dias de demora, cuantias) | `valores` en bruto, `tramos` (por defecto, regla de Sturges), `desde`, `hasta`, `unidad`, `nombre` |
| `radar` | ¿Que perfil tiene cada opcion en varios criterios? (de 3 a 8) | `ejes`, `series: [{nombre, valores}]`, `maximo` (por ejemplo 10 si se puntua de 0 a 10) |
| `embudo` | ¿Cuantos llegan a cada etapa y cuantos se pierden? | `etapas: [{rotulo, valor}]`; el modulo calcula el paso de cada etapa a la siguiente |
| `treemap` | ¿Que peso tiene cada partida cuando son muchas? | `elementos: [{rotulo, valor}]`, `unidad` |
| `pendiente` | ¿Como cambia cada partida entre dos momentos? | `etiquetas: ["antes", "despues"]`, `elementos: [{rotulo, antes, despues}]` |
| `halteras` | ¿Que distancia hay entre dos valores de cada partida? (pedido y concedido) | `nombres: {a, b}`, `elementos: [{rotulo, a, b}]` |
| `piramide` | ¿Como se comparan dos grupos por tramos? | `etiquetas`, `izquierda: {nombre, valores}`, `derecha: {nombre, valores}` |
| `calendario` | ¿Que dias concentran la actividad o los vencimientos? | `dias: {"AAAA-MM-DD": numero}`, `desde`, `hasta` |
| `pictograma` | Una proporcion contada en figuras («3 de cada 10») | `valor`, `total` (hasta 10 por fila), `rotulo` |

Reglas: los valores se dan en bruto y el modulo calcula escalas, tramos y porcentajes; el radar puntua todas las opciones con la misma escala y el mismo criterio, explicado en el texto; el histograma necesita al menos cinco valores; el pictograma no sirve para mas de unas decenas de figuras.

```js modulo=avanzados
<script>
/* Modulo de graficos avanzados para el motor de reportes. Se copia integro, despues
   del motor, solo en los reportes que usan alguno de estos tipos. */
(function(){
"use strict";
var R = Reportes, svg = R.svg, r1 = R.r1, fmt = R.fmt, color = R.color, consejo = R.consejo, T = R.T;
function num(v) { return typeof v === "number" && isFinite(v); }
function max(a) { return Math.max.apply(null, a.filter(num)); }
function min(a) { return Math.min.apply(null, a.filter(num)); }
function techo(v) {
  if (!(v > 0)) return 1;
  var m = Math.pow(10, Math.floor(Math.log10(v))), p = [1, 1.2, 1.6, 2, 2.4, 3, 4, 5, 6, 8, 10];
  for (var i = 0; i < p.length; i++) if (p[i] * m >= v * (1 - 1e-9)) return p[i] * m;
  return 10 * m;
}
function texto(s, at, contenido, clase) { return svg("text", Object.assign({"class": clase || "eje"}, at), s, contenido); }
/* Ancho del lienzo: el que pasa el motor (que ya tiene en cuenta impresion y escala) o el de la figura. */
function ancho(fig) { return Math.round(Math.min(700, Math.max(320, (fig.clientWidth || 700) / R.escala(fig)))); }

/* Dispersion y burbujas: relacion entre dos magnitudes; con "tamano", tercera magnitud. */
R.tipos.dispersion = function (fig, g, id, Wb) {
  var p = g.puntos || [], ex = g.eje_x || {}, ey = g.eje_y || {};
  if (p.length < 2) throw new Error("hacen falta al menos dos puntos");
  var W = Wb || ancho(fig), x0 = 64, x1 = W - 24, y0 = 24, y1 = 244;
  var tx = techo(max(p.map(function (d) { return d.x; }))), ty = techo(max(p.map(function (d) { return d.y; })));
  var tt = max(p.map(function (d) { return d.tamano || 0; })) || 1;
  var X = function (v) { return r1(x0 + v / tx * (x1 - x0)); }, Y = function (v) { return r1(y1 - v / ty * (y1 - y0)); };
  var s = R.lienzo(fig, W, 290, g.resumen || "");
  for (var k = 0; k <= 4; k++) {
    svg("line", {"class": "rejilla", x1: x0, y1: Y(ty * k / 4), x2: x1, y2: Y(ty * k / 4)}, s);
    texto(s, {x: x0 - 8, y: Y(ty * k / 4) + 4, "text-anchor": "end"}, k ? fmt(ty * k / 4, ey.unidad, true) : "0");
    texto(s, {x: X(tx * k / 4), y: y1 + 16, "text-anchor": "middle"}, k ? fmt(tx * k / 4, ex.unidad, true) : "0");
  }
  if (ex.nombre) texto(s, {x: x1, y: y1 + 34, "text-anchor": "end"}, ex.nombre);
  if (ey.nombre) texto(s, {x: x0, y: 14}, ey.nombre);
  p.forEach(function (d, i) {
    if (!num(d.x) || !num(d.y)) throw new Error("el punto " + (i + 1) + " necesita x e y numericos");
    var rad = d.tamano ? r1(5 + Math.sqrt(d.tamano / tt) * 20) : 5;
    consejo(svg("circle", {cx: X(d.x), cy: Y(d.y), r: rad, fill: color(d.color, 0), "fill-opacity": d.tamano ? ".45" : ".85", stroke: color(d.color, 0)}, s),
      (d.rotulo ? d.rotulo + ": " : "") + fmt(d.x, ex.unidad) + " · " + fmt(d.y, ey.unidad) + (d.tamano ? " · " + fmt(d.tamano, g.unidad_tamano) : ""));
    if (d.rotulo && (g.rotulos !== false)) texto(s, {x: X(d.x) + rad + 4, y: Y(d.y) + 4}, R.recortar(d.rotulo, 18), "eje");
  });
  return {cabecera: [T.concepto, ex.nombre || "x", ey.nombre || "y"].concat(p.some(function (d) { return d.tamano; }) ? [g.nombre_tamano || T.valor] : []),
    filas: p.map(function (d) { return [d.rotulo || "—", d.x, d.y].concat(d.tamano ? [d.tamano] : []); })};
};

/* Histograma: reparto de valores sueltos en tramos de igual anchura. */
R.tipos.histograma = function (fig, g, id, Wb) {
  var v = (g.valores || []).filter(num);
  if (v.length < 5) throw new Error("hacen falta al menos cinco valores");
  var lo = num(g.desde) ? g.desde : min(v), hi = num(g.hasta) ? g.hasta : max(v), n = g.tramos || Math.ceil(Math.log2(v.length) + 1);
  var paso = (hi - lo) / n || 1, cuenta = [];
  for (var i = 0; i < n; i++) cuenta.push(0);
  v.forEach(function (x) { cuenta[Math.min(n - 1, Math.max(0, Math.floor((x - lo) / paso)))]++; });
  var W = Wb || ancho(fig), x0 = 64, x1 = W - 24, tope = techo(max(cuenta)), banda = (x1 - x0) / n;
  var s = R.lienzo(fig, W, 280, g.resumen || "");
  for (var k = 0; k <= 4; k++) { var y = 244 - k * 50; svg("line", {"class": "rejilla", x1: x0, y1: y, x2: x1, y2: y}, s); texto(s, {x: x0 - 8, y: y + 4, "text-anchor": "end"}, k ? fmt(tope * k / 4, "entero", true) : "0"); }
  var etiquetas = cuenta.map(function (c, i) { return fmt(lo + i * paso, g.unidad, true) + "–" + fmt(lo + (i + 1) * paso, g.unidad, true); });
  cuenta.forEach(function (c, i) {
    var alto = c / tope * 200;
    consejo(svg("rect", {x: r1(x0 + i * banda + 1), y: r1(244 - alto), width: r1(banda - 2), height: r1(alto), fill: color(g.color, 0)}, s), etiquetas[i] + ": " + c);
  });
  [0, n].forEach(function (i) { texto(s, {x: r1(x0 + i * banda), y: 262, "text-anchor": i ? "end" : "start"}, fmt(lo + i * paso, g.unidad, true)); });
  if (g.nombre) texto(s, {x: x1, y: 278, "text-anchor": "end"}, g.nombre);
  return {cabecera: [T.concepto, T.valor], filas: etiquetas.map(function (e, i) { return [e, cuenta[i]]; }), unidad: "entero"};
};

/* Radar: perfil de varias opciones sobre los mismos criterios (de 3 a 8 ejes). */
R.tipos.radar = function (fig, g, id, Wb) {
  var ejes = g.ejes || [], series = g.series || [], n = ejes.length;
  if (n < 3 || n > 8) throw new Error("el radar necesita de tres a ocho ejes");
  var tope = g.maximo || techo(max([].concat.apply([], series.map(function (s) { return s.valores; })))), cx = 220, cy = 150, rad = 105;
  var s = R.lienzo(fig, 440, 300, g.resumen || ""); s.style.maxWidth = "440px";
  var punto = function (i, v) { var a = -Math.PI / 2 + i * 2 * Math.PI / n; return [r1(cx + Math.cos(a) * rad * v / tope), r1(cy + Math.sin(a) * rad * v / tope)]; };
  for (var k = 1; k <= 4; k++) svg("polygon", {points: ejes.map(function (_, i) { return punto(i, tope * k / 4).join(","); }).join(" "), fill: "none", stroke: "var(--linea-rejilla)"}, s);
  ejes.forEach(function (e, i) {
    var p = punto(i, tope), q = punto(i, tope * 1.18);
    svg("line", {x1: cx, y1: cy, x2: p[0], y2: p[1], stroke: "var(--linea-rejilla)"}, s);
    texto(s, {x: q[0], y: q[1] + 4, "text-anchor": Math.abs(q[0] - cx) < 8 ? "middle" : q[0] > cx ? "start" : "end"}, R.recortar(e, 16));
  });
  series.forEach(function (se, j) {
    var c = color(se.color, j);
    svg("polygon", {points: se.valores.map(function (v, i) { return punto(i, v || 0).join(","); }).join(" "), fill: c, "fill-opacity": ".16", stroke: c, "stroke-width": 2}, s);
    se.valores.forEach(function (v, i) { var p = punto(i, v || 0); consejo(svg("circle", {cx: p[0], cy: p[1], r: 3, fill: c}, s), se.nombre + " · " + ejes[i] + ": " + fmt(v, g.unidad)); });
  });
  R.leyenda(fig, series.map(function (se, j) { return {color: color(se.color, j), texto: se.nombre}; }));
  return {cabecera: [T.concepto].concat(series.map(function (se) { return se.nombre; })), unidad: g.unidad,
    filas: ejes.map(function (e, i) { return [e].concat(series.map(function (se) { return se.valores[i]; })); })};
};

/* Embudo: cuantos llegan a cada etapa y que proporcion pasa de una a la siguiente. */
R.tipos.embudo = function (fig, g, id, Wb) {
  var et = g.etapas || [];
  if (et.length < 2) throw new Error("hacen falta al menos dos etapas");
  var W = Wb || ancho(fig), tope = max(et.map(function (e) { return e.valor; })), fila = 44, centro = W / 2 + 40, util = W - 220;
  var s = R.lienzo(fig, W, et.length * fila + 8, g.resumen || "");
  et.forEach(function (e, i) {
    var w = Math.max(r1(e.valor / tope * util), 6), y = 4 + i * fila;
    texto(s, {x: 140, y: y + 23, "text-anchor": "end"}, R.recortar(e.rotulo, 20));
    consejo(svg("rect", {x: r1(centro - w / 2), y: y, width: w, height: 34, rx: 5, fill: color(e.color, 0), "fill-opacity": r1(1 - i * 0.12)}, s), e.rotulo + ": " + fmt(e.valor, g.unidad));
    texto(s, {x: centro, y: y + 22, "text-anchor": "middle", fill: "#fff", "font-weight": 650}, fmt(e.valor, g.unidad, true), "valor-punto dentro");
    if (i) texto(s, {x: W - 8, y: y + 22, "text-anchor": "end"}, fmt(e.valor / et[i - 1].valor * 100, "pct"));
  });
  return {cabecera: [T.concepto, T.valor, T.porcentaje], unidad: g.unidad,
    filas: et.map(function (e, i) { return [e.rotulo, e.valor, i ? fmt(e.valor / et[i - 1].valor * 100, "pct") : "—"]; })};
};

/* Treemap: peso de muchas partidas a la vez (disposicion cuadrada aproximada). */
R.tipos.treemap = function (fig, g, id, Wb) {
  var el = (g.elementos || []).filter(function (e) { return num(e.valor) && e.valor > 0; }).sort(function (a, b) { return b.valor - a.valor; });
  if (!el.length) throw new Error("faltan elementos con valor positivo");
  var W = Wb || ancho(fig), H = 300, total = el.reduce(function (s, e) { return s + e.valor; }, 0);
  var s = R.lienzo(fig, W, H, g.resumen || "");
  /* Particion por cortes alternos: cada partida ocupa su proporcion del rectangulo restante. */
  function partir(lista, x, y, w, h) {
    if (!lista.length) return;
    if (lista.length === 1) return pintar(lista[0], x, y, w, h);
    var suma = lista.reduce(function (s, e) { return s + e.valor; }, 0), acum = 0, corte = 0;
    while (corte < lista.length - 1 && (acum + lista[corte].valor) <= suma / 2) acum += lista[corte++].valor;
    if (!corte) { acum = lista[0].valor; corte = 1; }
    var f = acum / suma;
    if (w >= h) { partir(lista.slice(0, corte), x, y, w * f, h); partir(lista.slice(corte), x + w * f, y, w * (1 - f), h); }
    else { partir(lista.slice(0, corte), x, y, w, h * f); partir(lista.slice(corte), x, y + h * f, w, h * (1 - f)); }
  }
  function pintar(e, x, y, w, h) {
    var i = el.indexOf(e);
    consejo(svg("rect", {x: r1(x + 1), y: r1(y + 1), width: r1(Math.max(w - 2, 1)), height: r1(Math.max(h - 2, 1)), rx: 3, fill: color(e.color, i)}, s),
      e.rotulo + ": " + fmt(e.valor, g.unidad) + " (" + fmt(e.valor / total * 100, "pct") + ")");
    if (w > 70 && h > 34) {
      texto(s, {x: r1(x + 8), y: r1(y + 18), fill: "#fff", "font-weight": 650}, R.recortar(e.rotulo, Math.floor(w / 7)), "valor-punto dentro");
      texto(s, {x: r1(x + 8), y: r1(y + 33), fill: "#fff"}, fmt(e.valor / total * 100, "pct"), "valor-punto dentro");
    }
  }
  partir(el, 0, 0, W, H);
  return {cabecera: [T.concepto, T.valor, T.porcentaje], unidad: g.unidad, filas: el.map(function (e) { return [e.rotulo, e.valor, fmt(e.valor / total * 100, "pct")]; })};
};

/* Pendiente: como cambia cada partida entre dos momentos. */
R.tipos.pendiente = function (fig, g, id, Wb) {
  var el = g.elementos || [], et = g.etiquetas || ["", ""];
  if (!el.length) throw new Error("faltan elementos");
  var W = Wb || ancho(fig), xa = Math.round(W * 0.22), xb = Math.round(W * 0.58), tope = techo(max([].concat.apply([], el.map(function (e) { return [e.antes, e.despues]; }))));
  var Y = function (v) { return r1(260 - v / tope * 220); }, s = R.lienzo(fig, W, 290, g.resumen || "");
  texto(s, {x: xa, y: 20, "text-anchor": "middle", "font-weight": 650}, et[0]); texto(s, {x: xb, y: 20, "text-anchor": "middle", "font-weight": 650}, et[1]);
  [xa, xb].forEach(function (x) { svg("line", {"class": "rejilla", x1: x, y1: 36, x2: x, y2: 264}, s); });
  el.forEach(function (e, i) {
    var c = color(e.color, i);
    consejo(svg("line", {x1: xa, y1: Y(e.antes), x2: xb, y2: Y(e.despues), stroke: c, "stroke-width": 2.4}, s), e.rotulo + ": " + fmt(e.antes, g.unidad) + " → " + fmt(e.despues, g.unidad));
    svg("circle", {cx: xa, cy: Y(e.antes), r: 4, fill: c}, s); svg("circle", {cx: xb, cy: Y(e.despues), r: 4, fill: c}, s);
    /* A la izquierda solo la cifra; a la derecha, cifra y nombre, que tienen sitio. */
    texto(s, {x: xa - 10, y: Y(e.antes) + 4, "text-anchor": "end"}, fmt(e.antes, g.unidad, true));
    texto(s, {x: xb + 10, y: Y(e.despues) + 4}, fmt(e.despues, g.unidad, true) + " · " + R.recortar(e.rotulo, Math.max(8, Math.floor((W - xb - 70) / 6.5))));
  });
  return {cabecera: [T.concepto, et[0], et[1]], unidad: g.unidad, filas: el.map(function (e) { return [e.rotulo, e.antes, e.despues]; })};
};

/* Halteras: la distancia entre dos valores de cada partida (pedido y concedido, propuesta y definitiva). */
R.tipos.halteras = function (fig, g, id, Wb) {
  var el = g.elementos || [], nombres = g.nombres || {a: "A", b: "B"};
  if (!el.length) throw new Error("faltan elementos");
  var W = Wb || ancho(fig), x0 = W < 520 ? 112 : 150, x1 = W - 60, fila = 34, tope = techo(max([].concat.apply([], el.map(function (e) { return [e.a, e.b]; }))));
  var X = function (v) { return r1(x0 + v / tope * (x1 - x0)); }, s = R.lienzo(fig, W, el.length * fila + 30, g.resumen || "");
  el.forEach(function (e, i) {
    var y = 18 + i * fila;
    texto(s, {x: x0 - 10, y: y + 4, "text-anchor": "end"}, R.recortar(e.rotulo, W < 520 ? 16 : 26));
    svg("line", {x1: X(e.a), y1: y, x2: X(e.b), y2: y, stroke: "var(--borde)", "stroke-width": 4, "stroke-linecap": "round"}, s);
    consejo(svg("circle", {cx: X(e.a), cy: y, r: 6, fill: color(g.color_a || 6, 0)}, s), nombres.a + ": " + fmt(e.a, g.unidad));
    consejo(svg("circle", {cx: X(e.b), cy: y, r: 6, fill: color(g.color_b || 1, 0)}, s), nombres.b + ": " + fmt(e.b, g.unidad));
    texto(s, {x: Math.max(X(e.a), X(e.b)) + 10, y: y + 4}, fmt(e.b - e.a, g.unidad, true), "valor-punto");
  });
  [0, tope / 2, tope].forEach(function (v) { texto(s, {x: X(v), y: el.length * fila + 26, "text-anchor": "middle"}, v ? fmt(v, g.unidad, true) : "0"); });
  R.leyenda(fig, [{color: color(g.color_a || 6, 0), texto: nombres.a}, {color: color(g.color_b || 1, 0), texto: nombres.b}]);
  return {cabecera: [T.concepto, nombres.a, nombres.b, T.diferencia || "Diferencia"], unidad: g.unidad, filas: el.map(function (e) { return [e.rotulo, e.a, e.b, e.b - e.a]; })};
};

/* Piramide: dos grupos enfrentados por tramos (edad, antiguedad, cuantia). */
R.tipos.piramide = function (fig, g, id, Wb) {
  var et = g.etiquetas || [], iz = g.izquierda || {}, de = g.derecha || {};
  if (!et.length) throw new Error("faltan etiquetas");
  var W = Wb || ancho(fig), centro = W / 2, mitad = (W - 120) / 2, fila = 24, tope = techo(max((iz.valores || []).concat(de.valores || [])));
  var s = R.lienzo(fig, W, et.length * fila + 40, g.resumen || "");
  texto(s, {x: centro - 34, y: 14, "text-anchor": "end", "font-weight": 650}, iz.nombre || ""); texto(s, {x: centro + 34, y: 14, "font-weight": 650}, de.nombre || "");
  et.forEach(function (e, i) {
    var y = 22 + i * fila, a = (iz.valores || [])[i] || 0, b = (de.valores || [])[i] || 0, wa = a / tope * (mitad - 30), wb = b / tope * (mitad - 30);
    consejo(svg("rect", {x: r1(centro - 30 - wa), y: y, width: r1(wa), height: fila - 4, fill: color(iz.color, 0)}, s), (iz.nombre || "") + " · " + e + ": " + fmt(a, g.unidad));
    consejo(svg("rect", {x: centro + 30, y: y, width: r1(wb), height: fila - 4, fill: color(de.color, 1)}, s), (de.nombre || "") + " · " + e + ": " + fmt(b, g.unidad));
    texto(s, {x: centro, y: y + 14, "text-anchor": "middle"}, R.recortar(e, 9));
  });
  return {cabecera: [T.concepto, iz.nombre || "", de.nombre || ""], unidad: g.unidad, filas: et.map(function (e, i) { return [e, (iz.valores || [])[i], (de.valores || [])[i]]; })};
};

/* Calendario de calor: actividad o vencimientos por dia (semanas en columnas). */
R.tipos.calendario = function (fig, g, id, Wb) {
  var dias = g.dias || {}, claves = Object.keys(dias).sort();
  if (!claves.length) throw new Error("faltan dias");
  var f = function (t) { var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(t); if (!m) throw new Error("fecha no valida: " + t); return Date.UTC(+m[1], +m[2] - 1, +m[3]); };
  var D = 86400000, ini = f(g.desde || claves[0]), fin = f(g.hasta || claves[claves.length - 1]);
  ini -= ((new Date(ini).getUTCDay() + 6) % 7) * D;  /* la semana empieza en lunes */
  var semanas = Math.ceil((fin - ini + D) / (7 * D)), celda = 14, x0 = 34, y0 = 22, tope = max(claves.map(function (k) { return dias[k]; })) || 1;
  var s = R.lienzo(fig, x0 + semanas * (celda + 2) + 8, y0 + 7 * (celda + 2) + 8, g.resumen || "");
  s.setAttribute("width", x0 + semanas * (celda + 2) + 8);
  var mes = new Intl.DateTimeFormat(document.documentElement.lang || "es", {month: "short", timeZone: "UTC"}), largo = new Intl.DateTimeFormat(document.documentElement.lang || "es", {day: "numeric", month: "long", timeZone: "UTC"});
  ["L", "X", "V"].forEach(function (d, i) { texto(s, {x: x0 - 6, y: y0 + (i * 2) * (celda + 2) + 11, "text-anchor": "end"}, d); });
  var ultimoMes = -1;
  for (var t = ini; t <= fin; t += D) {
    var i = Math.floor((t - ini) / (7 * D)), d = (new Date(t).getUTCDay() + 6) % 7, k = new Date(t).toISOString().slice(0, 10), v = dias[k] || 0;
    if (new Date(t).getUTCMonth() !== ultimoMes && d === 0 && new Date(t).getUTCDate() <= 7) { ultimoMes = new Date(t).getUTCMonth(); texto(s, {x: x0 + i * (celda + 2), y: y0 - 8}, mes.format(t)); }
    consejo(svg("rect", {x: x0 + i * (celda + 2), y: y0 + d * (celda + 2), width: celda, height: celda, rx: 3,
      fill: v ? color(g.color || "acento", 0) : "var(--superficie-2)", "fill-opacity": v ? r1(0.2 + 0.8 * v / tope) : null, stroke: "var(--borde-suave)"}, s), largo.format(t) + ": " + v);
  }
  return {cabecera: [T.concepto, T.valor], filas: claves.map(function (k) { return [largo.format(f(k)), dias[k]]; })};
};

/* Pictograma: una proporcion contada en figuras («3 de cada 10»). */
R.tipos.pictograma = function (fig, g, id, Wb) {
  var total = g.total || 10, parte = g.valor;
  if (!num(parte) || parte < 0 || parte > total) throw new Error("valor debe estar entre 0 y total");
  var por = Math.min(total, 10), filas = Math.ceil(total / por), lado = 30;
  var s = R.lienzo(fig, por * lado + 8, filas * lado + 8, g.resumen || ""); s.setAttribute("width", por * lado + 8);
  for (var i = 0; i < total; i++) {
    var x = 4 + (i % por) * lado, y = 4 + Math.floor(i / por) * lado, lleno = i < Math.round(parte);
    var c = lleno ? color(g.color || 1, 0) : "var(--borde)";
    svg("circle", {cx: x + 15, cy: y + 9, r: 5.5, fill: c}, s);
    svg("path", {d: "M " + (x + 6) + " " + (y + 27) + " Q " + (x + 6) + " " + (y + 15) + " " + (x + 15) + " " + (y + 15) + " Q " + (x + 24) + " " + (y + 15) + " " + (x + 24) + " " + (y + 27) + " Z", fill: c}, s);
  }
  if (g.rotulo) R.html("p", "medidor-rotulo", fig, g.rotulo);
  return {cabecera: [T.valor, T.total], filas: [[parte, total]]};
};

["radar", "calendario", "pictograma"].forEach(function (t) { R.tipos[t].fijo = true; });
})();
</script>
```

---

## Iconos (`iconos`)

Un juego propio de iconos de trazo, sin recursos externos, para indicadores, avisos, listas y diapositivas. Se escriben en el HTML con `<span class="icono" data-icono="nombre"></span>` (o, en una diapositiva, dentro de cualquier texto como `{icono:nombre}`) y toman el tamano y el color del texto que los rodea.

Nombres: `plazo` (reloj), `calendario`, `juzgado`, `balanza`, `contrato`, `firma`, `euro`, `alerta`, `ok`, `persona`, `grupo`, `empresa`, `correo`, `telefono`, `ubicacion`, `candado`.

Uso con mesura: un icono acompana a un texto, nunca lo sustituye (el texto sigue diciendo lo que es), y no mas de un icono por indicador o por punto de una lista.

```js modulo=iconos
<script>
/* Iconos de trazo para los reportes. Se copia integro, despues del motor, solo si el
   reporte usa algun icono. */
(function(){
"use strict";
var NS = "http://www.w3.org/2000/svg";
var TRAZOS = {
  plazo: "M12 7v5l3 2M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0z",
  calendario: "M4 6h16v14H4zM4 10h16M8 3v4M16 3v4",
  juzgado: "M3 9l9-5 9 5M5 9v9M10 9v9M14 9v9M19 9v9M3 20h18",
  balanza: "M12 4v16M7 20h10M5 7h14M5 7l-3 7a3 3 0 0 0 6 0zM19 7l-3 7a3 3 0 0 0 6 0z",
  contrato: "M6 3h9l4 4v14H6zM14 3v5h5M9 12h7M9 16h5",
  firma: "M3 18c3 0 4-8 7-8s1 7 4 7 3-3 5-3M3 21h18",
  euro: "M18 6.5A7 7 0 1 0 18 17.5M4 10h10M4 14h10",
  alerta: "M12 3l10 18H2zM12 10v4M12 17.5v.5",
  ok: "M20 6L9 17l-5-5",
  persona: "M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM4 21c0-4 3.6-7 8-7s8 3 8 7",
  grupo: "M9 11a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zM2 20c0-3.5 3-6 7-6s7 2.5 7 6M16 4.5a3.5 3.5 0 0 1 0 6.5M18 14c2.5.8 4 3 4 6",
  empresa: "M4 21V5l8-2v18M12 9h8v12M4 21h18M7 8h2M7 12h2M7 16h2M15 13h2M15 17h2",
  correo: "M3 6h18v12H3zM3 7l9 6 9-6",
  telefono: "M5 3h4l2 5-3 2a12 12 0 0 0 6 6l2-3 5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z",
  ubicacion: "M12 21s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12zM12 11.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z",
  candado: "M6 11h12v10H6zM8 11V7a4 4 0 0 1 8 0v4"
};
function pintar(nodo) {
  var d = TRAZOS[nodo.getAttribute("data-icono")];
  if (!d) { console.error("Icono desconocido: " + nodo.getAttribute("data-icono")); return; }
  var s = document.createElementNS(NS, "svg"), p = document.createElementNS(NS, "path");
  s.setAttribute("viewBox", "0 0 24 24"); s.setAttribute("aria-hidden", "true");
  s.setAttribute("style", "width:1.1em;height:1.1em;vertical-align:-.18em;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;display:inline-block;margin-right:.3em");
  p.setAttribute("d", d); s.appendChild(p);
  nodo.textContent = ""; nodo.appendChild(s);
}
function todos() { document.querySelectorAll("[data-icono]").forEach(pintar); }
/* Tras la carga, para incluir los iconos de las diapositivas que monta su script. */
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", todos); else todos();
Reportes.iconos = TRAZOS;
})();
</script>
```


---

## Codigo QR (`qr`)

Un QR que lleva a la fuente, al expediente o a la version consolidada de una norma, para quien lee el documento en papel. Se genera dentro del documento, sin ningun servicio externo.

```json
{"tipo": "qr", "texto": "https://www.boe.es/buscar/act.php?id=BOE-A-2000-323", "rotulo": "Version consolidada de la norma citada", "tamano": 132}
```

- `texto`: la URL o el texto (hasta unos 210 caracteres). Solo URLs verificadas en la sesion o aportadas por el usuario.
- `tamano`: lado en pixeles en pantalla (por defecto 132; al imprimir, unos 3,5 cm).
- `rotulo`: lo que el lector encontrara al escanearlo. Un QR sin rotulo no dice a donde lleva.

```js modulo=qr
<script>
/* Codigo QR para los reportes (modo byte, correccion M, versiones 1 a 10: hasta unos 210
   caracteres). Se copia integro, despues del motor, solo si el reporte lleva un QR. */
(function(){
"use strict";
var R = Reportes;
var BLOQUES = [0, 1, 1, 1, 2, 2, 4, 4, 4, 5, 5], CORRECCION = [0, 10, 16, 26, 18, 24, 16, 18, 22, 22, 26];
function modulosDatos(v) {
  var n = (16 * v + 128) * v + 64;
  if (v >= 2) { var a = Math.floor(v / 7) + 2; n -= (25 * a - 10) * a - 55; if (v >= 7) n -= 36; }
  return n;
}
function mul(x, y) { var z = 0; for (var i = 7; i >= 0; i--) { z = (z << 1) ^ ((z >>> 7) * 0x11D); z ^= ((y >>> i) & 1) * x; } return z; }
function divisor(g) {
  var r = []; for (var i = 0; i < g - 1; i++) r.push(0); r.push(1);
  for (var k = 0, raiz = 1; k < g; k++) { for (var j = 0; j < r.length; j++) { r[j] = mul(r[j], raiz); if (j + 1 < r.length) r[j] ^= r[j + 1]; } raiz = mul(raiz, 2); }
  return r;
}
function resto(datos, div) {
  var r = div.map(function () { return 0; });
  datos.forEach(function (b) { var f = b ^ r.shift(); r.push(0); div.forEach(function (c, i) { r[i] ^= mul(c, f); }); });
  return r;
}
function codificar(texto) {
  var bytes = Array.from(new TextEncoder().encode(texto)), v, cap;
  for (v = 1; v <= 10; v++) { cap = Math.floor(modulosDatos(v) / 8) - CORRECCION[v] * BLOQUES[v]; if (4 + (v < 10 ? 8 : 16) + bytes.length * 8 <= cap * 8) break; }
  if (v > 10) throw new Error("el texto del QR es demasiado largo (maximo unos 210 caracteres)");
  var bits = [], pon = function (val, n) { for (var i = n - 1; i >= 0; i--) bits.push((val >>> i) & 1); };
  pon(4, 4); pon(bytes.length, v < 10 ? 8 : 16); bytes.forEach(function (b) { pon(b, 8); });
  pon(0, Math.min(4, cap * 8 - bits.length)); pon(0, (8 - bits.length % 8) % 8);
  for (var relleno = 0xEC; bits.length < cap * 8; relleno ^= 0xEC ^ 0x11) pon(relleno, 8);
  var datos = []; for (var i = 0; i < bits.length; i += 8) { var b = 0; for (var j = 0; j < 8; j++) b = b << 1 | bits[i + j]; datos.push(b); }
  /* Bloques con su correccion y entrelazado. */
  var nb = BLOQUES[v], ec = CORRECCION[v], total = Math.floor(modulosDatos(v) / 8), cortos = nb - total % nb, largoCorto = Math.floor(total / nb);
  var div = divisor(ec), bloques = [], k = 0;
  for (i = 0; i < nb; i++) {
    var d = datos.slice(k, k + largoCorto - ec + (i < cortos ? 0 : 1)); k += d.length;
    var e = resto(d, div); if (i < cortos) d.push(0); bloques.push(d.concat(e));
  }
  var cw = [];
  for (i = 0; i < bloques[0].length; i++) bloques.forEach(function (bl, j) { if (i !== largoCorto - ec || j >= cortos) cw.push(bl[i]); });
  return {v: v, cw: cw};
}
function matriz(v, cw) {
  var n = v * 4 + 17, m = [], f = [], x, y, i;
  for (y = 0; y < n; y++) { m.push([]); f.push([]); for (x = 0; x < n; x++) { m[y].push(false); f[y].push(false); } }
  var pon = function (x, y, o) { m[y][x] = o; f[y][x] = true; };
  for (i = 0; i < n; i++) { pon(6, i, i % 2 === 0); pon(i, 6, i % 2 === 0); }
  [[3, 3], [n - 4, 3], [3, n - 4]].forEach(function (c) {
    for (var dy = -4; dy <= 4; dy++) for (var dx = -4; dx <= 4; dx++) {
      var d = Math.max(Math.abs(dx), Math.abs(dy)), xx = c[0] + dx, yy = c[1] + dy;
      if (xx >= 0 && xx < n && yy >= 0 && yy < n) pon(xx, yy, d !== 2 && d !== 4);
    }
  });
  if (v > 1) {
    var na = Math.floor(v / 7) + 2, paso = Math.ceil((v * 4 + 4) / (na * 2 - 2)) * 2, pos = [6];
    for (i = 0, x = n - 7; i < na - 1; i++, x -= paso) pos.splice(1, 0, x);
    pos.forEach(function (ay, a) { pos.forEach(function (ax, b) {
      if ((a === 0 && b === 0) || (a === 0 && b === na - 1) || (a === na - 1 && b === 0)) return;
      for (var dy = -2; dy <= 2; dy++) for (var dx = -2; dx <= 2; dx++) pon(ax + dx, ay + dy, Math.max(Math.abs(dx), Math.abs(dy)) !== 1);
    }); });
  }
  var formato = function (mascara) {
    var d = mascara, r = d; /* correccion M = 00 */
    for (var j = 0; j < 10; j++) r = (r << 1) ^ ((r >>> 9) * 0x537);
    var b = ((d << 10) | r) ^ 0x5412, bit = function (i) { return ((b >>> i) & 1) !== 0; };
    for (j = 0; j <= 5; j++) pon(8, j, bit(j));
    pon(8, 7, bit(6)); pon(8, 8, bit(7)); pon(7, 8, bit(8));
    for (j = 9; j < 15; j++) pon(14 - j, 8, bit(j));
    for (j = 0; j < 8; j++) pon(n - 1 - j, 8, bit(j));
    for (j = 8; j < 15; j++) pon(8, n - 15 + j, bit(j));
    pon(8, n - 8, true);
  };
  formato(0);
  if (v >= 7) {
    var r = v; for (i = 0; i < 12; i++) r = (r << 1) ^ ((r >>> 11) * 0x1F25);
    var bv = v << 12 | r;
    for (i = 0; i < 18; i++) { var o = ((bv >>> i) & 1) !== 0, a = n - 11 + i % 3, c = Math.floor(i / 3); pon(a, c, o); pon(c, a, o); }
  }
  for (var der = n - 1, idx = 0; der >= 1; der -= 2) {
    if (der === 6) der = 5;
    for (var vert = 0; vert < n; vert++) for (var j = 0; j < 2; j++) {
      x = der - j; y = ((der + 1) & 2) === 0 ? n - 1 - vert : vert;
      if (!f[y][x] && idx < cw.length * 8) { m[y][x] = ((cw[idx >>> 3] >>> (7 - (idx & 7))) & 1) !== 0; idx++; }
    }
  }
  /* Mascara con menos penalizacion (rachas, bloques 2x2 y equilibrio de oscuros). */
  var mascaras = [
    function (x, y) { return (x + y) % 2 === 0; }, function (x, y) { return y % 2 === 0; }, function (x) { return x % 3 === 0; },
    function (x, y) { return (x + y) % 3 === 0; }, function (x, y) { return (Math.floor(x / 3) + Math.floor(y / 2)) % 2 === 0; },
    function (x, y) { return x * y % 2 + x * y % 3 === 0; }, function (x, y) { return (x * y % 2 + x * y % 3) % 2 === 0; },
    function (x, y) { return ((x + y) % 2 + x * y % 3) % 2 === 0; }];
  var aplicar = function (k) { for (y = 0; y < n; y++) for (x = 0; x < n; x++) if (!f[y][x] && mascaras[k](x, y)) m[y][x] = !m[y][x]; };
  var penalizacion = function () {
    var p = 0, oscuros = 0;
    for (var a = 0; a < n; a++) for (var dir = 0; dir < 2; dir++) {
      var racha = 1;
      for (var b = 1; b < n; b++) {
        var actual = dir ? m[b][a] : m[a][b], previo = dir ? m[b - 1][a] : m[a][b - 1];
        if (actual === previo) { racha++; if (racha === 5) p += 3; else if (racha > 5) p++; } else racha = 1;
      }
    }
    for (y = 0; y < n - 1; y++) for (x = 0; x < n - 1; x++) if (m[y][x] === m[y][x + 1] && m[y][x] === m[y + 1][x] && m[y][x] === m[y + 1][x + 1]) p += 3;
    for (y = 0; y < n; y++) for (x = 0; x < n; x++) if (m[y][x]) oscuros++;
    return p + Math.floor(Math.abs(oscuros * 20 - n * n * 10) / (n * n)) * 10;
  };
  var mejor = 0, menor = Infinity;
  for (var k = 0; k < 8; k++) { aplicar(k); formato(k); var pn = penalizacion(); if (pn < menor) { menor = pn; mejor = k; } aplicar(k); }
  aplicar(mejor); formato(mejor);
  return m;
}
R.tipos.qr = function (fig, g) {
  if (!g.texto) throw new Error("falta el texto o la URL del QR");
  var c = codificar(String(g.texto)), m = matriz(c.v, c.cw), n = m.length, borde = 4, lado = n + borde * 2, d = "";
  for (var y = 0; y < n; y++) for (var x = 0; x < n; x++) if (m[y][x]) d += "M" + (x + borde) + "," + (y + borde) + "h1v1h-1z";
  var s = R.lienzo(fig, lado, lado, g.resumen || ("QR: " + g.texto));
  s.setAttribute("width", g.tamano || 132); s.setAttribute("shape-rendering", "crispEdges"); s.style.margin = "0";
  R.svg("rect", {width: lado, height: lado, fill: "#fff"}, s);
  R.svg("path", {d: d, fill: "#000"}, s);
  if (g.rotulo) R.html("p", "fuente-grafico", fig, g.rotulo);
  return null;
};
R.tipos.qr.fijo = true;
})();
</script>
```
