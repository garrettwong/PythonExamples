import urllib.request
import urllib.parse
import json
from urllib import request, parse
import requests

class HttpRequest:
    def getAllDogs(self):
        url = 'https://dog.ceo/api/breeds/list/all'
        f = urllib.request.urlopen(url)
        print(f.read().decode('utf-8'))

    def getNextCommand(self):
        url = 'http://localhost/MAzure/api/AutomationEndpoint'
        f = urllib.request.urlopen(url)
        data = f.read().decode('utf-8')
        return json.loads(data)

    def sendSystemDetails(self, systemDetails):
        print(systemDetails)
        data = parse.urlencode(systemDetails).encode()
        print(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res =  requests.post('http://localhost/GBase/api/RegisterSystem', data=json.dumps(systemDetails), headers=headers) # this will make the method "POST"
        print(res.status_code)
        print(res.json())

# main
# if __name__ == "__main__":
#     hr = HttpRequest()
#     nextCommand = hr.getNextCommand()
#     print(nextCommand)
#     for key in nextCommand:
#         print("key: %s , value: %s" % (key, nextCommand[key]))