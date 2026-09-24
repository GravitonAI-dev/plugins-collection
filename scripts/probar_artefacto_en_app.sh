#!/usr/bin/env bash
#
# Genera un artefacto con la habilidad `artefacto-visual` desde la aplicación
# y lo audita, todo seguido.
#
# Hace falta una gateway que responda a POST /v1/chat/completions: el backend
# no habla con ningún modelo por su cuenta. Se le pasa por variables:
#
#   GATEWAY_HOST=1.2.3.4 GATEWAY_PORT=443 GATEWAY_PROTOCOL=https \
#     scripts/probar_artefacto_en_app.sh
#
# Lo que hace, en orden: sirve este repositorio como servidor de plugins,
# reinicia el backend apuntándolo a esa gateway y a ese servidor, cierra la
# aplicación abierta a mano, lanza el segmento de interfaz que escribe el
# encargo en el chat y espera al artefacto, lo audita y lo abre en el navegador.
set -euo pipefail

REPO_PLUGINS="$HOME/Documents/Mio/pluggin-builder"
REPO_BACKEND="$HOME/Documents/Mio/GPT"
REPO_APP="$HOME/Documents/Mio/GPT-UI-1/confidential_gpt"
PUERTO_PLUGINS=3050
BACKEND_URL="http://127.0.0.1:8765"

GATEWAY_HOST="${GATEWAY_HOST:-}"
GATEWAY_PORT="${GATEWAY_PORT:-443}"
GATEWAY_PROTOCOL="${GATEWAY_PROTOCOL:-https}"

if [[ -z "$GATEWAY_HOST" ]]; then
  echo "Falta GATEWAY_HOST: sin gateway no hay modelo y la habilidad no puede escribir nada." >&2
  exit 2
fi

echo "→ comprobando la gateway en $GATEWAY_PROTOCOL://$GATEWAY_HOST:$GATEWAY_PORT"
if ! curl -sf -m 10 -o /dev/null "$GATEWAY_PROTOCOL://$GATEWAY_HOST:$GATEWAY_PORT/v1/chat/completions" \
     -X POST -H 'Content-Type: application/json' -d '{"model":"MiniMax-M2.5","messages":[]}' 2>/dev/null; then
  echo "  (no contesta a una petición vacía; sigo igualmente, puede exigir credenciales)"
fi

echo "→ servidor de plugins con el repositorio local"
if ! lsof -nP -iTCP:"$PUERTO_PLUGINS" -sTCP:LISTEN >/dev/null 2>&1; then
  nohup python3 /tmp/stub_updates_manager.py > /tmp/stub_um.log 2>&1 &
  sleep 2
fi
curl -sf -I -m 10 "http://127.0.0.1:$PUERTO_PLUGINS/api/plugins/download?branch=develop" >/dev/null \
  || { echo "El servidor de plugins no responde en :$PUERTO_PLUGINS" >&2; exit 1; }

echo "→ reiniciando el backend contra esa gateway"
pkill -f "src/confidentialai/main.py" 2>/dev/null || true
sleep 3
cd "$REPO_BACKEND"
UPDATE_MANAGER_HOST=127.0.0.1 UPDATE_MANAGER_PORT="$PUERTO_PLUGINS" UPDATE_MANAGER_PROTOCOL=http \
GATEWAY_HOST="$GATEWAY_HOST" GATEWAY_PORT="$GATEWAY_PORT" GATEWAY_PROTOCOL="$GATEWAY_PROTOCOL" \
  nohup ./.venv/bin/python src/confidentialai/main.py > /tmp/backend_run.log 2>&1 &
for _ in $(seq 1 40); do
  curl -sf -m 3 "$BACKEND_URL/health" >/dev/null 2>&1 && break
  sleep 2
done
curl -sf -m 5 "$BACKEND_URL/health" >/dev/null || { echo "El backend no arrancó; mira /tmp/backend_run.log" >&2; exit 1; }

echo "→ la habilidad que ve el backend"
curl -s -m 20 -X POST "$BACKEND_URL/api/v1/orchestrator/plugins/sync-skills" \
  -H 'Content-Type: application/json' -d '{}' \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print([p['skills'] for p in d['data']['payload'] if p['name']=='asistente-general'])"

echo "→ cerrando la aplicación abierta a mano (macOS no deja dos copias)"
pkill -f "confidentialAI.app/Contents/MacOS/confidentialAI" 2>/dev/null || true
sleep 2

echo "→ generando el artefacto desde la aplicación (puede tardar varios minutos)"
cd "$REPO_APP"
flutter test integration_test/habilidad_artefacto_test.dart -d macos \
  --dart-define=BASE_URL="$BACKEND_URL" --reporter expanded | tee /tmp/ui_habilidad.log

ARTEFACTO="$(grep -o 'ARTEFACTO GENERADO: [^(]*' /tmp/ui_habilidad.log | tail -1 | sed 's/ARTEFACTO GENERADO: //;s/ *$//')"
if [[ -z "$ARTEFACTO" || ! -f "$ARTEFACTO" ]]; then
  echo "No se generó ningún artefacto; el registro está en /tmp/ui_habilidad.log y /tmp/backend_run.log" >&2
  exit 1
fi

echo
echo "→ auditando $ARTEFACTO"
python3 "$REPO_PLUGINS/scripts/auditar_artefacto.py" "$ARTEFACTO" --render

echo
echo "→ abriéndolo en el navegador"
open "$ARTEFACTO"
