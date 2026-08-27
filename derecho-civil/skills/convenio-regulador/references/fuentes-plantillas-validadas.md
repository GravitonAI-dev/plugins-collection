# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `convenio-regulador`. Registra las fuentes normativas y las
> plantillas validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el
> plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 1 se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Codigo Civil (Real Decreto de 24 de julio de 1889, texto consolidado) | BOE-A-1889-4763 | consolidado a 03/01/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado a 28/02/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| Ley 15/2015 de la Jurisdiccion Voluntaria | BOE-A-2015-7391 | 02/07/2015 (via notarial y ante LAJ, arts. 54 y 82/87 CC) | https://www.boe.es/buscar/act.php?id=BOE-A-2015-7391 |

Articulos relevantes:
- Codigo Civil: 81, 82, 84, 86, 87 (separacion y divorcio, via judicial vs notarial), 90 (contenido del convenio), 92 (guarda y custodia), 93 (alimentos de los hijos), 94 (regimen de visitas), 95 (efectos economicos), 96 (uso de la vivienda familiar), 97 (pension compensatoria).
- LEC: 777 (separacion o divorcio de mutuo acuerdo), 103 CC por remision (medidas).

---

## Plantillas validadas

| Recurso | Detalle |
|---|---|
| Estructura del convenio regulador | Contenido minimo del Art. 90.1 CC (guarda y custodia, visitas, vivienda, alimentos, liquidacion del regimen economico, pension compensatoria) |
| Estructura de la demanda de mutuo acuerdo | Art. 777 LEC: demanda conjunta + propuesta de convenio + certificaciones de matrimonio y nacimiento |
| Orientacion practica de convenios | Guias de los Colegios de la Abogacia y del Ministerio de Justicia sobre separacion y divorcio de mutuo acuerdo |

Los assets `assets/template-convenio-regulador.md` y `assets/template-demanda-divorcio-mutuo-acuerdo.md` reflejan esta estructura. En cada lanzamiento, la skill re-verifica los articulos citados en el BOE; si detecta una redaccion posterior, actualiza el asset y las references afectadas.

---

## Guias de estilo de redaccion (consulta)

| Recurso | Uso |
|---|---|
| Guia de redaccion judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminologia y correccion del lenguaje juridico |

Principios aplicados en los assets: convenio con clausulas numeradas por materia del Art. 90; demanda con estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO; evitar latinajos innecesarios; una idea por parrafo.

---

## Verificacion de normativa autonomica

El derecho civil foral (Cataluna, Aragon, Navarra, Pais Vasco, Baleares, Galicia) puede regular de forma propia el regimen economico matrimonial, la guarda y custodia o la vivienda familiar. Si el matrimonio se rige por un derecho foral, verificar con `web_search` la norma autonomica vigente antes de redactar y advertir al usuario.
