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
    hp: int = -1
    atk: int = -1
    dfs: int = -1
    spatk: int = -1
    spdef: int = -1
    spd: int = -1

class PokemonIVs(NamedTuple):
    """
        A named tuple to store a pokemon's IV intervals.
        IVs will have a low/high range.
    """
    hp_low: int = -1
    hp_high: int = -1
    atk_low: int = -1
    atk_high: int = -1
    dfs_low: int = -1
    dfs_high: int = -1
    spatk_low: int = -1
    spatk_high: int = -1
    spdef_low: int = -1
    spdef_high: int = -1
    spd_low: int = -1
    spd_high: int = -1

# this class might be used on a further update.
class PokemonData(NamedTuple):
    """
        A named tuple to store a pokemon's french name and base stats.
    """
    name: str
    stats: PokemonStats




