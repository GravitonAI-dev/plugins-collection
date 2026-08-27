# Gestoria

Plugin de GravitonAI para la preparacion de tramites administrativos de gestoria en Espana, verificando siempre la normativa y las tasas vigentes en el BOE y en la sede de cada organismo. Genera la solicitud o escrito, la hoja de datos para el formulario oficial y el checklist de documentos, tasas y organismo de presentacion.

Salida en DRAFT markdown para revision profesional en el editor. La presentacion telematica automatica se abordara mas adelante (conectores por API y presentacion asistida por navegador con firma humana).

---

## Que hace

- Prepara el cambio de titularidad de vehiculo ante la DGT y la notificacion de venta.
- Prepara el alta y la baja de autonomo (censo AEAT 036 y RETA de la Seguridad Social).
- Prepara altas y bajas en la Seguridad Social (afiliacion/NUSS, empresa y CCC, trabajadores del Regimen General, empleadas de hogar).
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

### `alta-baja-autonomo`

Prepara el alta y la baja de autonomo: alta y baja censal en la AEAT (modelo 036) y alta y baja en el RETA de la Seguridad Social por rendimientos reales (Ley 20/2007, RD-ley 13/2022).

Invocacion: `/gestoria:alta-baja-autonomo`

Inputs: tipo de operacion (alta / baja); datos del interesado; actividad y epigrafe IAE; fecha de inicio o de cese; rendimientos netos previstos (para el tramo); regimen de IVA e IRPF; tarifa plana; domicilio de la actividad.

Output: hojas de datos del alta o baja censal (036) y del alta o baja en RETA (con cuota estimada en el alta) y checklist de documentos, sedes y plazos, en markdown, DRAFT.

### `alta-baja-seguridad-social`

Prepara altas y bajas en la Seguridad Social por el lado del empleador y del Regimen General (LGSS, RD 84/1996): afiliacion inicial / NUSS (TA.1), inscripcion de empresa y CCC (TA.6), alta y baja de trabajadores por cuenta ajena (Sistema RED / Import@ss) y empleadas de hogar.

Invocacion: `/gestoria:alta-baja-seguridad-social`

Inputs: tipo de operacion (alta / baja); sujeto (afiliacion inicial / empresa / trabajador / empleada de hogar); datos del empleador (CIF, CCC); datos del trabajador (nombre, NIF, NUSS, grupo de cotizacion); fecha de efectos; tipo de contrato.

Output: hoja de datos del modelo TA correspondiente, checklist de documentos, organismo (TGSS) y via (Import@ss / Sistema RED) y plazos, en markdown, DRAFT.

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

### Servidores MCP

Ninguno por ahora. La presentacion telematica (conectores por API y presentacion asistida por navegador) se abordara mas adelante.

---

## Instalacion

```
/plugin marketplace add ./gestoria
```
