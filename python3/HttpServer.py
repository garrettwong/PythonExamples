#!/usr/bin/env python
"""
HttpServer.py
"""
import os
from Global import CONFIG
from SendCommand import SendCommand
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from Logger import Logger
from HttpRequest import HttpRequest

class MyServer(BaseHTTPRequestHandler):
    logger = Logger(CONFIG['LogFileName'])

    def _set_headers(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        self.logger.log(self.path)

        o = urlparse(self.path)
        self.logger.log(o)
        lowercase_url = self.path.lower()

        if 'ping' in lowercase_url:
            self.logger.log('ping')

        elif 'sendcommand' in lowercase_url:
            self.logger.log('send command: GET')
            
            #try executing command
            SendCommandManager = SendCommand()
            SendCommandManager.process(self)

            #once command finished, request next command
            #self.request_next_command()

        else:
            self.logger.log('else')

        self._set_headers()
        

    def do_POST(self):
         # Extract and print the contents of the POST
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        
        print(post_data)


        self.logger.log(self.path)

        o = urlparse(self.path)
        self.logger.log(o)
        lowercase_url = self.path.lower()

        if 'sendcommand' in lowercase_url:
            self.send_response(200)
            self.end_headers()


            self.logger.log('send command: POST')
            
            #try executing command
            SendCommandManager = SendCommand()
            SendCommandManager.process_post(self)

            #once command finished, request next command
            #self.request_next_command()
            

        else:
            self.logger.log('else')
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()


    def request_next_command(self):
        print('requesting next command')
        
        self.http_request = HttpRequest()

        # send with system id
        self.http_request.request_next_command(CONFIG['CurrentSystemHostnamePort'])


## usage

# hostName = "localhost"
# hostPort = 9000
# myServer = HTTPServer((hostName, hostPort), MyServer)
# print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

# try:
#     myServer.serve_forever()
# except KeyboardInterrupt:
#     pass

# myServer.server_close()
# print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))