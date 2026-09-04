#!/bin/sh
# Double-click to preview. Serves this folder and opens the home page.
cd "$(dirname "$0")" || exit 1
PORT=8080
while lsof -i :$PORT >/dev/null 2>&1; do PORT=$((PORT+1)); done
( sleep 1; open "http://localhost:$PORT/index.html" ) &
echo "FIBA 3x3 World Tour prototype — http://localhost:$PORT/index.html"
echo "Press Ctrl-C to stop."
python3 -m http.server $PORT
