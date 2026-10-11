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
var R = Reportes, svg = R.svg, r1 = R.r1, fmt = R.fmt, color = R.color, consejo = R.consejo, num = R.num, max = R.maximo, min = R.minimo, techo = R.techo;
var TX = Object.assign(/^en/.test(R.IDIOMA) ? {diferencia: "Difference"} : {diferencia: "Diferencia"}, R.T);
function texto(s, at, contenido, clase) { return svg("text", Object.assign({"class": clase || "eje"}, at), s, contenido); }
function topeDe(listas) { return techo(max([].concat.apply([], listas))); }
function sinNegativos(valores, tipo) { if (min(valores) < 0) throw new Error("el grafico " + tipo + " no admite valores negativos"); }
function pct(v, total) { return fmt(v / total * 100, "pct"); }

/* Dispersion y burbujas: relacion entre dos magnitudes; con "tamano", tercera magnitud. */
R.tipos.dispersion = function (fig, g, id, W) {
  var p = g.puntos || [], ex = g.eje_x || {}, ey = g.eje_y || {};
  if (p.length < 2) throw new Error("hacen falta al menos dos puntos");
  p.forEach(function (d, i) { if (!num(d.x) || !num(d.y)) throw new Error("el punto " + (i + 1) + " necesita x e y numericos"); });
  /* Ejes desde cero o desde el minimo negativo, con sitio a la derecha para los rotulos. */
  var xs = p.map(function (d) { return d.x; }), ys = p.map(function (d) { return d.y; });
  var x0 = 64, x1 = W - (g.rotulos === false ? 24 : 96), y0 = 44, y1 = 244;
  var tx = techo(max(xs)), ty = techo(max(ys)), bx = min(xs) < 0 ? -techo(-min(xs)) : 0, by = min(ys) < 0 ? -techo(-min(ys)) : 0;
  var tt = max(p.map(function (d) { return d.tamano || 0; })) || 1;
  var X = function (v) { return r1(x0 + (v - bx) / (tx - bx) * (x1 - x0)); }, Y = function (v) { return r1(y1 - (v - by) / (ty - by) * (y1 - y0)); };
  var s = R.lienzo(fig, W, 290, g.resumen);
  for (var k = 0; k <= 4; k++) {
    var vy = by + (ty - by) * k / 4, vx = bx + (tx - bx) * k / 4;
    svg("line", {"class": "rejilla", x1: x0, y1: Y(vy), x2: x1, y2: Y(vy)}, s);
    texto(s, {x: x0 - 8, y: Y(vy) + 4, "text-anchor": "end"}, vy ? fmt(vy, ey.unidad, true) : "0");
    texto(s, {x: X(vx), y: y1 + 16, "text-anchor": "middle"}, vx ? fmt(vx, ex.unidad, true) : "0");
  }
  if (bx < 0) svg("line", {"class": "cero", x1: X(0), y1: y0, x2: X(0), y2: y1}, s);
  if (by < 0) svg("line", {"class": "cero", x1: x0, y1: Y(0), x2: x1, y2: Y(0)}, s);
  if (ex.nombre) texto(s, {x: x1, y: y1 + 34, "text-anchor": "end"}, ex.nombre);
  if (ey.nombre) texto(s, {x: x0, y: y0 - 14}, ey.nombre);
  p.forEach(function (d) {
    var rad = d.tamano ? r1(5 + Math.sqrt(d.tamano / tt) * 20) : 5;
    consejo(svg("circle", {cx: X(d.x), cy: Y(d.y), r: rad, fill: color(d.color, 0), "fill-opacity": d.tamano ? ".45" : ".85", stroke: color(d.color, 0)}, s),
      (d.rotulo ? d.rotulo + ": " : "") + fmt(d.x, ex.unidad) + " · " + fmt(d.y, ey.unidad) + (d.tamano ? " · " + fmt(d.tamano, g.unidad_tamano) : ""));
    if (d.rotulo && g.rotulos !== false) texto(s, {x: X(d.x) + rad + 4, y: Y(d.y) + 4}, R.recortar(d.rotulo, 14));
  });
  return {cabecera: [R.T.concepto, ex.nombre || "x", ey.nombre || "y"].concat(p.some(function (d) { return d.tamano; }) ? [g.nombre_tamano || R.T.valor] : []),
    filas: p.map(function (d) { return [d.rotulo || "—", d.x, d.y].concat(d.tamano ? [d.tamano] : []); })};
};

/* Histograma: reparto de valores sueltos en tramos de igual anchura. */
R.tipos.histograma = function (fig, g, id, W) {
  var lo = num(g.desde) ? g.desde : min(g.valores || []), hi = num(g.hasta) ? g.hasta : max(g.valores || []);
  var v = (g.valores || []).filter(function (x) { return num(x) && x >= lo && x <= hi; });  /* fuera del rango indicado no cuentan */
  if (v.length < 5) throw new Error("hacen falta al menos cinco valores dentro del rango");
  var n = g.tramos || Math.ceil(Math.log2(v.length) + 1), paso = (hi - lo) / n || 1, cuenta = [];
  for (var i = 0; i < n; i++) cuenta.push(0);
  v.forEach(function (x) { cuenta[Math.min(n - 1, Math.floor((x - lo) / paso))]++; });
  /* Recuentos: el tope es multiplo de 4 para que la rejilla marque numeros enteros. */
  var tope = Math.max(4, Math.ceil(max(cuenta) / 4) * 4), banda = (W - 24 - 64) / n, s = R.lienzo(fig, W, 280, g.resumen);
  R.rejilla(s, tope, "entero");
  var etiquetas = cuenta.map(function (c, i) { return fmt(lo + i * paso, g.unidad, true) + "–" + fmt(lo + (i + 1) * paso, g.unidad, true); });
  cuenta.forEach(function (c, i) {
    consejo(svg("rect", {x: r1(64 + i * banda + 1), y: R.yDe(c, tope), width: r1(banda - 2), height: r1(c / tope * 200), fill: color(g.color, 0)}, s), etiquetas[i] + ": " + c);
  });
  [0, n].forEach(function (i) { texto(s, {x: r1(64 + i * banda), y: 262, "text-anchor": i ? "end" : "start"}, fmt(lo + i * paso, g.unidad, true)); });
  if (g.nombre) texto(s, {x: W - 24, y: 278, "text-anchor": "end"}, g.nombre);
  return {cabecera: [R.T.concepto, R.T.valor], filas: etiquetas.map(function (e, i) { return [e, cuenta[i]]; }), unidad: "entero"};
};

/* Radar: perfil de varias opciones sobre los mismos criterios (de 3 a 8 ejes). */
R.tipos.radar = function (fig, g) {
  var ejes = g.ejes || [], series = g.series || [], n = ejes.length;
  if (n < 3 || n > 8) throw new Error("el radar necesita de tres a ocho ejes");
  sinNegativos([].concat.apply([], series.map(function (s) { return s.valores; })), "radar");
  var tope = g.maximo || topeDe(series.map(function (s) { return s.valores; })), cx = 220, cy = 150, rad = 105;
  var s = R.lienzo(fig, 440, 300, g.resumen); s.style.maxWidth = "440px";
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
  return {cabecera: [R.T.concepto].concat(series.map(function (se) { return se.nombre; })), unidad: g.unidad,
    filas: ejes.map(function (e, i) { return [e].concat(series.map(function (se) { return se.valores[i]; })); })};
};

/* Embudo: cuantos llegan a cada etapa y que proporcion pasa de una a la siguiente. */
R.tipos.embudo = function (fig, g, id, W) {
  var et = g.etapas || [], tope = max(et.map(function (e) { return e.valor; }));
  if (et.length < 2) throw new Error("hacen falta al menos dos etapas");
  if (!(tope > 0)) throw new Error("las etapas necesitan valores positivos");
  var fila = 44, centro = W / 2 + 40, util = W - 220, s = R.lienzo(fig, W, et.length * fila + 8, g.resumen);
  et.forEach(function (e, i) {
    var w = Math.max(r1(e.valor / tope * util), 6), y = 4 + i * fila, paso = i ? pct(e.valor, et[i - 1].valor) : null;
    texto(s, {x: 140, y: y + 23, "text-anchor": "end"}, R.recortar(e.rotulo, 20));
    consejo(svg("rect", {x: r1(centro - w / 2), y: y, width: w, height: 34, rx: 5, fill: color(e.color, 0), "fill-opacity": r1(Math.max(0.5, 1 - i * 0.1))}, s), e.rotulo + ": " + fmt(e.valor, g.unidad));
    /* La cifra va dentro si cabe; si la barra es estrecha, al lado y en color de texto. */
    var dentro = w > 64;
    texto(s, {x: dentro ? centro : r1(centro + w / 2 + 6), y: y + 22, "text-anchor": dentro ? "middle" : "start"}, fmt(e.valor, g.unidad, true), dentro ? "valor-punto dentro" : "valor-punto");
    if (paso) texto(s, {x: W - 8, y: y + 22, "text-anchor": "end"}, paso);
    e.paso = paso;
  });
  return {cabecera: [R.T.concepto, R.T.valor, R.T.porcentaje], unidad: g.unidad, filas: et.map(function (e) { return [e.rotulo, e.valor, e.paso || "—"]; })};
};

/* Treemap: peso de muchas partidas a la vez (particion por cortes alternos). */
R.tipos.treemap = function (fig, g, id, W) {
  var el = (g.elementos || []).filter(function (e) { return num(e.valor) && e.valor > 0; }).sort(function (a, b) { return b.valor - a.valor; });
  if (!el.length) throw new Error("faltan elementos con valor positivo");
  var H = 300, total = el.reduce(function (s, e) { return s + e.valor; }, 0), s = R.lienzo(fig, W, H, g.resumen);
  el.forEach(function (e) { e.pct = pct(e.valor, total); });
  function partir(lista, x, y, w, h) {
    if (!lista.length) return;
    if (lista.length === 1) return pintar(lista[0], x, y, w, h);
    var suma = lista.reduce(function (s, e) { return s + e.valor; }, 0), acum = 0, corte = 0;
    while (corte < lista.length - 1 && acum + lista[corte].valor <= suma / 2) acum += lista[corte++].valor;
    if (!corte) { acum = lista[0].valor; corte = 1; }
    var f = acum / suma;
    if (w >= h) { partir(lista.slice(0, corte), x, y, w * f, h); partir(lista.slice(corte), x + w * f, y, w * (1 - f), h); }
    else { partir(lista.slice(0, corte), x, y, w, h * f); partir(lista.slice(corte), x, y + h * f, w, h * (1 - f)); }
  }
  function pintar(e, x, y, w, h) {
    consejo(svg("rect", {x: r1(x + 1), y: r1(y + 1), width: r1(Math.max(w - 2, 1)), height: r1(Math.max(h - 2, 1)), rx: 3, fill: color(e.color, el.indexOf(e))}, s),
      e.rotulo + ": " + fmt(e.valor, g.unidad) + " (" + e.pct + ")");
    if (w > 70 && h > 34) {
      texto(s, {x: r1(x + 8), y: r1(y + 18), "font-weight": 650}, R.recortar(e.rotulo, Math.floor(w / 7)), "valor-punto dentro");
      texto(s, {x: r1(x + 8), y: r1(y + 33)}, e.pct, "valor-punto dentro");
    }
  }
  partir(el, 0, 0, W, H);
  return {cabecera: [R.T.concepto, R.T.valor, R.T.porcentaje], unidad: g.unidad, filas: el.map(function (e) { return [e.rotulo, e.valor, e.pct]; })};
};

/* Separa en vertical rotulos que caerian encima unos de otros (minimo "hueco" px). */
function separar(ys, hueco) {
  var orden = ys.map(function (y, i) { return [y, i]; }).sort(function (a, b) { return a[0] - b[0]; }), salida = ys.slice();
  for (var k = 1; k < orden.length; k++) { var prev = salida[orden[k - 1][1]]; if (salida[orden[k][1]] - prev < hueco) salida[orden[k][1]] = prev + hueco; }
  return salida;
}

/* Pendiente: como cambia cada partida entre dos momentos. */
R.tipos.pendiente = function (fig, g, id, W) {
  var el = g.elementos || [], et = g.etiquetas || ["", ""];
  if (!el.length) throw new Error("faltan elementos");
  sinNegativos([].concat.apply([], el.map(function (e) { return [e.antes, e.despues]; })), "pendiente");
  var xa = Math.round(W * 0.22), xb = Math.round(W * 0.58), tope = topeDe(el.map(function (e) { return [e.antes, e.despues]; }));
  var Y = function (v) { return r1(260 - v / tope * 220); }, s = R.lienzo(fig, W, 290, g.resumen);
  texto(s, {x: xa, y: 20, "text-anchor": "middle", "font-weight": 650}, et[0]); texto(s, {x: xb, y: 20, "text-anchor": "middle", "font-weight": 650}, et[1]);
  [xa, xb].forEach(function (x) { svg("line", {"class": "rejilla", x1: x, y1: 36, x2: x, y2: 264}, s); });
  var ia = separar(el.map(function (e) { return Y(e.antes); }), 13), ib = separar(el.map(function (e) { return Y(e.despues); }), 13);
  el.forEach(function (e, i) {
    var c = color(e.color, i);
    consejo(svg("line", {x1: xa, y1: Y(e.antes), x2: xb, y2: Y(e.despues), stroke: c, "stroke-width": 2.4}, s), e.rotulo + ": " + fmt(e.antes, g.unidad) + " → " + fmt(e.despues, g.unidad));
    svg("circle", {cx: xa, cy: Y(e.antes), r: 4, fill: c}, s); svg("circle", {cx: xb, cy: Y(e.despues), r: 4, fill: c}, s);
    texto(s, {x: xa - 10, y: ia[i] + 4, "text-anchor": "end"}, fmt(e.antes, g.unidad, true));
    texto(s, {x: xb + 10, y: ib[i] + 4}, fmt(e.despues, g.unidad, true) + " · " + R.recortar(e.rotulo, Math.max(8, Math.floor((W - xb - 70) / 6.5))));
  });
  return {cabecera: [R.T.concepto, et[0], et[1]], unidad: g.unidad, filas: el.map(function (e) { return [e.rotulo, e.antes, e.despues]; })};
};

/* Halteras: la distancia entre dos valores de cada partida (pedido y concedido, propuesta y definitiva). */
R.tipos.halteras = function (fig, g, id, W) {
  var el = g.elementos || [], nombres = g.nombres || {a: "A", b: "B"};
  if (!el.length) throw new Error("faltan elementos");
  sinNegativos([].concat.apply([], el.map(function (e) { return [e.a, e.b]; })), "halteras");
  var x0 = R.columnaRotulos(), x1 = W - 60, fila = 34, tope = topeDe(el.map(function (e) { return [e.a, e.b]; }));
  var X = function (v) { return r1(x0 + v / tope * (x1 - x0)); }, s = R.lienzo(fig, W, el.length * fila + 30, g.resumen), ca = color(g.color_a || 6, 0), cb = color(g.color_b || 1, 0);
  el.forEach(function (e, i) {
    var y = 18 + i * fila;
    R.rotuloFila(s, y + 4, e.rotulo);
    svg("line", {x1: X(e.a), y1: y, x2: X(e.b), y2: y, stroke: "var(--borde)", "stroke-width": 4, "stroke-linecap": "round"}, s);
    consejo(svg("circle", {cx: X(e.a), cy: y, r: 6, fill: ca}, s), nombres.a + ": " + fmt(e.a, g.unidad));
    consejo(svg("circle", {cx: X(e.b), cy: y, r: 6, fill: cb}, s), nombres.b + ": " + fmt(e.b, g.unidad));
    texto(s, {x: Math.max(X(e.a), X(e.b)) + 10, y: y + 4}, fmt(e.b - e.a, g.unidad, true), "valor-punto");
  });
  [0, tope / 2, tope].forEach(function (v) { texto(s, {x: X(v), y: el.length * fila + 26, "text-anchor": "middle"}, v ? fmt(v, g.unidad, true) : "0"); });
  R.leyenda(fig, [{color: ca, texto: nombres.a}, {color: cb, texto: nombres.b}]);
  return {cabecera: [R.T.concepto, nombres.a, nombres.b, TX.diferencia], unidad: g.unidad, filas: el.map(function (e) { return [e.rotulo, e.a, e.b, e.b - e.a]; })};
};

/* Piramide: dos grupos enfrentados por tramos (edad, antiguedad, cuantia). */
R.tipos.piramide = function (fig, g, id, W) {
  var et = g.etiquetas || [], iz = g.izquierda || {}, de = g.derecha || {}, va = iz.valores || [], vb = de.valores || [];
  if (!et.length) throw new Error("faltan etiquetas");
  sinNegativos(va.concat(vb), "piramide");
  var centro = W / 2, mitad = (W - 120) / 2, fila = 24, tope = topeDe([va, vb]), s = R.lienzo(fig, W, et.length * fila + 40, g.resumen);
  texto(s, {x: centro - 34, y: 14, "text-anchor": "end", "font-weight": 650}, iz.nombre || ""); texto(s, {x: centro + 34, y: 14, "font-weight": 650}, de.nombre || "");
  et.forEach(function (e, i) {
    var y = 22 + i * fila, a = va[i] || 0, b = vb[i] || 0, wa = a / tope * (mitad - 30), wb = b / tope * (mitad - 30);
    consejo(svg("rect", {x: r1(centro - 30 - wa), y: y, width: r1(wa), height: fila - 4, fill: color(iz.color, 0)}, s), (iz.nombre || "") + " · " + e + ": " + fmt(a, g.unidad));
    consejo(svg("rect", {x: centro + 30, y: y, width: r1(wb), height: fila - 4, fill: color(de.color, 1)}, s), (de.nombre || "") + " · " + e + ": " + fmt(b, g.unidad));
    texto(s, {x: centro, y: y + 14, "text-anchor": "middle"}, R.recortar(e, 9));
  });
  return {cabecera: [R.T.concepto, iz.nombre || "", de.nombre || ""], unidad: g.unidad, filas: et.map(function (e, i) { return [e, va[i], vb[i]]; })};
};

/* Calendario de calor: actividad o vencimientos por dia (semanas en columnas, de lunes a domingo). */
R.tipos.calendario = function (fig, g) {
  var dias = g.dias || {}, claves = Object.keys(dias).sort(), DIA = R.DIA;
  if (!claves.length) throw new Error("faltan dias");
  var ini = R.fecha(g.desde || claves[0]), fin = R.fecha(g.hasta || claves[claves.length - 1]);
  ini -= ((new Date(ini).getUTCDay() + 6) % 7) * DIA;
  var semanas = Math.ceil((fin - ini + DIA) / (7 * DIA)), celda = 14, x0 = 34, y0 = 22, tope = max(claves.map(function (k) { return dias[k]; })) || 1;
  var ancho = x0 + semanas * (celda + 2) + 8, s = R.lienzo(fig, ancho, y0 + 7 * (celda + 2) + 8, g.resumen);
  s.setAttribute("width", ancho);
  var mes = new Intl.DateTimeFormat(R.IDIOMA, {month: "short", timeZone: "UTC"}), largo = new Intl.DateTimeFormat(R.IDIOMA, {day: "numeric", month: "long", timeZone: "UTC"});
  var inicial = new Intl.DateTimeFormat(R.IDIOMA, {weekday: "narrow", timeZone: "UTC"});
  [0, 2, 4].forEach(function (d) { texto(s, {x: x0 - 6, y: y0 + d * (celda + 2) + 11, "text-anchor": "end"}, inicial.format(Date.UTC(2026, 0, 5 + d))); });
  var ultimoMes = -1;
  for (var t = ini; t <= fin; t += DIA) {
    var f = new Date(t), i = Math.floor((t - ini) / (7 * DIA)), d = (f.getUTCDay() + 6) % 7, v = dias[f.toISOString().slice(0, 10)] || 0;
    /* El mes se rotula en su primera semana (y siempre en la primera columna). */
    if (d === 0 && f.getUTCMonth() !== ultimoMes && (i === 0 || f.getUTCDate() <= 7)) { ultimoMes = f.getUTCMonth(); texto(s, {x: x0 + i * (celda + 2), y: y0 - 8}, mes.format(t)); }
    consejo(svg("rect", {x: x0 + i * (celda + 2), y: y0 + d * (celda + 2), width: celda, height: celda, rx: 3,
      fill: v ? color(g.color || "acento", 0) : "var(--superficie-2)", "fill-opacity": v ? r1(0.2 + 0.8 * v / tope) : null, stroke: "var(--borde-suave)"}, s), largo.format(t) + ": " + v);
  }
  return {cabecera: [R.T.concepto, R.T.valor], filas: claves.map(function (k) { return [largo.format(R.fecha(k)), dias[k]]; })};
};

/* Pictograma: una proporcion contada en figuras («3 de cada 10»). */
R.tipos.pictograma = function (fig, g) {
  var total = g.total || 10, parte = g.valor;
  if (!num(parte) || parte < 0 || parte > total) throw new Error("valor debe estar entre 0 y total");
  var por = Math.min(total, 10), lado = 30, s = R.lienzo(fig, por * lado + 8, Math.ceil(total / por) * lado + 8, g.resumen);
  s.setAttribute("width", por * lado + 8);
  for (var i = 0; i < total; i++) {
    var x = 4 + (i % por) * lado, y = 4 + Math.floor(i / por) * lado, c = i < Math.round(parte) ? color(g.color || 1, 0) : "var(--borde)";
    svg("circle", {cx: x + 15, cy: y + 9, r: 5.5, fill: c}, s);
    svg("path", {d: "M " + (x + 6) + " " + (y + 27) + " Q " + (x + 6) + " " + (y + 15) + " " + (x + 15) + " " + (y + 15) + " Q " + (x + 24) + " " + (y + 15) + " " + (x + 24) + " " + (y + 27) + " Z", fill: c}, s);
  }
  if (g.rotulo) R.html("p", "medidor-rotulo", fig, g.rotulo);
  return {cabecera: [R.T.valor, R.T.total], filas: [[parte, total]]};
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
  nodo.textContent = "";
  Reportes.svg("path", {d: d}, Reportes.svg("svg", {viewBox: "0 0 24 24", "aria-hidden": "true",
    style: "width:1.1em;height:1.1em;vertical-align:-.18em;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;display:inline-block;margin-right:.3em"}, nodo));
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


---

## Identidad del despacho (`marca`)

Aplica los colores, el logo y el pie del despacho a partir del bloque `marca` de los datos, sin tocar el CSS. Es la forma de resolver `tema_personalizado`.

```json
"marca": {"nombre": "Lasheras & Gil Abogados", "acento": "#7a1f3d", "acento_fuerte": "#5c1730",
          "serie": ["#7a1f3d", "#b8893b", "#3f6b5a", "#4b5d86", "#9a5a7c", "#6b7280"],
          "oscuro": {"acento": "#e48aa6", "serie": ["#e48aa6", "#e0b36a", "#8fc2a8", "#9fb2e0", "#d49ab8", "#a0a7ad"]},
          "logo": "data:image/svg+xml;base64,...", "pie": "Lasheras & Gil Abogados, S.L.P. · Zaragoza"}
```

- Colores en hexadecimal de 3, 4, 6 u 8 cifras; otro valor se ignora. Rigen en el tema claro y en papel.
- `oscuro`: version para el tema oscuro. Un color corporativo oscuro (un granate, un azul marino) no se lee sobre fondo negro: si no se da, en tema oscuro se mantienen los colores del tema, que si contrastan.
- `logo`: solo si lo aporta el usuario, como data URI de imagen de menos de 15 KB. Va en la cabecera o, en una presentacion, en la portada. Sobre la portada oscura del documento largo conviene una version clara.
- `pie`: linea que se anade al pie del documento.

```js modulo=marca
<script>
/* Identidad del despacho para los reportes. Se copia integro, despues del motor, solo si
   los datos llevan el bloque marca. */
(function(){
"use strict";
var R = Reportes, D = document, m = R.datos.marca, hex = /^#([0-9a-f]{3,4}|[0-9a-f]{6}|[0-9a-f]{8})$/i;
if (!m) return;
function variables(c) {
  var v = "";
  if (hex.test(c.acento || "")) v += "--acento:" + c.acento + ";--acento-fuerte:" + (hex.test(c.acento_fuerte || "") ? c.acento_fuerte : c.acento) +
    ";--acento-suave:color-mix(in srgb," + c.acento + " 12%,var(--superficie));";
  (c.serie || []).slice(0, 6).forEach(function (x, i) { if (hex.test(x)) v += "--c" + (i + 1) + ":" + x + ";"; });
  return v;
}
/* En claro y en papel, los colores de marca; en oscuro, su version oscura o los del tema. */
var css = "@media (prefers-color-scheme:light),print{:root{" + variables(m) + "}}";
if (m.oscuro) css += "@media screen and (prefers-color-scheme:dark){:root{" + variables(m.oscuro) + "}}";
R.html("style", "", D.head).textContent = css;
if (m.pie) R.html("p", "", D.querySelector(".pie"), m.pie);
function logo() {
  if (!/^data:image\/(png|jpeg|svg\+xml|webp);base64,/.test(m.logo || "")) return;
  var destino = D.querySelector(".maqueta-portada") || D.querySelector(".contenedor>header"), img = R.html("img", "", null);
  img.src = m.logo; img.alt = m.nombre || "";
  img.setAttribute("style", "display:block;max-height:52px;max-width:220px;margin:0 0 12px");
  destino.insertBefore(img, destino.firstChild);
}
/* Tras la carga, para encontrar la portada de una presentacion, que monta su script. */
if (D.readyState === "loading") D.addEventListener("DOMContentLoaded", logo); else logo();
})();
</script>
```

---

## Plazos en dias habiles (`plazos`)

Anade dos calculos a `cifras`:

- `{"calculo": "dias_habiles", "desde": "2026-09-17", "hasta": "2026-10-05", "festivos": [...], "agosto_inhabil": true}`: los dias habiles entre dos fechas.
- `{"calculo": "vencimiento", "desde": "2026-10-01", "dias": 20, "festivos": [...], "unidad": "fecha"}`: la fecha en que vence un plazo de tantos dias habiles, contados desde el dia siguiente.

Se excluyen sabados y domingos. `festivos` es la lista de **todos los demas dias inhabiles** que correspondan (festivos nacionales, autonomicos y locales del lugar, y los que la norma procesal aplicable declare inhabiles), en `AAAA-MM-DD`, **aportados por el usuario o verificados en la sesion**: el modulo no trae ningun calendario. `agosto_inhabil` solo para plazos procesales en que agosto lo sea. Un vencimiento alimenta un diagrama de plazos con `"fin": "@clave"`. El resultado es orientativo y se dice asi en el bloque de supuestos.

```js modulo=plazos
<script>
/* Plazos en dias habiles para los reportes. Se copia integro, despues del motor, solo si
   alguna cifra usa dias_habiles o vencimiento. */
(function(){
"use strict";
var R = Reportes, DIA = R.DIA;
function habil(t, def) {
  var d = new Date(t), s = d.getUTCDay();
  return s !== 0 && s !== 6 && !(def.agosto_inhabil && d.getUTCMonth() === 7) && (def.festivos || []).indexOf(d.toISOString().slice(0, 10)) < 0;
}
R.calculos.dias_habiles = function (def) {
  for (var t = R.fecha(def.desde), fin = R.fecha(def.hasta), n = 0; t < fin;) { t += DIA; if (habil(t, def)) n++; }
  return n;
};
R.calculos.vencimiento = function (def) {
  if (!(def.dias > 0)) throw new Error("el vencimiento necesita dias");
  for (var t = R.fecha(def.desde), n = 0; n < def.dias;) { t += DIA; if (habil(t, def)) n++; }
  return t;
};
})();
</script>
```


---

## Mapa de Espana (`mapa`, con `mapa_ccaa` o `mapa_provincias`)

Mapa de coropletas: cada comunidad autonoma o provincia se pinta con mas o menos intensidad segun su valor, en cinco tramos iguales desde cero con cifras redondas, con leyenda, recuadro de Canarias y Ceuta y Melilla como puntos. Las zonas sin dato salen rayadas. Contornos simplificados de Natural Earth (dominio publico).

Se copian **dos** piezas: el modulo `mapa` (el codigo) y el bloque de contornos del nivel que se use: `mapa_ccaa` (unos 6 KB) o `mapa_provincias` (unos 11 KB).

```json
{"tipo": "mapa", "nivel": "ccaa", "unidad": "asuntos", "fuente": "cgpj",
 "valores": {"Andalucia": 412, "Madrid": 520, "ES-CT": 388}, "destacar": ["Madrid"]}
```

- `valores`: por codigo ISO 3166-2 (siempre seguro: `ES-AN`, `ES-MD`, `ES-Z`...) o por nombre, con o sin tildes. Se aceptan el nombre oficial y los habituales: «Madrid» o «Comunidad de Madrid», «Murcia», «Comunidad Valenciana», «Baleares», «Asturias», «Navarra»; en provincias, «Vizcaya» o «Bizkaia», «Gerona» o «Girona», «La Coruna», «Alicante» o «Alacant»... Un nombre que no existe da error, no se ignora. Un valor `null` deja la zona sin dato.
- `tasa`: en lugar de `valores`, `{"numerador": {...}, "denominador": {...}, "por": 1000}` calcula cada zona como numerador / denominador x por (reclamaciones por 1.000 polizas, asuntos por 100.000 habitantes). Para comparar zonas de tamano muy distinto se usan tasas, no totales. La unidad de una tasa se dice en el subtitulo y en `nombre_valor` («por 1.000 polizas»), con `"unidad": "num"`.
- `nivel`: `ccaa` (por defecto) o `provincias`. `destacar`: zonas con el borde marcado, por codigo o nombre.
- Solo valores no negativos. Cualquier valor puede ser `"@clave"` de `cifras`. La tabla de datos lista las zonas de mayor a menor.

```js modulo=mapa
<script>
/* Mapa de Espana para el motor de reportes. Natural Earth, dominio publico. */
(function(){
"use strict";
var R = Reportes, svg = R.svg, fmt = R.fmt, num = R.num, SIN = R.T.sin_dato || (/^en/.test(R.IDIOMA) ? "no data" : "sin dato");
var PUNTOS = {"ES-CE": ["Ceuta", 146, 368], "ES-ML": ["Melilla", 231, 396]}, RECUADRO = [303, 314, 183, 92];
/* Otros nombres habituales de cada zona (sin tildes ni mayusculas). */
var ALIAS = {
  ccaa: {madrid: "ES-MD", murcia: "ES-MC", comunidadvalenciana: "ES-VC", valenciana: "ES-VC", islasbaleares: "ES-IB", baleares: "ES-IB",
    principadodeasturias: "ES-AS", comunidadforaldenavarra: "ES-NC", catalunya: "ES-CT", euskadi: "ES-PV", islascanarias: "ES-CN", rioja: "ES-RI"},
  provincias: {alava: "ES-VI", araba: "ES-VI", vizcaya: "ES-BI", bizkaia: "ES-BI", guipuzcoa: "ES-SS", gipuzkoa: "ES-SS", gerona: "ES-GI", lerida: "ES-L",
    lacoruna: "ES-C", coruna: "ES-C", orense: "ES-OR", baleares: "ES-PM", islasbaleares: "ES-PM", alacant: "ES-A", castello: "ES-CS", rioja: "ES-LO",
    tenerife: "ES-TF", navarra: "ES-NA", nafarroa: "ES-NA"}
};
function normal(s) { return String(s).normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().replace(/[^a-z0-9]/g, ""); }
R.mapas = {};
R.tipos.mapa = function (fig, g, id) {
  var nivel = g.nivel || "ccaa", zonas = R.mapas[nivel];
  if (!zonas) throw new Error("falta el bloque de contornos mapa_" + nivel);
  var todas = Object.assign({}, zonas, PUNTOS), indice = Object.assign({}, ALIAS[nivel]);
  Object.keys(todas).forEach(function (c) { indice[normal(todas[c][0])] = c; indice[normal(c)] = c; });
  var zona = function (k) { var c = indice[normal(k)]; if (!c) throw new Error("no hay ninguna zona llamada " + k); return c; };
  /* "tasa" calcula cada valor como numerador / denominador x por (reclamaciones por 1.000 polizas...). */
  var origen = g.valores || {}, t = g.tasa;
  if (t) {
    origen = {};
    Object.keys(t.numerador || {}).forEach(function (k) {
      var d = (t.denominador || {})[k];
      if (!num(d) || !d) throw new Error("falta el denominador de " + k);
      origen[k] = t.numerador[k] / d * (t.por || 1);
    });
  }
  var valores = {}, marcadas = (g.destacar || []).map(zona);
  Object.keys(origen).forEach(function (k) { valores[zona(k)] = origen[k]; });
  var lista = Object.keys(valores).map(function (c) { return valores[c]; }).filter(num);
  if (!lista.length) throw new Error("faltan valores");
  if (R.minimo(lista) < 0) throw new Error("el mapa no admite valores negativos");
  /* Cinco tramos iguales desde cero, con un tope cuyos quintos son cifras redondas. */
  var m = Math.pow(10, Math.floor(Math.log10(R.maximo(lista) || 1))), tope = m * [1, 2, 2.5, 3, 4, 5, 10].filter(function (p) { return p * m >= R.maximo(lista); })[0];
  var opac = [0.22, 0.4, 0.58, 0.76, 0.94], tramo = function (v) { return Math.min(4, Math.floor(v / tope * 5)); };
  var c0 = R.color(g.color || "acento", 0), s = R.lienzo(fig, 500, 420, g.resumen);
  s.style.maxWidth = "560px";
  /* Sin dato: rayado, para que no se confunda con el tramo mas bajo. */
  var raya = svg("pattern", {id: "sin-dato-" + id, width: 6, height: 6, patternUnits: "userSpaceOnUse", patternTransform: "rotate(45)"}, svg("defs", {}, s));
  svg("rect", {width: 6, height: 6, fill: "var(--superficie-2)"}, raya); svg("line", {x1: 0, y1: 0, x2: 0, y2: 6, stroke: "var(--borde)", "stroke-width": 2}, raya);
  svg("rect", {x: RECUADRO[0], y: RECUADRO[1], width: RECUADRO[2], height: RECUADRO[3], rx: 4, fill: "none", stroke: "var(--borde)", "stroke-dasharray": "3 3"}, s);
  Object.keys(todas).forEach(function (c) {
    var v = valores[c], marca = marcadas.indexOf(c) > -1, at = num(v) ? {fill: c0, "fill-opacity": opac[tramo(v)]} : {fill: "url(#sin-dato-" + id + ")"};
    Object.assign(at, {stroke: marca ? "var(--texto)" : PUNTOS[c] ? "var(--borde)" : "var(--superficie)", "stroke-width": marca ? 2 : 0.8});
    var forma = PUNTOS[c] ? svg("circle", Object.assign({cx: PUNTOS[c][1], cy: PUNTOS[c][2], r: 5}, at), s) : svg("path", Object.assign({d: todas[c][1]}, at), s);
    R.consejo(forma, todas[c][0] + ": " + (num(v) ? fmt(v, g.unidad) : SIN));
  });
  /* La unidad solo al final de cada tramo («0\u2013120 asuntos»), salvo moneda y porcentaje, que la llevan en cada cifra. */
  var simbolo = /^(eur|moneda|pct)$/.test(g.unidad || ""), ini = function (v) { return fmt(v, simbolo ? g.unidad : "num", true); };
  R.leyenda(fig, opac.map(function (o, i) { return {color: c0, opacidad: o, texto: ini(tope * i / 5) + "\u2013" + fmt(tope * (i + 1) / 5, g.unidad, true)}; })
    .concat(lista.length < Object.keys(todas).length ? [{color: "repeating-linear-gradient(45deg,var(--superficie-2) 0 3px,var(--borde) 3px 5px)", texto: SIN}] : []));
  return {cabecera: [R.T.concepto, g.nombre_valor || R.T.valor], unidad: g.unidad,
    filas: Object.keys(valores).filter(function (c) { return num(valores[c]); }).sort(function (a, b) { return valores[b] - valores[a]; }).map(function (c) { return [todas[c][0], valores[c]]; })};
};
R.tipos.mapa.fijo = true;
})();
</script>
```

```js modulo=mapa_ccaa
<script>
Reportes.mapas.ccaa = {"ES-NC":["Navarra","M273 28l-3 3h-2l-1 4-3 3-1 4-7 2-2 9-1 1 1 3-2 1-2-1-3 3h3v5l12 2v2h3l4 6 6 2v4h-4l-3 3v2l12 5 5 1 3-6-2-4-1-5 5-14 2-1 2-4h4l1-3 4-2 3-7 3-1-2-1h-5l-12-5-1-3-2 4h-3l-2-2 3-3v-5l-5-2-2 2-2-2zM295 66v1h2l-1-2z"],"ES-PV":["Pais Vasco","M248 25l-7-3-1 2-2-3h-6l-4 3 1 3-3-2h-2l-1 2-5 1-5 3 1 4 6-3 4 1-1 7 3 1 2-2 1 2-1 1 2 2-2 2-7-2-2 3 2 2 4-2-1 5h4l7 5v4l3-2 2 4 4 2 3-2 3 2v-5l-2 1-1-2 3-2 2 1 2-1-1-3 1-1 2-9 7-2 1-4 3-3 1-4h2l3-3-2-5-4 3v1l-1-1-6 2z"],"ES-AR":["Aragon","M347 113v-2l3-3v-2l-3-1-1-3 10-9-1-3 3-3 2-5 1-10-2-7 3-5-4-5-9 1-2-2-3 3-3-3-8 2-2-2-2-3h-3l-3-2-3 2-4-1-1 2-6-5v-2l-3 1-2 6-5 3-1 3h-4l-2 4-2 1-5 14 1 5 3 3-3 5-1 2-5-1-11-4 2 7-1 3 2 4-1 2-6 3 1 8-3 2v-2l-2-1-3 4 1 8 3 1h4l5 3 7 7v4l2 2v10l-1 1-3-1-1 5-4 4 3 3v2h2l4 4h4v3h4l1-3 2 4 6 2-3 3v2h8l2 5 3-1-2-2 1-3 2-2 5-2 2-7 5-1 5-6-2-3 2-1-1-6-2-1-1-2 6-2 1-3 8 3 5-1 3-4v-3l1-5-3-5 5-6 1-5-2-3z"],"ES-CT":["Cataluna","M433 103l5-2 8-6 3-5-1-6-3-3v-4l1-2 4 1 2-3-5-2v-3l-9-2-8 3-2 1 1 2-4-1-2 1-8-4h-5l-3 3h-2l-2-4-8-3-7 4-2-1-2-2 2-1-2-1 1-3-3-5h-7l-2-3-15-3-1 4 3 6 2 1-3 5 2 4v6l-3 12-3 3 1 3-10 9 1 3 3 1v2l-3 3-1 4 2 3-1 5-5 5 3 6-1 5v3l-3 4 4 2v2l8 5 2-3 6-2-3 3h-2v1l3-1 7-6-4-3-3-1 11-11 3-2 3 1 2-2 11-4 18-4 4-3 5-6z"],"ES-EX":["Extremadura","M160 207l-8-9 2-5-1-4-5 2v-5l-3-1 1-10 1-1-1-6-6 2-6-4h-3l-1-2-4 2-6-3 1-2-6-4-10 6-2 4-8 1-2-1-3 1-3 3 1 3 2 1 2 4-1 7-3 2-1 5-19 1 2 4 7 6v6l2 3v3l3 2 1 3h5l1 4-3 5v2l-7 5v6l-4 8 9 12 6-1 5 1v3l7 1 1 3 3 1 2-2 3 2 6 3 8-3 1-5 3-3h4v4l5-2 2-4-1-9 7-7 2-1 4-3 1-2 6-2 2-6h3v-2l-3-2-1-4h4l-1-2 2-5 6 1-4-6 3-4-1-2-6 4z"],"ES-AN":["Andalucia","M181 254l-13-9-4-2-1-3-6-2-4 1-1 2-4 3-2 1-7 7 1 8v4l-6 3-1-4h-4l-3 3-1 5-8 3-6-3-3-2-2 2-3-1-1-3-7-1v-3l-5-1-3 8h-3l-2 2h-4l-1 6-5 6-2 6 3 19 12-1h-1l1-1 6 2-2-2 4-3-2 4 1 2 14 9 4 7h1v-4l5-1-5 2v4l-3 2 1 5 4 1 2 5h2l-2 2-1-2-2-1 6 10 4 6h4l5 4 3 1 3 3 6-2 1-6 3 2 1-6 4-7 10-4h9l2-3h2l5-7 6 1 13-2 4 1 5-1 6 2 3-2h14l7 3 3-1 3-5 3-1h6l5 5 4-2 2-5 4-3 3-12 6-8-3-3h-4l-6-10 1-9-7-2-6-6-7-2 4-5v-4l-2-2v-4l-3-1v-4l-6-1-5 3h-3l-1 2-2-3-3 2-6-2-5 4-3-2-2 2-6-1-4 2-12-1h-2v2z"],"ES-GA":["Galicia","M64 6v-1l-5 4h-1v2h-2l2-2-2-3-5 3v3l-1-1-5 4h-3l1 2-2 3 6-1-5 2 5 1-2 5-2-3-2-1-1 2-1-1-6 3-5 1-4-2-6 2 2 3-3-1-1 2h-3l-3 2 4 1-4 1-2 3 1 2-1 5 3-2 2 1 1 8 8-4-1 2-4 4-2 5 2 2 4-3h1l1-3 2 2 2-2-3 5v5l-2-1-2 1 3 3 7-2-4 5h-2l-2 4 7-2 2-3v3l-8 6 1 1-3 1 1 10 9-7 14-5 1 4h2l2 2-5 6 2 4h4l5-5 1 3 6-2 4 1v2l3-1h2v2l8-3 1-4 1-1 4 2 3-1v-3l-2-2 10-10v-3l-3-2v-4l-3-1h-5l2-6-1-3 6-5 1-5-1-3-4-1 5-6-1-2-3 2-1-3-3-2-2-6-2-1v-1l4-3 1-3h-8l-4-6-6-2-3 2v-3l-2 1z"],"ES-CL":["Castilla y Leon","M168 39l-3-3-1-3-2-3-6 3-2 3-9 1v2l-5 1-6-1-3 4-5-2-2-2-3-1-2 2h-3l-1 1-5-2-4 3 2 1-2 2h-7l-3 1-2-1-1 5-6 5 1 3-2 6h5l3 1v4l3 3-2 5-3 1-5 6 2 2v3l4 1 1-2 4 3 5-2v4h2l-2 6 1 4h6l6 4-4 7-6 6-5 1-6 10h-4l-1 2 5 7v10l-2 3 2 3-2 3 2 4-2 4 1 1 9-1 2-4 10-6 6 4-1 2 6 3 5-2v2h3l6 4 6-2 1 6 6 1 5-3 2 2 6-7h3l1 3h4l1-6 2 1 2-4 3-1 2-9 1 1 3-1 3-7 3-1 3-8 4-1 6-7 8-3-1-3h6l2-1h8l3-1 2 2h4l4 2 1 4 2-1 3 4h5l5-2 3 2v-4l-3-1-1-7 3-5 2 1v2l3-2-1-8 6-3 1-2-2-4 1-3-2-5-4 2-4-1-2-5 1-2h-5l-1-2-8 1-2 5-6-1v-4l-4 5-3-3-3-1-3-5 1-3-1-3 2-2v-3l-1-4-1-1 2-2v-2h8l-7-6h-4l1-5-4 2-2-2 2-3 5 2 4-2-2-2 1-1-1-2-2 2-3-1 1-7-4-1-7 3-7-2-4 4h-2l-5 4-1 4 2 1 3-2-2 4 3-1v3l-5 2h-1v-2l-2 2-4-1-1-1 2-2-3 1-1-5-4-2-2-3-10 2zM234 52v2l4 2 8 1v-1h-2l-1-1 2-2-2-1-7-1z"],"ES-VC":["Comunitat Valenciana","M351 154l-6-4v-2l-3-2-6 1-1-1-7-2-1 3-6 2 1 2 2 1 1 6-2 1 2 3-5 6-5 1-2 7-5 2-2 2-1 3 2 2-4 1v-4l-3-2-7 2-3 12h-4l-4 6-1 5 3 4 9 3-2 12 4 4h5l2 3-1 5 2 4-4 1v7l-2 4v2l3 2 1 3-2 9 3 6 5 5 5-7 1-8 4-2v-6l3-1 3-5 9-3 1-4 5-1v-1l5-4-3-4-6-2-3-3-4-8v-3l-3-6-1-8 9-17 18-25 3-6zM288 171l-1 2h-3l3 6 4 1 6-2-2-3-4-1-2-4z"],"ES-MC":["Region de Murcia","M308 278l-5-2-4-8 2-9-1-3-3-1v-3l2-3v-5v-3l-6-4-5 3-2-1-2 2-2 6 1 7-3 2-4 1-1-3h-2l-6 4h-4l-6 4-5 8 6 6 7 2-1 9 6 10h4l3 3 5-2 1-3 5-3 3-1 5 2v-2l6 1 7-2 1-2-4-1-1-4 2-3 1 1zM309 283l-1-1v4l1 1z"],"ES-AS":["Asturias","M86 19l2-3 2-1h10l5 1 2-1 8-1 6 1 6-1v-2l2-1 5 4 11 1-1 2 4-1 9 3 19 3v4l-1 2-2-1-4 1-1 4h-4l-2-3-6 3-2 3-9 1v2l-5 1-6-1-3 4-5-2-2-2-3-1-2 2h-3l-1 1-5-2-4 3 2 1-2 2h-7l-3 1-2-1-1-3-4-1 1-3 4-2-1-2v-1l-3 2-1-3-3-2-2-6-2-1v-1z"],"ES-CB":["Cantabria","M176 23l-1 5h-2l-4 1-1 3-4 1 1 3 3 5 11-1 2 2 4 2 1 4h3l-2 2 4 2 3-2v2h1l5-2v-3l-3 1 2-4-3 2-2-1 1-4 5-3 2-1 4-4 8 2v-5l4-2h4l2-2v-1l-2-2-9-1h-2l3-2-5-2-7 2 1 1-3 1-1-1 3-2h-2l-13 4z"],"ES-CN":["Canarias","M475 328l-1 1-9 4-3 8v1l3 1 3-4 8-3 2-10-2-1zM324 342h-4l-4 5 6 14 4-13zM457 349l-7 22-5 4-5 2v1l5 1 6-5 9-4 3-7 1-13-3-3zM373 369l1-5 9-9h-7l-7 7-9 3-3-1-2 1 8 17 5-2 4-5zM340 377l4 4 4-4v-2l-5-3-3 2zM408 378v-5l-2 2-9-1v4l-4 4v3l2 4 3 3 4 2 7-6v-7zM317 390l-2 3h-4v2l6 3 4-8-2-2z"],"ES-IB":["Illes Balears","M486 182l-4-6-1 2-2-2-10 1v2l1 1v2h5l9 6h2v-3l2 1zM451 191h-4l-2-2v-2l3-3-4 1v-2l4-2h-1l-13 4-16 12v3l1 1h2l2 3 2-3 4-1 2 1 2 7 6 1 4 4 6-5 3-7 4-6 1-4-4-2zM438 217l-1 1 2 2 1-3zM390 221l-2-1-5 2-3 2 1 3-3 1v3l6 2 1-3 7-6zM385 237l-2 2v3l3-2 4 1v-1l-3-1z"],"ES-RI":["La Rioja","M250 65l12 2v2h3l4 6 6 2v4h-4l-3 3 1 5-4 2-4-1-2-5 1-2h-5l-1-2-8 1-3 5-5-1 1-4h-2l-1 3-2 2-3-3-3-1-2-2-1-3 1-3-1-4 2-1v-7h-2l2-5h8v3l3-2 4 5 2 1 3-2z"],"ES-CM":["Castilla-La Mancha","M272 160l3-3 1-5 3 1 1-1v-10l-2-3v-3l-12-10h-4v4l-3-2-5 2h-5l-3-4-2 1-1-4-4-2h-4l-2-2-3 1h-8l-2 1h-6l1 3-5 2 4 4 1 3-4 10 2 1v4l5 2 1 5 3 1v3l2 2-2 6 1 1 2-1 1 1 1 7-1 1-4-1-5 2h-6l-11 7-2-1 9-6v-2l-19-9-5 3-2-4-6 5h-5l-1-3h-3l-6 7-3-2-4 3h-7l-1 10 3 1v5l4-2 2 3-2 6 11 11 6-4 1 1-3 5 4 6-6-1-2 5 1 2h-4l1 4 3 1v2l-3 1-2 6-2 1 6 2 1 3 4 2 10 8 6 2 1-2 13 1 4-2 6 1 2-2 3 2 5-4 6 2 3-2 2 3 1-2h3l5-3 2 1h3l1 4 3 1v4l2 2v4l-4 5 7 2 5-8 6-4h4l6-4h2l1 3 4-1 3-2-1-7 3-7 8-3 6 4h2l2-1-2-4 2-2-2-6-6 1-4-6 2-12-9-2-3-4 1-5 3-5 5-2 2-11 2-1v-2h-7l-3-6v-2l-4-1-4-4h-2z"],"ES-MD":["Comunidad de Madrid","M183 147l-1 2h3l-1-1zM226 170l-1-3-3 1 2-7-2-2v-3l-3-1-1-5-5-3v-3l-2-1 4-10-1-3-4-4-3 1-6 7-4 1-3 8-3 1-3 7-3 1-1-1-2 9-3 1-2 4-2-1-1 6h2l5-5 2 4 5-3 19 8v3l-9 6 3 1 10-7h6l5-2 4 1 1-1z"]};
</script>
```

```js modulo=mapa_provincias
<script>
Reportes.mapas.provincias = {"ES-NA":["Navarra","M273 28h3l2 2 2-2 5 2v5l-3 3 2 2h3l2-4 1 3 12 5h5l2 1-3 1-3 7-4 2-1 3h-4l-2 4-2 1-5 14 1 5 2 4-3 6-5-1-12-5v-2l3-3h4v-4l-6-2-4-6h-3v-2l-12-2v-5h-3l3-3 2 1 2-1-1-3 1-1 2-9 7-2 1-4 3-3 1-4h2zM296 65l1 2v1l-2-1z"],"ES-SS":["Gipuzkoa","M272 24l1 4-3 3h-2l-1 5-7 8h-3l-3 2-2-2-9-2 2-2 2-9 3-2v-3l10 2 6-2 1 1v-1z"],"ES-HU":["Huesca","M309 45v2l6 5 1-2 4 1 3-2 3 2h3l2 3 2 2 8-2 3 3 3-3 2 2 9-1 4 5-3 5 2 7-1 10-2 5-3 3 1 3-10 9 1 3 3 1v2l-3 3v4l-4-1-4 3-7-1-4-10-2 1-8-7-2-5-4-5-7-2v-4l2 1 1-2 1-10-1-3-1-1-1 6h-4l3-5-2-3-1-10 2-1-1-2 2-6 1-2z"],"ES-L":["Lleida","M360 48l13 4 2 3h7l3 5-1 3 2 1-2 1 1 2 3 1 7-4 1 3 2 1 2 5-6 2 2 5-3 7 2 1-2 1-1 6-2 3-5-1v7l-2 1 1 2h-7l-1 4h-4l-3 6h-5l-7 3-2-2-2 2-2-2-1 3h-2l-1 2 1-5-2-3 1-4 3-3v-2l-3-1-1-3 10-9-1-3 3-3 3-12v-6l-2-4 3-5-2-1-3-6 1-4z"],"ES-GI":["Girona","M395 65l8 2 3 4 4-3h5l8 4 2-1 4 1-1-2 2-1 8-3 9 2v3l5 2-2 3-4-1-1 2v4l3 3-1 2 2 3-2 4-14 11-1-4h-7l-9-6 1-1h2l3-1-1-2 2-4-1-2-7-3h-7l-2-4 1-3-7-1-2-5-2-1z"],"ES-BA":["Badajoz","M79 243v-6l7-5v-2l3-5-1-4h-5l-1-3-3-3 5-7h2v3h1v-3l-1-2v-1l9 3 2 3-2 3 1 3h3l1-1 4 2 8-1v3l6 4 5-4v2l7-3 4 3 3-1 1-2-1-2 2-1 4 2h2l1-3 1-4h5l3-4 2 2 4-2 2 2 6-4 1 2-3 4 4 6-6-1-2 5 1 2h-4l1 4 3 1v2l-3 1-2 6-6 2-1 2-4 3-2 1-7 7 1 8v4l-6 3-1-4h-4l-3 3-1 5-8 3-6-3-3-2-2 2-3-1-1-3-7-1v-3l-5-1-6 1-9-12z"],"ES-CA":["Cadiz","M147 357l-3-2-1 6-6 2-3-3-3-1-5-4h-4l-4-6-6-10 3 3 2-2h-2l-2-5h-3l-2-4v-2l3-2v-4l4-1 5 2 7 1 2-4h4l2-2 4 2 3-6 2 1-1 4 4-3 3 3 4-3 2 4-1 3-3 1-3-2-1 1-1 1 1 3-1 5-10 6 2 2 5-1 3 8h2l1 2z"],"ES-OR":["Ourense","M46 85l-1-5 2-4-2 1-2-1-2-11 6-4 5 1 3-1 1 3 10 5h4l4-2 5 1 2 4 5-8h5l3 1v4l3 3-2 5-3 1-5 6 2 2v3l-3 1-4-2-1 1-1 4-8 3v-2h-2l-3 1v-2l-4-1-6 2-1-3-5 5h-4l-2-4 5-6-2-2z"],"ES-CC":["Caceres","M79 213l-2-3v-6l-5-4-4-6 19-1 1-5 3-2 1-7-2-4-3-2 1-4 5-2 2 1 8-1 2-4 10-6 6 4-1 2 6 3 4-2 1 2h3l6 4 6-2 1 6-1 1-1 10 3 1v5l5-2 1 4-2 5 9 9-4 2-2-2-3 4h-5l-1 4-1 3h-2l-4-2-2 1 1 2-1 2-3 1-4-3-7 3v-2l-5 4-6-4v-3l-8 1-4-2-1 1h-3l-1-3 2-3-2-3-9-3v1l1 2v3h-1v-3h-2l-3 5z"],"ES-SA":["Salamanca","M93 167l2-4-2-4 2-3-2-3 2-3v-10l-5-7 1-2 4-1 6-9 5-2 6 1 7 4h3v2l3 1 2-4h3l5-1 6 3h3v2l3 1 3-4 4 3-1 4 2 3-3 9-6 5-2 4-4 1 1 1h2l-1 4h-2v2l-2-2-4 2 1 3-2 3h-2l-1-2-4 2h-1l-5-3 1-2-6-4-10 6-2 4-8 1z"],"ES-ZA":["Zamora","M106 119l6-5 4-7-6-4h-6l-1-4 2-6h-2v-4l-5 2-4-3-1 2-4-1v-3l-2-2 5-6 3-1 1-1 10 3 6-1 4 3 6-1 3 2 2-2 1 2 4-1v1l3-1 4 4 1-2 1 5 2 1 1-3 1-1 4 3-1 5 1 3-4 2 4 8-1 2 3 1-4 3 1 10-1 2 1 1v3l-4-1v-2h-3l-6-3-5 1h-3l-1 3-3 1-1-3h-3l-7-4z"],"ES-PO":["Pontevedra","M45 80l-14 5-9 7-1-10 3-1-1-1 8-6v-2l-6 3-3 1 2-4h2l4-5-7 2-3-3 2-1 2 1v-5l4-6 4-2h5l2-2h2v-3l2 2 4-2 7 1v2l4 4-3 6-3 1-5-1-6 4 2 11 2 1 2-1z"],"ES-H":["Huelva","M73 309l-3-19 2-6 5-6 1-6h4l2-2h3l3-8 5 1v3l7 1 1 3 3 1 3-2 2 2 8 5v4l-3 1v3l-2-2-6 2-3 3v1l4 2 3 7-2 5 1 2-1 11 1 11h-1l-4-7-14-9-1-2 2-4-4 3 2 2-6-2-1 1h1z"],"ES-B":["Barcelona","M433 104l-17 8-5 6-4 3-15 4v-2h-2l2-3-5-6v-3l-3-1 1-3-2-1 2-2v-7l5 1 2-3 1-6 2-1-2-1 3-7-2-5 8-2 5 1-1 3 2 4h7l7 3 1 2-2 4 1 2-3 1h-2v2l4 1 4 4h7z"],"ES-T":["Tarragona","M392 125l-14 4-2 2-3-1-3 2-11 11 3 1 4 3-7 6-3 1v-1h2l3-3-6 2-2 3-8-5v-2l-4-2 3-4v-3l1-5-3-6 3-2 3-5h2v-3l3 2 2-2 2 2 7-3h5l3-6h4l1-4h8l-1 3 3 1v3l3 3 2 4-2 2h2z"],"ES-CS":["Castellon","M353 155l-6 11-10 12-9 14-5-3-4 3-3-3-4 2v-4l-2-1-1 2-3-4-1-3 3-3 5-2 3-8h4l5-6-2-3 2-1-1-6-2-1-1-2 6-2 1-3 7 2 1 1 6-1 3 2v2z"],"ES-V":["Valencia","M328 192l-5 10v6l4 9-1 1 1 4 7 9-7 1-3-1-4 3-6 1 3 2-4 2-4-2h-3l-4-1-1-8-6 1-4-6 2-11-9-3-3-4 1-6 4-5h4l2-12 2-1h8l1 5 4-1 3 3v-2l2 5 4-2 3 3 4-3zM289 170l2 4 5 2 1 2-6 2-5-2-2-5h4z"],"ES-A":["Alicante","M334 231l6 2 3 4-5 4v1l-5 1-1 4-9 3-3 5-3 1v6l-4 2-1 8-5 7-5-5-3-6 2-9-1-3-3-2v-2l2-4v-7l4-1-2-4 5 1h3l4 2 4-2-3-2 6-1 4-3 3 1z"],"ES-MU":["Murcia","M308 278v3l-1-1-2 3 1 4 4 1-1 2-7 2-6-1v2l-5-2-3 1-5 3-1 3-5 2-3-3h-4l-6-10 1-9-7-2-6-6 5-8 6-4h4l6-4h2l1 3 4-1 3-2-1-7 2-6 2-2 2 1 5-3 6 4v3v5l-2 3v3l3 1 1 3-2 9 4 8z"],"ES-AL":["Almeria","M277 300l-6 8-3 12-3 2-5 8-3-1-5-4-8 1-1 4-3 2-6-1-2-2h-7l-1-2 4-2-2-3 3-4v-5h2l2-4 1-4 7 3 1-8 5-5 5-2-1-4h2l1-11 3-3 8 3-1 9 6 10h4z"],"ES-GR":["Granada","M225 329h-8l-3 2-6-2-6 1v-3l-2-3-11-4-5-4-1-7 2-2 1-5 5-3 8 1 2-4 10-7 4 2 6-3 5 2h4l2-3 1-5 4-7 6-4v-2l2-1 7 2 5 5-3 3-1 11h-2l1 4-5 2-5 5-1 8-7-3-1 4-2 4h-2v5l-3 4 2 3-4 2z"],"ES-MA":["Malaga","M202 330h-23l-4 7h-2l-2 3h-9l-10 4-2 6-1-2h-2l-3-8-5 1-2-2 10-6 1-5-1-3 1-1 1-1 3 2 3-1 1-3-2-4 8-5-2-3 3 1 1-1 2 1 2-2v-3l4 1 3 2 3-3h2l5 11 4 4 11 4 2 3z"],"ES-SE":["Sevilla","M115 322l1-1-5 1-1-2 1-16-1-2 2-5-3-7-4-2v-1l3-3 6-2 2 2v-3l3-1v-4l-2-2 8-3 2-5 2-3h4l1 1-1 3 5-2 10 17v3l-4 1 1 3 13-4 5 12 3 5 3-1 2 5-3-1v3l-2 2-2-1-1 1-3-1 2 3-11 8-3-3-5 3 1-4-2-1-3 6-4-2-2 2h-4l-2 4-7-1z"],"ES-C":["A Coruna","M27 56l-2 2-2-2-1 3h-1l-4 3-2-2 2-5 4-4 1-2-8 4-1-8-2-1-3 2 1-5-1-2 2-3 4-1-4-1 3-2h3l1-2 3 1-2-3 6-2 4 2 5-1 6-3 1 1 1-2 2 1 2 3 2-5-5-1 5-2-6 1 2-3-1-2h3l5-4v1h1v-3l5-3 2 2-2 3h2v-2h1l5-4v6l-3 10-2 2h-2l-2 5-1 5 2 9-1 4-3 3-5-1-4 2-2-2v3z"],"ES-LU":["Lugo","M64 8l2-1v3l3-2 6 2 4 6h8l-1 3-4 3v1l2 1 2 6 3 2 1 3 3-2 1 2-5 6 5 2-1 7-6 5 1 3-2 5-5 9-2-4-5-1-4 2h-4l-10-5-1-3 3-6-4-4v-2l-1-1 3-5-2-10 3-10h2l2-2 3-10z"],"ES-O":["Asturias","M86 19l2-3 2-1h10l5 1 2-1 8-1 6 1 6-1v-2l2-1 5 4 11 1-1 2 4-1 9 3 19 3v4l-1 2-2-1-4 1-1 4h-4l-2-3-6 3-2 3-9 1v2l-5 1-6-1-3 4-5-2-2-2-3-1-2 2h-3l-1 1-5-2-4 3 2 1-2 2h-7l-3 1-2-1-1-3-4-1 1-3 4-2-1-2v-1l-3 2-1-3-3-2-2-6-2-1v-1z"],"ES-S":["Cantabria","M176 23l4 1 7-1 13-4h2l-3 2 1 1 3-1-1-1 8-2 4 2-3 2 11 1 2 2v1l-2 2h-4l-4 2v5l-8-2-4 4-2 1-5 3-1 4 2 1 3-2-2 4 3-1v3l-5 2h-1v-2l-3 2-4-2 2-2h-3l-1-4-4-2-2-2-11 1-3-5-1-3 4-1 1-3 4-1h2z"],"ES-BI":["Bizkaia","M224 25h2l3 2-1-3 3-2 6-1 3 3 1-2 9 4v3l-3 2v6h-5v3h-2l-7-1-2-2v-2l-2-3-1 2-3 1-5-3-6 3v-5l4-2 5-1z"],"ES-TF":["Santa Cruz de Tenerife","M319 388l2 2-4 8-6-3v-2h4zM341 372h3l4 3v2l-3 3h-2l-3-3zM372 375l-4 5-5 2-8-17 2-1 3 1 6-2 3-1 7-7h6l1 2-9 7zM325 344l1 4-4 13-5-15 3-4z"],"ES-GC":["Las Palmas","M408 380l1 1v7l-3 3-4 3-4-2-3-3-2-7 4-4v-4l9 1 2-2zM458 348l4-1 2 3-1 13-3 7-9 4-6 5-5-1v-1l5-2 5-4zM476 325l2 1-2 10-8 3-3 4-3-1 3-9 5-3 4-1zM476 322l-1 2-1 1 1-3z"],"ES-PM":["Illes Balears","M389 240h1v1l-4-1-3 2v-3l2-2zM391 221l1 3-7 6-1 3-6-2v-3l3-1-1-3 3-2 5-2zM453 189l4 2-1 4-4 6-3 7-6 5-4-4-6-1-2-7-2-1-4 1-2 3-2-3h-2l-1-1v-3l20-14 9-2h1l-4 2v2l4-1-3 3v2l3 2zM486 183l2 3-2-1v3h-2l-9-6h-5v-2l-1-1v-2l10-1 2 2 1-2zM440 218l-1 2h-1l-1-2 3-1z"],"ES-Z":["Zaragoza","M297 58l6-5v14l2 3-3 6 4-1 1-5h2l-1 13-1 2-2-1v4l7 2 4 5 2 5 8 7 2-1 4 10 7 1 4-3 4 1-1 1 2 3-1 4-5 5v2l-6 1-3-4-13-6-3-4h-2l2 6-4-4-1 3 1 3-3 3-2-2-1 3-3-2-3 3-5-4-2 2-3-1-1 4-5-1-2 6h-5l-12-10h-4l-3-1-1-7 2-4 2-1 1 3 3-2-1-8 6-3 1-2-2-4 1-3-2-7 11 4 5 1 4-7-3-3-1-4 3-7-1-3 3-6h2l2-4z"],"ES-LO":["La Rioja","M250 65l12 2v2h3l4 6 6 2v4h-4l-3 3 1 5-4 2-4-1-2-5 1-2h-5l-1-2-8 1-3 5-5-1 1-4h-2l-1 3-2 2-3-3-3-1-2-2-1-3 1-3-1-4 2-1v-7h-2l2-5h8v3l3-2 4 5 2 1 3-2z"],"ES-VI":["Araba/Alava","M235 59l-1-2-6-5h-4l1-5-4 2-2-2 2-3 5 2 4-1-2-3 1-1-1-2-2 2-3-1 1-3-1-2 1-1h4l1-2 2 3v2l2 2 9 1-1-2 4-1v3l-2 2 9 2 3 2 1 2-3 6 1 3-2 1-2-1-3 2 1 2 2-1v5l-3-2-3 2-4-2-2-4-2 2z"],"ES-AB":["Albacete","M299 241l-6-4-5 3-2-1-4 8 1 7-3 2-4 1-1-3h-2l-6 4h-4l-6 4-5 8-7-2 4-5v-4l-2-2v-4l-3-1v-4l-6-1v-3l2-2 2-4-4-4-1-3-4-2 3-6-1-4 4-6-1-2 8-1 5 5 2-3 1 3 4-3 5 1-2-4h3l1 3h7l1-1 9-5 2 3 9 2-2 12 4 5h5l2 3-1 5 2 4z"],"ES-TE":["Teruel","M294 181v-2l3-1-1-2-5-2-2-4-1 3h-4v-3h-4l-4-4h-2v-2l-3-3 4-4 1-5 3 1 1-1v-10l-2-3v-3h5v-3l3-3 4 1 1-4 3 1 2-2 5 4 3-3 3 2 1-3 2 2 3-3-1-3 1-3 4 3-2-5h3l2 4 13 6 3 4 6-1 3 4-1 8-3 4-5 1-8-3-1 3-6 2 1 2 2 1 1 6-2 1 2 3-5 6-5 1-2 7-5 2-2 2-1 3 2 2-3 1-2-5z"],"ES-CU":["Cuenca","M294 179v2l-2 1-2 11-4 1-2 2-2 4v6l-9 5-1 1h-7l-1-3h-3l2 4-5-1-4 3-1-3-2 3-5-5-8 1-2-4-3 2 1-2-3-3 1-8-7-11 1-5h-2l-1-3 4-2-1-3h3v-2l3 2 4-2v-9h3l3-2 4 1-1-5 2 1 3-1v-4l3 2 1-3 3 1 2-2 6 3h2l2 8 4 2 1 4h2l4 4h4v3l3 6z"],"ES-TO":["Toledo","M145 185l1-10 1-1 6 1 5-3 2 2 6-7h3l1 3h5l6-5 3 4 4-3 19 9v2l-9 6 2 1 11-7 12-1 1 4h2l-1 5 7 11-1 8-1 1h-3l-3-2-5 1-1 3-6 1-3 4-5 1-3-1-2 1-4-1v-3h-6l1-5h2v-5h-4l-1 3-2 1-6-1-2 1-2-3-3 5-5 1v-4l-4-2-2 7-9-9 2-5-1-4-5 2v-5z"],"ES-LE":["Leon","M162 30l2 3 1 3 3 5-2 1-4 6-1 5 2 2-1 15h-2v4h-3v1l-2-2-5 2-1 2-4 1v7l-1 1-4-3-1 2-2-1-2-3-3 1v-1l-4 1-1-2-2 2-3-2h-6l-4-2-6 1-8-2-2-1 1-4-3-3v-4l-3-1h-5l2-6-1-3 6-5 1-5 2 1 3-1h7l2-2-2-1 4-3 5 2 1-1h3l2-2 3 1 2 2 5 2 3-4 6 1 5-1v-2l9-1 2-3z"],"ES-SO":["Soria","M269 89l2 5-1 3 2 4-1 2-6 3 1 8-3 2v-2l-2-1-3 5 1 7 3 1v4l-3-2-5 2h-5l-3-4-2 1-1-4-4-2h-4l-2-2-6 1h-5l-5-4v-4l-7-4v-2h3l4-7 2-1v-4h1l3 3 3-4h2l3-6 5-1 1-4 2 1-1 3 6 1 2-5 8-1 1 2h5l-1 2 2 5 4 1z"],"ES-BU":["Burgos","M235 58h-8v2l-2 2 1 1 1 4v3l-2 2 1 3-1 3 3 5 4 1v2l-2 5-7 6-4-3v4l-2 1-4 7-3-1-1 2h-3l-3 3v2h-1l-1-2h-1l-7-6-1-7-1-4h3l4-4-1-1-4 1 2-4-4 1-1-4-3-1v-2l-2-1-1-8-2-1 1-3h2l-2-5 1-5 4-3h2l4-3v2h1l5-2v-3l-2 1-1-1 2-2v-1l-3 2-2-2 1-3 5-4h2l4-4 8 2 6-3 4 1-1 7 3 1 2-2 1 2-1 1 2 2-4 2-5-2-2 3 2 2 4-2-1 5h4zM238 51l7 1-2 3 1 1h2v2l-8-2-4-2 1-3z"],"ES-AV":["Avila","M171 170l-2-3h-3l-6 7h-2l-1-2-5 3-5-1-1-6-6 2-7-4 2-3-1-3 4-2 2 2v-2h2l1-4h-2l-1-1 4-1 2-4 6-5 3-6v-5l-2-2 2-3 4-1 5 3 5-3v3l5 7v5h3l2 9 6-1v-2l3 1-1 3h-3l-2 9-3 1-2 4-2-1-1 5z"],"ES-P":["Palencia","M191 52l-7 4-1 5 2 5h-2l-1 3 2 1 1 8 2 1v2l3 1 1 4h4l-2 3 4-1-3 5h-3l1 5-3-2-11 2h-2v-3l-2 1-3-4-5 4-3-5h-4l2-11h-3v-3v-3h2v-4h2l1-6-1-2 1-7-2-2 1-5 4-6 13-3 2 3 4 2 1 4h3l-2 2z"],"ES-CR":["Ciudad Real","M238 211l1 2-4 6 1 4-3 6 4 2 1 3 2 2 2 3-2 3-2 2v3l-5 3h-2l-2 2-2-3-3 2-6-2-5 4-3-2-2 2-6-1-4 2-13-1-2 2-5-2-10-8-4-2-1-3-6-2 2-1 2-6 3-1v-2l-3-1-1-4h4l-1-2 2-5 6 1-4-6 3-4-1-2h3l3-5 2 3 2-1 6 1 2-1 1-3h4v5h-2l-1 4 1 2 1-1h4v3l3 1 4-1 2 1 5-1 3-4 6-1 1-3 5-1 3 2 4-1 3 3-1 2 3-2zM163 200l5 3-1 4-4 2-2-2z"],"ES-CO":["Cordoba","M194 299l-8 2-1 6-2 2-2-2-1-2h-2l-3 3-4-2-2-5-2 1-2-1-4-8v-3l-3-5-12 4-2-1 1-3h3v-3l-10-16 2-5-2-8 8-8 2-1 4-3 1-2 4-1 6 2 1 3 4 2 10 8 7 3 3 9-4 6v9l4 5-2 4z"],"ES-GU":["Guadalajara","M265 152l-6-3-2 2-3-1-1 3-3-2v4l-3 1-2-1 1 5-4-1-3 2h-3l-1 9-3 2-3-2v2h-3l-1-5-3 1 2-7-2-2v-3l-3-1-1-5-5-3v-3l-2-1 4-10-1-3-4-4 5-2-1-3h6l2-1h8l2-1 3 2h4l4 2 1 4 2-1 3 4h5l5-2 3 2v-4h4l12 10v3l2 3 1 7-2 4-3-1-1 5-4 4-2-1-2-8z"],"ES-J":["Jaen","M245 268l-2 1v2l-6 4-4 7-1 5-2 3h-4l-5-2-6 3-4-2-10 7-2 4h-3l-10-11 2-4-4-5v-9l4-6-4-11h14l4-2 6 1 2-2 3 2 5-4 6 2 3-2 2 3 1-2h3l5-3 2 1h3l1 4 3 1v4l2 2v4z"],"ES-M":["Madrid","M184 148l1 1h-3l1-1zM226 172v4l-4-1-5 2h-6l-10 7-3-1 9-6v-3l-19-8-5 3-2-4-5 5h-2l1-6 2 1 2-4 3-1 2-9 1 1 3-1 3-7 3-1 3-8 4-1 6-7 3-1 4 4 1 3-4 10 2 1v3l5 3 1 5 3 1v3l2 2-2 7 3-1z"],"ES-SG":["Segovia","M188 148l-5-1-1 2-3 1-2-9h-3v-5l-5-7v-3l4-5v-2l4 1-1-5 17-5 1-3 9 5v-2l2-2 5-1 1 2h3v2l3 1v4l5 4-2 1h-6l1 3-8 3-6 7-4 1-3 8-3 1z"],"ES-VA":["Valladolid","M140 83l4 3-1 3-2-1zM148 74v2h-1l-1-1zM194 107l-1 3-17 5 1 5-4-1v2l-4 5-5 3-5-3-5 1-4-3-3 1 1-3-1-10 4-3-3-1 1-2-4-8 4-2-1-3 1-5-4-3v-7l4-1 1-2 5-2 2 2v-1h1v6h3v3l-3 7 1 1h4l3 5 5-4 3 4 2-1v3h2l11-2 3 2 1 6z"]};
</script>
```
