# This is a dictionary/hash map that serves as a constant table for stats modifiers
# induced by a pokemon's nature. Of course it is a french table.

# Stats are listed as such:
# "Nature" : {"atk" : coef, "def": coef, "spatk": coef, "spdef": coef, "spd": coef}
# with coef = 0.9 or 1.0 or 1.1 depending of said nature's definition in the game.
NATURE = {
    "Assuré" : {
        "atk" : 0.9,
        "def" : 1.1,
        "spatk" : 1.0,
        "spdef" : 1.0,
        "spd" : 1.0
    },
    "Bizarre" : {
        "atk" : 1.0,
        "def" : 1.0,
        "spatk" : 1.0,
        "spdef" : 1.0,
        "spd" : 1.0
    },
    "Brave" : {
        "atk" : 1.1,
        "def" : 1.0,
        "spatk" : 1.0,
        "spdef" : 1.0,
        "spd" : 0.9
    },
    "Calme" : {
        "atk" : 0.9,
        "def" : 1.0,
        "spatk" : 1.0,
        "spdef" : 1.1,
        "spd" : 1.0
    },
    "Discret" : {
        "atk" : 1.0,
        "def" : 1.0,
        "spatk" : 1.1,
        "spdef" : 1.0,
        "spd" : 0.9
    },
    "Docile" : {
        "atk" : 1.0,
        "def" : 1.0,
        "spatk" : 1.0,
        "spdef" : 1.0,
        "spd" : 1.0
    },
    "Doux" : {
        "atk" : 1.0,
        "def" : 0.9,
        "spatk" : 1.1,
        "spdef" : 1.0,
        "spd" : 1.0
    },
    "Foufou" : {
        "atk" : 1.0,
        "def" : 1.0,
        "spatk" : 1.1,
        "spdef" : 0.9,
        "spd" : 1.0
    },
    "Gentil" : {
        "atk" : 1.0,
        "def" : 0.9,
        "spatk" : 1.0,
        "spdef" : 1.1,
        "spd" : 1.0
    },
    "Hardi" : {
        "atk" : 1.0,
        "def" : 1.0,
        "spatk" : 1.0,
        "spdef" : 1.0,
        "spd" : 1.0
    },
    "Jovial" : {
        "atk" : 1.0,
        "def" : 1.0,
        "spatk" : 0.9,
        "spdef" : 1.0,
        "spd" : 1.1
    },
    "Lâche" : {
        "atk" : 1.0,
        "def" : 1.1,
        "spatk" : 1.0,
        "spdef" : 0.9,
        "spd" : 1.0
    },
    "Malin" : {
        "atk" : 1.0,
        "def" : 1.1,
        "spatk" : 0.9,
        "spdef" : 1.0,
        "spd" : 1.0
    },
    "Malpoli" : {
        "atk" : 1.0,
        "def" : 1.0,
        "spatk" : 1.0,
        "spdef" : 1.1,
        "spd" : 0.9
    },
    "Mauvais" : {
        "atk" : 1.1,
        "def" : 1.0,
        "spatk" : 1.0,
        "spdef" : 0.9,
        "spd" : 1.0
    },
    "Modeste" : {
        "atk" : 0.9,
        "def" : 1.0,
        "spatk" : 1.1,
        "spdef" : 1.0,
        "spd" : 1.0
    },
    "Naïf" : {
        "atk" : 1.0,
        "def" : 1.0,
        "spatk" : 1.0,
        "spdef" : 0.9,
        "spd" : 1.1
    },
    "Pressé" : {
        "atk" : 1.0,
        "def" : 0.9,
        "spatk" : 1.0,
        "spdef" : 1.0,
        "spd" : 1.1
    },
    "Prudent" : {
        "atk" : 1.0,
        "def" : 1.0,
        "spatk" : 0.9,
        "spdef" : 1.1,
        "spd" : 1.0
    },
    "Pudique" : {
        "atk" : 1.0,
        "def" : 1.0,
        "spatk" : 1.0,
        "spdef" : 1.0,
        "spd" : 1.0
    },
    "Relax" : {
        "atk" : 1.0,
        "def" : 1.1,
        "spatk" : 1.0,
        "spdef" : 1.0,
        "spd" : 0.9
    },
    "Rigide" : {
        "atk" : 1.1,
        "def" : 1.0,
        "spatk" : 0.9,
        "spdef" : 1.0,
        "spd" : 1.0
    },
    "Sérieux" : {
        "atk" : 1.0,
        "def" : 1.0,
        "spatk" : 1.0,
        "spdef" : 1.0,
        "spd" : 1.0
    },
    "Solo" : {
        "atk" : 1.1,
        "def" : 0.9,
        "spatk" : 1.0,
        "spdef" : 1.0,
        "spd" : 1.0
    },
    "Timide" : {
        "atk" : 0.9,
        "def" : 1.0,
        "spatk" : 1.0,
        "spdef" : 1.0,
        "spd" : 1.1
    }
}