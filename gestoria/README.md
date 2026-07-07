# Gestoria

Plugin de GravitonAI para la preparacion de tramites administrativos de gestoria en Espana, verificando siempre la normativa y las tasas vigentes en el BOE y en la sede de cada organismo. Genera la solicitud o escrito, la hoja de datos para el formulario oficial y el checklist de documentos, tasas y organismo de presentacion.

Salida en DRAFT markdown para revision profesional en el editor. La presentacion telematica automatica se abordara mas adelante (conectores por API y presentacion asistida por navegador con firma humana).

---

## Que hace

- Prepara el cambio de titularidad de vehiculo ante la DGT y la notificacion de venta.
- Prepara el alta de autonomo (censo AEAT 036 e alta en el RETA de la Seguridad Social).
- Prepara la autoliquidacion del Impuesto de Sucesiones (modelo 650) y avisa de la plusvalia municipal.
- Prepara la solicitud de NIE o de autorizacion de residencia (formularios EX, tasa 790).
- Verifica la normativa, los modelos y las tasas vigentes en el BOE y auto-actualiza sus references si detecta una version posterior.

## Que NO hace

- No presta asesoramiento juridico ni redacta demandas (para eso, los plugins de derecho).
- No presenta todavia los tramites de forma automatica; genera el DRAFT e indica el organismo y la via.
- No calcula con caracter definitivo cuotas ni impuestos: los importes se entregan como estimacion y deben verificarse.
- No sustituye la revision por un gestor colegiado o profesional competente.

---

## Skills

### `transferencia-vehiculo`

Prepara el cambio de titularidad de un vehiculo usado ante la DGT y, en su caso, la notificacion de venta (RD 2822/1998). Genera el contrato de compraventa, la hoja de datos de la solicitud, la notificacion de venta y el checklist de documentos, tasa y organismo, con aviso del ITP autonomico.

Invocacion: `/gestoria:transferencia-vehiculo`

Inputs: rol (comprador / vendedor / ambos); datos del vehiculo (matricula, bastidor, marca, modelo, fecha 1a matriculacion); datos de vendedor y comprador; precio y fecha; comunidad autonoma (ITP); estado de la ITV.

Output: contrato de compraventa, solicitud de cambio de titularidad (hoja de datos + checklist + tasa) y notificacion de venta, en markdown, DRAFT.

### `alta-autonomo`

Prepara el alta de autonomo: alta censal en la AEAT (modelo 036) y alta en el RETA de la Seguridad Social por rendimientos reales (Ley 20/2007, RD-ley 13/2022).

Invocacion: `/gestoria:alta-autonomo`

Inputs: datos del interesado; actividad y epigrafe IAE; fecha de inicio; rendimientos netos previstos (para el tramo); regimen de IVA e IRPF; tarifa plana; domicilio de la actividad.

Output: hoja de datos del alta censal (036) y del alta en RETA (con cuota estimada) y checklist de documentos, sedes y plazos, en markdown, DRAFT.

### `liquidacion-impuesto-sucesiones`

Prepara la autoliquidacion del Impuesto de Sucesiones (modelo 650, mortis causa) de un heredero (Ley 29/1987 y normativa autonomica). Complementa a `particion-herencia` de derecho-civil (el cuaderno juridico); esta hace la liquidacion fiscal.

Invocacion: `/gestoria:liquidacion-impuesto-sucesiones`

Inputs: comunidad autonoma; datos del causante y del heredero (grupo I-IV); caudal hereditario (inventario y valores); cargas y deudas; seguros de vida; ajuar; vivienda habitual; empresa familiar; discapacidad.

Output: borrador del modelo 650 (base y cuota estimada, marcada para verificar) y checklist de documentacion, organismo y plazo (6 meses), en markdown, DRAFT. Avisa de la plusvalia municipal.

### `extranjeria-residencia`

Prepara la solicitud de NIE o de autorizacion de residencia (no lucrativa, arraigo, reagrupacion) ante la Oficina de Extranjeria (LOEX 4/2000 y RD 1155/2024). La resolucion es discrecional de la Administracion.

Invocacion: `/gestoria:extranjeria-residencia`

Inputs: tipo de tramite; datos del extranjero (nombre, nacionalidad, pasaporte); NIE previo; motivo; domicilio en Espana; datos de apoyo (medios economicos, seguro, reagrupante); lugar de presentacion.

Output: hoja de datos del formulario EX (con checklist, organismo y tasa 790) y escrito de solicitud, en markdown, DRAFT.

---

## Dependencias

### Tools requeridas

| ID | Uso |
|---|---|
| `io.gravitonai.tools.read_document` | Lectura en el BOE de la normativa de cada tramite (verificacion) |
| `io.gravitonai.tools.web_search` | Fallback normativo, tasas vigentes, modelos actualizados y especialidades autonomicas |
| `io.gravitonai.tools.draft_markdown` | Generacion de la solicitud, hoja de datos y checklist desde plantilla |

### Tools opcionales

| ID | Uso |
|---|---|
| `io.gravitonai.tools.escalate_to_attorney` | Derivacion a profesional en casos con sancion, litigio o denegacion |

### Servidores MCP

Ninguno por ahora. La presentacion telematica (conectores por API y presentacion asistida por navegador) se abordara mas adelante.

---

## Instalacion

```
/plugin marketplace add ./gestoria
```
