#!/usr/bin/env bash
# 図解 HTML（日報×Slack）だけをローカルで開く用。8765 など他アプリとポートが被らないよう、
# デフォルトは 38471 から空きを探して http.server を起動する。
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/output"
PORT="${1:-38471}"
for _ in $(seq 0 30); do
  if ! lsof -i ":${PORT}" >/dev/null 2>&1; then
    break
  fi
  PORT=$((PORT + 1))
done
URL="http://127.0.0.1:${PORT}/ai-daily-report-slack-apr2026/index.html"
echo ""
echo "  output/ を配信中: http://127.0.0.1:${PORT}/"
echo ""
echo "  図解ページは次の URL です（アドレスバーにそのまま貼り付け）:"
echo "  ${URL}"
echo ""
echo "  タブのタイトルが「日報作成をAIで全自動化…」なら正しいページです。"
echo "  「領収書生成」と出たら別アプリの URL を開いています。"
echo ""
echo "  停止: Ctrl+C"
echo ""
exec python3 -m http.server "${PORT}"
