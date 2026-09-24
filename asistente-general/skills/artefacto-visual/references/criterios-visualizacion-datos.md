# Criterios de visualizacion y de composicion

El valor de un artefacto no esta en que tenga graficos, sino en que cada elemento responda a una pregunta que el lector se hace. Este documento fija que forma corresponde a cada pregunta y que esta prohibido hacer.

## 1. Eleccion de la forma segun la pregunta

| Pregunta del lector | Forma correcta | Forma incorrecta |
| :--- | :--- | :--- |
| Cuanto suma en total, cual es la cifra clave | Indicador grande, con su unidad y su fecha | Grafico de un solo dato |
| Cual es mayor entre varias partidas | Barras horizontales ordenadas de mayor a menor | Anillo con muchas porciones |
| Como evoluciona a lo largo del tiempo | Linea con area, eje desde cero | Barras verticales para muchos periodos |
| Como evoluciona frente a un limite legal o pactado | Linea con banda de umbral | Linea suelta y el limite explicado en el pie |
| Que tendencia lleva un indicador, sin ocupar sitio | Minigrafico de tendencia en la propia tarjeta | Un grafico entero para una sola serie corta |
| Que peso tiene cada parte sobre el total | Anillo de tres o cuatro porciones, o barra apilada unica | Anillo con siete porciones |
| Como se compone cada periodo | Barras apiladas | Varias lineas superpuestas |
| Que proporcion representa cada parte, comparando periodos | Barras apiladas al cien por cien | Apiladas al cien por cien cuando importa el volumen |
| Como se llega desde el principal hasta el total | Cascada de importes | Tabla de sumas sin representacion |
| Cuanto plazo se ha consumido, cuanto avance hay | Medidor semicircular | Barra de progreso sin escala ni fecha |
| Que contingencias hay y cuales urgen | Matriz de riesgo e impacto | Lista de riesgos sin priorizar |
| Cuando ocurre cada cosa y que plazo corre | Cronologia de hitos o diagrama de plazos con marca de hoy | Tabla de fechas sin orden |
| Que opcion conviene entre varias vias | Tabla comparativa con distintivos | Texto corrido enumerando ventajas |
| Que pasa si cambio un parametro | Herramienta interactiva con campos y recalculo | Tres tablas con escenarios fijos |
| Que tengo que reunir o comprobar | Lista de verificacion con progreso | Parrafo con incisos |

Si la respuesta a la pregunta cabe en una frase, se escribe la frase. Un grafico que ilustra un unico numero resta, no suma.

## 2. Honestidad grafica (innegociable)

1. El eje de magnitudes **empieza en cero**. Recortar la base exagera diferencias y falsea la lectura.
2. La escala es lineal y uniforme; no se mezclan unidades ni periodos de distinta duracion en el mismo eje.
3. Ningun dato se redondea hacia el lado que favorece la tesis del documento. Los importes se muestran con dos decimales y los porcentajes con uno.
4. Si una serie esta incompleta o procede de una estimacion, se dice en el subtitulo del grafico, no en una nota al pie invisible.
5. Nunca se inventa un punto para "cerrar" una serie. Un hueco se representa interrumpiendo la linea.
6. Toda cifra que provenga de un calculo propio se acompana de la formula o del supuesto empleado, en el bloque de supuestos.

## 2 bis. Errores propios de cada forma

| Forma | Error a evitar |
| :--- | :--- |
| Barras verticales | Mas de ocho categorias: las etiquetas dejan de leerse. Pasar a horizontales |
| Apiladas al cien por cien | Usarlas cuando importa el volumen absoluto: una columna de 200 euros y otra de 200.000 se ven identicas |
| Linea con area | Rellenar el area de dos series a la vez: se tapan. La segunda serie va con trazo discontinuo y sin area |
| Banda de umbral | Dibujarla despues de las series, tapandolas, o no explicar en la leyenda que representa |
| Minigrafico de tendencia | Ponerle cifras o pretender que se lea una magnitud: solo muestra forma |
| Medidor semicircular | Usarlo para un valor que no es un porcentaje de algo, o sin indicar el maximo |
| Cascada | Mezclar conceptos que no suman al total, u olvidar que un saldo negativo baja la columna |
| Matriz de riesgo | Mas de cuatro niveles por eje, o celdas sin decir que hacer |
| Diagrama de plazos | Barra sin fecha de vencimiento en el rotulo: no permite calcular |
| Anillo | Mas de cuatro porciones, o rotar el grupo con CSS en lugar del atributo transform |

## 3. Color

- La serie categorica (`--c1` a `--c6`) se recorre en orden. No se reasignan colores entre graficos del mismo artefacto: si en el primero la parte actora es `--c1`, lo sigue siendo en todos.
- El semaforo (`--ok`, `--warn`, `--risk`) queda reservado a estados y riesgos. No se usa para distinguir categorias neutras.
- Maximo seis colores simultaneos. A partir de ahi se agrupa en una categoria "otros".
- El color nunca porta la informacion en solitario: siempre hay etiqueta, cifra o distintivo textual.
- Las paletas se comprueban en tema claro **y** en oscuro antes de dar el artefacto por bueno.

## 4. Jerarquia y composicion

- Una sola idea principal por artefacto, enunciada en el titulo y sostenida por la entradilla.
- Orden descendente de importancia: indicadores primero, despues el grafico que sostiene la tesis, luego el detalle tabular y por ultimo los supuestos y advertencias.
- Entre cuatro y siete bloques de contenido. Un artefacto que exige desplazarse cinco pantallas es un informe; conviene dividirlo.
- Cada grafico lleva titulo que afirma algo, no una etiqueta generica: "La deuda se concentra en dos facturas" informa; "Grafico de importes" no.
- Espacio en blanco generoso: es lo que separa un documento profesional de una hoja saturada.

## 5. Texto dentro del artefacto

- Frases cortas, voz activa, sin jerga procesal innecesaria cuando el destinatario es el cliente.
- Cifras en formato espanol: miles con punto, decimales con coma, moneda con el simbolo o el codigo detras del importe.
- Fechas completas en el cuerpo (12 de marzo de 2026) y abreviadas en tablas y ejes (12/03/2026).
- Las citas normativas se escriben completas la primera vez y verificadas en su version consolidada vigente; nunca de memoria.

## 6. Control de calidad antes de entregar

1. El archivo abre en el navegador sin errores en la consola.
2. No queda ningun `{{MARCADOR}}` salvo los que corresponden a datos que el usuario ha decidido expresamente no aportar.
3. Se lee bien en tema claro y en tema oscuro.
4. Se lee bien en una ventana estrecha: nada desborda en horizontal.
5. La vista previa de impresion cabe en pagina, sin botones y sin fondos oscuros.
6. Todas las cifras del texto coinciden con las de los graficos y las tablas.
7. Cada grafico tiene alternativa textual accesible.
8. El aviso DRAFT y el pie con fuentes estan presentes.
9. La animacion de entrada no se dispara para quien ha pedido movimiento reducido, y desaparece al imprimir.
10. El nombre del archivo, los rotulos, las leyendas y las unidades estan en el idioma del usuario.
