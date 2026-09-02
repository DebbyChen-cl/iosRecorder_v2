#!/usr/bin/env bash
# Prepare the local WDA tunnel for the Jenkins-configured iOS device.
#
# WDA itself is already running on the device. This script creates or reuses
# only the local iproxy tunnel to that exact device; it never starts, stops, or
# replaces device-side WDA.

set -euo pipefail

WDA_UDID="${WDA_UDID:?WDA_UDID must identify the Jenkins target device}"
WDA_LOCAL_PORT="${WDA_LOCAL_PORT:-8100}"
WDA_DEVICE_PORT="${WDA_DEVICE_PORT:-8100}"
WDA_READY_ATTEMPTS="${WDA_READY_ATTEMPTS:-3}"
WDA_REQUEST_TIMEOUT="${WDA_REQUEST_TIMEOUT:-15}"
WDA_RETRY_DELAY="${WDA_RETRY_DELAY:-1}"
WDA_URL="http://127.0.0.1:${WDA_LOCAL_PORT}"
WDA_STATUS_URL="${WDA_URL}/status"
IPROXY_LOG="${IPROXY_LOG:-/tmp/phd-ios-wda-iproxy-${WDA_UDID}.log}"

log() {
    printf '[WDA] %s\n' "$*"
}

fail() {
    log "ERROR: $*"
    exit 1
}

wda_responds() {
    local url="$1"
    curl --fail --silent --show-error \
        --connect-timeout 5 --max-time "$WDA_REQUEST_TIMEOUT" \
        "${url%/}/status" >/dev/null 2>&1
}

wait_for_wda() {
    local url="$1"
    local attempt
    for ((attempt = 1; attempt <= WDA_READY_ATTEMPTS; attempt++)); do
        if wda_responds "$url"; then
            return 0
        fi
        log "WDA readiness probe ${attempt}/${WDA_READY_ATTEMPTS} failed: ${url%/}/status"
        if (( attempt < WDA_READY_ATTEMPTS )); then
            sleep "$WDA_RETRY_DELAY"
        fi
    done
    return 1
}

listener_pid() {
    lsof -tiTCP:"$1" -sTCP:LISTEN 2>/dev/null | head -n 1 || true
}

probe_target_wda() {
    # This is the Recorder's probe pattern, restricted to WDA_UDID. A temporary
    # iproxy tunnel proves that the selected device (not merely any attached
    # device) is running WDA before the Jenkins tunnel is created.
    local probe_port=""
    local candidate probe_pid rc=1
    for candidate in 18100 18101 18102 18103 18104; do
        if [[ -z "$(listener_pid "$candidate")" ]]; then
            probe_port="$candidate"
            break
        fi
    done
    [[ -n "$probe_port" ]] || fail 'No temporary port is available to verify WDA on the configured device'

    iproxy -u "$WDA_UDID" "$probe_port" "$WDA_DEVICE_PORT" >/dev/null 2>&1 &
    probe_pid=$!
    sleep 2
    if wait_for_wda "http://127.0.0.1:${probe_port}"; then
        rc=0
    fi
    # This process belongs only to this short-lived probe; device-side WDA and
    # any pre-existing user tunnel are never terminated.
    kill "$probe_pid" >/dev/null 2>&1 || true
    wait "$probe_pid" 2>/dev/null || true
    return "$rc"
}

command -v curl >/dev/null 2>&1 || fail 'curl is required to verify WDA readiness'
command -v iproxy >/dev/null 2>&1 || fail 'iproxy is required to create the WDA tunnel'
command -v idevice_id >/dev/null 2>&1 || fail 'idevice_id is required to verify the configured device'
command -v lsof >/dev/null 2>&1 || fail 'lsof is required to inspect the WDA tunnel port'

if ! idevice_id -l | grep -Fxq "$WDA_UDID"; then
    fail "Configured WDA device is not connected: ${WDA_UDID}"
fi

existing_pid="$(listener_pid "$WDA_LOCAL_PORT")"
if [[ -n "$existing_pid" ]]; then
    existing_command="$(ps -p "$existing_pid" -o args= 2>/dev/null || true)"
    if [[ "$existing_command" != *iproxy* || "$existing_command" != *"$WDA_UDID"* ]]; then
        fail "Port ${WDA_LOCAL_PORT} is already used by a tunnel/process for a different or unknown device (pid ${existing_pid}: ${existing_command}). It was not changed."
    fi
    if ! wait_for_wda "$WDA_URL"; then
        fail "The existing tunnel on port ${WDA_LOCAL_PORT} targets ${WDA_UDID}, but WDA does not respond. It was not changed."
    fi
    log "Reusing WDA tunnel for configured device ${WDA_UDID} at ${WDA_STATUS_URL}"
    exit 0
fi

log "Verifying WDA on configured device ${WDA_UDID} before creating port ${WDA_LOCAL_PORT}"
if ! probe_target_wda; then
    fail "WDA is not ready on configured device ${WDA_UDID}. Start WebDriverAgent for this device, then rerun Jenkins."
fi

log "Creating iproxy ${WDA_LOCAL_PORT} -> ${WDA_DEVICE_PORT} for configured device ${WDA_UDID}"
nohup iproxy -u "$WDA_UDID" "$WDA_LOCAL_PORT" "$WDA_DEVICE_PORT" >"$IPROXY_LOG" 2>&1 &

if ! wait_for_wda "$WDA_URL"; then
    fail "The new tunnel for ${WDA_UDID} did not become ready at ${WDA_STATUS_URL}. Inspect ${IPROXY_LOG}."
fi

log "WDA is ready for configured device ${WDA_UDID} at ${WDA_STATUS_URL}"
