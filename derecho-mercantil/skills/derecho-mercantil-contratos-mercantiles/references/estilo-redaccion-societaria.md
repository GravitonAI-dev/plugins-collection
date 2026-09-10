# Estilo de redacción societaria y mercantil

Guía interna de redacción para los documentos de este plugin. No se publica al usuario.

## Estructura canónica del documento societario

1. **Encabezamiento:** tipo de documento y denominación de la sociedad en mayúsculas.
2. **Comparecencia o intervinientes:** identidad completa, NIF/NIE/CIF, domicilio y, cuando actúe una persona jurídica, sus datos registrales (tomo, folio, hoja, inscripción) y el título de representación.
3. **Exponen / Antecedentes:** hechos y voluntad de las partes, numerados con ordinales en negrita.
4. **Estipulaciones, artículos o acuerdos:** numeración correlativa. En estatutos, agrupación por capítulos y artículos. En contratos, estipulaciones. En actas, acuerdos por punto del orden del día.
5. **Cierre:** lugar, fecha y firmas. En actas, firma del presidente y del secretario.

## Reglas de redacción

- **Tiempo verbal:** presente de indicativo para las obligaciones ("la sociedad hará constar", "el socio comunicará"). Evitar el futuro de mandato salvo en la fórmula estatutaria clásica.
- **Terminología exacta:** en sociedad limitada se dice *participaciones sociales* y *socios*, nunca *acciones* ni *accionistas*. El órgano es *junta general*, no *asamblea*. La administración es *órgano de administración*.
- **Cifras:** los importes se expresan en letra y en número cuando aparecen por primera vez, y siempre en euros. El valor nominal debe ser divisor exacto del capital.
- **Numeración de participaciones:** siempre correlativa, con expresión "del X al Y, ambos inclusive", sin solapamientos entre socios.
- **Remisión a la ley:** cuando el pacto reproduzca el régimen legal supletorio, es preferible remitirse a la ley que transcribirla, salvo en estatutos, donde la transcripción facilita la calificación registral.
- **Citas normativas:** citar el precepto con el artículo y la norma abreviada ya presentada (por ejemplo, "Art. 108 LSC"). No inventar numeraciones: si no se tiene certeza del artículo, describir la regla sin numerarla.

## Prohibiciones de formato

- Prohibido el uso de corchetes simples para huecos: los marcadores son siempre `{{VARIABLE}}` en mayúsculas y con dobles llaves.
- Prohibidos los comentarios HTML y las notas condicionales dentro del documento entregado. Toda la lógica condicional vive en el SKILL.md, no en el asset.
- Prohibidos los emoticonos y los símbolos decorativos.
- Los correos electrónicos y las direcciones web se escriben en texto plano, sin enlaces Markdown ni `mailto:`.
- Saltos de línea duros entre bloques: cada campo de datos en su propia línea, para que el documento se lea correctamente en el editor.

## Advertencias que deben aparecer siempre

- Cabecera DRAFT al inicio del documento.
- Cuando el documento exija forma pública: advertencia de que se trata de una minuta para el notario y que la escritura la redacta y autoriza él.
- Cuando el documento deba inscribirse: mención del registro competente y del plazo de presentación.
- Cuando existan cláusulas cuya validez dependa de un límite temporal o de un derecho de separación (prohibición de transmitir, permanencia): advertencia expresa del límite legal.

## Control de calidad antes de entregar

1. Coherencia aritmética: capital, número de participaciones y valor nominal cuadran; la suma de lo suscrito por cada socio iguala el capital.
2. Coherencia de identidades: la misma persona se nombra igual en toda la minuta.
3. Coherencia con la clasificación: la forma de administración pactada es la que se refleja en el articulado y en el nombramiento.
4. Ningún marcador `{{VARIABLE}}` olvidado en secciones ya confirmadas por el usuario.
5. Ninguna cláusula nula: revisar en particular las restricciones a la transmisión de participaciones y los pactos de permanencia sin plazo.
