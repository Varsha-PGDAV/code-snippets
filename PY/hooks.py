import requests
def printData(r, *args, **kwargs):
   print(r.url)
   print(r.text)
getdata = requests.get('https://jsonplaceholder.typicode.com/users', 
hooks={'response': printData})
