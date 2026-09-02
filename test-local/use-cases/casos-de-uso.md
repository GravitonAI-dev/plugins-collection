# Casos de uso — skill `contrato-alquiler`

Casos de referencia para validar el arbol de decision. Todos los datos son genericos o placeholders; ninguno corresponde a personas reales.

## Caso 1 — Vivienda habitual, arrendador persona fisica, zona no tensionada

- Perfil: particular que alquila su piso a un inquilino.
- Ruta esperada del arbol: `N0-A -> N1V-fisica -> N2V-no -> N3 -> N4 -> HOJA`.
- Bloques activados: `vivienda`.
- Validaciones clave: duracion minima 5 anos; fianza minima 1 mensualidad.
- Resultado esperado: contrato de vivienda con prorroga del Art. 9/10 LAU, sin clausula de zona tensionada.

## Caso 2 — Vivienda habitual, arrendador persona juridica, zona tensionada

- Perfil: sociedad patrimonial que alquila vivienda en municipio tensionado.
- Ruta esperada: `N0-A -> N1V-juridica -> N2V-si -> N3 -> N4 -> HOJA`.
- Bloques activados: `vivienda`, `arrendador_juridica`, `zona_tensionada`.
- Validaciones clave: duracion minima 7 anos; limite de renta Art. 17.6 LAU; fianza minima 1 mensualidad.
- Resultado esperado: contrato con representante del arrendador, clausula de zona tensionada y advertencia de limite de renta.

## Caso 3 — Local de negocio, con garantia adicional y gastos a cargo del arrendatario

- Perfil: propietario que alquila un local para hosteleria.
- Ruta esperada: `N0-B -> N1L (actividad) -> N2L (cesion) -> N3 -> N4 -> HOJA`.
- Bloques activados: `local`, `garantia_adicional`, `gastos_arrendatario`.
- Validaciones clave: fianza minima 2 mensualidades; cesion/subarriendo por Art. 32 LAU.
- Resultado esperado: contrato de local con destino a la actividad, aval adicional y reparto de gastos generales.

## Caso 4 — Rama de fallback normativo

- Perfil: cualquiera de los anteriores cuando el BOE no responde.
- Comportamiento esperado: Paso 1.5 activa `web_search`; si tambien falla, se usa la referencia local y se emite la advertencia de verificacion manual.

## Caso 5 — Escalacion

- Perfil: existe litigio previo entre arrendador y arrendatario.
- Comportamiento esperado: la skill no redacta; escala via `escalate_to_attorney` (matriz de escalacion).
