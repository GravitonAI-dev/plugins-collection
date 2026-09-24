<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITULO_ARTEFACTO}}</title>
<style>
*,*::before,*::after{box-sizing:border-box}
:root{
  color-scheme:light dark;
  --fondo:#f6f7fb;--superficie:#ffffff;--superficie-2:#f4f6fb;--borde:#e3e7f0;--borde-suave:#eef1f7;
  --texto:#121722;--apagado:#5f6675;
  --acento:#2f6ae8;--acento-suave:#eaf1ff;--acento-fuerte:#1c46ad;
  --ok:#0f9d63;--aviso:#e08a12;--riesgo:#d1445a;--linea-rejilla:#e8ebf3;
  --c1:#2f6ae8;--c2:#12b886;--c3:#f59e0b;--c4:#7c5cf0;--c5:#e35d9a;--c6:#64748b;
  --e1:4px;--e2:8px;--e3:14px;--e4:22px;--e5:34px;--e6:56px;
  --radio:20px;--radio-s:12px;
  --sombra:0 1px 2px rgba(47,106,232,.07),0 8px 22px rgba(18,23,34,.07),0 28px 56px rgba(47,106,232,.07);
  --fuente:ui-sans-serif,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
}
@media (prefers-color-scheme:dark){
  :root{
    --fondo:#0d1017;--superficie:#161b25;--superficie-2:#1d232f;--borde:#2a3240;--borde-suave:#222935;
    --texto:#e9edf5;--apagado:#9aa4b8;
    --acento:#7aa5ff;--acento-suave:#17233a;--acento-fuerte:#a9c4ff;
    --ok:#3ddc97;--aviso:#f0b354;--riesgo:#ff7a90;--linea-rejilla:#242c39;
    --c1:#7aa5ff;--c2:#3ddc97;--c3:#f0b354;--c4:#a78bfa;--c5:#f472b6;--c6:#94a3b8;
    --sombra:0 1px 2px rgba(0,0,0,.5),0 10px 26px rgba(0,0,0,.45),0 30px 60px rgba(0,0,0,.4);
  }
}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--fondo);color:var(--texto);font-family:var(--fuente);font-size:16px;line-height:1.55;
  background-image:radial-gradient(900px 460px at 12% -8%,color-mix(in srgb,var(--acento) 13%,transparent),transparent 72%),radial-gradient(760px 420px at 92% 4%,color-mix(in srgb,var(--c2) 10%,transparent),transparent 70%);
  background-attachment:fixed}
.contenedor{max-width:var(--ancho);margin:0 auto;padding:var(--e5) var(--e4) var(--e6)}
a{color:var(--acento)}
.borrador{display:flex;gap:var(--e3);border:1px solid var(--borde);border-left:4px solid var(--aviso);
  background:var(--superficie-2);border-radius:var(--radio);padding:var(--e3) var(--e4);
  font-size:.86rem;color:var(--apagado);margin:0 0 var(--e5);box-shadow:var(--sombra)}
.borrador strong{color:var(--texto);letter-spacing:.04em}
.antetitulo{font-size:.73rem;letter-spacing:.16em;text-transform:uppercase;color:var(--acento);font-weight:650;margin:0 0 var(--e2)}
h1{font-size:clamp(1.65rem,3.6vw,2.4rem);line-height:1.12;margin:0 0 var(--e3);letter-spacing:-.022em;font-weight:680}
.entradilla{font-size:1.06rem;color:var(--apagado);margin:0 0 var(--e4);max-width:66ch}
.ficha{display:flex;flex-wrap:wrap;gap:var(--e2) var(--e5);font-size:.84rem;color:var(--apagado);margin:0;padding:0;list-style:none}
.ficha b{color:var(--texto);font-weight:620}
.indicadores{display:grid;grid-template-columns:repeat(auto-fit,minmax(212px,1fr));gap:var(--e3);margin:0 0 var(--e4)}
.indicador{background:var(--superficie);border:1px solid var(--borde);border-radius:var(--radio);
  padding:calc(var(--e4) + var(--e1)) var(--e4) var(--e4);box-shadow:var(--sombra);position:relative;overflow:hidden}
.indicador::before{content:"";position:absolute;inset:0 0 auto 0;height:4px;
  background:linear-gradient(90deg,var(--acento),color-mix(in srgb,var(--acento) 45%,var(--c2)))}
.indicador.es-ok::before{background:var(--ok)}
.indicador.es-atencion::before{background:var(--aviso)}
.indicador.es-riesgo::before{background:var(--riesgo)}
.indicador .rotulo{font-size:.74rem;text-transform:uppercase;letter-spacing:.09em;color:var(--apagado);margin:0 0 var(--e2)}
.indicador .cifra{font-size:clamp(1.6rem,2.3vw,2.25rem);font-weight:680;letter-spacing:-.032em;line-height:1.05;margin:0;
  font-variant-numeric:tabular-nums;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.indicador .detalle{font-size:.8rem;color:var(--apagado);margin:var(--e2) 0 0}
.indicador.es-ok .cifra{color:var(--ok)}
.indicador.es-atencion .cifra{color:var(--aviso)}
.indicador.es-riesgo .cifra{color:var(--riesgo)}
.tarjeta{background:var(--superficie);border:1px solid var(--borde);border-radius:var(--radio);
  padding:calc(var(--e4) + var(--e2)) calc(var(--e4) + var(--e3));box-shadow:var(--sombra)}
h2{font-size:clamp(1.02rem,1.5vw,1.16rem);margin:0 0 var(--e1);letter-spacing:-.012em;font-weight:660}
.subtitulo{font-size:.84rem;color:var(--apagado);margin:0 0 var(--e4)}
p{margin:0 0 var(--e3)}
ul,ol{margin:0 0 var(--e3);padding-left:22px}
li{margin:0 0 var(--e1)}
.aviso{border:1px solid var(--borde);border-left:4px solid var(--acento);background:var(--acento-suave);
  border-radius:var(--radio-s);padding:var(--e3) var(--e4);margin:var(--e4) 0 0;font-size:.93rem}
.aviso.riesgo{border-left-color:var(--riesgo)}
.aviso.favorable{border-left-color:var(--ok)}
.aviso .titulo{display:block;font-weight:660;margin-bottom:var(--e1)}
.tabla{overflow-x:auto;margin:var(--e3) 0 0;max-width:100%}
.malla>*,.columnas>*,.diseno>*,.indicadores>*{min-width:0}
table{border-collapse:collapse;width:100%;font-size:.91rem;min-width:460px}
caption{caption-side:top;text-align:left;font-size:.82rem;color:var(--apagado);padding-bottom:var(--e2)}
th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--borde-suave);vertical-align:top}
thead th{font-size:.73rem;text-transform:uppercase;letter-spacing:.07em;color:var(--apagado);border-bottom:1px solid var(--borde)}
tbody tr:nth-child(even){background:var(--superficie-2)}
tbody tr:hover{background:var(--acento-suave)}
tfoot td{font-weight:660;border-top:1px solid var(--borde);border-bottom:none}
td.cifra,th.cifra{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.distintivo{display:inline-block;font-size:.73rem;font-weight:630;padding:3px 10px;border-radius:999px;
  border:1px solid var(--borde);background:var(--superficie-2);color:var(--apagado);white-space:nowrap}
.distintivo.ok{color:var(--ok);border-color:var(--ok)}
.distintivo.atencion{color:var(--aviso);border-color:var(--aviso)}
.distintivo.riesgo{color:var(--riesgo);border-color:var(--riesgo)}
.barras{list-style:none;margin:0;padding:0}
.barras li{margin:0 0 var(--e3)}
.barras .fila{display:flex;justify-content:space-between;gap:var(--e3);font-size:.88rem;margin:0 0 5px}
.barras .fila .valor{font-variant-numeric:tabular-nums;color:var(--apagado)}
.pista{height:10px;border-radius:999px;background:var(--superficie-2);border:1px solid var(--borde-suave);overflow:hidden}
.pista span{display:block;height:100%;border-radius:999px;background:linear-gradient(90deg,var(--c1),color-mix(in srgb,var(--c1) 72%,white))}
.barras li:nth-child(2) .pista span{background:linear-gradient(90deg,var(--c2),color-mix(in srgb,var(--c2) 72%,white))}
.barras li:nth-child(3) .pista span{background:linear-gradient(90deg,var(--c3),color-mix(in srgb,var(--c3) 72%,white))}
.barras li:nth-child(4) .pista span{background:linear-gradient(90deg,var(--c4),color-mix(in srgb,var(--c4) 72%,white))}
.barras li:nth-child(5) .pista span{background:linear-gradient(90deg,var(--c5),color-mix(in srgb,var(--c5) 72%,white))}
svg{max-width:100%;height:auto;display:block}
.eje{font-size:11px;fill:var(--apagado)}
.rejilla{stroke:var(--linea-rejilla);stroke-width:1}
.serie-1{fill:none;stroke:var(--c1);stroke-width:2.6;stroke-linejoin:round;stroke-linecap:round}
.serie-2{fill:none;stroke:var(--c2);stroke-width:2.4;stroke-dasharray:7 5;stroke-linejoin:round;stroke-linecap:round}
.punto-1{fill:var(--c1)}
.area-1{fill:url(#degradado-area);stroke:none}
.banda{fill:var(--ok);opacity:.12}
.leyenda{display:flex;flex-wrap:wrap;gap:var(--e2) var(--e4);list-style:none;margin:var(--e3) 0 0;padding:0;font-size:.83rem;color:var(--apagado)}
.leyenda li{display:flex;align-items:center;gap:7px;margin:0}
.leyenda i{width:11px;height:11px;border-radius:3px;display:inline-block}
.acciones{display:flex;gap:var(--e3);flex-wrap:wrap;margin:var(--e5) 0 0}
button{font:inherit;font-size:.9rem;font-weight:620;color:var(--texto);background:var(--superficie);
  border:1px solid var(--borde);border-radius:var(--radio-s);padding:10px 18px;cursor:pointer;box-shadow:var(--sombra)}
button:hover{border-color:var(--acento);color:var(--acento)}
button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible{outline:2px solid var(--acento);outline-offset:2px}
.pie{margin-top:var(--e5);padding-top:var(--e4);border-top:1px solid var(--borde);font-size:.82rem;color:var(--apagado)}
@media (prefers-reduced-motion:no-preference){
  .aparece{animation:aparece .55s cubic-bezier(.22,.7,.3,1) both}
  .aparece:nth-child(2){animation-delay:.05s}
  .aparece:nth-child(3){animation-delay:.1s}
  .aparece:nth-child(4){animation-delay:.15s}
  .pista span{animation:crece .8s cubic-bezier(.22,.7,.3,1) both;transform-origin:left center}
  @keyframes aparece{from{opacity:0;transform:translateY(7px)}to{opacity:1;transform:none}}
  @keyframes crece{from{transform:scaleX(0)}to{transform:scaleX(1)}}
}
:root{--ancho:1020px}
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
.resultado .cifra{font-size:1.5rem;font-weight:670;letter-spacing:-.025em;margin:0;font-variant-numeric:tabular-nums}
.resultado.principal{background:var(--acento-suave);border-color:var(--acento)}
.resultado.principal .cifra{color:var(--acento-fuerte)}
.medidor{margin:0 auto var(--e3)}
.medidor .pista-arco{fill:none;stroke:var(--superficie-2);stroke-width:16;stroke-linecap:round}
.medidor .arco{fill:none;stroke:var(--acento);stroke-width:16;stroke-linecap:round;transition:stroke-dasharray .35s ease}
.medidor text{fill:var(--texto)}
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
  :root{--fondo:#fff;--superficie:#fff;--superficie-2:#fff;--borde:#c8c5bf;--borde-suave:#dcd9d3;
        --texto:#000;--apagado:#3f3d39;--sombra:none;--acento-suave:#f2f6f8}
  @page{size:A4;margin:16mm 14mm}
  *{animation:none!important;transition:none!important}
  body{font-size:10.5pt;background-image:none}
  .contenedor{max-width:none;padding:0}
  .columnas{grid-template-columns:1fr}
  .acciones{display:none}
  .tarjeta{break-inside:avoid;page-break-inside:avoid;box-shadow:none}
  thead{display:table-header-group}
  tbody tr:hover{background:transparent}
}

@media print{
  /* Los colores de los graficos y de las barras viajan al papel aunque no se
     marque "graficos de fondo" en el dialogo de impresion. */
  *{-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important}
  p{orphans:3;widows:3}
  h1,h2,h3{break-after:avoid;page-break-after:avoid}
  tr{break-inside:avoid;page-break-inside:avoid}
  caption{break-after:avoid}
  .aviso,.leyenda,.barras li,.cronologia li{break-inside:avoid;page-break-inside:avoid}
}
</style>
</head>
<body>
<main class="contenedor">

  <p class="borrador"><span><strong>DRAFT</strong> &mdash; Herramienta de apoyo generada en la plataforma. Los resultados son una estimacion orientativa calculada con los parametros introducidos y deben ser verificados por un profesional colegiado antes de adoptar cualquier decision.</span></p>

  <header>
    <p class="antetitulo">{{ETIQUETA_SUPERIOR}}</p>
    <h1>{{TITULO_ARTEFACTO}}</h1>
    <p class="entradilla">{{ENTRADILLA}}</p>
  </header>

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
          <li><input type="checkbox" id="punto4"><label class="texto" for="punto4">{{PUNTO_4}}<small>{{PUNTO_4_DETALLE}}</small></label></li>
        </ul>
        <div class="progreso"><span id="barra-progreso"></span></div>
        <p class="progreso-texto" id="texto-progreso">0 de 4 puntos verificados</p>
      </section>
    </div>

    <div>
      <section class="tarjeta aparece">
        <h2>{{TITULO_PANEL_RESULTADO}}</h2>
        <p class="subtitulo">{{SUBTITULO_PANEL_RESULTADO}}</p>

        <svg class="medidor" viewBox="0 0 180 118" width="230" role="img" aria-label="{{MEDIDOR_DESCRIPCION}}">
          <path class="pista-arco" d="M 20 96 A 70 70 0 0 1 160 96"></path>
          <path class="arco" id="arco-medidor" d="M 20 96 A 70 70 0 0 1 160 96" stroke-dasharray="0 219.9"></path>
          <text x="90" y="88" text-anchor="middle" font-size="27" font-weight="670" id="medidor-cifra">--</text>
          <text class="eje" x="90" y="110" text-anchor="middle">{{MEDIDOR_ROTULO}}</text>
        </svg>

        <div class="resultados">
          <div class="resultado principal"><p class="rotulo">{{RESULTADO_1_ROTULO}}</p><p class="cifra" id="resultado1">--</p></div>
          <div class="resultado"><p class="rotulo">{{RESULTADO_2_ROTULO}}</p><p class="cifra" id="resultado2">--</p></div>
          <div class="resultado"><p class="rotulo">{{RESULTADO_3_ROTULO}}</p><p class="cifra" id="resultado3">--</p></div>
        </div>

        <div class="tabla">
          <table>
            <caption>{{TITULO_DESGLOSE}}</caption>
            <thead>
              <tr><th>{{DESGLOSE_COLUMNA_1}}</th><th class="cifra">{{DESGLOSE_COLUMNA_2}}</th><th class="cifra">{{DESGLOSE_COLUMNA_3}}</th></tr>
            </thead>
            <tbody id="cuerpo-desglose"></tbody>
            <tfoot>
              <tr><td>{{DESGLOSE_TOTAL_ROTULO}}</td><td class="cifra" id="total-columna-2">--</td><td class="cifra" id="total-columna-3"></td></tr>
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

  <div class="acciones">
    <button type="button" id="imprimir">Imprimir o guardar en PDF</button>
    <button type="button" id="reiniciar">Restablecer valores</button>
  </div>

  <footer class="pie">
    <p>{{PIE_FUENTES}}</p>
    <p>{{PIE_AVISO_LEGAL}}</p>
  </footer>

</main>
<script>
(function(){
  "use strict";
  var euro = new Intl.NumberFormat("es-ES", {style:"currency", currency:"EUR", maximumFractionDigits:2});
  var numero = new Intl.NumberFormat("es-ES", {maximumFractionDigits:2});
  var LONGITUD_ARCO = 219.9;
  var iniciales = {};

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
    document.getElementById("resultado1").textContent = euro.format(r.resultado1);
    document.getElementById("resultado2").textContent = euro.format(r.resultado2);
    document.getElementById("resultado3").textContent = numero.format(r.resultado3);

    var proporcion = Math.max(0, Math.min(100, r.medidor || 0));
    var arco = LONGITUD_ARCO * proporcion / 100;
    document.getElementById("arco-medidor").setAttribute("stroke-dasharray", arco.toFixed(1) + " " + (LONGITUD_ARCO - arco).toFixed(1));
    document.getElementById("medidor-cifra").textContent = numero.format(proporcion) + "%";

    var cuerpo = document.getElementById("cuerpo-desglose");
    cuerpo.textContent = "";
    var total = 0;
    r.desglose.forEach(function(fila){
      var tr = document.createElement("tr");
      var c1 = document.createElement("td"); c1.textContent = fila.concepto;
      var c2 = document.createElement("td"); c2.className = "cifra"; c2.textContent = euro.format(fila.importe);
      var c3 = document.createElement("td"); c3.className = "cifra"; c3.textContent = fila.detalle;
      tr.appendChild(c1); tr.appendChild(c2); tr.appendChild(c3);
      cuerpo.appendChild(tr);
      total += fila.importe;
    });
    document.getElementById("total-columna-2").textContent = euro.format(total);
    document.getElementById("total-columna-3").textContent = (r.totalDetalle === undefined) ? "" : r.totalDetalle;
  }

  function actualizar(){ pintar(calcular(leer())); }

  function progreso(){
    var casillas = document.querySelectorAll("#verificacion input[type=checkbox]");
    var hechos = 0;
    casillas.forEach(function(c){ if(c.checked){ hechos += 1; } });
    var porcentaje = casillas.length ? Math.round(hechos * 100 / casillas.length) : 0;
    document.getElementById("barra-progreso").style.width = porcentaje + "%";
    document.getElementById("texto-progreso").textContent = hechos + " de " + casillas.length + " puntos verificados";
  }

  document.getElementById("formulario").addEventListener("input", actualizar);
  document.getElementById("verificacion").addEventListener("change", progreso);
  document.getElementById("imprimir").addEventListener("click", function(){ window.print(); });
  document.getElementById("reiniciar").addEventListener("click", function(){
    Object.keys(iniciales).forEach(function(id){ document.getElementById(id).value = iniciales[id]; });
    document.querySelectorAll("#verificacion input[type=checkbox]").forEach(function(c){ c.checked = false; });
    actualizar(); progreso();
  });

  ["campo1","campo2","campo3","campo4"].forEach(function(id){ iniciales[id] = document.getElementById(id).value; });
  actualizar();
  progreso();
})();
</script>
</body>
</html>
