# Temas visuales

Los 21 temas van **dentro de la base** (`assets/template-base-reportes.md`): se elige uno solo con la etiqueta `html`, `data-tema="<id>"`, y no se copia ni se borra nada. Por eso el usuario puede cambiar de tema despues, desde la barra del visor, sin pasar por la IA. El CSS de cada tema esta en la base y solo en la base; este documento es su catalogo.

Cada tema redefine los tokens de `:root` (colores, radios, sombra y, en algunos, la pila de fuentes), trae su version oscura en los mismos tokens con el sufijo `-o` (`--fondo-o`, `--c1-o`...) y, cuando el estilo lo pide, unas pocas reglas de forma (cabecera, tarjetas, titulares). Todos imprimen en blanco con la misma regla `@media print` de la base, que quita tambien los degradados de fondo; los temas siempre oscuros traen ademas su paleta de papel, con acentos y series que contrastan sobre blanco. Todos cumplen el contraste minimo 4.5:1 en claro y en oscuro.

**Modo claro u oscuro.** Sin mas, el artefacto sigue al sistema: claro de dia, oscuro de noche. `data-modo="claro"` o `data-modo="oscuro"` en la etiqueta `html` lo fija (pregunta `colores_reporte` de SKILL.md). Los seis temas siempre oscuros (`nocturno`, `dorado`, `esmeralda_noche`, `ambar`, `oliva_oro`, `lima`) ignoran el modo. En papel rige siempre la version clara.

**Colores del despacho.** Encima de cualquier tema se aplican con el bloque `marca` de los datos (`modulos-motor.md`), que sustituye el acento y la serie por los colores corporativos. Un tema nunca se edita para un caso.

## Catalogo

| Tema | `data-tema` | Para quien y para que | Rasgos |
| :--- | :--- | :--- | :--- |
| Moderno | `moderno` | Paneles de datos, herramientas, presentaciones; cliente empresa o startup | Azul vivo, degradado de fondo, tarjetas muy redondeadas con sombra, cifras grandes. Es la base de los colores propios del despacho |
| Sobrio de despacho | `sobrio` | Informes de viabilidad y dictamenes; juzgado, cliente institucional | Azul petroleo y neutros calidos, radios cortos, sin degradado |
| Editorial | `editorial` | White papers, memorias, dossieres largos que se van a imprimir | Serif de sistema, papel crema, filetes finos, sin sombras, titulares grandes |
| Corporativo | `corporativo` | Memorias anuales, informes de KPIs, comites de direccion | Azul marino y gris, tarjetas cuadradas con borde marcado, cabecera con filete lateral, titulos de seccion en mayusculas |
| Minimal | `minimal` | Resumenes ejecutivos de una pagina, propuestas de honorarios | Blanco, negro y un unico acento naranja; sin bordes ni sombras; serie de grises |
| Nocturno | `nocturno` | Presentaciones en pantalla, paneles para sala de reuniones | Oscuro siempre (tambien con el sistema en claro), turquesa e indigo, brillo suave. Imprime en blanco |
| Tecnico | `tecnico` | Auditorias, cumplimiento, informes forenses o de sistemas | Monoespaciada de sistema, verde azulado, bordes de un pixel, radios minimos |
| Calido | `calido` | Particulares, inmobiliario, herencias y familia; casos de exito | Tierras: terracota, oliva y ocre sobre arena; radios amplios |
| Institucional | `institucional` | Administracion, universidades, colegios profesionales, fundaciones | Granate y dorado, titulares en serif, cabecera con filete doble |
| Pizarra | `pizarra` | Paneles densos de seguimiento, facturacion y cobros, tablas largas | Grises pizarra con acento cian, tarjetas con filete lateral, tablas compactas |
| Suave | `suave` | Boletines, comunicacion interna, casos de exito | Pasteles sobre lila, radios grandes, sombra difusa |
| Prensa | `prensa` | Boletines normativos, notas de actualidad, newsletters | Serif de periodico, blanco y negro con un rojo, filete grueso de cabecera, entradilla en cursiva |
| Alto contraste | `alto_contraste` | Accesibilidad, lectores con baja vision, proyeccion con mala luz | Negro, blanco y amarillo (en oscuro), bordes de dos pixeles, sin radios ni colores suaves |
| Dorado | `dorado` | Direccion, patrimonio, banca privada, presentaciones de prestigio | Siempre oscuro: negro y oro con verde salvia, titulares en serifa, brillo dorado en las cifras |
| Esmeralda nocturno | `esmeralda_noche` | Paneles de seguimiento en pantalla, sostenibilidad, energia | Siempre oscuro: negro verdoso, esmeralda y oro |
| Ambar | `ambar` | Salas de control, paneles operativos, alertas | Siempre oscuro: negro, ambar y amarillo con verde lima, titulos en mayusculas |
| Oliva y oro | `oliva_oro` | Agroalimentario, rural, bodegas, patrimonio familiar | Siempre oscuro: verde oliva profundo con oro y verdes calidos |
| Lima | `lima` | Tecnologia, datos, startups | Siempre oscuro: negro con lima y amarillo, cifras monoespaciadas, radios cortos |
| Menta | `menta` | Salud, bienestar, comunicacion amable con particulares | Pastel: menta y melocoton sobre blanco verdoso, radios grandes |
| Melocoton | `melocoton` | Familia, educacion, eventos, boletines cercanos | Pastel: melocoton, rosa y verde agua |
| Lavanda | `lavanda` | Comunicacion interna, RR. HH., formacion | Pastel: lavanda y rosa con verde agua |

**Como orientar.** La eleccion la hace el usuario (SKILL.md, 1.2); si duda, se le recomienda segun el destinatario y el soporte: a un juzgado o a un organismo, `sobrio` o `institucional`; a una direccion financiera, `corporativo` o `pizarra`; a un particular, `calido` o `suave`; a una sala con proyector o una pantalla, `nocturno`, `dorado`, `esmeralda_noche`, `ambar`, `lima` o `alto_contraste`; a un comunicado cercano, `suave`, `menta`, `melocoton` o `lavanda`; a papel, `editorial`, `prensa` o `minimal`.

**Lo que no cambia con el tema.** Los graficos usan los tokens (`--c1` a `--c6`, `--ok`, `--aviso`, `--riesgo`) y por eso heredan la paleta solos; las clases y la estructura de las maquetas son las mismas; la regla de impresion es comun. Un tema nunca se edita para un caso: si hacen falta otros colores, se usa el bloque `marca`.

**Familias.** Claros: `moderno`, `sobrio`, `editorial`, `corporativo`, `minimal`, `tecnico`, `calido`, `institucional`, `pizarra`, `prensa` y `alto_contraste`. Siempre oscuros: `nocturno`, `dorado`, `esmeralda_noche`, `ambar`, `oliva_oro` y `lima`; sus acentos son claros, asi que las cifras dentro de barras se escriben en oscuro. Pastel: `suave`, `menta`, `melocoton` y `lavanda`, con version clara y oscura; sus series son suaves, asi que las cifras dentro de barras van en el color del texto y los titulares usan un acento mas profundo que la serie. La familia de cada tema va tambien en el catalogo `catalogo-reporte` de la base, que lee la app.
