import requests
import json

import api_logic

"""
# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))"""




# User chooses their pokemon from list. Computer is randomly assigned one from list.

    # Show user 20 potential pokemon, let them pick one.

        # If they attempt to pick a invalid pokemon, tell them no, try again.

        # Once valid pokemon is chosen, pass that off the API logic.

    # Computer gets given random pokemon based on API list.
        # num_py.choice list will pick a random item from the list.

        # Save whatever that is at the computer's pokemon.



# API call, retrieve data for computer_pokemon and user_pokemon

    # Retrieved data can be saved in an object, one for the user one for the computer.


# Fight logic - compare some sort of stats?