#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

IPROXY_PID=""
IPROXY_MJPEG_PID=""

cleanup() {
	if [[ -n "$IPROXY_PID" ]] && kill -0 "$IPROXY_PID" 2>/dev/null; then
		echo "Stopping iproxy on port 8100..."
		kill "$IPROXY_PID" 2>/dev/null || true
		wait "$IPROXY_PID" 2>/dev/null || true
	fi
	if [[ -n "$IPROXY_MJPEG_PID" ]] && kill -0 "$IPROXY_MJPEG_PID" 2>/dev/null; then
		echo "Stopping iproxy on port 9100..."
		kill "$IPROXY_MJPEG_PID" 2>/dev/null || true
		wait "$IPROXY_MJPEG_PID" 2>/dev/null || true
	fi
}

trap cleanup EXIT INT TERM

if ! command -v iproxy >/dev/null 2>&1; then
	echo "iproxy is required but was not found in PATH."
	exit 1
fi

EXISTING_8100_PID=$(lsof -tiTCP:8100 -sTCP:LISTEN | head -n 1)
if [[ -n "$EXISTING_8100_PID" ]]; then
	EXISTING_8100_CMD=$(ps -p "$EXISTING_8100_PID" -o comm= 2>/dev/null || true)
	if [[ "$EXISTING_8100_CMD" == *iproxy* ]]; then
		echo "Reusing existing iproxy on http://localhost:8100"
	else
		echo "Port 8100 is already in use by $EXISTING_8100_CMD. Stop the existing listener before running start.sh."
		exit 1
	fi
else
	echo "Starting iproxy on http://localhost:8100"
	iproxy 8100 8100 >/tmp/ios-recorder-iproxy.log 2>&1 &
	IPROXY_PID=$!
fi

EXISTING_9100_PID=$(lsof -tiTCP:9100 -sTCP:LISTEN | head -n 1)
if [[ -z "$EXISTING_9100_PID" ]]; then
	echo "Starting iproxy on http://localhost:9100 (MJPEG)"
	iproxy 9100 9100 >>/tmp/ios-recorder-iproxy.log 2>&1 &
	IPROXY_MJPEG_PID=$!
fi

EXISTING_8888_PID=$(lsof -tiTCP:8888 -sTCP:LISTEN | head -n 1)
if [[ -n "$EXISTING_8888_PID" ]]; then
	EXISTING_8888_CMD=$(ps -p "$EXISTING_8888_PID" -o args= 2>/dev/null || true)
	if [[ "$EXISTING_8888_CMD" == *"uvicorn app.main:app"* ]]; then
		echo "iOS Recorder is already running on http://localhost:8888"
		exit 0
	else
		echo "Port 8888 is already in use by: $EXISTING_8888_CMD"
		exit 1
	fi
fi

echo "Installing dependencies..."
python3 -m pip install -r requirements.txt -q

echo "Starting iOS Recorder on http://localhost:8888"
# Only watch app/ and static/ for reloads — writing to pytest/tests/ or export/ must NOT restart the server
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8888 --reload --reload-dir app --reload-dir static
