#!/usr/bin/env python3
"""Validador del catalogo de skills.

Comprueba, sobre cada `*/skills/*/SKILL.md`:

  1. Estructura   — frontmatter con sus claves, cinco fases, formulario JSON valido.
  2. Vectores     — todo identificador `Vn` usado esta declarado en el bloque de
                    correspondencia de la Fase 1.2, y todo `Vn = valor` usa un
                    identificador de opcion real de su campo.
  3. Ramas        — enumera el producto cartesiano de los dominios de los vectores
                    que consume la Fase 1.3 y verifica que ninguna combinacion se
                    quede sin rama, y que ninguna reciba dos plantillas exclusivas.

Uso:  python3 scripts/validar_skills.py   (desde la raiz del repositorio)
Salida: informe por skill y codigo de salida 1 si hay algun fallo.
"""
import re,glob,json,unicodedata,itertools
def norm(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','_',s).strip('_')
def cargar(f):
    t=open(f,encoding='utf-8').read()
    c=re.search(r'Correspondencia con el enrutamiento(.*?)\n\n', t, re.S)
    m=re.search(r'### 1\.2[^\n]*\n(.*?)(?=### 1\.3)', t, re.S)
    m3=re.search(r'### 1\.3(.*?)(?=\n### 1\.4|\n## FASE 2)', t, re.S)
    if not (c and m and m3): return None
    jb=re.search(r'```json\n(.*?)\n```', m.group(1), re.S)
    if not jb: return None
    ops={q["id"]:[o["id"] for o in q["options"]] for q in json.loads(jb.group(1))["form_data"]}
    mapa=dict(re.findall(r'`(V\d+(?:\.[a-z]|-bis|b)?)` — (?:respuesta a )?`?([a-z_]+)`?', c.group(1)))
    return {v:ops[q] for v,q in mapa.items() if q in ops}, m3.group(1)
def condiciones(linea, dom):
    cond={}
    for mm in re.finditer(r'(V\d+(?:\.[a-z]|-bis|b)?)\s*=\s*', linea):
        v=mm.group(1)
        if v not in dom: continue
        resto=linea[mm.end():]; vals=[]; pos=0
        while True:
            mt=re.match(r'\s*([A-Za-zÁÉÍÓÚÑáéíóúñ][\w\sÁÉÍÓÚÑáéíóúñ]*?)(?=\s*(?:,|\so\s|\sy\s|$|[\.\(\):;*\]\[→”"`]|->|\*\*))', resto[pos:])
            if not mt: break
            cand=norm(mt.group(1))
            if cand not in dom[v]: break
            vals.append(cand); pos+=mt.end()
            sep=re.match(r'\s*(?:,|\so\s)\s*(?![A-Z]?V\d)', resto[pos:])
            if not sep: break
            pos+=sep.end()
        if vals: cond.setdefault(v,set()).update(vals)
    return cond
ASSET=re.compile(r'assets/[\w.-]+\.md')
PARO=re.compile(r'DETENER|DETEN\b|DETENCION|no cre(ar|es|ir)|DERIVAR|Deriva a|det[eé]n el proceso|det[eé]n la redacci|detener proceso|no procede', re.I)
ADIC=re.compile(r'generar ademas|generar además|Documento adicional|se genera despues|se genera después|ademas ANTES|además ANTES|se generan DOS|dos documentos|los cinco assets', re.I)
COMOD=re.compile(r'todos los dem[aá]s casos|en cualquier otro caso|resto de casos', re.I)
CORTE=re.compile(r'->|→')
def ramas(texto, dom):
    out=[]; padre=None; ind_padre=-1
    for l in texto.split("\n"):
        if not l.strip().startswith(('-','*')): continue
        ind=len(l)-len(l.lstrip())
        cab=CORTE.split(l,1)[0] if CORTE.search(l) else l
        cond=condiciones(cab,dom)
        if ind<=ind_padre or padre is None:
            padre=cond if cond else None; ind_padre=ind; efec=dict(cond)
        else:
            efec=dict(padre or {})
            for k,vv in cond.items(): efec[k]=vv
        if ADIC.search(l): tipo='adicional'
        elif COMOD.search(l) and ASSET.search(l): tipo='comodin'
        elif ASSET.search(l): tipo='asset'
        elif PARO.search(l): tipo='paro'
        else: tipo=None
        if tipo=='comodin': out.append(({}, 'comodin', l.strip()[:95]))
        elif tipo and efec: out.append((efec,tipo,l.strip()[:95]))
    return out
TH=TC=0; det=[]
for f in sorted(glob.glob('*/skills/*/SKILL.md')):
    r=cargar(f)
    if not r: continue
    dom,texto=r; br=ramas(texto,dom)
    usados=sorted({v for c,_,_ in br for v in c}, key=lambda s:int(re.match(r'V(\d+)',s).group(1)))
    if not usados: continue
    n=1
    for v in usados: n*=len(dom[v])
    nombre=f.split('/skills/')[1][:-9]
    if n>200000: continue
    hue=[]; con=[]
    for combo in itertools.product(*[dom[v] for v in usados]):
        a=dict(zip(usados,combo))
        cas=[(t,l) for c,t,l in br if all(a[v] in vv for v,vv in c.items() if v in a)]
        prod={l for t,l in cas if t in ('asset','adicional')}
        excl={l for t,l in cas if t=='asset'}
        cuant={l for t,l in cas if 'uantia' in l}
        if not cas: hue.append(a)
        elif not prod and not any(t in ('paro','comodin') for t,_ in cas): hue.append(a)
        elif len(excl)>1 and not cuant: con.append((a,sorted(excl)))
    if hue or con:
        det.append((nombre,n,len(usados),hue,con)); TH+=len(hue); TC+=len(con)
for nombre,n,nv,hue,con in det:
    print(f"\n=== {nombre}  ({n} combinaciones, {nv} vectores)")
    if hue:
        print(f"  SIN RAMA: {len(hue)}/{n}")
        for h in hue[:5]: print("    "+", ".join(f"{v}={x}" for v,x in h.items()))
        if len(hue)>5: print(f"    ... y {len(hue)-5} mas")
    if con:
        print(f"  DOS PLANTILLAS A LA VEZ: {len(con)}/{n}")
        for a,ass in con[:2]:
            print("    "+", ".join(f"{v}={x}" for v,x in a.items()))
            for x in ass: print("       → "+x)
print(f"==== {TH} combinaciones sin rama | {TC} con dos plantillas | {len(det)} skills afectadas")

# ---------------------------------------------------------------- estructura y vectores
FALLOS=0
CLAVES={'name','description','when_to_use','inputs','outputs'}
TOKEN=re.compile(r'\bV\d+(?:\.[a-z]|-bis|b)?\b')
for f in sorted(glob.glob('*/skills/*/SKILL.md')):
    t=open(f,encoding='utf-8').read()
    nombre=f.split('/skills/')[1][:-9]
    fm=t.split('\n---\n')[0]
    if not CLAVES <= set(re.findall(r'^([a-z_]+):', fm, re.M)):
        print(f"  FALLO frontmatter incompleto: {nombre}"); FALLOS+=1
    if len(re.findall(r'^## FASE [1-5]', t, re.M))!=5:
        print(f"  FALLO no tiene cinco fases: {nombre}"); FALLOS+=1
    m=re.search(r'### 1\.2[^\n]*\n(.*?)(?=### 1\.3)', t, re.S)
    jb=re.search(r'```json\n(.*?)\n```', m.group(1), re.S) if m else None
    if jb:
        try: d=json.loads(jb.group(1))
        except Exception as e:
            print(f"  FALLO formulario JSON invalido: {nombre} ({e})"); FALLOS+=1; d=None
        if d:
            for q in d["form_data"]:
                if not {"id","rationale","question","options"} <= set(q) or len(q["options"])<2:
                    print(f"  FALLO pregunta mal formada: {nombre}/{q.get('id')}"); FALLOS+=1
    c=re.search(r'Correspondencia con el enrutamiento(.*?)\n\n', t, re.S)
    if c:
        decl=set(re.findall(r'`(V\d+(?:\.[a-z]|-bis|b)?)`', c.group(1)))
        resto=t[:c.start()]+t[c.end():]
        sin=sorted({x for x in TOKEN.findall(resto)}-decl)
        if sin: print(f"  FALLO vectores sin declarar: {nombre} {sin}"); FALLOS+=1
    elif TOKEN.search(t):
        print(f"  FALLO sin bloque de correspondencia: {nombre}"); FALLOS+=1
    import os
    for a in set(re.findall(r'assets/[\w.-]+\.md', t)):
        if not os.path.exists(os.path.join(os.path.dirname(f),a)):
            print(f"  FALLO asset inexistente: {nombre} {a}"); FALLOS+=1

# ---------------------------------------------------------------- registro de plugins y skills
import os as _os
_market='.claude-plugin/marketplace.json'
_reg=set()
if _os.path.exists(_market):
    _m=json.load(open(_market,encoding='utf-8'))
    _reg={p['name'] for p in _m.get('plugins',[])}
for _pj in sorted(glob.glob('*/.claude-plugin/plugin.json')):
    _p=_pj.split('/')[0]
    _d=json.load(open(_pj,encoding='utf-8'))
    _listadas=[s.split('/')[-1] for s in _d.get('skills',[])]
    _reales=sorted(_os.path.basename(x.rstrip('/')) for x in glob.glob(f'{_p}/skills/*/'))
    _falta=[s for s in _reales if s not in _listadas]
    _sobra=[s for s in _listadas if s not in _reales]
    if _falta: print(f"  FALLO skills en disco que {_p}/plugin.json no carga: {_falta}"); FALLOS+=1
    if _sobra: print(f"  FALLO skills listadas en {_p}/plugin.json que no existen: {_sobra}"); FALLOS+=1
    if _p not in _reg: print(f"  FALLO plugin sin registrar en marketplace.json: {_p}"); FALLOS+=1
    if _d.get('version')!=[x for x in _m.get('plugins',[]) if x['name']==_p][0].get('version') if _p in _reg else False:
        print(f"  FALLO version distinta entre {_p}/plugin.json y marketplace.json"); FALLOS+=1
for _s in sorted(glob.glob('*/skills/*/SKILL.md')):
    _fm=open(_s,encoding='utf-8').read().split('\n---\n')[0]
    if not re.search(r'^description:', _fm, re.M):
        print(f"  FALLO skill sin description: {_s}"); FALLOS+=1

if TH or TC: FALLOS+=1
print(("\nOK — catalogo coherente" if not FALLOS else f"\n{FALLOS} comprobaciones fallidas"))
raise SystemExit(1 if FALLOS else 0)

