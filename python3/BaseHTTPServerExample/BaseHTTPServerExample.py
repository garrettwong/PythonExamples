#!/usr/bin/env python
"""
    This is a basic example of the HTTPServer
"""

import os
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

### HTTPServerHandler class
class HTTPServerHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        
        print(query_components)
        print('do_GET')
        
        hello = query_components['hello'] 
        print(hello[0])

        self._set_headers()


    def do_POST(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)

        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        
        print('do_POST')
        print(post_data)
        print(post_data.decode())

        dict = json.loads(post_data.decode())

        print(dict['hello'])
        
        for key, value in post_data.items():
            print("%s=%s" % (key, value))


        self._set_headers()


## usage
host_name = "localhost"
port = 9000
server_instance = HTTPServer((host_name, port), HTTPServerHandler)
print(time.asctime(), "Server Starts - %s:%s" % (host_name, port))

try:
    server_instance.serve_forever()
except KeyboardInterrupt:
    pass

server_instance.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (host_name, port))