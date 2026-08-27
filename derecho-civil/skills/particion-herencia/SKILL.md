---
name: particion-herencia
description: >
  Genera documentos de particion de herencia conforme al Codigo Civil (BOE-A-1889-4763) en su version
  consolidada vigente verificada en el BOE: cuaderno particional o escritura de aceptacion y particion
  (inventario, avaluo, liquidacion y adjudicaciones por heredero, con respeto de la legitima de los arts.
  806 a 808), y documento de aceptacion de herencia (pura y simple o a beneficio de inventario) con
  opcion de renuncia. Pregunta si la sucesion es testada o intestada, los herederos, el inventario de
  bienes y deudas y las legitimas, y advierte del Impuesto de Sucesiones (autonomico, plazo de 6 meses)
  y de la plusvalia municipal. NO usar para redactar testamentos, para litigios sucesorios contenciosos,
  ni para sustituir la escritura notarial de particion.
when_to_use: |
  - El usuario quiere repartir una herencia entre varios herederos y necesita el cuaderno particional.
  - El usuario dispone del titulo sucesorio (testamento o declaracion de herederos) y del inventario de bienes y deudas.
  - El usuario pide un documento de aceptacion de herencia (pura y simple o a beneficio de inventario) o de renuncia.
inputs:
  - tipo_documento: cuaderno particional / aceptacion de herencia / ambos
  - tipo_sucesion: testada (hay testamento) / intestada (sin testamento, declaracion de herederos)
  - datos_causante: nombre, NIF, fecha y lugar de fallecimiento, ultimo domicilio
  - titulo_sucesorio: testamento (notario, fecha, protocolo) o acta de declaracion de herederos
  - herederos: nombre, NIF, parentesco con el causante y cuota o institucion en cada caso
  - legitimarios: descendientes, ascendientes o conyuge viudo, y su legitima (arts. 807-808)
  - inventario_bienes: relacion de bienes (inmuebles, cuentas, valores, vehiculos, ajuar) con su valor
  - inventario_deudas: deudas y cargas de la herencia y gastos deducibles
  - donaciones_colacionables: bienes recibidos en vida por herederos forzosos (Art. 1035)
  - modo_aceptacion: pura y simple / a beneficio de inventario
  - comunidad_autonoma: para advertir de la normativa del Impuesto de Sucesiones aplicable
outputs:
  - cuaderno_particional: cuaderno particional / escritura de aceptacion y particion en markdown, DRAFT
  - aceptacion_herencia: opcional, documento de aceptacion (o renuncia) de herencia en markdown, DRAFT
references:
  - references/cc-sucesiones-y-legitima.md
  - references/cc-particion-herencia.md
  - references/impuesto-sucesiones-y-plazos.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/cuaderno-particional.md
  - assets/aceptacion-herencia.md
---

# Generar Documentos de Particion de Herencia

> DRAFT — para revision por un abogado y elevacion a escritura notarial antes de su firma. No constituye asesoramiento juridico ni fiscal.

## Guardrails

1. Verificar siempre el Codigo Civil en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version del Codigo Civil posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 1). No usar una version desactualizada.
3. Respeto absoluto de la legitima (Arts. 806 a 808 CC). No redactar una particion que perjudique la legitima de un heredero forzoso: advertir, recalcular y, si el usuario insiste, escalar. La legitima es intangible salvo las causas legales de desheredacion o preterision.
4. La particion definitiva de una herencia con bienes inmuebles suele requerir escritura publica notarial para su inscripcion en el Registro de la Propiedad. El documento generado es un borrador de trabajo, no sustituye la escritura.
5. Guardar la posible igualdad en los lotes y adjudicaciones (Art. 1061 CC); los bienes indivisibles se adjudican a un heredero abonando el exceso en dinero a los demas (Art. 1062 CC).
6. Nunca omitir la advertencia del Impuesto de Sucesiones y Donaciones (autonomico, plazo de 6 meses desde el fallecimiento) ni de la plusvalia municipal cuando haya inmuebles urbanos. Indicar que la normativa del ISD se verifique para la comunidad autonoma concreta.
7. Marcar todos los campos a rellenar con `[DATO]` en mayusculas. Nunca inventar bienes, valores, cuotas ni fechas.
8. Nunca afirmar cuotas hereditarias sin base en el titulo sucesorio (testamento o declaracion de herederos). Nunca inventar clausulas testamentarias ni jurisprudencia.

## Procedimiento

### Paso 1 — Verificacion normativa

**1.1 — Consultar la version registrada en references.** Consultar el archivo `fuentes-plantillas-validadas.md` directamente desde el bloque `<document kind="references-collection">` de tu system prompt (TIENES ESTRICTAMENTE PROHIBIDO usar la herramienta `read_file` para leer references o assets) y anotar la "Version registrada" del Codigo Civil.

**1.2 — Consultar la fuente oficial vigente en vivo.** Invocar:
```
web_search("BOE-A-1889-4763 Codigo Civil sucesiones legitima particion herencia articulos 806 808 1035 1087 texto consolidado")
```
Extraer: fecha del texto consolidado vigente del Codigo Civil; redaccion actual de los arts. 657 y ss. (apertura de la sucesion), 806 a 808 (legitima), 834 y ss. (derechos del conyuge viudo), 912 y ss. (ordenes de la sucesion intestada) y 1035 a 1087 (colacion y particion).

**1.3 — Comparar.** Contrastar la version oficial con la registrada en `fuentes-plantillas-validadas.md` y con las referencias del prompt (`cc-sucesiones-y-legitima.md`, `cc-particion-herencia.md`).

**1.4 — Aplicar cambios normativos.** Si la version oficial es posterior o el texto de los articulos ha cambiado:
- Aplicar en memoria la redaccion vigente para adaptar el computo de legitimas y las clausulas particionales.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

**1.5 — Fallback si la busqueda no es accesible.** Si la busqueda web falla: usar las references cargadas en el prompt como respaldo y notificar al usuario:
"No se pudo verificar en vivo la version vigente del Codigo Civil en el BOE. Los documentos se generan con la version de referencia. Verificar manualmente antes de firmar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no redacta nada hasta recoger estos datos:

**Bloque A — Documento solicitado:**
"Desea generar (1) el cuaderno particional / escritura de aceptacion y particion, (2) solo el documento de aceptacion de herencia, o (3) ambos?"

**Bloque B — Tipo de sucesion (CRITICO):**
"La sucesion es (1) TESTADA (hay testamento) o (2) INTESTADA (sin testamento, con declaracion de herederos)?"
- Si TESTADA: pedir notario autorizante, fecha y numero de protocolo del testamento, y las disposiciones relevantes (institucion de herederos, legados, mejoras, sustituciones).
- Si INTESTADA: pedir el acta notarial de declaracion de herederos (o su tramitacion) y confirmar el orden sucesorio que resulta (descendientes, a falta ascendientes, luego conyuge, luego colaterales; ver reference).

**Bloque C — Datos del causante:**
- Nombre completo, NIF, fecha y lugar de fallecimiento, ultimo domicilio.
- Estado civil al fallecer y regimen economico matrimonial (para liquidar la sociedad de gananciales antes de la herencia, si procede).

**Bloque D — Herederos y legitimarios:**
- Nombre completo, NIF y parentesco de cada heredero.
- Cuota o titulo de cada uno segun el testamento o la declaracion de herederos.
- Identificar a los legitimarios (descendientes; a falta, ascendientes; y conyuge viudo) y su legitima (Arts. 807-808 CC).

**Bloque E — Inventario de bienes y deudas:**
- Relacion de bienes: inmuebles (con referencia catastral y valor), cuentas y depositos, valores, vehiculos, ajuar domestico, otros; con el valor de cada uno (avaluo).
- Relacion de deudas y cargas de la herencia y gastos deducibles (ultima enfermedad, entierro y funeral).
- Donaciones o anticipos recibidos en vida por herederos forzosos que deban colacionarse (Art. 1035 CC).

**Bloque F — Modo de aceptacion:**
"La herencia se acepta (1) pura y simplemente (el heredero responde de las deudas tambien con su patrimonio) o (2) a beneficio de inventario (responde solo hasta donde alcancen los bienes de la herencia)? Recuerde que existe la opcion de renunciar."

**Bloque G — Comunidad autonoma:**
"En que comunidad autonoma tenia su residencia habitual el causante? Es necesario para advertir de la normativa del Impuesto de Sucesiones y Donaciones aplicable (es un tributo cedido a las CCAA, con bonificaciones muy distintas segun el territorio)."

### Paso 3 — Validacion sucesoria y calculo

Antes de redactar, validar:

a) **Titulo sucesorio.** Que existe testamento o declaracion de herederos que fundamente las cuotas. Sin titulo, no procede: advertir y, si es intestada sin declaracion, indicar que primero debe tramitarse el acta notarial de declaracion de herederos.

b) **Liquidacion previa de gananciales (si procede).** Si el causante estaba casado en gananciales, separar la mitad del conyuge viudo antes de formar el caudal hereditario. El caudal relicto es solo la mitad del causante mas sus bienes privativos.

c) **Computo de la legitima (Arts. 806-808 CC).** Calcular el haber liquido (bienes + donaciones colacionables - deudas). Verificar que la legitima de los herederos forzosos queda cubierta: descendientes, dos tercios (un tercio de legitima estricta a partes iguales y un tercio de mejora); conyuge viudo, el usufructo que corresponda (Art. 834 y ss.). Si alguna disposicion es inoficiosa (excede el tercio de libre disposicion en perjuicio de la legitima), advertir y proponer la reduccion.

d) **Igualdad en los lotes (Arts. 1061-1062 CC).** Formar lotes homogeneos en lo posible; los bienes indivisibles se adjudican a uno con compensacion en metalico a los demas.

e) **Acreedores de la herencia (Arts. 1082-1083 CC).** Advertir de que los acreedores reconocidos pueden oponerse a la particion hasta ser pagados o afianzados.

### Paso 4 — Generacion de los documentos

Tomar la plantilla correspondiente directamente desde el bloque `<document kind="assets-collection">` de tu system prompt (NO uses la herramienta `read_file` para leer plantillas):
- Cuaderno particional: `cuaderno-particional.md`
- Aceptacion de herencia: `aceptacion-herencia.md`

Generar el documento en el workspace invocando `create_file`:
```
create_file(
  relative_file_path: "cuaderno_particional.md" | "aceptacion_herencia.md",
  file_content: "... contenido completo redactado a partir de la plantilla y los datos recogidos en los bloques A-G ..."
)
```

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado quedan como `[DATO — PENDIENTE DE COMPLETAR]`.

Aplicar las directivas de `estilo-redaccion-escritos.md` (disponible directamente en `<document kind="references-collection">` del prompt): estructura de documento notarial/particional (comparecencia, exposicion, inventario y avaluo, liquidacion del haber, adjudicaciones, otorgamiento), clausulas numeradas, una idea por apartado, sin latinismos innecesarios, cifras en numero y letra.

Tras guardar el archivo en disco del workspace, invocar `read_file` exclusivamente sobre la ruta del workspace para verificar la integridad del documento escrito.

### Paso 5 — Revision final y advertencias

Verificar que cada documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Identifica correctamente al causante, el titulo sucesorio y a todos los herederos con su cuota.
- Refleja el inventario, el avaluo, la liquidacion del haber y las adjudicaciones, y cuadra (suma de adjudicaciones = haber liquido partible).
- Respeta la legitima de todos los herederos forzosos.

Entregar los documentos y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado y, si hay inmuebles, elevado a escritura publica notarial para su inscripcion en el Registro de la Propiedad.
2. Version del Codigo Civil verificada: [fecha extraida en Paso 1].
3. Impuesto de Sucesiones y Donaciones: es un tributo AUTONOMICO. El plazo general de autoliquidacion es de 6 meses desde el fallecimiento (prorrogable). Verificar las bonificaciones y reducciones de la comunidad autonoma [CCAA] con web_search antes de liquidar.
4. Plusvalia municipal (IIVTNU): si la herencia incluye inmuebles urbanos, hay que liquidarla en el ayuntamiento correspondiente, tambien en el plazo de 6 meses.
5. La legitima de los herederos forzosos (Arts. 806-808 CC) es intangible: cualquier adjudicacion que la perjudique es impugnable.
6. La particion requiere el acuerdo de todos los herederos; si no lo hay, procede la particion judicial o la designacion de contador-partidor.
```

## Como NO se usa esta skill

- No usar para redactar testamentos ni codicilos (es un generador de documentos particionales, no de disposiciones de ultima voluntad).
- No usar para tramitar el acta notarial de declaracion de herederos (paso previo en la sucesion intestada).
- No usar para liquidar el Impuesto de Sucesiones ni la plusvalia municipal: la skill advierte de los plazos, no presenta autoliquidaciones.
- No usar para litigios sucesorios contenciosos (accion de peticion de herencia, impugnacion de particion, reduccion de donaciones inoficiosas por via judicial): derivar a un abogado especialista en derecho sucesorio.
- No usar para herencias sujetas a derecho foral o autonomico especial (Cataluna, Aragon, Navarra, Pais Vasco, Baleares, Galicia) sin verificar antes la normativa civil propia con web_search y advertir al usuario.

## Escalacion

| Situacion | Accion |
|---|---|
| Disposicion que perjudica la legitima de un heredero forzoso | Advertir, recalcular y, si el usuario insiste, derivar a un abogado |
| Desacuerdo entre herederos sobre bienes, valores o adjudicaciones | Advertir de la via de particion judicial o contador-partidor y ofrecer escalacion |
| Sucesion sujeta a derecho foral o autonomico especial | Advertir, verificar con web_search y escalar si excede el Codigo Civil comun |
| Heredero menor o con discapacidad sin representacion clara | Advertir de la necesidad de defensor judicial o aprobacion, y escalar |
| Impugnacion de testamento, preterision o desheredacion controvertida | Advertir y derivar a un abogado |
| Deudas de la herencia superiores al activo (herencia dudosa) | Recomendar aceptacion a beneficio de inventario y ofrecer escalacion |
