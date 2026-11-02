# Criterios de visualización y de composición

Cada elemento responde a una pregunta del lector. Si la respuesta cabe en una frase, se escribe la frase.

## 1. Elección de la forma según la pregunta

| Pregunta del lector | Forma (id del catálogo) |
| :--- | :--- |
| Cuál es la cifra clave | Indicador grande con unidad y fecha; con variación, `signo` en la cifra |
| Cuál es mayor entre partidas | `barras`; si son muchas, `treemap`; si pocas concentran casi todo, `pareto` |
| Cómo evoluciona, frente a qué límite | `linea` (con `umbral`); tendencia en tarjeta, `chispa` |
| Cómo se compone cada periodo o el total en el tiempo | `apiladas`; `area_apilada` |
| Valor que rige a tramos (interés, SMI) | `escalones` |
| Qué peso tiene cada parte | `anillo` (3-4), `tarta` (≤ 6); 3 de cada 10, `pictograma` |
| Cómo se llega al total | `cascada` |
| Plazo o avance consumido | `medidor`; por fases, `progreso`; ≤ 4 objetivos, `anillos` |
| Cuánto falta para cada objetivo | `bala` |
| Qué suma y qué resta | `divergentes` |
| Cambio entre dos momentos; distancia entre dos valores | `pendiente`; `halteras` |
| Dos grupos por tramos | `piramide` |
| Perfil en varios criterios; nota en escala corta | `radar`; `puntuacion` |
| Relación entre dos magnitudes | `dispersion` |
| Reparto de muchos valores; distribución por grupo | `histograma`; `cajas` |
| Qué parámetro mueve más el resultado | `tornado`; para probar, herramienta interactiva |
| Dónde cae una cifra en una horquilla | `rango` |
| Concentración en dos dimensiones; en el territorio | `mapa_calor`; `mapa` (tasas si las zonas difieren) |
| De dónde a dónde fluye; cuántos llegan a cada etapa | `sankey`; `embudo` |
| Qué contingencias urgen | `matriz` |
| Qué plazo corre; qué ocurrió y cuándo; qué días | `plazos`; `linea_tiempo`; `calendario` |
| Estado de cada punto de control | `semaforos`; lista de verificación si el usuario marca |
| Pasos, decisiones, organigrama, relaciones, quién hace qué | `diagrama` (`capas`, `arbol`, `radial`, `carriles`) |
| Qué opción conviene | Tabla comparativa con distintivos |

## 2. Honestidad gráfica

1. El eje de magnitudes empieza en cero; escala lineal y uniforme, sin mezclar unidades ni periodos distintos.
2. Nada se redondea hacia la tesis: importes con dos decimales, porcentajes con uno.
3. Serie incompleta o estimada: se dice en el subtítulo del gráfico. Un hueco es `null`, nunca un punto inventado.
4. Toda cifra calculada se declara en `cifras` y su fórmula va en el bloque de supuestos.

## 3. Errores a evitar

- `columnas` con más de ocho categorías (pasar a `barras`); `apiladas` al 100 % cuando importa el volumen.
- `linea` con área en dos series (se tapan); `umbral` sin explicar en la leyenda.
- `chispa` con cifras; `medidor` para algo que no es porcentaje de un máximo.
- `cascada` con conceptos que no suman; `matriz` con más de cuatro niveles o zonas sin acción.
- `anillo`/`tarta` para comparar partidas o con porciones casi iguales; `pareto` desordenado.
- `escalones` para valores continuos; `cajas` con menos de cinco valores; `tornado` con extremos arbitrarios.
- `sankey` con ciclos o más de 16 nodos; `mapa_calor` con más de doce columnas; `anillos` con más de cuatro.
- `diagrama` con más de 24 nodos o textos largos en las cajas; `linea_tiempo` para duraciones (eso es `plazos`).
- `semaforos` sin nota; `progreso` recortado sin el valor real en la tabla.
- Cualquiera: coordenadas, porcentajes o totales a mano; texto y gráfico acaban contradiciéndose.

## 4. Color y composición

- La serie `1`-`6` se recorre en orden y cada parte conserva su color en todo el artefacto; `ok`/`aviso`/`riesgo` solo para estados. Máximo seis colores; el color nunca informa solo. Tema monocromo (minimal, prensa): no más de tres series.
- Una idea principal por artefacto, en el título. Orden: indicadores, el gráfico que sostiene la tesis, detalle tabular, supuestos y avisos. Entre cuatro y siete bloques.
- Cada gráfico lleva un título que afirma algo («La deuda se concentra en dos facturas»), no una etiqueta.
- Frases cortas, cifras en formato español, fechas completas en el cuerpo y abreviadas en tablas y ejes; citas normativas verificadas, nunca de memoria.

## 5. Control de calidad antes de entregar

1. Abre sin errores de consola y ningún gráfico muestra el recuadro rojo.
2. Ningún `{{MARCADOR}}` salvo datos que el usuario decidió no dar; ninguna serie vacía por un dato que se pidió buscar (va la estimación marcada).
3. Las cifras del texto salen de `data-cifra` y coinciden con gráficos y tablas.
4. Se lee en claro, en oscuro y en ventana estrecha; la impresión cabe en página, sin botones, fondos oscuros, tablas cortadas ni páginas medio vacías.
5. Cada gráfico tiene `resumen`; rótulos, leyendas y unidades en el idioma del usuario.
6. Aviso DRAFT y pie con fuentes (fuente, URL y fecha en todo dato buscado; origen marcado si conviven datos del usuario y de internet).
7. La animación de entrada respeta el movimiento reducido y desaparece al imprimir.
