# Criterios de visualización y de composición

El valor de un artefacto no está en que tenga gráficos, sino en que cada elemento responda a una pregunta que el lector se hace. Este documento fija qué forma corresponde a cada pregunta y que está prohibido hacer.

## 1. Elección de la forma según la pregunta

| Pregunta del lector | Forma correcta | Forma incorrecta |
| :--- | :--- | :--- |
| Cuánto suma en total, cuál es la cifra clave | Indicador grande, con su unidad y su fecha | Gráfico de un solo dato |
| Cuál es mayor entre varias partidas | Barras horizontales ordenadas de mayor a menor | Anillo con muchas porciones |
| Cómo evoluciona a lo largo del tiempo | Línea con área, eje desde cero | Barras verticales para muchos periodos |
| Cómo evoluciona frente a un límite legal o pactado | Línea con banda de umbral | Línea suelta y el límite explicado en el pie |
| Qué tendencia lleva un indicador, sin ocupar sitio | Minigráfico de tendencia en la propia tarjeta | Un gráfico entero para una sola serie corta |
| Qué peso tiene cada parte sobre el total | Anillo de tres o cuatro porciones; tarta hasta seis; barra apilada única | Tarta o anillo con siete porciones (el motor agrupa el resto en Otros) |
| Cómo se compone cada periodo | Barras apiladas | Varias líneas superpuestas |
| Qué proporción representa cada parte, comparando periodos | Barras apiladas al cien por cien | Apiladas al cien por cien cuando importa el volumen |
| Cómo se llega desde el principal hasta el total | Cascada de importes | Tabla de sumas sin representación |
| Cuánto plazo se ha consumido, cuánto avance hay | Medidor semicircular | Barra de progreso sin escala ni fecha |
| Qué contingencias hay y cuáles urgen | Matriz de riesgo e impacto | Lista de riesgos sin priorizar |
| Cuándo ocurre cada cosa y que plazo corre | Cronología de hitos o diagrama de plazos con marca de hoy | Tabla de fechas sin orden |
| Qué opción conviene entre varias vías | Tabla comparativa con distintivos | Texto corrido enumerando ventajas |
| Cuánto falta para cada objetivo | Bala: valor, objetivo y tramos de fondo | Varios medidores sueltos |
| Qué meses o partidas suman y cuáles restan | Barras divergentes alrededor de cero | Columnas con negativos sin eje en cero |
| Cómo ha cambiado una cifra frente al periodo anterior | Cifra con variación (`signo`) dentro del indicador | Dos cifras sueltas para que el lector reste |
| Qué pasos sigue un proceso y dónde se decide | Diagrama por capas con rombos de decisión | Lista numerada con «si..., entonces...» |
| Quién depende de quién (grupo societario, organigrama) | Diagrama en árbol | Tabla de participaciones sin estructura |
| Qué relación tiene cada parte con el caso | Diagrama radial | Párrafo con todos los nombres |
| Quién hace que en cada momento | Diagrama por carriles | Cronología sin responsables |
| Dónde se concentra algo en el territorio | Mapa por comunidades o provincias, con tasas si las poblaciones son muy distintas | Tabla de diecisiete filas o barras sin orden geográfico |
| Qué pasa si cambio un parámetro | Herramienta interactiva con campos y recálculo | Tres tablas con escenarios fijos |
| Qué tengo que reunir o comprobar | Lista de verificación con progreso | Párrafo con incisos |
| Cómo se compone el total a lo largo del tiempo | Área apilada | Varias líneas que se cruzan, o apiladas al cien por cien si importa el volumen |
| Qué pocas partidas concentran casi todo (deudores, causas) | Pareto: barras ordenadas con porcentaje acumulado | Tarta con doce porciones |
| Cómo ha cambiado un valor que rige a tramos (tipo de interés, salario mínimo) | Escalones | Línea que interpola entre dos tipos como si subiera poco a poco |
| Cómo se distribuyen muchos valores en cada grupo (días por juzgado) | Cajas (mediana, cuartiles y atípicos) | Media por grupo, que oculta la dispersión |
| Qué parámetro mueve más el resultado de una simulación | Tornado | Tres escenarios en tabla |
| Dónde cae una cifra dentro de una horquilla legal (sanción, oferta frente a tasación) | Rango con tramos y marcas | Cifra suelta sin decir el mínimo y el máximo |
| Dónde se concentra algo en dos dimensiones (juzgado por mes) | Mapa de calor | Tabla de cifras sin color ni orden |
| De dónde a dónde fluye el importe o el volumen | Sankey | Varios anillos encadenados |
| Qué grado de avance tienen dos, tres o cuatro objetivos | Anillos concéntricos | Cuatro medidores sueltos |
| Qué nota tiene cada criterio en una escala corta | Puntuación en puntos | Radar para una sola opción |
| Cuánto se ha avanzado en cada fase o cobrado de cada partida | Progreso con marca de objetivo | Porcentajes en texto corrido |
| En que estado está cada punto de un control o requisito | Semáforos con nota | Tabla con «si» y «no» sin matiz |
| Qué ocurrió y cuando, sobre una escala real de tiempo | Línea de tiempo con marca de hoy | Cronología de hitos cuando importa la distancia real entre fechas |

Si la respuesta a la pregunta cabe en una frase, se escribe la frase. Un gráfico que ilustra un único número resta, no suma.

## 2. Honestidad gráfica (innegociable)

1. El eje de magnitudes **empieza en cero**. Recortar la base exagera diferencias y falsea la lectura.
2. La escala es lineal y uniforme; no se mezclan unidades ni periodos de distinta duración en el mismo eje.
3. Ningún dato se redondea hacia el lado que favorece la tesis del documento. Los importes se muestran con dos decimales y los porcentajes con uno.
4. Si una serie está incompleta o procede de una estimación, se dice en el subtitulo del gráfico, no en una nota al pie invisible.
5. Nunca se inventa un punto para "cerrar" una serie. Un hueco se representa interrumpiendo la línea.
6. Toda cifra que provenga de un cálculo propio se acompaña de la fórmula o del supuesto empleado, en el bloque de supuestos.

## 2 bis. Errores propios de cada forma

| Forma | Error a evitar |
| :--- | :--- |
| Barras verticales | Más de ocho categorías: las etiquetas dejan de leerse. Pasar a horizontales |
| Apiladas al cien por cien | Usarlas cuando importa el volumen absoluto: una columna de 200 euros y otra de 200.000 se ven idénticas |
| Línea con área | Rellenar el área de dos series a la vez: se tapan. La segunda serie va con trazo discontinuo y sin área |
| Banda de umbral | Dibujarla después de las series, tapándolas, o no explicar en la leyenda que representa |
| Minigráfico de tendencia | Ponerle cifras o pretender que se lea una magnitud: solo muestra forma |
| Medidor semicircular | Usarlo para un valor que no es un porcentaje de algo, o sin indicar el máximo |
| Cascada | Mezclar conceptos que no suman al total, u olvidar que un saldo negativo baja la columna |
| Matriz de riesgo | Más de cuatro niveles por eje, o celdas sin decir qué hacer |
| Diagrama de plazos | Barra sin fecha de vencimiento en el rotulo: no permite calcular |
| Bala | Tramos de fondo que no son una valoración real (inventar «bueno» y «malo» sin criterio) |
| Divergentes | Colorear en verde y rojo un signo que no es bueno ni malo: usar `colores` |
| Diagrama | Más de 24 nodos, textos largos dentro de las cajas o flechas que se cruzan sin necesidad: dividir o cambiar la disposición |
| Anillo y tarta | Usarlos para comparar partidas entre si (para eso, barras) o con porciones casi iguales, que el ojo no distingue |
| Área apilada | Leer una serie intermedia por su borde superior: solo la de abajo y el total se leen directos; para comparar series, línea |
| Pareto | Cambiar el orden de mayor a menor, o fijar un umbral distinto del 80 por ciento sin decir por qué |
| Escalones | Usarlo para valores que cambian de forma continua: ahí va la línea |
| Cajas | Menos de cinco valores por grupo, o presentar la mediana como si fuera la media |
| Tornado | Elegir extremos arbitrarios para cada parámetro: los extremos son los que de verdad se barajan y se dicen en los supuestos |
| Rango | Marcas fuera de la horquilla sin explicar que se pegan al extremo; tramos sin criterio legal o pactado |
| Mapa de calor | Más de doce columnas, o celdas sin la cifra cuando caben |
| Sankey | Más de dieciséis nodos, flujos que no conservan el total o un ciclo |
| Anillos | Más de cuatro, o porcentajes de bases distintas sin decirlo en la leyenda |
| Puntuación | Escalas distintas entre criterios, o más de diez puntos |
| Progreso | Barras que superan el cien por cien recortadas sin que la tabla muestre el valor real |
| Semáforos | Estados sin nota que explique el aviso o el riesgo |
| Línea de tiempo | Usarla para plazos con duración: para eso, el diagrama de plazos |
| Cualquiera | Escribir a mano coordenadas, porcentajes o totales que el motor ya calcula: el gráfico y el texto acaban contradiciéndose |

## 3. Color

- La serie categórica (`--c1` a `--c6`) se recorre en orden. No se reasignan colores entre gráficos del mismo artefacto: si en el primero la parte actora es `--c1`, lo sigue siendo en todos.
- El semáforo (`--ok`, `--warn`, `--risk`) queda reservado a estados y riesgos. No se usa para distinguir categorías neutras.
- Máximo seis colores simultáneos. A partir de ahí se agrupa en una categoría "otros".
- El color nunca porta la información en solitario: siempre hay etiqueta, cifra o distintivo textual.
- Las paletas se comprueban en tema claro **y** en oscuro antes de dar el artefacto por bueno.
- El tema (`temas-visuales.md`) lo fija el destinatario y el soporte, una vez por artefacto; los gráficos no llevan colores propios fuera de la serie y el semáforo del tema. Con un tema de serie monocroma (minimal, prensa) no se representan más de tres series por gráfico.

## 4. Jerarquía y composición

- La maqueta la fija la pregunta del reporte (¿cómo va el mes?, ¿qué riesgo hay?, ¿qué pasa si?) y el tema, el destinatario. Un reporte es datos: si lo que hay que entregar es sobre todo texto, es un documento y se redacta en Markdown.
- Una sola idea principal por artefacto, enunciada en el título y sostenida por la entradilla.
- Orden descendente de importancia: indicadores primero, después el gráfico que sostiene la tesis, luego el detalle tabular y por último los supuestos y advertencias.
- Entre cuatro y siete bloques de contenido. Un artefacto que exige desplazarse cinco pantallas es un informe; conviene dividirlo.
- Cada gráfico lleva título que afirma algo, no una etiqueta genérica: "La deuda se concentra en dos facturas" informa; "Gráfico de importes" no.
- Espacio en blanco generoso: es lo que separa un documento profesional de una hoja saturada.

## 5. Texto dentro del artefacto

- Frases cortas, voz activa, sin jerga procesal innecesaria cuando el destinatario es el cliente.
- Cifras en formato español: miles con punto, decimales con coma, moneda con el símbolo o el código detrás del importe.
- Fechas completas en el cuerpo (12 de marzo de 2026) y abreviadas en tablas y ejes (12/03/2026).
- Las citas normativas se escriben completas la primera vez y verificadas en su versión consolidada vigente; nunca de memoria.

## 6. Control de calidad antes de entregar

1. El archivo abre en el navegador sin errores en la consola.
2. No queda ningún `{{MARCADOR}}` salvo los que corresponden a datos que el usuario ha decidido expresamente no aportar. Ningún gráfico ni indicador tiene su serie a cero, vacía o `null` por un dato que se pidió buscar: en ese caso lleva la estimación marcada del fallback de la Fase 2.1 de la skill.
3. Se lee bien en tema claro y en tema oscuro.
4. Se lee bien en una ventana estrecha: nada desborda en horizontal.
5. La vista previa de impresión cabe en página, sin botones y sin fondos oscuros.
6. Todas las cifras del texto coinciden con las de los gráficos y las tablas: las que salen de un gráfico se escriben con `data-cifra`, no a mano.
6 bis. Ningún gráfico muestra el recuadro rojo de error y la consola del navegador no registra errores.
7. Cada gráfico tiene alternativa textual accesible.
8. El aviso DRAFT y el pie con fuentes están presentes; todo dato buscado en internet lleva su cita (fuente, URL y fecha de consulta) y, si conviven datos del usuario y de internet, el origen de cada uno queda marcado.
8 bis. La vista de impresión no corta tablas anchas por el borde derecho, no duplica la fila de totales y no deja paginas medio vacías por tarjetas más altas que el A4 (reglas de `anatomia-artefacto.md`).
9. La animación de entrada no se dispara para quien ha pedido movimiento reducido, y desaparece al imprimir.
10. El nombre del archivo, los rótulos, las leyendas y las unidades están en el idioma del usuario.
