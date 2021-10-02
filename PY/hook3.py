import requests
def printData(r, *args, **kwargs):
print(r.text)
s = requests.Session()
s.hooks['response'].append(printData)
s.get('https://jsonplaceholder.typicode.com/users')
