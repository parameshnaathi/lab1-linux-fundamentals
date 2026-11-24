from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import os
import time

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"UP")

        elif self.path == "/info":
            response = f"""
ARRISE Linux Lab
Hostname: {socket.gethostname()}
PID: {os.getpid()}
Status: Running
"""
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response.encode())

        elif self.path == "/slow":
            time.sleep(5)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Slow request completed")

        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ARRISE DevOps Lab")

server = HTTPServer(("127.0.0.1", 8080), Handler)

print("ARRISE Lab listening on port 8080", flush=True)

server.serve_forever()