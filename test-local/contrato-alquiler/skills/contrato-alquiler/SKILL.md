---
name: contrato-alquiler
description: >
  Genera un contrato de alquiler (vivienda habitual o local de negocio) conforme a la Ley 29/1994
  de Arrendamientos Urbanos (LAU) en su version consolidada vigente verificada en el BOE, navegando
  un arbol de decision de preguntas textuales que enruta la recogida de datos y activa los bloques
  condicionales del asset. NO usar para finca rustica, viviendas turisticas, contratos de temporada,
  viviendas militares, viviendas de porteros/guardas, ni para revisar contratos de terceros.
when_to_use: |
  - El usuario quiere redactar un contrato de alquiler de vivienda o local.
  - El usuario proporciona (o pedira que se le pregunten) los datos de las partes y el inmueble.
  - El usuario pide un contrato que cumpla la LAU.
inputs:
  - respuestas al arbol de decision (una por nodo)
  - datos_partes: nombre/razon social, NIF/CIF, domicilio de arrendador y arrendatario
  - datos_inmueble: direccion, referencia catastral, descripcion, CCAA, municipio
  - condiciones_economicas: renta, duracion, fianza, actualizacion, gastos
outputs:
  - contrato_alquiler: contrato completo en markdown, DRAFT, con los bloques activados segun el arbol
references: []
assets:
  - assets/contrato-alquiler.md
---

# Generar Contrato de Alquiler (con arbol de decision)

> DRAFT — para revision por un abogado antes de su firma. No constituye asesoramiento juridico.

## Guardrails

1. Verificar la LAU en el BOE antes de redactar (Paso 1). No proceder sin verificacion.
2. Nunca incluir clausulas nulas de pleno derecho (Art. 6 LAU).
3. Si el municipio es zona tensionada, aplicar los limites de renta (Art. 17.6 y 17.7 LAU) y advertir.
4. Arrendador persona juridica en vivienda: duracion minima 7 anos; persona fisica: 5 anos. Nunca reducir.
5. Nunca omitir la fianza legal minima (Art. 36 LAU).
6. Gastos de gestion y formalizacion siempre a cargo del arrendador (Art. 20.1 LAU).
7. Marcar los campos no proporcionados como `[DATO — PENDIENTE DE COMPLETAR]`. Nunca inventar datos.
8. Recorrer el arbol de decision de forma estricta: no saltar nodos ni redactar antes de llegar a una hoja.

## Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO)

Antes de cualquier pregunta al usuario:

1.1 Leer la version registrada localmente (ultima modificacion conocida de la LAU).
1.2 Consultar la fuente oficial:
```
read_document(path: "https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003", format: "text")
```
1.3 Comparar fecha/redaccion oficial con la registrada.
1.4 Si hay version posterior, actualizar el asset y notificar al usuario antes de redactar.
1.5 Fallback si la fuente falla:
```
web_search("Ley 29/1994 Arrendamientos Urbanos texto consolidado BOE ultima modificacion")
```
Si todo falla, usar la referencia local y advertir: "No se pudo verificar la LAU vigente; verificar manualmente antes de firmar."

## Paso 2 — ARBOL DE DECISION (preguntas textuales)

Formula al usuario, literalmente, la pregunta de cada nodo. Segun la respuesta, avanza al nodo indicado y anota que bloque del asset se activa. Si el usuario ya aporto un dato, no repitas la pregunta: registra la respuesta y avanza.

```
                                   [ N0 · TIPO DE INMUEBLE ]
                                             |
                    +------------------------+------------------------+
                    | A) vivienda habitual                            | B) local / uso distinto
                    v                                                 v
             [ N1V · ARRENDADOR ]                              [ N1L · ACTIVIDAD ]
                    |                                                 |
        +-----------+-----------+                                     v
        | fisica (min 5 anos)   | juridica (min 7 anos)        [ N2L · CESION ]
        v                       v                                     |
   [ N2V · ZONA TENSIONADA ] <--+                                     v
        |                                                     [ N3 · CONDICIONES ECONOMICAS ]
   +----+----+----+                                                   |
   | si | no | ns |                                                   v
   v    v    v    v                                          [ HOJA · GENERAR CONTRATO ]
 [ N3 · CONDICIONES ECONOMICAS ] --------------------------------------^
```

### N0 — Tipo de inmueble
Pregunta textual:
"El contrato es para: (A) vivienda habitual, o (B) local de negocio / uso distinto de vivienda?"
- A -> ir a N1V. Activar `BLOQUE vivienda`. `tipo_inmueble_titulo = VIVIENDA`.
- B -> ir a N1L. Activar `BLOQUE local`. `tipo_inmueble_titulo = LOCAL DE NEGOCIO`.

### N1V — Naturaleza del arrendador (solo vivienda)
Pregunta textual:
"El arrendador es persona fisica o persona juridica (empresa, sociedad)?"
- persona fisica -> `plazo_minimo = 5`. Ir a N2V.
- persona juridica -> `plazo_minimo = 7`; activar `BLOQUE arrendador_juridica`. Ir a N2V.

### N2V — Zona de mercado tensionado (solo vivienda)
Pregunta textual:
"El municipio esta declarado zona de mercado residencial tensionado? (si / no / no lo se)"
- si -> activar `BLOQUE zona_tensionada`. Ir a N3.
- no -> Ir a N3.
- no lo se -> invocar `web_search("zona mercado residencial tensionado [municipio] [comunidad autonoma]")`, comunicar el resultado y volver a resolver este nodo (si/no).

### N1L — Actividad del local (solo local)
Pregunta textual:
"Que actividad se ejercera en el local?"
- Registrar `actividad_local`. Ir a N2L.

### N2L — Cesion y subarriendo del local (solo local)
Pregunta textual:
"Se permitira al arrendatario ceder el contrato o subarrendar el local? (si, en los terminos del Art. 32 LAU / no)"
- Registrar la eleccion (el `BLOQUE local` de la clausula novena ya contempla el Art. 32). Ir a N3.

### N3 — Condiciones economicas (comun a ambas ramas)
Preguntas textuales, en bloque:
1. "Renta mensual pactada en euros?"
2. "Duracion del contrato en anos (o 'minimo legal')?"
3. "Fianza: numero de mensualidades (o 'segun ley')?"  -> validar minimo: 1 vivienda, 2 local (Art. 36.1 LAU).
4. "Indice de actualizacion de la renta (o 'segun ley')?"
5. "Los gastos generales (comunidad, IBI, seguro) van a cargo del arrendatario? (si -> activar `BLOQUE gastos_arrendatario` / no)"
6. "Se pacta alguna garantia adicional (aval, seguro de impago)? (si -> activar `BLOQUE garantia_adicional` / no)"
7. "Se incluyen elementos accesorios (garaje, trastero, mobiliario)? (si -> activar `BLOQUE accesorios` / no)"
Tras responder, ir a la HOJA.

### N4 — Datos de partes e inmueble (recogida final antes de la hoja)
Pregunta textual (en bloque): nombre/razon social, NIF/CIF y domicilio de arrendador y arrendatario; direccion completa, referencia catastral, descripcion, CCAA y municipio del inmueble; fecha de inicio.
Los datos no aportados quedan como `[DATO — PENDIENTE DE COMPLETAR]`.

## Paso 3 — Validacion en la hoja del arbol

Antes de generar, validar:
- Duracion >= plazo minimo segun N1V (5 o 7). Si es menor, aplicar prorroga obligatoria y advertir.
- Fianza >= minimo legal segun N0 (1 o 2 mensualidades). Si es menor, corregir y advertir.
- Si `BLOQUE zona_tensionada` activo: la renta no supera los limites del Art. 17.6 LAU. Advertir y pedir confirmacion.
- Ninguna clausula adicional contradice normas imperativas del Titulo II (vivienda) o III (local).

## Paso 4 — Generacion del contrato

Invocar:
```
draft_markdown(
  template_id: "contrato-alquiler",
  variables: { ...todas las respuestas del arbol... },
  active_blocks: [ ...lista de BLOQUE activados en el recorrido... ]
)
```
Rellenar los placeholders `{{...}}` con los datos reales. Eliminar del asset los `BLOQUE` no activados; conservar y desanotar los activados.

## Paso 5 — Entrega

Entregar el contrato con el header DRAFT, la fecha de verificacion normativa del Paso 1, y las advertencias finales del asset. Indicar que ruta del arbol se recorrio (p.ej. "N0-A -> N1V-fisica -> N2V-no -> N3 -> hoja").

## Como NO se usa esta skill

- No usar para revisar contratos existentes de terceros.
- No usar para finca rustica, viviendas turisticas ni contratos de temporada.
- No usar para consulta juridica sobre litigios: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| Litigio activo o previo entre las partes | Escalar via escalate_to_attorney |
| Clausulas no resolubles con la LAU | Escalar via escalate_to_attorney |
| Arrendatario en situacion de vulnerabilidad acreditada | Advertir y ofrecer escalacion |
| Duda sobre zona tensionada no resuelta por web_search | Recomendar consulta al ayuntamiento |
