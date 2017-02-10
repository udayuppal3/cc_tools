import test_data
import sys
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    games = json_data["games"]
    for game in games:
        platform = test_data.Platform(game["platform"]["name"], game["platform"]["launch year"])
        element = test_data.Game(game["title"], platform, game["year"])
        game_library.add_game(element)
    return game_library

# Handling command line arguments
#  Note: sys.argv is a list of strings that contains each command line argument
#        The first element in the list is always the name of the python file being run
# Command line format: <input json filename>

default_input_json_file = "data/test_data.json"

if len(sys.argv) == 2:
    input_json_file = sys.argv[1]
    print("Using command line args:", input_json_file)
else:
    print("Unknown command line options. Using default values:", default_input_json_file)
    input_json_file = default_input_json_file
with open(input_json_file, 'r') as reader:
    json_data = json.load(reader)

game_library_data = make_game_library_from_json(json_data)
test_data.print_game_library(game_library_data)