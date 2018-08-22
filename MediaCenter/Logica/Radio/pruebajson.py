import json


with open('menu.json') as j:
    data = json.load(j)

for item in data['acciones']:
    print(item["accion"])
