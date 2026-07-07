# Derecho de Consumo

Plugin de GravitonAI para la generacion de documentos de derecho de consumo espanol, verificando siempre la version consolidada vigente en el BOE y la jurisprudencia reciente del TJUE y del Tribunal Supremo: reclamacion de clausulas abusivas y restitucion de cantidades, y reclamaciones de consumidores frente a empresas.

---

## Que hace

- Genera la reclamacion extrajudicial a la entidad o empresa por clausulas abusivas.
- Genera la demanda de nulidad de clausula abusiva con restitucion de cantidades e intereses.
- Cubre gastos de formalizacion de hipoteca, clausula suelo, IRPH, comision de apertura, interes de demora, tarjeta revolving u otras condiciones no negociadas.
- Verifica la normativa vigente en el BOE y la jurisprudencia reciente del TJUE y del Tribunal Supremo antes de redactar.

## Que NO hace

- No cubre contratos entre empresarios sin consumidor ni clausulas negociadas individualmente.
- No ejercita acciones colectivas ni de cesacion.
- No garantiza el resultado: la abusividad depende de la jurisprudencia vigente.
- No da opinion juridica concreta; el output siempre es un DRAFT para revision por abogado.

---

## Skills

### `reclamacion-clausulas-abusivas`

Genera la reclamacion extrajudicial a la entidad o empresa y/o la demanda de nulidad de clausula abusiva con restitucion de cantidades, en contratos con consumidores (TRLGDCU, LCGC, Directiva 93/13).

Invocacion: `/derecho-consumo:reclamacion-clausulas-abusivas`

Inputs requeridos: alcance (extrajudicial / demanda); tipo de clausula; datos del reclamante (consumidor) y del predisponente; datos del contrato y clausula impugnada; cantidades reclamadas; comunidad autonoma.

Output: reclamacion extrajudicial y/o demanda de nulidad con restitucion, en markdown, DRAFT.

Que NO hace: no cubre contratos entre empresarios sin consumidor, clausulas negociadas individualmente ni reclamaciones ajenas al derecho de consumo.

---

## Dependencias

### Tools requeridas

| ID | Uso |
|---|---|
| `io.gravitonai.tools.read_document` | Lectura del TRLGDCU, LCGC y LEC en el BOE (verificacion normativa) |
| `io.gravitonai.tools.web_search` | Fallback normativo y verificacion de jurisprudencia reciente del TJUE y del Tribunal Supremo |
| `io.gravitonai.tools.draft_markdown` | Generacion del documento desde plantilla |

### Tools opcionales

| ID | Uso |
|---|---|
| `io.gravitonai.tools.escalate_to_attorney` | Escalacion a abogado en acciones colectivas o casos complejos |

### Servidores MCP

Ninguno.

---

## Instalacion

```
/plugin marketplace add ./derecho-consumo
```
