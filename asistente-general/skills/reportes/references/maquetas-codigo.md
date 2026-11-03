# Código de las maquetas (solo para el servidor)

Este archivo lo consume el servidor al montar un reporte con `create_file_from_skill_document` (`fragments` con selectores `maquetas-codigo.md#<id>/<parte>`); el modelo no lo lee. Las fichas de cada maqueta, con sus huecos y marcadores, están en `maquetas-reportes.md`.

## `panel_datos`

```html maqueta=panel_datos parte=ficha
<li><b>Periodo:</b> {{PERIODO}}</li>
      <li><b>Actualizado:</b> {{FECHA_ACTUALIZACION}}</li>
```

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

## `informe_visual`

```html maqueta=informe_visual parte=ficha
<li><b>Referencia:</b> {{REFERENCIA_EXPEDIENTE}}</li>
      <li><b>Fecha:</b> {{FECHA_EMISION}}</li>
      <li><b>Destinatario:</b> {{DESTINATARIO}}</li>
      <li><b>Preparado por:</b> {{AUTOR}}</li>
```

```css maqueta=informe_visual parte=estilos
.cronologia{list-style:none;margin:var(--e4) 0 0;padding:0 0 0 26px;border-left:2px solid var(--borde)}
.cronologia li{position:relative;margin:0 0 var(--e4)}
.cronologia li:last-child{margin-bottom:0}
.cronologia li::before{content:"";position:absolute;left:-33px;top:6px;width:12px;height:12px;border-radius:50%;
  background:var(--acento);border:3px solid var(--superficie);box-shadow:0 0 0 1px var(--borde)}
.cronologia .fecha{display:block;font-size:.76rem;letter-spacing:.07em;text-transform:uppercase;color:var(--apagado)}
.cronologia .hito{font-weight:650}
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
.firma{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:var(--e4);margin:var(--e4) 0 0;font-size:.9rem}
.firma div{border-top:1px solid var(--borde);padding-top:var(--e2);color:var(--apagado)}
@media (max-width:900px){.diseno{grid-template-columns:1fr}.indice{display:none}}
@media print{.diseno{display:block}.indice{display:none}}
```

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

## `herramienta_interactiva`

```html maqueta=herramienta_interactiva parte=ficha
<li><b>Referencia:</b> {{REFERENCIA_EXPEDIENTE}}</li>
```

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

```html maqueta=herramienta_interactiva parte=acciones
<button type="button" id="reiniciar">Restablecer valores</button>
```

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

## `presentacion`

```html maqueta=presentacion parte=ficha
<li><b>Diapositivas:</b> <span id="total-diapositivas"></span></li>
```

```css maqueta=presentacion parte=estilos
.contenedor>header,.pie>p:first-of-type{display:none}
.escenario{position:relative;width:100%;overflow:hidden;border-radius:var(--radio);box-shadow:var(--sombra);background:var(--superficie)}
.escenario:fullscreen{border-radius:0;background:#000}
.diapositivas{position:relative;width:1280px;height:720px;transform-origin:0 0}
.diapositiva{position:absolute;inset:0;padding:52px 72px 76px;background:var(--superficie);visibility:hidden;display:flex;flex-direction:column;overflow:hidden}
.diapositiva.activa{visibility:visible}
.diapositiva h2{font-size:40px;line-height:1.12;letter-spacing:-.02em;margin:0 0 28px;max-width:1040px}
.diapositiva p,.diapositiva li{font-size:22px;line-height:1.45}
.diapositiva .antetitulo{font-size:15px}
.diapositiva .pie-diapositiva{position:absolute;left:72px;right:72px;bottom:22px;display:flex;justify-content:space-between;font-size:13px;color:var(--apagado)}
.diapositiva .pie-diapositiva b{color:var(--aviso);letter-spacing:.06em}
.diapositiva .cuerpo{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center}
.diapositiva .grafico{--escala-grafico:1.5}
.diapositiva .grafico svg{width:100%;max-height:380px}
.diapositiva .barras .fila{font-size:19px}
.diapositiva .pista{height:14px}
.diapositiva .distintivo{font-size:14px;padding:4px 12px}
.diapositiva .fuente-grafico{font-size:13px}
.diapositiva .fuentes-reporte li{font-size:18px}
.diapositiva .datos-grafico{display:none}
.diapositiva .leyenda{font-size:16px}
.maqueta-portada{justify-content:center;background:linear-gradient(135deg,var(--acento-suave),var(--superficie) 62%)}
.maqueta-portada h2{font-size:64px;max-width:1000px}
.maqueta-portada .subtitulo{font-size:26px;color:var(--apagado);max-width:900px}
.maqueta-portada .firma-portada{margin-top:40px;font-size:18px;color:var(--apagado)}
.maqueta-separador{justify-content:center;background:var(--acento-fuerte)}
.maqueta-separador h2,.maqueta-separador p{color:#fff}
.maqueta-separador .numero{font-size:140px;font-weight:750;line-height:1;color:rgba(255,255,255,.28);margin:0}
.maqueta-separador .pie-diapositiva,.maqueta-separador .pie-diapositiva b{color:rgba(255,255,255,.75)}
.maqueta-cifra .numero:not(.delta-bien):not(.delta-mal){color:var(--acento)}
.maqueta-cifra .numero{font-size:128px;font-weight:720;letter-spacing:-.04em;line-height:1;margin:0 0 20px;font-variant-numeric:tabular-nums}
.lista-grande{margin:0;padding:0;list-style:none;counter-reset:punto}
.lista-grande li{position:relative;padding:14px 0 14px 64px;border-bottom:1px solid var(--borde-suave);counter-increment:punto}
.lista-grande li::before{content:counter(punto);position:absolute;left:0;top:12px;width:40px;height:40px;border-radius:50%;background:var(--acento-suave);color:var(--acento-fuerte);font-weight:700;font-size:18px;display:flex;align-items:center;justify-content:center}
.lado-a-lado{display:grid;grid-template-columns:repeat(auto-fit,minmax(0,1fr));gap:28px;align-items:start}
.lado-a-lado>div{background:var(--superficie-2);border:1px solid var(--borde);border-radius:var(--radio-s);padding:24px 28px}
.lado-a-lado h3{font-size:24px;margin:0 0 12px}
.lado-a-lado ul{padding-left:22px;margin:0}
.lado-a-lado .veredicto{margin-top:14px}
.lado-a-lado>.ok{border-top:5px solid var(--ok)}.lado-a-lado>.atencion{border-top:5px solid var(--aviso)}.lado-a-lado>.riesgo{border-top:5px solid var(--riesgo)}
.grafico-y-texto{display:grid;grid-template-columns:minmax(0,1.7fr) minmax(0,1fr);gap:36px;align-items:center}
.grafico-y-texto .conclusion{font-size:24px;font-weight:600;border-left:5px solid var(--acento);padding-left:20px}
.linea-tiempo{display:grid;grid-auto-flow:column;grid-auto-columns:1fr;gap:20px;margin-top:20px;border-top:3px solid var(--borde);padding-top:28px;position:relative}
.linea-tiempo>div{position:relative}
.linea-tiempo>div::before{content:"";position:absolute;top:-38px;left:0;width:18px;height:18px;border-radius:50%;background:var(--acento);border:4px solid var(--superficie)}
.linea-tiempo .fecha{font-size:15px;text-transform:uppercase;letter-spacing:.06em;color:var(--apagado)}
.linea-tiempo h3{font-size:21px;margin:6px 0}
.linea-tiempo p{font-size:17px;color:var(--apagado)}
.maqueta-cita{justify-content:center}
.maqueta-cita blockquote{margin:0;font-size:40px;line-height:1.3;font-weight:560;max-width:1000px;border-left:8px solid var(--acento);padding-left:36px}
.maqueta-cita .autor{margin:28px 0 0 44px;color:var(--apagado)}
.persona{text-align:center}
.persona .iniciales{width:96px;height:96px;margin:0 auto 14px;border-radius:50%;background:var(--acento-suave);color:var(--acento-fuerte);font-size:34px;font-weight:700;display:flex;align-items:center;justify-content:center}
.persona p{font-size:17px}
.pasos-tabla td,.pasos-tabla th{font-size:19px}
.diapositiva table{min-width:0}
.diapositiva td,.diapositiva th{font-size:18px;padding:12px 14px}
.controles{display:flex;flex-wrap:wrap;align-items:center;gap:var(--e3);margin:var(--e3) 0 0}
.controles .contador{font-variant-numeric:tabular-nums;color:var(--apagado);min-width:70px;text-align:center}
.panel-notas{margin:var(--e3) 0 0;padding:var(--e4);border:1px dashed var(--borde);border-radius:var(--radio-s);background:var(--superficie-2)}
.panel-notas[hidden]{display:none}
.panel-notas .reloj{float:right;font-variant-numeric:tabular-nums;color:var(--apagado)}
@media print{
  @page{size:338.67mm 190.5mm;margin:0;@bottom-right{content:none}}
  body{background:#fff}
  .borrador,.controles,.panel-notas,.pie{display:none}
  .escenario{box-shadow:none;border-radius:0;height:auto!important;overflow:visible}
  .diapositivas{transform:none!important;width:auto;height:auto}
  .diapositiva{position:relative;visibility:visible;width:1280px;height:720px;break-after:page;zoom:1}
  .diapositiva:last-child{break-after:auto}
}
```

```html maqueta=presentacion parte=contenido
<div class="escenario" id="escenario"><div class="diapositivas" id="diapositivas"></div></div>
  <div class="controles">
    <button type="button" id="anterior" aria-label="Diapositiva anterior">&larr;</button>
    <span class="contador" id="contador" aria-live="polite"></span>
    <button type="button" id="siguiente" aria-label="Diapositiva siguiente">&rarr;</button>
    <button type="button" id="completa">Pantalla completa</button>
    <button type="button" id="ver-notas">Notas</button>
  </div>
  <div class="panel-notas" id="panel-notas" hidden><span class="reloj" id="reloj">00:00</span><p id="texto-notas"></p></div>
```

```js maqueta=presentacion parte=script
<script>
(function(){
  "use strict";
  var R = Reportes, D = document, lista = R.datos.diapositivas || [], cont = D.getElementById("diapositivas");
  var titulo = D.title, actual = 0, inicio = Date.now();
  /* Los textos admiten {cifra:clave} (cifra enlazada al bloque de datos) y {icono:nombre} (modulo de iconos). */
  function el(tag, clase, padre, texto) {
    var n = R.html(tag, clase, padre);
    if (texto !== undefined) String(texto).split(/\{(cifra|icono):([\w-]+)\}/).forEach(function (trozo, i, partes) {
      if (i % 3 === 2) R.html("span", partes[i - 1] === "icono" ? "icono" : "", n).setAttribute("data-" + partes[i - 1], trozo);
      else if (i % 3 === 0 && trozo) n.appendChild(D.createTextNode(trozo));
    });
    return n;
  }
  function puntos(padre, items, clase) { var ul = el("ul", clase || "", padre); (items || []).forEach(function (p) { el("li", "", ul, p); }); return ul; }
  function figura(padre, nombre) { var f = el("figure", "grafico", padre); f.setAttribute("data-grafico", nombre); return f; }
  function columna(padre, c) { var d = el("div", c.estado || "", padre); el("h3", "", d, c.titulo || c.nombre || ""); if (c.texto) el("p", "", d, c.texto); if (c.puntos) puntos(d, c.puntos); if (c.veredicto) { var v = el("p", "veredicto", d); el("span", "distintivo " + (c.estado || ""), v, c.veredicto); } }
  var maquetas = {
    portada: function (s, d) { if (d.antetitulo) el("p", "antetitulo", s, d.antetitulo); el("h2", "", s, d.titulo); if (d.subtitulo) el("p", "subtitulo", s, d.subtitulo); el("p", "firma-portada", s, [d.autor, d.fecha].filter(Boolean).join(" · ")); },
    agenda: function (s, d, c) { puntos(c, d.puntos, "lista-grande"); },
    separador: function (s, d) { if (d.numero) el("p", "numero", s, d.numero); el("h2", "", s, d.titulo); if (d.texto) el("p", "", s, d.texto); },
    cifra: function (s, d, c) { var n = el("p", "numero", c, d.cifra || ""); if (d.dato) n.setAttribute("data-cifra", d.dato); el("h2", "", c, d.titulo); if (d.texto) el("p", "", c, d.texto); },
    /* Un diagrama necesita todo el ancho: su conclusion va debajo y no al lado. */
    grafico: function (s, d, c) { var diag = ((R.datos.graficos || {})[d.grafico] || {}).tipo === "diagrama", g = el("div", d.conclusion && !diag ? "grafico-y-texto" : "", c); figura(g, d.grafico); if (d.conclusion) el("p", "conclusion", g, d.conclusion); },
    puntos: function (s, d, c) { var g = el("div", d.grafico ? "grafico-y-texto" : "", c); puntos(g, d.puntos, "lista-grande"); if (d.grafico) figura(g, d.grafico); },
    dos_columnas: function (s, d, c) { var g = el("div", "lado-a-lado", c); columna(g, d.izquierda || {}); columna(g, d.derecha || {}); },
    comparativa: function (s, d, c) { var g = el("div", "lado-a-lado", c); (d.opciones || []).forEach(function (o) { columna(g, o); }); },
    cronologia: function (s, d, c) { var g = el("div", "linea-tiempo", c); (d.hitos || []).forEach(function (h) { var x = el("div", "", g); el("p", "fecha", x, h.fecha); el("h3", "", x, h.titulo); if (h.texto) el("p", "", x, h.texto); }); },
    tabla: function (s, d, c) { var t = el("table", "", el("div", "tabla", c)), f = el("tr", "", el("thead", "", t)); (d.cabecera || []).forEach(function (h) { el("th", "", f, h); }); var b = el("tbody", "", t); (d.filas || []).forEach(function (fila) { var tr = el("tr", "", b); fila.forEach(function (v) { el("td", /^[\d\s.,%€+\u2212-]+$/.test(String(v)) ? "cifra" : "", tr, v); }); }); if (d.nota) el("p", "subtitulo", c, d.nota); },
    cita: function (s, d) { el("blockquote", "", s, d.cita); if (d.autor) el("p", "autor", s, d.autor); },
    equipo: function (s, d, c) { var g = el("div", "lado-a-lado", c); (d.personas || []).forEach(function (p) { var x = el("div", "persona", g); el("div", "iniciales", x, p.nombre.split(/\s+/).map(function (w) { return w[0]; }).slice(0, 2).join("")); el("h3", "", x, p.nombre); el("p", "", x, p.cargo); if (p.texto) el("p", "", x, p.texto); }); },
    proximos_pasos: function (s, d, c) { var t = el("table", "pasos-tabla", el("div", "tabla", c)), b = el("tbody", "", t); (d.pasos || []).forEach(function (p, i) { var tr = el("tr", "", b); el("td", "", tr, (i + 1) + ". " + p.texto); el("td", "", tr, p.responsable || ""); el("td", "cifra", tr, p.fecha || ""); }); },
    cierre: function (s, d) { el("h2", "", s, d.titulo); if (d.texto) el("p", "", s, d.texto); if (d.contacto) el("p", "subtitulo", s, d.contacto); },
    fuentes: function (s, d, c) {
      c.appendChild(D.getElementById("fuentes-reporte"));
      var aviso = D.querySelector(".pie > p:last-of-type");  /* el aviso legal del pie tambien se imprime */
      if (aviso) el("p", "subtitulo", c, aviso.textContent);
    }
  };
  var todas = lista.concat([{maqueta: "fuentes", titulo: R.T.fuentes}]);
  todas.forEach(function (d, i) {
    var s = el("section", "diapositiva maqueta-" + d.maqueta, cont), c;
    s.setAttribute("aria-roledescription", "diapositiva");
    s.setAttribute("data-generado", "");  /* el motor la quita si el documento se guardo con ella */
    if (!maquetas[d.maqueta]) { console.error("Diapositiva " + (i + 1) + ": maqueta desconocida " + d.maqueta); el("p", "error-grafico", s, "Maqueta desconocida: " + d.maqueta); return; }
    c = ["portada", "separador", "cita", "cierre"].indexOf(d.maqueta) < 0 ? el("div", "cuerpo", null) : null;
    /* Una diapositiva con datos mal declarados muestra su error sin romper las demas. */
    if (c && d.maqueta !== "cifra") el("h2", "", s, d.titulo);
    try {
      maquetas[d.maqueta](s, d, c);
      if (d.aviso) el("div", "aviso", c || s, d.aviso);  /* aviso o supuestos en cualquier diapositiva */
      if (c) s.appendChild(c);
    }
    catch (e) { console.error("Diapositiva " + (i + 1) + ": " + e.message); el("p", "error-grafico", s, "Diapositiva " + (i + 1) + ": " + e.message); }
    var pie = el("div", "pie-diapositiva", s), izq = el("span", "", pie);
    el("b", "", izq, "DRAFT"); izq.appendChild(D.createTextNode(" · " + titulo));
    el("span", "", pie, (i + 1) + " / " + todas.length);
    s.notas = d.notas || "";
  });
  var diapos = [].slice.call(cont.children), escenario = D.getElementById("escenario");
  D.getElementById("total-diapositivas").textContent = diapos.length;
  function escalar() {
    var lleno = D.fullscreenElement === escenario;
    var w = lleno ? window.innerWidth : escenario.clientWidth, h = lleno ? window.innerHeight : Infinity;
    var e = Math.min(w / 1280, h / 720);
    /* A pantalla completa se centra a mano: el escalado parte de la esquina superior izquierda. */
    var dx = lleno ? (w - 1280 * e) / 2 : 0, dy = lleno ? (h - 720 * e) / 2 : 0;
    cont.style.transform = "translate(" + dx + "px," + dy + "px) scale(" + e + ")";
    escenario.style.height = lleno ? "" : Math.round(720 * e) + "px";
  }
  function ir(n) {
    actual = Math.max(0, Math.min(diapos.length - 1, n));
    diapos.forEach(function (s, i) { s.classList.toggle("activa", i === actual); s.setAttribute("aria-hidden", i !== actual); });
    D.getElementById("contador").textContent = (actual + 1) + " / " + diapos.length;
    D.getElementById("texto-notas").textContent = diapos[actual].notas || "—";
  }
  D.getElementById("anterior").addEventListener("click", function () { ir(actual - 1); });
  D.getElementById("siguiente").addEventListener("click", function () { ir(actual + 1); });
  D.getElementById("completa").addEventListener("click", function () { if (escenario.requestFullscreen) escenario.requestFullscreen(); });
  /* El reloj solo corre mientras las notas estan a la vista. */
  var reloj = null;
  function notas() {
    var p = D.getElementById("panel-notas"); p.hidden = !p.hidden;
    clearInterval(reloj);
    if (!p.hidden) reloj = setInterval(function () { var s = Math.floor((Date.now() - inicio) / 1000); D.getElementById("reloj").textContent = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0"); }, 1000);
  }
  D.getElementById("ver-notas").addEventListener("click", notas);
  D.addEventListener("keydown", function (e) {
    if (/INPUT|SELECT|TEXTAREA/.test(e.target.tagName) || e.ctrlKey || e.metaKey || e.altKey) return;
    if (["ArrowRight", "PageDown", " "].indexOf(e.key) > -1) { e.preventDefault(); ir(actual + 1); }
    else if (["ArrowLeft", "PageUp"].indexOf(e.key) > -1) { e.preventDefault(); ir(actual - 1); }
    else if (e.key === "Home") ir(0);
    else if (e.key === "End") ir(diapos.length - 1);
    else if (e.key === "n" || e.key === "N") notas();
    else if (e.key === "f" || e.key === "F") D.getElementById("completa").click();
  });
  var x0 = null;
  escenario.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, {passive: true});
  escenario.addEventListener("touchend", function (e) { if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) ir(actual + (dx < 0 ? 1 : -1)); x0 = null; });
  window.addEventListener("resize", escalar);
  D.addEventListener("fullscreenchange", escalar);
  escalar();
  ir(0);
})();
</script>
```

## `documento_largo`

```html maqueta=documento_largo parte=ficha
<li><b>Autor:</b> {{AUTOR}}</li>
      <li><b>Fecha:</b> {{FECHA_EMISION}}</li>
```

```css maqueta=documento_largo parte=estilos
.cronologia{list-style:none;margin:var(--e4) 0 0;padding:0 0 0 26px;border-left:2px solid var(--borde)}
.cronologia li{position:relative;margin:0 0 var(--e4)}
.cronologia li:last-child{margin-bottom:0}
.cronologia li::before{content:"";position:absolute;left:-33px;top:6px;width:12px;height:12px;border-radius:50%;
  background:var(--acento);border:3px solid var(--superficie);box-shadow:0 0 0 1px var(--borde)}
.cronologia .fecha{display:block;font-size:.76rem;letter-spacing:.07em;text-transform:uppercase;color:var(--apagado)}
.cronologia .hito{font-weight:650}
.contenedor>header{min-height:88vh;display:flex;flex-direction:column;justify-content:center;padding:var(--e6) var(--e5);margin:0 0 var(--e5);border-radius:var(--radio);color:#fff;
  background:linear-gradient(150deg,var(--acento-fuerte),color-mix(in srgb,var(--acento) 70%,#000))}
.contenedor>header .antetitulo,.contenedor>header .ficha,.contenedor>header .ficha b{color:rgba(255,255,255,.85)}
.contenedor>header h1{font-size:clamp(2.2rem,5vw,3.4rem);color:#fff;max-width:18ch}
.contenedor>header .entradilla{color:rgba(255,255,255,.88);font-size:1.2rem}
.contenedor>header .ficha{margin-top:auto;padding-top:var(--e6)}
.resumen-ejecutivo{border-top:5px solid var(--acento)}
.resumen-ejecutivo ol{margin:0;padding-left:22px}
.resumen-ejecutivo li{margin:0 0 var(--e2);font-size:1.02rem}
.indice-documento{margin:0 0 var(--e5)}
.indice-documento li::marker{color:var(--acento);font-weight:650}
.indice-documento a{display:block;padding:7px 0;color:var(--texto);text-decoration:none;border-bottom:1px dotted var(--borde)}
main{counter-reset:capitulo}
.capitulo{margin:0 0 var(--e6)}
.capitulo>h2{font-size:clamp(1.4rem,2.6vw,1.8rem);counter-increment:capitulo;border-bottom:2px solid var(--acento);padding-bottom:var(--e2);margin:0 0 var(--e4)}
.capitulo>h2::before{content:counter(capitulo) ". ";color:var(--acento)}
.capitulo h3{font-size:1.12rem;margin:var(--e4) 0 var(--e2)}
.capitulo p,.capitulo li{font-size:1.02rem;line-height:1.7}
.capitulo .grafico{margin:var(--e3) 0 var(--e4)}
.destacado{font-size:1.25rem;line-height:1.45;font-weight:600;border-left:5px solid var(--acento);padding:var(--e2) 0 var(--e2) var(--e4);margin:var(--e5) 0}
sup.nota{color:var(--acento);font-weight:650}
.notas-documento li{font-size:.88rem;color:var(--apagado)}
@media print{
  @page{margin:20mm 18mm 22mm;@bottom-left{content:"DRAFT";font-size:8pt;color:#a8650f;font-weight:600}}
  @page :first{margin:0;@bottom-right{content:none}@bottom-left{content:none}@top-left{content:none}}
  main{position:relative}
  /* El aviso DRAFT va impreso sobre la portada, para que tambien conste en navegadores sin cajas de margen. */
  .borrador{position:absolute;top:12mm;left:18mm;right:18mm;z-index:1;margin:0;background:rgba(255,255,255,.92)}
  .contenedor>header{min-height:0;height:297mm;margin:0;border-radius:0;break-after:page;padding:40mm 24mm 24mm}
  .resumen-ejecutivo{break-inside:avoid}
  .indice-documento{break-after:page}
  .capitulo.nueva-pagina{break-before:page}
  .capitulo p,.capitulo li{font-size:10.5pt;line-height:1.55}
}
```

```html maqueta=documento_largo parte=contenido
<section class="tarjeta resumen-ejecutivo">
    <h2>{{TITULO_RESUMEN}}</h2>
    <ol>
      <li>{{CONCLUSION_1}}</li>
      <li>{{CONCLUSION_2}}</li>
      <li>{{CONCLUSION_3}}</li>
    </ol>
  </section>

  <nav class="indice-documento" aria-label="Indice">
    <h2>{{TITULO_INDICE}}</h2>
    <ol id="indice-documento"></ol>
  </nav>

  <section class="capitulo" id="capitulo-1">
    <h2>{{TITULO_CAPITULO_1}}</h2>
    <p>{{TEXTO_CAPITULO_1}}</p>
    <p class="destacado">{{IDEA_DESTACADA_1}}</p>
  </section>

  <section class="capitulo nueva-pagina" id="capitulo-2">
    <h2>{{TITULO_CAPITULO_2}}</h2>
    <p>{{TEXTO_CAPITULO_2}}</p>
    <figure class="grafico" data-grafico="figura_1"></figure>
    <p>{{TEXTO_CAPITULO_2_CONTINUACION}}</p>
  </section>

  <section class="capitulo nueva-pagina" id="capitulo-3">
    <h2>{{TITULO_CAPITULO_3}}</h2>
    <p>{{TEXTO_CAPITULO_3}}</p>
    <h3>{{SUBTITULO_CAPITULO_3}}</h3>
    <ul>
      <li>{{PUNTO_1}}</li>
      <li>{{PUNTO_2}}</li>
    </ul>
  </section>

  <section class="capitulo nueva-pagina" id="notas">
    <h2>{{TITULO_NOTAS}}</h2>
    <ol class="notas-documento">
      <li>{{NOTA_1}}</li>
    </ol>
  </section>
```

```js maqueta=documento_largo parte=script
<script>
(function(){
  "use strict";
  var D = document, indice = D.getElementById("indice-documento");
  [].forEach.call(D.querySelectorAll(".capitulo"), function (cap, i) {
    var h = cap.querySelector("h2");
    if (!h) return;  /* un capitulo sin titular no entra en el indice */
    if (!cap.id) cap.id = "capitulo-" + (i + 1);
    var li = Reportes.html("li", "", indice), a = Reportes.html("a", "", li, h.textContent);
    li.setAttribute("data-generado", "");  /* el motor la quita si el documento se guardo con ella */
    a.href = "#" + cap.id;
  });
  /* Cabecera de pagina impresa con el titulo corto (desde la segunda pagina). */
  var estilo = D.createElement("style");
  estilo.setAttribute("data-generado", "");
  estilo.textContent = "@media print{@page{@top-left{content:" + JSON.stringify(D.title) + ";font-size:8.5pt;color:#555}}}";
  D.head.appendChild(estilo);
})();
</script>
```

## `resumen_ejecutivo`

```html maqueta=resumen_ejecutivo parte=ficha
<li><b>Para:</b> {{DESTINATARIO}}</li>
      <li><b>Fecha:</b> {{FECHA_EMISION}}</li>
```

```css maqueta=resumen_ejecutivo parte=estilos
:root{--encaje:703 1000}  /* ancho y alto utiles de la hoja, en px: lo lee el modulo encaje */
.una-pagina{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:var(--e4);align-items:start}
.una-pagina .conclusiones ol{margin:0;padding-left:20px}
.una-pagina .conclusiones li{margin:0 0 var(--e3);font-size:.98rem}
.decision{font-weight:600}
@media screen and (max-width:760px){.una-pagina{grid-template-columns:1fr}}
@media print{
  @page{margin:12mm 12mm 14mm}
  .contenedor{font-size:9.5pt}
  .una-pagina{gap:var(--e3)}
  .indicadores{grid-template-columns:repeat(3,1fr);gap:var(--e2);margin-bottom:var(--e3)}
  .indicador{padding:var(--e2) var(--e3)}
  .indicador .cifra{font-size:17pt}
  .una-pagina svg{max-height:62mm}
  .borrador{margin-bottom:var(--e2)}
  .fuente-grafico{display:none}
  .pie{margin-top:var(--e3);padding-top:var(--e2);font-size:7.5pt}
  .pie p{margin:0 0 2px}
}
```

```html maqueta=resumen_ejecutivo parte=contenido
<div class="indicadores">
    <div class="indicador"><p class="rotulo">{{INDICADOR_1_ROTULO}}</p><p class="cifra" data-cifra="indicador_1"></p><p class="detalle">{{INDICADOR_1_DETALLE}}</p></div>
    <div class="indicador"><p class="rotulo">{{INDICADOR_2_ROTULO}}</p><p class="cifra" data-cifra="indicador_2"></p><p class="detalle">{{INDICADOR_2_DETALLE}}</p></div>
    <div class="indicador"><p class="rotulo">{{INDICADOR_3_ROTULO}}</p><p class="cifra" data-cifra="indicador_3"></p><p class="detalle">{{INDICADOR_3_DETALLE}}</p></div>
  </div>
  <div class="una-pagina">
    <section class="tarjeta">
      <h2>{{TITULO_GRAFICO}}</h2>
      <figure class="grafico" data-grafico="principal"></figure>
    </section>
    <section class="tarjeta conclusiones">
      <h2>{{TITULO_CONCLUSIONES}}</h2>
      <ol>
        <li>{{CONCLUSION_1}}</li>
        <li>{{CONCLUSION_2}}</li>
        <li>{{CONCLUSION_3}}</li>
      </ol>
      <p class="aviso decision">{{DECISION_QUE_SE_PIDE}}</p>
    </section>
  </div>
```

## `cuadro_mando`

```html maqueta=cuadro_mando parte=ficha
<li><b>Periodo:</b> {{PERIODO}}</li>
      <li><b>Actualizado:</b> {{FECHA_ACTUALIZACION}}</li>
```

```css maqueta=cuadro_mando parte=estilos
.contenedor>.indicadores{grid-template-columns:repeat(4,minmax(0,1fr))}
.contenedor>.indicadores .indicador .cifra{font-size:clamp(1.3rem,1.9vw,1.85rem)}
table.compacta th,table.compacta td{padding:7px 10px}
@media (max-width:900px){.contenedor>.indicadores{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media print{.contenedor>.indicadores{grid-template-columns:repeat(4,1fr)}}
```

```html maqueta=cuadro_mando parte=contenido
<div class="indicadores">
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_1_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_1"></p>
      <p class="detalle"><span data-cifra="variacion_1"></span> {{INDICADOR_1_DETALLE}}</p>
      <div class="tendencia" data-grafico="tendencia_1"></div>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_2_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_2"></p>
      <p class="detalle"><span data-cifra="variacion_2"></span> {{INDICADOR_2_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_3_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_3"></p>
      <p class="detalle"><span data-cifra="variacion_3"></span> {{INDICADOR_3_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_4_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_4"></p>
      <p class="detalle"><span data-cifra="variacion_4"></span> {{INDICADOR_4_DETALLE}}</p>
    </div>
  </div>
  <div class="indicadores">
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_5_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_5"></p>
      <p class="detalle">{{INDICADOR_5_DETALLE}}</p>
      <div class="tendencia" data-grafico="tendencia_5"></div>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_6_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_6"></p>
      <p class="detalle">{{INDICADOR_6_DETALLE}}</p>
    </div>
    <div class="indicador aparece es-atencion">
      <p class="rotulo">{{INDICADOR_7_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_7"></p>
      <p class="detalle">{{INDICADOR_7_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_8_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_8"></p>
      <p class="detalle">{{INDICADOR_8_DETALLE}}</p>
    </div>
  </div>

  <div class="malla tres">
    <section class="tarjeta">
      <h2>{{TITULO_OBJETIVOS}}</h2>
      <p class="subtitulo">{{SUBTITULO_OBJETIVOS}}</p>
      <figure class="grafico" data-grafico="objetivos"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_CUMPLIMIENTO}}</h2>
      <p class="subtitulo">{{SUBTITULO_CUMPLIMIENTO}}</p>
      <figure class="grafico" data-grafico="cumplimiento"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_ESTADO}}</h2>
      <p class="subtitulo">{{SUBTITULO_ESTADO}}</p>
      <figure class="grafico" data-grafico="estado"></figure>
    </section>
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_TABLA}}</h2>
      <p class="subtitulo">{{SUBTITULO_TABLA}}</p>
      <div class="tabla">
        <table class="compacta">
          <thead><tr><th>{{COLUMNA_1}}</th><th class="cifra">{{COLUMNA_2}}</th><th class="cifra">{{COLUMNA_3}}</th><th class="cifra">{{COLUMNA_4}}</th></tr></thead>
          <tbody>
            <tr><td>{{FILA_1_C1}}</td><td class="cifra">{{FILA_1_C2}}</td><td class="cifra">{{FILA_1_C3}}</td><td class="cifra">{{FILA_1_C4}}</td></tr>
            <tr><td>{{FILA_2_C1}}</td><td class="cifra">{{FILA_2_C2}}</td><td class="cifra">{{FILA_2_C3}}</td><td class="cifra">{{FILA_2_C4}}</td></tr>
            <tr><td>{{FILA_3_C1}}</td><td class="cifra">{{FILA_3_C2}}</td><td class="cifra">{{FILA_3_C3}}</td><td class="cifra">{{FILA_3_C4}}</td></tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
```

## `ficha_una_pagina`

```html maqueta=ficha_una_pagina parte=ficha
<li><b>Referencia:</b> {{REFERENCIA}}</li>
      <li><b>Fecha:</b> {{FECHA_EMISION}}</li>
```

```css maqueta=ficha_una_pagina parte=estilos
:root{--encaje:703 1000}  /* ancho y alto utiles de la hoja, en px: lo lee el modulo encaje */
.datos-clave{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;margin:0 0 var(--e4);border:1px solid var(--borde);border-radius:var(--radio-s);overflow:hidden;background:var(--superficie)}
.datos-clave div{padding:var(--e3) var(--e4);border-right:1px solid var(--borde-suave);border-bottom:1px solid var(--borde-suave)}
.datos-clave div:nth-child(3n){border-right:0}
.datos-clave div:nth-last-child(-n+3){border-bottom:0}
.datos-clave dt{font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;color:var(--apagado);margin:0 0 2px}
.datos-clave dd{margin:0;font-weight:620}
.una-pagina{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:var(--e4);align-items:start}
@media screen and (max-width:760px){.datos-clave{grid-template-columns:1fr 1fr}.una-pagina{grid-template-columns:1fr}}
@media print{
  @page{margin:12mm 12mm 14mm}
  .contenedor{font-size:9.5pt}
  .indicadores{grid-template-columns:repeat(3,1fr);gap:var(--e2);margin-bottom:var(--e3)}
  .indicador{padding:var(--e2) var(--e3)}
  .indicador .cifra{font-size:17pt}
  .una-pagina svg{max-height:62mm}
  .fuente-grafico{display:none}
  .pie{margin-top:var(--e3);padding-top:var(--e2);font-size:7.5pt}
}
```

```html maqueta=ficha_una_pagina parte=contenido
<dl class="datos-clave">
    <div><dt>{{DATO_1_ROTULO}}</dt><dd>{{DATO_1_VALOR}}</dd></div>
    <div><dt>{{DATO_2_ROTULO}}</dt><dd>{{DATO_2_VALOR}}</dd></div>
    <div><dt>{{DATO_3_ROTULO}}</dt><dd>{{DATO_3_VALOR}}</dd></div>
    <div><dt>{{DATO_4_ROTULO}}</dt><dd>{{DATO_4_VALOR}}</dd></div>
    <div><dt>{{DATO_5_ROTULO}}</dt><dd>{{DATO_5_VALOR}}</dd></div>
    <div><dt>{{DATO_6_ROTULO}}</dt><dd>{{DATO_6_VALOR}}</dd></div>
  </dl>
  <div class="indicadores">
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_1_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_1"></p>
      <p class="detalle">{{INDICADOR_1_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_2_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_2"></p>
      <p class="detalle">{{INDICADOR_2_DETALLE}}</p>
    </div>
    <div class="indicador aparece es-atencion">
      <p class="rotulo">{{INDICADOR_3_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_3"></p>
      <p class="detalle">{{INDICADOR_3_DETALLE}}</p>
    </div>
  </div>
  <div class="una-pagina">
    <section class="tarjeta">
      <h2>{{TITULO_GRAFICO}}</h2>
      <p class="subtitulo">{{SUBTITULO_GRAFICO}}</p>
      <figure class="grafico" data-grafico="principal"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_ESTADO}}</h2>
      <p class="subtitulo">{{SUBTITULO_ESTADO}}</p>
      <figure class="grafico" data-grafico="estado"></figure>
    </section>
  </div>
```

## `infografia`

```html maqueta=infografia parte=ficha
<li><b>Fuente:</b> {{FUENTE_BREVE}}</li>
```

```css maqueta=infografia parte=estilos
header{text-align:center}
.entradilla{margin-left:auto;margin-right:auto}
.ficha{justify-content:center}
.bloque-info{text-align:center;padding:var(--e5) var(--e4);border-radius:var(--radio);margin:0 0 var(--e3);background:var(--superficie);border:1px solid var(--borde)}
.bloque-info h2{margin-bottom:var(--e3)}
.bloque-info.invertido{background:var(--acento);border-color:var(--acento);color:var(--superficie)}
.cifra-grande{font-size:clamp(3rem,10vw,5.2rem);font-weight:760;letter-spacing:-.04em;line-height:1;margin:0 0 var(--e3);color:var(--acento);font-variant-numeric:tabular-nums}
.invertido .cifra-grande{color:var(--superficie)}
.frase{font-size:1.15rem;max-width:34ch;margin:0 auto}
.bloque-info .leyenda{justify-content:center}
@media print{.bloque-info{break-inside:avoid;padding:var(--e4)}.cifra-grande{font-size:40pt}}
```

```html maqueta=infografia parte=contenido
<section class="bloque-info">
    <p class="cifra-grande" data-cifra="cifra_1"></p>
    <p class="frase">{{FRASE_1}}</p>
  </section>
  <section class="bloque-info">
    <h2>{{TITULO_PROPORCION}}</h2>
    <figure class="grafico" data-grafico="proporcion"></figure>
  </section>
  <section class="bloque-info invertido">
    <p class="cifra-grande" data-cifra="cifra_2"></p>
    <p class="frase">{{FRASE_2}}</p>
  </section>
  <section class="bloque-info">
    <h2>{{TITULO_AVANCE}}</h2>
    <figure class="grafico" data-grafico="avance"></figure>
  </section>
  <section class="bloque-info">
    <h2>{{TITULO_HITOS}}</h2>
    <figure class="grafico" data-grafico="hitos"></figure>
  </section>
  <section class="bloque-info invertido">
    <p class="cifra-grande" data-cifra="cifra_3"></p>
    <p class="frase">{{FRASE_3}}</p>
  </section>
```

## `comparativa`

```html maqueta=comparativa parte=ficha
<li><b>Referencia:</b> {{REFERENCIA}}</li>
      <li><b>Fecha:</b> {{FECHA_EMISION}}</li>
```

```css maqueta=comparativa parte=estilos
.recomendacion{margin:0 0 var(--e4)}
.opciones{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:var(--e3);margin:0 0 var(--e3)}
.opcion dl{margin:var(--e3) 0 0}
.opcion dl div{display:flex;justify-content:space-between;gap:var(--e3);padding:8px 0;border-top:1px solid var(--borde-suave);font-size:.9rem}
.opcion dt{color:var(--apagado)}
.opcion dd{margin:0;font-weight:620;text-align:right}
.opcion .veredicto{margin:0 0 var(--e2)}
.opcion.ganadora{border:2px solid var(--ok);box-shadow:0 0 0 4px color-mix(in srgb,var(--ok) 14%,transparent),var(--sombra)}
@media print{.opciones{grid-template-columns:repeat(3,1fr)}.opcion{break-inside:avoid}}
```

```html maqueta=comparativa parte=contenido
<div class="aviso favorable recomendacion"><span class="titulo">{{TITULO_RECOMENDACION}}</span>{{RECOMENDACION}}</div>
  <div class="opciones">
    <section class="tarjeta opcion ganadora">
      <p class="veredicto"><span class="distintivo ok">{{OPCION_1_VEREDICTO}}</span></p>
      <h2>{{OPCION_1_NOMBRE}}</h2>
      <dl>
        <div><dt>{{CRITERIO_1}}</dt><dd>{{OPCION_1_C1}}</dd></div>
        <div><dt>{{CRITERIO_2}}</dt><dd>{{OPCION_1_C2}}</dd></div>
        <div><dt>{{CRITERIO_3}}</dt><dd>{{OPCION_1_C3}}</dd></div>
        <div><dt>{{CRITERIO_4}}</dt><dd>{{OPCION_1_C4}}</dd></div>
      </dl>
    </section>
    <section class="tarjeta opcion">
      <p class="veredicto"><span class="distintivo ">{{OPCION_2_VEREDICTO}}</span></p>
      <h2>{{OPCION_2_NOMBRE}}</h2>
      <dl>
        <div><dt>{{CRITERIO_1}}</dt><dd>{{OPCION_2_C1}}</dd></div>
        <div><dt>{{CRITERIO_2}}</dt><dd>{{OPCION_2_C2}}</dd></div>
        <div><dt>{{CRITERIO_3}}</dt><dd>{{OPCION_2_C3}}</dd></div>
        <div><dt>{{CRITERIO_4}}</dt><dd>{{OPCION_2_C4}}</dd></div>
      </dl>
    </section>
    <section class="tarjeta opcion">
      <p class="veredicto"><span class="distintivo ">{{OPCION_3_VEREDICTO}}</span></p>
      <h2>{{OPCION_3_NOMBRE}}</h2>
      <dl>
        <div><dt>{{CRITERIO_1}}</dt><dd>{{OPCION_3_C1}}</dd></div>
        <div><dt>{{CRITERIO_2}}</dt><dd>{{OPCION_3_C2}}</dd></div>
        <div><dt>{{CRITERIO_3}}</dt><dd>{{OPCION_3_C3}}</dd></div>
        <div><dt>{{CRITERIO_4}}</dt><dd>{{OPCION_3_C4}}</dd></div>
      </dl>
    </section>
  </div>
  <div class="malla dos">
    <section class="tarjeta">
      <h2>{{TITULO_PERFIL}}</h2>
      <p class="subtitulo">{{SUBTITULO_PERFIL}}</p>
      <figure class="grafico" data-grafico="perfil"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_DISTANCIA}}</h2>
      <p class="subtitulo">{{SUBTITULO_DISTANCIA}}</p>
      <figure class="grafico" data-grafico="distancia"></figure>
    </section>
  </div>
```

## `cronograma_expediente`

```html maqueta=cronograma_expediente parte=ficha
<li><b>Referencia:</b> {{REFERENCIA}}</li>
      <li><b>Fecha:</b> {{FECHA_EMISION}}</li>
```

```css maqueta=cronograma_expediente parte=estilos
.contenedor>.aviso{margin:0 0 var(--e3)}
.pasos{list-style:none;counter-reset:paso;padding:0;margin:0}
.pasos li{counter-increment:paso;display:grid;grid-template-columns:28px 1fr;column-gap:var(--e2);padding:10px 0;border-bottom:1px solid var(--borde-suave)}
.pasos li::before{content:counter(paso);grid-row:span 2;width:24px;height:24px;border-radius:50%;background:var(--acento);color:var(--superficie);font-size:.78rem;font-weight:700;display:grid;place-items:center}
.pasos span{font-size:.82rem;color:var(--apagado)}
```

```html maqueta=cronograma_expediente parte=contenido
<div class="indicadores">
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_1_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_1_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_1_DETALLE}}</p>
    </div>
    <div class="indicador aparece es-atencion">
      <p class="rotulo">{{INDICADOR_2_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_2_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_2_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_3_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_3_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_3_DETALLE}}</p>
    </div>
  </div>
  <div class="aviso riesgo"><span class="titulo">{{TITULO_AVISO}}</span>{{AVISO_PLAZO}}</div>
  <div class="malla dos">
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_HITOS}}</h2>
      <p class="subtitulo">{{SUBTITULO_HITOS}}</p>
      <figure class="grafico" data-grafico="hitos"></figure>
    </section>
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_PLAZOS}}</h2>
      <p class="subtitulo">{{SUBTITULO_PLAZOS}}</p>
      <figure class="grafico" data-grafico="plazos"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_FASES}}</h2>
      <p class="subtitulo">{{SUBTITULO_FASES}}</p>
      <figure class="grafico" data-grafico="fases"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_PASOS}}</h2>
      <p class="subtitulo">{{SUBTITULO_PASOS}}</p>
      <ol class="pasos">
        <li><b>{{PASO_1}}</b><span>{{RESPONSABLE_1}} · {{FECHA_PASO_1}}</span></li>
        <li><b>{{PASO_2}}</b><span>{{RESPONSABLE_2}} · {{FECHA_PASO_2}}</span></li>
        <li><b>{{PASO_3}}</b><span>{{RESPONSABLE_3}} · {{FECHA_PASO_3}}</span></li>
      </ol>
    </section>
  </div>
```

## `lista_control`

```html maqueta=lista_control parte=ficha
<li><b>Referencia:</b> {{REFERENCIA}}</li>
      <li><b>Fecha:</b> {{FECHA_EMISION}}</li>
```

```css maqueta=lista_control parte=estilos
.tabla td:last-child{white-space:nowrap}
```

```html maqueta=lista_control parte=contenido
<div class="indicadores">
    <div class="indicador aparece es-ok">
      <p class="rotulo">{{INDICADOR_1_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_1"></p>
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
  <div class="malla dos">
    <section class="tarjeta">
      <h2>{{TITULO_BLOQUES}}</h2>
      <p class="subtitulo">{{SUBTITULO_BLOQUES}}</p>
      <figure class="grafico" data-grafico="bloques"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_REQUISITOS}}</h2>
      <p class="subtitulo">{{SUBTITULO_REQUISITOS}}</p>
      <figure class="grafico" data-grafico="requisitos"></figure>
    </section>
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_TABLA}}</h2>
      <p class="subtitulo">{{SUBTITULO_TABLA}}</p>
      <div class="tabla">
        <table>
          <thead><tr><th>{{COLUMNA_1}}</th><th>{{COLUMNA_2}}</th><th>{{COLUMNA_3}}</th></tr></thead>
          <tbody>
            <tr><td>{{FILA_1_REQUISITO}}</td><td>{{FILA_1_EVIDENCIA}}</td><td><span class="distintivo {{FILA_1_CLASE}}">{{FILA_1_ESTADO}}</span></td></tr>
            <tr><td>{{FILA_2_REQUISITO}}</td><td>{{FILA_2_EVIDENCIA}}</td><td><span class="distintivo {{FILA_2_CLASE}}">{{FILA_2_ESTADO}}</span></td></tr>
            <tr><td>{{FILA_3_REQUISITO}}</td><td>{{FILA_3_EVIDENCIA}}</td><td><span class="distintivo {{FILA_3_CLASE}}">{{FILA_3_ESTADO}}</span></td></tr>
            <tr><td>{{FILA_4_REQUISITO}}</td><td>{{FILA_4_EVIDENCIA}}</td><td><span class="distintivo {{FILA_4_CLASE}}">{{FILA_4_ESTADO}}</span></td></tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
```

## `mapa_riesgos`

```html maqueta=mapa_riesgos parte=ficha
<li><b>Referencia:</b> {{REFERENCIA}}</li>
      <li><b>Fecha:</b> {{FECHA_EMISION}}</li>
```

```html maqueta=mapa_riesgos parte=contenido
<div class="indicadores">
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_1_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_1_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_1_DETALLE}}</p>
    </div>
    <div class="indicador aparece es-riesgo">
      <p class="rotulo">{{INDICADOR_2_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_2_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_2_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_3_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_3"></p>
      <p class="detalle">{{INDICADOR_3_DETALLE}}</p>
    </div>
  </div>
  <div class="malla dos">
    <section class="tarjeta">
      <h2>{{TITULO_MATRIZ}}</h2>
      <p class="subtitulo">{{SUBTITULO_MATRIZ}}</p>
      <figure class="grafico" data-grafico="matriz"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_MEDIDAS}}</h2>
      <p class="subtitulo">{{SUBTITULO_MEDIDAS}}</p>
      <figure class="grafico" data-grafico="medidas"></figure>
    </section>
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_IMPACTO}}</h2>
      <p class="subtitulo">{{SUBTITULO_IMPACTO}}</p>
      <figure class="grafico" data-grafico="impacto"></figure>
    </section>
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_EXPOSICION}}</h2>
      <p class="subtitulo">{{SUBTITULO_EXPOSICION}}</p>
      <figure class="grafico" data-grafico="exposicion"></figure>
    </section>
  </div>
```

## `escenarios`

```html maqueta=escenarios parte=ficha
<li><b>Referencia:</b> {{REFERENCIA}}</li>
      <li><b>Fecha:</b> {{FECHA_EMISION}}</li>
```

```html maqueta=escenarios parte=contenido
<div class="indicadores">
    <div class="indicador aparece es-ok">
      <p class="rotulo">{{INDICADOR_1_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_1"></p>
      <p class="detalle">{{INDICADOR_1_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_2_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_2"></p>
      <p class="detalle">{{INDICADOR_2_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_3_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_3"></p>
      <p class="detalle">{{INDICADOR_3_DETALLE}}</p>
    </div>
  </div>
  <div class="malla dos">
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_SUPUESTOS}}</h2>
      <p class="subtitulo">{{SUBTITULO_SUPUESTOS}}</p>
      <div class="tabla">
        <table>
          <thead><tr><th>{{COLUMNA_1}}</th><th class="cifra">{{COLUMNA_2}}</th><th class="cifra">{{COLUMNA_3}}</th><th class="cifra">{{COLUMNA_4}}</th></tr></thead>
          <tbody>
            <tr><td>{{FILA_1_C1}}</td><td class="cifra">{{FILA_1_C2}}</td><td class="cifra">{{FILA_1_C3}}</td><td class="cifra">{{FILA_1_C4}}</td></tr>
            <tr><td>{{FILA_2_C1}}</td><td class="cifra">{{FILA_2_C2}}</td><td class="cifra">{{FILA_2_C3}}</td><td class="cifra">{{FILA_2_C4}}</td></tr>
            <tr><td>{{FILA_3_C1}}</td><td class="cifra">{{FILA_3_C2}}</td><td class="cifra">{{FILA_3_C3}}</td><td class="cifra">{{FILA_3_C4}}</td></tr>
          </tbody>
        </table>
      </div>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_POR_ESCENARIO}}</h2>
      <p class="subtitulo">{{SUBTITULO_POR_ESCENARIO}}</p>
      <figure class="grafico" data-grafico="por_escenario"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_SENSIBILIDAD}}</h2>
      <p class="subtitulo">{{SUBTITULO_SENSIBILIDAD}}</p>
      <figure class="grafico" data-grafico="sensibilidad"></figure>
    </section>
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_HORQUILLA}}</h2>
      <p class="subtitulo">{{SUBTITULO_HORQUILLA}}</p>
      <figure class="grafico" data-grafico="horquilla"></figure>
    </section>
  </div>
```

## `embudo_conversion`

```html maqueta=embudo_conversion parte=ficha
<li><b>Periodo:</b> {{PERIODO}}</li>
      <li><b>Actualizado:</b> {{FECHA_ACTUALIZACION}}</li>
```

```html maqueta=embudo_conversion parte=contenido
<div class="indicadores">
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_1_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_1"></p>
      <p class="detalle">{{INDICADOR_1_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_2_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_2"></p>
      <p class="detalle"><span data-cifra="variacion_2"></span> {{INDICADOR_2_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_3_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_3"></p>
      <p class="detalle">{{INDICADOR_3_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_4_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_4_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_4_DETALLE}}</p>
    </div>
  </div>
  <div class="malla dos">
    <section class="tarjeta">
      <h2>{{TITULO_EMBUDO}}</h2>
      <p class="subtitulo">{{SUBTITULO_EMBUDO}}</p>
      <figure class="grafico" data-grafico="embudo"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_EVOLUCION}}</h2>
      <p class="subtitulo">{{SUBTITULO_EVOLUCION}}</p>
      <figure class="grafico" data-grafico="evolucion"></figure>
    </section>
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_FLUJOS}}</h2>
      <p class="subtitulo">{{SUBTITULO_FLUJOS}}</p>
      <figure class="grafico" data-grafico="flujos"></figure>
    </section>
  </div>
```

## `actividad_equipo`

```html maqueta=actividad_equipo parte=ficha
<li><b>Periodo:</b> {{PERIODO}}</li>
      <li><b>Actualizado:</b> {{FECHA_ACTUALIZACION}}</li>
```

```html maqueta=actividad_equipo parte=contenido
<div class="indicadores">
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_1_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_1"></p>
      <p class="detalle">{{INDICADOR_1_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_2_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_2"></p>
      <p class="detalle">{{INDICADOR_2_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_3_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_3_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_3_DETALLE}}</p>
    </div>
    <div class="indicador aparece es-atencion">
      <p class="rotulo">{{INDICADOR_4_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_4_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_4_DETALLE}}</p>
    </div>
  </div>
  <div class="malla dos">
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_POR_AREA}}</h2>
      <p class="subtitulo">{{SUBTITULO_POR_AREA}}</p>
      <figure class="grafico" data-grafico="por_area"></figure>
    </section>
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_DIAS}}</h2>
      <p class="subtitulo">{{SUBTITULO_DIAS}}</p>
      <figure class="grafico" data-grafico="dias"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_TIEMPOS}}</h2>
      <p class="subtitulo">{{SUBTITULO_TIEMPOS}}</p>
      <figure class="grafico" data-grafico="tiempos"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_HORAS}}</h2>
      <p class="subtitulo">{{SUBTITULO_HORAS}}</p>
      <figure class="grafico" data-grafico="horas"></figure>
    </section>
  </div>
```

## `informe_territorial`

```html maqueta=informe_territorial parte=ficha
<li><b>Periodo:</b> {{PERIODO}}</li>
      <li><b>Actualizado:</b> {{FECHA_ACTUALIZACION}}</li>
```

```html maqueta=informe_territorial parte=contenido
<div class="indicadores">
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_1_ROTULO}}</p>
      <p class="cifra" data-cifra="indicador_1"></p>
      <p class="detalle">{{INDICADOR_1_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_2_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_2_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_2_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_3_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_3_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_3_DETALLE}}</p>
    </div>
  </div>
  <div class="malla dos">
    <section class="tarjeta ancho-total">
      <h2>{{TITULO_MAPA}}</h2>
      <p class="subtitulo">{{SUBTITULO_MAPA}}</p>
      <figure class="grafico" data-grafico="mapa"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_RANKING}}</h2>
      <p class="subtitulo">{{SUBTITULO_RANKING}}</p>
      <figure class="grafico" data-grafico="ranking"></figure>
    </section>
    <section class="tarjeta">
      <h2>{{TITULO_CONCENTRACION}}</h2>
      <p class="subtitulo">{{SUBTITULO_CONCENTRACION}}</p>
      <figure class="grafico" data-grafico="concentracion"></figure>
    </section>
  </div>
```

## `poster`

```html maqueta=poster parte=ficha
<li><b>Fuente:</b> {{FUENTE_BREVE}}</li>
```

```css maqueta=poster parte=estilos
:root{--encaje:1497 1032}  /* ancho y alto utiles de la hoja, en px: lo lee el modulo encaje */
h1{font-size:clamp(2.2rem,5vw,3.8rem)}
.entradilla{font-size:1.25rem;max-width:80ch}
.poster{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2.4fr);gap:var(--e5);align-items:stretch}
.poster-cifras{display:flex;flex-direction:column;justify-content:space-between;gap:var(--e4)}
.poster-cifras div{border-left:6px solid var(--acento);padding-left:var(--e4)}
.poster-cifras p{margin:0;font-size:1.05rem;color:var(--apagado)}
.cifra-poster{font-size:clamp(2.6rem,5vw,4.4rem)!important;font-weight:760;letter-spacing:-.04em;line-height:1.05;color:var(--texto)!important;font-variant-numeric:tabular-nums}
.poster-grafico svg{max-height:none}
@media (max-width:900px){.poster{grid-template-columns:1fr}}
@media print{@page{size:A3 landscape;margin:12mm}.poster{grid-template-columns:1fr 2.4fr}.cifra-poster{font-size:44pt!important}.datos-grafico,.fuente-grafico{display:none}}
```

```html maqueta=poster parte=contenido
<div class="poster">
    <div class="poster-cifras">
      <div><p class="cifra-poster" data-cifra="cifra_1"></p><p>{{CIFRA_1_ROTULO}}</p></div>
      <div><p class="cifra-poster" data-cifra="cifra_2"></p><p>{{CIFRA_2_ROTULO}}</p></div>
      <div><p class="cifra-poster" data-cifra="cifra_3"></p><p>{{CIFRA_3_ROTULO}}</p></div>
    </div>
    <section class="tarjeta poster-grafico">
      <h2>{{TITULO_GRAFICO}}</h2>
      <figure class="grafico" data-grafico="principal"></figure>
    </section>
  </div>
```
