#!/usr/bin/env bash
# Marca el commit actual como revisado con /simplify y /code-review. Se ejecuta solo
# despues de pasar las dos revisiones sobre el diff y aplicar lo que encuentren, y sin
# cambios pendientes: la marca vale para este commit exacto. Si despues se anade otro
# commit, hay que revisar de nuevo y volver a marcar.
#   scripts/marcar_revisado.sh
set -e
if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
  echo "Hay cambios sin commitear: commitea primero y marca despues." >&2
  exit 1
fi
registro="$(git rev-parse --git-common-dir)/revisiones-ok"
commit=$(git rev-parse HEAD)
echo "$commit $(date +%Y-%m-%dT%H:%M:%S) $(git log -1 --format=%s | cut -c1-80)" >> "$registro"
echo "Revisado: $(git log -1 --format='%h %s' | cut -c1-90)"
