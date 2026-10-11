# Maquetas de reportes

Cada reporte se construye con dos piezas:

1. **La base** (`assets/template-base-reportes.md`). Se copia integra: estilos, tema claro y oscuro, impresion, aviso DRAFT, cabecera, pie con fuentes y motor de graficos. No se resume ni se recorta.
2. **La maqueta** del tipo de entregable elegido (este documento). Rellena los marcadores de la base:
   - `{{ANCHO}}`: el ancho de la maqueta;
   - `{{FICHA}}` y `{{CONTENIDO}}`: sus partes `ficha` y `contenido`;
   - `{{ESTILOS_MAQUETA}}`: su parte `estilos`, o se borra la linea si no tiene;
   - `{{ACCIONES}}`: su parte `acciones`, o se borra si no tiene;
   - el bloque `datos-reporte`: su parte `datos`, completada con los datos del caso.

Los graficos **no se dibujan a mano**. En el HTML solo se coloca el hueco, `<figure class="grafico" data-grafico="nombre"></figure>`, y en el bloque `datos-reporte` se declaran los datos con ese mismo nombre. El motor dibuja el grafico, su tabla de datos, su fuente y el pie de fuentes del documento. El contrato de datos de cada tipo de grafico esta en `biblioteca-componentes-visuales.md`.

Reglas comunes a todas las maquetas:

- El tema se fija en la etiqueta `html`: `data-tema="moderno"` o `data-tema="sobrio"`.
- Los bloques se pueden repetir, quitar o reordenar. Lo que no cambia es la estructura de cada bloque: las clases son las de la base y no se renombran.
- Toda cifra del texto que salga de un grafico se escribe con `<span data-cifra="clave"></span>` y se declara en `cifras`. Asi el texto y el grafico no pueden contradecirse.
- Las cifras que no salen de un grafico (un plazo en meses, una fecha) se escriben como texto.

---

## 1. Panel de datos (`panel_datos`)

**Ancho:** `1120px`. Rejilla de tarjetas con indicadores, graficos y tabla de detalle.

### Ficha

```html maqueta=panel_datos parte=ficha
<li><b>Periodo:</b> {{PERIODO}}</li>
      <li><b>Actualizado:</b> {{FECHA_ACTUALIZACION}}</li>
```

### Contenido

```html maqueta=panel_datos parte=contenido
<div class="indicadores">
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_1_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_1"></p>
      <p class="detalle">{{INDICADOR_1_DETALLE}}</p>
      <div class="tendencia" data-grafico="tendencia"></div>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_2_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_2"></p>
      <p class="detalle">{{INDICADOR_2_DETALLE}}</p>
    </div>
    <div class="indicador aparece es-atencion">
      <p class="rotulo">{{INDICADOR_3_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_3_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_3_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_4_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_4"></p>
      <p class="detalle">{{INDICADOR_4_DETALLE}}</p>
    </div>
  </div>

  <div class="malla">
    <section class="tarjeta">
      <h2>{{TITULO_COMPARATIVA}}</h2>
      <p class="subtitulo">{{SUBTITULO_COMPARATIVA}}</p>
      <figure class="grafico" data-grafico="comparativa"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_REPARTO}}</h2>
      <p class="subtitulo">{{SUBTITULO_REPARTO}}</p>
      <figure class="grafico" data-grafico="reparto"></figure>
    </section>
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_EVOLUCION}}</h2>
      <p class="subtitulo">{{SUBTITULO_EVOLUCION}}</p>
      <figure class="grafico" data-grafico="evolucion"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_DESCOMPOSICION}}</h2>
      <p class="subtitulo">{{SUBTITULO_DESCOMPOSICION}}</p>
      <figure class="grafico" data-grafico="descomposicion"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_MEDIDOR}}</h2>
      <p class="subtitulo">{{SUBTITULO_MEDIDOR}}</p>
      <figure class="grafico" data-grafico="medidor"></figure>
      <div class="aviso">
        <span class="titulo">{{TITULO_NOTA_MEDIDOR}}</span>
        {{NOTA_MEDIDOR}}
      </div>
    </section>
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_TABLA}}</h2>
      <p class="subtitulo">{{SUBTITULO_TABLA}}</p>
      <div class="tabla">
        <table>
          <thead>
            <tr><th>{{COLUMNA_1}}</th><th>{{COLUMNA_2}}</th><th class="cifra">{{COLUMNA_3}}</th><th class="cifra">{{COLUMNA_4}}</th><th>{{COLUMNA_5}}</th></tr>
          </thead>
          <tbody>
            <tr><td>{{FILA_1_C1}}</td><td>{{FILA_1_C2}}</td><td class="cifra">{{FILA_1_C3}}</td><td class="cifra">{{FILA_1_C4}}</td><td><span class="distintivo">{{FILA_1_C5}}</span></td></tr>
            <tr><td>{{FILA_2_C1}}</td><td>{{FILA_2_C2}}</td><td class="cifra">{{FILA_2_C3}}</td><td class="cifra">{{FILA_2_C4}}</td><td><span class="distintivo">{{FILA_2_C5}}</span></td></tr>
          </tbody>
          <tfoot>
            <tr><td>{{TOTAL_ROTULO}}</td><td></td><td class="cifra">{{TOTAL_C3}}</td><td class="cifra"></td><td></td></tr>
          </tfoot>
        </table>
      </div>
    </section>
  </div>
```

### Datos

```json maqueta=panel_datos parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {
    "indicador_1": {"de": "evolucion", "calculo": "ultimo", "unidad": "eur"},
    "indicador_2": {"de": "descomposicion", "calculo": "suma", "unidad": "eur"},
    "indicador_4": {"valor": 0, "unidad": "eur"}
  },
  "graficos": {
    "tendencia": {"tipo": "chispa", "valores": [], "etiquetas": [], "resumen": "{{RESUMEN}}"},
    "comparativa": {"tipo": "barras", "unidad": "eur", "fuente": "cliente", "elementos": []},
    "reparto": {"tipo": "anillo", "unidad": "eur", "fuente": "cliente", "porciones": [], "centro": {"rotulo": "{{ROTULO_CENTRO}}"}},
    "evolucion": {"tipo": "linea", "unidad": "eur", "fuente": "cliente", "etiquetas": [], "series": [], "umbral": null, "anotaciones": []},
    "descomposicion": {"tipo": "cascada", "unidad": "eur", "fuente": "cliente", "pasos": [], "total": {"rotulo": "{{ROTULO_TOTAL}}"}},
    "medidor": {"tipo": "medidor", "valor": 0, "maximo": 100, "rotulo": "{{ROTULO_MEDIDOR}}"}
  }
}
```

---

## 2. Informe visual (`informe_visual`)

**Ancho:** `1000px`. Lectura secuencial con indice lateral, secciones numeradas, tabla, cronologia, avisos y firmas. Admite graficos dentro de cualquier seccion.

### Ficha

```html maqueta=informe_visual parte=ficha
<li><b>Referencia:</b> {{REFERENCIA_EXPEDIENTE}}</li>
      <li><b>Fecha:</b> {{FECHA_EMISION}}</li>
      <li><b>Destinatario:</b> {{DESTINATARIO}}</li>
      <li><b>Preparado por:</b> {{AUTOR}}</li>
```

### Estilos

```css maqueta=informe_visual parte=estilos
.diseno{display:grid;grid-template-columns:196px minmax(0,1fr);gap:var(--e5);align-items:start}
.indice{position:sticky;top:var(--e4);font-size:.85rem}
.indice p{font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;color:var(--apagado);margin:0 0 var(--e2)}
.indice ol{list-style:none;margin:0;padding:0;border-left:2px solid var(--borde)}
.indice li{margin:0}
.indice a{display:block;padding:7px 0 7px 14px;color:var(--apagado);text-decoration:none;border-left:2px solid transparent;margin-left:-2px}
.indice a:hover{color:var(--acento);border-left-color:var(--acento)}
.bloque{margin:0 0 var(--e3)}
.bloque h2{display:flex;gap:var(--e2);align-items:baseline}
.bloque h2 .orden{color:var(--acento);font-variant-numeric:tabular-nums}
.cronologia{list-style:none;margin:var(--e4) 0 0;padding:0 0 0 26px;border-left:2px solid var(--borde)}
.cronologia li{position:relative;margin:0 0 var(--e4)}
.cronologia li:last-child{margin-bottom:0}
.cronologia li::before{content:"";position:absolute;left:-33px;top:6px;width:12px;height:12px;border-radius:50%;
  background:var(--acento);border:3px solid var(--superficie);box-shadow:0 0 0 1px var(--borde)}
.cronologia .fecha{display:block;font-size:.76rem;letter-spacing:.07em;text-transform:uppercase;color:var(--apagado)}
.cronologia .hito{font-weight:650}
.firma{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:var(--e4);margin:var(--e4) 0 0;font-size:.9rem}
.firma div{border-top:1px solid var(--borde);padding-top:var(--e2);color:var(--apagado)}
@media (max-width:900px){.diseno{grid-template-columns:1fr}.indice{display:none}}
@media print{.diseno{display:block}.indice{display:none}}
```

### Contenido

```html maqueta=informe_visual parte=contenido
<div class="indicadores">
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_1_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_1_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_1_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_2_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_2_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_2_DETALLE}}</p>
    </div>
    <div class="indicador aparece es-riesgo">
      <p class="rotulo">{{INDICADOR_3_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_3_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_3_DETALLE}}</p>
    </div>
  </div>

  <div class="diseno">
    <nav class="indice" aria-label="Indice del documento">
      <p>Contenido</p>
      <ol>
        <li><a href="#seccion-1">{{TITULO_SECCION_1}}</a></li>
        <li><a href="#seccion-2">{{TITULO_SECCION_2}}</a></li>
        <li><a href="#seccion-3">{{TITULO_SECCION_3}}</a></li>
        <li><a href="#seccion-4">{{TITULO_SECCION_4}}</a></li>
      </ol>
    </nav>
    <div>
      <section class="tarjeta bloque" id="seccion-1">
        <h2><span class="orden">1.</span>{{TITULO_SECCION_1}}</h2>
        <p class="subtitulo">{{SUBTITULO_SECCION_1}}</p>
        <p>{{CONTENIDO_SECCION_1}}</p>
        <div class="aviso">
          <span class="titulo">{{TITULO_NOTA}}</span>
          {{CONTENIDO_NOTA}}
        </div>
      </section>
      <section class="tarjeta bloque" id="seccion-2">
        <h2><span class="orden">2.</span>{{TITULO_SECCION_2}}</h2>
        <p class="subtitulo">{{SUBTITULO_SECCION_2}}</p>
        <p>{{CONTENIDO_SECCION_2}}</p>
        <div class="tabla">
          <table>
            <caption>{{TITULO_TABLA}}</caption>
            <thead>
              <tr><th>{{COLUMNA_1}}</th><th>{{COLUMNA_2}}</th><th class="cifra">{{COLUMNA_3}}</th><th>{{COLUMNA_4}}</th></tr>
            </thead>
            <tbody>
              <tr><td>{{FILA_1_C1}}</td><td>{{FILA_1_C2}}</td><td class="cifra">{{FILA_1_C3}}</td><td><span class="distintivo">{{FILA_1_C4}}</span></td></tr>
              <tr><td>{{FILA_2_C1}}</td><td>{{FILA_2_C2}}</td><td class="cifra">{{FILA_2_C3}}</td><td><span class="distintivo">{{FILA_2_C4}}</span></td></tr>
            </tbody>
          </table>
        </div>
      </section>
      <section class="tarjeta bloque" id="seccion-3">
        <h2><span class="orden">3.</span>{{TITULO_SECCION_3}}</h2>
        <p class="subtitulo">{{SUBTITULO_SECCION_3}}</p>
        <p>{{CONTENIDO_SECCION_3}}</p>
        <figure class="grafico" data-grafico="plazos"></figure>
        <ol class="cronologia">
          <li><span class="fecha">{{HITO_1_FECHA}}</span><span class="hito">{{HITO_1_TITULO}}</span><br>{{HITO_1_DETALLE}}</li>
          <li><span class="fecha">{{HITO_2_FECHA}}</span><span class="hito">{{HITO_2_TITULO}}</span><br>{{HITO_2_DETALLE}}</li>
        </ol>
      </section>
      <section class="tarjeta bloque" id="seccion-4">
        <h2><span class="orden">4.</span>{{TITULO_SECCION_4}}</h2>
        <p class="subtitulo">{{SUBTITULO_SECCION_4}}</p>
        <p>{{CONTENIDO_SECCION_4}}</p>
        <ol>
          <li>{{PASO_1}}</li>
          <li>{{PASO_2}}</li>
        </ol>
        <div class="aviso riesgo">
          <span class="titulo">{{TITULO_ADVERTENCIA}}</span>
          {{CONTENIDO_ADVERTENCIA}}
        </div>
        <div class="firma">
          <div>{{FIRMA_1}}</div>
          <div>{{FIRMA_2}}</div>
        </div>
      </section>
    </div>
  </div>
```

### Datos

```json maqueta=informe_visual parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {},
  "graficos": {
    "plazos": {"tipo": "plazos", "hoy": "{{FECHA_AAAA_MM_DD}}", "plazos": [], "fuente": "cliente"}
  }
}
```

---

## 3. Herramienta interactiva (`herramienta_interactiva`)

**Ancho:** `1020px`. Panel de entrada, recalculo inmediato, medidor que se mueve con el resultado, desglose y lista de verificacion.

La herramienta es la unica maqueta que anade codigo: un **segundo** `<script>`, colocado justo despues del script del motor. En ese script solo cambia la funcion `calcular`. Las cifras se formatean con el motor (`Reportes.fmt`, que respeta el idioma y la moneda del bloque de datos) y el medidor lo sigue dibujando el motor: el script le pasa el nuevo valor con `Reportes.actualizar("resultado", {valor: ...})`.

### Ficha

```html maqueta=herramienta_interactiva parte=ficha
<li><b>Referencia:</b> {{REFERENCIA_EXPEDIENTE}}</li>
```

### Estilos

```css maqueta=herramienta_interactiva parte=estilos
.columnas{display:grid;grid-template-columns:minmax(290px,1fr) minmax(320px,1.2fr);gap:var(--e3);align-items:start}
.columnas .tarjeta + .tarjeta{margin-top:var(--e3)}
.campo{margin:0 0 var(--e4)}
.campo label{display:block;font-size:.86rem;font-weight:620;margin-bottom:6px}
.campo .ayuda{display:block;font-size:.78rem;color:var(--apagado);margin-top:6px}
input,select{width:100%;font:inherit;font-size:.95rem;color:var(--texto);background:var(--superficie-2);
  border:1px solid var(--borde);border-radius:var(--radio-s);padding:10px 12px}
input:focus,select:focus{border-color:var(--acento)}
input[type=number]{font-variant-numeric:tabular-nums}
.resultados{display:grid;grid-template-columns:repeat(auto-fit,minmax(126px,1fr));gap:var(--e3);margin:0 0 var(--e4)}
.resultado{background:var(--superficie-2);border:1px solid var(--borde-suave);border-radius:var(--radio-s);padding:var(--e3) var(--e4)}
.resultado .rotulo{font-size:.73rem;text-transform:uppercase;letter-spacing:.09em;color:var(--apagado);margin:0 0 5px}
.resultado .cifra{font-size:clamp(1rem,1.45vw,1.3rem);white-space:nowrap;font-weight:670;letter-spacing:-.025em;margin:0;font-variant-numeric:tabular-nums}
.resultado.principal{background:var(--acento-suave);border-color:var(--acento)}
.resultado.principal .cifra{color:var(--acento-fuerte)}
.verificacion{list-style:none;margin:0;padding:0}
.verificacion li{display:flex;gap:var(--e3);align-items:flex-start;padding:10px 0;border-bottom:1px solid var(--borde-suave)}
.verificacion li:last-child{border-bottom:none}
.verificacion input[type=checkbox]{width:17px;height:17px;margin-top:3px;flex:0 0 auto;accent-color:var(--acento)}
.verificacion .texto{font-size:.93rem}
.verificacion .texto small{display:block;color:var(--apagado);font-size:.8rem}
.progreso{height:9px;border-radius:999px;background:var(--superficie-2);border:1px solid var(--borde-suave);overflow:hidden;margin:var(--e4) 0 6px}
.progreso span{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--ok),color-mix(in srgb,var(--ok) 70%,white));transition:width .25s ease}
.progreso-texto{font-size:.82rem;color:var(--apagado);margin:0}
@media (max-width:760px){.columnas{grid-template-columns:1fr}}
@media print{
  .columnas{grid-template-columns:1fr}
  /* Una tarjeta mas alta que un A4 no puede evitar el corte: se deja partir y se protegen sus bloques. */
  .permite-corte{break-inside:auto}
  .permite-corte .grafico,.permite-corte .resultados,.permite-corte .tabla,.permite-corte .aviso{break-inside:avoid}
}
```

### Acciones

```html maqueta=herramienta_interactiva parte=acciones
<button type="button" id="reiniciar">Restablecer valores</button>
```

### Contenido

```html maqueta=herramienta_interactiva parte=contenido
<div class="columnas">
    <div>
      <section class="tarjeta aparece">
        <h2>{{TITULO_PANEL_ENTRADA}}</h2>
        <p class="subtitulo">{{SUBTITULO_PANEL_ENTRADA}}</p>
        <form id="formulario">
          <div class="campo">
            <label for="campo1">{{CAMPO_1_ROTULO}}</label>
            <input type="number" id="campo1" name="campo1" step="0.01" min="0" value="{{CAMPO_1_VALOR_INICIAL}}">
            <span class="ayuda">{{CAMPO_1_AYUDA}}</span>
          </div>
          <div class="campo">
            <label for="campo2">{{CAMPO_2_ROTULO}}</label>
            <input type="number" id="campo2" name="campo2" step="0.01" min="0" value="{{CAMPO_2_VALOR_INICIAL}}">
            <span class="ayuda">{{CAMPO_2_AYUDA}}</span>
          </div>
          <div class="campo">
            <label for="campo3">{{CAMPO_3_ROTULO}}</label>
            <input type="number" id="campo3" name="campo3" step="1" min="0" value="{{CAMPO_3_VALOR_INICIAL}}">
            <span class="ayuda">{{CAMPO_3_AYUDA}}</span>
          </div>
          <div class="campo">
            <label for="campo4">{{CAMPO_4_ROTULO}}</label>
            <select id="campo4" name="campo4">
              <option value="{{OPCION_1_VALOR}}">{{OPCION_1_ROTULO}}</option>
              <option value="{{OPCION_2_VALOR}}">{{OPCION_2_ROTULO}}</option>
            </select>
            <span class="ayuda">{{CAMPO_4_AYUDA}}</span>
          </div>
        </form>
      </section>
      <section class="tarjeta aparece">
        <h2>{{TITULO_VERIFICACION}}</h2>
        <p class="subtitulo">{{SUBTITULO_VERIFICACION}}</p>
        <ul class="verificacion" id="verificacion">
          <li><input type="checkbox" id="punto1"><label class="texto" for="punto1">{{PUNTO_1}}<small>{{PUNTO_1_DETALLE}}</small></label></li>
          <li><input type="checkbox" id="punto2"><label class="texto" for="punto2">{{PUNTO_2}}<small>{{PUNTO_2_DETALLE}}</small></label></li>
          <li><input type="checkbox" id="punto3"><label class="texto" for="punto3">{{PUNTO_3}}<small>{{PUNTO_3_DETALLE}}</small></label></li>
        </ul>
        <div class="progreso"><span id="barra-progreso"></span></div>
        <p class="progreso-texto" id="texto-progreso"></p>
      </section>
    </div>
    <div>
      <section class="tarjeta aparece permite-corte">
        <h2>{{TITULO_PANEL_RESULTADO}}</h2>
        <p class="subtitulo">{{SUBTITULO_PANEL_RESULTADO}}</p>
        <figure class="grafico" data-grafico="resultado"></figure>
        <div class="resultados">
          <div class="resultado principal"><p class="rotulo">{{RESULTADO_1_ROTULO}}</p><p class="cifra" id="resultado1"></p></div>
          <div class="resultado"><p class="rotulo">{{RESULTADO_2_ROTULO}}</p><p class="cifra" id="resultado2"></p></div>
          <div class="resultado"><p class="rotulo">{{RESULTADO_3_ROTULO}}</p><p class="cifra" id="resultado3"></p></div>
        </div>
        <div class="tabla">
          <table>
            <caption>{{TITULO_DESGLOSE}}</caption>
            <thead>
              <tr><th>{{DESGLOSE_COLUMNA_1}}</th><th class="cifra">{{DESGLOSE_COLUMNA_2}}</th><th class="cifra">{{DESGLOSE_COLUMNA_3}}</th></tr>
            </thead>
            <tbody id="cuerpo-desglose"></tbody>
            <tfoot>
              <tr><td>{{DESGLOSE_TOTAL_ROTULO}}</td><td class="cifra" id="total-columna-2"></td><td class="cifra" id="total-columna-3"></td></tr>
            </tfoot>
          </table>
        </div>
        <div class="aviso">
          <span class="titulo">{{TITULO_SUPUESTOS}}</span>
          {{CONTENIDO_SUPUESTOS}}
        </div>
        <div class="aviso riesgo">
          <span class="titulo">{{TITULO_ADVERTENCIA}}</span>
          {{CONTENIDO_ADVERTENCIA}}
        </div>
      </section>
    </div>
  </div>
```

### Datos

```json maqueta=herramienta_interactiva parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {},
  "graficos": {
    "resultado": {"tipo": "medidor", "valor": 0, "maximo": 100, "tramos": [60, 85], "rotulo": "{{ROTULO_MEDIDOR}}", "tabla": false}
  }
}
```

### Script de calculo

Se coloca despues del script del motor. `UNIDAD` es la unidad de los resultados 1 y 2 y del desglose (`eur` por defecto; `dias`, `num` o cualquier texto si la herramienta calcula otra magnitud).

```js maqueta=herramienta_interactiva parte=script
<script>
(function(){
  "use strict";
  var UNIDAD = "eur", f = function(v, u){ return Reportes.fmt(v, u || UNIDAD); };
  var formulario = document.getElementById("formulario");

  function leer(){
    return {
      campo1: parseFloat(document.getElementById("campo1").value) || 0,
      campo2: parseFloat(document.getElementById("campo2").value) || 0,
      campo3: parseFloat(document.getElementById("campo3").value) || 0,
      campo4: document.getElementById("campo4").value
    };
  }

  function calcular(d){
    {{BLOQUE_CALCULO}}
  }

  function pintar(r){
    document.getElementById("resultado1").textContent = f(r.resultado1);
    document.getElementById("resultado2").textContent = f(r.resultado2);
    document.getElementById("resultado3").textContent = f(r.resultado3, "num");
    Reportes.actualizar("resultado", {valor: r.medidor || 0});
    var cuerpo = document.getElementById("cuerpo-desglose"), total = 0;
    cuerpo.textContent = "";
    r.desglose.forEach(function(fila){
      var tr = cuerpo.insertRow();
      [fila.concepto, f(fila.importe), fila.detalle].forEach(function(texto, i){
        var celda = tr.insertCell(); celda.textContent = texto; if (i) celda.className = "cifra";
      });
      total += fila.importe;
    });
    document.getElementById("total-columna-2").textContent = f(total);
    document.getElementById("total-columna-3").textContent = (r.totalDetalle === undefined) ? "" : r.totalDetalle;
  }

  function actualizar(){ pintar(calcular(leer())); }

  function progreso(){
    var casillas = document.querySelectorAll("#verificacion input[type=checkbox]");
    var hechos = document.querySelectorAll("#verificacion input:checked").length;
    document.getElementById("barra-progreso").style.width = (casillas.length ? Math.round(hechos * 100 / casillas.length) : 0) + "%";
    document.getElementById("texto-progreso").textContent = hechos + " de " + casillas.length + " puntos verificados";
  }

  formulario.addEventListener("input", actualizar);
  document.getElementById("verificacion").addEventListener("change", progreso);
  document.getElementById("reiniciar").addEventListener("click", function(){
    formulario.reset();
    document.querySelectorAll("#verificacion input[type=checkbox]").forEach(function(c){ c.checked = false; });
    actualizar(); progreso();
  });

  actualizar();
  progreso();
})();
</script>
```

El bloque de calculo recibe el objeto de `leer()` y devuelve `{resultado1, resultado2, resultado3, medidor, desglose: [{concepto, importe, detalle}]}`. `medidor` es un porcentaje de 0 a 100; `totalDetalle` es opcional, porque sumar dias o porcentajes carece de sentido.
