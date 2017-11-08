# Slave.py
#
#   This file is responsible for communicating basic SystemDetails and setting up a web server
#
#
from SystemDetails import SystemDetails
from HttpRequest import HttpRequest
from HttpServer import MyServer
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class Slave:
    def __init__(self):
        self.systemDetails = SystemDetails()

        print(self.systemDetails.getHostname())

        # get system details
        json = {}
        json['os'] = self.systemDetails.getOs()
        json['ipAddress'] = self.systemDetails.getIpAddress()
        json['hostname'] = self.systemDetails.getHostname()

        # communicate system details
        self.sendJson(json)

        # start server
        self.startServer()

    # sends json
    def sendJson(self, json):
        self.httpRequest = HttpRequest()
        self.httpRequest.sendSystemDetails(json)

    # starts the web server
    def startServer(self):
        hostname = "localhost"
        port = 9001
        print('starting ser')

        self.myServer = HTTPServer((hostname, port), MyServer)
        print(time.asctime(), "Server Starts - %s:%s" % (hostname, port))

        try:
            self.myServer.serve_forever()
        except KeyboardInterrupt:
            pass

        self.myServer.server_close()
        print(time.asctime(), "Server Stops - %s:%s" % (hostname, port))


# start
slaveInstance = Slave()