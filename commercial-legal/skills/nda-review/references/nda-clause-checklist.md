# Checklist de clausulas — NDA review

> Material de referencia para la skill `nda-review`. Lo lee Claude al aplicar el triage. NO se incluye en el output al usuario.

## Como usar este checklist

Para cada item:
1. Buscar la clausula correspondiente en el NDA.
2. Comparar el lenguaje con el patron descrito abajo.
3. Asignar veredicto de clausula: VERDE (aceptable), AMARILLO (flag para revision), ROJO (inaceptable), o AUSENTE (no esta en el documento — no es fallo por si mismo, pero combinar con el resto).

> Las reglas concretas de veredicto agregado (cuantas AMARILLO/ROJO disparan cada nivel) viven en `CLAUDE.md` del plugin, no aqui. Este archivo define el veredicto **por clausula**.

## Clausulas criticas

### 1. Partes identificadas

- **Que buscar**: el NDA nombra explicitamente las partes (persona juridica o individuo) con su domicilio legal o al menos su nombre completo.
- **VERDE**: ambas partes nombradas con denominacion legal o nombre completo.
- **AMARILLO**: partes nombradas pero sin domicilio. Una de las partes es un nombre comercial sin forma juridica.
- **ROJO**: partes no identificadas, o el NDA es "tropicalizado" (una sola parte que "incluye a sus afiliadas" sin definirlas).

### 2. Definicion de Informacion Confidencial

- **Que buscar**: seccion que define que constituye informacion confidencial.
- **VERDE**: definicion amplia pero razonable (incluye informacion escrita, oral, electronica; markings no requeridos si la divulgacion es oral y se confirma por escrito en X dias).
- **AMARILLO**: definicion muy amplia que incluye "cualquier informacion" sin exclusion, o requiere markings en toda divulgacion (friccion operativa).
- **ROJO**: definicion ausente, o excluye informacion que claramente es confidencial (ej: excluye "informacion que era conocida antes" sin limitar a conocimiento documentado).

### 3. Direccion del NDA

- **Que buscar**: unilateral (solo una parte disclose) o mutuo (ambas partes discloser y recipient).
- **VERDE**: direccion claramente especificada. Mutuo preferido por defecto del plugin.
- **AMARILLO**: direccion no especificada — asumir mutuo y marcar `[verificar]`.
- **ROJO**: direccion especificada como unilateral en sentido desfavorable al equipo (receptor es siempre la contraparte).

### 4. Termino (duracion)

- **Que buscar**: cuanto tiempo dura la obligacion de confidencialidad.
- **VERDE**: 1-5 anos, plazo explicito.
- **AMARILLO**: mas de 5 anos, o atado a la duracion de un proyecto sin fecha limite clara.
- **ROJO**: perpetuo, o sin plazo, o "mientras la informacion permanezca confidencial" (de facto perpetuo).

### 5. Exclusiones estandar

- **Que buscar**: lista de exclusiones de la obligacion (informacion publica, conocido previamente, desarrollado independientemente, recibido de tercero, requerido por ley).
- **VERDE**: las cinco exclusiones clasicas presentes, redactadas en lenguaje claro.
- **AMARILLO**: faltan una o dos exclusiones, o una esta redactada con condiciones irrazonables.
- **ROJO**: ninguna exclusion presente, o exclusion de "requerido por ley" ausente (peligro de incumplimiento si la contraparte recibe una subpoena).

### 6. Residuals clause

- **Que buscar**: clausula que permite al receptor usar informacion que retenga en la memoria de sus empleados ("residuals").
- **VERDE**: ausente (mejor para la parte que protege informacion) o presente con plazo post-empleo < 12 meses y exclusion de PII.
- **AMARILLO**: presente con plazo post-empleo 12-24 meses, o sin exclusion explicita de PII.
- **ROJO**: presente, perpetua, y/o cubre PII o secretos comerciales sin proteccion adicional.

### 7. Obligaciones del receptor

- **Que buscar**: que debe hacer el receptor con la informacion (no divulgar, proteger con el mismo cuidado que su propia informacion, limitar acceso a need-to-know, etc.).
- **VERDE**: obligaciones claras, "mismo cuidado que su propia informacion confidencial de tipo similar" o "estandar de cuidado razonable".
- **AMARILLO**: obligaciones presentes pero vagas, o sin mencion de need-to-know.
- **ROJO**: obligaciones practicamente ausentes, o delegadas enteramente a una "politica interna" sin compromiso especifico.

### 8. Transferencia / cesion

- **Que buscar**: bajo que condiciones el receptor puede transferir el NDA u obligar a terceros (asesores, afiliadas).
- **VERDE**: cesion requiere consentimiento escrito de la otra parte; se permite divulgacion a asesores bajo obligationes de confidencialidad por escrito.
- **AMARILLO**: cesion libre a afiliadas sin restriccion, o a "asesores profesionales" sin exigirles firma de back-to-back NDA.
- **ROJO**: cesion libre a cualquier tercero, o a competidores del discloser.

### 9. Propiedad intelectual

- **Que buscar**: clausula sobre IP — usualmente "no se transfiere IP por el NDA".
- **VERDE**: presente y clara — "este NDA no transfiere ninguna IP; toda IP sigue siendo del discloser".
- **AMARILLO**: presente pero con lenguaje ambiguo, o ausente (riesgo de interpretacion posterior).
- **ROJO**: clausula que sugiera que el receptor adquiere alguna licencia o derecho sobre la informacion.

### 10. Carta de indemnidad (indemnity)

- **Que buscar**: el NDA incluye una indemnidad a favor de la contraparte.
- **VERDE**: ausente (no aplica a NDAs).
- **AMARILLO**: indemnidad limitada a breach de confidencialidad, cap razonable, sin punitive damages.
- **ROJO**: indemnidad amplia, sin cap, cubre danos consecuenciales o punitivos. Una indemnidad amplia en un NDA es una bandera roja de que el "NDA" es en realidad un acuerdo mas complejo y debe ir a un abogado.

### 11. Inyeccion / retorno de informacion

- **Que buscar**: al terminar, que pasa con la informacion confidencial (devolver, destruir, certificar).
- **VERDE**: opcion del discloser entre retorno o destruccion; certificacion por escrito de cumplimiento.
- **AMARILLO**: solo destruccion obligatoria (puede ser friccion si la informacion esta embebida en sistemas que no se pueden borrar facilmente) o solo retorno.
- **ROJO**: ausente, o permite al receptor "conservar una copia" sin restriccion.

### 12. Remedios (equitable relief)

- **Que buscar**: reconocimiento de que el breach causa dano irreparable y da derecho a injunctive relief sin probar danos.
- **VERDE**: presente, lenguaje estandar ("the parties acknowledge that monetary damages may be inadequate...").
- **AMARILLO**: ausente (no es bloqueante, pero es deseable tenerla).
- **ROJO**: presente pero en sentido inverso (restringe al discloser de buscar injunctive relief).

### 13. Ley aplicable y jurisdiccion

- **Que buscar**: `governing law` y `venue / jurisdiction`.
- **VERDE**: ley aplicable y foro en una jurisdiccion donde el equipo tiene presencia operativa. Para equipos en EE.UU.: Delaware, California, New York son default aceptables.
- **AMARILLO**: ley aplicable / foro en otra jurisdiccion de EE.UU. (no es bloqueante pero requiere confirmacion de que litigar alli es viable). LATAM / UK / UE son AMARILLO por defecto.
- **ROJO**: ley aplicable en jurisdiccion sin tratado de ejecucion de sentencias con la jurisdiccion de operacion del equipo, o foro claramente hostil (arbitraje obligatorio en sede especifica con reglas desfavorables).

### 14. Conflicto con otros acuerdos

- **Que buscar**: clausula que diga que este NDA "no afecta", "reemplaza" o "prevalece sobre" acuerdos previos.
- **VERDE**: clausula de "entire agreement" o "supersession" presente y razonable, o silencio (no hay acuerdo previo relevante).
- **AMARILLO**: silencio, y el equipo tiene acuerdos previos con la misma contraparte — verificar manualmente.
- **ROJO**: clausula que expresamente derogue protecciones de un NDA previo sin la firma simultanea del reemplazo.

### 15. Firma electronica / counterparts

- **Que buscar**: el NDA permite firma electronica (DocuSign, Adobe Sign) o ejecucion en counterparts.
- **VERDE**: permite firma electronica y counterparts.
- **AMARILLO**: solo firma original (friccion operativa pero no bloqueante).
- **ROJO**: requiere firma notarizada, apostill, o similar (incompatible con la mayoria de los flujos comerciales).

## Resumen rapido (cheat sheet)

| Clausula | Ausente | Tipico VERDE | Tipico AMARILLO | Tipico ROJO |
|---|---|---|---|---|
| Partes | × | Ambas con domicilio | Una sin domicilio | No identificadas |
| Def. Confidencial | × | Amplia y razonable | Muy amplia o markings requeridos | Ausente o excluye info clara |
| Direccion | AMARILLO | Mutuo | No especificada | Unilateral en contra |
| Termino | ROJO | 1-5 anos | > 5 anos o atado a proyecto | Perpetuo o sin plazo |
| Exclusiones | ROJO | 5 clasicas | Faltan 1-2 | Ninguna o sin requerida-por-ley |
| Residuals | VERDE | Ausente o plazo < 12m | Plazo 12-24m o cubre PII | Perpetua y amplia |
| Obligaciones receptor | AMARILLO | Claras + need-to-know | Vagas | Ausentes o delegadas |
| Cesion | AMARILLO | Requiere consentimiento | Libre a afiliadas | Libre a terceros/competidores |
| IP | AMARILLO | "No transfiere IP" | Ambiguo o ausente | Sugiere licencia |
| Indemnity | VERDE | Ausente | Limitada a breach, con cap | Amplia, sin cap |
| Retorno / destruccion | AMARILLO | Opcion del discloser + cert. | Solo retorno o solo destruccion | Ausente o "conservar copia" libre |
| Equitable relief | AMARILLO | Presente, lenguaje estandar | Ausente | Presente pero en contra |
| Ley aplicable | AMARILLO | Del estado de operacion | Otro estado UE/LATAM | Sin tratado de ejecucion |
| Conflicto | VERDE | Entire agreement o silencio | Silencio con NDA previo | Deroga proteccion previa |
| Firma electronica | AMARILLO | Permitida | Solo firma original | Notario / apostilla |
