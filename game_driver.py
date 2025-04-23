import requests
import json

import api_logic
from api_logic import return_pokemon_list

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


# Call pokemon_return_list first, keep list.
computer_pokemon_list = return_pokemon_list()

# Pokemon choosing function - user gives a string as a pokemon name, pass it to API.
    # User input picks a pokemon.
    # Passes it to API call as argument.

        # If valid, save it was user_pokemon
            # Assuming no pokemons contain numbers in their name, can use isDigit() as one check.

        # If not valid, tell user they chose a fake pokemon and that they need to try again.


    # Pass to API logic as user_pokemon_name


    # Computer gets given random pokemon based on API list.
        # List of computer choices is saved as computer_pokemon_list

            # num_py.choice list will pick a random item from the list.

            # Save whatever that is at the computer's pokemon.

            # Pass to API logic as comp_pokemon_name



# API call, retrieve data for computer_pokemon and user_pokemon

    # Retrieved data can be saved in an object, one for the user one for the computer.


# Fight logic - compare some sort of stats?

    # Speed highest goes first, first turn.

    # On your turn:
        # Given list of their abilities.

        # Choose which ability you want.
            # Check to make sure ability option is valid.

        # Computer randomly chooses ability from their respective list.

        # maths - who wins.

        # Subtraction of health, call HP check???

    # HP checking function, called at end of fight round.
        # Damage done to the pokemon is passed by the fight_round logic.

        # Checks to make sure if either pokemon is ded.

            # If no one ded, call fight round again. Repeat process.

            # If someone ded, either user wins or computer wins.

