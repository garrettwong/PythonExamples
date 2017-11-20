#!/usr/bin/env python
"""
HttpServer.py

https://wiki.python.org/moin/BaseHttpServer
"""
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from http.server import HTTPServer

from HtmlWriter import HtmlWriter
from HtmlWriterHttpRequest import HtmlWriterHttpRequest

class HTMLWriterHttpServer(BaseHTTPRequestHandler):
    htmlWriter = HtmlWriter()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.htmlWriter.writeHtml(self.wfile, self.path)
        



## usage

hostName = "localhost"
hostPort = 9000
myServer = HTTPServer((hostName, hostPort), HTMLWriterHttpServer)

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()