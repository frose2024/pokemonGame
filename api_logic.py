import requests
import json

stats_list = ["hp", "attack", "defense", "special-attack", "special-defense", "speed"]

def return_pokemon_list():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/')
    pokemon_list = json.loads(response.text)['results']
    name_list = []
    for pokemon in pokemon_list:
        name_list.append(pokemon['name'])
    return name_list

def validate_pokemon(name: str):
    try:
        response = requests.get('https://pokeapi.co/api/v2/pokemon/' + name.lower())
        json.loads(response.text)
        return True
    except:
        return False

def return_pokemon_stat(name: str, stat : str):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + name.lower())
    pokemon = json.loads(response.text)
    return pokemon[stat]

def return_pokemon_deeper_stat(name: str, stat: str):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + name.lower())
    pokemon = json.loads(response.text)
    stats = pokemon["stats"]
    return stats[stats_list.index(stat)]["base_stat"]

def return_pokemon_dict(name: str):
    name = name.lower()
    dict = {
        "name": name,
        "speed": return_pokemon_deeper_stat(name, "speed"),
        "hp": return_pokemon_deeper_stat(name, "hp"),
        "attack": return_pokemon_deeper_stat(name, "attack"),
        "defense": return_pokemon_deeper_stat(name, "defense"),
    }
    return dict

def return_pokemon_moves(name: str):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + name.lower())
    pokemon = json.loads(response.text)
    full_moves = pokemon["moves"]
    moves = []
    for move in full_moves:
        if len(moves) < 5:
            moves.append(move["move"]["name"])
    return moves

def return_move_stats(name: str):
    response = requests.get('https://pokeapi.co/api/v2/move/' + name.lower())
    move_stats = json.loads(response.text)
    move = {
        "accuracy": move_stats["accuracy"],
        "power": move_stats["power"]
    }
    return move

def output_api_call(call):
    print(json.dumps(call, indent=4))