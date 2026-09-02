# Test de ejecucion — skill `derecho-civil-testamento-planificacion`

Ejecucion manual del arbol de decision sobre cuatro escenarios (3 principales + 1 contra-caso). Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuente unica: Codigo Civil (BOE-A-1889-4763), texto consolidado.
- Verificacion real efectuada el 03/09/2026 contra la API de legislacion consolidada del BOE (`https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{N}`, cabecera `Accept: application/xml`), leyendo la ULTIMA `<version>` de cada bloque. Articulos leidos: 9, 14, 15, 16, 662-673, 675, 676, 678, 679, 685, 687, 688, 694-699, 706, 737-743, 756, 774, 775, 781-787, 806-833, 834-840, 849-857, 858, 859, 860, 864, 869, 882, 982, 1056, 1406 y 1407.
- Confirmado: el **art. 808** esta en la redaccion de la **Ley 8/2021** (BOE-A-2021-9233), con efectos desde el **03/09/2021**, e incorpora los parrafos 4.º y 5.º sobre el legitimario en situacion de discapacidad. Tambien proceden de esa reforma los arts. 663, 665, 695, 697, 706, 742, 756, 782, 813 y 822. El art. 823 (mejora) esta en la redaccion de la Ley 15/1996; el 834 y el 835, en la de la Ley 15/2015; el 831 y el 821, en la de la Ley 41/2003; el 849, 850, 851 y 856, en su redaccion originaria de 1889.
- **Modelo oficial de testamento del Consejo General del Notariado: NO existe.** Verificado el 03/09/2026 en notariado.org: el CGN publica material divulgativo (folletos, "pregunte al notario", guia notarial) pero **ningun modelo ni formulario descargable**. Es coherente con el art. 695 CC, que atribuye al Notario la redaccion del instrumento. Registrado como tal en `references/fuentes-plantillas-validadas.md`.
- Pendientes de verificacion manual, registrados expresamente en la reference: derechos forales (no verificados, causa de detencion), Registro General de Actos de Ultima Voluntad (Reglamento Notarial, no consultado), cautela socini (construccion de la practica, sin articulo propio), Ley 29/1987 del ISD (la skill no calcula el impuesto) y Reglamento UE 650/2012 (causa de escalacion, no de redaccion).

---

## Test 1 — Matrimonio con dos hijos, vecindad comun, usufructo universal con cautela socini

**Mensaje inicial:** "Estoy casado en gananciales y tengo dos hijos. Quiero hacer testamento y lo que mas me preocupa es que mi mujer se quede tranquila y pueda seguir viviendo de todo el patrimonio si yo falto primero."

### Recorrido del arbol
```
V1  -> PREGUNTA: vecindad civil -> 1                       V1 = comun -> PROCEDE
V2  -> escucha activa: "que mi mujer... pueda seguir
        viviendo de todo el patrimonio"                    V2 = con planificacion (sin pregunta)
V3a -> escucha activa: "tengo dos hijos"                   V3a = hay descendientes (sin pregunta)
V3b -> no aplica (solo si V3a = 2)
V3c -> escucha activa: "estoy casado en gananciales"       V3c = casado no separado (sin pregunta)
V3d -> PREGUNTA: situacion de discapacidad -> 2            V3d = ninguno
V4  -> PREGUNTA: desheredacion -> 2                        V4 = no deshereda
HOJA PLANIFICACION -> assets/checklist-planificacion-sucesoria.md
                   -> assets/minuta-testamento-abierto.md
```

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija + V1 (vecindad civil), en el mismo mensaje. **V1 se pregunta el primero aunque sea el vector mas abstracto**, porque una respuesta foral haria inutil todo lo demas.
- Turno 2: V3d. (V2, V3a y V3c ya resueltos por escucha activa.)
- Turno 3: V4.
- Turno 4: Confirmacion visible (Punto 3): texto fijo PLANIFICACION + advertencia fija de que la minuta **no es un testamento** y de que es el Notario quien lo redacta (art. 695 CC) + enlace al BOE + eleccion plantilla/documento propio.
- Turno 5: creacion del checklist con `Write` + `Read` + ruta absoluta y, en la MISMA respuesta, anuncio de la seccion 1 ("Comenzamos por la documentacion que debera reunir...") y su primera pregunta. **No hay turno intermedio preguntando "¿desea empezar?"**.
- Turnos 6-8: documentacion a reunir; mapa familiar (HEREDERO A y HEREDERO B, confirmacion agrupada por cada uno, con la advertencia de la preterición del art. 814); inventario orientativo, incluida la advertencia de que las donaciones en vida se computan (arts. 818 y 819).
- Turno 9: **legitima y margen real de libre disposicion `[negociacion]`** — la skill explica, ANTES de pedir ninguna decision, que dos de cada tres partes son legitima (art. 808), que solo un tercio es libre y que la legitima es intangible (art. 813) e irrenunciable en vida (art. 816). Aplicado al caso: legitima estricta 1/3 a repartir por mitad entre los dos hijos, tercio de mejora 1/3, libre disposicion 1/3.
- Turno 10: destino del tercio de libre disposicion y legados — el testador no ordena legados especificos.
- Turno 11: mejora — no desea mejorar a ninguno de los dos hijos.
- Turno 12: legitimario con discapacidad — **SE OMITE** (V3d = 2).
- Turno 13: desheredacion — **SE OMITE** (V4 = 2).
- Turno 14: **derechos del conyuge y cautela socini `[negociacion]`** — la skill explica en este orden: (a) el regimen por defecto, usufructo del tercio de mejora (art. 834); (b) que el usufructo universal que el cliente quiere grava tambien la legitima estricta y el art. 813 lo prohibe; (c) **el mecanismo y el dilema**: cada hijo elegira entre aceptar el usufructo y recibir su parte completa en nuda propiedad gravada de por vida, o no aceptarlo y recibir solo su legitima estricta libre y de inmediato — cobrar mas y mas tarde, o menos y ya, al amparo del art. 820.3.º; (d) la posicion conservadora: la cautela **no esta tipificada en el Codigo Civil**, es construccion de la practica notarial, y su redaccion definitiva corresponde al Notario. El cliente confirma expresamente que ha entendido el dilema que plantea a sus hijos antes de que se escriba.
- Turno 15: sustituciones — sustitucion vulgar a favor de los respectivos descendientes de cada heredero. Fideicomiso no solicitado.
- Turno 16: albacea contador-partidor y facultades del art. 831 — no se designa albacea; no se confieren las facultades del art. 831.
- Turno 17: **aviso fiscal `[negociacion]`** — la skill advierte de que el ISD es autonomico, que las bonificaciones varian mucho entre comunidades y que **no lo calcula**; pide la comunidad autonoma de residencia y recomienda asesor fiscal.
- Turno 18: aplicacion del Punto 4.b — creacion de la minuta con TODAS las decisiones ya volcadas, `Read`, ruta absoluta y, en la misma respuesta, anuncio de la seccion 13 y su primera pregunta.
- Turnos 19-22: testador (confirmacion agrupada; el estado civil NO se vuelve a preguntar, se escribe "casado" desde V3c); conyuge (confirmacion agrupada); naturaleza del documento y revocacion de anteriores; instrucciones para la notaria.
- Cierre: numeracion final de los ordinales, verificacion de cero comentarios HTML y bucle de realimentacion.

### Bloques activados y NO activados en `minuta-testamento-abierto.md`
| Bloque condicional | Estado |
|---|---|
| Datos del conyuge (seccion I) | **ACTIVADO** |
| Legitimario en situacion de discapacidad (seccion II) | NO activado |
| Desheredacion | NO activado |
| Legados | NO activado |
| Mejora | NO activado |
| Usufructo universal con cautela | **ACTIVADO** |
| Derechos del conyuge en su version de cuota legal | NO activado (excluyente con el anterior) |
| Institucion en nuda propiedad | **ACTIVADO** |
| Sustitucion vulgar | **ACTIVADO** |
| Disposicion del art. 808 in fine | NO activado |
| Derecho de habitacion del art. 822 | NO activado |
| Sustitucion fideicomisaria general | NO activado |
| Facultades del art. 831 | NO activado |
| Albacea contador-partidor | NO activado |
| Ruegos no vinculantes | NO activado |
| Testigos del art. 697 / dificultad de lectura del art. 695 | NO activados |

### Documento generado (extracto real, datos sinteticos)
```
MINUTA DE TESTAMENTO ABIERTO NOTARIAL — TESTADOR A
> DRAFT — para revision por un abogado colegiado antes de su firma. No constituye asesoramiento juridico definitivo.
> ESTE DOCUMENTO NO ES UN TESTAMENTO. [...] Conforme al articulo 695 del Codigo Civil, es el Notario quien redacta el testamento con arreglo a la voluntad que le exprese el testador.
> Version del Codigo Civil verificada en el BOE: 03/09/2026
> Vecindad civil declarada por el testador: comun.

II. LEGITIMARIOS
Descendientes: HEREDERO A y HEREDERO B, hijos del testador
Conyuge legitimario: CONYUGE A, no separado legalmente ni de hecho

PRIMERA — Revocacion de disposiciones anteriores.
SEGUNDA — Usufructo universal a favor del conyuge y cautela.
  El testador lega a su conyuge CONYUGE A el usufructo universal y vitalicio de la totalidad de su
  herencia [...]. Si alguno de los herederos forzosos no aceptare este legado de usufructo por entender
  que grava su legitima, percibira unicamente aquello que por legitima estricta le corresponda,
  acreciendo el resto de su participacion [...] a los demas herederos que si lo acepten [...]. Esta
  disposicion se ampara en la opcion que el articulo 820, numero 3.º, del Codigo Civil reconoce a los
  herederos forzosos.
TERCERA — Institucion de herederos. (HEREDERO A y HEREDERO B, por partes iguales)
  La institucion de herederos se entiende hecha en la nuda propiedad de los bienes afectados [...].
CUARTA — Sustitucion vulgar. (art. 774 CC)
QUINTA — Manifestacion final. (art. 695 CC)
```
Resultado: **PASA**. La cautela socini se redacta sin vulnerar la legitima (respeta la legitima estricta como suelo), la institucion se ajusta automaticamente a nuda propiedad, y no aparece ningun bloque de las ramas no elegidas.

---

## Test 2 — Testamento con mejora a un hijo y legado especifico a un nieto

**Mensaje inicial:** "Soy viudo y tengo tres hijos. Quiero que mi hija mayor, que es la que se ha ocupado de mi, se lleve mas que los otros, y ademas quiero dejarle a mi nieto el piso de la playa."

### Recorrido del arbol
```
V1  -> PREGUNTA: vecindad civil -> 1                       V1 = comun -> PROCEDE
V2  -> escucha activa: "se lleve mas que los otros" +
        "dejarle a mi nieto el piso"                        V2 = con planificacion (sin pregunta)
V3a -> escucha activa: "tengo tres hijos"                   V3a = hay descendientes (sin pregunta)
V3c -> escucha activa: "soy viudo"                          V3c = no casado (sin pregunta)
V3d -> PREGUNTA: situacion de discapacidad -> 2             V3d = ninguno
V4  -> PREGUNTA: desheredacion -> 2                         V4 = no deshereda
HOJA PLANIFICACION -> checklist + minuta
```

### Momento de las preguntas
- Turno 1: linea de carga + introduccion + V1.
- Turnos 2-3: V3d y V4.
- Turno 4: Confirmacion visible + eleccion de plantilla.
- Turno 5: creacion del checklist + anuncio de seccion 1 + primera pregunta, en la misma respuesta.
- Turnos 6-8: documentacion; mapa familiar (HEREDERO A, HEREDERO B y HEREDERO C, confirmacion agrupada por cada uno); inventario, con el piso de la playa identificado por direccion y referencia catastral.
- Turno 9: legitima y margen real — aplicado a tres hijos: legitima estricta 1/3 a repartir en tres partes iguales, mejora 1/3, libre disposicion 1/3. El cliente descubre aqui que "llevarse mas" tiene un techo.
- Turno 10: **destino del tercio de libre disposicion y legados `[negociacion]`** — la skill explica que el legado al nieto se imputa al tercio de libre disposicion y no puede perjudicar la legitima (arts. 813, 817 y 820), y advierte del **art. 869**: si el piso se vende o se transforma, el legado queda sin efecto. El cliente confirma el legado del piso de la playa a NIETO A.
- Turno 11: **mejora `[negociacion]`** — la skill explica que el tercio de mejora solo puede ir a hijos o descendientes, que si no se ordena nada se reparte como legitima, y sobre todo que **la mejora debe declararse EXPRESAMENTE** (arts. 823, 825 y 828): decir "que se lleve mas" o dejarle un bien no mejora a nadie. El cliente confirma mejorar a HEREDERO A en el tercio de mejora.
- Turno 12: legitimario con discapacidad — **SE OMITE** (V3d = 2).
- Turno 13: desheredacion — **SE OMITE** (V4 = 2).
- Turno 14: derechos del conyuge y cautela socini — **SE OMITE** (V3c = 2, es viudo: no hay conyuge legitimario).
- Turno 15: sustituciones — vulgar a favor de los descendientes de cada heredero.
- Turno 16: albacea contador-partidor — el cliente lo designa, previendo desacuerdo entre los hijos; facultades del art. 831 **SE OMITEN** (no hay conyuge).
- Turno 17: aviso fiscal.
- Turno 18: creacion de la minuta (Punto 4.b) + anuncio de seccion 13 en la misma respuesta.
- Turnos 19-21: testador (el sub-apartado de estado civil se limita a precisar "viudo", ya resuelto por V3c que no esta casado); seccion de conyuge **OMITIDA**; naturaleza y revocacion; instrucciones para la notaria.

### Bloques activados y NO activados
| Bloque condicional | Estado |
|---|---|
| Datos del conyuge (seccion I) | NO activado (viudo) |
| Legados | **ACTIVADO** (piso de la playa a NIETO A) |
| Mejora | **ACTIVADO** (HEREDERO A, tercio de mejora, declarada expresamente) |
| Usufructo universal con cautela | NO activado |
| Derechos del conyuge en su version de cuota legal | NO activado |
| Institucion en nuda propiedad | NO activado (no hay usufructo) |
| Sustitucion vulgar | **ACTIVADO** |
| Albacea contador-partidor | **ACTIVADO** |
| Facultades del art. 831 | NO activado (no hay conyuge) |
| Desheredacion, discapacidad, fideicomiso, ruegos | NO activados |

### Documento generado (extracto, datos sinteticos)
```
MINUTA DE TESTAMENTO ABIERTO NOTARIAL — TESTADOR B
> DRAFT — para revision por un abogado colegiado antes de su firma. [...]

PRIMERA — Revocacion de disposiciones anteriores.
SEGUNDA — Legados.
  El testador lega a NIETO A la vivienda sita en {{direccion}}, referencia catastral {{referencia}}.
  Los legados se imputan al tercio de libre disposicion y no podran perjudicar la legitima de los
  herederos forzosos, conforme a los articulos 813, 817 y 820 del Codigo Civil.
TERCERA — Mejora.
  El testador mejora expresamente, en concepto de mejora y conforme a los articulos 808 y 823 del
  Codigo Civil, a HEREDERO A, su hija, en el tercio de mejora de su herencia.
CUARTA — Institucion de herederos. (HEREDERO A, HEREDERO B y HEREDERO C, por partes iguales)
QUINTA — Sustitucion vulgar.
SEXTA — Albacea contador-partidor.
SEPTIMA — Manifestacion final.
```
Resultado: **PASA**. La numeracion dinamica produce siete ordinales correlativos sin huecos pese a haberse activado unos bloques y descartado otros. La mejora consta con la formula expresa que exige el art. 825.

---

## Test 3 — Hijo en situacion de discapacidad (arts. 808 in fine y 822)

**Mensaje inicial:** "Tengo dos hijos. El pequeno tiene una discapacidad y vive conmigo en casa; no va a poder valerse solo cuando yo falte. Quiero dejarle todo lo que pueda y asegurarme de que no le echan de la vivienda."

### Recorrido del arbol
```
V1  -> PREGUNTA: vecindad civil -> 1                       V1 = comun -> PROCEDE
V2  -> escucha activa: "dejarle todo lo que pueda"         V2 = con planificacion (sin pregunta)
V3a -> escucha activa: "tengo dos hijos"                   V3a = hay descendientes (sin pregunta)
V3c -> PREGUNTA: estado civil -> 2                         V3c = no casado / separado
V3d -> escucha activa: "el pequeno tiene una
        discapacidad"                                      V3d = SI hay legitimario con discapacidad
V4  -> PREGUNTA: desheredacion -> 2                        V4 = no deshereda
HOJA PLANIFICACION, con los bloques de los arts. 808 in fine, 782 y 822 ACTIVOS y la seccion 7
del Punto 5 tratada como OBLIGATORIA, no opcional.
```

### Momento de las preguntas
- Turno 1: linea de carga + introduccion + V1.
- Turnos 2-3: V3c y V4. V3d no se pregunta: resuelto por escucha activa.
- Turno 4: Confirmacion visible + **advertencia adicional fija por V3d = 1**: "Al encontrarse uno de sus legitimarios en situacion de discapacidad, dispone usted de un margen de planificacion mas amplio del ordinario, conforme a los articulos 808 y 822 del Codigo Civil en la redaccion dada por la Ley 8/2021." La skill **se adelanta** al cliente en vez de esperar a que pregunte.
- Turno 5: creacion del checklist + anuncio de seccion 1 + primera pregunta.
- Turnos 6-8: documentacion (incluida la acreditativa de la situacion de discapacidad); mapa familiar (HEREDERO A y HEREDERO B, este ultimo en situacion de discapacidad); inventario, con la vivienda habitual identificada.
- Turno 9: legitima y margen real — legitima estricta 1/3 (a repartir entre los dos hijos), mejora 1/3, libre disposicion 1/3.
- Turno 10: libre disposicion y legados — el cliente destina el tercio de libre disposicion a HEREDERO B.
- Turno 11: mejora — el cliente mejora a HEREDERO B en el tercio de mejora.
- Turno 12: **legitimario en situacion de discapacidad `[negociacion]`, seccion OBLIGATORIA** — la skill explica las dos herramientas de la Ley 8/2021, en turnos separados:
  a) **Art. 808, ultimo parrafo**: puede disponer a favor de HEREDERO B de la legitima estricta de HEREDERO A. Lo recibido queda gravado con sustitucion fideicomisaria de residuo a favor de HEREDERO A, sin que HEREDERO B pueda disponer de esos bienes a titulo gratuito ni mortis causa; y si HEREDERO A impugna el gravamen, **es el quien debe acreditar que no concurre causa que lo justifique** (parrafo 5.º). La skill advierte de que esta es una de las **pocas excepciones a la intangibilidad de la legitima** (art. 782 en relacion con el 813). El cliente lo confirma.
  b) **Art. 822**: derecho de habitacion sobre la vivienda habitual. La skill explica que **no se computa para el calculo de las legitimas** si al fallecer ambos convivian en ella, que es **intransmisible**, que su titular no puede impedir que sigan conviviendo los demas legitimarios mientras lo necesiten, y que ademas **se atribuye por ministerio de la ley** salvo exclusion expresa del testador — es decir, que ordenarlo expresamente refuerza y documenta un derecho que la ley ya da. El cliente lo confirma y aporta la direccion completa de la vivienda.
  c) La skill advierte de que la acreditacion concreta de la situacion de discapacidad debera confirmarse con la notaria (registrado como pendiente de verificacion manual en la reference).
- Turno 13: desheredacion — **SE OMITE** (V4 = 2).
- Turno 14: conyuge y cautela socini — **SE OMITE** (V3c = 2).
- Turno 15: sustituciones — vulgar. El fideicomiso de residuo del art. 808 ya quedo ordenado en la seccion anterior y **no se pregunta dos veces**.
- Turno 16: albacea — designado.
- Turno 17: aviso fiscal.
- Turno 18: creacion de la minuta (Punto 4.b) + anuncio de seccion 13.
- Turnos 19-21: testador; conyuge **OMITIDO**; naturaleza y revocacion; instrucciones para la notaria.

### Bloques activados y NO activados
| Bloque condicional | Estado |
|---|---|
| Mencion de la situacion de discapacidad (seccion II) | **ACTIVADO** |
| Mejora (a HEREDERO B) | **ACTIVADO** |
| Disposicion del art. 808 in fine con fideicomiso de residuo | **ACTIVADO** |
| Derecho de habitacion del art. 822 | **ACTIVADO** |
| Sustitucion vulgar | **ACTIVADO** |
| Albacea contador-partidor | **ACTIVADO** |
| Datos del conyuge, usufructo universal, cuota legal viudal, facultades del art. 831 | NO activados (no hay conyuge) |
| Legados, desheredacion, fideicomiso general, ruegos | NO activados |

### Documento generado (extracto, datos sinteticos)
```
MINUTA DE TESTAMENTO ABIERTO NOTARIAL — TESTADOR C

II. LEGITIMARIOS
Descendientes: HEREDERO A y HEREDERO B, hijos del testador
Se hace constar expresamente que HEREDERO B se encuentra en situacion de discapacidad, a los efectos
de los articulos 808, ultimo parrafo, 782 y 822 del Codigo Civil.

PRIMERA — Revocacion de disposiciones anteriores.
SEGUNDA — Mejora. (HEREDERO B, tercio de mejora, declarada expresamente)
TERCERA — Institucion de herederos. (HEREDERO A y HEREDERO B)
CUARTA — Sustitucion vulgar.
QUINTA — Disposicion a favor del legitimario en situacion de discapacidad.
  El testador dispone a favor de HEREDERO B [...] de la legitima estricta que corresponderia a los
  demas legitimarios sin discapacidad, al amparo del ultimo parrafo del articulo 808 del Codigo Civil.
  Lo asi recibido queda gravado con sustitucion fideicomisaria de residuo a favor de HEREDERO A [...].
SEXTA — Derecho de habitacion sobre la vivienda habitual.
  El testador lega a HEREDERO B, con quien convive en la vivienda habitual sita en {{direccion}}, el
  derecho de habitacion sobre dicha vivienda, con caracter intransmisible y sin que su titular pueda
  impedir que continuen conviviendo en ella los demas legitimarios mientras lo necesiten [...]. Este
  derecho no se computara para el calculo de las legitimas.
SEPTIMA — Albacea contador-partidor.
OCTAVA — Manifestacion final.
```
Resultado: **PASA**. La skill no espera a que el cliente conozca los arts. 808 in fine y 822: los ofrece proactivamente desde la Confirmacion, que es donde aportan valor. El gravamen de la legitima estricta se redacta con su fideicomiso de residuo obligatorio, no suelto.

---

## Contra-caso — Testador con vecindad civil catalana

**Mensaje inicial:** "Soy de Barcelona, catalan de toda la vida, casado y con dos hijos. Quiero hacer testamento y dejarle a mi mujer lo maximo posible."

### Recorrido del arbol
```
V1 -> PREGUNTA: vecindad civil -> 2 (foral, Cataluna)      V1 = FORAL -> DETENER
V2, V3a, V3b, V3c, V3d, V4 -> NO SE PREGUNTAN
Punto 2 (verificacion), Punto 3 (Confirmacion) y Punto 4 (creacion) -> NO SE EJECUTAN
```

### Comportamiento esperado
La skill **no pregunta ningun otro vector, no pide ningun dato del testador y no crea ningun documento**. En el mismo turno en que recibe la respuesta emite la advertencia fija de `references/vecindad-civil-y-ambito-de-la-skill.md`, apartado 6: que la sujecion al derecho comun o al foral se determina por la vecindad civil (art. 14 CC), que en los territorios con derecho civil propio el regimen de legitimas y de sucesion difiere sustancialmente, que redactar su testamento con las reglas del Codigo Civil comun produciria disposiciones incorrectas, y que debe acudir a un abogado o notario especializado en el derecho civil de su territorio, con el enlace al BOE.

Lo que la skill **NO** hace, y es el nucleo de este contra-caso:
- **No estima la legitima.** No dice "en su caso serian dos tercios": en derecho catalan no lo son.
- **No genera un borrador provisional** "para adaptarlo despues".
- **No responde a la pregunta de fondo** ("dejarle a mi mujer lo maximo posible"), porque la respuesta depende de una norma que no ha verificado y que no cubre.
- **No se apoya en el domicilio.** Vivir en Barcelona no determina la vecindad civil (art. 14.5 CC, adquisicion por residencia de dos o diez anos); la skill se atiene a lo que el testador declara.

**Variante del contra-caso:** si el cliente hubiera respondido "3. No lo se con seguridad", el resultado es **el mismo**: detencion y escalacion. La skill **no aplica el art. 14.6** (en caso de duda prevalece la del lugar de nacimiento) para presumir la vecindad por su cuenta: esa regla resuelve un conflicto juridico, no autoriza a un asistente a suponer el dato del que depende todo el regimen aplicable.

**Resultado: PASA.** La detencion ocurre en el primer turno de clasificacion, antes de la verificacion normativa y antes de pedir un solo dato personal, que es el punto donde una mala clasificacion habria costado al cliente toda una sesion y le habria entregado un documento sustantivamente erroneo con apariencia de correcto.

---

## Verificacion en vivo (no solo sobre el papel)

Ademas del recorrido simulado de los cuatro escenarios, se ejecutaron realmente los pasos mecanicos del Escenario 1, sin instalar el plugin como skill invocable de Claude Code (no esta registrado en este entorno):

1. **Punto 2 real contra el BOE.** Se leyeron en vivo, uno a uno, los bloques `artNNN` del Codigo Civil listados en el apartado de verificacion normativa, tomando la ULTIMA `<version>` de cada bloque. Se confirmo palabra por palabra el contenido de `references/cc-legitimas-y-libre-disposicion.md`, `references/cc-desheredacion-causas-tasadas.md`, `references/cc-formas-revocacion-y-sustituciones.md` y `references/vecindad-civil-y-ambito-de-la-skill.md`, incluida la fecha de vigencia de la Ley 8/2021 (03/09/2021) en los arts. 663, 665, 695, 697, 756, 782, 808, 813 y 822.
2. **Punto 4 real.** Se aplico `Write` en `test-local/output/minuta-testamento-abierto-prueba.md` con los datos sinteticos del Escenario 1, seguido de `Read` de verificacion.
3. **Numeracion final real.** Se aplicaron cuatro ciclos de `Edit` sobre los placeholders `{{ordinal_...}}`, con el `oldString` copiado literalmente del `Read` previo. **Los cuatro coincidieron a la primera**, sin fallos de localizacion.

Comprobaciones automaticas sobre el archivo real, no sobre un extracto manual:

| Comprobacion | Resultado |
|---|---|
| Comentarios HTML residuales (`<!--`) | **0** |
| Placeholders de ordinal sin resolver (`{{ordinal`) | **0** |
| Ordinales presentes | PRIMERA, SEGUNDA, TERCERA, CUARTA, QUINTA — correlativos, sin huecos ni repeticiones |
| Placeholders con texto de ayuda o anidados en los assets (`{{...:...}}`, `{{...{{...}}...}}`) | **0** en los dos assets |
| Placeholders que persisten en el documento | 10, todos con nombre propio: `{{dni_conyuge}}`, `{{documentacion_a_aportar}}`, `{{domicilio_testador}}`, `{{fecha_nacimiento_testador}}`, `{{fecha_prevista_otorgamiento}}`, `{{lugar_nacimiento_testador}}`, `{{nombre_madre_testador}}`, `{{nombre_padre_testador}}`, `{{notaria_designada}}`, `{{poblacion_notaria}}` — exactamente los datos que el `SKILL.md` deja para las secciones 13 y 16 del Punto 5. Ninguno inventado, ninguno omitido por error, ningun `{{DATO_FALTANTE}}` generico repetido |
| Bloques de ramas no elegidas presentes en el documento | Ninguno: desheredacion, mejora, legados, art. 808 in fine, art. 822, fideicomiso general, art. 831, albacea y ruegos ausentes por completo, no comentados |
| Bloque condicional insertado como texto plano | El de "institucion en nuda propiedad" aparece como parrafo normal, sin envoltorio de comentario |

**PASA.**

### Defecto real detectado durante la ejecucion en vivo, y corregido

Al rellenar la seccion 1 del Punto 5 (Testador) se detecto que el sub-apartado f) pedia el **estado civil**, un dato que **el vector V3c ya habia resuelto** en el Punto 1 ("Estoy casado y no separado legalmente ni de hecho"). Preguntarlo de nuevo infringe la regla de no-backtracking del `CLAUDE.md` raiz, seccion 3, y hace que la skill parezca no haber escuchado.

**Fix aplicado** en el `SKILL.md`, HOJA SIMPLE, seccion 1: si V3c = 1, se escribe "casado" sin preguntarlo; si V3c = 2, el sub-apartado f) se formula unicamente para precisar cual es (soltero, viudo, divorciado o separado). El Test 2 (viudo) y el Test 3 (no casado) reflejan ya el comportamiento corregido.

---

## Revision UX

Hallazgos:

1. **La vecindad civil se pregunta la primera, contra la regla general de orden.** La guia de autoria recomienda dejar los vectores de puro filtro de alcance para el final, pero admite la excepcion cuando preguntarlos antes ahorra trabajo si la respuesta probable deja el caso fuera. Aqui la excepcion es clara: un testador foral que respondiera al final habria entregado antes su filiacion, su patrimonio y sus decisiones familiares para nada, y —peor— habria recibido durante toda la sesion explicaciones sobre tercios y legitimas que no se le aplican. El coste de una pregunta abstracta en el turno 1 es muy inferior al de una sesion entera mal encaminada.

2. **La opcion "no lo se con seguridad" es tan importante como la opcion "foral".** Sin ella, un cliente que no distingue domicilio de vecindad civil respondera "comun" por defecto y la skill redactara con seguridad aparente sobre una premisa falsa. Ofrecerla explicitamente convierte una suposicion silenciosa en una detencion controlada.

3. **El punto de mayor valor de la skill es una explicacion, no un documento.** La seccion de legitima y margen real de libre disposicion (turno 9 en los tres tests) es donde el cliente descubre que solo puede repartir libremente un tercio. Colocarla ANTES de todas las decisiones —y no al final, como advertencia— evita que construya una planificacion entera sobre una premisa equivocada y tenga que rehacerla.

4. **La cautela socini se explica como dilema, no como truco.** Presentarla en tres pasos (regimen por defecto, por que el usufructo universal choca con el art. 813, y la eleccion concreta que se pone ante cada hijo) hace que el cliente entienda el precio de la clausula: introduce una tension entre su conyuge y sus hijos que se activara justo cuando el ya no este. Presentarla como una forma de "saltarse la legitima" seria comodo y falso.

5. **En desheredacion, la alternativa importa mas que la negativa.** Un cliente al que solo se le dice "su motivo no es causa legal" se marcha frustrado y probablemente acuda a otro que se la redacte. Ofrecerle en el mismo turno la salida valida —reducir a esa persona a su legitima estricta y dirigir la mejora y el tercio libre a quien quiera— resuelve buena parte de su objetivo real sin ningun riesgo de nulidad. El art. 857 (los descendientes del desheredado conservan la legitima) suele ser ademas el dato que le hace cambiar de idea por si mismo.

6. **En discapacidad, la skill se adelanta.** Los arts. 808 in fine y 822 son poco conocidos y el cliente no va a preguntarlos por su nombre. Anunciar en la Confirmacion que su margen de planificacion es mas amplio del ordinario, y tratar esa seccion como obligatoria en vez de opcional, es la diferencia entre una skill que responde y una que asesora.

7. **La numeracion de las clausulas se resuelve al final, no durante.** Con nueve bloques condicionales, numerar sobre la marcha garantiza huecos ("PRIMERA, TERCERA, SEPTIMA") cuando una rama se descarta. Dejar los ordinales como placeholders y numerarlos en una pasada final, rehecha cada vez que el bucle de realimentacion anade o quita una clausula, es lo unico que produce un documento correlativo de forma fiable. El Test 2 (siete ordinales tras activar tres bloques y descartar seis) es el caso que lo demuestra.

Ajustes aplicados: el fix de no-backtracking del estado civil (seccion 1 del Punto 5), ya descrito arriba. El resto de hallazgos estaban previstos en el diseno y no requirieron cambios.

---

## QA en vivo por agente independiente

Ejecucion real (no simulada sobre el papel) por un agente sin contexto previo de la skill, el 03/09/2026. Escenario: **viudo de 71 anos, tres hijos, sin trato con uno de ellos desde hace ocho anos, al que quiere dejar "lo minimo o nada"; el piso, a partes iguales, a los otros dos; nacido y residente siempre en Valladolid.** Datos sinteticos: TESTADOR A, NIF 00000000-T, HEREDERO A / B / C.

Verificacion normativa del Punto 2 ejecutada de verdad contra la API del BOE (arts. 14, 808, 813, 841, 842, 843, 844, 847, 850, 851, 853, 857, 912, 931, 1056 y 1062, leyendo la ultima `<version>` de cada bloque). Ficheros generados y editados realmente:

- `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/checklist-planificacion-sucesoria-qa-prueba.md` (`Write` + 4 `Edit`)
- `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/testamento-qa-prueba.md` (`Write` + 4 `Edit`)

Enrutamiento: V1 = 1 (comun), V2 = 2 y V3a = 1 y V3c = 2 por escucha activa, V3d = 2, V4 = 1 → **HOJA PLANIFICACION**.

### Extractos literales del texto emitido al cliente

**Turno 1 (carga + introduccion + V1, en el mismo mensaje):**

> **Skill cargada satisfactoriamente.**
>
> Vamos a preparar la documentacion para que pueda ordenar su sucesion en vida y llevarla resuelta a la notaria. Para ajustarla correctamente a su caso, es necesario precisar antes algunos datos.
>
> Su vecindad civil es:
> 1. Comun
> 2. Foral o especial (Cataluna, Aragon, Navarra, Illes Balears, Pais Vasco o Galicia)
> 3. No lo se con seguridad

**Seccion 4 — legitima y margen real (explicacion previa a toda decision):**

> Antes de tomar ninguna decision, debe conocer que parte de su patrimonio puede repartir libremente.
>
> La ley no le deja disponer de todo. Con hijos, dos de cada tres partes de la herencia son legitima y estan reservadas a ellos (articulo 808 del Codigo Civil). De esas dos partes, una es la legitima estricta y se reparte por partes iguales entre los tres, sin que usted pueda alterarla; la otra es el tercio de mejora, que tampoco puede salir de sus hijos, pero dentro de ellos usted elige a cual o cuales se lo atribuye. Solo el tercio restante es de libre disposicion.
>
> Aplicado a su patrimonio, de 192.000 euros orientativos: 64.000 euros de legitima estricta, que son 21.333,33 euros para cada uno de sus tres hijos y no admiten discusion; 64.000 euros de mejora, que puede dirigir a quien decida entre ellos; y 64.000 euros de libre disposicion. Es decir, puede orientar 128.000 de los 192.000 euros hacia HEREDERO A y HEREDERO B, pero 21.333,33 euros corresponden a HEREDERO C en todo caso.

**Seccion 9 — desheredacion (el punto critico):**

> Debo darle una respuesta clara, aunque no sea la que espera: el motivo que me expone no permite desheredar a su hijo.
>
> La desheredacion no admite motivos genericos. El Codigo Civil enumera de forma cerrada las causas por las que un padre puede privar a un hijo de su legitima: haberle negado los alimentos sin motivo legitimo y haberle maltratado de obra o injuriado gravemente de palabra (articulo 853), ademas de los supuestos de indignidad del articulo 756 a los que remite el articulo 852, que exigen condena penal firme. La falta de trato, el distanciamiento o la ausencia de visitas y de llamadas, por dolorosa que sea, no figura entre ellas.
>
> Las consecuencias de desheredar sin causa legal son peores que no hacerlo. Conforme al articulo 851 del Codigo Civil, la desheredacion hecha sin expresion de causa, o por causa que no sea de las senaladas por la ley, anula la institucion de heredero en cuanto perjudique al desheredado: la clausula no solo no surtiria efecto, sino que dejaria a sus otros dos hijos en un pleito con su hermano y la particion bloqueada. Debe saber ademas que la prueba de la causa no le corresponderia a usted, que ya no estaria, sino a los herederos favorecidos si el desheredado la niega (articulo 850), y que, aun prosperando, la desheredacion no apartaria a esa rama de la familia: los hijos del desheredado ocupan su lugar y conservan la legitima (articulo 857).
>
> Existe una alternativa que produce buena parte del efecto que usted busca y no admite discusion: reducir a HEREDERO C a su legitima estricta. Le corresponderia unicamente la novena parte de la herencia que la ley le reserva, y el tercio de mejora y el tercio de libre disposicion, dos terceras partes del total, irian integramente a HEREDERO A y a HEREDERO B.
>
> ¿Desea que ordenemos su testamento de esta segunda forma, sin desheredacion?

**Seccion 5 — el piso a dos de los tres hijos (advertencia previa a redactar):**

> Debo advertirle de una dificultad antes de redactar nada. El piso, valorado en 180.000 euros, es practicamente todo su patrimonio. La legitima estricta de HEREDERO C asciende a 21.333,33 euros y, adjudicado el piso a sus otros dos hijos, en la herencia solo quedarian 12.000 euros en efectivo: no bastan para pagarle lo que la ley le reserva, de modo que la adjudicacion seria inoficiosa y su hijo podria pedir su reduccion.
>
> Hay dos formas de ordenarlo correctamente. La primera: adjudicar el piso a HEREDERO A y a HEREDERO B y ordenar en el testamento que la porcion de HEREDERO C se le pague en dinero, al amparo del articulo 841 del Codigo Civil. Exige autorizar expresamente al contador-partidor, comunicar la decision a su hijo dentro del ano siguiente a su fallecimiento y pagarle en el plazo de otro ano mas (articulo 844); incumplidos esos plazos, la facultad caduca y la herencia se reparte por las reglas generales. Debe saber que el hijo obligado a pagar puede, a su vez, exigir que la cuota se satisfaga con bienes de la herencia (articulo 842) y que la particion necesitara aprobacion notarial salvo que los tres la confirmen expresamente (articulo 843).
>
> La segunda: no ordenar nada y dejar que el piso se adjudique en la particion abonando el exceso en dinero (articulo 1062). Es mas simple, pero mas fragil: basta con que uno solo de los herederos pida la venta en publica subasta para que el piso deba subastarse.
>
> ¿Cual de las dos prefiere?

### A) Veredicto sobre el texto emitido — **correcto**

Tratamiento de usted sostenido en los 20 turnos, sin una sola aparicion de "vale", "genial" o "perfecto"; verbos de despacho ("indiqueme", "debe saber", "adviertole"). Cero menciones de vectores, hojas o fases: el cliente nunca lee "V4", "HOJA PLANIFICACION" ni "paso al punto 5". Los tres puntos `[negociacion]` se explican integramente antes de pedir la decision, con la consecuencia economica traducida a euros. Cero invenciones: los articulos citados se leyeron en el BOE en esta misma sesion antes de redactar; no se cito ninguna sentencia.

Unica friccion de estilo: el texto fijo de Confirmacion PLANIFICACION anunciaba a un viudo que "los derechos de su conyuge" se rigen por los articulos 834 y siguientes. **Corregido** (ver defecto 5).

### B) Veredicto sobre los assets — **con defectos, corregidos**

Placeholders desnudos y sin anidar en los dos assets; ninguno con texto de ayuda dentro; ningun `[DATO]`. El documento escrito en disco quedo con **cero comentarios HTML** (verificado por `grep`) y con la numeracion **PRIMERA a OCTAVA correlativa y sin huecos** pese a haberse descartado seis bloques condicionales. La minuta leida de corrido suena a documento real.

Friccion menor no corregida: `instituye herederos universales ... a X, Y y Z, por partes {{forma_reparto_herencia}}` obliga a rellenar "desiguales, correspondiendo cuatro novenas partes a...". Funciona, pero la preposicion fija encorseta el reparto desigual.

### C) Los dos puntos criticos

**C.1 Desheredacion — PASA, y con nota alta.** La skill no redacto la clausula. Contrasto el motivo con los arts. 852 a 855, dijo sin rodeos que "no me habla" no es causa legal, explico el efecto del art. 851 (anula la institucion en cuanto perjudique al desheredado), advirtio de la carga de la prueba del art. 850 y de que el art. 857 mantiene la legitima en la rama del desheredado, y ofrecio la alternativa real. El asset colabora: el bloque de desheredacion exige `{{articulo_causa_desheredacion}}` y `{{hechos_desheredacion}}`, de modo que no puede redactarse sin causa.

*Observacion, no defecto:* la reference afirma de plano que "no me habla" no encaja en el art. 853, sin mencionar que la linea jurisprudencial sobre el maltrato psicologico como maltrato de obra ha discutido ese limite. La posicion conservadora es defendible y no se ha tocado: anadir la matizacion exigiria citar sentencias verificadas, y el guardrail 2 del plugin prohibe citarlas de memoria. Queda anotado para una revision con fuente en la mano.

**C.2 Legitima — PASA en la explicacion, FALLA en la mecanica.** El calculo y la advertencia aparecen antes de redactar, correctamente. Pero la skill no tenia nada que decir sobre el problema real del caso: adjudicar un piso que vale el 94 % del caudal a dos de los tres hijos deja al tercero sin con que cobrar su legitima. Ni el SKILL.md ni los assets mencionaban los arts. 841 a 847 (pago en metalico) ni el art. 1062, que son la unica via valida. **Corregido** (defectos 1 y 2).

### Defectos encontrados y corregidos

1. **No se preguntaba nunca a quien instituye herederos en la HOJA PLANIFICACION.** Las secciones eran: documentacion, mapa familiar, inventario, legitima, libre disposicion y legados, mejora, discapacidad, desheredacion, conyuge, sustituciones, albacea y fiscal; despues, en la minuta, testador, conyuge, revocacion e instrucciones. La institucion de herederos —clausula obligatoria del asset, con `{{relacion_herederos_instituidos}}` y `{{forma_reparto_herencia}}`— no se pedia en ningun momento, pese a que la HOJA SIMPLE si la tiene (su seccion 5). Toda desheredacion enruta a PLANIFICACION, de modo que el caso mas delicado era justo el que se quedaba sin la clausula central. **Fix:** nueva seccion 5 "Institucion de herederos y reparto del caudal" `[negociacion — PUNTO CLAVE]`, nueva fila en la tabla de decisiones del checklist y guardrail 13.
2. **Faltaba la via de pago de la legitima cuando el caudal es un bien indivisible.** **Fix:** el apartado c) de la nueva seccion 5 (arts. 841 a 844, 847, 842, 843 y 1062), un bullet nuevo en la Validacion de presupuestos, el guardrail 14, un bloque condicional nuevo en la minuta ("Adjudicacion de bien indivisible y pago en metalico de la legitima"), una fila nueva en el checklist y el apartado 5.1 de `references/cc-legitimas-y-libre-disposicion.md` con el texto verificado de los arts. 841 a 847, 1062 y 1056.2.
3. **Numeracion de secciones desincronizada.** El Punto 4.b cerraba el checklist "completadas sus secciones 1 a 8" y mandaba anunciar "la seccion 9"; el encabezado decia "(secciones 1 a 8)"; el cierre del checklist hablaba de la seccion 12 y de saltar a la 13. Un LLM que siguiera el 4.b al pie de la letra cerraba el checklist justo despues de la desheredacion y se saltaba conyuge, sustituciones, albacea y **el aviso fiscal**. **Fix:** renumeracion completa 1 a 17 y actualizacion de las cuatro referencias cruzadas.
4. **Referencia cruzada erronea a la cautela socini.** La seccion 6 de la HOJA SIMPLE remitia "a la seccion 12 de la HOJA PLANIFICACION", que es el aviso fiscal. **Fix:** ahora remite a la seccion 10, que es la correcta.
5. **Texto fijo que habla de un conyuge inexistente.** **Fix:** instruccion expresa de suprimir la mencion final a los derechos del conyuge cuando V3c = 2.
6. **V1 podia darse por resuelto por escucha activa desde el lugar de residencia.** "Naci y he vivido siempre en Valladolid" invita a fijar V1 = comun sin preguntar, y V1 es el filtro de alcance de toda la skill. **Fix:** el vector V1 advierte ahora que la vecindad se adquiere por filiacion (art. 14.2) y solo muda por residencia de dos anos con manifestacion o de diez sin declaracion en contrario (art. 14.5), y que debe preguntarse siempre de forma expresa.

### Lo que se comporto bien sin necesidad de tocarlo

La linea de carga y la introduccion salieron en el mismo turno que la primera pregunta; tras el `Write` la skill encadeno el anuncio de seccion y su pregunta **sin ningun turno intermedio del tipo "¿desea empezar?"**; los anuncios de seccion aparecieron en todas las transiciones; la confirmacion agrupada de los datos del testador se emitio en el turno siguiente al ultimo sub-apartado, no en el mismo; y la numeracion final de clausulas produjo PRIMERA a OCTAVA sin huecos.
