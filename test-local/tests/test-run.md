# Test de ejecucion — skill `contrato-alquiler`

Ejecucion manual del arbol de decision sobre dos escenarios. Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el relleno del asset.

## Verificacion normativa (Paso 1)

- Fuente: BOE, Ley 29/1994 (LAU), texto consolidado.
- En este test la lectura online se marca como no disponible -> se aplica Paso 1.5 (fallback) y se usa la fecha de referencia local.
- `fecha_verificacion_lau` = 25/05/2023 (Ley 12/2023) [verificar manualmente en produccion].

---

## Test 1 — Caso 1 (vivienda, arrendador persona fisica, no tensionada)

### Recorrido del arbol
```
N0  -> "A" (vivienda)                         activa BLOQUE vivienda
N1V -> "persona fisica"                        plazo_minimo = 5
N2V -> "no"                                     (sin zona_tensionada)
N3  -> renta 800, duracion 5, fianza 1,
        indice IGC, gastos NO, garantia NO,
        accesorios NO
N4  -> datos de partes e inmueble
HOJA -> generar
```
Ruta: `N0-A -> N1V-fisica -> N2V-no -> N3 -> N4 -> HOJA`
Bloques activados: `vivienda`.

### Validaciones
- Duracion 5 >= minimo 5: OK.
- Fianza 1 mensualidad >= minimo vivienda (1): OK.
- Zona tensionada: no aplica.

### Contrato generado (extracto relleno)
```
CONTRATO DE ARRENDAMIENTO DE VIVIENDA — ARRENDADOR A / ARRENDATARIO A
> DRAFT — para revision por un abogado antes de su firma.
> Version de la LAU verificada en el BOE: 25/05/2023

REUNIDOS
ARRENDADOR: ARRENDADOR A — NIF 00000000-T — Calle Ejemplo 1, Ciudad — persona fisica
ARRENDATARIO: ARRENDATARIO A — NIF 11111111-H — Calle Ejemplo 2, Ciudad — persona fisica

PRIMERA — Objeto: vivienda sita en Calle Ejemplo 1, Ciudad (CCAA Ejemplo, CP 00000),
  ref. catastral 0000000AA0000A0000AA. Descripcion: 70 m2 utiles, 3 hab., 1 bano, salon, cocina.
SEGUNDA — Destino: vivienda habitual (Art. 2 LAU).
TERCERA — Duracion: 5 anos desde 01/09/2026. Prorroga Art. 9/10 LAU.
CUARTA — Renta: 800 euros/mes (primeros 7 dias, transferencia).
SEXTA — Fianza: 800 euros (1 mensualidad, Art. 36.1 LAU).
SEPTIMA — Gastos de gestion a cargo del ARRENDADOR (Art. 20.1 LAU).
```
Resultado: **PASA**. El contrato no contiene bloques `local`, `zona_tensionada`, `gastos_arrendatario` ni `garantia_adicional`.

---

## Test 2 — Caso 3 (local, garantia adicional, gastos al arrendatario)

### Recorrido del arbol
```
N0  -> "B" (local)                              activa BLOQUE local
N1L -> actividad = "cafeteria"
N2L -> cesion "si (Art. 32 LAU)"
N3  -> renta 1500, duracion 5, fianza 2,
        indice IPC, gastos SI, garantia SI, accesorios NO
N4  -> datos de partes e inmueble
HOJA -> generar
```
Ruta: `N0-B -> N1L -> N2L -> N3 -> N4 -> HOJA`
Bloques activados: `local`, `garantia_adicional`, `gastos_arrendatario`.

### Validaciones
- Fianza 2 mensualidades >= minimo local (2): OK.
- Cesion/subarriendo por Art. 32 LAU: reflejado en clausula novena (rama local).

### Contrato generado (extracto relleno)
```
CONTRATO DE ARRENDAMIENTO DE LOCAL DE NEGOCIO — ARRENDADOR B / ARRENDATARIO B
> DRAFT — para revision por un abogado antes de su firma.
> Version de la LAU verificada en el BOE: 25/05/2023

PRIMERA — Objeto: local sito en Avenida Ejemplo 10, Ciudad.
SEGUNDA — Destino: ejercicio de la actividad de cafeteria (Art. 3 LAU).
CUARTA — Renta: 1500 euros/mes.
SEXTA — Fianza: 3000 euros (2 mensualidades, Art. 36.1 LAU).
        GARANTIA ADICIONAL: aval bancario por 3000 euros.
SEPTIMA — Gastos generales (comunidad, IBI, seguro) a cargo del ARRENDATARIO: 1200 euros/ano.
NOVENA — Cesion/subarriendo conforme al Art. 32 LAU, con notificacion en un mes.
```
Resultado: **PASA**. El contrato no contiene bloques `vivienda` ni `zona_tensionada`.

---

## Resumen del test

| Test | Ruta | Bloques activados | Validaciones | Resultado |
|---|---|---|---|---|
| 1 | N0-A / N1V-fisica / N2V-no | vivienda | duracion, fianza | PASA |
| 2 | N0-B / N1L / N2L | local, garantia_adicional, gastos_arrendatario | fianza, cesion | PASA |

Conclusion: el arbol de decision enruta correctamente, activa solo los bloques de la rama recorrida y aplica las validaciones de la LAU. Pendiente en produccion: verificacion en vivo del BOE (Paso 1).
