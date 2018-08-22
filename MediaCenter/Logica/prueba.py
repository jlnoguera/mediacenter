import json
import menu


m = None
m = menu.Menu()

for item in m.Opciones()['actions']:
    print(item['params'])
    print(item['values'])

    