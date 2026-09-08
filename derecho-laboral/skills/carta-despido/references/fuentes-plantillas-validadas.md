# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `carta-despido`. Registra las fuentes normativas que la skill
> verifica en cada lanzamiento y las plantillas sobre las que se construyen sus assets.

---

## Regla de verificación permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una versión posterior a la registrada, aplica la redacción vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la referencia local y se advierte expresamente al usuario de que la verificación queda pendiente.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Estatuto de los Trabajadores — texto refundido aprobado por Real Decreto Legislativo 2/2015 | BOE-A-2015-11430 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430 |
| Ley 36/2011, reguladora de la Jurisdicción Social | BOE-A-2011-15936 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2011-15936 |
| Ley General de la Seguridad Social — texto refundido aprobado por Real Decreto Legislativo 8/2015 | BOE-A-2015-11724 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |

Artículos relevantes para esta skill: 14 (periodo de prueba), 15 (duración del contrato), 49.1.c (finalización de contrato temporal), 52 y 53 (extinción por causas objetivas), 54 y 55 (despido disciplinario), 56 (despido improcedente), 59 (prescripción y caducidad) y 60.2 (prescripción de faltas) del Estatuto de los Trabajadores; 103 a 113 (proceso de despido) y 105.2 de la Ley 36/2011.

Normas complementarias cuya identificación y versión vigente debe verificarse con `web_search` antes de citarlas: Real Decreto-ley 32/2021 de reforma laboral, Ley 10/2021 de trabajo a distancia, Ley Orgánica 3/2007 de igualdad efectiva de mujeres y hombres, y Ley 15/2022 integral para la igualdad de trato y la no discriminación.

---

## Convenio colectivo aplicable (verificación obligatoria en cada asunto)

El convenio colectivo no es una fuente accesoria: tipifica las faltas y gradúa las sanciones, fija los preavisos y puede mejorar los mínimos legales. **Ninguna carta de despido disciplinario se redacta sin haber localizado el artículo del convenio que tipifica la falta.**

| Registro | Ámbito | URL |
|---|---|---|
| REGCON — Registro y depósito de convenios y acuerdos colectivos | Estatal y consulta general | https://expinterweb.mites.gob.es/regcon/ |
| Boletín oficial de la comunidad autónoma | Convenios autonómicos | Verificar con `web_search` el boletín correspondiente |
| Boletín oficial de la provincia | Convenios provinciales | Verificar con `web_search` el boletín correspondiente |

Procedimiento de localización: identificar la actividad real de la empresa (no su objeto social formal) y su ámbito territorial, buscar el convenio sectorial correspondiente en REGCON y comprobar la existencia de convenio propio de empresa, que desplaza al sectorial en las materias del artículo 84.2 del Estatuto de los Trabajadores.

---

## Jurisprudencia

Esta skill **no cita jurisprudencia de memoria**. Cuando la redacción o el asesoramiento dependan de doctrina jurisprudencial —señaladamente la relativa a la audiencia previa al trabajador en el despido disciplinario derivada del artículo 7 del Convenio 158 de la Organización Internacional del Trabajo, o la relativa al alcance de la exigencia de concreción de los hechos imputados—, debe verificarse el estado actual de la doctrina con `web_search` en el buscador del CENDOJ antes de afirmar nada en el chat.

| Recurso | Uso | URL |
|---|---|---|
| CENDOJ — Buscador de jurisprudencia del Poder Judicial | Verificación de doctrina del Tribunal Supremo, Sala Cuarta | https://www.poderjudicial.es/search/indexAN.jsp |

---

## Estilo de redacción

Principios aplicados en los assets: encabezamiento con identificación completa de ambas partes; cuerpo dividido en apartados numerados con ordinales; hechos imputados en párrafos separados, uno por hecho, con fecha y conducta; pie de firma de la empresa y recibí del trabajador con la salvedad de que la firma acredita recepción y no conformidad; bloque final de advertencias dirigido al profesional que revisa el borrador, nunca al trabajador destinatario.
