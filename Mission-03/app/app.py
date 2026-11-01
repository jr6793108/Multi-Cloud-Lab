import json
import os
import socket
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Lock

REQUESTS = {}
DURATIONS = {}
LOCK = Lock()
BUCKETS = (0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10)

def metrics():
    lines = [
        "# HELP mission03_http_requests_total Total HTTP requests",
        "# TYPE mission03_http_requests_total counter",
        "# HELP mission03_http_request_duration_seconds HTTP request duration",
        "# TYPE mission03_http_request_duration_seconds histogram",
    ]
    with LOCK:
        for path, count in sorted(REQUESTS.items()):
            lines.append(
                f'mission03_http_requests_total{{path="{path}"}} {count}'
            )
        for path, values in sorted(DURATIONS.items()):
            for bucket in BUCKETS:
                count = sum(v <= bucket for v in values)
                lines.append(
                    f'mission03_http_request_duration_seconds_bucket'
                    f'{{path="{path}",le="{bucket}"}} {count}'
                )
            lines.append(
                f'mission03_http_request_duration_seconds_bucket'
                f'{{path="{path}",le="+Inf"}} {len(values)}'
            )
            lines.append(
                f'mission03_http_request_duration_seconds_sum'
                f'{{path="{path}"}} {sum(values)}'
            )
            lines.append(
                f'mission03_http_request_duration_seconds_count'
                f'{{path="{path}"}} {len(values)}'
            )
    return ("\n".join(lines) + "\n").encode()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        start = time.monotonic()
        path = self.path.split("?")[0]
        status = 200

        if path == "/":
            body = json.dumps({
                "application": "Multi-Cloud Lab Mission-03",
                "version": os.getenv("APP_VERSION", "1.0"),
                "hostname": socket.gethostname(),
                "status": "running"
            }).encode()
            content_type = "application/json"
        elif path == "/health":
            body = b'{"status":"healthy"}'
            content_type = "application/json"
        elif path == "/metrics":
            body = metrics()
            content_type = "text/plain; version=0.0.4"
        else:
            status = 404
            body = b'{"error":"not found"}'
            content_type = "application/json"

        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

        if path != "/metrics":
            elapsed = time.monotonic() - start
            with LOCK:
                REQUESTS[path] = REQUESTS.get(path, 0) + 1
                DURATIONS.setdefault(path, []).append(elapsed)

if __name__ == "__main__":
    print("Mission-03 application starting on port 8080", flush=True)
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
