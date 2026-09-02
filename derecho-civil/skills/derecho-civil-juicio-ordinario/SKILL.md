---
name: derecho-civil-juicio-ordinario
description: >
  Prepara de principio a fin un juicio ordinario civil conforme a la Ley de Enjuiciamiento Civil (LEC)
  en su version consolidada vigente verificada en el BOE. Cubre el ciclo completo por fases y genera el
  documento de cada una: intake del caso, comprobacion de admisibilidad (ambito del Art. 249, cuantia,
  competencia, postulacion de abogado y procurador, y requisito de MASC de la LO 1/2025), demanda del
  Art. 399 con sus documentos, guion de la audiencia previa (Arts. 414-430), proposicion de prueba
  (Art. 429 y 281-386) y minuta de conclusiones (Art. 433). NO usar para asuntos atribuidos al juicio
  verbal por la materia o por cuantia igual o inferior a 15.000 euros, para procesos especiales
  (familia, sucesiones contenciosas, division de patrimonios, monitorio, cambiario), ni para redactar
  la contestacion, la reconvencion o los recursos del demandado.
when_to_use: |
  - El usuario quiere demandar en un juicio ordinario civil (cuantia superior a 15.000 euros o materia del Art. 249.1).
  - El usuario necesita determinar si su asunto se tramita por juicio ordinario y preparar la demanda.
  - El usuario esta en un juicio ordinario ya iniciado y necesita el guion de la audiencia previa, la proposicion de prueba o las conclusiones.
  - El usuario pide una demanda de juicio ordinario del Art. 399 LEC con sus documentos.
inputs:
  - fase: intake / admisibilidad / demanda / audiencia-previa / proposicion-prueba / conclusiones (o ciclo completo)
  - materia: descripcion de la pretension y de la accion que se ejercita
  - via_ordinario: por la materia (Art. 249.1) / por la cuantia (Art. 249.2, superior a 15.000 euros)
  - naturaleza_actor: persona fisica o persona juridica
  - datos_actor: nombre o razon social, NIF o CIF, domicilio a efectos de notificaciones
  - naturaleza_demandado: persona fisica o persona juridica
  - datos_demandado: nombre o razon social, NIF o CIF, domicilio donde pueda ser emplazado
  - hechos: relato ordenado de los hechos en que se funda la pretension
  - cuantia: interes economico de la demanda y su justificacion (Arts. 251-253)
  - documentos: documentos fundamentales de la accion y dictamenes periciales disponibles (Arts. 265, 336)
  - partido_judicial: fuero aplicable (domicilio del demandado, lugar del inmueble, domicilio del consumidor, etc.)
  - postulacion: datos del procurador y del abogado (preceptivos, Arts. 23 y 31)
  - masc_intentado: si se ha intentado un medio adecuado de solucion de controversias (si / no)
  - hechos_controvertidos: solo para audiencia previa, prueba y conclusiones; hechos discutidos por el demandado
outputs:
  - checklist_admisibilidad: comprobacion de ambito, cuantia, competencia, postulacion y MASC, en markdown, DRAFT
  - demanda_juicio_ordinario: demanda del Art. 399 LEC en markdown, DRAFT
  - guion_audiencia_previa: guion / escrito de preparacion de la audiencia previa en markdown, DRAFT
  - proposicion_prueba: proposicion de prueba ordenada por medios en markdown, DRAFT
  - escrito_conclusiones: minuta de conclusiones (Art. 433) en markdown, DRAFT
references:
  - references/lec-ambito-y-cuantia.md
  - references/admisibilidad-competencia-postulacion-masc.md
  - references/lec-demanda-y-documentos.md
  - references/lec-audiencia-previa.md
  - references/lec-prueba-y-conclusiones.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/checklist-admisibilidad.md
  - assets/demanda-juicio-ordinario.md
  - assets/guion-audiencia-previa.md
  - assets/proposicion-de-prueba.md
  - assets/escrito-de-conclusiones.md
---

# Preparar un Juicio Ordinario Civil (ciclo completo)

> DRAFT — para revision por un abogado antes de su presentacion. No constituye asesoramiento juridico.

## 0. CONFIRMACION DE CARGA Y ARRANQUE (visible, una sola vez)

Al cargarse esta skill, lo PRIMERO que emites en el chat, antes de cualquier otro texto, es esta linea fija:

**Skill cargada satisfactoriamente.**

A continuacion, en el MISMO mensaje y sin esperar ninguna confirmacion del usuario, ARRANCAS la ejecucion del procedimiento: emite la introduccion fija que la skill defina y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa. Si el procedimiento arranca con una verificacion normativa interna, ejecutala en silencio y continua hasta la primera pregunta o hasta la Confirmacion visible, segun corresponda.

PROHIBIDO detenerse tras la linea de carga, preguntar si desea empezar, o emitir la linea a solas en un turno propio: la skill queda cargada y en ejecucion en ese mismo turno.

Esta linea es, junto con la introduccion fija, la UNICA excepcion a la prohibicion de mencionar la mecanica interna. Se emite una sola vez, al cargar, y no se repite en ningun turno posterior.

## Guardrails

1. Verificar siempre la LEC en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version de la LEC posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 1). No usar una version desactualizada. El umbral de cuantia (15.000 euros desde el 20/03/2024, RDL 6/2023) y el requisito de MASC (LO 1/2025) han cambiado recientemente: confirmar siempre la redaccion vigente.
3. Determinar correctamente la clase de juicio: procede el ordinario por la materia (Art. 249.1) o por cuantia superior a 15.000 euros o de interes incalculable (Art. 249.2). Si el asunto corresponde al juicio verbal (materia del Art. 250.1 o cuantia igual o inferior a 15.000 euros), no usar esta skill: advertir y derivar.
4. Postulacion preceptiva: en el juicio ordinario son obligatorios abogado y procurador (Arts. 23 y 31). Nunca redactar la demanda como si pudiera presentarse sin ellos.
5. Competencia: identificar el fuero aplicable (Arts. 45, 50-52). No admitir sumision en fueros imperativos (inmuebles, consumidores). Marcar la jurisdiccion asumida.
6. Posicion conservadora sobre el MASC: la LO 1/2025 exige acreditar el intento previo de un medio adecuado de solucion de controversias como requisito de procedibilidad (Art. 403.2 LEC). Ante la duda, recomendar e integrar el intento previo y advertir de la cuestion (riesgo de inadmision, Art. 403.2).
7. Documentos y preclusion: advertir SIEMPRE de que los documentos fundamentales de la accion y los dictamenes periciales deben acompanarse con la demanda (Arts. 265, 336) y de la preclusion del Art. 269. No admitir aportacion tardia salvo los supuestos del Art. 270.
8. Carga de la prueba (Art. 217): al preparar la prueba y las conclusiones, atribuir a cada parte la carga que le corresponde. Nunca afirmar que un hecho esta probado sin base en las pruebas practicadas.
9. Los campos a rellenar usan el placeholder propio del asset en doble llave, p. ej. `{{cuantia_reclamada}}` (NUNCA corchete simple `[DATO]`: colisiona con los identificadores de privacidad `[PERSON_1]`). Si hace falta marcar un hueco suelto sin placeholder propio, usa `{{DATO_FALTANTE}}` una sola vez por documento: nunca lo repitas para dos datos distintos, porque el `Edit` posterior necesita un `oldString` unico. Nunca inventar datos, cuantias, fechas ni referencias catastrales. Nunca inventar jurisprudencia.

## Procedimiento

El procedimiento recorre el ciclo completo del juicio ordinario en seis fases. El usuario puede pedir el ciclo entero o solo la fase que necesite; en todo caso, el Paso 1 (verificacion normativa) se ejecuta SIEMPRE antes de generar cualquier documento.

### Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, antes de cualquier otra accion)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la fecha/version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" de la LEC, el umbral de cuantia registrado (15.000 euros) y el estado de la LO 1/2025.

**1.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-2000-323",
  format: "text"
)
```
Extraer: fecha del texto consolidado vigente de la LEC; redaccion actual de los arts. 248-255 (ambito y cuantia), 23 y 31 (postulacion), 45 y 50-52 (competencia), 399 y 264-266, 269-270, 336 (demanda y documentos), 414-430 (audiencia previa), 217 y 281-386, 429 (prueba) y 433 (conclusiones); el umbral vigente de cuantia entre juicio verbal y ordinario; y el estado de aplicacion de la LO 1/2025 (BOE-A-2025-76) sobre el requisito de MASC (arts. 403.2, 264.4 y 399.3).

**1.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references. Prestar especial atencion a: (i) el importe del umbral de cuantia del Art. 249.2; (ii) la vigencia y el alcance del requisito de MASC; (iii) la redaccion de los ordinales del Art. 249.1.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/lec-ambito-y-cuantia.md`, `references/admisibilidad-competencia-postulacion-masc.md`, `references/lec-demanda-y-documentos.md`, `references/lec-audiencia-previa.md` y/o `references/lec-prueba-y-conclusiones.md` con la redaccion vigente.
- Ajustar la estructura de los assets si cambian los tramites (p. ej. plazos, fases de la audiencia previa, forma de proponer la prueba, umbral de cuantia).
- Actualizar la tabla "Version registrada" y el umbral de cuantia en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_document` falla (error HTTP, timeout):
```
web_search("Ley Enjuiciamiento Civil juicio ordinario articulo 249 399 audiencia previa 414 texto consolidado BOE")
```
y
```
web_search("LO 1/2025 MASC requisito procedibilidad articulo 403 264 399 LEC texto consolidado")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LEC en el BOE. Los documentos se generan con la version de referencia. Verificar manualmente antes de presentar."

### Paso 2 — FASE 1: INTAKE del caso (una pregunta por bloque si no las ha proporcionado)

El agente no redacta nada hasta recoger estos datos. Preguntar primero que fase o fases necesita el usuario (intake, admisibilidad, demanda, audiencia previa, proposicion de prueba, conclusiones, o ciclo completo).

**Bloque A — Objeto y accion:** que se reclama y cual es la accion que se ejercita (p. ej. resolucion de contrato con indemnizacion, reclamacion de cantidad superior a 15.000 euros, responsabilidad contractual o extracontractual, nulidad, propiedad, etc.).

**Bloque B — Datos del actor (demandante):** nombre o razon social, NIF/CIF, domicilio a efectos de notificaciones; persona fisica o juridica (si juridica, datos del representante).

**Bloque C — Datos del demandado:** nombre o razon social, NIF/CIF si se conoce, domicilio o lugar donde pueda ser emplazado.

**Bloque D — Hechos:** relato cronologico y ordenado de los hechos, con indicacion de los documentos que los acreditan.

**Bloque E — Cuantia:** interes economico de la demanda y como se calcula (Arts. 251-253). Si es incalculable, justificarlo.

**Bloque F — Documentos y periciales:** documentos fundamentales de la accion disponibles y si se aportara dictamen pericial (Art. 336).

**Bloque G — Postulacion:** datos del procurador y del abogado que intervienen (preceptivos, Arts. 23 y 31).

**Bloque H — MASC (procedibilidad):** "Se ha intentado ya algun medio adecuado de solucion de controversias (negociacion, mediacion, conciliacion) antes de demandar? (si / no)". Si responde "no", advertir de que la LO 1/2025 lo exige como requisito de admisibilidad (Art. 403.2 LEC) y recomendar realizarlo antes de presentar.

Para las fases de audiencia previa, prueba y conclusiones, recoger ademas los **hechos controvertidos** (los negados o discutidos por el demandado en su contestacion).

### Paso 3 — FASE 2: ADMISIBILIDAD y preparacion previa

Antes de redactar la demanda, completar la comprobacion de admisibilidad (asset `checklist-admisibilidad.md`) validando:

a) **Clase de juicio (Art. 249):** confirmar que procede el ordinario, por la materia (Art. 249.1) o por cuantia superior a 15.000 euros o interes incalculable (Art. 249.2). Si corresponde al verbal, no procede esta skill: advertir y derivar (para reclamaciones de renta o desahucio, derivar a `derecho-civil-desahucio`; para deuda dineraria liquida por monitorio, a `derecho-civil-monitorio`).

b) **Determinacion de la cuantia (Arts. 251-253):** fijar el interes economico y justificarlo. La cuantia se expresa en la demanda (Art. 253).

c) **Competencia (Arts. 45, 50-52):** identificar el organo (Juzgado de Primera Instancia o, en su caso, de lo Mercantil) y el fuero territorial. Advertir de los fueros imperativos (inmuebles, consumidores) donde no cabe sumision.

d) **Postulacion (Arts. 23 y 31):** confirmar que se cuenta con procurador y abogado. Sin ellos, no puede seguirse el ordinario.

e) **MASC (Art. 403.2, 264.4, 399.3 — LO 1/2025):** confirmar el intento previo o la concurrencia de una excepcion. Por defecto conservador, recomendar acreditar el intento previo para evitar la inadmision.

f) **Documentos (Arts. 264-266, 336) y preclusion (Art. 269):** verificar que se dispone de los documentos fundamentales y de los dictamenes periciales para acompanarlos con la demanda.

### Paso 4 — FASE 3: DEMANDA de juicio ordinario (Art. 399)

Generar la demanda con el asset `demanda-juicio-ordinario.md`. Invocar:
```
draft_markdown(
  template_id: "demanda-juicio-ordinario",
  variables: { todos los datos recogidos en las fases 1 y 2 }
)
```
La demanda debe: identificar a las partes y la postulacion; exponer los HECHOS numerados y separados, relacionando cada documento (Documento nº 1, nº 2, ...); ordenar los FUNDAMENTOS DE DERECHO procesales (competencia, procedimiento, cuantia, postulacion, procedibilidad-MASC) y de fondo (la accion); fijar expresamente la CUANTIA; formular un SUPLICO concreto; y anadir los OTROSIES (recibimiento a prueba, designacion de domicilios). Aplicar el estilo de `references/estilo-redaccion-escritos.md`.

Los campos que el usuario no haya proporcionado conservan el placeholder propio del asset en doble llave (nunca corchete simple).

### Paso 5 — FASE 4: AUDIENCIA PREVIA (Arts. 414-430)

Cuando el usuario lo pida (proceso ya trabado con contestacion), generar el guion con el asset `guion-audiencia-previa.md`. El guion ordena, en el orden legal: (i) posicion ante un eventual acuerdo o transaccion (Art. 415); (ii) cuestiones procesales a plantear o a las que responder —capacidad, litisconsorcio, cosa juzgada, inadecuacion de procedimiento, defecto legal— (Arts. 416-425); (iii) alegaciones complementarias y aclaratorias sin alterar la pretension (Art. 426) y fijacion de hechos controvertidos (Arts. 427-428); (iv) anticipo de la prueba a proponer (Art. 429). Advertir de la prohibicion de mutatio libelli.

### Paso 6 — FASE 5: PROPOSICION DE PRUEBA (Art. 429 y 281-386)

Generar la proposicion con el asset `proposicion-de-prueba.md`, ordenando los medios de prueba (Art. 299): interrogatorio de partes, documental, testifical, pericial, reconocimiento judicial y medios de reproduccion. Para cada medio, justificar su pertinencia y utilidad respecto de los hechos controvertidos y precisar lo necesario (identidad de testigos, objeto de la pericial, documentos). Recordar la regla de carga de la prueba (Art. 217).

### Paso 7 — FASE 6: ESCRITO DE CONCLUSIONES (Art. 433)

Tras la practica de la prueba, generar la minuta con el asset `escrito-de-conclusiones.md`, que enlaza cada hecho controvertido con la prueba practicada, aplica la carga de la prueba (Art. 217) a los hechos dudosos y resume los fundamentos juridicos sin alterar la causa de pedir. Advertir de que el Art. 433 preve conclusiones orales; la minuta es material de apoyo del letrado en la vista.

### Paso 8 — Revision final y advertencias

Verificar que cada documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Identifica correctamente a las partes, el organo competente y la postulacion.
- Fija con claridad la cuantia y la clase de juicio, y relaciona los documentos.
- Sigue el estilo de redaccion judicial clara (hechos y fundamentos numerados, una idea por parrafo).

Entregar los documentos y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado antes de su presentacion.
2. Version de la LEC verificada: [fecha extraida en Paso 1]. Umbral de cuantia verbal/ordinario aplicado: [importe].
3. En el juicio ordinario son preceptivos abogado y procurador (Arts. 23 y 31 LEC).
4. La LO 1/2025 exige acreditar el intento previo de un MASC como requisito de admisibilidad (Art. 403.2 LEC). Conservar el justificante o la declaracion responsable (Art. 264.4).
5. Los documentos fundamentales y los dictamenes periciales deben acompanarse con la demanda (Arts. 265, 336 LEC); rige la preclusion del Art. 269.
6. La cuantia determina la clase de juicio y debe expresarse justificadamente (Arts. 251-253 LEC).
7. En la audiencia previa no cabe alterar sustancialmente la pretension (prohibicion de mutatio libelli, Art. 412).
```

## Como NO se usa esta skill

- No usar para asuntos atribuidos al juicio verbal por la materia (Art. 250.1) ni por cuantia igual o inferior a 15.000 euros.
- No usar para el desahucio ni la reclamacion de rentas: derivar a la skill `derecho-civil-desahucio` (o `derecho-civil-monitorio` para deuda dineraria liquida).
- No usar para procesos especiales: capacidad, filiacion, matrimonio y menores, division judicial de patrimonios, particion de herencia contenciosa, monitorio, cambiario.
- No usar para redactar la contestacion a la demanda, la reconvencion ni los recursos del demandado.
- No usar si el usuario pide opinion juridica sobre la viabilidad o la estrategia del litigio: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| Asunto de cuantia igual o inferior a 15.000 euros o de materia del Art. 250.1 | Advertir que procede juicio verbal y derivar a la skill correspondiente |
| Materia atribuida a proceso especial (familia, sucesiones contenciosas, division de patrimonios) | Advertir que no procede el ordinario y escalar |
| Duda sobre la exigencia del MASC en el caso concreto | Advertir y recomendar confirmar el criterio del partido judicial competente |
| Duda sobre la clase de juicio, la competencia o la determinacion de la cuantia | Usar web_search para verificar y, si persiste, escalar via escalate_to_attorney |
| Litisconsorcio necesario, acumulacion compleja o reconvencion previsible | Escalar via escalate_to_attorney |
| Caso con componente penal, medidas cautelares urgentes o litigio conexo activo | Escalar a abogado via escalate_to_attorney |
