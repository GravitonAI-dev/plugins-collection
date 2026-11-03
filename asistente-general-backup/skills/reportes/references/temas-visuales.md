# Temas visuales

Los 21 temas van **dentro de la base** (`assets/template-base-reportes.md`): se elige uno solo con la etiqueta `html`, `data-tema="<id>"`, y no se copia ni se borra nada. Por eso el usuario puede cambiar de tema después, desde la barra del visor, sin pasar por la IA. El CSS de cada tema está en la base y solo en la base; este documento es su catálogo.

Cada tema redefine los tokens de `:root` (colores, radios, sombra y, en algunos, la pila de fuentes), trae su versión oscura en los mismos tokens con el sufijo `-o` (`--fondo-o`, `--c1-o`...) y, cuando el estilo lo pide, unas pocas reglas de forma (cabecera, tarjetas, titulares). Todos imprimen en blanco con la misma regla `@media print` de la base, que quita también los degradados de fondo; los temas siempre oscuros traen además su paleta de papel, con acentos y series que contrastan sobre blanco. Todos cumplen el contraste mínimo 4.5:1 en claro y en oscuro.

**Modo claro u oscuro.** Sin más, el artefacto sigue al sistema: claro de día, oscuro de noche. `data-modo="claro"` o `data-modo="oscuro"` en la etiqueta `html` lo fija (pregunta `colores_reporte` de SKILL.md). Los seis temas siempre oscuros (`nocturno`, `dorado`, `esmeralda_noche`, `ambar`, `oliva_oro`, `lima`) ignoran el modo. En papel rige siempre la versión clara.

**Colores del despacho.** Encima de cualquier tema se aplican con el bloque `marca` de los datos (`modulos-motor.md`), que sustituye el acento y la serie por los colores corporativos. Un tema nunca se edita para un caso.

## Catálogo

| Tema | `data-tema` | Para quién y para que | Rasgos |
| :--- | :--- | :--- | :--- |
| Moderno | `moderno` | Paneles de datos, herramientas, presentaciones; cliente empresa o startup | Azul vivo, degradado de fondo, tarjetas muy redondeadas con sombra, cifras grandes |
| Sobrio de despacho | `sobrio` | Informes de viabilidad y dictámenes; juzgado, cliente institucional | Azul petroleo y neutros cálidos, radios cortos, sin degradado |
| Editorial | `editorial` | White papers, memorias, dossieres largos que se van a imprimir | Serif de sistema, papel crema, filetes finos, sin sombras, titulares grandes |
| Corporativo | `corporativo` | Memorias anuales, informes de KPIs, comités de dirección | Azul marino y gris, tarjetas cuadradas con borde marcado, cabecera con filete lateral, títulos de sección en mayúsculas |
| Minimal | `minimal` | Resúmenes ejecutivos de una página, propuestas de honorarios | Blanco, negro y un único acento naranja; sin bordes ni sombras; serie de grises |
| Nocturno | `nocturno` | Presentaciones en pantalla, paneles para sala de reuniones | Oscuro siempre (también con el sistema en claro), turquesa e indigo, brillo suave. Imprime en blanco |
| Técnico | `tecnico` | Auditorias, cumplimiento, informes forenses o de sistemas | Monoespaciada de sistema, verde azulado, bordes de un pixel, radios mínimos |
| Cálido | `calido` | Particulares, inmobiliario, herencias y familia; casos de éxito | Tierras: terracota, oliva y ocre sobre arena; radios amplios |
| Institucional | `institucional` | Administración, universidades, colegios profesionales, fundaciones | Granate y dorado, titulares en serif, cabecera con filete doble |
| Pizarra | `pizarra` | Paneles densos de seguimiento, facturación y cobros, tablas largas | Grises pizarra con acento cian, tarjetas con filete lateral, tablas compactas |
| Suave | `suave` | Boletines, comunicación interna, casos de éxito | Pasteles sobre lila, radios grandes, sombra difusa |
| Prensa | `prensa` | Boletines normativos, notas de actualidad, newsletters | Serif de periódico, blanco y negro con un rojo, filete grueso de cabecera, entradilla en cursiva |
| Alto contraste | `alto_contraste` | Accesibilidad, lectores con baja visión, proyección con mala luz | Negro, blanco y amarillo (en oscuro), bordes de dos pixeles, sin radios ni colores suaves |
| Dorado | `dorado` | Dirección, patrimonio, banca privada, presentaciones de prestigio | Siempre oscuro: negro y oro con verde salvia, titulares en serifa, brillo dorado en las cifras |
| Esmeralda nocturno | `esmeralda_noche` | Paneles de seguimiento en pantalla, sostenibilidad, energía | Siempre oscuro: negro verdoso, esmeralda y oro |
| Ámbar | `ambar` | Salas de control, paneles operativos, alertas | Siempre oscuro: negro, ámbar y amarillo con verde lima, títulos en mayúsculas |
| Oliva y oro | `oliva_oro` | Agroalimentario, rural, bodegas, patrimonio familiar | Siempre oscuro: verde oliva profundo con oro y verdes cálidos |
| Lima | `lima` | Tecnología, datos, startups | Siempre oscuro: negro con lima y amarillo, cifras monoespaciadas, radios cortos |
| Menta | `menta` | Salud, bienestar, comunicación amable con particulares | Pastel: menta y melocotón sobre blanco verdoso, radios grandes |
| Melocotón | `melocoton` | Familia, educación, eventos, boletines cercanos | Pastel: melocotón, rosa y verde agua |
| Lavanda | `lavanda` | Comunicación interna, RR. HH., formación | Pastel: lavanda y rosa con verde agua |

**Cómo orientar.** La elección la hace el usuario (SKILL.md, 1.2); si duda, se le recomienda según el destinatario y el soporte: a un juzgado o a un organismo, `sobrio` o `institucional`; a una dirección financiera, `corporativo` o `pizarra`; a un particular, `calido` o `suave`; a una sala con proyector o una pantalla, `nocturno`, `dorado`, `esmeralda_noche`, `ambar`, `lima` o `alto_contraste`; a un comunicado cercano, `suave`, `menta`, `melocoton` o `lavanda`; a papel, `editorial`, `prensa` o `minimal`.

**Lo que no cambia con el tema.** Los gráficos usan los tokens (`--c1` a `--c6`, `--ok`, `--aviso`, `--riesgo`) y por eso heredan la paleta solos; las clases y la estructura de las maquetas son las mismas; la regla de impresión es común. Un tema nunca se edita para un caso: si hacen falta otros colores, se usa el bloque `marca`.

**Familias.** Claros: `moderno`, `sobrio`, `editorial`, `corporativo`, `minimal`, `tecnico`, `calido`, `institucional`, `pizarra`, `prensa` y `alto_contraste`. Siempre oscuros: `nocturno`, `dorado`, `esmeralda_noche`, `ambar`, `oliva_oro` y `lima`; sus acentos son claros, así que las cifras dentro de barras se escriben en oscuro. Pastel: `suave`, `menta`, `melocoton` y `lavanda`, con versión clara y oscura; sus series son suaves, así que las cifras dentro de barras van en el color del texto y los titulares usan un acento más profundo que la serie. La familia de cada tema va también en el catálogo `catalogo-reporte` de la base, que lee la app.
