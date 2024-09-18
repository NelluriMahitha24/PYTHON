import json
fp=open("data.json","r")
data=json.load(fp)
print(type(data))
print(data)
print(len(data))
