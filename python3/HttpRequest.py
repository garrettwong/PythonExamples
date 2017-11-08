import urllib.request
import urllib.parse
import json
from urllib import request, parse

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
        data = parse.urlencode(systemDetails).encode()
        req =  request.Request('http://localhost/GBase/api/RegisterSystem', data=data) # this will make the method "POST"
        resp = request.urlopen(req)

# main
# if __name__ == "__main__":
#     hr = HttpRequest()
#     nextCommand = hr.getNextCommand()
#     print(nextCommand)
#     for key in nextCommand:
#         print("key: %s , value: %s" % (key, nextCommand[key]))