# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-herencia`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica en cada lanzamiento para aplicar la redacción vigente al documento que redacta.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada (verificada 31/08/2026) | URL |
|---|---|---|---|
| Código Civil (texto consolidado) | BOE-A-1889-4763 | consolidado, última actualización publicada el 03/01/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado, última actualización publicada el 28/02/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LO 1/2025 de eficiencia del Servicio Público de Justicia (MASC) | BOE-A-2025-76 | 02/01/2025 (en vigor 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |
| Ley 29/1987 del Impuesto sobre Sucesiones y Donaciones | BOE-A-1987-28141 | consolidado, última actualización publicada el 28/12/2022 | https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141 |
| RD 1629/1991, Reglamento del ISD | BOE-A-1991-27678 | consolidado, última actualización publicada el 05/04/2023 | https://www.boe.es/buscar/act.php?id=BOE-A-1991-27678 |
| TR Ley Reguladora de las Haciendas Locales (plusvalía municipal, IIVTNU) | BOE-A-2004-4214 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 |

Artículos relevantes verificados para esta skill (redacción vigente comprobada en el texto consolidado del BOE el 31/08/2026):

- **Código Civil:** 657 y ss. (apertura de la sucesión); 806 a 808 (legítima; el 808 en su redacción por la Ley 8/2021); 834 y ss. (cónyuge viudo); 912 y ss. (sucesión intestada); 988 a 1009 (aceptación y repudiación: 988 voluntariedad, 989 retroacción, 997 irrevocabilidad, 998-1000 formas y aceptación tácita, 1003 responsabilidad ultra vires de la aceptación pura, **1005 interpelación notarial con plazo de TREINTA DÍAS NATURALES y silencio = aceptación pura y simple** (redacción por la Ley 15/2015, en vigor desde el 23/07/2015), **1008 repudiación ante Notario en instrumento público** (redacción por la Ley 15/2015)); 1010 a 1034 (beneficio de inventario: 1011 declaración ante Notario, 1014-1015 plazo de treinta días, 1023 efectos); 1035 y ss. (colación); 1051 y ss. (partición: 1052 legitimación, 1059 remisión a la LEC a falta de acuerdo, 1061-1062 igualdad de lotes e indivisibles).
- **LEC:** 52.1.4 (competencia territorial en cuestiones hereditarias: último domicilio del finado); 264 y 399.3 (acreditación del MASC); 403.2 (inadmisión sin MASC, redacción por la LO 1/2025); **782 a 789 (división judicial de la herencia:** 782 solicitud y legitimación, 783 junta, 784 contador y peritos, 786 operaciones divisorias, 787 aprobación y oposición, 788 entrega, 789 terminación por acuerdo).
- **LO 1/2025:** art. 5 (requisito de procedibilidad MASC: exigible en los procesos especiales del Libro IV de la LEC — donde se ubica la división judicial de la herencia —, que no figura entre las excepciones del art. 5.2).
- **Ley 29/1987 (ISD):** art. 28 (repudiación y renuncia: en la renuncia pura, simple y gratuita tributan los beneficiarios; en la renuncia a favor de persona determinada tributa el renunciante y además se liquida la cesión o donación; la renuncia tras prescribir el impuesto se reputa donación).
- **RD 1629/1991:** art. 67.1.a (plazo de presentación de 6 meses desde el fallecimiento) y art. 68 (prórroga por otro plazo igual, solicitada dentro de los 5 primeros meses; silencio positivo al mes; devenga intereses de demora).

---

## Plantillas del plugin

| Asset | Base |
|---|---|
| `assets/cuaderno-particional.md` | Estructura estándar de escritura de aceptación y partición de herencia: comparecencia, exposición (título sucesorio), inventario y avalúo, liquidación del haber, formación de lotes y adjudicaciones (Arts. 1058, 1061-1062, 1068 CC) |
| `assets/aceptacion-herencia.md` | Documento de aceptación pura y simple o a beneficio de inventario (Arts. 988, 998, 1003, 1010-1034 CC). El bloque opcional de renuncia que contiene NO se usa: la renuncia se genera siempre con `assets/renuncia-herencia.md` |
| `assets/renuncia-herencia.md` | Minuta de renuncia (repudiación) de herencia para su elevación a escritura pública notarial (Art. 1008 CC), con advertencia de irrevocabilidad (Art. 997 CC) y de la fiscalidad de la renuncia pura frente a la traslativa (Art. 28 Ley 29/1987) |
| `assets/requerimiento-1005-cc.md` | Solicitud de interpelación notarial al heredero que no acepta ni repudia (Art. 1005 CC): plazo de 30 días naturales y efecto de aceptación pura y simple si calla |
| `assets/solicitud-division-judicial-herencia.md` | Solicitud de división judicial de la herencia (Arts. 782 y ss. LEC), estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO, con requisito MASC (LO 1/2025) |

Los assets no reproducen un modelo notarial oficial único (no existe un formulario normalizado estatal para estos documentos, a diferencia del monitorio del CGPJ): se construyen sobre la estructura que exigen el Código Civil y la LEC y la práctica notarial y forense. En cada lanzamiento la skill re-verifica los artículos aplicables; si su redacción cambia, actualiza el asset afectado.

---

## Guías de estilo de redacción (consulta)

| Recurso | Uso |
|---|---|
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminología y corrección del lenguaje jurídico |
| Práctica notarial de partición de herencias (Consejo General del Notariado) | Estructura del documento particional: comparecencia, exposición, inventario, avalúo, adjudicaciones, otorgamiento |
| Guía de redacción judicial clara (Ministerio de Justicia) | Escritos judiciales: frases cortas, una idea por frase, voz activa |

Principios aplicados en los assets notariales: estructura COMPARECENCIA / EXPONE / MANIFIESTA / OTORGAMIENTO; y en los judiciales: AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO. Cláusulas y hechos numerados; cifras en número y letra; una idea por apartado; sin latinismos innecesarios.

---

## Verificación de derecho foral o autonómico

Para herencias sujetas a derecho civil foral o especial (Cataluña, Aragon, Navarra, País Vasco, Baleares, Galicia), las reglas de legítima, órdenes de sucesión, aceptación y partición pueden diferir del Código Civil común. Verificar con `web_search` la normativa foral vigente antes de redactar y advertir al usuario.
