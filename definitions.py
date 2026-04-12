from typing import NamedTuple
from pathlib import Path

# CONSTANTS
DATA_DIR = Path("data")
DB_NAME = "pkmn.db"
PRECISION = 2 # this is used to set the floating point precision for IVs

# Definitions
class PokemonStats(NamedTuple): # in case I want to add new fields in the future? Also, kinda clearer and somehow more secure...and still efficient.
    """
        A named tuple to store a pokemon's base stats.
    """
    hp: int
    atk: int
    dfs: int
    spatk: int
    spdef: int
    spd: int

class PokemonIVs(NamedTuple):
    """
        A named tuple to store a pokemon's IVs.
        IVs will be calculated "raw" i.e. they will retain their floating point.
    """
    hp: float
    atk: float
    dfs: float
    spatk: float
    spdef: float
    spd: float

class PokemonData(NamedTuple):
    """
        A named tuple to store a pokemon's french name and base stats.
    """
    name: str
    stats: PokemonStats




