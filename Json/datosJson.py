import json
from urllib import request

url = 'https://my.api.mockaroo.com/personas.json?key=e8355070'
response = request.urlopen(url)
#print(response.read())
contenido = response.read()
#print(contenido)
json_obtenido = json.loads(contenido.decode('utf-8'))
#print(json_obtenido)
for persona in json_obtenido:
    print("*************************************")
    print(f"Nombre: {persona['nombre']}")
    print(f"Apellido: {persona['apellido']}")
    print(f"Genero: {persona['genero']}")
    print("*************************************")
    print("\n")
