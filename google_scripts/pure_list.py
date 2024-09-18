import json

with open("url_remove.json","r") as file:
    data = json.load(file)
data = [i['productUrl'] for i in data]
with open("urls_only.json","w") as file:
    json.dump(data,file)