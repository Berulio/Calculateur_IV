## IV_Calculator

# Requirements:
- Python 3
- Requests library
- Pyside 6 library

# Optional:
- Kode Mono Font




French Version:
Un calculateur d'IV qui fonctionne hors ligne (sauf pour l'initialisation).

Les données des pokémons sont stockées localement sous ./data/pkmn.db
Le script db_creation.py fait appel à l'API PokeAPI pour remplir la base données.
Les noms des pokémons seront en français, et leurs stats de base seront celles depuis la 3ème génération, ce qui veut dire que ce calculateur d'IV ne fonctionnera PAS sur les jeux de la première et deuxième génération (car le système d'IV et les stats étaient différentes).
Il n'y a pour le moment aucune prise en charge des Méga-évolutions ou autres formes spéciales.
Il n'y a pas de prise en charge des EVs non plus pour l'instant.
Ce calculateur sert pour le moment à évaluer les pokémons que l'on vient tout juste de capturer ou de faire éclore (quand leurs EVs sont à zéro).

# Utilisation
1. Création de la base de données. (si vous avez déjà la base de données, passez à l'étape 2)
Il faut lancer db_creation.py et attendre. C'est la seule étape qui nécessite internet. (il faudra voir dans le futur si j'upload la base de données pour une utilisation 100% hors ligne...)

2. Pour utiliser le calculateur, c'est gui.py qu'il faut lancer. 



-----

English Version:
An offline IV Calculator project (except to create the database)

The first scripts fills a database stored locally under ./data/pkmm.db
It uses PokeAPI to fill the database in.
Pokemons' names will be stored in French, with their base stats since gen 3. (No there won't be English names. There are already plenty of English IV calculators.)
--> Meaning this calculator won't work on Gen 1 and Gen 2 games.
No alternative forms or special forms are supported yet (and I don't think I would implement those in the future).
No EVs are taken into account yet. For the moment this calculator serves to evaluate pokemons freshly caught or hatched.

# Usage
1. You must have a database containing all the pokemon base stats. To create this database, use the script db_creation.py. It might take a while to fetch every pokemon but then you won't need to do that, unless there's a need to update the database. For this sole step you'll need a connection to the internet. If you already have the database, you can skip this step.

2. To use the calculator, you must run gui.py.


