#!/usr/bin/env python3

import http.server
import socketserver
import json

PORT = 8000
data = {"name": "John", "age": 30, "city": "New York"}
info = {"version": "1.0", "description": "A simple API built with http.server"}
json_data = json.dumps(data)
json_info = json.dumps(info)

class my_server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json_data, "utf-8"))
        elif self.path == "/status":
            self.send_response(200)
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json_info, "utf-8"))

        else:
            self.send_response(404)
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("404: Endpoint not found", "utf-8"))

with socketserver.TCPServer(("", PORT), my_server) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
