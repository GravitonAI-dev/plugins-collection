# Ejemplos de la skill `reportes`

Artefactos de demostración generados con la base `../assets/template-base-reportes.md` y las maquetas de `../references/maquetas-reportes.md`. Se abren **con doble clic** en cualquier navegador: no necesitan servidor, ni conexión, ni instalar nada. El botón inferior de cada página la imprime o la guarda como PDF; al lado de cada `.html` está ese PDF ya generado.

> DRAFT — Los datos son ficticios y sirven únicamente para mostrar el formato. Ningún importe, plazo o conclusión de estos archivos es real.

| Archivo | Maqueta | Qué demuestra |
| :--- | :--- | :--- |
| `panel_reclamacion_cantidad.html` | `panel_datos` | Panel con indicadores, minigráfico de tendencia, barras comparativas, anillo de reparto, evolución con área y umbral, cascada de importes, medidor de plazo y tabla con totales |
| `informe_viabilidad_monitorio.html` | `informe_visual` (tema sobrio) | Informe de lectura con índice lateral, indicadores, secciones numeradas, tabla comparativa, diagrama de plazos, cronología de hitos, avisos y firmas |
| `simulador_intereses_demora.html` | `herramienta_interactiva` | Herramienta que recalcula al instante, con medidor, desglose y lista de verificación con progreso |
| `presentacion_reclamacion_cliente.html` | `presentacion` + módulo de diagramas | 13 diapositivas para una reunión de cliente: portada, agenda, cifra enlazada a un gráfico, cascada, barras, separador, diagrama de flujo, comparativa, cronología, cita, próximos pasos, equipo y cierre; notas del orador y fuentes automáticas |
| `white_paper_morosidad_pymes.html` | `documento_largo` (tema editorial + bloque marca) + módulo de diagramas | White paper de siete paginas: portada, resumen ejecutivo con cifra enlazada, índice con enlaces, capítulos en página nueva con línea, barras, diagrama y matriz, notas y fuentes; cabecera y numeración al imprimir |
| `resumen_reclamacion_una_pagina.html` | `resumen_ejecutivo` (tema corporativo) | Una sola página A4: titular con la recomendación, tres indicadores (uno calculado), un gráfico, conclusiones y la decisión que se pide |
| `cuadro_mando_comite.html` | `cuadro_mando` (tema dorado) | Ocho KPIs con variación, objetivos en anillos, horas en bala, estado por área y tabla compacta |
| `ficha_deudor_una_pagina.html` | `ficha_una_pagina` (tema minimal) | Datos clave del deudor, tres indicadores (uno calculado), barras y semáforos; una página A4 |
| `infografia_morosidad.html` | `infografia` (tema menta) | Tres cifras enormes, pictograma, anillos y línea de tiempo en vertical |
| `comparativa_vias.html` | `comparativa` (tema corporativo) | Tres vías frente a frente con veredicto, radar y halteras de coste |
| `cronograma_expediente_0417.html` | `cronograma_expediente` (tema esmeralda nocturno) | Línea de tiempo, plazos con la marca de hoy, avance por fase y próximos pasos |
| `lista_control_rgpd.html` | `lista_control` (tema técnico) | Cumplimiento calculado, avance por bloque, semáforos y tabla de evidencias |
| `mapa_riesgos_operacion.html` | `mapa_riesgos` (tema ámbar) | Matriz, medidas en semáforos, tornado de impacto y rango de exposición |
| `escenarios_indemnizacion.html` | `escenarios` (tema oliva y oro) | Supuestos, resultado por escenario, tornado de sensibilidad y horquilla |
| `embudo_captacion.html` | `embudo_conversion` (tema lima) | Embudo, área apilada y sankey, con la conversión calculada |
| `actividad_equipo_t3.html` | `actividad_equipo` (tema pizarra) | Mapa de calor, calendario, cajas y bala de horas |
| `informe_territorial_asuntos.html` | `informe_territorial` (tema lavanda) | Mapa por comunidades con tasas, ranking y pareto |
| `poster_morosidad.html` | `poster` (tema nocturno) | Tres cifras y un gráfico grande; imprime en A3 apaisado |
| `galeria_maquetas.html` | índice | Las 18 maquetas con su miniatura (carpeta `miniaturas/`), filtro por familia y enlaces al HTML y al PDF |
| `galeria_catalogo.html` | índice | Catálogo visual de la skill: los 21 estilos y los 44 gráficos con su caso de uso. Incluye los 18 formatos con su miniatura. Con `?solo=formatos`, `?solo=temas` o `?solo=grupo-N` deja un solo bloque en modo compacto (iconos pequeños, 760 px, fondo transparente; los formatos llevan su "para que" debajo del nombre); así se generan las imágenes de `catalogo/`, que la descripción de la skill enlaza desde GitHub (rama `develop`) porque la ficha de la app solo pinta imágenes por URL y a su tamaño natural |
| `galeria_graficos.html` | base sin maqueta + todos los módulos | Los 43 tipos (con el mapa de España por comunidades y por provincias): los del motor, las cuatro disposiciones de diagrama, los gráficos avanzados, analíticos y de seguimiento, el QR, iconos y un vencimiento en días hábiles, cada uno con su tabla de datos, su CSV y su fuente |
| `galeria_temas.html` | `panel_datos` con un selector de tema y modo | El mismo panel con cada tema de `../references/temas-visuales.md`, en el modo del sistema, claro u oscuro, cambiando con los botones (o con `?tema=prensa&modo=oscuro` en la URL). Los botones solo cambian `data-tema` y `data-modo`, como en cualquier artefacto. `galeria_temas.png` es la hoja de contacto de los 42 estados |

El informe conserva a propósito el marcador `{{LETRADO_RESPONSABLE}}`: así se ve como queda un dato que el usuario decide no aportar.

## Regenerar

```bash
python3 generar_ejemplos.py            # HTML y PDF (necesita Google Chrome para el PDF)
python3 generar_ejemplos.py --sin-pdf  # HTML y comprobacion en Chrome, sin PDF
```

Además saca las miniaturas del cuestionario, `../assets/vista-<id>.png`: una por opción de las preguntas `identidad_visual` (los 21 estilos) y `colores_reporte` (modo del sistema, claro, oscuro y colores del despacho) de SKILL.md, a 480 × 300, con la primera pantalla del panel de ejemplo. La app las ensena como galería; avisa si las opciones de SKILL.md y las miniaturas no coinciden.

El guion compone cada ejemplo igual que lo hará el modelo: copia la base, inserta la maqueta leída de la referencia y escribe el bloque de datos. Después abre cada archivo en Chrome sin ventana y **falla** si la consola registra algún error (un gráfico mal declarado, una fuente sin declarar) o si queda algún marcador sin resolver. Si se cambia la base o una maqueta, basta con volver a ejecutarlo para que los ejemplos y sus PDF queden al día.

```bash
python3 probar_diseno.py               # diseno editable de todos los ejemplos
```

`probar_diseno.py` prueba en Chrome sin ventana lo que hace la app con un reporte abierto (`window.Reportes`): los 21 temas en modo claro, oscuro y del sistema, los colores del despacho puestos y quitados, cada gráfico cambiado por cada una de sus alternativas y `restaurar()`, con el sistema en claro y en oscuro. También guarda cada ejemplo como lo guarda el visor (el DOM serializado, tras una vista previa con otro tema, modo y marca), lo reabre y comprueba que no se duplica nada de lo que añaden el motor, los módulos o la maqueta. Después comprueba que el papel sale igual con cualquier modo. Falla si algo no cuadra.

## Contornos del mapa

`generar_mapa.py` produce los contornos simplificados de los bloques `mapa_ccaa` y `mapa_provincias` a partir de Natural Earth (`ne_10m_admin_1_states_provinces`, dominio público): agrupa las provincias en comunidades, proyecta, simplifica, coloca Canarias en recuadro y deja Ceuta y Melilla como puntos. Necesita `pyshp` y `shapely` y el shapefile descargado de naturalearthdata.com en la misma carpeta. Solo hace falta si se quieren regenerar.
