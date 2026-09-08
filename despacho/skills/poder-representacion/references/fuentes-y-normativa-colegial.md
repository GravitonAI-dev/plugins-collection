# Fuentes Oficiales y Normativa Aplicable

> Material de referencia para la skill `poder-representacion`.

---

## Regla de verificación permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una versión posterior a la registrada, aplica la redacción vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la referencia local y se advierte al usuario de que la verificación queda pendiente.

---

## Fuentes normativas

| Norma | Identificación | Preceptos relevantes |
|---|---|---|
| Ley 1/2000, de Enjuiciamiento Civil | BOE-A-2000-323 | 23 (comparecencia por procurador), 24 (forma del poder), **25 (poder general y poderes especiales)**, 26 (aceptación y deberes del procurador) |
| Ley 36/2011, reguladora de la Jurisdicción Social | BOE-A-2011-15936 | 18 y 21 (representación y defensa en el orden social) |
| Ley 39/2015, del Procedimiento Administrativo Común de las Administraciones Públicas | Verificar identificador BOE | **5 (representación)** y 6 (registros electrónicos de apoderamientos) |
| Estatuto General de la Abogacía Española, aprobado por Real Decreto 135/2021 | Verificar identificador BOE | Deberes en la asunción y cese de la dirección técnica |
| Legislación notarial | Verificar norma e identificador | Forma del instrumento público y juicio de capacidad |

**Regla estricta:** esta skill no consigna identificadores BOE ni números de artículo que no haya verificado en la sesión. El artículo 25.2 de la Ley de Enjuiciamiento Civil, por su carácter central, se verifica **siempre** antes de enumerar las facultades que exigen poder especial.

---

## Registros electrónicos de apoderamientos

Existen registros distintos según el ámbito, con denominaciones, sedes y requisitos propios que **deben verificarse con `web_search` en cada asunto**:

| Ámbito | Registro | Qué verificar |
|---|---|---|
| Judicial | Registro electrónico de apoderamientos judiciales | Sede de acceso, medios de identificación admitidos, y si el apoderamiento apud acta electrónico se practica ante el órgano o en la sede general |
| Administración General del Estado | Registro electrónico de apoderamientos de ámbito estatal | Tipos de poder inscribibles, plazos de vigencia y efectos de la inscripción |
| Comunidades autónomas y entidades locales | Registros propios, con interoperabilidad variable | Si la administración destinataria admite el registro estatal o exige el propio |

Advertencia operativa: la existencia de un registro no significa que la administración o el órgano lo consulte de oficio. Comprobar si hay que aportar además la acreditación al expediente.

---

## Aranceles y costes

| Instrumento | Coste |
|---|---|
| Poder notarial | Arancel notarial, según el tipo de poder y las copias solicitadas |
| Apoderamiento apud acta ante el letrado de la Administración de Justicia | Sin coste |
| Apoderamiento apud acta por comparecencia electrónica | Sin coste, requiere medio de identificación electrónica |
| Inscripción en registro electrónico de apoderamientos | Sin coste, con requisitos de identificación |

**Los importes de arancel no se consignan de memoria.** Si el cliente necesita una estimación, se le remite a la notaría.

---

## Estilo de redacción

Principios aplicados en los assets: en las minutas de poder, estructura de OTORGANTE / APODERADOS / ÁMBITO / FACULTADES, con las facultades ordinarias enumeradas y las del artículo 25.2 en **tabla de decisión expresa**, para que el otorgante se pronuncie una a una y quede constancia de lo concedido y de lo excluido; en los escritos judiciales, estructura AL JUZGADO / DIGO / SOLICITO con aceptación del apoderado; en la autorización administrativa, tabla que refleja la distinción legal entre actos de mero trámite y actuaciones que exigen acreditación; bloque final de advertencias dirigido al profesional que revisa, con la insistencia en que la minuta no es la escritura y en que el notario es quien valora capacidad y suficiencia de facultades.
