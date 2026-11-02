# Vecindad Civil: el Filtro de Alcance de esta Skill

> Material de referencia para la skill `derecho-civil-testamento-planificacion`. Código Civil verificado en el BOE
> (BOE-A-1889-4763) el 03/09/2026. Determina cuándo la skill PUEDE redactar y cuando DEBE detenerse.
> No forma parte del output al usuario.

---

## 1. Por qué este es el primer filtro y no un detalle

El régimen sucesorio español **no es uno solo**. El Código Civil común convive con seis derechos civiles forales o especiales con normativa sucesoria propia, y las diferencias no son de matiz: cambian la cuantía de la legítima, quiénes son legitimarios, si la legítima es un derecho a bienes o un simple crédito, si cabe el testamento mancomunado y si son válidos los pactos sucesorios.

Una minuta redactada sobre los arts. 806 a 833 del Código Civil para un testador de vecindad civil foral **es sustantivamente errónea**, aunque esté bien escrita. Por eso la vecindad civil se pregunta **antes que ningún dato del testador**, y una respuesta foral **detiene el proceso**.

---

## 2. Que determina la ley aplicable

**Art. 14.1 CC:** "La sujeción al derecho civil común o al especial o foral **se determina por la vecindad civil**."

**Art. 16.1.1.ª CC:** en los conflictos de leyes internos, **la ley personal es la determinada por la vecindad civil**.

**Art. 9.8 CC (redacción de la Ley 8/2021):** la sucesión por causa de muerte se rige por la ley nacional del causante **en el momento de su fallecimiento**. Las disposiciones hechas en testamento conforme a la ley nacional del testador **al tiempo de otorgarlas conservan su validez** aunque sea otra la ley que rija la sucesión, **si bien las legitimas se ajustaran a esta última**.

Consecuencia que conviene explicar al cliente: la vecindad civil **puede cambiar** después de otorgar el testamento (apartado 3), y con ella el régimen de legitimas que se aplicará a su herencia. El testamento no "congela" la ley sucesoria.

---

## 3. Como se determina y como cambia la vecindad civil (art. 14 CC)

- **Por filiación (art. 14.2):** tienen vecindad civil en territorio de derecho común, o en uno foral, **los nacidos de padres que tengan tal vecindad**. Por la adopción, el adoptado no emancipado adquiere la de los adoptantes.
- **Padres de distinta vecindad (art. 14.3):** el hijo tiene la de aquel respecto del cual la filiación se determino antes; en su defecto, la del lugar de nacimiento; en último término, la de derecho común. Los padres pueden atribuirle la de cualquiera de ellos dentro de los **seis meses** siguientes al nacimiento o a la adopción. Desde los **catorce años** y hasta un año después de su emancipación, el hijo puede optar por la del lugar de su nacimiento o por la última de cualquiera de sus padres.
- **Matrimonio (art. 14.4):** **no altera** la vecindad civil. Cualquiera de los cónyuges no separados puede, en todo momento, optar por la del otro.
- **Por residencia (art. 14.5):** se adquiere **por residencia continuada de dos años con manifestación expresa de esa voluntad**, o **por residencia continuada de diez años sin declaración en contrario**. Ambas declaraciones se hacen constar en el Registro Civil.
- **Duda (art. 14.6):** "En caso de duda **prevalecerá la vecindad civil que corresponda al lugar de nacimiento**."

**Art. 15 CC (Ley 8/2021):** el extranjero que adquiere la nacionalidad española debe optar, al inscribirla, por la vecindad del lugar de residencia, la del lugar de nacimiento, la última de cualquiera de sus progenitores o adoptantes, o la del cónyuge.

**Trampa frecuente:** vivir en Barcelona o en Bilbao **no significa** tener vecindad civil catalana o vasca, y haber nacido en Madrid no garantiza la común si la familia era foral. La vecindad no se deduce del domicilio actual. Si el cliente no lo sabe con certeza, la skill **no lo presume**: lo trata como incertidumbre y escala.

---

## 4. Territorios con derecho civil foral o especial propio

Cataluña, Aragon, Navarra, Illes Balears, País Vasco y Galicia. Cada uno tiene su propia norma civil sucesoria, **ninguna de ellas verificada en esta skill** (ver `references/fuentes-plantillas-validadas.md`, punto 1 de "verificar manualmente").

Diferencias estructurales que ilustran por qué no cabe adaptar la minuta común:

- La cuantía y la naturaleza de la legítima difieren del sistema de tercios del art. 808 CC.
- El circulo de legitimarios no coincide con el del art. 807 CC.
- El **testamento mancomunado**, nulo en derecho común (art. 669 CC), se admite en varios territorios forales.
- Los **pactos sucesorios**, con alcance muy limitado en derecho común, tienen allí regulación propia y uso habitual.

**Regla absoluta de la skill:** si la vecindad civil es foral, o el cliente no puede afirmarla con seguridad, **se detiene el proceso y se escala**. No se redacta la minuta "adaptándola después", no se genera un borrador "provisional", y no se responde a la pregunta de cuanta legítima corresponde. La skill informa de por qué se detiene y deriva a un especialista en el derecho civil de ese territorio.

---

## 5. Elemento internacional

Si el testador tiene otra nacionalidad, residencia habitual en el extranjero o bienes situados fuera de España, entra en juego el **Reglamento (UE) 650/2012** en materia de sucesiones, cuya regla general es la ley de la residencia habitual del causante al fallecer, con posibilidad de elección de la ley de la nacionalidad. Esa norma **no está verificada en esta skill**.

**Regla operativa:** cualquier elemento internacional es causa de **escalación**. La skill lo detecta y lo advierte; no redacta la professio iuris ni valora la ley aplicable.

---

## 6. Texto fijo de la advertencia de detención (visible al cliente)

Cuando la vecindad civil resulte foral, o el cliente no pueda afirmarla, la skill emite este mensaje y **no crea ningún documento**:

"Su caso queda fuera del alcance de esta herramienta. La sujeción al derecho civil común o al foral se determina por la vecindad civil, conforme al artículo 14 del Código Civil, y en los territorios con derecho civil propio el régimen de legitimas y de sucesión difiere sustancialmente del Código Civil común sobre el que se ha elaborado esta documentación. Redactar su testamento con las reglas del Código Civil común produciría disposiciones incorrectas. Le recomiendo acudir a un abogado o notario especializado en el derecho civil de su territorio. Puede consultar el texto oficial del artículo 14 del Código Civil en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
