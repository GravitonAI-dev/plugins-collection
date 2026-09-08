# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `sancion-disciplinaria`. Registra las fuentes normativas que la
> skill verifica en cada lanzamiento y las plantillas sobre las que se construyen sus assets.

---

## Regla de verificación permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una versión posterior a la registrada, aplica la redacción vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la referencia local y se advierte al usuario de que la verificación queda pendiente.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Estatuto de los Trabajadores — texto refundido aprobado por Real Decreto Legislativo 2/2015 | BOE-A-2015-11430 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430 |
| Ley 36/2011, reguladora de la Jurisdicción Social | BOE-A-2011-15936 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2011-15936 |

Artículos relevantes: 58 (faltas y sanciones), 60.2 (prescripción de faltas), 64.4.c (información a la representación legal), 68.a (garantías de los representantes) del Estatuto de los Trabajadores; 63, 114 y 115 de la Ley 36/2011.

Norma complementaria cuyo identificador y versión vigente debe verificarse con `web_search` antes de citarla: Ley Orgánica 11/1985, de 2 de agosto, de Libertad Sindical, cuyo artículo 10.3 extiende a los delegados sindicales las garantías reconocidas a los miembros del comité de empresa.

---

## El convenio colectivo es la fuente principal de esta skill

A diferencia de otras materias, en el régimen disciplinario la ley se limita a habilitar la potestad y a fijar límites: **la tipificación de las faltas, su graduación y el cuadro de sanciones aplicable a cada una son materia del convenio colectivo** (artículo 58.1). Sin convenio identificado no hay falta tipificada ni sanción aplicable, y la sanción impuesta queda expuesta a la revocación.

| Registro | Ámbito | URL |
|---|---|---|
| REGCON — Registro y depósito de convenios y acuerdos colectivos | Estatal y consulta general | https://expinterweb.mites.gob.es/regcon/ |
| Boletín oficial de la comunidad autónoma | Convenios autonómicos | Verificar con `web_search` |
| Boletín oficial de la provincia | Convenios provinciales | Verificar con `web_search` |

Datos que deben extraerse del convenio antes de redactar:
1. Artículo que tipifica la conducta y gravedad asignada.
2. Cuadro de sanciones aplicable a esa gravedad, con la duración máxima de la suspensión de empleo y sueldo.
3. Plazo de cancelación de antecedentes disciplinarios.
4. Exigencias procedimentales adicionales (expediente, audiencia previa, plazos de descargo).
5. Obligación de comunicar la sanción a la representación legal de los trabajadores.

---

## Jurisprudencia

Esta skill **no cita jurisprudencia de memoria**. Cuando la valoración de la proporcionalidad o del alcance de la potestad disciplinaria dependa de doctrina jurisprudencial, verificarla con `web_search` en el buscador del CENDOJ (https://www.poderjudicial.es/search/indexAN.jsp) antes de afirmar nada en el chat.

---

## Estilo de redacción

Principios aplicados en los assets: identificación completa de ambas partes; hechos en párrafos separados y numerados, uno por hecho, con fecha y conducta objetiva; calificación citando artículo legal y artículo de convenio; sanción con tipo, duración y fechas de inicio, fin y reincorporación; advertencia de reiteración; pie de firma con recibí del trabajador y salvedad de que la firma acredita recepción y no conformidad; bloque final de advertencias dirigido al profesional que revisa, nunca al trabajador.
