# Estilo de Redaccion de los Documentos de Liquidacion de Gananciales

> Material de referencia para la skill `derecho-civil-liquidacion-gananciales`. Reglas de estilo aplicables a la propuesta
> de inventario, al convenio de liquidacion y a la solicitud judicial de formacion de inventario.
> Basado en guias de colegios de la abogacia y organismos oficiales.
> La skill aplica estas reglas al redactar; no forman parte del output al usuario.

---

## Fuentes

| Guia | Organismo |
|---|---|
| Guia de buenas practicas sobre escritos e informes y actuaciones judiciales | ICAB — Colegio de la Abogacia de Barcelona |
| Guia de redaccion judicial clara | Ministerio de Justicia |
| Libro de estilo de la Justicia | RAE / CGPJ |
| Recomendaciones de lenguaje juridico claro | Consejo General de la Abogacia Espanola |

---

## Reglas de extension

| Documento | Extension razonable |
|---|---|
| Solicitud de formacion de inventario (escrito procesal) | 2 a 4 folios; el peso del documento esta en la propuesta que se acompana, no en el escrito |
| Propuesta de inventario (anexo del art. 808.2 LEC) | Tan larga como exija el patrimonio: es una relacion, no una argumentacion |
| Convenio de liquidacion | 4 a 10 folios segun el numero de bienes |

La solicitud de inventario **no es una demanda de divorcio ni un relato del matrimonio**: no se narra el conflicto conyugal, no se argumentan las medidas personales ni se reproducen reproches. El escrito identifica a las partes y el proceso, invoca la disolucion del regimen y se remite a la propuesta. Todo el contenido patrimonial vive en la propuesta.

---

## Reglas de claridad y lenguaje

- Cada frase transmite una sola idea, sin ambiguedad.
- Frases y parrafos cortos. Evitar construcciones largas o enrevesadas.
- Usar la voz activa en lugar de la pasiva.
- Escribir con naturalidad: evitar palabras rebuscadas, latinismos y extranjerismos innecesarios.
- **Precision terminologica del regimen economico.** Distinguir con rigor y no usar como sinonimos:
  - **Disolucion** (la sociedad concluye, art. 1392 CC) frente a **liquidacion** (se inventaria, se pagan deudas y reintegros y se divide el remanente, arts. 1396 a 1410 CC). Una sociedad puede estar disuelta y sin liquidar durante anos.
  - **Bien privativo** frente a **bien ganancial**: nunca "bien propio" ni "bien personal" en un documento juridico.
  - **Activo y pasivo del inventario** (arts. 1397 y 1398 CC) frente a **haber de cada conyuge** (art. 1404 CC): el activo es de la sociedad, el haber es de la persona.
  - **Reintegro / reembolso** (credito de una masa contra la otra, arts. 1358, 1364, 1397.3.º y 1398.3.ª CC) frente a **compensacion por exceso de adjudicacion** (pago en metalico entre conyuges para igualar lotes). Son conceptos distintos y pueden concurrir en el mismo documento.
  - **Adjudicacion** (atribucion de un bien concreto en pago del haber) frente a **division** (reparto del remanente por mitad).
- No abusar de mayusculas, subrayados ni negritas.
- No llamar "reparto de bienes" a la liquidacion en el cuerpo del documento, aunque si puede usarse esa expresion al explicarselo al cliente en el chat.

---

## Reglas de estructura

### Escrito procesal (solicitud de formacion de inventario)

- Encabezamiento con el organo judicial. Se dirige al juzgado que esta conociendo, ha conocido o hubiera tenido competencia para el proceso de nulidad, separacion o divorcio (art. 807 LEC), indicando el numero de autos si existe.
- Identificacion clara de ambos conyuges con sus datos, y del solicitante frente al otro.
- HECHOS numerados (PRIMERO, SEGUNDO...), un hecho por apartado. El orden natural es: matrimonio y regimen — causa y fecha de disolucion — proceso en curso o sentencia firme — remision a la propuesta que se acompana.
- Documentos referenciados y numerados (Documento nº 1, nº 2...), correlativos a los hechos. La propuesta de inventario es siempre uno de ellos, y **cada partida de la propuesta debe tener su documento justificativo** (art. 808.2, parrafo segundo, LEC).
- FUNDAMENTOS DE DERECHO ordenados: competencia, procedimiento, disolucion del regimen, contenido de la propuesta, postulacion.
- SUPLICO limpio y concreto: que se admita la solicitud, se cite a los conyuges para la formacion del inventario y se acuerde lo procedente sobre administracion y disposicion de los bienes inventariados. Nada mas.
- OTROSIES separados y numerados, cada uno con su propio SUPLICO breve.
- Lugar, fecha y firma al final.

### Documento negocial (convenio de liquidacion)

- Estructura tomada de la particion de herencia por remision del art. 1410 CC: COMPARECEN — EXPONEN — INVENTARIO Y AVALUO — LIQUIDACION — ADJUDICACIONES — OTORGAMIENTO.
- El INVENTARIO se presenta **con la debida separacion** entre activo y pasivo, y dentro del activo, entre bienes gananciales y creditos de la sociedad contra un conyuge. Cada partida numerada y con su valor.
- La LIQUIDACION expresa la operacion aritmetica completa, no solo el resultado: activo menos pasivo, pago de reintegros, remanente, mitad de cada conyuge.
- Las ADJUDICACIONES se expresan bien por bien, indicando a quien se adjudica y por que valor, y cerrando con la comprobacion de que la suma de lo adjudicado a cada uno coincide con su haber.
- Cada bien inmueble se identifica con su descripcion registral, referencia catastral y datos de finca, tomo, libro y folio, no solo con la direccion postal.

---

## Reglas especificas de la cuantificacion

- **Toda partida lleva valor.** Un inventario con bienes sin valorar no permite formar lotes ni calcular el haber. Si un valor no se conoce, queda como placeholder pendiente, nunca estimado por la skill.
- **Expresar los totales en cifra y en letra**, igual que en cualquier documento con trascendencia patrimonial.
- **Los reintegros del art. 1358 CC se expresan con su importe ACTUALIZADO al tiempo de la liquidacion**, no con el importe nominal de la aportacion original. Indicar siempre la aportacion original, el criterio de actualizacion empleado y el importe resultante, para que la operacion sea verificable.
- **La deuda hipotecaria se consigna por su saldo pendiente a una fecha concreta**, acreditado por certificado de la entidad, no por el importe inicial del prestamo.
- **Nunca compensar de oficio partidas de distinto signo sin explicarlo.** Si un conyuge es a la vez acreedor de la sociedad por un reintegro y deudor de ella por una cantidad pagada en su interes, hacer explicitas ambas partidas y la compensacion final (art. 1403 CC).
- **La suma de las adjudicaciones debe cuadrar con el haber liquido.** Si no cuadra, la diferencia es un exceso de adjudicacion y exige su clausula de compensacion en metalico: no se deja descuadrado el documento.

---

## Reglas especificas del inventario contradictorio

- Cuando la naturaleza de un bien esta discutida, la propuesta **no la afirma como pacifica**: identifica el bien, expresa el caracter que se le atribuye y **el motivo concreto** por el que se le atribuye, con su documento justificativo.
- La presuncion del art. 1361 CC se invoca de forma tecnica y sin retorica: el bien se incluye en el activo porque existe en el matrimonio y no se ha probado su caracter privativo, correspondiendo la carga de esa prueba a quien lo alegue.
- No calificar de fraudulenta la conducta del otro conyuge sin base documental. Si se invoca el art. 1397.2.º CC (bienes enajenados por negocio ilegal o fraudulento), la partida debe ir acompanada de la documentacion de la enajenacion y de su valor actualizado.

---

## Aplicacion en esta skill

Al rellenar los assets, mantener la separacion estricta activo/pasivo, numerar cada partida y acompanarla de su valor y su documento justificativo; redactar los HECHOS de la solicitud de forma numerada y concisa, sin narrar el conflicto conyugal; expresar las operaciones de liquidacion completas y verificables; y mantener el SUPLICO ajustado a lo estrictamente pedido. Evitar formulas grandilocuentes y latinismos. Nunca dar por pacifica la naturaleza de un bien discutido ni por valorada una partida sin valor aportado por el cliente.
