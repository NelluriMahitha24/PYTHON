import requests
data=requests.get('https://dummyjson.com/users')
users=data.json()
print(type(data))
print(type(data.json()))