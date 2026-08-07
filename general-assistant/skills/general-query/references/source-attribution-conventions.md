# Convenciones de atribucion de fuentes

> Material de referencia para la skill `general-query`. Lo lee Claude al componer la respuesta final. NO se incluye en el output al usuario; las convenciones mismas si se aplican al output.

## Objetivo

Toda respuesta del plugin `general-assistant` debe permitir al usuario **verificar** las afirmaciones que contiene. Esto se logra con:

1. **Lista de Fuentes** al final, con URL visible por cada resultado de `io.gravitonai.tools.web_search` usado.
2. **Marcador `[verificar]`** en todo claim factual que no se haya podido confirmar con una fuente directa.

## Cuando citar una fuente

Citar una fuente (incluir URL en la seccion "Fuentes") cuando la respuesta usa un resultado de `io.gravitonai.tools.web_search` para sustentar un claim factual. Concretamente:

- Cifras, estadisticas, fechas concretas.
- Nombres de entidades, productos, servicios, organizaciones.
- Citas textuales o parafraseadas de documentos publicos.
- Referencias a jurisprudencia, regulacion o doctrina abierta.
- Definiciones tecnicas sacadas de fuentes autoritativas.

NO citar fuente cuando la respuesta es:

- Razonamiento logico o matematico propio.
- Explicacion conceptual pedagogica (no factual).
- Redaccion, traduccion, estructura.
- Opiniones o recomendaciones generales no factuales.

## Cuando marcar `[verificar]`

Marcar `[verificar]` cuando:

- La respuesta invoca `io.gravitonai.tools.web_search` pero la busqueda no dio resultados utiles. → Marcar los claims que dependian de esa busqueda.
- La tool no esta disponible y la respuesta se basa en conocimiento general. → Marcar todos los claims factuales.
- El usuario hace una afirmacion que el plugin no puede confirmar ni desmentir. → Marcar la afirmacion como `[verificar]` en lugar de confirmarla o desmentirla.
- La respuesta depende de datos que cambian rapidamente (cotizaciones, resultados deportivos, estado de servicios) y la fuente es de hace mas de 24h.

## Formato de la seccion "Fuentes"

Lista numerada, una entrada por cada resultado de `io.gravitonai.tools.web_search` usado:

```
## Fuentes

1. Titulo del resultado — https://url-del-resultado
2. Otro titulo — https://otra-url
```

Reglas:
- **Solo resultados efectivamente usados.** Si se invoco web_search pero solo se uso un resultado, listar solo ese.
- **Titulo del resultado, no titulo inventado.** Usar el `title` que devolvio `web_search`.
- **URL completa, no acortada.** Sin `...` ni parametros de tracking. URL limpia, la que devolvio la tool.
- **Sin numeracion decorativa.** Numerar consecutivamente desde 1.
- **Al final del output.** Despues del cuerpo de la respuesta y, si aplica, despues de "Verificar".

## Formato de la seccion "Verificar"

Lista con guion, una entrada por claim no confirmado:

```
## Verificar

- Afirmacion que depende de datos publicos no confirmados.
- Otra afirmacion que el plugin no pudo verificar.
```

Reglas:
- **Conciso.** Una frase corta por claim, sin entrar en detalle.
- **Trazable.** Si el claim se derivo de una fuente especifica que no se pudo cargar, mencionarla.
- **Opcional.** Solo incluir si hay claims no confirmados. Si la respuesta es totalmente verificable con fuentes citadas, omitir la seccion.

## Ejemplo completo

Supongamos que el usuario pregunta: "Cual es la poblacion actual de Tokio?".

1. Se invoca `io.gravitonai.tools.web_search` con `query="Tokyo population 2025"`.
2. La tool devuelve 5 resultados; 2 son utiles (Wikipedia, datos de la oficina de estadistica de Tokio).
3. La respuesta sintetiza: "Segun las fuentes consultadas, la poblacion de Tokio (area metropolitana) ronda los 37-41 millones en 2025."
4. La seccion "Fuentes" lista los 2 resultados.
5. No hay seccion "Verificar" porque los claims principales estan citados.

```
La poblacion del area metropolitana de Tokio ronda los 37-41 millones de habitantes en 2025, segun las estimaciones mas recientes.

## Fuentes

1. Tokyo - Wikipedia — https://en.wikipedia.org/wiki/Tokyo
2. Tokyo Metropolitan Government Statistics — https://www.stat.go.jp/english/
```

## Anti-patrones (lo que NO se debe hacer)

- **No usar numeros redondos sin fuente.** "Alrededor de 100 millones" sin cita es peor que decir "segun las fuentes consultadas, alrededor de X".
- **No inventar URL.** Si la tool no devolvio una URL, no inventar una.
- **No citar mas de lo necesario.** Si la respuesta solo uso 2 resultados, no listar los 5.
- **No mezclar Fuentes y Verificar.** Son secciones distintas: Fuentes = confirmado, Verificar = no confirmado.
- **No usar ambos para el mismo claim.** Si algo esta en Fuentes, no lo marques tambien como `[verificar]`.
