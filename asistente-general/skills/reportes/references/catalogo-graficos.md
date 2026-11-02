# Catálogo de gráficos: contrato de declaración

Un gráfico se declara dos veces con el mismo nombre: el hueco `<figure class="grafico" data-grafico="evolucion"></figure>` (minigráfico de indicador: `<div class="tendencia" data-grafico="…">`) y los datos en `graficos.evolucion` del bloque `<script type="application/json" id="datos-reporte">`. Los 44 tipos van dentro de la base: no se copia ni se añade código.
- El motor dibuja, calcula escalas, totales y porcentajes y añade tabla de datos (`"tabla": false` la quita), descripción accesible y fuente. **Nunca se escriben coordenadas, porcentajes ni totales a mano.**
- Comunes: `tipo`, `resumen` (frase para lector de pantalla), `fuente` (clave o lista de `fuentes`; en series, `series[].fuente`), `unidad` (`eur`, `pct`, `num`, `entero` o un texto), `color` en elementos, series o porciones (`1`-`6`, `ok`, `aviso`, `riesgo`).
- `fuentes`: `{"clave": {"nombre", "url", "consulta": "AAAA-MM-DD"}}`. `cifras`: `{"valor", "unidad"}`, una operación `{"operacion": "suma|diferencia|producto|cociente|porcentaje", "a", "b", "unidad"}` o un cálculo sobre un gráfico `{"de": "grafico", "calculo": "suma|media|maximo|minimo|primero|ultimo|cuenta|variacion|porcentaje|diferencia", "serie": 0, "elemento": "rotulo", "unidad"}`; opc. `decimales`, `signo` (flecha y color), `mejor` (`bajar`/`neutro`). En el HTML, `<span data-cifra="clave"></span>`; en diapositivas, `{cifra:clave}`. Cualquier valor numérico puede ser `"@clave"`. Un dato ausente es `null`, nunca un cero.

## Comparar magnitudes

**barras** — ¿Cuál es mayor entre varias partidas? `elementos: [{rotulo, valor}]`, `unidad`; opc. `orden: "original"`, `nombre_valor`. Ej.: `{"tipo": "barras", "unidad": "eur", "elementos": [{"rotulo": "Factura 118", "valor": 18400}]}`
**columnas** — ¿Cómo comparan hasta ocho periodos, con una o varias series? `etiquetas`, `series: [{nombre, valores}]`, `unidad`; `"valores": false` quita las cifras.
**apiladas** — ¿Cómo se compone cada periodo? Como `columnas`; `"cien": true` normaliza al 100 % (solo si importa la proporción). Sin negativos.
**pareto** — ¿Qué pocas partidas concentran casi todo? `elementos: [{rotulo, valor}]`, `unidad`; opc. `umbral` (80). El motor ordena y acumula.
**bala** — ¿Cuánto falta para cada objetivo? `elementos: [{rotulo, valor, objetivo, tramos: [malo, medio, bueno]}]`, `unidad`.
**halteras** — ¿Qué distancia hay entre dos valores de cada partida? `nombres: {a, b}`, `elementos: [{rotulo, a, b}]`, `unidad`; opc. `color_a`, `color_b`.
**pendiente** — ¿Cómo cambia cada partida entre dos momentos? `etiquetas: ["antes", "después"]`, `elementos: [{rotulo, antes, despues}]`, `unidad`.
**divergentes** — ¿Qué partidas suman y cuáles restan? `elementos: [{rotulo, valor}]` con signo, `unidad`; opc. `nombres: {positivo, negativo}`, `colores: {positivo, negativo}` si el signo no es bueno ni malo.
**tornado** — ¿Qué parámetro mueve más el resultado? `base`, `elementos: [{rotulo, bajo, alto}]`, `nombres: {bajo, alto}`, `unidad`; opc. `color_bajo`, `color_alto`.
**piramide** — ¿Cómo comparan dos grupos por tramos? `etiquetas`, `izquierda: {nombre, valores}`, `derecha: {nombre, valores}`, `unidad`.
**radar** — ¿Qué perfil tiene cada opción en 3-8 criterios? `ejes`, `series: [{nombre, valores}]`, `maximo` (misma escala para todas).
**puntuacion** — ¿Qué nota tiene cada criterio en una escala corta? `elementos: [{rotulo, valor}]`, `maximo` (5; hasta 10).

## Evolución

**linea** — ¿Cómo evoluciona, frente a qué límite? `etiquetas`, `series: [{nombre, valores, fuente, destacar}]`, `unidad`; opc. `umbral: {desde, hasta, rotulo, color}`, `anotaciones: [{indice, texto}]`, `destacar: ["maximo", "minimo", "primero", "ultimo"]`, `"area": false`. Eje desde cero, sin negativos. Ej.: `{"tipo": "linea", "unidad": "eur", "etiquetas": ["Ene", "Feb"], "series": [{"nombre": "Principal", "valores": [12400, 21800]}]}`
**area_apilada** — ¿Cómo se compone el total a lo largo del tiempo? `etiquetas`, `series: [{nombre, valores}]`, `unidad`. Sin negativos.
**escalones** — ¿Cómo cambia un valor que rige a tramos (tipo de interés, SMI)? Como `area_apilada`; cada valor rige hasta la etiqueta siguiente.
**chispa** — ¿Qué tendencia lleva un indicador? Solo forma, sin ejes. `valores`; opc. `etiquetas: ["primero", "último"]` (el motor escribe la variación), `nota`.
**calendario** — ¿Qué días concentran la actividad o los vencimientos? `dias: {"AAAA-MM-DD": numero}`, `desde`, `hasta`; opc. `color`.
**linea_tiempo** — ¿Qué ocurrió y cuándo, sobre una escala real? `hitos: [{fecha, rotulo, estado}]`; opc. `hoy` (los anteriores van en gris). No representa duraciones (eso es `plazos`).
**plazos** — ¿Qué plazos corren y cuánto queda? `hoy`, `plazos: [{rotulo, inicio, fin, aproximada}]` en `AAAA-MM-DD`; sin `fin` = en curso; `"fin": "@clave"` admite un vencimiento calculado.

## Reparto

**anillo** / **tarta** — ¿Qué peso tiene cada parte sobre el total? Máximo seis porciones (el motor agrupa en «Otros»). `porciones: [{rotulo, valor}]`, `unidad`; en anillo, opc. `centro: {rotulo, cifra}`. Ej.: `{"tipo": "anillo", "unidad": "eur", "porciones": [{"rotulo": "Principal", "valor": 12000}], "centro": {"rotulo": "total"}}`
**treemap** — ¿Qué peso tiene cada partida cuando son muchas? `elementos: [{rotulo, valor}]`, `unidad`.
**cascada** — ¿Cómo se llega desde el principal al total? `pasos: [{rotulo, valor}]` (negativo baja), `total: {rotulo}` (lo calcula el motor), `unidad`.
**embudo** — ¿Cuántos llegan a cada etapa? `etapas: [{rotulo, valor}]`, `unidad`; el motor calcula el paso entre etapas.
**sankey** — ¿De dónde a dónde fluye el importe o el volumen? `nodos: [{id, texto}]`, `flujos: [{de, a, valor}]`, `unidad`; hasta 16 nodos, sin ciclos.
**pictograma** — Una proporción contada en figuras («3 de cada 10»). `valor`, `total` (hasta 10 por fila), `rotulo`.

## Relación y distribución

**dispersion** — ¿Hay relación entre dos magnitudes (y una tercera como tamaño)? `puntos: [{rotulo, x, y, tamano}]`, `eje_x: {nombre, unidad}`, `eje_y: {nombre, unidad}`; opc. `nombre_tamano`, `unidad_tamano`.
**histograma** — ¿Cómo se reparten muchos valores sueltos? `valores` en bruto (al menos cinco), `unidad`; opc. `tramos`, `desde`, `hasta`, `nombre`.
**cajas** — ¿Cómo se distribuyen los valores en cada grupo? `grupos: [{rotulo, valores}]` (al menos cinco por grupo), `unidad`. El motor calcula cuartiles, mediana y atípicos.
**rango** — ¿Dónde cae una cifra dentro de una horquilla (sanción, oferta frente a tasación)? `minimo`, `maximo`, `marcas: [{rotulo, valor}]`, `unidad`; opc. `tramos: [{hasta, rotulo, color}]` (el último sin `hasta`).
**mapa_calor** — ¿Dónde se concentra algo en dos dimensiones (juzgado por mes)? `filas`, `columnas`, `valores` (una lista por fila, `null` vacía), `unidad`.
**matriz** — ¿Qué contingencias hay y cuáles urgen? `filas` (grave primero), `columnas` (grave al final), `eje_filas`, `eje_columnas`, `elementos: [{nombre, fila, columna}]`, `zonas: {ok, aviso, riesgo}`. De dos a cuatro niveles por eje.

## Seguimiento y estado

**medidor** — ¿Cuánto plazo o avance se ha consumido sobre un máximo conocido? `valor`, `maximo`, `rotulo`; opc. `unidad` (la cifra pasa a ser el valor), `cifra` (texto central), `tramos: [ok_hasta, aviso_hasta]`.
**progreso** — ¿Cuánto se ha avanzado en cada fase o cobrado de cada partida? `elementos: [{rotulo, valor, maximo, objetivo}]` (`maximo` 100), `unidad`; opc. `tramos: [60, 85]`.
**anillos** — ¿Qué grado de avance tienen hasta cuatro objetivos? `elementos: [{rotulo, valor, maximo}]` (`maximo` 100).
**semaforos** — ¿En qué estado está cada punto de un control? `elementos: [{rotulo, estado, nota}]` con `estado` en `ok`, `aviso`, `riesgo`, `pendiente`; opc. `nombres` para los rótulos de estado.

## Diagramas y mapa

**diagrama** — ¿Qué pasos sigue un proceso, quién depende de quién, quién hace qué? El modelo no coloca nada. `disposicion` (`capas`, `arbol`, `radial`, `carriles`), `nodos: [{id, texto, forma, grupo, carril}]` (`forma`: `caja`, `inicio`, `decision`, `nota`), `conexiones: [{de, a, texto, estilo}]` (`estilo`: `discontinua`, `destacada`); opc. `direccion` (`horizontal`/`vertical`), `grupos: {"1": "nombre"}`, `centro` (radial), `carriles` (orden). Máximo 24 nodos; solo pasos que constan. Ej.: `{"tipo": "diagrama", "nodos": [{"id": "pago", "texto": "¿Paga?", "forma": "decision"}, {"id": "fin", "texto": "Archivo"}], "conexiones": [{"de": "pago", "a": "fin", "texto": "sí"}]}`
**mapa** — ¿Dónde se concentra algo en España? `valores: {"ES-MD": 520, "Andalucía": 412}` (código ISO 3166-2 o nombre) o `tasa: {numerador, denominador, por}` para zonas de tamaño distinto; `nivel` (`ccaa`/`provincias`), `unidad`; opc. `destacar: [zona]`, `nombre_valor`. Solo valores no negativos; nombre inexistente = error.

## Marca, iconos, QR, plazos, encaje

**marca** (bloque `marca` de los datos) — colores, logo y pie del despacho sobre cualquier tema. `acento` (hexadecimal, basta con este); opc. `nombre`, `acento_fuerte`, `serie: [6 hex]`, `oscuro: {acento, serie}`, `logo` (data URI < 15 KB, solo si lo aporta el usuario), `pie`.
**iconos** — `<span class="icono" data-icono="nombre"></span>` o `{icono:nombre}` en diapositiva. Nombres: `plazo`, `calendario`, `juzgado`, `balanza`, `contrato`, `firma`, `euro`, `alerta`, `ok`, `persona`, `grupo`, `empresa`, `correo`, `telefono`, `ubicacion`, `candado`.
**qr** — Lleva al lector en papel a una URL verificada en la sesión. `texto` (≤ 210 caracteres), `rotulo` (adónde lleva); opc. `tamano` (132).
**plazos en días hábiles** (en `cifras`) — `{"calculo": "dias_habiles", "desde", "hasta", "festivos": [...], "agosto_inhabil": true}` y `{"calculo": "vencimiento", "desde", "dias": 20, "festivos": [...], "unidad": "fecha"}`. Sin sábados ni domingos; `festivos` los aporta el usuario o se verifican en la sesión; resultado orientativo (va en los supuestos).
**encaje** — Las maquetas de una hoja fijan `:root{--encaje:<ancho> <alto>}` en sus estilos y el motor reduce la escala al imprimir si no cabe.
