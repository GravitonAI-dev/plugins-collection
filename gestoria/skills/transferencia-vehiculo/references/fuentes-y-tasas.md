# Fuentes Oficiales y Tasas Vigentes

> Material de referencia para la skill `transferencia-vehiculo`. Registra las fuentes normativas, el
> procedimiento oficial de la DGT y las tasas vigentes que la skill verifica y, si detecta una versión
> posterior, aplica la redacción vigente al documento que redacta en cada lanzamiento.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada o un cambio en las tasas, la skill aplica el dato vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Reglamento General de Vehículos (RD 2822/1998, texto consolidado) | BOE-A-1999-1826 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826 |
| RD 52/2026, modifica el RGV (Registro de Vehículos Personales Ligeros) | BOE-A-2026-2140 | 28/01/2026 | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-2140 |
| TR Ley del ITP y AJD (RD Legislativo 1/1993) | BOE-A-1993-25359 | texto consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-1993-25359 |
| Orden de precios medios de venta de vehículos (fiscalidad 2026) | Orden HAC/1501/2025 | BOE de 23/12/2025 | https://www.boe.es/diario_boe/ |

Artículos relevantes del RGV para esta skill: 32 (transmisión entre personas que no se dedican a la compraventa; plazos del comprador y del vendedor) y 33 (transmisión a favor de compraventa profesional).

---

## Procedimiento y tasas — Sede Electrónica DGT

| Recurso | Detalle |
|---|---|
| Procedimiento de transferencia | https://sede.dgt.gob.es/es/vehiculos/transferencias-de-vehiculos/ |
| Pago y actualización de tasas | https://sede.dgt.gob.es/es/otros-tramites/compra-y-actualizacion-de-tasas/ |
| Descripción de tasas | https://sede.dgt.gob.es/export/sites/dgt/.galleries/otros-tramites/pago-de-tasas/Descripcion_tasas_existentes.pdf |

| Tasa | Número | Importe registrado |
|---|---|---|
| Transferencia de vehículo (turismo y demás) | 1.5 | 55,70 EUR |
| Transferencia de ciclomotores y ligeros | 1.2 | 27,85 EUR |
| Notificación de venta / custodia | 4.1 | 8,67 EUR |

---

## Fiscalidad autonómica (ITP)

| Recurso | Uso |
|---|---|
| Modelo 620 (Agencia Tributaria y Haciendas autonómicas) | Autoliquidación del ITP en la transmisión de vehículos usados entre particulares |
| Orden anual de precios medios de venta | Base para el valor de mercado (valor venal) del vehículo |

Los tipos de ITP y los plazos de presentación los fija cada comunidad autónoma. Verificar con `web_search` el tipo y el plazo vigentes de la comunidad autónoma del comprador antes de estimar. Ver `itp-vehiculos-usados.md`.

---

## Verificación de otras especialidades

Para vehículos importados, vehículos históricos, transmisiones con representación (autorización a gestor) o vehículos personales ligeros afectados por el RD 52/2026, verificar con `web_search` los requisitos vigentes antes de preparar el trámite.
