# Anatomia de un artefacto HTML autocontenido

Reglas tecnicas invariables del formato. Todo artefacto que produzca esta skill debe cumplirlas sin excepcion, porque el archivo se abre directamente en el navegador del usuario desde su espacio de trabajo (esquema `file://`), sin servidor ni conexion garantizada.

## 1. Un unico archivo, cero dependencias externas

- **Extension `.html`** y **un solo archivo**. Todo el CSS va en un unico `<style>` dentro de `<head>`; todo el JavaScript en un unico `<script>` antes de `</body>`.
- **Prohibido** cualquier recurso remoto: `<script src="https://...">`, `<link rel="stylesheet" href="https://...">`, fuentes de Google Fonts, imagenes por URL, `fetch`, `XMLHttpRequest`, `import` de modulos remotos, iframes a terceros. Bajo `file://` fallan en silencio o los bloquea el navegador y el artefacto se ve roto.
- **Prohibidas las librerias** (Chart.js, D3, Tailwind por CDN, React, jQuery). Los graficos se dibujan con SVG en linea o con CSS, segun `biblioteca-componentes-visuales.md`.
- Si hace falta una imagen, se incrusta como SVG en linea o como `data:` URI, y solo si es imprescindible.
- Tipografia: pila de fuentes del sistema (`ui-sans-serif, -apple-system, "Segoe UI", Roboto, Arial, sans-serif`). Nunca fuentes descargadas.

## 2. Cabecera obligatoria

```html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Titulo del artefacto</title>
```

El `lang` es el idioma de la conversacion. El `<title>` es un nombre corto y reconocible, no un resumen: es lo que se ve en la pestana del navegador.

## 3. Sistema de diseno por tokens

Todos los colores, espacios, radios y sombras se declaran como variables CSS en `:root`, en espanol, y se consumen con `var(--token)`. Nunca se escribe un color literal en una regla.

- La paleta clara completa se define en `:root` sin condiciones.
- El tema oscuro **solo redefine tokens** dentro de `@media (prefers-color-scheme: dark)`. Ningun color puede tener su unica definicion dentro del bloque oscuro.
- `color-scheme: light dark` en `:root`, y `body` siempre con `background: var(--fondo)` explicito.

| Grupo | Tokens |
| :--- | :--- |
| Superficies | `--fondo`, `--superficie`, `--superficie-2`, `--borde`, `--borde-suave` |
| Texto | `--texto`, `--apagado` |
| Acento y estado | `--acento`, `--acento-suave`, `--acento-fuerte`, `--ok`, `--aviso`, `--riesgo` |
| Serie categorica | `--c1` a `--c6`, `--linea-rejilla` |
| Espaciado | `--e1` 4px, `--e2` 8px, `--e3` 12px, `--e4` 20px, `--e5` 32px, `--e6` 52px |
| Forma | `--radio`, `--radio-s`, `--sombra` |
| Tipografia | `--fuente`, `--ancho` (ancho maximo del contenedor, propio de cada plantilla) |

### Escala tipografica y profundidad

- Titulo principal con `clamp(1.65rem, 3.6vw, 2.4rem)`, tracking `-.022em` y peso 680; cifras de indicador con `clamp(1.5rem, 2.5vw, 1.95rem)` y `font-variant-numeric: tabular-nums`.
- Todo el espaciado sale de la escala `--e1` a `--e6`: no se escriben pixeles sueltos.
- La sombra es de tres capas (contacto, media y ambiental) en un unico token, y desaparece en impresion.
- El fondo lleva un degradado radial muy tenue derivado del acento (`color-mix`); si el navegador no soporta `color-mix`, la regla se ignora y queda el color plano.
- Cada tarjeta de indicador lleva una linea superior de 3px con el color de su estado.

### Movimiento

Solo dos animaciones, ambas dentro de `@media (prefers-reduced-motion: no-preference)` y anuladas en impresion con `*{animation:none!important}`:

- `.aparece`: entrada escalonada de las tarjetas (opacidad y 7px de desplazamiento, 0,55 s).
- Las barras crecen desde la izquierda con `transform: scaleX()`, sin necesidad de JavaScript.

### Nombres en espanol

Clases e identificadores del documento estan en espanol y no se traducen ni se renombran: `.contenedor`, `.borrador`, `.antetitulo`, `.entradilla`, `.ficha`, `.indicadores`, `.indicador`, `.tarjeta`, `.malla`, `.aviso`, `.distintivo`, `.cronologia`, `.barras`, `.pista`, `.leyenda`, `.tabla`, `.cifra`, `.acciones`, `.pie`, `.medidor`, `.anillo`, `.cascada`, `.chispa`, `.verificacion`, `.progreso`, `.indice`, `.firma`. Identificadores del script: `imprimir`, `reiniciar`, `formulario`, `verificacion`, `resultado1` a `resultado3`, `cuerpo-desglose`, `barra-progreso`, `texto-progreso`, `arco-medidor`, `medidor-cifra`.

## 4. Adaptabilidad y desbordamiento

- Unidades relativas, `grid` con `repeat(auto-fit, minmax(...))` y `flex-wrap`. El cuerpo de la pagina nunca desborda en horizontal.
- Todo contenido ancho (tablas, graficos, bloques de codigo) va dentro de un contenedor con `overflow-x: auto`.
- **Los hijos de una rejilla llevan `min-width: 0`**. Sin esa regla, una tabla con `min-width` empuja su columna y toda la pagina desborda en horizontal aunque el contenedor tenga `overflow-x: auto`. Es el fallo de maquetacion mas frecuente y no se ve en pantalla ancha.
- `svg { max-width: 100%; height: auto; }` y `viewBox` siempre presente para que el grafico escale.

## 5. Impresion y exportacion a PDF

El usuario imprime el artefacto o lo guarda como PDF desde el navegador (dialogo de impresion, destino *Guardar como PDF*). Es obligatorio:

- Un bloque `@media print` que redefina los tokens a papel (`--fondo:#fff`, `--superficie:#fff`, `--texto:#000`, `--sombra:none`), quite el degradado de fondo (`background-image:none`), oculte los botones (`.acciones{display:none}`) y anule animaciones y transiciones.
- `@page` con tamano y margen segun la plantilla: A4 vertical, con 16 mm de margen en el informe, 15 mm en la herramienta y 14 mm en el panel.
- **Las rejillas se deshacen al imprimir** (`.malla{display:block}`, `.columnas{grid-template-columns:1fr}`): Chrome pagina mal dentro de una rejilla y deja medias paginas en blanco. En papel las tarjetas van una debajo de otra.
- Los graficos de las tarjetas estrechas se limitan con `max-height` para que no impongan saltos de pagina; los de las tarjetas a todo lo ancho conservan su tamano.
- `break-inside: avoid` en tarjetas, indicadores y secciones; `break-after: avoid` en los encabezados.
- `thead { display: table-header-group }` para que el encabezado de una tabla larga se repita en cada pagina.
- En el informe, el indice lateral desaparece y el contenido pasa a una sola columna.
- **Fidelidad de color en papel:** `*{-webkit-print-color-adjust:exact; print-color-adjust:exact}` dentro de `@media print`. Sin esto, quien imprima sin marcar *graficos de fondo* se lleva las barras y las areas en blanco, y el artefacto pierde justo lo que lo hacia util.
- **Tipografia de pagina:** `p{orphans:3;widows:3}`, `h1,h2,h3{break-after:avoid}`, `tr{break-inside:avoid}`, y `break-inside:avoid` en avisos, leyendas, barras e hitos de cronologia. Una fila partida por la mitad o un titulo solo al pie de pagina delatan el documento.
- Un boton visible en pantalla que invoque `window.print()`. El nombre del PDF que propone el navegador sale del `<title>`, asi que ese titulo es tambien el nombre del archivo.
- **Cabeceras y pies repetidos en cada pagina: no.** Un elemento `position:fixed` parece la solucion evidente, pero Chrome lo coloca una sola vez y fuera de sitio —acaba al pie de la primera pagina y tapando la primera linea de la siguiente—. Si hace falta identificacion en cada hoja, se deja al dialogo de impresion del navegador (que anade cabecera, pie, fecha y numero de pagina) o se acepta que la identificacion viva en la cabecera del documento y en su pie final.

## 6. JavaScript permitido y prohibido

- Permitido: JavaScript nativo, envuelto en una funcion autoejecutada con `"use strict"`, que lee campos del formulario, calcula y actualiza el DOM.
- **Prohibido**: `alert()`, `confirm()` y `prompt()` (bloquean la ventana), `eval()`, `new Function()`, `document.write()`, temporizadores infinitos y cualquier llamada de red.
- **Prohibido inyectar texto con `innerHTML`** a partir de valores introducidos por el usuario: siempre `textContent` o `createElement`. Es la unica proteccion real frente a contenido malicioso pegado en un campo.
- El almacenamiento del navegador (`localStorage`, `sessionStorage`) falla o lanza excepcion bajo `file://` en varios navegadores. No se usa; si excepcionalmente se usara, siempre dentro de `try/catch` y con la pagina funcionando igual sin el.
- El artefacto debe renderizar contenido util aunque el JavaScript este desactivado: los datos ya calculados van escritos en el HTML, y el script solo aporta recalculo e interaccion.

## 7. Accesibilidad

- Estructura semantica: `main`, `header`, `section`, `footer`, jerarquia de encabezados sin saltos (`h1` unico, luego `h2`, `h3`).
- Todo grafico SVG lleva `role="img"` y un `aria-label` que resume el dato, o un `<title>` dentro del SVG. Un grafico sin texto alternativo es un grafico invisible.
- El color nunca es el unico portador de informacion: se acompana de etiqueta, cifra o icono textual.
- Contraste minimo 4.5:1 en texto normal, verificado en tema claro y oscuro.
- Estados de foco visibles: `:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px }`.
- Todo `input` y `select` tiene su `<label for="...">`.

## 8. Nomenclatura y ubicacion

- Nombre de archivo descriptivo en `snake_case.html` (ej. `panel_reclamacion_cantidad.html`, `simulador_indemnizacion_despido.html`).
- Se crea en la raiz del espacio de trabajo de la conversacion, igual que cualquier otro documento.
- El idioma del nombre del archivo sigue al de la plantilla; el contenido visible sigue al idioma del usuario.

## 8 bis. Edicion posterior

El artefacto se edita **siempre desde el chat**, pidiendo el cambio al asistente, que lo aplica sobre el archivo. Nunca se edita a mano en el editor de texto de la plataforma: ese editor trabaja en markdown y al guardar reescribiria la pagina, perdiendo estilos, graficos y comportamiento.

## 9. Datos y marcadores

- Ningun dato inventado. Cifras, fechas, importes y referencias proceden de lo aportado por el usuario, de un documento de su espacio de trabajo o de una fuente verificada en la sesion.
- Los datos que falten permanecen como `{{VARIABLE}}` visible en la pagina, nunca como un cero o un guion que simule un valor real.
- Todo artefacto lleva su aviso DRAFT visible en la parte superior y el pie con fuentes y advertencia legal.

## 10. Tamano

El archivo completo no deberia superar unos **100 KB**. Los documentos abiertos del espacio de trabajo se incorporan enteros al contexto de la conversacion y compiten por un presupuesto comun: un artefacto desmesurado desplaza a los documentos de trabajo del usuario. Si el volumen de datos es mayor, se resume la serie, se agrupa por tramos o se reparte en dos artefactos: un panel con lo esencial y un documento con el detalle.

Los tres artefactos de ejemplo pesan entre 18 y 27 KB con todos sus graficos, que es el orden de magnitud esperable.
