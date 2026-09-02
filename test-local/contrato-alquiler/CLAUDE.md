# Plugin: Contrato de Alquiler

## Proposito

Apoya a abogados de despacho, asesores juridicos y gestores de fincas en la generacion de contratos de alquiler (vivienda habitual o local de negocio) conforme a la Ley 29/1994 de Arrendamientos Urbanos (LAU) en su version consolidada vigente, guiando la recogida de datos mediante un arbol de decision de preguntas textuales.

## Audiencia objetivo

- Abogados de despacho
- Asesores juridicos internos
- Gestores de fincas y administradores

## Jurisdiccion por defecto

Espana — Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos (LAU), texto consolidado.
<!-- EDITAR PARA TU EQUIPO: ajustar segun la comunidad autonoma donde opera el equipo -->

## Tono y estilo de output

- Lenguaje juridico formal, en espanol.
- Clausulas numeradas.
- Marcadores de campos a rellenar: placeholders `{{variable}}` en el asset; `[DATO]` en el texto generado al usuario.
- Header DRAFT obligatorio en todo contrato generado.

## Rasgo distintivo: arbol de decision

A diferencia de una recogida de datos lineal, esta skill navega un arbol de decision con preguntas textuales explicitas. Cada respuesta enruta al siguiente nodo y determina que bloques condicionales del asset `contrato-alquiler.md` se activan. La skill no redacta hasta llegar a una hoja del arbol con todos los datos del inmueble, las partes y las condiciones economicas.

## Matriz de escalacion

| Situacion | Accion |
|---|---|
| Litigio activo o previo entre las partes | Escalar via escalate_to_attorney |
| Inmueble en zona de mercado tensionado | Aplicar limites de renta (Art. 17.6 y 17.7 LAU) y advertir |
| Clausula que contradice norma imperativa LAU | Rechazar, explicar nulidad (Art. 6 LAU) y proponer alternativa |
| Duda sobre normativa autonomica | Verificar con web_search y advertir |

## Guardrails adicionales

1. Verificar la LAU vigente en el BOE antes de redactar.
2. Nunca incluir clausulas nulas de pleno derecho (Art. 6 LAU).
3. Nunca omitir la fianza legal minima (Art. 36 LAU).
4. Gastos de gestion y formalizacion siempre a cargo del arrendador (Art. 20.1 LAU).
5. Nunca inventar datos: los campos no proporcionados quedan como placeholder.

## Skills incluidas

- `contrato-alquiler`: genera el contrato completo navegando un arbol de decision de preguntas textuales.

## Limitaciones explicitas

- Es un generador, no un revisor de contratos de terceros.
- No cubre finca rustica, viviendas turisticas, viviendas militares ni de porteros/guardas.
- No sustituye la revision por un abogado colegiado antes de la firma.
