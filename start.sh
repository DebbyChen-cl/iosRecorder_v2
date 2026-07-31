#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

IPROXY_PID=""
IPROXY_MJPEG_PID=""
UNIT_TEST_MODE=0
XPATH_MODE=0
# Device to tunnel to. Empty = auto-detect (see below). Never rely on iproxy's
# implicit "first device" pick: with two devices attached it silently chooses the
# wrong one and every WDA call fails with "Error connecting to device: Connection refused".
UDID="${RECORDER_UDID:-}"

EXPECT_UDID=0
for arg in "$@"; do
	if [[ "$EXPECT_UDID" -eq 1 ]]; then
		UDID="$arg"
		EXPECT_UDID=0
		continue
	fi
  if [[ "$arg" == "--unit_test" ]]; then
    UNIT_TEST_MODE=1
    echo "[Unit Test Capture Mode] Fixture captures will be saved to test_unittest/fixtures/"
	elif [[ "$arg" == "--xpath" ]]; then
		XPATH_MODE=1
		echo "[XPath Mode] Selector output is forced to XPath"
	elif [[ "$arg" == "--udid" ]]; then
		EXPECT_UDID=1
	elif [[ "$arg" == --udid=* ]]; then
		UDID="${arg#--udid=}"
  fi
done

if [[ "$EXPECT_UDID" -eq 1 ]]; then
	echo "--udid requires a value, e.g. --udid 00008130-000A750C36F0001C"
	exit 1
fi

if [[ "$UNIT_TEST_MODE" -eq 1 && "$XPATH_MODE" -eq 1 ]]; then
	echo "--xpath and --unit_test cannot be used together."
	exit 1
fi

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

# Poll WDA /status with a generous timeout and retries. A busy WDA (mid page-source
# fetch, which routinely takes 4-5s) serialises requests, so a single short probe
# reports a healthy tunnel as dead.
wda_responds() {
	local url="$1" attempt
	for attempt in 1 2 3; do
		if curl -sf -m 15 "$url/status" >/dev/null 2>&1; then
			return 0
		fi
		sleep 1
	done
	return 1
}

# Tunnel device port 8100 through a throwaway local port and ask WDA for /status.
# Returns 0 only when that device is actually running WebDriverAgent.
probe_wda() {
	local udid="$1" port probe_pid rc=1
	for port in 18100 18101 18102 18103 18104; do
		if [[ -z "$(lsof -tiTCP:"$port" -sTCP:LISTEN | head -n 1)" ]]; then
			break
		fi
		port=""
	done
	if [[ -z "$port" ]]; then
		return 1
	fi
	iproxy -u "$udid" "$port" 8100 >/dev/null 2>&1 &
	probe_pid=$!
	sleep 2
	if wda_responds "http://localhost:$port"; then
		rc=0
	fi
	kill "$probe_pid" 2>/dev/null || true
	wait "$probe_pid" 2>/dev/null || true
	return "$rc"
}

UDID_SOURCE="--udid / RECORDER_UDID"

if [[ -z "$UDID" ]]; then
	if ! command -v idevice_id >/dev/null 2>&1; then
		echo "idevice_id is required to auto-detect the device. Pass --udid <UDID> instead."
		exit 1
	fi
	DEVICES=($(idevice_id -l 2>/dev/null || true))
	if [[ "${#DEVICES[@]}" -eq 0 ]]; then
		echo "No iOS device detected. Connect the device and trust this Mac."
		exit 1
	fi

	# Same device the pytest run will target, so recording and playback never diverge.
	CONFIG_UDID=$(python3 -c "import sys; sys.path.insert(0, 'pytest'); import config; print(config.IOS_CAPABILITIES.get('appium:udid', '') or '')" 2>/dev/null || true)
	if [[ -n "$CONFIG_UDID" ]]; then
		for candidate in "${DEVICES[@]}"; do
			if [[ "$candidate" == "$CONFIG_UDID" ]]; then
				UDID="$CONFIG_UDID"
				UDID_SOURCE="pytest/config.py"
				break
			fi
		done
		if [[ -z "$UDID" ]]; then
			echo "pytest/config.py targets $CONFIG_UDID but that device is not attached — falling back to auto-detect."
		fi
	fi

	if [[ -z "$UDID" ]]; then
		if [[ "${#DEVICES[@]}" -eq 1 ]]; then
			UDID="${DEVICES[0]}"
			UDID_SOURCE="only attached device"
		else
			echo "${#DEVICES[@]} devices attached — probing which one runs WebDriverAgent..."
			for candidate in "${DEVICES[@]}"; do
				if probe_wda "$candidate"; then
					UDID="$candidate"
					UDID_SOURCE="WDA probe"
					break
				fi
				echo "  $candidate — no WDA on port 8100"
			done
			if [[ -z "$UDID" ]]; then
				echo "None of the attached devices is running WebDriverAgent on port 8100."
				echo "Launch WDA (Xcode: WebDriverAgentRunner test) then rerun, or pass --udid <UDID>."
				exit 1
			fi
		fi
	fi
fi
echo "Using device $UDID ($UDID_SOURCE)"

EXISTING_8100_PID=$(lsof -tiTCP:8100 -sTCP:LISTEN | head -n 1)
if [[ -n "$EXISTING_8100_PID" ]]; then
	EXISTING_8100_CMD=$(ps -p "$EXISTING_8100_PID" -o comm= 2>/dev/null || true)
	if [[ "$EXISTING_8100_CMD" == *iproxy* ]]; then
		# An iproxy left over from an earlier run may be bound to a different device.
		# Verify it actually reaches WDA instead of silently reusing a dead tunnel.
		if wda_responds http://localhost:8100; then
			echo "Reusing existing iproxy on http://localhost:8100"
		else
			echo "An iproxy is listening on 8100 (pid $EXISTING_8100_PID) but WDA does not answer —"
			echo "it is most likely tunnelling to the wrong device. Stop it with: kill $EXISTING_8100_PID"
			exit 1
		fi
	else
		echo "Port 8100 is already in use by $EXISTING_8100_CMD. Stop the existing listener before running start.sh."
		exit 1
	fi
else
	echo "Starting iproxy on http://localhost:8100"
	iproxy -u "$UDID" 8100 8100 >/tmp/ios-recorder-iproxy.log 2>&1 &
	IPROXY_PID=$!
fi

EXISTING_9100_PID=$(lsof -tiTCP:9100 -sTCP:LISTEN | head -n 1)
if [[ -z "$EXISTING_9100_PID" ]]; then
	echo "Starting iproxy on http://localhost:9100 (MJPEG)"
	iproxy -u "$UDID" 9100 9100 >>/tmp/ios-recorder-iproxy.log 2>&1 &
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

mkdir -p log
LOG_FILE="log/server_$(date +%Y%m%d_%H%M%S).log"
echo "Starting iOS Recorder on http://localhost:8888 (log: $LOG_FILE)"
# Only watch app/ and static/ for reloads — writing to pytest/tests/ or export/ must NOT restart the server
RECORDER_UNIT_TEST="$UNIT_TEST_MODE" RECORDER_XPATH_ONLY="$XPATH_MODE" python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8888 --reload --reload-dir app --reload-dir static 2>&1 | tee "$LOG_FILE"
