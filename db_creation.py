# pokemon database building using python 3

import sqlite3 as sql
import api_manips
import sys
from pathlib import Path

# CONSTANTS
DATA_DIR = Path("data")
DB_NAME = "pkmn.db"
FIRST_PKMN = 1 # change this index if you want to start the database at an other pokemon index and continue onward.

def db_init() -> sql.Connection: # it returns the db connected.
    """
        Connects to database and creates database if it doesn't exist yet.
        Returns the database object.
    """
    # Creates the ./data directory if it doesn't exist, else does nothing.
    DATA_DIR.mkdir(parents=False, exist_ok=True)

    db = sql.connect(DATA_DIR/DB_NAME)
    cursor = db.cursor()

    # Create table if it doesn't exist yet, and name it "pokemon"
    # multi line quoting as we use python to enter orders.
    # yes stats are in french because I play in french
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pkmn_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT, -- item id, each item (pkmn) has a unique id (primary key) that is an integer and that will auto-increment byitself with each new item
            nom TEXT NOT NULL, -- a pkmn has a name.
            pv INTEGER,
            atk INTEGER,
            def INTEGER,
            atkspe INTEGER,
            defspe INTEGER,
            vit INTEGER,
            num INTEGER -- num of said pkmn in the pokedex (mega evolutions and other alt forms will be added later.)
        )'''
    )
    return db

def add_pkmn(_db : sql.Connection, _hp: int, _atk: int, _def: int, _spatk: int, _spdef: int, _spd: int, _name, _num):
    """
        Adds a pokemon in the database.
        in: db which is the database,
            the 6 base stats of a pokemon,
            the pokemon's french name, 
            and its number in the national pokedex.
    """
    cursor = _db.cursor()
    cursor.execute("INSERT INTO pkmn_table(nom, pv, atk, def, atkspe, defspe, vit, num) VALUES (?,?,?,?,?,?,?,?)", (_name, _hp, _atk, _def, _spatk, _spdef, _spd, _num))
    print(f"pokémon {_name} enregistré !\n")

def main():

    print("Connexion à la base de données...")
    db = db_init()

    isLastPkmn = False
    i = FIRST_PKMN
    while not isLastPkmn:
        pkmn = api_manips.api_call(i)
        name = pkmn.name
        stats = pkmn.stats
        # There's a more elegant and pythonic way to write that, 
        # but we'll lose a bit on security if we happen to modify 
        # the pokemonData tuple in the future.
        # name, stats = api_manips.api_call(i)
        
        if name is None or stats is None:
            isLastPkmn = True
        else:
            add_pkmn(db, stats.bhp, stats.batk, stats.bdef, stats.batkspe, stats.bdefspe, stats.bspd, name, i)

            if (i % 100) == 0:
                db.commit() # periodic save, in case the program crashes, so that we don't lose everything.
            i+=1

    print("Sauvegarde de la base de données...")
    db.commit()

    print("Fermeture de la base de données...")
    db.close()
    return 0

if __name__ == "__main__":
    sys.exit(main())



