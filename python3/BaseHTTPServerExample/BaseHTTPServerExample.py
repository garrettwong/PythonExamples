#!/usr/bin/env python
"""
    This is a basic example of the HTTPServer
"""

import os
import json
import time
import threading
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


    def other_func(self, post_data):
        print('other func:')
        self.sleep_with_incremental_status(2)

        print(post_data)

        print('decoding')
        self.sleep_with_incremental_status(5)

        print(post_data.decode())
        dict = json.loads(post_data.decode())
        print(dict)
        
        for key, value in dict.items():
            print("%s=%s" % (key, value))

        return

    def sleep_with_incremental_status(self, seconds):
        for i in range(1, seconds+1):
            print(str(i) + ' seconds have elapsed')
            time.sleep(1)

    def do_POST(self):
        print('do_POST')

        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)

        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        
<<<<<<< HEAD
        print('do_POST')
        print(post_data)
        print(post_data.decode())

        dict = json.loads(post_data.decode())

        print(dict['hello'])
        
=======
        bg_thread = threading.Thread(target=self.other_func, args=[post_data])
        bg_thread.start()

>>>>>>> 444a43b2eef618a6e96e0a45ab330450ed57cacd

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