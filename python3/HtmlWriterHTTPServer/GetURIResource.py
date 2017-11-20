import urllib.request

class GetURIResource:
    def __init__(self):
        self.jqueryUrl = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.js'
        self.vueJsUrl = 'https://cdnjs.cloudflare.com/ajax/libs/vue/2.4.4/vue.js'

    def getJquery(self):
        return self.getUriResponse(self.jqueryUrl)

    def getVueJs(self):
        return self.getUriResponse(self.vueJsUrl)
    
    def getUriResponse(self, url):
        with urllib.request.urlopen(url) as response:
            self.html = response.read()
            return self.html

c = GetURIResource()

res1 = c.getJquery()
res2 = c.getVueJs()

print (res1)
print (res2)