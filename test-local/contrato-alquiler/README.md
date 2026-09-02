# Contrato de Alquiler (plugin de prueba)

Plugin de ejemplo generado con el Plugin & Skill Builder para probar el flujo end-to-end: creacion de skill con arbol de decision, casos de uso, test y catalogo.

## Que hace

Genera un contrato de alquiler (vivienda o local) conforme a la LAU, guiando la recogida de datos mediante un arbol de decision de preguntas textuales que determina que bloques del contrato se activan.

## Que NO hace

- No revisa contratos existentes de terceros.
- No cubre finca rustica, viviendas turisticas, militares ni de porteros/guardas.
- No sustituye la revision por un abogado colegiado.

## Skills

| Skill | Proposito |
|---|---|
| `contrato-alquiler` | Genera el contrato navegando un arbol de decision con preguntas textuales. |

## Dependencias

- Tools (catalogo global): `io.gravitonai.tools.read_document`, `io.gravitonai.tools.draft_markdown`, `io.gravitonai.tools.web_search`, `io.gravitonai.tools.escalate_to_attorney`.
- MCP: ninguno.

## Instalacion

Copiar la carpeta `contrato-alquiler/` a la raiz de un marketplace `plugins-collection` y registrar el plugin en `.claude-plugin/marketplace.json`.

## Tuning

Editar los marcadores `<!-- EDITAR PARA TU EQUIPO -->` en `CLAUDE.md` para ajustar jurisdiccion por defecto.
