import json
import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            data = {"status": "healthy", "version": "2.0"}
        elif self.path == "/":
            data = {
                "application": "Mission 02 Kubernetes Lab",
                "version": os.getenv("APP_VERSION", "2.0"),
                "hostname": socket.gethostname(),
                "status": "running",
                "deployment": "Kubernetes Rolling Update"
            }
        else:
            self.send_error(404, "Not Found")
            return

        body = json.dumps(data).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
