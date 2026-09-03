# Vecindad Civil: el Filtro de Alcance de esta Skill

> Material de referencia para la skill `derecho-civil-testamento-planificacion`. Codigo Civil verificado en el BOE
> (BOE-A-1889-4763) el 03/09/2026. Determina cuando la skill PUEDE redactar y cuando DEBE detenerse.
> No forma parte del output al usuario.

---

## 1. Por que este es el primer filtro y no un detalle

El regimen sucesorio espanol **no es uno solo**. El Codigo Civil comun convive con seis derechos civiles forales o especiales con normativa sucesoria propia, y las diferencias no son de matiz: cambian la cuantia de la legitima, quienes son legitimarios, si la legitima es un derecho a bienes o un simple credito, si cabe el testamento mancomunado y si son validos los pactos sucesorios.

Una minuta redactada sobre los arts. 806 a 833 del Codigo Civil para un testador de vecindad civil foral **es sustantivamente erronea**, aunque este bien escrita. Por eso la vecindad civil se pregunta **antes que ningun dato del testador**, y una respuesta foral **detiene el proceso**.

---

## 2. Que determina la ley aplicable

**Art. 14.1 CC:** "La sujecion al derecho civil comun o al especial o foral **se determina por la vecindad civil**."

**Art. 16.1.1.ª CC:** en los conflictos de leyes internos, **la ley personal es la determinada por la vecindad civil**.

**Art. 9.8 CC (redaccion de la Ley 8/2021):** la sucesion por causa de muerte se rige por la ley nacional del causante **en el momento de su fallecimiento**. Las disposiciones hechas en testamento conforme a la ley nacional del testador **al tiempo de otorgarlas conservan su validez** aunque sea otra la ley que rija la sucesion, **si bien las legitimas se ajustaran a esta ultima**.

Consecuencia que conviene explicar al cliente: la vecindad civil **puede cambiar** despues de otorgar el testamento (apartado 3), y con ella el regimen de legitimas que se aplicara a su herencia. El testamento no "congela" la ley sucesoria.

---

## 3. Como se determina y como cambia la vecindad civil (art. 14 CC)

- **Por filiacion (art. 14.2):** tienen vecindad civil en territorio de derecho comun, o en uno foral, **los nacidos de padres que tengan tal vecindad**. Por la adopcion, el adoptado no emancipado adquiere la de los adoptantes.
- **Padres de distinta vecindad (art. 14.3):** el hijo tiene la de aquel respecto del cual la filiacion se determino antes; en su defecto, la del lugar de nacimiento; en ultimo termino, la de derecho comun. Los padres pueden atribuirle la de cualquiera de ellos dentro de los **seis meses** siguientes al nacimiento o a la adopcion. Desde los **catorce anos** y hasta un ano despues de su emancipacion, el hijo puede optar por la del lugar de su nacimiento o por la ultima de cualquiera de sus padres.
- **Matrimonio (art. 14.4):** **no altera** la vecindad civil. Cualquiera de los conyuges no separados puede, en todo momento, optar por la del otro.
- **Por residencia (art. 14.5):** se adquiere **por residencia continuada de dos anos con manifestacion expresa de esa voluntad**, o **por residencia continuada de diez anos sin declaracion en contrario**. Ambas declaraciones se hacen constar en el Registro Civil.
- **Duda (art. 14.6):** "En caso de duda **prevalecera la vecindad civil que corresponda al lugar de nacimiento**."

**Art. 15 CC (Ley 8/2021):** el extranjero que adquiere la nacionalidad espanola debe optar, al inscribirla, por la vecindad del lugar de residencia, la del lugar de nacimiento, la ultima de cualquiera de sus progenitores o adoptantes, o la del conyuge.

**Trampa frecuente:** vivir en Barcelona o en Bilbao **no significa** tener vecindad civil catalana o vasca, y haber nacido en Madrid no garantiza la comun si la familia era foral. La vecindad no se deduce del domicilio actual. Si el cliente no lo sabe con certeza, la skill **no lo presume**: lo trata como incertidumbre y escala.

---

## 4. Territorios con derecho civil foral o especial propio

Cataluna, Aragon, Navarra, Illes Balears, Pais Vasco y Galicia. Cada uno tiene su propia norma civil sucesoria, **ninguna de ellas verificada en esta skill** (ver `references/fuentes-plantillas-validadas.md`, punto 1 de "verificar manualmente").

Diferencias estructurales que ilustran por que no cabe adaptar la minuta comun:

- La cuantia y la naturaleza de la legitima difieren del sistema de tercios del art. 808 CC.
- El circulo de legitimarios no coincide con el del art. 807 CC.
- El **testamento mancomunado**, nulo en derecho comun (art. 669 CC), se admite en varios territorios forales.
- Los **pactos sucesorios**, con alcance muy limitado en derecho comun, tienen alli regulacion propia y uso habitual.

**Regla absoluta de la skill:** si la vecindad civil es foral, o el cliente no puede afirmarla con seguridad, **se detiene el proceso y se escala**. No se redacta la minuta "adaptandola despues", no se genera un borrador "provisional", y no se responde a la pregunta de cuanta legitima corresponde. La skill informa de por que se detiene y deriva a un especialista en el derecho civil de ese territorio.

---

## 5. Elemento internacional

Si el testador tiene otra nacionalidad, residencia habitual en el extranjero o bienes situados fuera de Espana, entra en juego el **Reglamento (UE) 650/2012** en materia de sucesiones, cuya regla general es la ley de la residencia habitual del causante al fallecer, con posibilidad de eleccion de la ley de la nacionalidad. Esa norma **no esta verificada en esta skill**.

**Regla operativa:** cualquier elemento internacional es causa de **escalacion**. La skill lo detecta y lo advierte; no redacta la professio iuris ni valora la ley aplicable.

---

## 6. Texto fijo de la advertencia de detencion (visible al cliente)

Cuando la vecindad civil resulte foral, o el cliente no pueda afirmarla, la skill emite este mensaje y **no crea ningun documento**:

"Su caso queda fuera del alcance de esta herramienta. La sujecion al derecho civil comun o al foral se determina por la vecindad civil, conforme al articulo 14 del Codigo Civil, y en los territorios con derecho civil propio el regimen de legitimas y de sucesion difiere sustancialmente del Codigo Civil comun sobre el que se ha elaborado esta documentacion. Redactar su testamento con las reglas del Codigo Civil comun produciria disposiciones incorrectas. Le recomiendo acudir a un abogado o notario especializado en el derecho civil de su territorio. Puede consultar el texto oficial del articulo 14 del Codigo Civil en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
