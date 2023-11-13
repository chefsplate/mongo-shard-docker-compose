import pymongo
import subprocess
import os
import time

### --- URL CONNEXION MONGO --- ###
mongodb_uri = 'mongodb://MYUSERNAME:MYPASSWORD@localhost:27018/?authSource=test'
### --- Data for tests --- ###
donnees_eleves = [
    {
        "nom": "Alice",
        "âge": 20,
        "note": "A",
        "matieres": ["Mathematiques", "Science", "Histoire"]
    },
    {
        "nom": "Bob",
        "âge": 22,
        "note": "B",
        "matieres": ["Mathematiques", "Anglais"]
    },
    {
        "nom": "Charlie",
        "âge": 21,
        "note": "A",
        "matieres": ["Science", "Histoire"]
    }
]

try:
     # Connctions Mongo
    client = pymongo.MongoClient(mongodb_uri)

    # Create the collection named 'classe'
    classe = client["classe"]
    eleves = classe.get_collection("eleves")

    # Insert data sample
    eleves.insert_many(donnees_eleves)
    eleves_entrees = eleves.find()
    print("### --- Read collection --- ###")
    for eleve in eleves_entrees:
        print(eleve)
    
    # Update Bob's information
    eleves.update_one({"nom": "Bob"}, { "$set": { "note": "A" } })
    print("### --- Read Bob's information after the update --- ###")
    eleves_apres_update = eleves.find()
    for eleve in eleves_apres_update:
        print(eleve)

    # Get the informations about the shards - sharding
    print("### --- On recupere les informations sur les shards avec la commande sh.status() --- ###")
    informations_shards = client["admin"].command('listShards')
    for shard in informations_shards["shards"]:
        print(shard)
except pymongo.errors.ConnectionFailure as e:
    print(e)
except Exception as e:
    print(e)