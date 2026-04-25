#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            data = {"status": "OK"}

            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            error = {"error": "Endpoint not found"}

            self.wfile.write(json.dumps(error).encode())


# SERVER START
server = HTTPServer(("localhost", 8000), MyHandler)

print("Server running on http://localhost:8000")
server.serve_forever()
