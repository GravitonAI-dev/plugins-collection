# Estilo de redacción de documentación de cumplimiento

Guía interna de redacción para este plugin. No se publica al usuario.

## Principio rector: el documento es una prueba

Todo lo que se redacta aquí puede acabar en manos de un inspector, de la autoridad de control o de un juzgado. De ahí tres consecuencias que gobiernan la redacción:

1. **Fechable y versionable.** Todo documento lleva fecha de aprobación, órgano que aprueba, número de versión e historial. Un protocolo sin fecha no acredita nada.
2. **Verificable.** Cada afirmación debe poder comprobarse: si dice que se imparte formación, debe existir registro de asistencia; si dice que hay cifrado, debe existir la configuración.
3. **Cierto.** Prohibido declarar medidas, plazos o procedimientos que la empresa no aplica. Documentar un cumplimiento inexistente convierte un incumplimiento en una declaración falsa, y agrava la responsabilidad.

## Estructura canónica

1. **Identificación de la entidad** (razón social, CIF, domicilio, actividad y plantilla), porque los umbrales de plantilla determinan qué obligaciones son exigibles.
2. **Objeto y ámbito de aplicación**: a quién se aplica el documento (personas trabajadoras, directivos, becarios, personal de empresas contratistas, candidatos).
3. **Cuerpo por apartados numerados**, con un apartado por obligación.
4. **Responsables y plazos**: cada obligación con una persona o cargo responsable y un plazo o periodicidad.
5. **Aprobación, publicación y difusión**: cómo se aprueba, dónde se publica y cómo se acredita que las personas afectadas lo conocen.
6. **Control de versiones y revisión.**

## Reglas de redacción

- **Tiempo verbal:** presente de indicativo con sujeto explícito ("la empresa notificará", "el responsable del sistema acusará recibo"). Nunca pasiva refleja sin sujeto: sin sujeto no hay responsable.
- **Plazos en cifras y en unidad exacta**, diciendo si son días naturales o hábiles.
- **Umbrales:** cuando la obligación dependa del número de personas trabajadoras, consignar el número real de la empresa y el umbral legal, para que se vea por qué aplica.
- **Sin condicionales vacíos:** evitar "se podrá" cuando la ley obliga. Si es obligatorio, se escribe como obligación.
- **Citas normativas:** nombrar la norma con su número y su denominación. No inventar artículos: si no se tiene certeza del número, describir la regla sin numerarla.
- **Terminología constante:** una misma figura se nombra siempre igual en todo el documento ("responsable del sistema", no "encargado del canal" en un apartado y "gestor" en otro).

## Prohibiciones de formato

- Marcadores siempre `{{VARIABLE}}` en mayúsculas y dobles llaves. Prohibidos los corchetes simples.
- Prohibidos los comentarios HTML y las notas condicionales dentro del documento entregado: toda la lógica condicional vive en el `SKILL.md`.
- Correos electrónicos y direcciones web en texto plano, sin enlaces Markdown ni `mailto:`.
- Sin emoticonos ni símbolos decorativos.
- Un dato por línea, con saltos duros entre bloques, para que el documento se lea bien en el editor.

## Advertencias que deben aparecer siempre

- Cabecera DRAFT al inicio.
- Qué ocurre si la obligación no se cumple (sanción, nulidad, inversión de la carga de la prueba). Es lo que permite al cliente decidir.
- Que el documento exige **implantación real**: publicación, formación, registro y revisión periódica.
- Cuándo la obligación deja de ser documental y pasa a exigir intervención profesional (investigación en curso, brecha activa, caso de acoso actual, expediente sancionador).

## Control de calidad antes de entregar

1. El número de personas trabajadoras consta y sostiene las obligaciones que se declaran exigibles.
2. Cada obligación tiene responsable, plazo y forma de acreditarse.
3. No hay ninguna medida declarada que la empresa no aplique.
4. El documento tiene fecha, versión y órgano de aprobación.
5. Ningún marcador `{{VARIABLE}}` olvidado en apartados ya confirmados por el usuario.
6. Los canales y direcciones de contacto que figuran existen y están operativos.
