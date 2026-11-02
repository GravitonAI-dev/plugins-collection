# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-testamento-planificacion`. Registra las fuentes normativas y las
> plantillas validadas que la skill verifica en cada lanzamiento para aplicar la redacción vigente al documento que redacta.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local, se informa al usuario y el punto queda marcado como pendiente de verificación manual. **Prohibido dar por vigente lo que no se ha podido verificar.**

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Código Civil — Real Decreto de 24 de julio de 1889 (texto consolidado), Libro III, Título III | BOE-A-1889-4763 | última modificación aplicada a los preceptos sucesorios usados por esta skill: Ley 8/2021, de 2 de junio, con efectos desde 03/09/2021 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| Ley 8/2021, de 2 de junio, de reforma para el apoyo a las personas con discapacidad en el ejercicio de su capacidad jurídica | BOE-A-2021-9233 | publicada 03/06/2021; efectos desde 03/09/2021 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2021-9233 |
| Ley 41/2003, de protección patrimonial de las personas con discapacidad (origen del art. 822 CC y del anterior párrafo 3.º del art. 808) | BOE-A-2003-21053 | publicada 19/11/2003 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2003-21053 |
| Ley 29/1987, del Impuesto sobre Sucesiones y Donaciones | BOE-A-1987-28141 | no verificada en esta skill: la skill NO calcula el impuesto, solo advierte de su existencia y de su carácter autonómico | https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141 |
| Reglamento (UE) 650/2012, sucesiones con repercusión transfronteriza | Reglamento UE 650/2012 | no verificado en esta skill: su concurrencia es causa de ESCALACIÓN, no de redacción | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32012R0650 |

**Endpoint de verificación artículo por artículo (API de legislación consolidada del BOE).** Devuelve todas las versiones históricas del precepto; **la vigente es la última `<version>` del bloque**. Requiere cabecera `Accept: application/xml`:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{numero_articulo}
```

Ejemplo: `.../bloque/art808` para el art. 808 CC.

**Aviso sobre el identificador de bloque:** no todas las normas usan el mismo formato. El Código Civil usa `artNNN`; la LEC usa `aNNN`; la LOPJ y la LPH los usan deletreados (`aochentaynueve`). Si un identificador devuelve 404, probar la otra convención antes de dar el precepto por inaccesible.

---

## Artículos del Código Civil verificados el 03/09/2026

| Artículos | Materia | Redacción vigente verificada |
|---|---|---|
| 9.8 | Ley aplicable a la sucesión por causa de muerte | Modificado por la Ley 8/2021 (efectos 03/09/2021). Rige la ley nacional del causante al fallecer. Las disposiciones testamentarias ordenadas conforme a la ley nacional del testador al otorgarlas conservan validez aunque otra ley rija la sucesión, ajustándose las legitimas a esta última |
| 14 | Vecindad civil | Redacción de la Ley 11/1990 (vigente desde 07/11/1990). La sujeción al derecho civil común o al foral se determina por la vecindad civil. Se adquiere por residencia continuada de dos años con manifestación de voluntad, o de diez años sin declaración en contrario. El matrimonio no la altera. **En caso de duda prevalece la del lugar de nacimiento (apartado 6)** |
| 15 | Vecindad civil del extranjero que adquiere la nacionalidad | Modificado por la Ley 8/2021 (efectos 03/09/2021) |
| 16 | Conflictos de leyes internos | Redacción de la Ley 11/1990. Ley personal = la determinada por la vecindad civil |
| 662 | Quién puede testar | Pueden testar todos aquellos a quienes la ley no lo prohíbe expresamente. Redacción originaria de 1889 |
| 663 | Quién no puede testar | Modificado por la Ley 8/2021 (efectos 03/09/2021). No pueden testar: 1.º la persona menor de catorce años; 2.º la que en el momento de testar no pueda conformar o expresar su voluntad ni aun con ayuda de medios o apoyos |
| 664 | Testamento anterior a la enajenación mental | Válido. Redacción originaria |
| 665 | Testamento de la persona con discapacidad | Modificado por la Ley 8/2021 (efectos 03/09/2021). Podrá otorgar testamento **cuando, a juicio del Notario, pueda comprender y manifestar el alcance de sus disposiciones**. El Notario procurara que desarrolle su propio proceso de toma de decisiones, con los ajustes necesarios. Ya NO exige el dictamen previo de dos facultativos que preveía la redacción anterior |
| 666 | Momento en que se aprecia la capacidad | Se atiende únicamente al estado en que se halle al tiempo de otorgar el testamento. Redacción originaria |
| 667, 668 | Concepto de testamento; herencia y legado | Redacción originaria. En la duda, si la voluntad es clara, vale como disposición a título universal |
| 669 | Prohibición del testamento mancomunado | Nulo en derecho común: no pueden testar dos o más personas mancomunadamente ni en un mismo instrumento. Redacción originaria. **Es una de las diferencias prácticas más relevantes con varios derechos forales** |
| 670 | Carácter personalísimo | No cabe dejar la formación del testamento al arbitrio de un tercero ni hacerlo por comisario o mandatario. Redacción originaria |
| 671, 672 | Distribución encomendada a un tercero; remisión a cédulas o papeles privados | Redacción originaria. El art. 672 declara nula la disposición que se remita a papeles privados sin los requisitos del testamento ológrafo |
| 673 | Violencia, dolo o fraude | Nulidad del testamento. Redacción originaria |
| 675 | Interpretación del testamento | Sentido literal de las palabras salvo que aparezca claramente otra voluntad. Redacción originaria |
| 676, 678, 679 | Clases de testamento común: ológrafo, abierto y cerrado | Redacción originaria |
| 685 | Deber del Notario de conocer al testador y de apreciar su capacidad | Redacción de la Ley 30/1991 (vigente desde 12/01/1992). El Notario debe asegurarse de que, **a su juicio**, el testador tiene la capacidad legal necesaria para testar |
| 687 | Nulidad por defecto de forma | **Será nulo el testamento en cuyo otorgamiento no se hayan observado las formalidades establecidas en el capítulo.** Redacción originaria. Fundamento de que una minuta privada no valga como testamento |
| 688 | Testamento ológrafo | Redacción de 1904. Solo personas mayores de edad; escrito íntegramente y firmado de puño y letra del testador, con expresión de año, mes y día. Fuera del alcance de esta skill |
| 694 | Testamento abierto: Notario hábil | Deberá otorgarse ante Notario hábil para actuar en el lugar del otorgamiento. Redacción de la Ley 30/1991 |
| 695 | Otorgamiento del testamento abierto | Modificado por la Ley 8/2021 (efectos 03/09/2021). El testador expresa su última voluntad **oralmente, por escrito o mediante cualquier medio técnico, material o humano**; **es el Notario quien redacta el testamento con arreglo a ella**, con expresión de lugar, año, mes, día y hora, lo lee en alta voz y lo firma el testador. Si hay dificultad o imposibilidad de leer u oír, el Notario se asegura con los medios adecuados de que el testador ha entendido y de que el testamento recoge fielmente su voluntad |
| 696 | Fe de conocimiento y juicio de capacidad | Redacción de la Ley 30/1991. El Notario hará constar que, a su juicio, el testador tiene la capacidad legal necesaria |
| 697 | Testigos | Modificado por la Ley 8/2021 (efectos 03/09/2021). Solo son necesarios dos testigos idóneos cuando el testador declare que no sabe o no puede firmar, o cuando el testador o el Notario lo soliciten |
| 698 | Otros concurrentes | Redacción de la Ley 30/1991. Testigos de conocimiento, facultativos e intérprete |
| 699 | Unidad de acto | Todas las formalidades en un solo acto que comienza con la lectura, sin interrupción licita salvo accidente pasajero. Redacción de la Ley 30/1991 |
| 706 | Testamento cerrado | Modificado por la Ley 8/2021. Fuera del alcance de esta skill |
| 737 | Revocabilidad esencial | **Todas las disposiciones testamentarias son esencialmente revocables**, aunque el testador exprese su voluntad de no revocarlas. Se tienen por no puestas las cláusulas derogatorias de disposiciones futuras. Redacción originaria |
| 738 | Forma de la revocación | El testamento no puede ser revocado sino con las solemnidades necesarias para testar. Redacción originaria |
| 739 | Revocación por testamento posterior | El anterior queda revocado de derecho por el posterior perfecto, salvo que el testador exprese que aquel subsista. Redacción originaria |
| 740 a 743 | Efectos de la revocación; caducidad | Redacción originaria salvo el 741 (Ley 11/1981) y el 742 (Ley 8/2021) |
| 756 | Causas de indignidad | Modificado por la Ley 8/2021 (efectos 03/09/2021). El número 7.º incorpora la falta de atenciones debidas a la persona con discapacidad. Los números 1.º, 2.º, 3.º, 5.º y 6.º son causa de desheredación por remisión del art. 852 |
| 774, 775 | Sustitución vulgar y pupilar | Redacción originaria. La sustitución simple, sin expresión de casos, comprende premoriencia, incapacidad y renuncia |
| 781 a 787 | Sustituciones fideicomisarias | Redacción originaria salvo el 782 (Ley 8/2021). El 781 limita el fideicomiso al segundo grado o a personas que vivan al fallecer el testador; el 783 exige llamamiento expreso; el 785 enumera lo que no surte efecto |
| 782 | Fideicomiso sobre la legítima | Modificado por la Ley 8/2021 (efectos 03/09/2021). **Las sustituciones fideicomisarias nunca podrán gravar la legítima, salvo cuando se establezcan, en los términos del art. 808, en beneficio de uno o varios hijos del testador en situación de discapacidad.** Sobre el tercio de mejora, solo a favor de descendientes |
| 806 | Concepto de legítima | Porción de bienes de que el testador no puede disponer por haberla reservado la ley a los herederos forzosos. Redacción originaria |
| 807 | Herederos forzosos | Redacción de la Ley 11/1981. 1.º hijos y descendientes; 2.º a falta de ellos, padres y ascendientes; 3.º el viudo o viuda en la forma y medida que establece el Código |
| 808 | Cuantía de la legítima de descendientes | **Modificado por la Ley 8/2021, con efectos de 03/09/2021.** Dos terceras partes del haber hereditario de los progenitores; de esas dos, una puede aplicarse como mejora; el tercio restante es de libre disposición. **Párrafo 4.º (redacción de 2021): cuando alguno o varios de los legitimarios se encontraren en situación de discapacidad, el testador podrá disponer a su favor de la legítima estricta de los demás legitimarios sin discapacidad**, quedando lo así recibido gravado con sustitución fideicomisaria de residuo a favor de los perjudicados, salvo disposición contraria. Párrafo 5.º: corresponde al hijo que impugne el gravamen acreditar que no concurre causa que lo justifique |
| 809, 810 | Legítima de padres y ascendientes | Redacción de 1958 (art. 809) y originaria (art. 810). La mitad del haber hereditario, o **un tercio si concurren con el cónyuge viudo** del descendiente causante |
| 811, 812 | Reserva lineal y reversión de donaciones | Redacción originaria |
| 813 | Intangibilidad de la legítima | Modificado por la Ley 8/2021 (efectos 03/09/2021). El testador no puede privar de la legítima salvo en los casos determinados por la ley, **ni imponer sobre ella gravamen, condición ni sustitución de ninguna especie, salvo lo dispuesto en cuanto al usufructo del viudo y lo establecido en los artículos 782 y 808** |
| 814 | Preterición | Redacción de la Ley 11/1981. La preterición no intencional de hijos o descendientes anula la institución de herederos (y, si todos resultan preteridos, las disposiciones patrimoniales) |
| 815 | Complemento de legítima | El heredero forzoso que reciba menos de su legítima puede pedir el complemento. Redacción originaria |
| 816 | Nulidad de la renuncia a la legítima futura | Redacción originaria. **Ningún legitimario puede renunciar válidamente a su legítima en vida del causante** |
| 817 | Reducción de disposiciones inoficiosas | Se reducirán, a petición de los legitimarios, en lo que fueren inoficiosas o excesivas. Redacción originaria |
| 818, 819 | Cómputo de la legítima e imputación de donaciones | Redacción de la Ley 11/1981 (818) y originaria (819). Valor de los bienes al morir, menos deudas y cargas, más el valor de las donaciones colacionables |
| 820, 821 | Orden de la reducción; legado de finca indivisible | Redacción originaria (820) y de la Ley 41/2003 (821). El 820.3.º da al legitimario la opción frente al legado de usufructo o renta vitalicia que exceda de la parte disponible: **cumplir la disposición o entregar al legatario la parte de libre disposición** — base legal de la cautela socini |
| 822 | Derecho de habitación del legitimario con discapacidad | **Modificado por la Ley 8/2021, con efectos de 03/09/2021.** La donación o legado del derecho de habitación sobre la vivienda habitual a favor de un legitimario en situación de discapacidad **no se computa para el cálculo de las legitimas** si al fallecer ambos convivían en ella. El derecho se atribuye además **por ministerio de la ley** al legitimario que lo necesite y conviviera con el fallecido, salvo disposición contraria o exclusión expresa del testador. Es **intransmisible** y coexiste con los derechos del cónyuge de los arts. 1406 y 1407 |
| 823 | Mejora | Redacción de la Ley 15/1996 (vigente desde 16/02/1996). El padre o la madre pueden disponer en concepto de mejora, a favor de alguno o algunos de sus hijos o descendientes, de **una de las dos terceras partes destinadas a legítima** |
| 824 a 833 | Régimen de la mejora | Redacción originaria salvo 826-833 en parte. No caben sobre la mejora otros gravámenes que los establecidos en favor de legitimarios o sus descendientes (824). **La mejora exige declaración expresa** (825 y 828). Es revocable salvo capitulaciones o contrato oneroso con tercero (827). Puede señalarse en cosa determinada, con abono en metálico del exceso (829). **La facultad de mejorar no puede encomendarse a otro (830)**, salvo la fiducia del 831 |
| 831 | Facultades del cónyuge (fiducia sucesoria) | Redacción de la Ley 41/2003 (vigente desde 20/11/2003). Cabe conferir al cónyuge, en testamento, facultades para mejorar y adjudicar a favor de los hijos o descendientes comunes, incluso con cargo al tercio de libre disposición, y para partir. Plazo supletorio de dos años. Cesan si pasa a ulterior matrimonio o relación análoga o tiene hijo no común, salvo disposición contraria. Aplicable también a personas con descendencia común no casadas entre sí |
| 834 | Usufructo del cónyuge viudo con descendientes | Redacción de la Ley 15/2015 (vigente desde 23/07/2015). El cónyuge no separado legalmente ni de hecho que concurre con hijos o descendientes tiene derecho al **usufructo del tercio destinado a mejora** |
| 835 | Reconciliación | Redacción de la Ley 15/2015. Conserva sus derechos el separado reconciliado con notificación al Juzgado o al Notario |
| 836 | (Suprimido) | Suprimido por la Ley 11/1981 |
| 837 | Usufructo del viudo con ascendientes | Redacción de la Ley 15/2005. **Usufructo de la mitad de la herencia** |
| 838 | Usufructo del viudo sin descendientes ni ascendientes | Redacción de 1958. **Usufructo de los dos tercios de la herencia** |
| 839, 840 | Conmutación del usufructo viudal | Redacción de 1958 (839) y de la Ley 15/2005 (840). Los herederos pueden satisfacer el usufructo con renta vitalicia, productos de bienes o capital en efectivo, de mutuo acuerdo o por mandato judicial |
| 849 | Forma de la desheredación | **La desheredación solo podrá hacerse en testamento, expresando en el la causa legal en que se funde.** Redacción originaria |
| 850 | Carga de la prueba | **La prueba de ser cierta la causa corresponde a los herederos del testador si el desheredado la negare.** Redacción originaria |
| 851 | Desheredación sin causa legal | **La desheredación hecha sin expresión de causa, o por causa cuya certeza no se probare, o que no sea una de las señaladas en los cuatro artículos siguientes, anulara la institución de heredero en cuanto perjudique al desheredado**; valdrán los legados, mejoras y demás disposiciones en lo que no perjudiquen a la legítima. Redacción originaria |
| 852 | Causas comunes por remisión a la indignidad | Redacción de la Ley 15/1996. Son justas causas las de indignidad del art. 756 números **1.º, 2.º, 3.º, 5.º y 6.º** |
| 853 | Causas para desheredar a hijos y descendientes | Redacción de la Ley 11/1990. Además de las del art. 756 números 2, 3, 5 y 6: **1.ª haber negado, sin motivo legítimo, los alimentos al padre o ascendiente que le deshereda; 2.ª haberle maltratado de obra o injuriado gravemente de palabra** |
| 854 | Causas para desheredar a padres y ascendientes | Redacción de la Ley 11/1981. Además de las del art. 756 números 1, 2, 3, 5 y 6: pérdida de la patria potestad por las causas del art. 170; negativa de alimentos sin motivo legítimo; atentado de uno de los padres contra la vida del otro sin reconciliación |
| 855 | Causas para desheredar al cónyuge | Redacción de la Ley 15/1996. Además de las del art. 756 números 2.º, 3.º, 5.º y 6.º: incumplimiento grave o reiterado de los deberes conyugales; causas de pérdida de la patria potestad; negativa de alimentos a los hijos o al otro cónyuge; atentado contra la vida del cónyuge testador sin reconciliación |
| 856 | Reconciliación | **La reconciliación posterior priva del derecho de desheredar y deja sin efecto la desheredación ya hecha.** Redacción originaria |
| 857 | Descendientes del desheredado | **Los hijos o descendientes del desheredado ocupan su lugar y conservan los derechos de herederos forzosos respecto a la legítima.** Redacción de la Ley 11/1981 |
| 858 a 882 | Legados | Redacción originaria de los verificados (858, 859, 860, 864, 869, 882). El 869 recoge las causas de ineficacia sobrevenida del legado: transformación, enajenación y pérdida de la cosa legada |
| 982 | Derecho de acrecer en la sucesión testamentaria | Redacción originaria. Exige llamamiento de dos o más a una misma herencia o porción **sin especial designación de partes**, y premoriencia, renuncia o incapacidad de uno de ellos |
| 1056 | Partición hecha por el testador | Redacción de la Ley 7/2003 (vigente desde 02/06/2003). El testador puede partir por acto entre vivos o por última voluntad en cuanto no perjudique la legítima; el párrafo 2.º permite preservar indivisa una explotación económica o el control societario pagando en metálico la legítima de los demás, incluso con efectivo extrahereditario y con aplazamiento máximo de cinco años |
| 1406, 1407 | Atribución preferente al cónyuge de la vivienda habitual | Redacción de la Ley 7/2003 (1406) y de la Ley 11/1981 (1407). Coexisten con el derecho de habitación del art. 822 |

---

## Plantillas: NO existe modelo oficial de testamento del Consejo General del Notariado

Verificado el 03/09/2026 en https://www.notariado.org : el Consejo General del Notariado publica **material divulgativo** sobre el testamento (folletos, sección "pregunte al notario", guía notarial de búsqueda de notarios), pero **no publica un modelo, formulario ni guía oficial de testamento descargable**.

Esto es coherente con el propio régimen legal: conforme al **artículo 695 del Código Civil**, en el testamento abierto es **el Notario quien redacta el instrumento** con arreglo a la voluntad que le expresa el testador. No existe, ni puede existir, un formulario oficial que el cliente rellene y firme.

Consecuencia operativa para esta skill: el asset `minuta-testamento-abierto.md` **no reproduce ningún modelo oficial**. Es una minuta de trabajo —un documento preparatorio que el cliente y su abogado llevan a la notaría— construida sobre el contenido sustantivo exigido y permitido por los artículos 667 a 672, 694 a 699, 737 a 739, 774 a 787, 806 a 833, 849 a 857 y 858 a 882 del Código Civil, y sobre las guías de redacción jurídica clara recogidas en `references/estilo-redaccion-escritos.md`.

| Asset | Base normativa de su estructura |
|---|---|
| `assets/minuta-testamento-abierto.md` | Arts. 662-666, 667-672, 687, 694-699, 737-739, 774-787, 806-833, 849-857, 858-882 y 1056 CC |
| `assets/checklist-planificacion-sucesoria.md` | Arts. 807-808, 813, 818-823, 831, 834-840 y 849-857 CC; Ley 29/1987 (advertencia fiscal, sin cálculo) |

---

## Verificar manualmente (no resuelto por fuente oficial en esta verificación)

1. **Derecho civil foral o especial.** Esta skill cubre **solo derecho común**. Las legitimas, la libertad de testar, la admisibilidad del testamento mancomunado y los pactos sucesorios varían sustancialmente en Cataluña, Aragon, Navarra, Baleares, País Vasco y Galicia. Ninguna de esas normas está verificada aquí. Si la vecindad civil del testador es foral, la skill **detiene el proceso y escala**: no se redacta con el Código Civil común.
2. **Registro General de Actos de Última Voluntad.** La comunicación notarial del otorgamiento al Registro se regula en el Anexo II del Reglamento Notarial, no en el Código Civil, y no se ha verificado en el BOE en esta pasada. La skill lo menciona como paso práctico posterior al otorgamiento; verificar antes de afirmar plazos o requisitos concretos.
3. **Cautela socini.** Es una construcción de la práctica notarial y de la jurisprudencia, **no una figura tipificada en el Código Civil**. Su encaje legal se apoya en el artículo 820.3.º (opción del legitimario entre cumplir la disposición o recibir la parte de libre disposición) y en el límite del artículo 813. La skill nunca debe presentarla como una figura con artículo propio.
4. **Impuesto sobre Sucesiones y Donaciones.** Tributo cedido a las comunidades autónomas, con bonificaciones y reducciones muy dispares. Esta skill **no lo calcula ni lo verifica**: se limita a advertir de su existencia y a recomendar el análisis de la normativa autonómica aplicable.
5. **Redacción literal de los artículos.** La API del BOE devuelve la versión consolidada vigente, que es la fuente utilizada aquí. Antes de transcribir literalmente un precepto en un documento que se vaya a otorgar, contrastarlo de nuevo en el BOE.
6. **Situación de discapacidad a efectos de los arts. 808 y 822.** El Código Civil, tras la Ley 8/2021, se refiere a "situación de discapacidad" sin remitir a un grado administrativo concreto en esos preceptos. La acreditación concreta que exigirá el Notario debe confirmarse con la notaría antes del otorgamiento.
