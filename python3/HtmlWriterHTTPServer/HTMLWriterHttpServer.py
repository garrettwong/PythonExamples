#!/usr/bin/env python
"""
HttpServer.py
"""
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from HtmlWriter import HtmlWriter
from HtmlWriterHttpRequest import HtmlWriterHttpRequest

class HTMLWriterHttpServer(BaseHTTPRequestHandler):
    htmlWriter = HtmlWriter()

    def do_GET(self):
        self.htmlWriter.writeHtml(self.wfile, self.path)
        
        o = urlparse(self.path)
        self.logger.log(o)
        lowercase_url = self.path.lower()

        self.send_response(200)
        self.end_headers()

        

    def do_POST(self):
         # Extract and print the contents of the POST
        length = int(self.headers['Content-Length'])
        post_data = parse_qs(self.rfile.read(length).decode('utf-8'))
        print(post_data)
        for key, value in post_data.items():
            print("%s=%s" % (key, value))


        self.data_string = self.rfile.read(int(self.headers['Content-Length']))


        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()


        data = simplejson.loads(self.data_string)
        with open("test123456.json", "w") as outfile:
            simplejson.dump(data, outfile)
        print ({}.format(data))
        f = open("for_presen.py")
        self.wfile.write(f.read())


## usage

hostName = "localhost"
hostPort = 9000
myServer = HTTPServer((hostName, hostPort), HTMLWriterHttpServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))