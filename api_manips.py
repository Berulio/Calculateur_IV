import requests
import sys
from typing import NamedTuple

# Constants
NAME_URL = "https://pokeapi.co/api/v2/pokemon-species/"
STATS_URL = "https://pokeapi.co/api/v2/pokemon/"

# Definitions
class PokemonStats(NamedTuple): # in case I want to add new fields in the future? Also, kinda clearer and somehow more secure...and still efficient.
    """
        A named tuple to store a pokemon's base stats.
    """
    bhp : int
    batk : int
    bdef : int
    batkspe : int
    bdefspe : int
    bspd : int

class PokemonData(NamedTuple):
    """
        A named tuple to store a pokemon's french name and base stats.
    """
    name: str
    stats: PokemonStats


# functions
def get_french_name(_id: str|int) -> str:
    """
        Takes a pokemon id (name or number in the national pokedex) and returns its french name.
        in: pokemon id as a string (english name) or as an integer (number in the national pokedex)
        out: pokemon's french name as a string.
    """
    if isinstance(_id, int):
        url = NAME_URL + str(_id)
    elif isinstance(_id, str):
        url = NAME_URL + _id
    else:
        raise TypeError("ID has to be an integer or a string.")
    
    try:
        rep = requests.get(url)

        # french name fetching
        if rep.status_code == 200: # 200 is the normal "ok" code. U know the error 404? it is code 404. Yep those are url response codes.
            data = rep.json() # retrieves data that is in json format.
            for entry in data["names"]: # the requests module already has json parsing. So we use it. Very convenient.
                if entry["language"]["name"] == "fr":
                    # print(type(entry["name"]), entry["name"]) # debug
                    return entry["name"]
    except requests.exceptions.HTTPError:
        print("HTTP Error.")
        pass

def get_stats(_id: str|int) -> PokemonStats:
    """
        Takes a pokemon id (name or number in the national pokedex) and returns its base stats.
        in: pokemon id as a string (english name) or as an integer (number in the national pokedex)
        out: A named Tuple containing the pokemon's base stats.
    """
    if isinstance(_id, int):
        url = STATS_URL + str(_id)
    elif isinstance(_id, str):
        url = STATS_URL + _id
    else:
        raise TypeError("ID has to be an integer or a string.")

    try:
        rep = requests.get(url)

        # stats fetching
        if rep.status_code == 200:
            data = rep.json()
            # using a dictionnary for performance and security.
            raw_data = {entry["stat"]["name"]:entry["base_stat"] for entry in data["stats"]}
            # print(raw_data) # debug
            return PokemonStats(
                bhp=raw_data["hp"],
                batk=raw_data["attack"],
                bdef=raw_data["defense"],
                batkspe=raw_data["special-attack"],
                bdefspe=raw_data["special-defense"],
                bspd=raw_data["speed"]
            )
    except requests.exceptions.HTTPError:
        print("HTTP Error.")
        pass

def api_call(_id) -> PokemonData:
    """
        api_call() will call the function get_french_name and get_stats, then returns
        a named tuple with fields matching the correct data fetched from pokeapi.
        Said data are the pokemon's french name and its base stats.
    """
    pkmn_name = get_french_name(_id)
    pkmn_stats = get_stats(_id)
    return PokemonData(name=pkmn_name, stats=pkmn_stats)

# Main code
def main():
    # used for testing purposes
    pkmn_01 = api_call("bulbasaur")
    print(pkmn_01.name, pkmn_01.stats)
    pkmn_04 = api_call(4)
    print(pkmn_04.name, pkmn_04.stats)
    pkmn = api_call(1026) # should not exist, debug purposes
    print(type(pkmn.name), type(pkmn.stats), pkmn)
    return 0

if __name__ == "__main__":
    sys.exit(main())
