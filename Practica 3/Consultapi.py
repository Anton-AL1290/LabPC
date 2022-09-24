import requests
import json
#request a Star Wars Api
req = requests.get('https://swapi.dev/api/people/4')

response = json.loads(req.content)

print("El resultado a la consulta de Swapi fue: " + response['name'])

#request a PokeApi
poke = requests.get('https://www.pokeapi.co/api/v2/pokemon/bulbasaur')

respuesta = json.loads(poke.content)
print("El mejor pokemon es: " + respuesta['name'])
