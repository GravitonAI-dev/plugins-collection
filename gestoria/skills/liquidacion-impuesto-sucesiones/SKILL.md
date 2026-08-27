---
name: liquidacion-impuesto-sucesiones
description: >
  Prepara la autoliquidacion del Impuesto sobre Sucesiones y Donaciones (modelo 650, adquisiciones
  mortis causa) de un heredero conforme a la Ley 29/1987 (BOE-A-1987-28141) y su Reglamento (RD 1629/1991)
  en su version consolidada vigente verificada en el BOE, y con la normativa autonomica vigente de la
  comunidad autonoma competente verificada con web_search (reducciones y bonificaciones varian mucho por
  CCAA). Genera una hoja de datos y borrador del modelo 650 con la base y una estimacion de la cuota
  marcada [verificar], el checklist de documentos, el organismo y plazo de presentacion (6 meses,
  prorrogable) y el aviso de la plusvalia municipal por inmuebles urbanos. NO usar para el reparto
  juridico de la herencia (eso lo hace la skill particion-herencia de derecho-civil), para donaciones o
  seguros liquidados de forma independiente por otro modelo, ni para dar la cuota como definitiva.
when_to_use: |
  - El usuario ya sabe que heredero es y que recibe, y necesita preparar la autoliquidacion del Impuesto de Sucesiones (modelo 650).
  - El usuario dispone del inventario y los valores de la herencia (propios o del cuaderno particional) y quiere saber base, estimacion de cuota, plazo y organismo.
  - El usuario pide el checklist de documentos y tasas para presentar el Impuesto de Sucesiones y saber donde se presenta.
inputs:
  - comunidad_autonoma: CCAA de residencia habitual del causante (clave: determina bonificaciones y organismo)
  - datos_causante: nombre, NIF, fecha y lugar de fallecimiento, ultimo domicilio, CCAA de residencia habitual
  - datos_heredero: nombre, NIF, domicilio, parentesco con el causante y grupo (I a IV)
  - caudal_hereditario: inventario de bienes y sus valores (del cuaderno particional si existe)
  - cargas_deudas: cargas, deudas deducibles y gastos (ultima enfermedad, entierro y funeral)
  - seguros_vida: importe de seguros de vida cuyo beneficiario sea el heredero, si los hay
  - ajuar_domestico: valor declarado del ajuar, o aplicar el 3% del caudal relicto (Art. 15) salvo prueba
  - vivienda_habitual: si el heredero adquiere la vivienda habitual del causante (reduccion Art. 20.2.c)
  - empresa_familiar: si se adquiere empresa individual, negocio o participaciones (reduccion Art. 20.2.c)
  - discapacidad: grado de discapacidad del heredero, si procede reduccion
outputs:
  - borrador_autoliquidacion_650: hoja de datos y borrador del modelo 650 con base, reducciones y cuota estimada [verificar], en markdown, DRAFT
  - checklist_documentacion: checklist de documentos, tasas, organismo y plazo para la presentacion, en markdown, DRAFT
references:
  - references/isd-ley-29-1987.md
  - references/isd-normativa-autonomica.md
  - references/plusvalia-municipal.md
  - references/fuentes-y-plazos.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/borrador-autoliquidacion-650.md
  - assets/checklist-documentacion-sucesiones.md
---

# Preparar la Autoliquidacion del Impuesto de Sucesiones (Modelo 650)

> DRAFT — para revision por un gestor o asesor fiscal antes de su presentacion. No constituye asesoramiento fiscal ni juridico.

## Guardrails

1. Verificar siempre la Ley 29/1987 y su Reglamento en el BOE antes de preparar el tramite. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version posterior a la registrada en las references, actualizar los archivos del plugin antes de preparar (ver Paso 1). No usar una version desactualizada.
3. El ISD es un tributo CEDIDO a las comunidades autonomas. Las reducciones y bonificaciones varian de forma drastica por CCAA. Es OBLIGATORIO verificar con web_search la normativa autonomica vigente de la comunidad autonoma competente antes de estimar la cuota. Nunca aplicar las reducciones estatales como si fueran definitivas cuando la CCAA mejora el regimen.
4. La cuota es siempre una ESTIMACION marcada [verificar]. Nunca presentar la cuota como definitiva: la determinacion final corresponde al gestor o asesor fiscal y a la validacion de valores de la administracion.
5. Marcar con [verificar] todos los importes, reducciones, bonificaciones, tarifas y coeficientes: dependen de la CCAA y del ejercicio, y cambian con frecuencia.
6. Indicar siempre el organismo competente (Hacienda autonomica de la residencia habitual del causante), el plazo (6 meses desde el fallecimiento, prorrogable) y el modelo aplicable.
7. Nunca omitir el aviso de la plusvalia municipal (IIVTNU) cuando la herencia incluya inmuebles urbanos: es un tributo distinto, del ayuntamiento, con su propio plazo.
8. No inventar NIF, valores, fechas, referencias catastrales ni cuotas. Los datos que falten quedan como campo pendiente de completar.

## Procedimiento

### Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, antes de cualquier otra accion)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de preparar el tramite. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la fecha/version registrada localmente.** Abrir `references/fuentes-y-plazos.md` y anotar la "Version registrada" de la Ley 29/1987, del RD 1629/1991, del modelo 650 y del TR de la Ley Reguladora de las Haciendas Locales (plusvalia).

**1.2 — Consultar la fuente oficial estatal vigente.** Invocar:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141",
  format: "text"
)
```
Extraer: fecha del texto consolidado vigente de la Ley 29/1987; redaccion actual del hecho imponible (Arts. 3 y 5-8), la base imponible y el ajuar (Arts. 9 y 15), las reducciones estatales y los grupos de parentesco (Art. 20), y la tarifa y coeficientes multiplicadores (Arts. 21-22).

Consultar tambien el Reglamento (RD 1629/1991):
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-1991-27678",
  format: "text"
)
```

**1.3 — Verificar la NORMATIVA AUTONOMICA vigente (OBLIGATORIO).** El importe del impuesto depende sobre todo de la CCAA. Una vez conocida la comunidad autonoma competente (Paso 2, Bloque A), invocar:
```
web_search("Impuesto Sucesiones [comunidad autonoma] reducciones bonificaciones vigentes 2026 grupo parentesco cuota")
```
Extraer: reducciones autonomicas propias o mejoradas, bonificaciones de la cuota (muchas CCAA aplican bonificaciones cercanas al 99% para Grupos I y II), tarifa y coeficientes autonomicos si los hubiera, y el modelo y la sede de presentacion de esa CCAA. Anotar estos datos como [verificar].

Verificar tambien la plusvalia municipal si hay inmuebles urbanos:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214",
  format: "text"
)
```

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto ha cambiado, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/isd-ley-29-1987.md` (reducciones estatales, grupos, tarifa) y/o `references/plusvalia-municipal.md`.
- Actualizar `references/isd-normativa-autonomica.md` con lo verificado para la CCAA concreta (dejando el resto de la tabla como ejemplo marcado [verificar]).
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-y-plazos.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No preparar ningun tramite hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_document` falla (error HTTP, timeout):
```
web_search("Ley 29/1987 Impuesto sobre Sucesiones y Donaciones texto consolidado BOE reducciones articulo 20")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la normativa del Impuesto de Sucesiones. El borrador se genera con la version de referencia y con importes marcados [verificar]. Verificar manualmente antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no prepara nada hasta recoger estos datos:

**Bloque A — Comunidad autonoma competente (CRITICO):**
"En que comunidad autonoma tenia su residencia habitual el causante en los ultimos anos? Es la clave del tramite: determina las bonificaciones aplicables y el organismo (Hacienda autonomica) donde se presenta. Como regla general se atiende a la CCAA donde el causante residio mas dias de los ultimos cinco anos."

**Bloque B — Datos del causante:**
- Nombre completo, NIF, fecha y lugar de fallecimiento, ultimo domicilio.
- Confirmar la CCAA de residencia habitual (para puntos de conexion).

**Bloque C — Datos y parentesco del heredero:**
- Nombre completo, NIF y domicilio del heredero para el que se prepara la autoliquidacion.
- Parentesco con el causante, para asignar el GRUPO (I a IV; ver `references/isd-ley-29-1987.md`), del que dependen las reducciones y los coeficientes.
- Patrimonio preexistente del heredero solo si la CCAA lo exige para el coeficiente multiplicador (indicarlo como [verificar]).

**Bloque D — Caudal hereditario (inventario y valores):**
- Relacion de bienes y derechos con su valor: inmuebles (con referencia catastral y valor de referencia/mercado), cuentas y depositos, valores, vehiculos, otros.
- Si existe cuaderno particional (skill `particion-herencia`), tomar de ahi el inventario y el avaluo, y la parte que corresponde a ESTE heredero.
- Ajuar domestico: valor declarado o, en su defecto, el 3% del caudal relicto (Art. 15), salvo prueba en contrario.

**Bloque E — Cargas, deudas y gastos deducibles:**
- Cargas y gravamenes que disminuyen el valor de los bienes (Art. 12).
- Deudas deducibles del causante (Art. 13).
- Gastos deducibles: ultima enfermedad, entierro y funeral (Art. 14).

**Bloque F — Seguros de vida:**
"El heredero es beneficiario de algun seguro de vida por el fallecimiento? Los seguros de vida tienen su propia reduccion (Art. 20.2.b) y se acumulan a la porcion hereditaria del beneficiario."

**Bloque G — Reducciones aplicables:**
- Vivienda habitual del causante: si el heredero (conyuge, descendiente, ascendiente o colateral mayor de 65 conviviente) la adquiere, reduccion del 95% con limite y permanencia (Art. 20.2.c), mejorable por la CCAA.
- Empresa familiar, negocio o participaciones: reduccion del 95% (Art. 20.2.c), mejorable por la CCAA.
- Discapacidad del heredero: reduccion adicional segun grado.

### Paso 3 — Calculo estimado (todo marcado [verificar])

Antes de generar el borrador, componer la estimacion siguiendo el esquema del ISD (ver `references/isd-ley-29-1987.md`), aplicando primero el regimen autonomico verificado en el Paso 1.3:

a) **Masa hereditaria neta.** Caudal relicto (bienes + ajuar) - cargas, deudas y gastos deducibles.

b) **Porcion individual del heredero.** La parte que le corresponde segun su cuota o adjudicacion, mas los seguros de vida de los que sea beneficiario.

c) **Base liquidable.** Porcion individual - reducciones aplicables (parentesco por grupo, seguros, vivienda habitual, empresa familiar, discapacidad), aplicando el importe autonomico cuando mejore al estatal. Marcar cada reduccion [verificar].

d) **Cuota integra.** Aplicar la tarifa (estatal o autonomica) a la base liquidable. Marcar [verificar].

e) **Cuota tributaria.** Aplicar el coeficiente multiplicador segun grupo y, en su caso, patrimonio preexistente. Marcar [verificar].

f) **Cuota a ingresar.** Aplicar las bonificaciones de la cuota de la CCAA (frecuentes al 99% para Grupos I y II). Marcar [verificar].

Advertir de forma expresa que el resultado es una estimacion orientativa, no la cuota definitiva.

### Paso 4 — Generacion de los documentos

Generar el borrador de autoliquidacion y el checklist:
```
draft_markdown(
  template_id: "borrador-autoliquidacion-650",
  variables: { todos los datos recogidos en los bloques A-G y la estimacion del Paso 3 }
)
```
```
draft_markdown(
  template_id: "checklist-documentacion-sucesiones",
  variables: { comunidad_autonoma, organismo, plazo, si hay inmuebles urbanos }
)
```

Rellenar los campos con los datos reales. Los campos que el usuario no haya proporcionado quedan como campo pendiente de completar. Aplicar el estilo de `references/estilo-redaccion-escritos.md`: lenguaje administrativo claro, cifras en numero, una idea por apartado, sin formulas grandilocuentes.

### Paso 5 — Revision final y advertencias

Verificar que cada documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1) y la CCAA competente.
- Identifica al causante y al heredero, con el grupo de parentesco.
- Expresa la base, las reducciones aplicadas y la cuota estimada, todo marcado [verificar].
- Indica organismo, sede, modelo y plazo, y el aviso de la plusvalia municipal si hay inmuebles urbanos.

Entregar los documentos y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un gestor o asesor fiscal antes de su presentacion.
2. La cuota es una ESTIMACION [verificar], no la cuota definitiva. Los importes, reducciones y bonificaciones dependen de la CCAA [CCAA] y del ejercicio, y deben verificarse.
3. Version de la Ley 29/1987 verificada: [fecha extraida en Paso 1].
4. Plazo de autoliquidacion: 6 meses desde el fallecimiento, prorrogable por otros 6 si se solicita dentro de los 5 primeros meses.
5. Organismo competente: Hacienda autonomica de la comunidad de residencia habitual del causante [CCAA]. Modelo: 650 (o el modelo autonomico equivalente [verificar]).
6. Plusvalia municipal (IIVTNU): si la herencia incluye inmuebles urbanos, hay que liquidarla ademas en el ayuntamiento correspondiente, con su propio plazo.
```

## Como NO se usa esta skill

- No usar para el reparto juridico de la herencia (inventario, avaluo, legitima, adjudicaciones): eso lo hace la skill `particion-herencia` del plugin `derecho-civil`. Esta skill parte de ese reparto para preparar la liquidacion fiscal.
- No usar para donaciones en vida (modelo 651) ni para seguros de vida liquidados de forma independiente por otro modelo.
- No usar para calcular ni presentar la plusvalia municipal: la skill solo avisa de su existencia y plazo.
- No usar para dar la cuota como definitiva ni para sustituir la revision de un gestor o asesor fiscal.
- No usar para herencias con litigio, comprobacion de valores en curso, sancion o aplazamiento controvertido: derivar a un gestor o asesor fiscal colegiado.

## Escalacion

| Situacion | Accion |
|---|---|
| Herencia con litigio sucesorio o desacuerdo entre herederos | Advertir de que primero debe resolverse el reparto (`particion-herencia`) y ofrecer escalacion |
| Comprobacion de valores o liquidacion complementaria de la administracion | Advertir y derivar a gestor o asesor fiscal |
| Bonificacion autonomica dudosa o cambio normativo reciente en la CCAA | Verificar con web_search, marcar [verificar] y advertir |
| Solicitud de aplazamiento, fraccionamiento o prorroga del pago | Indicar la via ante la Hacienda autonomica y ofrecer escalacion |
| Empresa familiar o participaciones con requisitos de exencion dudosos | Advertir de la complejidad del Art. 20.2.c y escalar |
| Causante o heredero no residente, o bienes en el extranjero | Advertir de las reglas de competencia (AEAT vs. CCAA) y escalar |
