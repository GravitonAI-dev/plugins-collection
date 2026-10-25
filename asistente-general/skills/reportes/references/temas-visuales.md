# Temas visuales

La base trae dos temas incorporados, `moderno` y `sobrio`, que se eligen solo con la etiqueta `html` (`data-tema="moderno"` o `data-tema="sobrio"`). Los demas temas de este documento se anaden **copiando su bloque `css` integro en el marcador `{{ESTILOS_TEMA}}` de la base** (dentro del unico `<style>`, justo despues del tema sobrio) y fijando `data-tema` con su nombre. Un tema es una sola pieza: no se mezclan dos ni se copia la mitad de uno.

Cada tema redefine los tokens de `:root` (colores, radios, sombra y, en algunos, la pila de fuentes), trae su version para el modo oscuro del sistema y, cuando el estilo lo pide, unas pocas reglas de forma (cabecera, tarjetas, titulares). Todos imprimen en blanco con la misma regla `@media print` de la base, que quita tambien los degradados de fondo; los temas siempre oscuros traen ademas su paleta de papel, con acentos y series que contrastan sobre blanco. Todos cumplen el contraste minimo 4.5:1 en claro y en oscuro.

Con un tema personalizado (`tema_personalizado`) se parte de cualquier tema y se aplica encima el modulo `marca` (`modulos-motor.md`), que sustituye el acento y la serie por los colores corporativos.

## Catalogo

| Tema | `data-tema` | Para quien y para que | Rasgos |
| :--- | :--- | :--- | :--- |
| Moderno | `moderno` | Paneles de datos, herramientas, presentaciones; cliente empresa o startup | Azul vivo, degradado de fondo, tarjetas muy redondeadas con sombra, cifras grandes. Es la base de los colores propios del despacho |
| Sobrio de despacho | `sobrio` | Informes de viabilidad y dictamenes; juzgado, cliente institucional | Azul petroleo y neutros calidos, radios cortos, sin degradado |
| Editorial | `editorial` | White papers, memorias, dossieres largos que se van a imprimir | Serif de sistema, papel crema, filetes finos, sin sombras, titulares grandes |
| Corporativo | `corporativo` | Memorias anuales, informes de KPIs, comites de direccion | Azul marino y gris, tarjetas cuadradas con borde marcado, cabecera con filete lateral, titulos de seccion en mayusculas |
| Minimal | `minimal` | Resumenes ejecutivos de una pagina, propuestas de honorarios | Blanco, negro y un unico acento naranja; sin bordes ni sombras; serie de grises |
| Nocturno | `nocturno` | Presentaciones en pantalla, paneles para sala de reuniones | Oscuro siempre (tambien con el sistema en claro), turquesa e indigo, brillo suave. Imprime en blanco |
| Tecnico | `tecnico` | Auditorias, cumplimiento, informes forenses o de sistemas | Monoespaciada de sistema, verde azulado, bordes de un pixel, radios minimos |
| Calido | `calido` | Particulares, inmobiliario, herencias y familia; casos de exito | Tierras: terracota, oliva y ocre sobre arena; radios amplios |
| Institucional | `institucional` | Administracion, universidades, colegios profesionales, fundaciones | Granate y dorado, titulares en serif, cabecera con filete doble |
| Pizarra | `pizarra` | Paneles densos de seguimiento, facturacion y cobros, tablas largas | Grises pizarra con acento cian, tarjetas con filete lateral, tablas compactas |
| Suave | `suave` | Boletines, comunicacion interna, casos de exito | Pasteles sobre lila, radios grandes, sombra difusa |
| Prensa | `prensa` | Boletines normativos, notas de actualidad, newsletters | Serif de periodico, blanco y negro con un rojo, filete grueso de cabecera, entradilla en cursiva |
| Alto contraste | `alto_contraste` | Accesibilidad, lectores con baja vision, proyeccion con mala luz | Negro, blanco y amarillo (en oscuro), bordes de dos pixeles, sin radios ni colores suaves |
| Dorado | `dorado` | Direccion, patrimonio, banca privada, presentaciones de prestigio | Siempre oscuro: negro y oro con verde salvia, titulares en serifa, brillo dorado en las cifras |
| Esmeralda nocturno | `esmeralda_noche` | Paneles de seguimiento en pantalla, sostenibilidad, energia | Siempre oscuro: negro verdoso, esmeralda y oro |
| Ambar | `ambar` | Salas de control, paneles operativos, alertas | Siempre oscuro: negro, ambar y amarillo con verde lima, titulos en mayusculas |
| Oliva y oro | `oliva_oro` | Agroalimentario, rural, bodegas, patrimonio familiar | Siempre oscuro: verde oliva profundo con oro y verdes calidos |
| Lima | `lima` | Tecnologia, datos, startups | Siempre oscuro: negro con lima y amarillo, cifras monoespaciadas, radios cortos |
| Menta | `menta` | Salud, bienestar, comunicacion amable con particulares | Pastel: menta y melocoton sobre blanco verdoso, radios grandes |
| Melocoton | `melocoton` | Familia, educacion, eventos, boletines cercanos | Pastel: melocoton, rosa y verde agua |
| Lavanda | `lavanda` | Comunicacion interna, RR. HH., formacion | Pastel: lavanda y rosa con verde agua |

**Como orientar.** La eleccion la hace el usuario (SKILL.md, 1.2); si duda, se le recomienda segun el destinatario y el soporte: a un juzgado o a un organismo, `sobrio` o `institucional`; a una direccion financiera, `corporativo` o `pizarra`; a un particular, `calido` o `suave`; a una sala con proyector o una pantalla, `nocturno`, `dorado`, `esmeralda_noche`, `ambar`, `lima` o `alto_contraste`; a un comunicado cercano, `suave`, `menta`, `melocoton` o `lavanda`; a papel, `editorial`, `prensa` o `minimal`.

**Lo que no cambia con el tema.** Los graficos usan los tokens (`--c1` a `--c6`, `--ok`, `--aviso`, `--riesgo`) y por eso heredan la paleta solos; las clases y la estructura de las maquetas son las mismas; la regla de impresion es comun. Un tema nunca se edita para un caso: si hacen falta otros colores, se usa el modulo `marca`.

---

## Editorial (`editorial`)

```css tema=editorial
:root[data-tema="editorial"]{
  --degradado:none;
  --fondo:#f9f6ef;--superficie:#fffdf8;--superficie-2:#f3eee3;--borde:#d9d2c3;--borde-suave:#e9e3d6;
  --texto:#1b1a17;--apagado:#5c574d;
  --acento:#8b2e2e;--acento-suave:#f4e6e3;--acento-fuerte:#5e1d1d;
  --ok:#3b6e3f;--aviso:#9c6a12;--riesgo:#a62f3b;--linea-rejilla:#e4ded0;
  --c1:#8b2e2e;--c2:#2f4f6f;--c3:#b7812b;--c4:#4f6b44;--c5:#6b4a7a;--c6:#7a7468;
  --radio:4px;--radio-s:3px;--sombra:none;
  --fuente:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
}
@media (prefers-color-scheme:dark){
  :root[data-tema="editorial"]{
    --fondo:#171511;--superficie:#1f1c17;--superficie-2:#27231d;--borde:#3a352c;--borde-suave:#2f2a23;
    --texto:#ece6d8;--apagado:#a69e8e;
    --acento:#e08a8a;--acento-suave:#33211f;--acento-fuerte:#f0b0b0;
    --ok:#8cc48f;--aviso:#e2b35a;--riesgo:#f08a94;--linea-rejilla:#2e2922;
    --c1:#e08a8a;--c2:#8fb3d6;--c3:#e0b86a;--c4:#9fc08f;--c5:#c4a0d4;--c6:#a09a8e;--sombra:none;
  }
}
:root[data-tema="editorial"] h1{font-weight:600;letter-spacing:-.01em;font-size:clamp(1.9rem,4vw,2.8rem)}
:root[data-tema="editorial"] .antetitulo,:root[data-tema="editorial"] .indicador .rotulo,:root[data-tema="editorial"] thead th,:root[data-tema="editorial"] .distintivo,:root[data-tema="editorial"] .eje{font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
:root[data-tema="editorial"] .indicador::before{background:var(--texto);height:2px}
:root[data-tema="editorial"] .indicador .cifra{font-weight:600}
:root[data-tema="editorial"] .entradilla{font-style:italic;font-size:1.12rem}
:root[data-tema="editorial"] .tarjeta{border-top:2px solid var(--texto)}
:root[data-tema="editorial"] .distintivo{border-radius:3px}
```

## Corporativo (`corporativo`)

```css tema=corporativo
:root[data-tema="corporativo"]{
  --degradado:none;--color-cifra:var(--acento-fuerte);
  --fondo:#eef1f5;--superficie:#ffffff;--superficie-2:#f4f6f9;--borde:#cfd6e0;--borde-suave:#e1e6ed;
  --texto:#0f1b2d;--apagado:#51607a;
  --acento:#0b3d91;--acento-suave:#e4ebf7;--acento-fuerte:#072a66;
  --ok:#1b7f4b;--aviso:#b26a00;--riesgo:#b3261e;--linea-rejilla:#dfe4eb;
  --c1:#0b3d91;--c2:#4f81bd;--c3:#9bbb59;--c4:#8064a2;--c5:#f79646;--c6:#7f8c9b;
  --radio:6px;--radio-s:4px;--sombra:0 1px 2px rgba(15,27,45,.08);
}
@media (prefers-color-scheme:dark){
  :root[data-tema="corporativo"]{
    --fondo:#0f1623;--superficie:#162032;--superficie-2:#1c283d;--borde:#2c3a52;--borde-suave:#243149;
    --texto:#e6ebf4;--apagado:#9fb0c9;
    --acento:#7ea6ea;--acento-suave:#1b2b47;--acento-fuerte:#a9c4f5;
    --ok:#5ec98f;--aviso:#e3a74c;--riesgo:#ef7b74;--linea-rejilla:#243149;
    --c1:#7ea6ea;--c2:#9dc0ea;--c3:#b6d37a;--c4:#b39ddb;--c5:#f9b27c;--c6:#9aa7b8;--sombra:0 1px 2px rgba(0,0,0,.5);
  }
}
:root[data-tema="corporativo"] .contenedor>header{border-left:6px solid var(--acento);padding-left:var(--e4);margin-bottom:var(--e4)}
:root[data-tema="corporativo"] .indicador::before{background:var(--acento)}
:root[data-tema="corporativo"] h2{text-transform:uppercase;letter-spacing:.07em;font-size:.9rem}
:root[data-tema="corporativo"] .distintivo{border-radius:4px}
:root[data-tema="corporativo"] thead th{background:var(--superficie-2)}
```

## Minimal (`minimal`)

```css tema=minimal
:root[data-tema="minimal"]{
  --degradado:none;
  --fondo:#ffffff;--superficie:#ffffff;--superficie-2:#f6f6f6;--borde:#e4e4e4;--borde-suave:#efefef;
  --texto:#111111;--apagado:#5f5f5f;
  --acento:#e4531b;--acento-suave:#fdeee7;--acento-fuerte:#b33a0b;
  --ok:#1a8f5a;--aviso:#b86f00;--riesgo:#d12f2f;--linea-rejilla:#ececec;
  --c1:#111111;--c2:#e4531b;--c3:#8a8a8a;--c4:#c4c4c4;--c5:#4d4d4d;--c6:#adadad;
  --radio:0;--radio-s:0;--sombra:none;
}
@media (prefers-color-scheme:dark){
  :root[data-tema="minimal"]{
    --fondo:#0e0e0e;--superficie:#0e0e0e;--superficie-2:#1a1a1a;--borde:#2c2c2c;--borde-suave:#212121;
    --texto:#f2f2f2;--apagado:#a6a6a6;
    --acento:#ff7a47;--acento-suave:#2a1710;--acento-fuerte:#ffa07a;
    --ok:#4ccf8d;--aviso:#f0a53a;--riesgo:#ff6b6b;--linea-rejilla:#262626;
    --c1:#f2f2f2;--c2:#ff7a47;--c3:#9a9a9a;--c4:#555555;--c5:#cfcfcf;--c6:#737373;--sombra:none;
  }
}
:root[data-tema="minimal"] .indicador,:root[data-tema="minimal"] .tarjeta{border:0;border-top:1px solid var(--texto);border-radius:0;padding-left:0;padding-right:0;background:transparent}
:root[data-tema="minimal"] .indicador::before{display:none}
:root[data-tema="minimal"] .borrador{box-shadow:none;background:transparent;border-left-width:2px}
:root[data-tema="minimal"] h1{font-weight:500;letter-spacing:-.03em;font-size:clamp(1.9rem,4vw,2.9rem)}
:root[data-tema="minimal"] .indicador .cifra{font-weight:500;letter-spacing:-.04em;font-size:clamp(2rem,3vw,2.9rem)}
:root[data-tema="minimal"] .distintivo,:root[data-tema="minimal"] button{border-radius:0}
:root[data-tema="minimal"] .aviso{background:transparent;border-width:0 0 0 2px;border-radius:0;padding-left:var(--e3)}
:root[data-tema="minimal"] tbody tr:nth-child(even){background:transparent}
```

## Nocturno (`nocturno`)

```css tema=nocturno
:root[data-tema="nocturno"]{
  --degradado:radial-gradient(800px 420px at 10% -10%,rgba(94,234,212,.16),transparent 70%),radial-gradient(700px 380px at 90% 0,rgba(129,140,248,.16),transparent 70%);--texto-sobre-serie:#0b0f1a;
  color-scheme:dark;
  --fondo:#0b0f1a;--superficie:#121829;--superficie-2:#182036;--borde:#263050;--borde-suave:#1e2740;
  --texto:#e6ecff;--apagado:#a3aecf;
  --acento:#5eead4;--acento-suave:#11313a;--acento-fuerte:#99f6e4;
  --ok:#4ade80;--aviso:#fbbf24;--riesgo:#fb7185;--linea-rejilla:#1f2941;
  --c1:#5eead4;--c2:#818cf8;--c3:#fbbf24;--c4:#f472b6;--c5:#60a5fa;--c6:#94a3b8;
  --radio:16px;--radio-s:10px;--sombra:0 0 0 1px rgba(94,234,212,.08),0 12px 32px rgba(0,0,0,.55);
}
:root[data-tema="nocturno"] .indicador::before{background:linear-gradient(90deg,var(--c1),var(--c2))}
:root[data-tema="nocturno"] .indicador .cifra{text-shadow:0 0 24px color-mix(in srgb,var(--acento) 35%,transparent)}
/* En papel: la base pone fondo blanco, texto negro y estados legibles; el tema solo da su acento y su serie de papel. */
@media print{
  :root[data-tema="nocturno"]{--acento:#0f766e;--acento-fuerte:#0b5a54;--c1:#0f766e;--c2:#4f46e5;--c3:#b45309;--c4:#be185d;--c5:#1d4ed8;--c6:#64748b;}
}
```

## Tecnico (`tecnico`)

```css tema=tecnico
:root[data-tema="tecnico"]{
  --degradado:none;
  --fondo:#f4f5f2;--superficie:#fbfbf9;--superficie-2:#eceee8;--borde:#c9cdc2;--borde-suave:#dde0d7;
  --texto:#161a16;--apagado:#55605a;
  --acento:#0f766e;--acento-suave:#e0f2ef;--acento-fuerte:#0a4f4a;
  --ok:#2e7d32;--aviso:#a35b00;--riesgo:#b42318;--linea-rejilla:#dcdfd6;
  --c1:#0f766e;--c2:#b45309;--c3:#4338ca;--c4:#6b7280;--c5:#be185d;--c6:#1f2937;
  --radio:4px;--radio-s:3px;--sombra:none;
  --fuente:ui-monospace,"SF Mono",Menlo,Consolas,"Liberation Mono","Courier New",monospace;
}
@media (prefers-color-scheme:dark){
  :root[data-tema="tecnico"]{
    --fondo:#0f1412;--superficie:#141a17;--superficie-2:#1a221e;--borde:#2b3530;--borde-suave:#222b26;
    --texto:#dfe7e2;--apagado:#9baba3;
    --acento:#5eead4;--acento-suave:#113a35;--acento-fuerte:#99f6e4;
    --ok:#6fdc8c;--aviso:#f5b64a;--riesgo:#ff7b72;--linea-rejilla:#222b26;
    --c1:#5eead4;--c2:#f5b64a;--c3:#a5b4fc;--c4:#9ca3af;--c5:#f9a8d4;--c6:#d1d5db;--sombra:none;
  }
}
:root[data-tema="tecnico"] body{font-size:15px}
:root[data-tema="tecnico"] h1{font-size:clamp(1.4rem,3vw,2rem);letter-spacing:0;font-weight:700}
:root[data-tema="tecnico"] .antetitulo::before{content:"// "}
:root[data-tema="tecnico"] .indicador::before{background:var(--acento);height:3px}
:root[data-tema="tecnico"] .indicador .cifra{letter-spacing:-.01em;font-size:clamp(1.4rem,2vw,1.9rem)}
:root[data-tema="tecnico"] .distintivo{border-radius:3px;text-transform:uppercase;letter-spacing:.04em}
:root[data-tema="tecnico"] .tarjeta,:root[data-tema="tecnico"] .indicador{border-color:var(--borde)}
:root[data-tema="tecnico"] .borrador{box-shadow:none}
```

## Calido (`calido`)

```css tema=calido
:root[data-tema="calido"]{
  --degradado:radial-gradient(900px 460px at 8% -8%,color-mix(in srgb,var(--c3) 16%,transparent),transparent 70%),radial-gradient(760px 420px at 95% 2%,color-mix(in srgb,var(--c1) 10%,transparent),transparent 70%);
  --fondo:#f8f1e7;--superficie:#fffaf3;--superficie-2:#f3e9da;--borde:#e2d3bd;--borde-suave:#ecdfcc;
  --texto:#2b2118;--apagado:#6b5a4a;
  --acento:#c2410c;--acento-suave:#fbe9df;--acento-fuerte:#8f2f08;
  --ok:#4d7c0f;--aviso:#b45309;--riesgo:#b91c1c;--linea-rejilla:#e9dece;
  --c1:#c2410c;--c2:#5b7a2a;--c3:#d4a017;--c4:#7c3f58;--c5:#2f6f8f;--c6:#8c7b6b;
  --radio:18px;--radio-s:10px;--sombra:0 2px 6px rgba(43,33,24,.06),0 12px 28px rgba(194,65,12,.06);
}
@media (prefers-color-scheme:dark){
  :root[data-tema="calido"]{
    --fondo:#1a1512;--superficie:#231c17;--superficie-2:#2b231d;--borde:#3f342b;--borde-suave:#342b24;
    --texto:#f1e8dd;--apagado:#b3a392;
    --acento:#fb923c;--acento-suave:#3a2415;--acento-fuerte:#fdba74;
    --ok:#a3d96b;--aviso:#f6b352;--riesgo:#f87171;--linea-rejilla:#342b24;
    --c1:#fb923c;--c2:#a3d96b;--c3:#f2c94c;--c4:#d98fb0;--c5:#7cc0e0;--c6:#b0a08f;--sombra:0 2px 6px rgba(0,0,0,.4),0 12px 28px rgba(0,0,0,.35);
  }
}
:root[data-tema="calido"] .indicador::before{background:linear-gradient(90deg,var(--c1),var(--c3))}
:root[data-tema="calido"] h1{font-weight:640}
```

## Institucional (`institucional`)

```css tema=institucional
:root[data-tema="institucional"]{
  --degradado:none;
  --fondo:#f5f3f0;--superficie:#ffffff;--superficie-2:#f1ede8;--borde:#d6cfc6;--borde-suave:#e6e0d8;
  --texto:#1f1a1a;--apagado:#5f5651;
  --acento:#6b1f2a;--acento-suave:#f3e4e6;--acento-fuerte:#48141c;
  --ok:#2f6b3a;--aviso:#946200;--riesgo:#a31d2d;--linea-rejilla:#e4ded6;
  --c1:#6b1f2a;--c2:#b08d3c;--c3:#2f4a6b;--c4:#4f6b3a;--c5:#7a4b70;--c6:#7b746d;
  --radio:8px;--radio-s:5px;--sombra:0 1px 2px rgba(31,26,26,.08);
}
@media (prefers-color-scheme:dark){
  :root[data-tema="institucional"]{
    --fondo:#151212;--superficie:#1d1818;--superficie-2:#251f1f;--borde:#3a3131;--borde-suave:#2e2727;
    --texto:#efe9e6;--apagado:#aa9f9a;
    --acento:#e39aa5;--acento-suave:#35202a;--acento-fuerte:#f2bfc6;
    --ok:#86c58f;--aviso:#e3b35a;--riesgo:#f08b95;--linea-rejilla:#2e2727;
    --c1:#e39aa5;--c2:#dcc27a;--c3:#90aed0;--c4:#a3c48f;--c5:#cfa0c4;--c6:#a8a09a;--sombra:0 1px 2px rgba(0,0,0,.5);
  }
}
:root[data-tema="institucional"] h1,:root[data-tema="institucional"] h2{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;font-weight:600}
:root[data-tema="institucional"] h1{font-size:clamp(1.8rem,3.8vw,2.6rem)}
:root[data-tema="institucional"] .contenedor>header{border-bottom:3px double var(--acento);padding-bottom:var(--e4);margin-bottom:var(--e4)}
:root[data-tema="institucional"] .antetitulo{color:var(--c2)}
:root[data-tema="institucional"] .indicador::before{background:linear-gradient(90deg,var(--c1),var(--c2))}
```

## Pizarra (`pizarra`)

```css tema=pizarra
:root[data-tema="pizarra"]{
  --degradado:none;
  --fondo:#e9edf0;--superficie:#f7f9fa;--superficie-2:#eef2f4;--borde:#c9d3d9;--borde-suave:#dae2e7;
  --texto:#152028;--apagado:#546470;
  --acento:#0e7490;--acento-suave:#dff3f8;--acento-fuerte:#0a4f61;
  --ok:#15803d;--aviso:#a16207;--riesgo:#b91c1c;--linea-rejilla:#d8e0e5;
  --c1:#0e7490;--c2:#334155;--c3:#0d9488;--c4:#64748b;--c5:#7c3aed;--c6:#94a3b8;
  --radio:10px;--radio-s:6px;--sombra:0 1px 3px rgba(21,32,40,.08);
}
@media (prefers-color-scheme:dark){
  :root[data-tema="pizarra"]{
    --fondo:#1e2a32;--superficie:#263540;--superficie-2:#2e3f4b;--borde:#3f5260;--borde-suave:#354653;
    --texto:#e7eef2;--apagado:#a7b8c3;
    --acento:#67d3ee;--acento-suave:#163844;--acento-fuerte:#a5e6f5;
    --ok:#6ad08a;--aviso:#f0bf55;--riesgo:#f27c7c;--linea-rejilla:#354653;
    --c1:#67d3ee;--c2:#b5c4d0;--c3:#5fd4c6;--c4:#8ea2b1;--c5:#c4a7f8;--c6:#7f93a1;--sombra:0 1px 3px rgba(0,0,0,.4);
  }
}
:root[data-tema="pizarra"] .indicador{border-left:4px solid var(--acento);padding-top:var(--e4)}
:root[data-tema="pizarra"] .indicador::before{display:none}
:root[data-tema="pizarra"] .indicador.es-ok{border-left-color:var(--ok)}
:root[data-tema="pizarra"] .indicador.es-atencion{border-left-color:var(--aviso)}
:root[data-tema="pizarra"] .indicador.es-riesgo{border-left-color:var(--riesgo)}
:root[data-tema="pizarra"] table{font-size:.86rem}
:root[data-tema="pizarra"] th,:root[data-tema="pizarra"] td{padding:7px 10px}
:root[data-tema="pizarra"] h2{font-size:1rem}
```

## Suave (`suave`)

```css tema=suave
:root[data-tema="suave"]{
  --degradado:radial-gradient(900px 460px at 10% -8%,color-mix(in srgb,var(--c1) 14%,transparent),transparent 72%),radial-gradient(760px 420px at 92% 4%,color-mix(in srgb,var(--c4) 10%,transparent),transparent 70%);
  --fondo:#f7f5fb;--superficie:#ffffff;--superficie-2:#f3f0fa;--borde:#e4dff0;--borde-suave:#ede9f6;
  --texto:#2a2440;--apagado:#655e80;
  --acento:#7c5cbf;--acento-suave:#efe9fb;--acento-fuerte:#58409a;
  --ok:#2e9e73;--aviso:#b8780f;--riesgo:#c94a62;--linea-rejilla:#ebe7f3;
  --c1:#7c5cbf;--c2:#3fa89d;--c3:#e58f3f;--c4:#d86a95;--c5:#4f82d3;--c6:#8f8ba3;
  --radio:24px;--radio-s:14px;--sombra:0 2px 4px rgba(42,36,64,.04),0 14px 34px rgba(124,92,191,.10);
}
@media (prefers-color-scheme:dark){
  :root[data-tema="suave"]{
    --fondo:#17141f;--superficie:#201c2b;--superficie-2:#282335;--borde:#3a3449;--borde-suave:#302a3e;
    --texto:#ece8f5;--apagado:#aaa3bf;
    --acento:#b39ae8;--acento-suave:#2b2340;--acento-fuerte:#d2c2f5;
    --ok:#6fd3a6;--aviso:#f0bb62;--riesgo:#f28aa0;--linea-rejilla:#302a3e;
    --c1:#b39ae8;--c2:#7fd3ca;--c3:#f7bf85;--c4:#f0a3c0;--c5:#8fb3f0;--c6:#9a95ad;--sombra:0 2px 4px rgba(0,0,0,.4),0 14px 34px rgba(0,0,0,.35);
  }
}
:root[data-tema="suave"] .indicador::before{background:linear-gradient(90deg,var(--c1),var(--c4))}
:root[data-tema="suave"] .borrador{border-radius:var(--radio-s)}
:root[data-tema="suave"] button{border-radius:999px}
```

## Prensa (`prensa`)

```css tema=prensa
:root[data-tema="prensa"]{
  --degradado:none;
  --fondo:#ffffff;--superficie:#ffffff;--superficie-2:#f4f4f4;--borde:#1a1a1a;--borde-suave:#cfcfcf;
  --texto:#111111;--apagado:#4a4a4a;
  --acento:#c8102e;--acento-suave:#fbe9ec;--acento-fuerte:#8e0b20;
  --ok:#1f7a3c;--aviso:#9a6400;--riesgo:#c8102e;--linea-rejilla:#dcdcdc;
  --c1:#111111;--c2:#c8102e;--c3:#6b6b6b;--c4:#a8a8a8;--c5:#3d3d3d;--c6:#d2d2d2;
  --radio:0;--radio-s:0;--sombra:none;
  --fuente:Georgia,"Times New Roman",Times,serif;
}
@media (prefers-color-scheme:dark){
  :root[data-tema="prensa"]{
    --fondo:#121212;--superficie:#121212;--superficie-2:#1c1c1c;--borde:#e5e5e5;--borde-suave:#3a3a3a;
    --texto:#f0f0f0;--apagado:#b5b5b5;
    --acento:#ff5a73;--acento-suave:#33161c;--acento-fuerte:#ff8fa0;
    --ok:#5fcf85;--aviso:#f2b84b;--riesgo:#ff5a73;--linea-rejilla:#2e2e2e;
    --c1:#f0f0f0;--c2:#ff5a73;--c3:#a5a5a5;--c4:#6a6a6a;--c5:#cfcfcf;--c6:#474747;--sombra:none;
  }
}
:root[data-tema="prensa"] .contenedor>header{border-top:4px solid var(--texto);border-bottom:1px solid var(--texto);padding:var(--e3) 0 var(--e3);margin-bottom:var(--e4)}
:root[data-tema="prensa"] h1{font-weight:700;font-size:clamp(2rem,4.4vw,3rem);letter-spacing:-.015em}
:root[data-tema="prensa"] .entradilla{font-style:italic;font-size:1.1rem}
:root[data-tema="prensa"] .antetitulo,:root[data-tema="prensa"] .indicador .rotulo,:root[data-tema="prensa"] thead th,:root[data-tema="prensa"] .distintivo,:root[data-tema="prensa"] .eje,:root[data-tema="prensa"] .ficha{font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
:root[data-tema="prensa"] .antetitulo{color:var(--texto)}
:root[data-tema="prensa"] .indicador,:root[data-tema="prensa"] .tarjeta{border:0;border-top:1px solid var(--texto);border-radius:0;padding-left:0;padding-right:0}
:root[data-tema="prensa"] .indicador::before{display:none}
:root[data-tema="prensa"] .indicador .cifra{font-weight:700}
:root[data-tema="prensa"] thead th{color:var(--texto);border-bottom:2px solid var(--texto)}
:root[data-tema="prensa"] .borrador{box-shadow:none;border-radius:0}
:root[data-tema="prensa"] .distintivo,:root[data-tema="prensa"] button{border-radius:0}
```

## Alto contraste (`alto_contraste`)

```css tema=alto_contraste
:root[data-tema="alto_contraste"]{
  --degradado:none;--texto-sobre-serie:var(--fondo);
  --fondo:#ffffff;--superficie:#ffffff;--superficie-2:#f0f0f0;--borde:#000000;--borde-suave:#555555;
  --texto:#000000;--apagado:#222222;
  --acento:#0000d6;--acento-suave:#e8e8ff;--acento-fuerte:#000080;
  --ok:#006400;--aviso:#7a4200;--riesgo:#b00020;--linea-rejilla:#8a8a8a;
  --c1:#0000d6;--c2:#006400;--c3:#7a4200;--c4:#6a0dad;--c5:#b00020;--c6:#333333;
  --radio:0;--radio-s:0;--sombra:none;
}
@media (prefers-color-scheme:dark){
  :root[data-tema="alto_contraste"]{
    --fondo:#000000;--superficie:#000000;--superficie-2:#161616;--borde:#ffffff;--borde-suave:#aaaaaa;
    --texto:#ffffff;--apagado:#dddddd;
    --acento:#ffff00;--acento-suave:#333300;--acento-fuerte:#ffff80;
    --ok:#00ff7f;--aviso:#ffb000;--riesgo:#ff6070;--linea-rejilla:#777777;
    --c1:#ffff00;--c2:#00ff7f;--c3:#ffb000;--c4:#d8a0ff;--c5:#ff6070;--c6:#cccccc;--sombra:none;
  }
}
:root[data-tema="alto_contraste"] .indicador,:root[data-tema="alto_contraste"] .tarjeta,:root[data-tema="alto_contraste"] .aviso,:root[data-tema="alto_contraste"] .borrador,:root[data-tema="alto_contraste"] button,:root[data-tema="alto_contraste"] .distintivo{border-width:2px}
:root[data-tema="alto_contraste"] .aviso,:root[data-tema="alto_contraste"] .borrador{border-left-width:8px}
:root[data-tema="alto_contraste"] .indicador::before{height:6px;background:var(--acento)}
:root[data-tema="alto_contraste"] .indicador .rotulo,:root[data-tema="alto_contraste"] thead th,:root[data-tema="alto_contraste"] .subtitulo,:root[data-tema="alto_contraste"] .leyenda,:root[data-tema="alto_contraste"] .eje{color:var(--texto);fill:var(--texto);font-weight:700}
:root[data-tema="alto_contraste"] .distintivo{font-weight:700}
:root[data-tema="alto_contraste"] .grafico .numero-riesgo,:root[data-tema="alto_contraste"] a{text-decoration:underline}
```

---

## Temas oscuros de acento dorado y verde

Los cinco temas siguientes son **siempre oscuros**, como `nocturno`: no cambian con el modo del sistema y al imprimir pasan a blanco con la regla comun de la base. Sirven para pantallas, salas, presentaciones y paneles de direccion con un aire premium. Las cifras dentro de barras se escriben en oscuro porque los acentos son claros.

## Dorado (`dorado`)

```css tema=dorado
:root[data-tema="dorado"]{
  --degradado:radial-gradient(900px 460px at 10% -10%,rgba(212,175,55,.14),transparent 70%),radial-gradient(700px 380px at 92% 0,rgba(143,191,106,.08),transparent 70%);--texto-sobre-serie:#0b0a08;--color-cifra:var(--acento-fuerte);
  color-scheme:dark;
  --fondo:#0b0a08;--superficie:#15130f;--superficie-2:#1d1a14;--borde:#332d22;--borde-suave:#26221a;
  --texto:#f3ecdc;--apagado:#b3a88f;
  --acento:#d4af37;--acento-suave:#2a2312;--acento-fuerte:#f0d27a;
  --ok:#7bc96f;--aviso:#f0b429;--riesgo:#ef6f6c;--linea-rejilla:#2a251c;
  --c1:#d4af37;--c2:#8fbf6a;--c3:#f5d76e;--c4:#c08a3e;--c5:#6fb8a8;--c6:#a39b88;
  --radio:12px;--radio-s:8px;--sombra:0 0 0 1px rgba(212,175,55,.10),0 14px 34px rgba(0,0,0,.6);
}
:root[data-tema="dorado"] h1,:root[data-tema="dorado"] h2{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;font-weight:600}
:root[data-tema="dorado"] .indicador::before{background:linear-gradient(90deg,#8a6d1f,var(--acento),#f0d27a)}
:root[data-tema="dorado"] .indicador .cifra{text-shadow:0 0 22px rgba(212,175,55,.25)}
:root[data-tema="dorado"] .antetitulo{letter-spacing:.24em}
/* En papel: la base pone fondo blanco, texto negro y estados legibles; el tema solo da su acento y su serie de papel. */
@media print{
  :root[data-tema="dorado"]{--acento:#8a6d1f;--acento-fuerte:#6b5416;--c1:#9a7b1c;--c2:#4f7a3a;--c3:#b8902a;--c4:#8a5a22;--c5:#2f6f63;--c6:#6b6455;}
}
```

## Esmeralda nocturno (`esmeralda_noche`)

```css tema=esmeralda_noche
:root[data-tema="esmeralda_noche"]{
  --degradado:radial-gradient(800px 420px at 8% -10%,rgba(52,211,153,.14),transparent 70%),radial-gradient(700px 380px at 95% 0,rgba(212,175,55,.10),transparent 70%);--texto-sobre-serie:#07110d;
  color-scheme:dark;
  --fondo:#07110d;--superficie:#0e1a15;--superficie-2:#13231c;--borde:#1f3a2e;--borde-suave:#182d24;
  --texto:#e6f2ec;--apagado:#9db8ab;
  --acento:#34d399;--acento-suave:#0f2a20;--acento-fuerte:#86efc4;
  --ok:#4ade80;--aviso:#fbbf24;--riesgo:#fb7185;--linea-rejilla:#183026;
  --c1:#34d399;--c2:#d4af37;--c3:#a3e635;--c4:#2dd4bf;--c5:#fbbf24;--c6:#94a3b8;
  --radio:14px;--radio-s:9px;--sombra:0 0 0 1px rgba(52,211,153,.08),0 12px 32px rgba(0,0,0,.55);
}
:root[data-tema="esmeralda_noche"] .indicador::before{background:linear-gradient(90deg,var(--c1),var(--c2))}
/* En papel: la base pone fondo blanco, texto negro y estados legibles; el tema solo da su acento y su serie de papel. */
@media print{
  :root[data-tema="esmeralda_noche"]{--acento:#0f7a55;--acento-fuerte:#0b5c40;--c1:#0f7a55;--c2:#9a7b1c;--c3:#5b8a1e;--c4:#0e7470;--c5:#b07a0f;--c6:#64748b;}
}
```

## Ambar (`ambar`)

```css tema=ambar
:root[data-tema="ambar"]{
  --degradado:radial-gradient(900px 440px at 50% -12%,rgba(251,191,36,.13),transparent 70%);--texto-sobre-serie:#0c0b07;--color-cifra:var(--acento);
  color-scheme:dark;
  --fondo:#0c0b07;--superficie:#16140d;--superficie-2:#1e1b12;--borde:#36301c;--borde-suave:#292414;
  --texto:#f7f1de;--apagado:#b9ae8c;
  --acento:#fbbf24;--acento-suave:#2d2410;--acento-fuerte:#fde68a;
  --ok:#84cc16;--aviso:#fb923c;--riesgo:#f87171;--linea-rejilla:#2a2516;
  --c1:#fbbf24;--c2:#84cc16;--c3:#fde68a;--c4:#f97316;--c5:#22d3ee;--c6:#a8a29e;
  --radio:10px;--radio-s:6px;--sombra:0 0 0 1px rgba(251,191,36,.10),0 12px 30px rgba(0,0,0,.6);
}
:root[data-tema="ambar"] .indicador::before{background:var(--acento);height:3px}
:root[data-tema="ambar"] h2{text-transform:uppercase;letter-spacing:.06em;font-size:.92rem}
/* En papel: la base pone fondo blanco, texto negro y estados legibles; el tema solo da su acento y su serie de papel. */
@media print{
  :root[data-tema="ambar"]{--acento:#a86a00;--acento-fuerte:#7f5000;--c1:#b07a00;--c2:#4d7c0f;--c3:#c49a2c;--c4:#c2410c;--c5:#0e7490;--c6:#78716c;}
}
```

## Oliva y oro (`oliva_oro`)

```css tema=oliva_oro
:root[data-tema="oliva_oro"]{
  --degradado:radial-gradient(900px 460px at 10% -8%,rgba(227,179,65,.12),transparent 70%),radial-gradient(760px 420px at 95% 2%,rgba(155,191,76,.10),transparent 70%);--texto-sobre-serie:#10140b;
  color-scheme:dark;
  --fondo:#10140b;--superficie:#181e11;--superficie-2:#1f2717;--borde:#33402a;--borde-suave:#28331f;
  --texto:#eef1e4;--apagado:#aeb79a;
  --acento:#e3b341;--acento-suave:#2a2814;--acento-fuerte:#f2d27e;
  --ok:#9bd16b;--aviso:#f0b354;--riesgo:#f08a7a;--linea-rejilla:#28331f;
  --c1:#e3b341;--c2:#9bbf4c;--c3:#d9e07a;--c4:#6b9e5a;--c5:#c97b3d;--c6:#9aa08a;
  --radio:16px;--radio-s:10px;--sombra:0 2px 6px rgba(0,0,0,.4),0 14px 32px rgba(0,0,0,.45);
}
:root[data-tema="oliva_oro"] h1{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;font-weight:600}
:root[data-tema="oliva_oro"] .indicador::before{background:linear-gradient(90deg,var(--c2),var(--c1))}
/* En papel: la base pone fondo blanco, texto negro y estados legibles; el tema solo da su acento y su serie de papel. */
@media print{
  :root[data-tema="oliva_oro"]{--acento:#8a6a14;--acento-fuerte:#6b5210;--c1:#a8841f;--c2:#5b7a2a;--c3:#8c8f2e;--c4:#3f6b34;--c5:#9a5a24;--c6:#6b6f5d;}
}
```

## Lima (`lima`)

```css tema=lima
:root[data-tema="lima"]{
  --degradado:none;--texto-sobre-serie:#090b08;
  color-scheme:dark;
  --fondo:#090b08;--superficie:#111410;--superficie-2:#171b15;--borde:#283024;--borde-suave:#1e241b;
  --texto:#ecf2e6;--apagado:#a3ae98;
  --acento:#a3e635;--acento-suave:#1f2b10;--acento-fuerte:#d9f99d;
  --ok:#4ade80;--aviso:#facc15;--riesgo:#fb7185;--linea-rejilla:#1e241b;
  --c1:#a3e635;--c2:#facc15;--c3:#22c55e;--c4:#e2e8f0;--c5:#38bdf8;--c6:#78716c;
  --radio:6px;--radio-s:4px;--sombra:0 0 0 1px rgba(163,230,53,.10),0 10px 28px rgba(0,0,0,.6);
  --fuente:ui-sans-serif,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
}
:root[data-tema="lima"] .indicador::before{background:var(--acento);height:2px}
:root[data-tema="lima"] .indicador .cifra,:root[data-tema="lima"] td.cifra{font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace;letter-spacing:-.02em}
:root[data-tema="lima"] .antetitulo::before{content:"● ";color:var(--acento)}
/* En papel: la base pone fondo blanco, texto negro y estados legibles; el tema solo da su acento y su serie de papel. */
@media print{
  :root[data-tema="lima"]{--acento:#4d7c0f;--acento-fuerte:#3a5e0b;--c1:#4d7c0f;--c2:#a16207;--c3:#15803d;--c4:#475569;--c5:#0369a1;--c6:#57534e;}
}
```

---

## Temas pastel

Tres paletas pastel con version clara y oscura. Los colores de serie son suaves; por eso las cifras dentro de barras y celdas se escriben en el color del texto y los titulares usan un acento mas profundo que la serie, para mantener el contraste 4.5:1.

## Menta (`menta`)

```css tema=menta
:root[data-tema="menta"]{
  --degradado:radial-gradient(900px 460px at 10% -8%,rgba(127,209,178,.22),transparent 72%),radial-gradient(760px 420px at 92% 4%,rgba(255,198,168,.18),transparent 70%);--texto-sobre-serie:#1d2b26;
  --fondo:#f2faf6;--superficie:#ffffff;--superficie-2:#eaf6f0;--borde:#d2eadf;--borde-suave:#e3f2eb;
  --texto:#1d2b26;--apagado:#5b6f67;
  --acento:#2a8a68;--acento-suave:#dff3ea;--acento-fuerte:#1c6a4f;
  --ok:#2a8a68;--aviso:#b8770f;--riesgo:#c4506a;--linea-rejilla:#e2efe9;
  --c1:#7fd1b2;--c2:#ffc6a8;--c3:#a9c8f5;--c4:#f6e08f;--c5:#d7b6f2;--c6:#b9c4bf;
  --radio:22px;--radio-s:14px;--sombra:0 2px 4px rgba(29,43,38,.04),0 14px 34px rgba(42,138,104,.10);
}
@media (prefers-color-scheme:dark){
  :root[data-tema="menta"]{
    --fondo:#101a16;--superficie:#17231e;--superficie-2:#1d2c26;--borde:#2c4038;--borde-suave:#24352e;
    --texto:#e8f4ee;--apagado:#a3b9b0;
    --acento:#8ee0c1;--acento-suave:#1d3a2f;--acento-fuerte:#bff0dc;
    --ok:#8ee0c1;--aviso:#f5c87a;--riesgo:#f4a0b4;--linea-rejilla:#24352e;
    --c1:#8ee0c1;--c2:#ffc6a8;--c3:#b4d0f7;--c4:#f6e08f;--c5:#dcc0f4;--c6:#9fb0a9;
    --sombra:0 2px 4px rgba(0,0,0,.4),0 14px 34px rgba(0,0,0,.35);
  }
}
:root[data-tema="menta"] .indicador::before{background:linear-gradient(90deg,var(--c1),var(--c2))}
:root[data-tema="menta"] button{border-radius:999px}
```

## Melocoton (`melocoton`)

```css tema=melocoton
:root[data-tema="melocoton"]{
  --degradado:radial-gradient(900px 460px at 10% -8%,rgba(255,179,143,.24),transparent 72%),radial-gradient(760px 420px at 92% 4%,rgba(242,168,192,.16),transparent 70%);--texto-sobre-serie:#2e2320;
  --fondo:#fff6f1;--superficie:#ffffff;--superficie-2:#fdeee6;--borde:#f3dccf;--borde-suave:#f8e8df;
  --texto:#2e2320;--apagado:#76625a;
  --acento:#c4572e;--acento-suave:#fde6da;--acento-fuerte:#9a3f1d;
  --ok:#3f8f6a;--aviso:#b5730c;--riesgo:#c0405a;--linea-rejilla:#f5e6dd;
  --c1:#ffb38f;--c2:#9fd8c6;--c3:#f7d488;--c4:#f2a8c0;--c5:#a8c6ef;--c6:#cdbcb4;
  --radio:22px;--radio-s:14px;--sombra:0 2px 4px rgba(46,35,32,.04),0 14px 34px rgba(196,87,46,.10);
}
@media (prefers-color-scheme:dark){
  :root[data-tema="melocoton"]{
    --fondo:#1b1311;--superficie:#241a17;--superficie-2:#2c211d;--borde:#43332d;--borde-suave:#382a25;
    --texto:#f6ebe6;--apagado:#c0aaa1;
    --acento:#ffb38f;--acento-suave:#3a2419;--acento-fuerte:#ffd3bf;
    --ok:#9fd8c6;--aviso:#f7d488;--riesgo:#f4a0b4;--linea-rejilla:#382a25;
    --c1:#ffb38f;--c2:#9fd8c6;--c3:#f7d488;--c4:#f2a8c0;--c5:#a8c6ef;--c6:#b8a69e;
    --sombra:0 2px 4px rgba(0,0,0,.4),0 14px 34px rgba(0,0,0,.35);
  }
}
:root[data-tema="melocoton"] .indicador::before{background:linear-gradient(90deg,var(--c1),var(--c4))}
:root[data-tema="melocoton"] button{border-radius:999px}
```

## Lavanda (`lavanda`)

```css tema=lavanda
:root[data-tema="lavanda"]{
  --degradado:radial-gradient(900px 460px at 10% -8%,rgba(184,166,245,.24),transparent 72%),radial-gradient(760px 420px at 92% 4%,rgba(245,184,212,.16),transparent 70%);--texto-sobre-serie:#24203a;
  --fondo:#f7f5ff;--superficie:#ffffff;--superficie-2:#f0edfd;--borde:#e0daf7;--borde-suave:#ebe7fb;
  --texto:#24203a;--apagado:#635d80;
  --acento:#6a4fc4;--acento-suave:#ece6ff;--acento-fuerte:#4e379c;
  --ok:#2f8f74;--aviso:#b4740f;--riesgo:#c2456a;--linea-rejilla:#ebe7f8;
  --c1:#b8a6f5;--c2:#f5b8d4;--c3:#9fdcd0;--c4:#ffd59e;--c5:#a6c8f7;--c6:#c4bfd6;
  --radio:22px;--radio-s:14px;--sombra:0 2px 4px rgba(36,32,58,.04),0 14px 34px rgba(106,79,196,.10);
}
@media (prefers-color-scheme:dark){
  :root[data-tema="lavanda"]{
    --fondo:#141221;--superficie:#1c192d;--superficie-2:#232038;--borde:#363150;--borde-suave:#2c2843;
    --texto:#ece9f8;--apagado:#aaa4c6;
    --acento:#c4b5fd;--acento-suave:#2a2448;--acento-fuerte:#e0d8fe;
    --ok:#9fdcd0;--aviso:#ffd59e;--riesgo:#f5b8d4;--linea-rejilla:#2c2843;
    --c1:#c4b5fd;--c2:#f5b8d4;--c3:#9fdcd0;--c4:#ffd59e;--c5:#a6c8f7;--c6:#aaa4c6;
    --sombra:0 2px 4px rgba(0,0,0,.4),0 14px 34px rgba(0,0,0,.35);
  }
}
:root[data-tema="lavanda"] .indicador::before{background:linear-gradient(90deg,var(--c1),var(--c2))}
:root[data-tema="lavanda"] button{border-radius:999px}
```
