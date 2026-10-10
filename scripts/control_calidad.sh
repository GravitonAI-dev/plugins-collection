#!/usr/bin/env bash
#
# Control de calidad del catalogo. Es la unica puerta de entrada para skills y
# plugins: lo ejecutan el constructor al cerrar, el hook pre-push y GitHub en
# cada PR. Si sale en rojo, no se sube ni se fusiona.
#
#   scripts/control_calidad.sh [rama_base]     (por defecto origin/develop)
#
set -u
cd "$(git rev-parse --show-toplevel)"
fallo=0

echo "== Formato y datos de skills y plugins"
python3 scripts/validar_skills.py || fallo=1

echo
echo "== Versiones de los plugins modificados"
python3 scripts/comprobar_version.py "$@" || fallo=1

echo
if [ "$fallo" -ne 0 ]; then
  echo "CONTROL DE CALIDAD EN ROJO: corrige los FALLO de arriba antes de subir."
  exit 1
fi
echo "Control de calidad en verde. Antes de subir: /simplify y /code-review sobre el diff."
