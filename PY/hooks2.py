import requests
def printRequestedUrl(r, *args, **kwargs):
   print(r.url)
def printData(r, *args, **kwargs):
   print(r.text)
getdata = requests.get('https://jsonplaceholder.typicode.com/users', 
hooks = {'response': [printRequestedUrl, printData]})
