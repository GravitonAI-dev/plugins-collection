# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-testamento-planificacion`. Registra las fuentes normativas y las
> plantillas validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso de verificacion se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local, se informa al usuario y el punto queda marcado como pendiente de verificacion manual. **Prohibido dar por vigente lo que no se ha podido verificar.**

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Codigo Civil — Real Decreto de 24 de julio de 1889 (texto consolidado), Libro III, Titulo III | BOE-A-1889-4763 | ultima modificacion aplicada a los preceptos sucesorios usados por esta skill: Ley 8/2021, de 2 de junio, con efectos desde 03/09/2021 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| Ley 8/2021, de 2 de junio, de reforma para el apoyo a las personas con discapacidad en el ejercicio de su capacidad juridica | BOE-A-2021-9233 | publicada 03/06/2021; efectos desde 03/09/2021 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2021-9233 |
| Ley 41/2003, de proteccion patrimonial de las personas con discapacidad (origen del art. 822 CC y del anterior parrafo 3.º del art. 808) | BOE-A-2003-21053 | publicada 19/11/2003 (verificado 03/09/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2003-21053 |
| Ley 29/1987, del Impuesto sobre Sucesiones y Donaciones | BOE-A-1987-28141 | no verificada en esta skill: la skill NO calcula el impuesto, solo advierte de su existencia y de su caracter autonomico | https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141 |
| Reglamento (UE) 650/2012, sucesiones con repercusion transfronteriza | Reglamento UE 650/2012 | no verificado en esta skill: su concurrencia es causa de ESCALACION, no de redaccion | https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32012R0650 |

**Endpoint de verificacion articulo por articulo (API de legislacion consolidada del BOE).** Devuelve todas las versiones historicas del precepto; **la vigente es la ultima `<version>` del bloque**. Requiere cabecera `Accept: application/xml`:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{numero_articulo}
```

Ejemplo: `.../bloque/art808` para el art. 808 CC.

**Aviso sobre el identificador de bloque:** no todas las normas usan el mismo formato. El Codigo Civil usa `artNNN`; la LEC usa `aNNN`; la LOPJ y la LPH los usan deletreados (`aochentaynueve`). Si un identificador devuelve 404, probar la otra convencion antes de dar el precepto por inaccesible.

---

## Articulos del Codigo Civil verificados el 03/09/2026

| Articulos | Materia | Redaccion vigente verificada |
|---|---|---|
| 9.8 | Ley aplicable a la sucesion por causa de muerte | Modificado por la Ley 8/2021 (efectos 03/09/2021). Rige la ley nacional del causante al fallecer. Las disposiciones testamentarias ordenadas conforme a la ley nacional del testador al otorgarlas conservan validez aunque otra ley rija la sucesion, ajustandose las legitimas a esta ultima |
| 14 | Vecindad civil | Redaccion de la Ley 11/1990 (vigente desde 07/11/1990). La sujecion al derecho civil comun o al foral se determina por la vecindad civil. Se adquiere por residencia continuada de dos anos con manifestacion de voluntad, o de diez anos sin declaracion en contrario. El matrimonio no la altera. **En caso de duda prevalece la del lugar de nacimiento (apartado 6)** |
| 15 | Vecindad civil del extranjero que adquiere la nacionalidad | Modificado por la Ley 8/2021 (efectos 03/09/2021) |
| 16 | Conflictos de leyes internos | Redaccion de la Ley 11/1990. Ley personal = la determinada por la vecindad civil |
| 662 | Quien puede testar | Pueden testar todos aquellos a quienes la ley no lo prohibe expresamente. Redaccion originaria de 1889 |
| 663 | Quien no puede testar | Modificado por la Ley 8/2021 (efectos 03/09/2021). No pueden testar: 1.º la persona menor de catorce anos; 2.º la que en el momento de testar no pueda conformar o expresar su voluntad ni aun con ayuda de medios o apoyos |
| 664 | Testamento anterior a la enajenacion mental | Valido. Redaccion originaria |
| 665 | Testamento de la persona con discapacidad | Modificado por la Ley 8/2021 (efectos 03/09/2021). Podra otorgar testamento **cuando, a juicio del Notario, pueda comprender y manifestar el alcance de sus disposiciones**. El Notario procurara que desarrolle su propio proceso de toma de decisiones, con los ajustes necesarios. Ya NO exige el dictamen previo de dos facultativos que preveia la redaccion anterior |
| 666 | Momento en que se aprecia la capacidad | Se atiende unicamente al estado en que se halle al tiempo de otorgar el testamento. Redaccion originaria |
| 667, 668 | Concepto de testamento; herencia y legado | Redaccion originaria. En la duda, si la voluntad es clara, vale como disposicion a titulo universal |
| 669 | Prohibicion del testamento mancomunado | Nulo en derecho comun: no pueden testar dos o mas personas mancomunadamente ni en un mismo instrumento. Redaccion originaria. **Es una de las diferencias practicas mas relevantes con varios derechos forales** |
| 670 | Caracter personalisimo | No cabe dejar la formacion del testamento al arbitrio de un tercero ni hacerlo por comisario o mandatario. Redaccion originaria |
| 671, 672 | Distribucion encomendada a un tercero; remision a cedulas o papeles privados | Redaccion originaria. El art. 672 declara nula la disposicion que se remita a papeles privados sin los requisitos del testamento olografo |
| 673 | Violencia, dolo o fraude | Nulidad del testamento. Redaccion originaria |
| 675 | Interpretacion del testamento | Sentido literal de las palabras salvo que aparezca claramente otra voluntad. Redaccion originaria |
| 676, 678, 679 | Clases de testamento comun: olografo, abierto y cerrado | Redaccion originaria |
| 685 | Deber del Notario de conocer al testador y de apreciar su capacidad | Redaccion de la Ley 30/1991 (vigente desde 12/01/1992). El Notario debe asegurarse de que, **a su juicio**, el testador tiene la capacidad legal necesaria para testar |
| 687 | Nulidad por defecto de forma | **Sera nulo el testamento en cuyo otorgamiento no se hayan observado las formalidades establecidas en el capitulo.** Redaccion originaria. Fundamento de que una minuta privada no valga como testamento |
| 688 | Testamento olografo | Redaccion de 1904. Solo personas mayores de edad; escrito integramente y firmado de puno y letra del testador, con expresion de ano, mes y dia. Fuera del alcance de esta skill |
| 694 | Testamento abierto: Notario habil | Debera otorgarse ante Notario habil para actuar en el lugar del otorgamiento. Redaccion de la Ley 30/1991 |
| 695 | Otorgamiento del testamento abierto | Modificado por la Ley 8/2021 (efectos 03/09/2021). El testador expresa su ultima voluntad **oralmente, por escrito o mediante cualquier medio tecnico, material o humano**; **es el Notario quien redacta el testamento con arreglo a ella**, con expresion de lugar, ano, mes, dia y hora, lo lee en alta voz y lo firma el testador. Si hay dificultad o imposibilidad de leer u oir, el Notario se asegura con los medios adecuados de que el testador ha entendido y de que el testamento recoge fielmente su voluntad |
| 696 | Fe de conocimiento y juicio de capacidad | Redaccion de la Ley 30/1991. El Notario hara constar que, a su juicio, el testador tiene la capacidad legal necesaria |
| 697 | Testigos | Modificado por la Ley 8/2021 (efectos 03/09/2021). Solo son necesarios dos testigos idoneos cuando el testador declare que no sabe o no puede firmar, o cuando el testador o el Notario lo soliciten |
| 698 | Otros concurrentes | Redaccion de la Ley 30/1991. Testigos de conocimiento, facultativos e interprete |
| 699 | Unidad de acto | Todas las formalidades en un solo acto que comienza con la lectura, sin interrupcion licita salvo accidente pasajero. Redaccion de la Ley 30/1991 |
| 706 | Testamento cerrado | Modificado por la Ley 8/2021. Fuera del alcance de esta skill |
| 737 | Revocabilidad esencial | **Todas las disposiciones testamentarias son esencialmente revocables**, aunque el testador exprese su voluntad de no revocarlas. Se tienen por no puestas las clausulas derogatorias de disposiciones futuras. Redaccion originaria |
| 738 | Forma de la revocacion | El testamento no puede ser revocado sino con las solemnidades necesarias para testar. Redaccion originaria |
| 739 | Revocacion por testamento posterior | El anterior queda revocado de derecho por el posterior perfecto, salvo que el testador exprese que aquel subsista. Redaccion originaria |
| 740 a 743 | Efectos de la revocacion; caducidad | Redaccion originaria salvo el 741 (Ley 11/1981) y el 742 (Ley 8/2021) |
| 756 | Causas de indignidad | Modificado por la Ley 8/2021 (efectos 03/09/2021). El numero 7.º incorpora la falta de atenciones debidas a la persona con discapacidad. Los numeros 1.º, 2.º, 3.º, 5.º y 6.º son causa de desheredacion por remision del art. 852 |
| 774, 775 | Sustitucion vulgar y pupilar | Redaccion originaria. La sustitucion simple, sin expresion de casos, comprende premoriencia, incapacidad y renuncia |
| 781 a 787 | Sustituciones fideicomisarias | Redaccion originaria salvo el 782 (Ley 8/2021). El 781 limita el fideicomiso al segundo grado o a personas que vivan al fallecer el testador; el 783 exige llamamiento expreso; el 785 enumera lo que no surte efecto |
| 782 | Fideicomiso sobre la legitima | Modificado por la Ley 8/2021 (efectos 03/09/2021). **Las sustituciones fideicomisarias nunca podran gravar la legitima, salvo cuando se establezcan, en los terminos del art. 808, en beneficio de uno o varios hijos del testador en situacion de discapacidad.** Sobre el tercio de mejora, solo a favor de descendientes |
| 806 | Concepto de legitima | Porcion de bienes de que el testador no puede disponer por haberla reservado la ley a los herederos forzosos. Redaccion originaria |
| 807 | Herederos forzosos | Redaccion de la Ley 11/1981. 1.º hijos y descendientes; 2.º a falta de ellos, padres y ascendientes; 3.º el viudo o viuda en la forma y medida que establece el Codigo |
| 808 | Cuantia de la legitima de descendientes | **Modificado por la Ley 8/2021, con efectos de 03/09/2021.** Dos terceras partes del haber hereditario de los progenitores; de esas dos, una puede aplicarse como mejora; el tercio restante es de libre disposicion. **Parrafo 4.º (redaccion de 2021): cuando alguno o varios de los legitimarios se encontraren en situacion de discapacidad, el testador podra disponer a su favor de la legitima estricta de los demas legitimarios sin discapacidad**, quedando lo asi recibido gravado con sustitucion fideicomisaria de residuo a favor de los perjudicados, salvo disposicion contraria. Parrafo 5.º: corresponde al hijo que impugne el gravamen acreditar que no concurre causa que lo justifique |
| 809, 810 | Legitima de padres y ascendientes | Redaccion de 1958 (art. 809) y originaria (art. 810). La mitad del haber hereditario, o **un tercio si concurren con el conyuge viudo** del descendiente causante |
| 811, 812 | Reserva lineal y reversion de donaciones | Redaccion originaria |
| 813 | Intangibilidad de la legitima | Modificado por la Ley 8/2021 (efectos 03/09/2021). El testador no puede privar de la legitima salvo en los casos determinados por la ley, **ni imponer sobre ella gravamen, condicion ni sustitucion de ninguna especie, salvo lo dispuesto en cuanto al usufructo del viudo y lo establecido en los articulos 782 y 808** |
| 814 | Preterición | Redaccion de la Ley 11/1981. La preterición no intencional de hijos o descendientes anula la institucion de herederos (y, si todos resultan preteridos, las disposiciones patrimoniales) |
| 815 | Complemento de legitima | El heredero forzoso que reciba menos de su legitima puede pedir el complemento. Redaccion originaria |
| 816 | Nulidad de la renuncia a la legitima futura | Redaccion originaria. **Ningun legitimario puede renunciar validamente a su legitima en vida del causante** |
| 817 | Reduccion de disposiciones inoficiosas | Se reduciran, a peticion de los legitimarios, en lo que fueren inoficiosas o excesivas. Redaccion originaria |
| 818, 819 | Computo de la legitima e imputacion de donaciones | Redaccion de la Ley 11/1981 (818) y originaria (819). Valor de los bienes al morir, menos deudas y cargas, mas el valor de las donaciones colacionables |
| 820, 821 | Orden de la reduccion; legado de finca indivisible | Redaccion originaria (820) y de la Ley 41/2003 (821). El 820.3.º da al legitimario la opcion frente al legado de usufructo o renta vitalicia que exceda de la parte disponible: **cumplir la disposicion o entregar al legatario la parte de libre disposicion** — base legal de la cautela socini |
| 822 | Derecho de habitacion del legitimario con discapacidad | **Modificado por la Ley 8/2021, con efectos de 03/09/2021.** La donacion o legado del derecho de habitacion sobre la vivienda habitual a favor de un legitimario en situacion de discapacidad **no se computa para el calculo de las legitimas** si al fallecer ambos convivian en ella. El derecho se atribuye ademas **por ministerio de la ley** al legitimario que lo necesite y conviviera con el fallecido, salvo disposicion contraria o exclusion expresa del testador. Es **intransmisible** y coexiste con los derechos del conyuge de los arts. 1406 y 1407 |
| 823 | Mejora | Redaccion de la Ley 15/1996 (vigente desde 16/02/1996). El padre o la madre pueden disponer en concepto de mejora, a favor de alguno o algunos de sus hijos o descendientes, de **una de las dos terceras partes destinadas a legitima** |
| 824 a 833 | Regimen de la mejora | Redaccion originaria salvo 826-833 en parte. No caben sobre la mejora otros gravamenes que los establecidos en favor de legitimarios o sus descendientes (824). **La mejora exige declaracion expresa** (825 y 828). Es revocable salvo capitulaciones o contrato oneroso con tercero (827). Puede senalarse en cosa determinada, con abono en metalico del exceso (829). **La facultad de mejorar no puede encomendarse a otro (830)**, salvo la fiducia del 831 |
| 831 | Facultades del conyuge (fiducia sucesoria) | Redaccion de la Ley 41/2003 (vigente desde 20/11/2003). Cabe conferir al conyuge, en testamento, facultades para mejorar y adjudicar a favor de los hijos o descendientes comunes, incluso con cargo al tercio de libre disposicion, y para partir. Plazo supletorio de dos anos. Cesan si pasa a ulterior matrimonio o relacion analoga o tiene hijo no comun, salvo disposicion contraria. Aplicable tambien a personas con descendencia comun no casadas entre si |
| 834 | Usufructo del conyuge viudo con descendientes | Redaccion de la Ley 15/2015 (vigente desde 23/07/2015). El conyuge no separado legalmente ni de hecho que concurre con hijos o descendientes tiene derecho al **usufructo del tercio destinado a mejora** |
| 835 | Reconciliacion | Redaccion de la Ley 15/2015. Conserva sus derechos el separado reconciliado con notificacion al Juzgado o al Notario |
| 836 | (Suprimido) | Suprimido por la Ley 11/1981 |
| 837 | Usufructo del viudo con ascendientes | Redaccion de la Ley 15/2005. **Usufructo de la mitad de la herencia** |
| 838 | Usufructo del viudo sin descendientes ni ascendientes | Redaccion de 1958. **Usufructo de los dos tercios de la herencia** |
| 839, 840 | Conmutacion del usufructo viudal | Redaccion de 1958 (839) y de la Ley 15/2005 (840). Los herederos pueden satisfacer el usufructo con renta vitalicia, productos de bienes o capital en efectivo, de mutuo acuerdo o por mandato judicial |
| 849 | Forma de la desheredacion | **La desheredacion solo podra hacerse en testamento, expresando en el la causa legal en que se funde.** Redaccion originaria |
| 850 | Carga de la prueba | **La prueba de ser cierta la causa corresponde a los herederos del testador si el desheredado la negare.** Redaccion originaria |
| 851 | Desheredacion sin causa legal | **La desheredacion hecha sin expresion de causa, o por causa cuya certeza no se probare, o que no sea una de las senaladas en los cuatro articulos siguientes, anulara la institucion de heredero en cuanto perjudique al desheredado**; valdran los legados, mejoras y demas disposiciones en lo que no perjudiquen a la legitima. Redaccion originaria |
| 852 | Causas comunes por remision a la indignidad | Redaccion de la Ley 15/1996. Son justas causas las de indignidad del art. 756 numeros **1.º, 2.º, 3.º, 5.º y 6.º** |
| 853 | Causas para desheredar a hijos y descendientes | Redaccion de la Ley 11/1990. Ademas de las del art. 756 numeros 2, 3, 5 y 6: **1.ª haber negado, sin motivo legitimo, los alimentos al padre o ascendiente que le deshereda; 2.ª haberle maltratado de obra o injuriado gravemente de palabra** |
| 854 | Causas para desheredar a padres y ascendientes | Redaccion de la Ley 11/1981. Ademas de las del art. 756 numeros 1, 2, 3, 5 y 6: perdida de la patria potestad por las causas del art. 170; negativa de alimentos sin motivo legitimo; atentado de uno de los padres contra la vida del otro sin reconciliacion |
| 855 | Causas para desheredar al conyuge | Redaccion de la Ley 15/1996. Ademas de las del art. 756 numeros 2.º, 3.º, 5.º y 6.º: incumplimiento grave o reiterado de los deberes conyugales; causas de perdida de la patria potestad; negativa de alimentos a los hijos o al otro conyuge; atentado contra la vida del conyuge testador sin reconciliacion |
| 856 | Reconciliacion | **La reconciliacion posterior priva del derecho de desheredar y deja sin efecto la desheredacion ya hecha.** Redaccion originaria |
| 857 | Descendientes del desheredado | **Los hijos o descendientes del desheredado ocupan su lugar y conservan los derechos de herederos forzosos respecto a la legitima.** Redaccion de la Ley 11/1981 |
| 858 a 882 | Legados | Redaccion originaria de los verificados (858, 859, 860, 864, 869, 882). El 869 recoge las causas de ineficacia sobrevenida del legado: transformacion, enajenacion y perdida de la cosa legada |
| 982 | Derecho de acrecer en la sucesion testamentaria | Redaccion originaria. Exige llamamiento de dos o mas a una misma herencia o porcion **sin especial designacion de partes**, y premoriencia, renuncia o incapacidad de uno de ellos |
| 1056 | Particion hecha por el testador | Redaccion de la Ley 7/2003 (vigente desde 02/06/2003). El testador puede partir por acto entre vivos o por ultima voluntad en cuanto no perjudique la legitima; el parrafo 2.º permite preservar indivisa una explotacion economica o el control societario pagando en metalico la legitima de los demas, incluso con efectivo extrahereditario y con aplazamiento maximo de cinco anos |
| 1406, 1407 | Atribucion preferente al conyuge de la vivienda habitual | Redaccion de la Ley 7/2003 (1406) y de la Ley 11/1981 (1407). Coexisten con el derecho de habitacion del art. 822 |

---

## Plantillas: NO existe modelo oficial de testamento del Consejo General del Notariado

Verificado el 03/09/2026 en https://www.notariado.org : el Consejo General del Notariado publica **material divulgativo** sobre el testamento (folletos, seccion "pregunte al notario", guia notarial de busqueda de notarios), pero **no publica un modelo, formulario ni guia oficial de testamento descargable**.

Esto es coherente con el propio regimen legal: conforme al **articulo 695 del Codigo Civil**, en el testamento abierto es **el Notario quien redacta el instrumento** con arreglo a la voluntad que le expresa el testador. No existe, ni puede existir, un formulario oficial que el cliente rellene y firme.

Consecuencia operativa para esta skill: el asset `minuta-testamento-abierto.md` **no reproduce ningun modelo oficial**. Es una minuta de trabajo —un documento preparatorio que el cliente y su abogado llevan a la notaria— construida sobre el contenido sustantivo exigido y permitido por los articulos 667 a 672, 694 a 699, 737 a 739, 774 a 787, 806 a 833, 849 a 857 y 858 a 882 del Codigo Civil, y sobre las guias de redaccion juridica clara recogidas en `references/estilo-redaccion-escritos.md`.

| Asset | Base normativa de su estructura |
|---|---|
| `assets/minuta-testamento-abierto.md` | Arts. 662-666, 667-672, 687, 694-699, 737-739, 774-787, 806-833, 849-857, 858-882 y 1056 CC |
| `assets/checklist-planificacion-sucesoria.md` | Arts. 807-808, 813, 818-823, 831, 834-840 y 849-857 CC; Ley 29/1987 (advertencia fiscal, sin calculo) |

---

## Verificar manualmente (no resuelto por fuente oficial en esta verificacion)

1. **Derecho civil foral o especial.** Esta skill cubre **solo derecho comun**. Las legitimas, la libertad de testar, la admisibilidad del testamento mancomunado y los pactos sucesorios varian sustancialmente en Cataluna, Aragon, Navarra, Baleares, Pais Vasco y Galicia. Ninguna de esas normas esta verificada aqui. Si la vecindad civil del testador es foral, la skill **detiene el proceso y escala**: no se redacta con el Codigo Civil comun.
2. **Registro General de Actos de Ultima Voluntad.** La comunicacion notarial del otorgamiento al Registro se regula en el Anexo II del Reglamento Notarial, no en el Codigo Civil, y no se ha verificado en el BOE en esta pasada. La skill lo menciona como paso practico posterior al otorgamiento; verificar antes de afirmar plazos o requisitos concretos.
3. **Cautela socini.** Es una construccion de la practica notarial y de la jurisprudencia, **no una figura tipificada en el Codigo Civil**. Su encaje legal se apoya en el articulo 820.3.º (opcion del legitimario entre cumplir la disposicion o recibir la parte de libre disposicion) y en el limite del articulo 813. La skill nunca debe presentarla como una figura con articulo propio.
4. **Impuesto sobre Sucesiones y Donaciones.** Tributo cedido a las comunidades autonomas, con bonificaciones y reducciones muy dispares. Esta skill **no lo calcula ni lo verifica**: se limita a advertir de su existencia y a recomendar el analisis de la normativa autonomica aplicable.
5. **Redaccion literal de los articulos.** La API del BOE devuelve la version consolidada vigente, que es la fuente utilizada aqui. Antes de transcribir literalmente un precepto en un documento que se vaya a otorgar, contrastarlo de nuevo en el BOE.
6. **Situacion de discapacidad a efectos de los arts. 808 y 822.** El Codigo Civil, tras la Ley 8/2021, se refiere a "situacion de discapacidad" sin remitir a un grado administrativo concreto en esos preceptos. La acreditacion concreta que exigira el Notario debe confirmarse con la notaria antes del otorgamiento.
