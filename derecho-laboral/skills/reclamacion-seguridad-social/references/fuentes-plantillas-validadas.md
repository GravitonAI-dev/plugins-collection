# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `reclamacion-seguridad-social`.

---

## Regla de verificación permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una versión posterior a la registrada, aplica la redacción vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la referencia local y se advierte al usuario de que la verificación queda pendiente.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Ley General de la Seguridad Social — texto refundido aprobado por Real Decreto Legislativo 8/2015 | BOE-A-2015-11724 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| Ley 36/2011, reguladora de la Jurisdicción Social | BOE-A-2011-15936 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2011-15936 |
| Estatuto de los Trabajadores — texto refundido aprobado por Real Decreto Legislativo 2/2015 | BOE-A-2015-11430 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430 |

Artículos relevantes de la Ley 36/2011: 2.o) (ámbito), 64 (excepción de conciliación), 71 (reclamación administrativa previa), 140 a 147 (procedimiento en materia de prestaciones) y 143 (remisión del expediente administrativo).

Normativa de desarrollo cuya identificación y versión vigente debe verificarse con `web_search` antes de citarla: normativa reglamentaria de la incapacidad temporal y del procedimiento de disconformidad con el alta médica, reglamento general de prestaciones económicas, y órdenes anuales de cotización y de revalorización de pensiones.

---

## Magnitudes que se verifican en cada asunto y nunca se escriben de memoria

| Magnitud | Fuente |
|---|---|
| Salario mínimo interprofesional del ejercicio | Real decreto anual publicado en el BOE |
| Indicador público de renta de efectos múltiples | Ley de presupuestos generales del Estado del ejercicio |
| Bases máximas y mínimas de cotización | Orden anual de cotización |
| Topes máximo y mínimo de pensión | Normativa de revalorización de pensiones del ejercicio |
| Porcentajes aplicables a cada grado y a cada prestación | Texto consolidado vigente de la Ley General de la Seguridad Social |
| Plazos de la reclamación previa y de resolución de la entidad | Artículo 71 de la Ley 36/2011, en su redacción vigente |
| Plazo y procedimiento de disconformidad con el alta médica | Ley General de la Seguridad Social y su normativa de desarrollo, en su redacción vigente |
| Definición de los grados de incapacidad permanente | Texto vigente **y su régimen transitorio** |

---

## Sedes electrónicas y organismos

El órgano destinatario exacto y su sede electrónica **se verifican con `web_search` en cada asunto**. Como orientación general:

| Entidad | Competencia típica |
|---|---|
| Instituto Nacional de la Seguridad Social | Incapacidad temporal a partir de los plazos legalmente previstos, incapacidad permanente, jubilación, muerte y supervivencia, nacimiento y cuidado |
| Instituto Social de la Marina | Las mismas prestaciones respecto del régimen especial de trabajadores del mar |
| Servicio Público de Empleo Estatal | Prestaciones y subsidios por desempleo |
| Mutuas colaboradoras con la Seguridad Social | Gestión de la incapacidad temporal por contingencias profesionales y, en su caso, comunes; prestación por riesgo durante el embarazo y la lactancia; cuidado de menores con enfermedad grave |
| Tesorería General de la Seguridad Social | Afiliación, cotización y recaudación — **fuera del alcance de esta skill** |

---

## Jurisprudencia

Esta skill **no cita jurisprudencia de memoria**. Toda cita debe verificarse en la misma sesión mediante `web_search` en el CENDOJ (https://www.poderjudicial.es/search/indexAN.jsp), con órgano, sala, fecha y número de recurso. Si no se puede verificar, no se cita.

---

## Estilo de redacción

Principios aplicados en los assets: cabecera con el plazo aplicable y la fecha límite calculada, visible antes que nada; datos del interesado y del expediente en tabla, con el número de afiliación y el de expediente destacados, sin los cuales el escrito no se vincula al procedimiento; **separación estricta entre diagnóstico y limitación funcional**, con tabla de informes médicos por fecha, facultativo y contenido; descripción real de las tareas del puesto como sección propia; solicitud expresa del expediente administrativo completo; bloque final de advertencias con los riesgos específicos de cada trámite, señaladamente el riesgo de reducción del grado en la solicitud de revisión.
