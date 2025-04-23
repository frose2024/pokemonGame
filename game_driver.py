import requests
import json
import random

import api_logic
from api_logic import validate_pokemon

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
computer_pokemon_list = api_logic.return_pokemon_list()
user_pokemon = " "
comp_pokemon = " "


# Pokemon choosing function - user gives a string as a pokemon name, pass it to API.
def user_pokemon_choice():
    while True:
        user_input = input("Choose your fighter: ").strip().lower()

        if any(char.isdigit() for char in user_input):
            print("Sorry, I do not think that's a real Pokémon. Try again.\n")
            continue

        if not api_logic.validate_pokemon((user_input)):
            print(f"Sorry, I do not think that's a real pokemon. Try again\n")
            continue

        print(f"You chose '{user_input.capitalize()}'!")
        return user_input

# Computer randomly selects from the official list
def comp_pokemon_choice(pokemon_list):
    comp_choice = random.choice(pokemon_list)
    print(f"The computer chose '{comp_choice.capitalize()}'!")
    return comp_choice


user_pokemon = user_pokemon_choice()
comp_pokemon = comp_pokemon_choice(computer_pokemon_list)

# Combine as one dictionary. user_pokemon is first key, comp_pokemon is second key
user_stats = api_logic.return_pokemon_dict(user_pokemon)
comp_stats = api_logic.return_pokemon_dict(comp_pokemon)

combined_stats = {
    "player_pokemon": user_stats,
    "computer_pokemon": comp_stats
}

# List of moves dictionary for both pokemon.

print(combined_stats)
# Call the API logic to retrieve the information - so use API call logic to retrieve the stats for the comp
#   pokemon and the user pokemon, store that in a dictionary, pass it to fight logic.

# comp_pokemon_choice(comp_pokemon)
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

