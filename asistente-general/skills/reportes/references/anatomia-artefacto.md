# Anatomia de un artefacto HTML autocontenido

Reglas tecnicas invariables del formato. Todo artefacto que produzca esta skill debe cumplirlas sin excepcion, porque el archivo se abre directamente en el navegador del usuario desde su espacio de trabajo (esquema `file://`), sin servidor ni conexion garantizada.

## 1. Un unico archivo, cero dependencias externas

- **Extension `.html`** y **un solo archivo**, construido copiando integra la base `assets/template-base-reportes.md` e insertando la maqueta del tipo de entregable (`maquetas-reportes.md`). Todo el CSS va en el unico `<style>` de la base. El JavaScript es el del motor de la base, que no se modifica; solo la herramienta interactiva anade un segundo `<script>` con su bloque de calculo, justo despues del motor.
- **Prohibido** cualquier recurso remoto: `<script src="https://...">`, `<link rel="stylesheet" href="https://...">`, fuentes de Google Fonts, imagenes por URL, `fetch`, `XMLHttpRequest`, `import` de modulos remotos, iframes a terceros. Bajo `file://` fallan en silencio o los bloquea el navegador y el artefacto se ve roto.
- **Prohibidas las librerias** (Chart.js, D3, Tailwind por CDN, React, jQuery). Los graficos los dibuja en SVG el motor propio que viaja dentro de la base, a partir del bloque de datos `datos-reporte` (contrato en `biblioteca-componentes-visuales.md`). Nunca se escriben coordenadas a mano.
- Si hace falta una imagen, se incrusta como SVG en linea o como `data:` URI, y solo si es imprescindible.
- **Fotografias:** se incrustan como `data:image/jpeg;base64,...` dentro de una `<figure>`, comprimidas antes a un ancho maximo de unos 520 px y calidad media (el objetivo es que la foto pese menos de 30 KB, porque cuenta para el limite de 170 KB del archivo). Toda foto lleva `alt` descriptivo y `<figcaption>` con su credito: autor, titulo, origen y licencia con URL. Solo se usan imagenes con licencia que permita el uso (dominio publico, CC0, CC BY, CC BY-SA) y nunca una foto sin fuente conocida.
- Tipografia: pilas de fuentes del sistema (la sans de la base; serif o monoespaciada en los temas editorial, institucional, prensa y tecnico). Nunca fuentes descargadas.

## 2. Cabecera obligatoria

```html
<!doctype html>
<html lang="es" data-tema="moderno">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="reportes-diseno" content="1">
<title>Titulo del artefacto</title>
```

El `lang` es el idioma de la conversacion. `data-tema` es el tema elegido y, si el usuario fijo el modo, va al lado `data-modo="claro"` u `"oscuro"`. La etiqueta `reportes-diseno` dice a la app que el diseno del reporte se puede cambiar desde el visor (seccion 7): no se quita. El `<title>` es un nombre corto y reconocible, no un resumen: es lo que se ve en la pestana del navegador.

## 3. Diseno, adaptabilidad e impresion: lo resuelve la base

La base ya trae el sistema de tokens (colores, espaciado, radios y sombras en `:root`, con su version oscura, y los 21 temas de `temas-visuales.md`, que se eligen con `data-tema` y `data-modo`), la escala tipografica, las dos animaciones permitidas (anuladas con movimiento reducido y al imprimir), la rejilla adaptable sin desbordamiento horizontal y el bloque `@media print` completo: A4, fidelidad de color, tablas compactadas, `thead` repetido, `tfoot` sin duplicar, sin cortes de tarjeta ni titulos huerfanos. **No se toca.** Lo que si depende de quien rellena el artefacto:

- **Colores siempre con tokens** (`var(--c1)`, `var(--riesgo)`), nunca literales. Para otro aspecto se elige un tema del catalogo (`temas-visuales.md`) con `data-tema`; para colores corporativos, el bloque `marca` de los datos. Nunca se redefinen tokens a mano ni se mezclan dos temas.
- **Nombres en espanol:** las clases e identificadores de la base y de las maquetas no se traducen ni se renombran. Lo que cambia de idioma es el texto visible.
- **Tarjetas mas altas que un A4:** se les da la clase `permite-corte` (la herramienta ya la usa en su tarjeta de resultados), que deja partir la tarjeta y protege sus bloques internos.
- **Texto dentro de un SVG:** solo cifras y rotulos cortos. Cualquier frase va en HTML junto al grafico, porque dentro del SVG se recorta sin aviso. El motor ya sigue esta regla.
- **Numeracion y cabeceras de pagina:** la base numera las paginas impresas («3 / 12») con las cajas de margen de `@page`, y el documento largo anade cabecera con el titulo corto. Funciona en Chrome y Edge actuales; otros navegadores imprimen igual, sin numero. Nunca con `position:fixed`, que Chrome coloca una sola vez y fuera de sitio.
- Un boton visible invoca `window.print()` (ya en la base). El nombre del PDF que propone el navegador sale del `<title>`, asi que ese titulo es tambien el nombre del archivo.

## 4. JavaScript permitido y prohibido

- Permitido: JavaScript nativo, envuelto en una funcion autoejecutada con `"use strict"`, que lee campos del formulario, calcula y actualiza el DOM.
- **Prohibido**: `alert()`, `confirm()` y `prompt()` (bloquean la ventana), `eval()`, `new Function()`, `document.write()`, temporizadores infinitos y cualquier llamada de red.
- **Prohibido inyectar texto con `innerHTML`** a partir de valores introducidos por el usuario: siempre `textContent` o `createElement`. Es la unica proteccion real frente a contenido malicioso pegado en un campo.
- El almacenamiento del navegador (`localStorage`, `sessionStorage`) falla o lanza excepcion bajo `file://` en varios navegadores. No se usa; si excepcionalmente se usara, siempre dentro de `try/catch` y con la pagina funcionando igual sin el.
- Los textos, indicadores escritos como texto y tablas van en el HTML y se leen aunque el JavaScript este desactivado. Los graficos y las cifras con `data-cifra` necesitan el motor: el aviso `noscript` de la base lo indica. Ningun dato debe existir solo dentro de un grafico: lo que importa se dice tambien en el texto o en una tabla.

## 5. Accesibilidad

- Estructura semantica: `main`, `header`, `section`, `footer`, jerarquia de encabezados sin saltos (`h1` unico, luego `h2`, `h3`).
- Todo grafico SVG lleva `role="img"` y un `aria-label` que resume el dato, o un `<title>` dentro del SVG. Un grafico sin texto alternativo es un grafico invisible.
- El color nunca es el unico portador de informacion: se acompana de etiqueta, cifra o icono textual.
- Contraste minimo 4.5:1 en texto normal, verificado en tema claro y oscuro.
- Estados de foco visibles: `:focus-visible { outline: 2px solid var(--acento); outline-offset: 2px }`.
- Todo `input` y `select` tiene su `<label for="...">`.

## 6. Nomenclatura y ubicacion

- Nombre de archivo descriptivo en `snake_case.html` (ej. `panel_reclamacion_cantidad.html`, `simulador_indemnizacion_despido.html`).
- Se crea en la raiz del espacio de trabajo de la conversacion, igual que cualquier otro documento.
- El idioma del nombre del archivo sigue al de la plantilla; el contenido visible sigue al idioma del usuario.

## 7. Edicion posterior

El artefacto se edita **siempre desde el chat**, pidiendo el cambio al asistente, que lo aplica sobre el archivo. Nunca se edita a mano en el editor de texto de la plataforma: ese editor trabaja en markdown y al guardar reescribiria la pagina, perdiendo estilos, graficos y comportamiento.

**Diseno editable desde el visor.** El estilo, el modo claro u oscuro, los colores del despacho y la forma de un grafico se cambian tambien sin la IA: el visor de la app (macOS y Windows) tiene los botones «Estilo» y «Colores del reporte» y, con el boton derecho sobre un grafico, «Cambiar gráfico». La app escribe solo `data-tema` y `data-modo` de la etiqueta `html` y las claves `marca` y `graficos.<id>.tipo` del bloque `datos-reporte`; las cifras no cambian. Para eso la base lleva el catalogo `catalogo-reporte` (los 21 temas y las familias de graficos que se pueden intercambiar porque leen los mismos datos) y el motor expone en `window.Reportes`:

| Llamada | Que hace |
| :--- | :--- |
| `catalogo` | El JSON de `catalogo-reporte` |
| `estado()` | `{tema, modo, marca, graficos: [{id, tipo, titulo}]}`; `modo` es `claro`, `oscuro` o `sistema`, y `titulo`, el encabezado visible del grafico |
| `vistaPrevia({tema, modo, marca})` | Lo aplica en pantalla sin guardar nada; `marca: null` quita los colores del despacho |
| `alternativas(id)` | Los tipos de la familia del grafico cargados en el motor: `[{tipo, nombre, pregunta, actual, aviso}]`, con `aviso` en el idioma del documento si ese tipo no conviene con estos datos; `[]` si el tipo no tiene familia |
| `actualizar(id, {tipo})` | Redibuja el grafico con otro tipo |
| `restaurar()` | Vuelve al diseno con el que cargo la pagina |

**El visor guarda lo que ve.** Al guardar, la app serializa el DOM (`outerHTML`), asi que lo que los scripts anaden al cargar acaba en el archivo. Por eso todo nodo que un script anade fuera de un grafico (un `<style>` en el `head`, una diapositiva, una linea del indice, el pie o el logo de la marca) lleva `data-generado`, y el motor, que se ejecuta antes que los modulos y la maqueta, quita al arrancar todos los `[data-generado]` que vengan del archivo; la hoja de la marca tiene ademas el id fijo `estilo-marca`. Lo que se dibuja dentro de un hueco `data-grafico` no lo necesita: el motor vacia el hueco antes de dibujar. Un script nuevo de maqueta o de modulo sigue la misma regla.

Por eso el catalogo, la etiqueta `reportes-diseno` y los 21 temas no se quitan nunca de la base, y un grafico que se quiera poder cambiar de forma usa un tipo de una familia (`biblioteca-componentes-visuales.md`). Los tipos de modulo de las familias (`area_apilada`, `escalones`, `pareto`, `anillos`, `treemap` y `progreso`) solo aparecen como alternativa si su modulo va copiado.

## 8. Datos y marcadores

- Ningun dato inventado. Cifras, fechas, importes y referencias proceden de lo aportado por el usuario, de un documento de su espacio de trabajo o de una fuente verificada en la sesion.
- Los datos que falten permanecen como `{{VARIABLE}}` visible en la pagina, nunca como un cero o un guion que simule un valor real.
- Todo artefacto lleva su aviso DRAFT visible en la parte superior y el pie con fuentes y advertencia legal.

## 9. Tamano

El archivo completo no deberia superar unos **170 KB**; la base con el motor ocupa unos 100, de los que unos 35 son los 21 temas y el catalogo que permiten cambiar el diseno desde la app. Los documentos abiertos del espacio de trabajo se incorporan enteros al contexto de la conversacion y compiten por un presupuesto comun: un artefacto desmesurado desplaza a los documentos de trabajo del usuario. Si el volumen de datos es mayor, se resume la serie, se agrupa por tramos o se reparte en dos artefactos: un panel con lo esencial y un documento con el detalle.

Los artefactos de ejemplo pesan entre 105 y 155 KB (los que llevan varios modulos son los mayores), que es el orden de magnitud esperable.
