# RETA — Cotizacion por Rendimientos Reales y Tarifa Plana

> Material de referencia para la skill `alta-baja-autonomo`. Resume el sistema de cotizacion del Regimen
> Especial de Trabajadores Autonomos (RETA) por rendimientos netos, conforme al RD-ley 13/2022 y a la
> tabla de cuotas del ejercicio en curso, y las reglas de la baja en el RETA. TODOS los importes son
> ORIENTATIVOS: la skill los verifica en el Paso 1 y los marca `[verificar]`; se regularizan anualmente
> segun los rendimientos reales.

---

## Sistema de cotizacion por rendimientos reales

Desde el 1 de enero de 2023 (RD-ley 13/2022), el autonomo cotiza al RETA en funcion de sus rendimientos netos anuales previstos. Elige una base de cotizacion dentro del tramo que corresponde a esos rendimientos; la cuota mensual resulta de aplicar el tipo de cotizacion a la base elegida.

- Puede cambiar de base hasta seis veces al ano si sus previsiones varian.
- Al ano siguiente, la Seguridad Social cruza datos con la AEAT y REGULARIZA: si cotizo de menos, abona la diferencia; si cotizo de mas, se le devuelve.
- El tipo de cotizacion incluye el MEI (Mecanismo de Equidad Intergeneracional).

---

## Tabla de tramos y cuotas (ejercicio en curso) [verificar]

> Importes ORIENTATIVOS. La tabla de cuotas del ejercicio en curso quedo congelada respecto al ejercicio
> anterior. Verificar en el Paso 1 los tramos, las bases minimas y las cuotas vigentes antes de usarlos.

| Tramo | Tabla | Rendimientos netos mensuales | Cuota mensual orientativa [verificar] |
|---|---|---|---|
| 1 | Reducida | hasta 670 euros | ~200 euros |
| 2 | Reducida | 670 - 900 euros | ~220 euros |
| 3 | Reducida | 900 - 1.166,70 euros | ~260 euros |
| 4 | General | 1.166,70 - 1.300 euros | ~291 euros |
| 5 | General | 1.300 - 1.500 euros | ~294 euros |
| 6 | General | 1.500 - 1.700 euros | ~302 euros |
| 7 | General | 1.700 - 1.850 euros | ~350 euros |
| 8 | General | 1.850 - 2.030 euros | ~370 euros |
| 9 | General | 2.030 - 2.330 euros | ~390 euros |
| 10 | General | 2.330 - 2.760 euros | ~423 euros |
| 11 | General | 2.760 - 3.190 euros | ~451 euros |
| 12 | General | 3.190 - 3.620 euros | ~468 euros |
| 13 | General | 3.620 - 4.050 euros | ~504 euros |
| 14 | General | 4.050 - 6.000 euros | ~530 euros |
| 15 | General | mas de 6.000 euros | ~590 euros |

Parametros de referencia [verificar]:
- Base maxima general: ~4.720,50 euros/mes.
- Tipo de cotizacion: ~31,4 % (contingencias comunes y profesionales, cese de actividad, formacion y MEI).
- MEI: sube al 0,9 % de la base, a cargo integro del autonomo.

---

## Tarifa plana (cuota reducida de inicio de actividad) [verificar]

Cuota reducida para quienes inician su actividad como autonomos:

| Aspecto | Detalle [verificar] |
|---|---|
| Cuota | ~80 euros/mes durante los primeros 12 meses (mas MEI, ~85-88 euros totales) |
| Prorroga | Segundo periodo de 12 meses a cuota reducida si los rendimientos netos no superan el SMI |
| Requisito 1 | No haber estado de alta en el RETA en los 2 anos anteriores (3 si ya disfruto antes de la bonificacion) |
| Requisito 2 | No ser autonomo colaborador |
| Requisito 3 | No tener deudas pendientes con la Seguridad Social ni con la AEAT |
| Solicitud | Marcar la bonificacion al tramitar el alta en el RETA (Import@ss), antes del inicio |

Si el usuario no cumple los requisitos o hay duda, NO aplicar la tarifa plana: usar la cuota del tramo y advertir.

---

## Presentacion del alta en el RETA

| Aspecto | Detalle |
|---|---|
| Organismo | Tesoreria General de la Seguridad Social (TGSS) |
| Sede | Import@ss (portal de la Seguridad Social) e Importass app |
| Identificacion | Certificado digital, DNI electronico o Cl@ve |
| Plazo | Hasta 60 dias naturales antes del inicio; efectos desde la fecha de inicio real de la actividad |
| Base de la cuota | Rendimientos netos previstos, elegidos por el interesado dentro del tramo |

---

## Baja en el RETA (cese de actividad)

Al cesar la actividad, el autonomo debe comunicar la baja en el RETA. Es el tramite mas urgente del cese por su plazo corto.

| Aspecto | Detalle [verificar] |
|---|---|
| Organismo | Tesoreria General de la Seguridad Social (TGSS) |
| Sede | Import@ss (portal de la Seguridad Social) e Importass app |
| Identificacion | Certificado digital, DNI electronico o Cl@ve |
| Plazo | 3 dias naturales siguientes al cese de la actividad (se cuentan fines de semana y festivos) |
| Fecha de efecto | La fecha real de cese, si se comunica en plazo; si se comunica fuera de plazo, la fecha de presentacion |

### Efectos en la cuota

Desde el sistema de cotizacion por rendimientos reales (RD-ley 13/2022):

- Las **tres primeras bajas de cada ano natural** surten efecto desde el dia del cese: se cotiza solo por los dias efectivamente trabajados de ese mes (prorrata diaria).
- A partir de la **cuarta baja del mismo ano natural**, se cotiza el **mes completo** aunque el cese sea a mitad de mes.
- Si la baja se comunica **fuera del plazo de 3 dias**, surte efecto la fecha de presentacion y se generan cuotas hasta entonces, aunque no haya habido actividad.

Marcar estas reglas como `[verificar]` y confirmarlas en el Paso 1, ya que dependen de la normativa del ejercicio en curso.

### Obligaciones tras la baja

- La baja en el RETA no da derecho automatico a prestacion: la prestacion por cese de actividad (paro del autonomo) es un tramite distinto, con requisitos propios, que EXCEDE el alcance de esta skill.
- Regularizar la cotizacion del ejercicio del cese segun los rendimientos reales cuando la AEAT los comunique a la TGSS.

---

