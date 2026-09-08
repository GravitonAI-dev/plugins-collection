# Vias de Reclamacion y Organismo Competente por Sector

> Referencia de la skill `reclamacion-consumo`. El organismo, el plazo y la forma de presentacion se
> verifican con `web_search` en cada caso: cambian por sector y por comunidad autonoma.

---

## 1. El itinerario general

```
1. Reclamacion a la empresa          -> imprescindible, y de ella dependen todos los pasos siguientes
2. Hoja oficial de reclamaciones     -> en el establecimiento, modelo autonomico
3. Administracion de consumo         -> oficina municipal o direccion general autonomica
4. Arbitraje de consumo              -> gratuito, laudo vinculante, voluntario para la empresa no adherida
5. Via judicial                      -> con el requisito previo del medio adecuado de solucion de controversias
```

**Regla practica:** ningun escalon se salta. Los organismos exigen acreditar el anterior, y saltarselo devuelve el expediente y consume plazo.

---

## 2. Sectores con supervisor propio

En cuatro sectores existe una via especifica que **precede o sustituye** a la administracion general de consumo. Es el error mas frecuente: presentar en consumo lo que corresponde al supervisor sectorial.

| Sector | Primer paso | Segundo paso | Que verificar antes de redactar |
|---|---|---|---|
| Banca, financiacion y seguros | Servicio de atencion al cliente o defensor del cliente de la entidad | Supervisor competente en la materia | Denominacion vigente del organismo, plazo de respuesta de la entidad y plazo para acudir al supervisor |
| Telecomunicaciones | Servicio de atencion al cliente del operador, con numero de referencia | Oficina de atencion al usuario de telecomunicaciones | Plazo para acudir tras la respuesta o su ausencia, y forma de presentacion |
| Electricidad, gas y agua | Servicio de atencion de la comercializadora o distribuidora | Organismo competente de la comunidad autonoma | Que organismo es en esa comunidad, y si el asunto es de comercializadora o de distribuidora |
| Transporte aereo | Reclamacion a la compania | Organismo nacional de supervision | Regimen del Reglamento (CE) 261/2004 y plazo de reclamacion |

**Nota sobre banca:** es el sector con mas reclamaciones de consumo en Espana. Conviene ser especialmente preciso con el numero de referencia que asigna el servicio de atencion al cliente: sin el, el supervisor no admite el expediente.

---

## 3. Que documento corresponde a cada paso

| Paso | Asset |
|---|---|
| Reclamacion a la empresa | `assets/template-reclamacion-previa-empresa.md` |
| Hoja oficial | `assets/template-hoja-reclamaciones.md` |
| Administracion de consumo | `assets/template-escrito-administracion-consumo.md` |
| Arbitraje | `assets/template-solicitud-arbitraje-consumo.md` |
| Via judicial | Fuera de esta skill: `derecho-civil:reclamacion-cantidad` |

---

## 4. Lo que hay que preguntar para acertar de organismo

1. **Comunidad autonoma** del domicilio del consumidor y del establecimiento. No siempre coinciden, y determina la competencia.
2. **Sector** de la empresa.
3. **Si ya existe numero de referencia** de una reclamacion previa.
4. **Si la empresa opera solo en linea**, en cuyo caso hay que localizar su domicilio social.

---

## 5. Derivaciones fuera del plugin

| Situacion | Skill |
|---|---|
| Se pide declarar nula una clausula del contrato | `derecho-civil:reclamacion-clausulas-abusivas` |
| Hay danos personales o lesiones | `derecho-civil:responsabilidad-civil` |
| Procede ya demandar el pago | `derecho-civil:reclamacion-cantidad` |
| Falta el intento previo exigido para demandar | `derecho-civil:masc-acuerdos` |
| Quien reclama es empresario o profesional | `derecho-civil:reclamacion-cantidad`, con el regimen ordinario |
