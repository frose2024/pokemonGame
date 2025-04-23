import requests
import json

def return_pokemon_list():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/')
    pokemon_list = json.loads(response.text)['results']
    name_list = []
    for pokemon in pokemon_list:
        name_list.append(pokemon['name'])
    return name_list

