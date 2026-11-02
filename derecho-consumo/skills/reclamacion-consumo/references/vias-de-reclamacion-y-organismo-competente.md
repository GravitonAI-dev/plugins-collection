# Vías de Reclamación y Organismo Competente por Sector

> Referencia de la skill `reclamacion-consumo`. El organismo, el plazo y la forma de presentación se
> verifican con `web_search` en cada caso: cambian por sector y por comunidad autónoma.

---

## 1. El itinerario general

```
1. Reclamación a la empresa          -> imprescindible, y de ella dependen todos los pasos siguientes
2. Hoja oficial de reclamaciones     -> en el establecimiento, modelo autonómico
3. Administración de consumo         -> oficina municipal o dirección general autonómica
4. Arbitraje de consumo              -> gratuito, laudo vinculante, voluntario para la empresa no adherida
5. Vía judicial                      -> con el requisito previo del medio adecuado de solución de controversias
```

**Regla práctica:** ningún escalón se salta. Los organismos exigen acreditar el anterior, y saltárselo devuelve el expediente y consume plazo.

---

## 2. Sectores con supervisor propio

En cuatro sectores existe una vía específica que **precede o sustituye** a la administración general de consumo. Es el error más frecuente: presentar en consumo lo que corresponde al supervisor sectorial.

| Sector | Primer paso | Segundo paso | Qué verificar antes de redactar |
|---|---|---|---|
| Banca, financiación y seguros | Servicio de atención al cliente o defensor del cliente de la entidad | Supervisor competente en la materia | Denominación vigente del organismo, plazo de respuesta de la entidad y plazo para acudir al supervisor |
| Telecomunicaciones | Servicio de atención al cliente del operador, con número de referencia | Oficina de atención al usuario de telecomunicaciones | Plazo para acudir tras la respuesta o su ausencia, y forma de presentación |
| Electricidad, gas y agua | Servicio de atención de la comercializadora o distribuidora | Organismo competente de la comunidad autónoma | Qué organismo es en esa comunidad, y si el asunto es de comercializadora o de distribuidora |
| Transporte aéreo | Reclamación a la compañía | Organismo nacional de supervisión | Régimen del Reglamento (CE) 261/2004 y plazo de reclamación |

**Nota sobre banca:** es el sector con más reclamaciones de consumo en España. Conviene ser especialmente preciso con el número de referencia que asigna el servicio de atención al cliente: sin él, el supervisor no admite el expediente.

---

## 3. Que documento corresponde a cada paso

| Paso | Asset |
|---|---|
| Reclamación a la empresa | `assets/template-reclamacion-previa-empresa.md` |
| Hoja oficial | `assets/template-hoja-reclamaciones.md` |
| Administración de consumo | `assets/template-escrito-administracion-consumo.md` |
| Arbitraje | `assets/template-solicitud-arbitraje-consumo.md` |
| Vía judicial | Fuera de esta skill: `derecho-civil:reclamacion-cantidad` |

---

## 4. Lo que hay que preguntar para acertar de organismo

1. **Comunidad autónoma** del domicilio del consumidor y del establecimiento. No siempre coinciden, y determina la competencia.
2. **Sector** de la empresa.
3. **Si ya existe número de referencia** de una reclamación previa.
4. **Si la empresa opera solo en línea**, en cuyo caso hay que localizar su domicilio social.

---

## 5. Derivaciones fuera del plugin

| Situación | Skill |
|---|---|
| Se pide declarar nula una cláusula del contrato | `derecho-civil:reclamacion-clausulas-abusivas` |
| Hay daños personales o lesiones | `derecho-civil:responsabilidad-civil` |
| Procede ya demandar el pago | `derecho-civil:reclamacion-cantidad` |
| Falta el intento previo exigido para demandar | `derecho-civil:masc-acuerdos` |
| Quien reclama es empresario o profesional | `derecho-civil:reclamacion-cantidad`, con el régimen ordinario |
