#!/usr/bin/env bash
# Marca el commit actual como revisado (README, seccion 10). Solo despues de pasar /simplify
# y /code-review sobre el diff y commitear lo que encuentren. Exige ademas el control de
# calidad en verde, asi que la marca significa "revisado y en verde" para este commit exacto.
# El hook pre-push lee el mismo registro: una linea "<sha> <fecha> <asunto>" por commit.
set -e
if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
  echo "Hay cambios sin commitear: commitea primero y marca despues." >&2
  exit 1
fi
scripts/control_calidad.sh
read -r commit corto asunto < <(git log -1 --format='%H %h %s')
echo "$commit $(date +%Y-%m-%dT%H:%M:%S) ${asunto:0:80}" >> "$(git rev-parse --git-common-dir)/revisiones-ok"
echo "Revisado y en verde: $corto ${asunto:0:80}"
