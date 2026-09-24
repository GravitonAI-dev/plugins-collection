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
:root{--ancho:1120px}
.malla{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:var(--e3);margin:0 0 var(--e3);align-items:start}
.malla .ancho-total{grid-column:1/-1}
.tendencia{margin:var(--e3) 0 0;padding-top:var(--e2);border-top:1px solid var(--borde-suave)}
.chispa{display:block;width:100%;height:30px}
.chispa-area{fill:var(--acento);opacity:.13;stroke:none}
.chispa-linea{fill:none;stroke:var(--acento);stroke-width:1.8;stroke-linejoin:round;stroke-linecap:round;vector-effect:non-scaling-stroke}
.chispa-punto{fill:var(--acento)}
.tendencia-nota{font-size:.76rem;color:var(--apagado);margin:5px 0 0}
.medidor text{fill:var(--texto)}
.medidor .pista-arco{fill:none;stroke:var(--superficie-2);stroke-width:18;stroke-linecap:round}
.medidor .arco{fill:none;stroke-width:18;stroke-linecap:round}
.cascada rect{stroke:none}
.cascada .conector{stroke:var(--linea-rejilla);stroke-width:1;stroke-dasharray:3 3}
.anillo circle{fill:none;stroke-width:24}
.anillo .base{stroke:var(--superficie-2)}
.centro-anillo{text-anchor:middle;fill:var(--texto);font-weight:670}
@media print{
  :root{--fondo:#fff;--superficie:#fff;--superficie-2:#fff;--borde:#c8c5bf;--borde-suave:#dcd9d3;
        --linea-rejilla:#d5d2cc;--texto:#000;--apagado:#3f3d39;--sombra:none;--acento-suave:#f2f6f8}
  @page{size:A4;margin:16mm 14mm}
  *{animation:none!important;transition:none!important}
  body{font-size:10.5pt;background-image:none}
  .contenedor{max-width:none;padding:0}
  .acciones{display:none}
  .tarjeta,.indicador{break-inside:avoid;page-break-inside:avoid;box-shadow:none;padding:var(--e3) var(--e4)}
  .malla{display:block}
  .tarjeta{margin:0 0 var(--e3)}
  .tarjeta svg{max-height:170px}
  .tarjeta.ancho-total svg{max-height:none}
  .borrador{padding:var(--e2) var(--e3);font-size:.78rem;margin-bottom:var(--e3)}
  h1{margin-bottom:var(--e2)}
  .entradilla{margin-bottom:var(--e2)}
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

  <p class="borrador"><span><strong>DRAFT</strong> &mdash; Panel de trabajo generado en la plataforma a partir de los datos aportados. Los importes, plazos y conclusiones deben ser verificados por un profesional colegiado antes de su uso externo.</span></p>

  <header>
    <p class="antetitulo">{{ETIQUETA_SUPERIOR}}</p>
    <h1>{{TITULO_ARTEFACTO}}</h1>
    <p class="entradilla">{{ENTRADILLA}}</p>
    <ul class="ficha">
      <li><b>Periodo:</b> {{PERIODO}}</li>
      <li><b>Fuente:</b> {{FUENTE_DATOS}}</li>
      <li><b>Actualizado:</b> {{FECHA_ACTUALIZACION}}</li>
    </ul>
  </header>

  <div class="indicadores">
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_1_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_1_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_1_DETALLE}}</p>
      <div class="tendencia">
        <svg class="chispa" viewBox="0 0 120 32" preserveAspectRatio="none" role="img" aria-label="{{CHISPA_DESCRIPCION}}">
          <polygon class="chispa-area" points="{{CHISPA_AREA}}"></polygon>
          <polyline class="chispa-linea" points="{{CHISPA_PUNTOS}}"></polyline>
          <circle class="chispa-punto" cx="119" cy="{{CHISPA_ULTIMO_Y}}" r="2.4"></circle>
        </svg>
        <p class="tendencia-nota">{{CHISPA_NOTA}}</p>
      </div>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_2_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_2_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_2_DETALLE}}</p>
    </div>
    <div class="indicador aparece es-atencion">
      <p class="rotulo">{{INDICADOR_3_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_3_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_3_DETALLE}}</p>
    </div>
    <div class="indicador aparece">
      <p class="rotulo">{{INDICADOR_4_ROTULO}}</p>
      <p class="cifra">{{INDICADOR_4_CIFRA}}</p>
      <p class="detalle">{{INDICADOR_4_DETALLE}}</p>
    </div>
  </div>

  <div class="malla">

    <section class="tarjeta">
      <h2>{{TITULO_BARRAS}}</h2>
      <p class="subtitulo">{{SUBTITULO_BARRAS}}</p>
      <ul class="barras">
        <li>
          <p class="fila"><span>{{BARRA_1_ROTULO}}</span><span class="valor">{{BARRA_1_VALOR}}</span></p>
          <div class="pista" role="img" aria-label="{{BARRA_1_ROTULO}}: {{BARRA_1_VALOR}}"><span style="width:{{BARRA_1_PORCENTAJE}}%"></span></div>
        </li>
        <li>
          <p class="fila"><span>{{BARRA_2_ROTULO}}</span><span class="valor">{{BARRA_2_VALOR}}</span></p>
          <div class="pista" role="img" aria-label="{{BARRA_2_ROTULO}}: {{BARRA_2_VALOR}}"><span style="width:{{BARRA_2_PORCENTAJE}}%"></span></div>
        </li>
        <li>
          <p class="fila"><span>{{BARRA_3_ROTULO}}</span><span class="valor">{{BARRA_3_VALOR}}</span></p>
          <div class="pista" role="img" aria-label="{{BARRA_3_ROTULO}}: {{BARRA_3_VALOR}}"><span style="width:{{BARRA_3_PORCENTAJE}}%"></span></div>
        </li>
        <li>
          <p class="fila"><span>{{BARRA_4_ROTULO}}</span><span class="valor">{{BARRA_4_VALOR}}</span></p>
          <div class="pista" role="img" aria-label="{{BARRA_4_ROTULO}}: {{BARRA_4_VALOR}}"><span style="width:{{BARRA_4_PORCENTAJE}}%"></span></div>
        </li>
      </ul>
    </section>

    <section class="tarjeta">
      <h2>{{TITULO_ANILLO}}</h2>
      <p class="subtitulo">{{SUBTITULO_ANILLO}}</p>
      <svg class="anillo" viewBox="0 0 230 190" role="img" aria-label="{{ANILLO_DESCRIPCION}}">
        <g transform="translate(115,95) rotate(-90)">
          <circle class="base" cx="0" cy="0" r="62"></circle>
          <circle cx="0" cy="0" r="62" stroke="var(--c1)" stroke-dasharray="{{ANILLO_ARCO_1}} {{ANILLO_RESTO_1}}" stroke-dashoffset="0"></circle>
          <circle cx="0" cy="0" r="62" stroke="var(--c2)" stroke-dasharray="{{ANILLO_ARCO_2}} {{ANILLO_RESTO_2}}" stroke-dashoffset="{{ANILLO_DESPLAZAMIENTO_2}}"></circle>
          <circle cx="0" cy="0" r="62" stroke="var(--c3)" stroke-dasharray="{{ANILLO_ARCO_3}} {{ANILLO_RESTO_3}}" stroke-dashoffset="{{ANILLO_DESPLAZAMIENTO_3}}"></circle>
        </g>
        <text class="centro-anillo" x="115" y="92" font-size="27">{{ANILLO_CIFRA_CENTRAL}}</text>
        <text class="centro-anillo eje" x="115" y="112" font-size="11">{{ANILLO_ROTULO_CENTRAL}}</text>
      </svg>
      <ul class="leyenda">
        <li><i style="background:var(--c1)"></i>{{ANILLO_LEYENDA_1}}</li>
        <li><i style="background:var(--c2)"></i>{{ANILLO_LEYENDA_2}}</li>
        <li><i style="background:var(--c3)"></i>{{ANILLO_LEYENDA_3}}</li>
      </ul>
    </section>

    <section class="tarjeta ancho-total">
      <h2>{{TITULO_EVOLUCION}}</h2>
      <p class="subtitulo">{{SUBTITULO_EVOLUCION}}</p>
      <svg viewBox="0 0 700 300" role="img" aria-label="{{EVOLUCION_DESCRIPCION}}">
        <defs>
          <linearGradient id="degradado-area" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="var(--c1)" stop-opacity=".34"></stop>
            <stop offset="100%" stop-color="var(--c1)" stop-opacity="0"></stop>
          </linearGradient>
        </defs>
        <rect class="banda" x="64" y="{{BANDA_Y}}" width="600" height="{{BANDA_ALTO}}"></rect>
        <line class="rejilla" x1="64" y1="44" x2="664" y2="44"></line>
        <line class="rejilla" x1="64" y1="94" x2="664" y2="94"></line>
        <line class="rejilla" x1="64" y1="144" x2="664" y2="144"></line>
        <line class="rejilla" x1="64" y1="194" x2="664" y2="194"></line>
        <line class="rejilla" x1="64" y1="244" x2="664" y2="244"></line>
        <text class="eje" x="56" y="48" text-anchor="end">{{EJE_Y_4}}</text>
        <text class="eje" x="56" y="98" text-anchor="end">{{EJE_Y_3}}</text>
        <text class="eje" x="56" y="148" text-anchor="end">{{EJE_Y_2}}</text>
        <text class="eje" x="56" y="198" text-anchor="end">{{EJE_Y_1}}</text>
        <text class="eje" x="56" y="248" text-anchor="end">0</text>
        <polygon class="area-1" points="{{AREA_SERIE_1}}"></polygon>
        <polyline class="serie-1" points="{{PUNTOS_SERIE_1}}"></polyline>
        <polyline class="serie-2" points="{{PUNTOS_SERIE_2}}"></polyline>
        <text class="eje" x="64" y="266">{{EJE_X_1}}</text>
        <text class="eje" x="214" y="266">{{EJE_X_2}}</text>
        <text class="eje" x="364" y="266">{{EJE_X_3}}</text>
        <text class="eje" x="514" y="266">{{EJE_X_4}}</text>
        <text class="eje" x="664" y="266" text-anchor="end">{{EJE_X_5}}</text>
      </svg>
      <ul class="leyenda">
        <li><i style="background:var(--c1)"></i>{{LEYENDA_SERIE_1}}</li>
        <li><i style="background:var(--c2)"></i>{{LEYENDA_SERIE_2}}</li>
        <li><i style="background:var(--ok);opacity:.35"></i>{{LEYENDA_BANDA}}</li>
      </ul>
    </section>

    <section class="tarjeta">
      <h2>{{TITULO_CASCADA}}</h2>
      <p class="subtitulo">{{SUBTITULO_CASCADA}}</p>
      <svg class="cascada" viewBox="0 0 460 280" role="img" aria-label="{{CASCADA_DESCRIPCION}}">
        <line class="rejilla" x1="40" y1="240" x2="440" y2="240"></line>
        <rect x="52" y="{{CASCADA_1_Y}}" width="72" height="{{CASCADA_1_ALTO}}" fill="var(--c1)" rx="3"></rect>
        <rect x="152" y="{{CASCADA_2_Y}}" width="72" height="{{CASCADA_2_ALTO}}" fill="var(--c2)" rx="3"></rect>
        <rect x="252" y="{{CASCADA_3_Y}}" width="72" height="{{CASCADA_3_ALTO}}" fill="var(--c4)" rx="3"></rect>
        <rect x="352" y="{{CASCADA_4_Y}}" width="72" height="{{CASCADA_4_ALTO}}" fill="var(--acento-fuerte)" rx="3"></rect>
        <line class="conector" x1="124" y1="{{CASCADA_1_Y}}" x2="152" y2="{{CASCADA_1_Y}}"></line>
        <line class="conector" x1="224" y1="{{CASCADA_2_Y}}" x2="252" y2="{{CASCADA_2_Y}}"></line>
        <line class="conector" x1="324" y1="{{CASCADA_3_Y}}" x2="352" y2="{{CASCADA_3_Y}}"></line>
        <text class="eje" x="88" y="258" text-anchor="middle">{{CASCADA_1_ROTULO}}</text>
        <text class="eje" x="188" y="258" text-anchor="middle">{{CASCADA_2_ROTULO}}</text>
        <text class="eje" x="288" y="258" text-anchor="middle">{{CASCADA_3_ROTULO}}</text>
        <text class="eje" x="388" y="258" text-anchor="middle">{{CASCADA_4_ROTULO}}</text>
        <text class="eje" x="88" y="{{CASCADA_1_ETIQUETA_Y}}" text-anchor="middle">{{CASCADA_1_VALOR}}</text>
        <text class="eje" x="188" y="{{CASCADA_2_ETIQUETA_Y}}" text-anchor="middle">{{CASCADA_2_VALOR}}</text>
        <text class="eje" x="288" y="{{CASCADA_3_ETIQUETA_Y}}" text-anchor="middle">{{CASCADA_3_VALOR}}</text>
        <text class="eje" x="388" y="{{CASCADA_4_ETIQUETA_Y}}" text-anchor="middle">{{CASCADA_4_VALOR}}</text>
      </svg>
    </section>

    <section class="tarjeta">
      <h2>{{TITULO_MEDIDOR}}</h2>
      <p class="subtitulo">{{SUBTITULO_MEDIDOR}}</p>
      <svg class="medidor" viewBox="0 0 240 150" role="img" aria-label="{{MEDIDOR_DESCRIPCION}}">
        <path class="pista-arco" d="M 30 125 A 90 90 0 0 1 210 125"></path>
        <path class="arco" d="M 30 125 A 90 90 0 0 1 210 125" stroke="{{MEDIDOR_COLOR}}"
              stroke-dasharray="{{MEDIDOR_ARCO}} {{MEDIDOR_RESTO}}"></path>
        <text x="120" y="112" text-anchor="middle" font-size="34" font-weight="670">{{MEDIDOR_CIFRA}}</text>
        <text class="eje" x="120" y="136" text-anchor="middle">{{MEDIDOR_ROTULO}}</text>
        <text class="eje" x="30" y="145" text-anchor="middle">0</text>
        <text class="eje" x="210" y="145" text-anchor="middle">{{MEDIDOR_MAXIMO}}</text>
      </svg>
      <div class="aviso">
        <span class="titulo">{{MEDIDOR_TITULO_NOTA}}</span>
        {{MEDIDOR_NOTA}}
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
            <tr><td>{{FILA_3_C1}}</td><td>{{FILA_3_C2}}</td><td class="cifra">{{FILA_3_C3}}</td><td class="cifra">{{FILA_3_C4}}</td><td><span class="distintivo">{{FILA_3_C5}}</span></td></tr>
          </tbody>
          <tfoot>
            <tr><td>{{TOTAL_ROTULO}}</td><td></td><td class="cifra">{{TOTAL_C3}}</td><td class="cifra">{{TOTAL_C4}}</td><td></td></tr>
          </tfoot>
        </table>
      </div>
    </section>

  </div>

  <div class="acciones">
    <button type="button" id="imprimir">Imprimir o guardar en PDF</button>
  </div>

  <footer class="pie">
    <p>{{PIE_FUENTES}}</p>
    <p>{{PIE_AVISO_LEGAL}}</p>
  </footer>

</main>
<script>
document.getElementById("imprimir").addEventListener("click", function(){ window.print(); });
</script>
</body>
</html>
H
cat /tmp/panel_head.html /tmp/base.css /tmp/panel_css2.css > template-panel-datos.md
rm -f template-artefacto-panel-datos.md
grep -c . template-panel-datos.md