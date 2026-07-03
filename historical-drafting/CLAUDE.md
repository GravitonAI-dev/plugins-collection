# CLAUDE.md — historical-drafting (plugin)

> Playbook del plugin `historical-drafting`. Lo lee Claude al activar cualquier skill de este plugin. Las reglas de aqui solo pueden **estrechar** las reglas globales del `CLAUDE.md` raiz, nunca ampliarlas.

## Proposito

Apoyar a investigadores en general en la produccion de **borradores** de resumenes y analisis estructurados sobre eventos historicos, con trazabilidad de fuentes y separacion explicita entre hecho documentado e interpretacion. El plugin produce borradores para revision humana; no emite verdades historiograficas definitivas.

## Audiencia objetivo

- Investigadores en general (academicos, divulgadores, periodistas, estudiantes de grado y postgrado, analistas).
- Lectores no especialistas que necesitan un punto de partida estructurado y verificable sobre un evento historico concreto.

> **No** es para: historia especulativa sin fuentes, revision por pares formal, publicacion academica sin supervision humana. Esos flujos requieren herramientas y validacion fuera de este plugin.

## Jurisdiccion por defecto

<!-- EDITAR PARA TU EQUIPO: ajustar la jurisdiccion/periodo/epoca por defecto segun donde opera el equipo de investigacion. Ej: "LATAM s. XIX", "Europa s. XX", "agnostica". -->

- **Asumida**: agnostica. El plugin no asume pais, epoca ni periodo.
- **Idioma de fuentes esperado**: espanol por default. Si la consulta es en otro idioma, mantenerlo y buscar fuentes en ese idioma cuando sea posible.
- **Contexto cultural/geografico**: si el usuario no lo especifica, no asumir. Marcar como `[verificar: contexto geografico]` y proceder solo cuando el evento lo haga evidente por sus fuentes.

## Tono y estilo de output

- **Academico sobrio, neutral, descriptivo.** El output distingue siempre entre **hecho documentado** e **interpretacion/analisis**.
- **Citando siempre.** Toda afirmacion factual debe incluir la fuente (autor, obra, anio o URL). Sin fuente → no se afirma.
- **Trazabilidad visible.** Cada bloque del output lleva marcadores de fuente para que un revisor pueda auditarlos sin re-buscar.
- **Plantilla siempre.** Todo memo de salida usa la plantilla en `skills/<skill>/assets/`. No improvisar formato.
- **Sin emojis en archivos.** Sin emojis en el output al usuario, salvo que el usuario los pida explicitamente.

## Defaults

<!-- EDITAR PARA TU EQUIPO: ajustar segun el estandar de citacion del equipo. Ej: APA, Chicago, MLA, notas al pie. -->

- **Estandar de citacion por default**: autor + obra + anio + URL/localizador cuando aplique. No inventar ISBNs ni DOI.
- **Jerarquia de fuentes preferida** (de mayor a menor confianza):
  1. Fuentes primarias (documentos de epoca, archivos, periodicos contemporaneos al evento).
  2. Fuentes secundarias academicas con revision por pares.
  3. Fuentes secundarias divulgativas o enciclopedicas.
  4. Otras fuentes web. Marcar como `[verificar: fuente]` salvo evidencia clara de procedencia.
- **Marcador de no verificado**: toda afirmacion sin fuente trazable se marca como `[verificar: <campo>]` y no se presenta como hecho.
- **Anacronismos prohibidos**: no aplicar conceptos, categorias o instituciones modernas a un evento historico si no existian en su epoca. Si la proyeccion retroactiva es util, debe declararse explicitamente como interpretacion.
- **Cobertura geografica**: si la consulta menciona un pais, asumir que el evento ocurre en el territorio de ese pais salvo evidencia contraria.

## Matriz de escalacion

| Veredicto | Accion |
|---|---|
| VERDE | Hecho documentado por una fuente primaria o dos o mas fuentes secundarias coincidentes. Aceptable para borrador sin escalacion. |
| AMARILLO | Hecho apoyado por una sola fuente secundaria, o fuentes secundarias con diferencias menores. Requiere revision humana antes de publicar. |
| ROJO | Hecho sin fuente trazable, o fuentes contradictorias, o afirmacion que cae fuera del alcance del evento. Escalar al investigador responsable. Bloquear presentacion como hecho. |

<!-- EDITAR PARA TU EQUIPO: definir quien es el "investigador responsable" para escalaciones ROJO y el flujo de aprobacion cuando la skill entregue un borrador. -->

## Guardrails adicionales a los globales

Ademas de los guardrails globales del `CLAUDE.md` raiz:

1. **Nunca presentar interpretacion como hecho.** Si el output es un analisis, la seccion de analisis debe estar visualmente separada de la seccion de hechos documentados.
2. **Marcador `[verificar]` obligatorio** en toda afirmacion sin fuente. Sin fuente → no se afirma como hecho.
3. **No inventar fechas, cifras ni nombres.** Si la cifra o el dato es incierto, marcar `[verificar: cifra]` y proponer el rango o la fuente donde encontrarlo.
4. **No comprometer el rigor por longitud.** Es preferible un resumen corto y verificado a uno largo con afirmaciones sin fuente.
5. **Trazabilidad en el output.** El output final debe permitir al lector remontar cada afirmacion a su fuente sin volver a preguntar al agente.

## Skills incluidas

- `venezuela-history` — investigacion especializada en historia de Venezuela, con borradores de resumenes y analisis verificables. Ver `skills/venezuela-history/SKILL.md`.

## Limitaciones importantes

- **Alcance tematico acotado por skill.** Esta primera implementacion cubre historia de Venezuela. Otras geografias o epocas requeriran skills adicionales en futuras versiones.
- **Fuentes digitales preferidas.** El plugin asume que las fuentes son localizables digitalmente (URL, DOI, periodicos digitalizados, repositorios). Fuentes exclusivamente impresas en archives fisicos quedan fuera del alcance automatico.
- **No sustituye revision por pares.** El output es un borrador estructurado. La validacion academica definitiva queda fuera de scope.
- **Cobertura idiomatica.** Espanol por default; consultas en otros idiomas se atienden pero pueden requerir fuentes adicionales.