import requests
r = requests.get('https://api.github.com/user', auth=('garrettwong', ''))

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())