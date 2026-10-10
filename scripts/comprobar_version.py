#!/usr/bin/env python3
"""Comprueba que todo plugin modificado sube su version.

Compara el arbol de trabajo con el punto en que la rama se separo de la base
(por defecto `origin/develop`). Si un plugin tiene ficheros cambiados y su
`version` de `.claude-plugin/plugin.json` no es mayor que la de la base, falla.
La igualdad entre `plugin.json` y `marketplace.json` ya la vigila
`validar_skills.py`.

Uso:  python3 scripts/comprobar_version.py [rama_base]   (desde la raiz del repo)
      BASE_REF=origin/main python3 scripts/comprobar_version.py
Salida: codigo 1 si algun plugin cambiado no sube version.
"""
import json, os, subprocess, sys


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True)


def version(texto):
    return tuple(int(x) for x in json.loads(texto)["version"].split("."))


base = (sys.argv[1] if len(sys.argv) > 1 else os.environ.get("BASE_REF")) or "origin/develop"
mb = git("merge-base", base, "HEAD")
if mb.returncode:
    print(f"  AVISO no se encuentra la rama base {base}: no se comprueban versiones")
    sys.exit(0)
mb = mb.stdout.strip()

cambiados = set(git("diff", "--name-only", mb).stdout.split())
cambiados |= set(git("ls-files", "--others", "--exclude-standard").stdout.split())
plugins = sorted({d for d in (f.split("/")[0] for f in cambiados if "/" in f)
                  if os.path.exists(f"{d}/.claude-plugin/plugin.json")})

fallos = 0
for p in plugins:
    manifiesto = f"{p}/.claude-plugin/plugin.json"
    antes = git("show", f"{mb}:{manifiesto}")
    if antes.returncode:
        print(f"  OK {p}: plugin nuevo")
        continue
    v0 = version(antes.stdout)
    v1 = version(open(manifiesto, encoding="utf-8").read())
    if v1 <= v0:
        print(f"  FALLO {p} tiene cambios y no sube version ({'.'.join(map(str, v0))} en {base}): "
              "sube MAJOR, MINOR o PATCH en plugin.json y marketplace.json (README, seccion 15)")
        fallos += 1
    else:
        print(f"  OK {p}: {'.'.join(map(str, v0))} -> {'.'.join(map(str, v1))}")

print("\nOK — versiones al dia" if not fallos else f"\n{fallos} plugins sin subir version")
sys.exit(1 if fallos else 0)
