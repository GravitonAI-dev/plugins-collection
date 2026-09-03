# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-herencia`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Punto 2 se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada (verificada 31/08/2026) | URL |
|---|---|---|---|
| Codigo Civil (texto consolidado) | BOE-A-1889-4763 | consolidado, ultima actualizacion publicada el 03/01/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado, ultima actualizacion publicada el 28/02/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LO 1/2025 de eficiencia del Servicio Publico de Justicia (MASC) | BOE-A-2025-76 | 02/01/2025 (en vigor 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |
| Ley 29/1987 del Impuesto sobre Sucesiones y Donaciones | BOE-A-1987-28141 | consolidado, ultima actualizacion publicada el 28/12/2022 | https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141 |
| RD 1629/1991, Reglamento del ISD | BOE-A-1991-27678 | consolidado, ultima actualizacion publicada el 05/04/2023 | https://www.boe.es/buscar/act.php?id=BOE-A-1991-27678 |
| TR Ley Reguladora de las Haciendas Locales (plusvalia municipal, IIVTNU) | BOE-A-2004-4214 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 |

Articulos relevantes verificados para esta skill (redaccion vigente comprobada en el texto consolidado del BOE el 31/08/2026):

- **Codigo Civil:** 657 y ss. (apertura de la sucesion); 806 a 808 (legitima; el 808 en su redaccion por la Ley 8/2021); 834 y ss. (conyuge viudo); 912 y ss. (sucesion intestada); 988 a 1009 (aceptacion y repudiacion: 988 voluntariedad, 989 retroaccion, 997 irrevocabilidad, 998-1000 formas y aceptacion tacita, 1003 responsabilidad ultra vires de la aceptacion pura, **1005 interpelacion notarial con plazo de TREINTA DIAS NATURALES y silencio = aceptacion pura y simple** (redaccion por la Ley 15/2015, en vigor desde el 23/07/2015), **1008 repudiacion ante Notario en instrumento publico** (redaccion por la Ley 15/2015)); 1010 a 1034 (beneficio de inventario: 1011 declaracion ante Notario, 1014-1015 plazo de treinta dias, 1023 efectos); 1035 y ss. (colacion); 1051 y ss. (particion: 1052 legitimacion, 1059 remision a la LEC a falta de acuerdo, 1061-1062 igualdad de lotes e indivisibles).
- **LEC:** 52.1.4 (competencia territorial en cuestiones hereditarias: ultimo domicilio del finado); 264 y 399.3 (acreditacion del MASC); 403.2 (inadmision sin MASC, redaccion por la LO 1/2025); **782 a 789 (division judicial de la herencia:** 782 solicitud y legitimacion, 783 junta, 784 contador y peritos, 786 operaciones divisorias, 787 aprobacion y oposicion, 788 entrega, 789 terminacion por acuerdo).
- **LO 1/2025:** art. 5 (requisito de procedibilidad MASC: exigible en los procesos especiales del Libro IV de la LEC — donde se ubica la division judicial de la herencia —, que no figura entre las excepciones del art. 5.2).
- **Ley 29/1987 (ISD):** art. 28 (repudiacion y renuncia: en la renuncia pura, simple y gratuita tributan los beneficiarios; en la renuncia a favor de persona determinada tributa el renunciante y ademas se liquida la cesion o donacion; la renuncia tras prescribir el impuesto se reputa donacion).
- **RD 1629/1991:** art. 67.1.a (plazo de presentacion de 6 meses desde el fallecimiento) y art. 68 (prorroga por otro plazo igual, solicitada dentro de los 5 primeros meses; silencio positivo al mes; devenga intereses de demora).

---

## Plantillas del plugin

| Asset | Base |
|---|---|
| `assets/cuaderno-particional.md` | Estructura estandar de escritura de aceptacion y particion de herencia: comparecencia, exposicion (titulo sucesorio), inventario y avaluo, liquidacion del haber, formacion de lotes y adjudicaciones (Arts. 1058, 1061-1062, 1068 CC) |
| `assets/aceptacion-herencia.md` | Documento de aceptacion pura y simple o a beneficio de inventario (Arts. 988, 998, 1003, 1010-1034 CC). El bloque opcional de renuncia que contiene NO se usa: la renuncia se genera siempre con `assets/renuncia-herencia.md` |
| `assets/renuncia-herencia.md` | Minuta de renuncia (repudiacion) de herencia para su elevacion a escritura publica notarial (Art. 1008 CC), con advertencia de irrevocabilidad (Art. 997 CC) y de la fiscalidad de la renuncia pura frente a la traslativa (Art. 28 Ley 29/1987) |
| `assets/requerimiento-1005-cc.md` | Solicitud de interpelacion notarial al heredero que no acepta ni repudia (Art. 1005 CC): plazo de 30 dias naturales y efecto de aceptacion pura y simple si calla |
| `assets/solicitud-division-judicial-herencia.md` | Solicitud de division judicial de la herencia (Arts. 782 y ss. LEC), estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO, con requisito MASC (LO 1/2025) |

Los assets no reproducen un modelo notarial oficial unico (no existe un formulario normalizado estatal para estos documentos, a diferencia del monitorio del CGPJ): se construyen sobre la estructura que exigen el Codigo Civil y la LEC y la practica notarial y forense. En cada lanzamiento la skill re-verifica los articulos aplicables; si su redaccion cambia, actualiza el asset afectado.

---

## Guias de estilo de redaccion (consulta)

| Recurso | Uso |
|---|---|
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminologia y correccion del lenguaje juridico |
| Practica notarial de particion de herencias (Consejo General del Notariado) | Estructura del documento particional: comparecencia, exposicion, inventario, avaluo, adjudicaciones, otorgamiento |
| Guia de redaccion judicial clara (Ministerio de Justicia) | Escritos judiciales: frases cortas, una idea por frase, voz activa |

Principios aplicados en los assets notariales: estructura COMPARECENCIA / EXPONE / MANIFIESTA / OTORGAMIENTO; y en los judiciales: AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO. Clausulas y hechos numerados; cifras en numero y letra; una idea por apartado; sin latinismos innecesarios.

---

## Verificacion de derecho foral o autonomico

Para herencias sujetas a derecho civil foral o especial (Cataluna, Aragon, Navarra, Pais Vasco, Baleares, Galicia), las reglas de legitima, ordenes de sucesion, aceptacion y particion pueden diferir del Codigo Civil comun. Verificar con `web_search` la normativa foral vigente antes de redactar y advertir al usuario.
