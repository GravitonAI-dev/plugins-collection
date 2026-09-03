# Estilo de Redaccion de Contratos entre Particulares

> Material de referencia para la skill `derecho-civil-contratos-particulares`. Reglas de estilo aplicables al contrato de
> prestamo, al reconocimiento de deuda, al contrato de comodato y al contrato de compraventa de bien mueble.
> Basado en guias de colegios de la abogacia y organismos oficiales, adaptadas al documento contractual.
> La skill aplica estas reglas al redactar; no forman parte del output al usuario.

---

## Fuentes

| Guia | Organismo |
|---|---|
| Guia de buenas practicas sobre escritos e informes y actuaciones judiciales | ICAB — Colegio de la Abogacia de Barcelona |
| Guia de redaccion judicial clara | Ministerio de Justicia |
| Libro de estilo de la Justicia | RAE / CGPJ |
| Recomendaciones de lenguaje juridico claro | Consejo General de la Abogacia Española |

---

## Diferencia esencial respecto de un escrito procesal

Un contrato entre particulares **no se dirige a un juez, sino a las propias partes**, y muchas veces a partes sin formacion juridica. Dos consecuencias:

1. **Se lee antes de firmarlo, y se relee cuando hay conflicto.** Cada clausula tiene que ser comprensible para quien la firma, no solo defendible ante un tribunal.
2. **Es la unica prueba de lo pactado.** Lo que no este escrito con precision se discutira. El art. 1281 CC ordena estar al sentido literal cuando los terminos son claros: la claridad es, literalmente, la mejor defensa.

**Extension razonable:** un prestamo entre particulares o un reconocimiento de deuda caben en dos o tres folios; un comodato, en dos; una compraventa de bien mueble, en dos. Un contrato de este tipo que pase de cinco folios casi siempre esta arrastrando clausulas de estilo innecesarias.

---

## Reglas de claridad y lenguaje

- Cada clausula transmite **una sola obligacion**, con sujeto, verbo y consecuencia identificables.
- Frases cortas. Evitar los periodos subordinados encadenados tipicos del formulario notarial antiguo.
- **Voz activa**: "EL PRESTATARIO devolvera", no "sera devuelto por el prestatario".
- **Nada de latinismos ni formulas rituales** sin contenido ("a todos los efectos oportunos", "en la mejor forma que en derecho proceda", "sirva el presente"). Si una formula no añade una consecuencia juridica, sobra.
- **Precision terminologica y constante:** PRESTAMISTA / PRESTATARIO, COMODANTE / COMODATARIO, ACREEDOR / DEUDOR, VENDEDOR / COMPRADOR. Elegida la denominacion, no alternarla nunca con sinonimos ("el que presta", "la parte prestadora") a lo largo del documento.
- **Cifras en numero y en letra** en todo importe relevante (principal, precio, cuotas, interes). Si hay discordancia, indicar en el propio contrato que prevalece la expresada en letra.
- No abusar de mayusculas, subrayados ni negritas. Reservar la negrita para los nombres de las partes en el encabezamiento y para las advertencias.

---

## Reglas de estructura

La estructura canonica del contrato entre particulares, comun a los cuatro assets:

1. **Titulo** del contrato, con los nombres de las partes.
2. **Header DRAFT** obligatorio del plugin.
3. **Lugar y fecha** de celebracion.
4. **REUNIDOS** — identificacion completa de cada parte: nombre o razon social, documento de identidad, domicilio a efectos de notificaciones, y en persona juridica la representacion con que actua. Cada dato en su propia linea, con salto duro.
5. **Reconocimiento reciproco de capacidad** — una sola frase, sin barroquismo.
6. **EXPONEN** — apartados romanos (I, II, III), cada uno con un hecho. Aqui se situa la **causa** del contrato: por que las partes contratan. Es el apartado que evita discusiones posteriores sobre la causa (arts. 1274 a 1277 CC).
7. **CLAUSULAS** numeradas en ordinal escrito (PRIMERA, SEGUNDA...), cada una con **rubrica** que anuncia su contenido. Orden natural: objeto — contraprestacion — plazo — obligaciones de cada parte — garantias — incumplimiento — forma — notificaciones — ley y fuero.
8. **FIRMAS** de todas las partes intervinientes, incluidos fiadores si los hay.
9. **Advertencias finales** del plugin.

---

## Reglas especificas del contenido

- **El objeto se describe hasta hacerlo inconfundible.** Un prestamo: importe exacto, moneda y **medio de entrega** (la transferencia bancaria identificable es preferible al efectivo, porque prueba la entrega). Un comodato o una compraventa de mueble: marca, modelo, numero de serie o bastidor, matricula, estado y accesorios.
- **La entrega se documenta, no se presume.** En el prestamo, indicar si el dinero ya se entrego (y como) o si se entrega en el acto. En el comodato y en la compraventa, si la cosa se entrega en el acto o en fecha posterior.
- **Toda obligacion de pago lleva: importe, fecha de vencimiento, medio de pago y cuenta de destino.** Sin los cuatro datos la clausula genera conflicto.
- **Los calendarios de cuotas van en tabla**, con numero de cuota, fecha de vencimiento e importe. Es el unico caso en que la tabla es preferible a la prosa.
- **El incumplimiento tiene consecuencia expresa.** No basta decir que el deudor "debera pagar": hay que decir desde cuando hay mora, que interes devenga y si se produce vencimiento anticipado.
- **Las clausulas que dependen de una decision del cliente se insertan o se omiten enteras**, nunca se dejan a medias ni con opciones alternativas visibles en el documento final.
- **La numeracion de las clausulas es dinamica.** Si un bloque condicional no se activa, las clausulas siguientes se renumeran: el documento final nunca salta de la QUINTA a la SEPTIMA.

---

## Reglas de cita normativa dentro del contrato

- Citar el articulo **solo cuando aporte algo**: cuando la clausula reproduce un regimen legal que conviene que las partes conozcan (art. 1755 CC sobre intereses, art. 1750 CC sobre reclamacion del comodato, art. 1490 CC sobre el plazo de saneamiento), o cuando la clausula se aparta del regimen dispositivo y conviene dejar constancia de que se hace conscientemente.
- Citarlo **con el nombre completo de la norma la primera vez** ("articulo 1.755 del Codigo Civil") y de forma abreviada despues.
- **Nunca transcribir literalmente el precepto** dentro de una clausula sin haberlo contrastado en el BOE en ese mismo lanzamiento.
- **Nunca citar jurisprudencia** en el cuerpo del contrato: no es su sitio y el guardrail de cero invenciones del plugin lo prohibe sin verificacion.

---

## Aplicacion en esta skill

Al rellenar los assets: clausulas numeradas y rubricadas, una obligacion por clausula, importes en numero y en letra, calendarios en tabla, denominacion de las partes constante, cero latinismos, cero comentarios HTML residuales y renumeracion coherente cuando un bloque condicional no se active. Las advertencias legales (usura, ausencia de fuerza ejecutiva del documento privado, plazo de saneamiento) se emiten **en el chat** al negociar la clausula correspondiente, y se recogen ademas en el bloque de advertencias finales del documento cuando afecten a la validez o a la exigibilidad.
