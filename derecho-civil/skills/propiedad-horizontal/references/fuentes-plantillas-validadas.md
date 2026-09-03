# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-propiedad-horizontal`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso de verificacion se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| LPH — Ley 49/1960, de 21 de julio, sobre propiedad horizontal (texto consolidado) | BOE-A-1960-10906 | consolidado, ultima actualizacion del texto 23/03/2026 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906 |
| LEC — Ley 1/2000, de 7 de enero, de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LO 1/2025, de 2 de enero, de medidas en materia de eficiencia del Servicio Publico de Justicia | BOE-A-2025-76 | publicada 03/01/2025, en vigor 03/04/2025 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |

### API de legislacion consolidada del BOE (metodo de verificacion usado)

La verificacion se hizo contra la API de datos abiertos del BOE, que devuelve el texto consolidado bloque a bloque y el historial de modificaciones de cada articulo:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1960-10906/texto
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1960-10906/metadatos
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a813
```

Los identificadores de bloque de la LPH son ordinales en letra (`aseptimo`, `anoveno`, `adiecisiete`, `adieciocho`, `aveintiuno`); los de la LEC son `a` + numero (`a249`, `a812`, `a813`, `a814`, `a815`, `a818`, `a264`, `a403`). Cada bloque incluye varias `<version>`: **la vigente es la ultima**.

---

## Articulos verificados de la LPH (redaccion vigente el 31/08/2026)

| Articulo | Materia | Ultima modificacion verificada |
|---|---|---|
| 7.2 | Actividades prohibidas, dañosas, molestas, insalubres, nocivas, peligrosas o ilicitas. Requerimiento del presidente, accion de cesacion por juicio ordinario, medidas cautelares y consecuencias de la sentencia | Ley 1/2000 (parrafo tercero) sobre la redaccion de la Ley 8/1999 |
| 7.3 | Alquiler turistico (art. 5.e LAU): requiere aprobacion expresa previa de la comunidad; el presidente requiere la cesacion de la actividad no aprobada, con remision al 7.2 | Apartado AÑADIDO por la disposicion final 4.1 de la LO 1/2025, con efectos de 03/04/2025 |
| 9.1.e) | Obligacion de contribuir a los gastos generales; credito preferente (art. 1923 CC) y afeccion real del piso o local por la anualidad en curso y los tres años naturales anteriores; certificacion de deudas para transmitir (7 dias naturales) | Ley 8/2013 |
| 9.1.f) | Fondo de reserva, no inferior al 10 % del ultimo presupuesto ordinario | Ley 10/2022, de 14 de junio |
| 9.1.h) | Domicilio en España a efectos de notificaciones; en su defecto, el piso o local; si resulta imposible, tablon de anuncios con diligencia firmada por el secretario con el visto bueno del presidente, con plenos efectos a los tres dias naturales | Ley 8/1999 |
| 9.1.i) | Deber de comunicar el cambio de titularidad; responsabilidad solidaria del transmitente que lo incumple por las deudas posteriores | Ley 8/1999 |
| 17 | Regimen de mayorias de la junta (1/3, mayoria simple, 3/5, unanimidad, voto presunto del ausente en 30 dias naturales, alquiler turistico 3/5 en el 17.12) | Apartado 12 modificado por la LO 1/2025 con efectos de 03/04/2025; apartado 1 modificado por el RDL 7/2026, de 20 de marzo |
| 18 | Impugnacion de acuerdos: supuestos, legitimacion, requisito de estar al corriente, plazos de caducidad y no suspension automatica | Ley 8/1999 (sin modificaciones posteriores) |
| 21 | Impago de gastos comunes, medidas disuasorias, reclamacion por el proceso monitorio especial y mediacion o arbitraje | **Ley 10/2022, de 14 de junio** (art. 2.3), en vigor desde el 16/06/2022 |

**Nota sobre el art. 21:** la reforma en vigor es la de la **Ley 10/2022, de 14 de junio**, que traia causa del RDL 19/2021, de 5 de octubre. No consta ninguna modificacion posterior del art. 21 en el texto consolidado a 23/03/2026. El texto vigente ya no contiene la regla de competencia territorial del lugar de la finca que figuraba en la version de 1999: esa regla vive hoy en el art. 813 de la LEC.

---

## Articulos verificados de la LEC (redaccion vigente el 31/08/2026)

| Articulo | Contenido verificado |
|---|---|
| 249.1.8º | Se deciden en juicio ordinario, cualquiera que sea su cuantia, las acciones que la Ley 49/1960 otorga a las Juntas de Propietarios y a estos, **siempre que no versen exclusivamente sobre reclamaciones de cantidad**, en cuyo caso se tramitan por las reglas del juicio verbal o por el procedimiento especial que corresponda. Redaccion del RDL 6/2023, en vigor desde el 20/03/2024 |
| 812.2.2º | Cabe el monitorio cuando la deuda se acredite **mediante certificaciones de impago de cantidades debidas en concepto de gastos comunes de Comunidades de propietarios de inmuebles urbanos** |
| 813 | Competencia exclusiva del Juzgado de Primera Instancia del domicilio o residencia del deudor; **en el caso del art. 812.2.2º es tambien competente el Juzgado del lugar donde se halle la finca, a eleccion del solicitante**. No cabe sumision expresa ni tacita |
| 814.1 | Contenido de la peticion inicial: identidad del deudor, domicilios, origen y cuantia de la deuda, con los documentos del art. 812. Puede extenderse en impreso o formulario, tambien por sede electronica. Redaccion del RDL 6/2023 |
| 815.1 | Requerimiento de pago en veinte dias; la oposicion debe ser **fundada y motivada** |
| 815.2 | En las reclamaciones del art. 812.2.2º la notificacion se practica en el domicilio previamente designado por el deudor para los asuntos de la comunidad; si no lo hubiera designado, **en el propio piso o local**; y si tampoco fuera posible, conforme al art. 164 (edictos) |
| 815.3 | Control judicial del importe y de las clausulas abusivas en contratos entre empresario o profesional y consumidor. Redaccion del RDL 6/2023 (el antiguo 815.4 quedo refundido aqui) |
| 818 | Oposicion del deudor: hasta 15.000 euros el asunto sigue por el verbal (impugnacion de la oposicion en 10 dias); por encima, el acreedor debe demandar en ordinario en el plazo de un mes desde el traslado de la oposicion. Apartado 2 modificado por la LO 1/2025 con efectos de 03/04/2025 |
| 249.2 y 250.2 | Umbral de 15.000 euros entre ordinario y verbal (RDL 6/2023, en vigor 20/03/2024) |
| 264.4º | Debe acompañarse a la demanda el documento que acredite haberse intentado la actividad negociadora previa cuando la ley la exija como requisito de procedibilidad. Punto AÑADIDO por la LO 1/2025 con efectos de 03/04/2025 |
| 403.2 | No se admiten las demandas que no acompañen los documentos exigidos ni las que omitan las circunstancias del art. 399.3 cuando el MASC sea requisito de procedibilidad. Modificado por la LO 1/2025 |
| 23.2.1º y 31.2.1º | No son preceptivos procurador ni abogado en los verbales por cuantia que no exceda de 2.000 euros **ni para la peticion inicial de los procedimientos monitorios** |

---

## Plantillas validadas — Modelos Normalizados del CGPJ

### Proceso monitorio

| Recurso | Detalle |
|---|---|
| Nombre | Guia sobre el Procedimiento Monitorio y Proceso Monitorio. Modelo normalizado (PDF y Word) |
| Landing oficial | https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/El-proceso-monitorio |
| Verificacion | Landing accesible el 31/08/2026; ultima actualizacion publicada 01/08/2025 |
| Alcance | Modelo **generico** de monitorio. **No existe modelo normalizado especifico del CGPJ para el monitorio de cuotas de comunidad de propietarios**: el asset `assets/peticion-monitorio-cuotas-lph.md` toma la estructura del modelo generico y le añade los requisitos propios del art. 21 de la LPH y de los arts. 812.2.2º, 813 y 815.2 de la LEC |

### Documentos sin modelo normalizado oficial

| Asset | Base estructural |
|---|---|
| `assets/certificacion-deuda-comunidad.md` | Art. 21.3 de la LPH (certificado del acuerdo de liquidacion emitido por quien haga las funciones de secretario, con el visto bueno del presidente, con importe adeudado y su desglose) y art. 9.1.h) de la LPH (notificacion al deudor y notificacion subsidiaria en el tablon de anuncios) |
| `assets/demanda-impugnacion-acuerdos.md` | Arts. 399 y 249.1.8º de la LEC y art. 18 de la LPH |
| `assets/requerimiento-cesacion-actividad.md` | Art. 7.2 de la LPH (requerimiento previo del presidente como presupuesto de la accion de cesacion) |

---

## Guias de estilo de redaccion judicial (consulta)

| Recurso | Uso |
|---|---|
| Guia de redaccion judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminologia y correccion del lenguaje juridico |

Ver `references/estilo-redaccion-escritos.md`.

---

## Notas de verificacion (31/08/2026)

- La redaccion literal de los arts. 7, 9, 17, 18 y 21 de la LPH y de los arts. 249, 264, 403, 812, 813, 814, 815 y 818 de la LEC se extrajo directamente de la API de legislacion consolidada del BOE (respuestas con `status 200`), tomando en cada bloque la ultima `<version>`. No se han usado repositorios secundarios.
- El texto consolidado de la LPH tiene fecha de actualizacion 23/03/2026 (metadato `fecha_actualizacion`), por la modificacion del art. 17.1 operada por el RDL 7/2026, de 20 de marzo. Esa modificacion no afecta a los articulos que usa esta skill.
- **Verificar manualmente antes de presentar un escrito:** los criterios del juzgado competente sobre la exigencia de MASC en el monitorio de cuotas (ver `references/masc-y-requisitos-previos-lph.md`) y la eventual existencia de estatutos o titulo constitutivo que alteren el regimen legal supletorio (cuotas, mayorias, actividades prohibidas). Ninguna de las dos cosas es verificable desde una fuente publica.
- **Verificar manualmente:** la posible normativa autonomica o sectorial turistica aplicable al alquiler de uso turistico en el municipio de la finca, que condiciona los supuestos de los arts. 7.3 y 17.12 de la LPH.
