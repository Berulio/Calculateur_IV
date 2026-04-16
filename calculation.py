# IV Computing using Python
# Regarding the purpose of this calculator to me i.e. knowing the IVs
# of a pokemon I freshly caught/hatched...
# EVs will have a default value set to 0.
# IVs will also have a set of low and high bounds after computing.

import sqlite3 as sql
import sys
import definitions as df
import Nature
import math


def db_init() -> sql.Connection: # it returns the db connected.
    """
        Connects to database and returns the database object.
    """
    db = sql.connect(df.DATA_DIR/df.DB_NAME)

    return db

def get_base_stat(db: sql.Connection, name: str) -> df.PokemonStats:
    """
        Returns the base stats of a pokemon.
    """
    cursor = db.cursor()
    # request = "SELECT * FROM pkmn_table WHERE nom = ?" # lazy mode, makes future changes more complex though
    request = "SELECT pv, atk, def, atkspe, defspe, vit FROM pkmn_table WHERE nom = ?" 

    cursor.execute(request, [name])
    pkmn = cursor.fetchone()
    # print(pkmn) # debug
    # print(type(pkmn[0]), pkmn[0]) # debug

    return df.PokemonStats(
                hp=pkmn[0],
                atk=pkmn[1],
                dfs=pkmn[2],
                spatk=pkmn[3],
                spdef=pkmn[4],
                spd=pkmn[5]
            )


def calc_IV(bpkmn: df.PokemonStats, pkmn: df.PokemonStats, lvl: int, nat: str) -> df.PokemonIVs:
    """
        Calculate a pokemon IV with its nature taken into account.
    """
    return df.PokemonIVs(
        hp_low=hp_calc_low(lvl, pkmn.hp, bpkmn.hp),
        hp_high=hp_calc_high(lvl, pkmn.hp, bpkmn.hp),
        atk_low=stats_calc_low(lvl, pkmn.atk, bpkmn.atk, float(Nature.NATURE[nat]["atk"])),
        atk_high=stats_calc_high(lvl, pkmn.atk, bpkmn.atk, float(Nature.NATURE[nat]["atk"])),
        dfs_low=stats_calc_low(lvl, pkmn.dfs, bpkmn.dfs, float(Nature.NATURE[nat]["def"])),
        dfs_high=stats_calc_high(lvl, pkmn.dfs, bpkmn.dfs, float(Nature.NATURE[nat]["def"])),
        spatk_low=stats_calc_low(lvl, pkmn.spatk, bpkmn.spatk, float(Nature.NATURE[nat]["spatk"])),
        spatk_high=stats_calc_high(lvl, pkmn.spatk, bpkmn.spatk, float(Nature.NATURE[nat]["spatk"])),
        spdef_low=stats_calc_low(lvl, pkmn.spdef, bpkmn.spdef, float(Nature.NATURE[nat]["spdef"])),
        spdef_high=stats_calc_high(lvl, pkmn.spdef, bpkmn.spdef, float(Nature.NATURE[nat]["spdef"])),
        spd_low=stats_calc_low(lvl, pkmn.spd, bpkmn.spd, float(Nature.NATURE[nat]["spd"])),
        spd_high=stats_calc_high(lvl, pkmn.spd, bpkmn.spd, float(Nature.NATURE[nat]["spd"]))
    )





# There are no magic numbers. These are the actual formulas
def hp_calc_low(lvl: int, hp: int, bhp : int, ev : int = 0) -> int:
    iv = math.ceil((hp-lvl-10)*(100/lvl)-math.floor(ev/4)-(2*bhp))
    return 0 if iv < 0 else (31 if iv > 31 else iv) # one-line version

def hp_calc_high(lvl: int, hp: int, bhp : int, ev : int = 0) -> int:
    iv = math.ceil((hp-lvl-10+1)*(100/lvl)-math.floor(ev/4)-(2*bhp)-1)
    return max(0, min(31, iv)) # min-max version, more readable but less directly understandable.

def stats_calc_low(lvl: int, stat: int, bstat: int, nat : float, ev : int = 0) -> int:
    iv = math.ceil(math.ceil(stat/nat - 5)*100/lvl-math.floor(ev/4)-2*bstat)
    return 0 if iv < 0 else (31 if iv > 31 else iv)

def stats_calc_high(lvl: int, stat: int, bstat: int, nat : float, ev : int = 0) -> int:
    iv =  math.ceil((math.ceil((stat+1)/nat - 6)+1)*100/lvl-math.floor(ev/4)-2*bstat-1)
    return 0 if iv < 0 else (31 if iv > 31 else iv)
    

def main():
    db = db_init()
    get_base_stat(db, "Carapuce")
    db.close()


if __name__ == "__main__":
    sys.exit(main())

