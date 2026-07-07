# Sucesiones

Plugin de GravitonAI para la generacion de documentos de derecho sucesorio espanol, verificando siempre la version consolidada vigente en el BOE: particion de herencia, aceptacion o renuncia de herencia y voluntades, con respeto de la legitima y aviso de las obligaciones fiscales.

---

## Que hace

- Genera el cuaderno particional / escritura de aceptacion y particion de herencia (inventario, avaluo, liquidacion y adjudicaciones).
- Genera el documento de aceptacion de herencia (pura y simple o a beneficio de inventario) y, en su caso, de renuncia.
- Respeta la legitima de los herederos forzosos (arts. 806-808 CC).
- Advierte del Impuesto de Sucesiones (autonomico, plazo de 6 meses) y de la plusvalia municipal.
- Verifica la normativa vigente en el BOE antes de redactar y actualiza sus references si detecta una version posterior.

## Que NO hace

- No redacta testamentos ni resuelve litigios sucesorios contenciosos.
- No sustituye la escritura notarial de particion ni la inscripcion registral.
- No liquida impuestos; solo advierte de ellos.
- No da opinion juridica concreta; el output siempre es un DRAFT para revision por abogado o notario.

---

## Skills

### `particion-herencia`

Genera el cuaderno particional o escritura de aceptacion y particion y el documento de aceptacion de herencia, para sucesion testada o intestada.

Invocacion: `/sucesiones:particion-herencia`

Inputs requeridos: tipo de documento; sucesion testada o intestada; datos del causante y titulo sucesorio; herederos y legitimarios; inventario de bienes y deudas; donaciones colacionables; modo de aceptacion; comunidad autonoma.

Output: cuaderno particional en markdown, DRAFT (y, opcionalmente, aceptacion de herencia).

Que NO hace: no redacta testamentos, no resuelve litigios sucesorios contenciosos ni sustituye la escritura notarial de particion.

---

## Dependencias

### Tools requeridas

| ID | Uso |
|---|---|
| `io.gravitonai.tools.read_document` | Lectura del Codigo Civil en el BOE (verificacion normativa) |
| `io.gravitonai.tools.web_search` | Fallback normativo y consulta del Impuesto de Sucesiones autonomico y derecho foral |
| `io.gravitonai.tools.draft_markdown` | Generacion del documento desde plantilla |

### Tools opcionales

| ID | Uso |
|---|---|
| `io.gravitonai.tools.escalate_to_attorney` | Escalacion a abogado en litigios sucesorios o casos complejos |

### Servidores MCP

Ninguno.

---

## Instalacion

```
/plugin marketplace add ./sucesiones
```
