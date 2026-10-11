# Modulos opcionales del motor

Algunos tipos de grafico pesan demasiado para ir en todos los reportes. Viven aqui como **modulos**: un `<script>` que se copia integro, sin modificarlo, **justo despues del script del motor** y solo en los reportes que usan ese tipo. El modulo registra su tipo en el motor y, a partir de ahi, se declara en `datos-reporte` como cualquier otro grafico.

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

- **Maximo 24 nodos.** Un diagrama mayor no se lee: se divide en dos o se resume.
- Texto de cada caja corto, en una o dos lineas. Los detalles van en el texto del reporte, no dentro de la caja.
- Una conexion que vuelve atras (un ciclo) se dibuja por fuera, curvada. Si hay muchas, el proceso esta mal descrito o necesita otra forma.
- El diagrama va en una tarjeta `ancho-total` si tiene mas de tres pasos en horizontal.

```js modulo=diagramas
<script>
/* Modulo de diagramas con conectores para el motor de reportes. Se copia integro,
   despues del motor, solo en los reportes con algun grafico de tipo diagrama. */
(function(){
"use strict";
var R = Reportes, svg = R.svg, r1 = R.r1, CAR = 6.7, LINEA = 15;
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
function marcarCiclos(nodos, conexiones, porId) {
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
  function colocar(n) {
    if (!hijos[n.id].length) { n.x = cursor + n.w / 2; cursor += n.w + sep; return; }
    hijos[n.id].forEach(colocar);
    var a = hijos[n.id][0], b = hijos[n.id][hijos[n.id].length - 1];
    n.x = (a.x + b.x) / 2;
  }
  nodos.filter(function (n) { return !padre[n.id]; }).forEach(function (raiz) { profundidad(raiz, 0); colocar(raiz); cursor += sep; });
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
  marcarCiclos(nodos, conexiones, porId);
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
  var x0 = Math.min.apply(null, nodos.map(function (n) { return n.x - n.w / 2; })) - 18;
  var y0 = Math.min.apply(null, nodos.map(function (n) { return n.y - n.h / 2; })) - 18;
  var x1 = Math.max.apply(null, nodos.map(function (n) { return n.x + n.w / 2; })) + 18;
  var y1 = Math.max.apply(null, nodos.map(function (n) { return n.y + n.h / 2; })) + 18;
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
    svg("text", {"class": "texto-nodo", x: 10, y: fr[0] + fr[1] / 2 + 4}, s, R.recortar(nombre, 14));
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
      svg("text", {"class": "texto-conexion", x: r1(m.x), y: r1(m.y + 4), "text-anchor": "middle"}, s, c.texto);
    }
  });
  nodos.forEach(function (n, i) {
    var c = n.grupo === undefined ? "var(--acento)" : R.color(n.grupo, 0), grupo = svg("g", {}, s), x = r1(n.x - n.w / 2), y = r1(n.y - n.h / 2);
    var comun = {fill: c, "fill-opacity": ".12", stroke: c, "stroke-width": 1.6};
    if (n.forma === "decision") svg("polygon", Object.assign({points: [n.x + "," + y, (x + n.w) + "," + n.y, n.x + "," + (y + n.h), x + "," + n.y].join(" ")}, comun), grupo);
    else svg("rect", Object.assign({x: x, y: y, width: n.w, height: n.h, rx: n.forma === "inicio" ? n.h / 2 : n.forma === "nota" ? 3 : 8,
      "stroke-dasharray": n.forma === "nota" ? "4 3" : null}, comun), grupo);
    var t = svg("text", {"class": "texto-nodo", x: n.x, y: r1(n.y - (n.lineas.length - 1) * LINEA / 2 + 4), "text-anchor": "middle"}, grupo);
    n.lineas.forEach(function (l, k) { svg("tspan", {x: n.x, dy: k ? LINEA : 0}, t, l); });
    R.consejo(grupo, n.texto);
  });
  if (g.grupos) R.leyenda(fig, Object.keys(g.grupos).map(function (k) { return {color: R.color(isNaN(k) ? k : +k, 0), texto: g.grupos[k]}; }));
  return {cabecera: [R.T.desde, R.T.hacia, R.T.rotulo], filas: conexiones.map(function (c) { return [porId[c.de].texto, porId[c.a].texto, c.texto || "—"]; })};
};
})();
</script>
```
