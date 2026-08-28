# Fuentes Oficiales y Tasas Vigentes

> Material de referencia para la skill `transferencia-vehiculo`. Registra las fuentes normativas, el
> procedimiento oficial de la DGT y las tasas vigentes que la skill verifica y, si detecta una version
> posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 1 se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada o un cambio en las tasas, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Reglamento General de Vehiculos (RD 2822/1998, texto consolidado) | BOE-A-1999-1826 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826 |
| RD 52/2026, modifica el RGV (Registro de Vehiculos Personales Ligeros) | BOE-A-2026-2140 | 28/01/2026 | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-2140 |
| TR Ley del ITP y AJD (RD Legislativo 1/1993) | BOE-A-1993-25359 | texto consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-1993-25359 |
| Orden de precios medios de venta de vehiculos (fiscalidad 2026) | Orden HAC/1501/2025 | BOE de 23/12/2025 | https://www.boe.es/diario_boe/ |

Articulos relevantes del RGV para esta skill: 32 (transmision entre personas que no se dedican a la compraventa; plazos del comprador y del vendedor) y 33 (transmision a favor de compraventa profesional).

---

## Procedimiento y tasas — Sede Electronica DGT

| Recurso | Detalle |
|---|---|
| Procedimiento de transferencia | https://sede.dgt.gob.es/es/vehiculos/transferencias-de-vehiculos/ |
| Pago y actualizacion de tasas | https://sede.dgt.gob.es/es/otros-tramites/compra-y-actualizacion-de-tasas/ |
| Descripcion de tasas | https://sede.dgt.gob.es/export/sites/dgt/.galleries/otros-tramites/pago-de-tasas/Descripcion_tasas_existentes.pdf |

| Tasa | Numero | Importe registrado |
|---|---|---|
| Transferencia de vehiculo (turismo y demas) | 1.5 | 55,70 EUR |
| Transferencia de ciclomotores y ligeros | 1.2 | 27,85 EUR |
| Notificacion de venta / custodia | 4.1 | 8,67 EUR |

---

## Fiscalidad autonomica (ITP)

| Recurso | Uso |
|---|---|
| Modelo 620 (Agencia Tributaria y Haciendas autonomicas) | Autoliquidacion del ITP en la transmision de vehiculos usados entre particulares |
| Orden anual de precios medios de venta | Base para el valor de mercado (valor venal) del vehiculo |

Los tipos de ITP y los plazos de presentacion los fija cada comunidad autonoma. Verificar con `web_search` el tipo y el plazo vigentes de la comunidad autonoma del comprador antes de estimar. Ver `itp-vehiculos-usados.md`.

---

## Verificacion de otras especialidades

Para vehiculos importados, vehiculos historicos, transmisiones con representacion (autorizacion a gestor) o vehiculos personales ligeros afectados por el RD 52/2026, verificar con `web_search` los requisitos vigentes antes de preparar el tramite.
