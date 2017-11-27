
import json
import urllib.request
import urllib.parse
import os

from urllib.parse import urlparse
from Global import CONFIG
from subprocess import Popen, PIPE, STDOUT

class SendCommand:
    def __init__(self):
        if os.name == 'nt':
            self.log_path = 'C:\Temp\sendcommand.log'
            self.cwd = r'C:\Temp'
        else:
            self.log_path = '/tmp/sendcommand.log'
            self.cwd = r'/root/l'
        
    def parse_command(self, server):
        query = urlparse(server.path).query
        print('query : ' + query)
        query_components = dict(qc.split('=') for qc in query.split('&'))
        cmd = query_components['command']
        print('cmd : ' + cmd)
        return cmd
     
    def get_command_with_args_from_command_object(self, command):
        args = ''

        formatted_command = command + ' ' + args
        return formatted_command

    def parse_post_command(self, server):
        print('parse_post_command: ' + str(server))

        # Extract and print the contents of the POST
        content_len = int(server.headers['content-length'])
        post_body = server.rfile.read(content_len)

        data = json.loads(post_body)   
        print(data)

        return data

    def get_post_command_with_args(self, command):
        commandText = ''
        args = ''
        
        print(type(command))

        if command['CommandText'] is not None:
            commandText = command['CommandText']
        
        if command['Args'] is not None:
            args = command['Args']

        formatted_command = commandText + ' ' + args
        return formatted_command

    def execute_command(self, command_with_args):
        p = Popen(command_with_args, stdout=PIPE, stderr=PIPE, shell=True, cwd=self.cwd)
        output = p.communicate()

        with open((self.log_path),'a') as outf: outf.write(str(output) + "\n")

        if p.returncode != 0:
            print("Fail")
            with open((self.log_path),'a') as outf: outf.write(str("Fail") + "\n")
        else:
            print("Pass")
            with open((self.log_path),'a') as outf: outf.write(str("Pass") + "\n")

        return output
    
    def get_uri_response(self, url):
        print(url)
        with urllib.request.urlopen(url) as response:
            self.html = response.read()
            return self.html

    def process(self, server):
        command = self.parse_command(server)
        print(command)

        command_with_args = self.get_command_with_args_from_command_object(command)
            
        print("Running Command ", str(command_with_args))

        output = self.execute_command(command_with_args)
        print(output)

        # test_run_id = 2927366
        # response = self.get_uri_response("http://garrett.labspan.wdc.com/PRVX/api/TestRun/" + str(test_run_id) + "/GetNextCommand")
        # print(response)


    def process_post(self, server):
        command = self.parse_post_command(server)
        print(command)
        print(type(command))

        command_with_args = self.get_post_command_with_args(command)

        output = self.execute_command(command_with_args)
        print(output)
        