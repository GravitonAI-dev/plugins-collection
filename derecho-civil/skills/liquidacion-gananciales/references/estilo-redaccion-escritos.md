# Estilo de Redacción de los Documentos de Liquidación de Gananciales

> Material de referencia para la skill `derecho-civil-liquidacion-gananciales`. Reglas de estilo aplicables a la propuesta
> de inventario, al convenio de liquidación y a la solicitud judicial de formación de inventario.
> Basado en guías de colegios de la abogacía y organismos oficiales.
> La skill aplica estas reglas al redactar; no forman parte del output al usuario.

---

## Fuentes

| Guía | Organismo |
|---|---|
| Guía de buenas prácticas sobre escritos e informes y actuaciones judiciales | ICAB — Colegio de la Abogacía de Barcelona |
| Guía de redacción judicial clara | Ministerio de Justicia |
| Libro de estilo de la Justicia | RAE / CGPJ |
| Recomendaciones de lenguaje jurídico claro | Consejo General de la Abogacía Española |

---

## Reglas de extensión

| Documento | Extensión razonable |
|---|---|
| Solicitud de formación de inventario (escrito procesal) | 2 a 4 folios; el peso del documento está en la propuesta que se acompaña, no en el escrito |
| Propuesta de inventario (anexo del art. 808.2 LEC) | Tan larga como exija el patrimonio: es una relación, no una argumentación |
| Convenio de liquidación | 4 a 10 folios según el número de bienes |

La solicitud de inventario **no es una demanda de divorcio ni un relato del matrimonio**: no se narra el conflicto conyugal, no se argumentan las medidas personales ni se reproducen reproches. El escrito identifica a las partes y el proceso, invoca la disolución del régimen y se remite a la propuesta. Todo el contenido patrimonial vive en la propuesta.

---

## Reglas de claridad y lenguaje

- Cada frase transmite una sola idea, sin ambigüedad.
- Frases y párrafos cortos. Evitar construcciones largas o enrevesadas.
- Usar la voz activa en lugar de la pasiva.
- Escribir con naturalidad: evitar palabras rebuscadas, latinismos y extranjerismos innecesarios.
- **Precisión terminológica del régimen económico.** Distinguir con rigor y no usar como sinónimos:
  - **Disolución** (la sociedad concluye, art. 1392 CC) frente a **liquidación** (se inventaria, se pagan deudas y reintegros y se divide el remanente, arts. 1396 a 1410 CC). Una sociedad puede estar disuelta y sin liquidar durante años.
  - **Bien privativo** frente a **bien ganancial**: nunca "bien propio" ni "bien personal" en un documento jurídico.
  - **Activo y pasivo del inventario** (arts. 1397 y 1398 CC) frente a **haber de cada cónyuge** (art. 1404 CC): el activo es de la sociedad, el haber es de la persona.
  - **Reintegro / reembolso** (crédito de una masa contra la otra, arts. 1358, 1364, 1397.3.º y 1398.3.ª CC) frente a **compensación por exceso de adjudicación** (pago en metálico entre cónyuges para igualar lotes). Son conceptos distintos y pueden concurrir en el mismo documento.
  - **Adjudicación** (atribución de un bien concreto en pago del haber) frente a **división** (reparto del remanente por mitad).
- No abusar de mayúsculas, subrayados ni negritas.
- No llamar "reparto de bienes" a la liquidación en el cuerpo del documento, aunque si puede usarse esa expresión al explicárselo al cliente en el chat.

---

## Reglas de estructura

### Escrito procesal (solicitud de formación de inventario)

- Encabezamiento con el órgano judicial. Se dirige al juzgado que está conociendo, ha conocido o hubiera tenido competencia para el proceso de nulidad, separación o divorcio (art. 807 LEC), indicando el número de autos si existe.
- Identificación clara de ambos cónyuges con sus datos, y del solicitante frente al otro.
- HECHOS numerados (PRIMERO, SEGUNDO...), un hecho por apartado. El orden natural es: matrimonio y régimen — causa y fecha de disolución — proceso en curso o sentencia firme — remisión a la propuesta que se acompaña.
- Documentos referenciados y numerados (Documento nº 1, nº 2...), correlativos a los hechos. La propuesta de inventario es siempre uno de ellos, y **cada partida de la propuesta debe tener su documento justificativo** (art. 808.2, párrafo segundo, LEC).
- FUNDAMENTOS DE DERECHO ordenados: competencia, procedimiento, disolución del régimen, contenido de la propuesta, postulación.
- SUPLICO limpio y concreto: que se admita la solicitud, se cite a los cónyuges para la formación del inventario y se acuerde lo procedente sobre administración y disposición de los bienes inventariados. Nada más.
- OTROSÍES separados y numerados, cada uno con su propio SUPLICO breve.
- Lugar, fecha y firma al final.

### Documento negocial (convenio de liquidación)

- Estructura tomada de la partición de herencia por remisión del art. 1410 CC: COMPARECEN — EXPONEN — INVENTARIO Y AVALÚO — LIQUIDACIÓN — ADJUDICACIONES — OTORGAMIENTO.
- El INVENTARIO se presenta **con la debida separación** entre activo y pasivo, y dentro del activo, entre bienes gananciales y créditos de la sociedad contra un cónyuge. Cada partida numerada y con su valor.
- La LIQUIDACIÓN expresa la operación aritmética completa, no solo el resultado: activo menos pasivo, pago de reintegros, remanente, mitad de cada cónyuge.
- Las ADJUDICACIONES se expresan bien por bien, indicando a quién se adjudica y por qué valor, y cerrando con la comprobación de que la suma de lo adjudicado a cada uno coincide con su haber.
- Cada bien inmueble se identifica con su descripción registral, referencia catastral y datos de finca, tomo, libro y folio, no solo con la dirección postal.

---

## Reglas específicas de la cuantificación

- **Toda partida lleva valor.** Un inventario con bienes sin valorar no permite formar lotes ni calcular el haber. Si un valor no se conoce, queda como placeholder pendiente, nunca estimado por la skill.
- **Expresar los totales en cifra y en letra**, igual que en cualquier documento con trascendencia patrimonial.
- **Los reintegros del art. 1358 CC se expresan con su importe ACTUALIZADO al tiempo de la liquidación**, no con el importe nominal de la aportación original. Indicar siempre la aportación original, el criterio de actualización empleado y el importe resultante, para que la operación sea verificable.
- **La deuda hipotecaria se consigna por su saldo pendiente a una fecha concreta**, acreditado por certificado de la entidad, no por el importe inicial del préstamo.
- **Nunca compensar de oficio partidas de distinto signo sin explicarlo.** Si un cónyuge es a la vez acreedor de la sociedad por un reintegro y deudor de ella por una cantidad pagada en su interés, hacer explicitas ambas partidas y la compensación final (art. 1403 CC).
- **La suma de las adjudicaciones debe cuadrar con el haber líquido.** Si no cuadra, la diferencia es un exceso de adjudicación y exige su cláusula de compensación en metálico: no se deja descuadrado el documento.

---

## Reglas específicas del inventario contradictorio

- Cuando la naturaleza de un bien está discutida, la propuesta **no la afirma como pacifica**: identifica el bien, expresa el carácter que se le atribuye y **el motivo concreto** por el que se le atribuye, con su documento justificativo.
- La presunción del art. 1361 CC se invoca de forma técnica y sin retorica: el bien se incluye en el activo porque existe en el matrimonio y no se ha probado su carácter privativo, correspondiendo la carga de esa prueba a quien lo alegue.
- No calificar de fraudulenta la conducta del otro cónyuge sin base documental. Si se invoca el art. 1397.2.º CC (bienes enajenados por negocio ilegal o fraudulento), la partida debe ir acompañada de la documentación de la enajenación y de su valor actualizado.

---

## Aplicación en esta skill

Al rellenar los assets, mantener la separación estricta activo/pasivo, numerar cada partida y acompañarla de su valor y su documento justificativo; redactar los HECHOS de la solicitud de forma numerada y concisa, sin narrar el conflicto conyugal; expresar las operaciones de liquidación completas y verificables; y mantener el SUPLICO ajustado a lo estrictamente pedido. Evitar fórmulas grandilocuentes y latinismos. Nunca dar por pacifica la naturaleza de un bien discutido ni por valorada una partida sin valor aportado por el cliente.
