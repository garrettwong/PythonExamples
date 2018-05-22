#!/usr/bin/env python
"""
SysAgent.py
    Lightweight python wrapper to communicate ip address,
    protocol & identifier and identifier metadata,
    group and matching kvps.

    Communicates to the SystemHub master endpoint.

    Also implememts a ping method to return 200 if called.
    On successful registration, the agent shall set itself to
    the ready state from the notready state.

    This means we can send commands.
"""

import time
import json
from http.server import HTTPServer
from SystemDetails import SystemDetails
from HttpRequest import HttpRequest
from HttpServer import MyServer
from Logger import Logger

class SysAgent:
    """SysAgent class"""

    available = False

    def __init__(self):
        self.logger = Logger('SysAgent.log')
        self.system_details = SystemDetails()

        self.logger.log('SysAgent init')

        # get system details
        self.logger.log('Getting System Details')

        json = self.get_system_details()

        # communicate system details
        self.logger.log('Sending System Details JSON: ' + str(json))
        self.send_system_details(json)

        self.available = True

        # start server
        self.logger.log('Success, start server.  Setting state to available.')
        self.start_server()

    def get_system_details(self):
        """creates the system_details object"""

        system_details = {}
        keys = {}
        keys['os'] = self.system_details.getOs()
        keys['ipAddress'] = self.system_details.getIpAddress()
        keys['hostname'] = self.system_details.get_hostname()

        system_details['group'] = 'FIT'
        system_details['identifier'] = keys['hostname'] + str(':9001')
        system_details['ipAddress'] = keys['ipAddress']
        system_details['name'] = keys['hostname']
        system_details['protocol'] = 'http'
        system_details['identifierMetadata'] = {}
        system_details['identifierMetadata']['metadata'] = True

        system_details['matchingDetails'] = keys

        return system_details

    def send_system_details(self, system_details):
        """sends the system details object to the backend server"""

        self.http_request = HttpRequest()
        self.http_request.send_system_details(system_details)

    def start_server(self):
        """starts the web server"""

        hostname = "localhost"
        hostname = self.system_details.get_hostname()
        port = 9001
        print('starting server...')

        self.server = HTTPServer((hostname, port), MyServer)
        print(time.asctime(), "Server Starts - %s:%s" % (hostname, port))

        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            pass

        self.server.server_close()
        print(time.asctime(), "Server Stops - %s:%s" % (hostname, port))


# start
if __name__ == "__main__":
    sys_agent = SysAgent()
    