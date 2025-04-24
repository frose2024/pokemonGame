import requests
import json
import random

import api_logic
from api_logic import validate_pokemon
import numpy as np
import math
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
# NICK: Print list of pokemon to choose from?; Make sure accuracy and power of moves is not None
def user_pokemon_choice():
    while True:
        user_input = input("Choose your fighter: ").strip().lower()

        if any(char.isdigit() for char in user_input):
            print("Sorry, I do not think that's a real Pokémon. Try again.\n")
            continue

        if not api_logic.validate_pokemon((user_input)):
            print(f"Sorry, I do not think that's a real pokemon. Try again\n")
            show_options = input("Would you like to see some options? (Y/N").strip.lower()

            if show_options == 'y':
                print(computer_pokemon_list.capitalize())
            elif show_options != 'n':
                print("Please answer the question.")
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
player_moves_list = api_logic.return_pokemon_moves(user_pokemon)
computer_moves_list = api_logic.return_pokemon_moves(comp_pokemon)

player_moves_dict = {}
for move in player_moves_list:
    player_moves_dict[move] = api_logic.return_move_stats(move)

computer_moves_dict = {}
for move in computer_moves_list:
    computer_moves_dict[move] = api_logic.return_move_stats(move)

print(player_moves_dict)
print(computer_moves_dict)
# Call the API logic to retrieve the information - so use API call logic to retrieve the stats for the comp
#   pokemon and the user pokemon, store that in a dictionary, pass it to fight logic.

# comp_pokemon_choice(comp_pokemon)
# API call, retrieve data for computer_pokemon and user_pokemon

    # Retrieved data can be saved in an object, one for the user one for the computer.

def damage(move_power,pokemon_attack,enemy_defense):
    damage_dealt = int((pokemon_attack + move_power - enemy_defense) / 10)
    return max(1,damage_dealt)

# Fight logic - compare some sort of stats?

    # Speed highest goes first, first turn.
if combined_stats["player_pokemon"]["speed"] > combined_stats["computer_pokemon"]["speed"]:
    turn = 0
elif combined_stats["computer_pokemon"]["speed"] > combined_stats["player_pokemon"]["speed"]:
    turn = 1
else:
    turn = np.random.choice([0,1])
while combined_stats["player_pokemon"]["hp"] > 0 and combined_stats["computer_pokemon"]["hp"] > 0:
     if turn % 2 == 0:

    # On your turn:
        # Given list of their abilities.
         print(player_moves_list)
        # Choose which ability you want.
            # Check to make sure ability option is valid.
         move = ""
         while move not in player_moves_list:
             move = input("Select move to use: ")
         if np.random.randint(0,100) < player_moves_dict[move]["accuracy"]:
            combined_stats["computer_pokemon"]["hp"] -= damage(player_moves_dict[move]["power"],combined_stats["player_pokemon"]["attack"],combined_stats["computer_pokemon"]["defense"])
            print(f"Hit! Enemy hp: {combined_stats["computer_pokemon"]["hp"]}")
         else:
             print("You missed")
         turn += 1
        # Computer randomly chooses ability from their respective list.
     else:
         enemy_move = np.random.choice(computer_moves_list)
         if np.random.randint(0, 100) < computer_moves_dict[enemy_move]["accuracy"]:
            print(f"Ouch, {enemy_move}!")
            combined_stats["player_pokemon"]["hp"] -= damage(computer_moves_dict[enemy_move]["power"],combined_stats["computer_pokemon"]["attack"],combined_stats["player_pokemon"]["defense"])
            print(f"Your hp : {combined_stats["player_pokemon"]["hp"]}")
         else:
             print(f"{comp_pokemon} misses")
         turn += 1
        # maths - who wins.
if combined_stats["computer_pokemon"]["hp"] <= 0:
    print("You Win!")
else:
    print("You Lose")

