---
name: transferencia-vehiculo
description: >
  Prepara el tramite de cambio de titularidad (transferencia) de un vehiculo usado ante la DGT y,
  en su caso, la notificacion de venta por el vendedor, conforme al Reglamento General de Vehiculos
  (RD 2822/1998, texto consolidado verificado en el BOE) y a la normativa de tasas vigente de la DGT.
  Genera el contrato de compraventa del vehiculo, la hoja de datos para la solicitud de cambio de
  titularidad, la notificacion de venta y el checklist de documentos, tasas y organismo, con aviso del
  ITP autonomico del vehiculo usado. NO usar para altas de vehiculo nuevo, matriculaciones, bajas,
  duplicados de permiso, transmisiones por herencia con adjudicacion pendiente, ni para vehiculos de
  compraventa profesional en regimen de existencias.
when_to_use: |
  - Un particular compra o vende un vehiculo usado y necesita cambiar la titularidad en la DGT.
  - El usuario quiere el contrato de compraventa del vehiculo y la hoja de datos del tramite.
  - El vendedor quiere notificar la venta a la DGT para dejar de figurar como titular.
  - El usuario pide el checklist de documentos, tasas y organismo para presentar la transferencia.
inputs:
  - rol_usuario: comprador que transfiere / vendedor que notifica venta / ambas partes
  - alcance: contrato + solicitud de cambio de titularidad / solo notificacion de venta / todo
  - datos_vehiculo: matricula, numero de bastidor (VIN), marca, modelo, fecha de primera matriculacion, tipo (turismo / ciclomotor / motocicleta / otro)
  - datos_vendedor: nombre o razon social, NIF o CIF, domicilio
  - datos_comprador: nombre o razon social, NIF o CIF, domicilio
  - precio: precio de venta pactado en euros y fecha de la transmision
  - comunidad_autonoma: comunidad autonoma del comprador a efectos del ITP
  - estado_itv: si el vehiculo tiene la ITV en vigor (si / no / no aplica)
outputs:
  - contrato_compraventa: contrato de compraventa del vehiculo en markdown, DRAFT
  - solicitud_cambio_titularidad: hoja de datos + checklist + organismo + tasa para la solicitud DGT, DRAFT
  - notificacion_venta: opcional, escrito de notificacion de venta del vendedor a la DGT, DRAFT
references:
  - references/dgt-cambio-titularidad.md
  - references/itp-vehiculos-usados.md
  - references/fuentes-y-tasas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/contrato-compraventa-vehiculo.md
  - assets/solicitud-cambio-titularidad-dgt.md
  - assets/notificacion-venta-dgt.md
---

# Preparar el Cambio de Titularidad de un Vehiculo (DGT)

> DRAFT — para revision por un gestor o profesional antes de su presentacion. No constituye asesoramiento juridico ni fiscal.

## Guardrails

1. Verificar siempre en el BOE el Reglamento General de Vehiculos (RD 2822/1998) y en la sede de la DGT las tasas vigentes antes de preparar el tramite. Sin verificacion, no proceder.
2. Si se detecta en el BOE o en la sede de la DGT una version del reglamento, del procedimiento o de las tasas posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 1). No usar una version desactualizada.
3. El cambio de titularidad exige que el vehiculo tenga la ITV en vigor (cuando le sea exigible) y que este al corriente del Impuesto sobre Vehiculos de Traccion Mecanica (IVTM). Si falta la ITV o hay recibos de IVTM impagados, advertir de que la DGT puede denegar el tramite.
4. La liquidacion previa del ITP (modelo 620) del vehiculo usado es requisito para la transferencia entre particulares. Nunca omitir el aviso del ITP ni afirmar que no aplica sin confirmar la comunidad autonoma y la existencia de exencion.
5. Indicar siempre el organismo (Sede Electronica DGT u oficina de Trafico, y Hacienda autonomica para el ITP), la tasa y los plazos aplicables.
6. Marcar todos los campos a rellenar segun el patron del asset. Nunca inventar matricula, bastidor, NIF, precio, fechas ni importes de tasa o impuesto.
7. Recordar al vendedor su obligacion de notificar la venta en plazo para dejar de figurar como titular y evitar responsabilidad por sanciones e impuestos posteriores.
8. El DRAFT no sustituye la revision por un gestor colegiado ni la presentacion ante el organismo competente.

## Procedimiento

### Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, antes de cualquier otra accion)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la fecha/version registrada localmente.** Abrir `references/fuentes-y-tasas.md` y anotar la "Version registrada" del Reglamento General de Vehiculos, del procedimiento de cambio de titularidad y de las tasas de la DGT.

**1.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826",
  format: "text"
)
```
Extraer: fecha del texto consolidado vigente del Reglamento General de Vehiculos; redaccion actual de los arts. 32 y 33 (transmision de la titularidad y plazos del comprador y del vendedor).

Consultar tambien el procedimiento y las tasas vigentes en la sede de la DGT:
```
read_document(
  path: "https://sede.dgt.gob.es/es/vehiculos/transferencias-de-vehiculos/",
  format: "text"
)
```

**1.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references. Comprobar en particular el importe vigente de la tasa de transferencia (turismo y ciclomotor) y de la tasa de notificacion de venta.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto/importe ha cambiado, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/dgt-cambio-titularidad.md` (procedimiento, documentos, plazos) y en `references/fuentes-y-tasas.md` (IDs BOE, importes de tasa, fechas).
- Si cambia la fiscalidad del vehiculo usado (Orden anual de precios medios, tipos autonomicos), actualizar `references/itp-vehiculos-usados.md`.
- Si cambia el formulario oficial o el modelo del tramite, actualizar la estructura de `assets/solicitud-cambio-titularidad-dgt.md`.
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-y-tasas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma o tasa, y fecha).

No preparar ningun documento hasta haber completado esta actualizacion.

**1.5 — Fallback si la fuente no es accesible.** Si `read_document` falla (error HTTP, timeout):
```
web_search("cambio de titularidad vehiculo DGT tasa transferencia importe vigente sede electronica")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la normativa/tasas de la DGT. El tramite se prepara con la version de referencia. Verificar el importe de la tasa y el procedimiento antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no prepara nada hasta recoger estos datos:

**Bloque A — Rol y alcance:**
"Actua como (1) comprador que transfiere el vehiculo a su nombre, (2) vendedor que quiere notificar la venta, o (3) ambas partes? Desea generar el contrato de compraventa, la solicitud de cambio de titularidad, la notificacion de venta, o todo?"

**Bloque B — Datos del vehiculo:**
- Matricula, numero de bastidor (VIN), marca, modelo y fecha de primera matriculacion.
- Tipo de vehiculo (turismo / ciclomotor / motocicleta / otro), a efectos de la tasa aplicable.

**Bloque C — Datos del vendedor:**
- Nombre completo o razon social, NIF/CIF y domicilio.

**Bloque D — Datos del comprador:**
- Nombre completo o razon social, NIF/CIF y domicilio.
- Comunidad autonoma del comprador (a efectos del ITP).

**Bloque E — Precio y fecha:**
- Precio de venta pactado en euros y fecha de la transmision.

**Bloque F — Estado del vehiculo:**
- ITV en vigor (si / no / no aplica).
- Situacion del IVTM (al corriente / desconocido).

### Paso 3 — Validacion de requisitos

Antes de preparar los documentos, validar:

a) **Titularidad transmisible.** Que el vehiculo no consta con reserva de dominio, precinto, embargo o baja. Si el usuario indica cargas, advertir de que pueden impedir la transferencia y ofrecer escalacion.

b) **ITV e IVTM.** Que la ITV este en vigor (cuando le sea exigible) y que el IVTM del ejercicio este pagado. Si falta cualquiera, advertir del riesgo de denegacion.

c) **ITP.** Confirmar la comunidad autonoma del comprador y advertir de que debe autoliquidarse el ITP (modelo 620) sobre el mayor valor entre el precio pactado y el valor de mercado del vehiculo, salvo exencion. Ver `references/itp-vehiculos-usados.md`.

d) **Plazos.** Recordar que el comprador dispone de 30 dias naturales desde la transmision para solicitar el cambio de titularidad, y el vendedor de 10 dias para notificar la venta (arts. 32-33 RGV).

### Paso 4 — Generacion de los documentos

Seleccionar los assets segun el alcance del Bloque A:
- Contrato de compraventa: `assets/contrato-compraventa-vehiculo.md`
- Solicitud de cambio de titularidad (hoja de datos + checklist + organismo + tasa): `assets/solicitud-cambio-titularidad-dgt.md`
- Notificacion de venta del vendedor: `assets/notificacion-venta-dgt.md`

Invocar por cada documento pedido:
```
draft_markdown(
  template_id: "contrato-compraventa-vehiculo" | "solicitud-cambio-titularidad-dgt" | "notificacion-venta-dgt",
  variables: {
    todos los datos recogidos en los bloques A-F
  }
)
```

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado quedan con el marcador del asset, sin inventar valores.

Aplicar el estilo de `references/estilo-redaccion-escritos.md`: escrito administrativo breve, datos en tablas, encabezamiento al organismo, expone y solicita, sin formulas grandilocuentes.

### Paso 5 — Revision final y advertencias

Verificar que cada documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Identifica correctamente el vehiculo (matricula y bastidor), al vendedor y al comprador.
- Indica el organismo, la tasa aplicable y los plazos.

Entregar los documentos y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un gestor o profesional antes de su presentacion.
2. Version del Reglamento General de Vehiculos y tasas verificada: [fecha extraida en Paso 1].
3. El comprador dispone de 30 dias naturales desde la transmision para solicitar el cambio de titularidad; el vendedor de 10 dias para notificar la venta (arts. 32-33 RGV).
4. Antes de la transferencia debe autoliquidarse el ITP (modelo 620) en la Hacienda autonomica del comprador, salvo exencion.
5. El vehiculo debe tener la ITV en vigor (cuando le sea exigible) y el IVTM del ejercicio pagado.
6. Tasa DGT de transferencia y organismo: ver la hoja de datos generada. La presentacion se realiza en la Sede Electronica de la DGT o en oficina de Trafico con cita previa.
```

## Como NO se usa esta skill

- No usar para matriculacion de vehiculo nuevo, baja definitiva o temporal, ni duplicado de permiso de circulacion.
- No usar para transmisiones por herencia mientras la adjudicacion no este resuelta (procede antes la particion; derivar a la skill de sucesiones o a un profesional).
- No usar para vehiculos de compraventa profesional en regimen de existencias (transmision a compraventa autorizada, art. 33 RGV): advertir y derivar.
- No usar para calcular con caracter definitivo el ITP: la skill avisa y estima, pero el importe debe verificarse en la Hacienda autonomica.
- No usar para recurrir una denegacion o una sancion asociada al vehiculo: derivar a un gestor colegiado o abogado.

## Escalacion

| Situacion | Accion |
|---|---|
| Vehiculo con embargo, reserva de dominio, precinto o baja | Advertir que puede impedir la transferencia y ofrecer escalacion |
| ITV caducada o IVTM impagado | Advertir del riesgo de denegacion y recomendar regularizar antes |
| Transmision por herencia o con varios titulares en disputa | Derivar a la particion / a un profesional |
| Duda sobre el tipo de ITP o exencion en la comunidad autonoma | Verificar con web_search y advertir; no fijar el importe como definitivo |
| Denegacion previa del tramite o sancion asociada | Advertir y derivar a un gestor colegiado |
