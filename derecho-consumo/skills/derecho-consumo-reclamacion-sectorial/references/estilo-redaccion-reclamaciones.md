# Estilo de redacción de reclamaciones de consumo

Guía interna de redacción para esta skill. No se publica al usuario.

## Registro y tono

- El destinatario es una empresa o una administración, no un juzgado: tono firme, cortés y **breve**. Una reclamación de consumo que se lee en un minuto se resuelve antes.
- Evitar la retórica procesal («en méritos de lo expuesto», «esta parte») en el escrito dirigido a la empresa. Reservar el registro más jurídico para el escalado al organismo sectorial.
- Primera persona del singular cuando reclama un consumidor particular; primera del plural solo si reclaman varios titulares de la misma reserva o contrato.
- Nunca amenazar con acciones que no se van a ejercitar. Sí anunciar, en una línea, el paso siguiente real (organismo sectorial, consumo, arbitraje o juzgado).

## Estructura canónica

1. **Destinatario y fecha.**
2. **Datos del reclamante**, con un medio de contacto que la empresa pueda usar.
3. **Datos del contrato, reserva o pedido**, con el identificador que la empresa maneja (localizador, número de pedido, referencia de suministro). Sin ese identificador la reclamación se pierde en su sistema.
4. **Hechos**, en orden cronológico, con fechas e importes concretos. Un párrafo numerado por hecho.
5. **Fundamento**, corto: qué derecho se invoca y por qué se aplica al caso. Sin transcribir artículos enteros.
6. **Cuantificación** en tabla, con total.
7. **Petición** numerada, cada punto una acción concreta y verificable.
8. **Documentos que se acompañan**, numerados.

## Reglas de precisión

- **Fechas siempre absolutas** y completas. Prohibido «la semana pasada» o «hace un mes».
- **Importes con dos decimales** y en euros, y que la suma cuadre con el total pedido.
- Distinguir con rigor los conceptos que se acumulan (compensación, reembolso, gastos, indemnización): mezclarlos en una cifra única facilita que la empresa pague solo una parte.
- Pedir **plazo de respuesta concreto** y dejar constancia del medio de envío.
- Solicitar siempre el **número de incidencia**: es la prueba de la reclamación previa que exige el organismo sectorial.

## Prohibiciones de formato

- Marcadores siempre `{{VARIABLE}}` en mayúsculas y dobles llaves. Prohibidos los corchetes simples.
- Prohibidos los comentarios HTML y las notas condicionales dentro del documento entregado: la lógica condicional vive en el `SKILL.md`.
- Correos electrónicos y direcciones web en texto plano, sin enlaces Markdown ni `mailto:`.
- Sin emoticonos ni símbolos decorativos.
- Saltos de línea duros entre campos, un dato por línea, para que el escrito se lea bien en el editor.

## Control de calidad antes de entregar

1. El identificador del contrato, reserva o pedido está presente y es el que usa la empresa.
2. Las fechas permiten comprobar que el plazo se cumple, y el plazo está calculado en el escrito.
3. La cuantificación suma exactamente lo que se pide en la petición.
4. Cada documento mencionado en los hechos aparece en la relación final.
5. Ningún marcador `{{VARIABLE}}` olvidado en secciones ya confirmadas por el usuario.
6. Si el derecho invocado tiene una excepción que podría aplicarse al caso, está mencionada y descartada de forma expresa.
