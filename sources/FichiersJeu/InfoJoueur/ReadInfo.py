"""Fichier qui li le csv et return les info"""

import csv

def ReadGold():

    with open("FichiersJeu\InfoJoueur\InfoGen.csv", 'r', newline='') as csvInfo:
        reader = csv.reader(csvInfo, delimiter=':')
        for row in reader:
            if row[0] == 'Gold':
                return int(row[1])


def ReadStatsPlayers():
    """Read the stats of Caracterse
    li les stats des personnage
    """

    StatsPlayers = []
    with open("FichiersJeu\InfoJoueur\StatsPersonnages.csv", 'r', newline='') as csvStat:
        reader = csv.DictReader(csvStat, delimiter=';')
        for row in reader:
            if "Stats" in row['Personages']:
                StatsPersonnage = { "name": row['name'], "price": int(row['price']) ,"vie": int(row['vie']), 
                    "regen": {"timer": 0, "cooldown": int(row['regenCooldown']), "eficiency": float(row['regenEficiency']) },
                    "weapon": {"name": row['weaponName'], "price": int(row['WeaponPrice']), "damage": int(row['damage']), "range": int(row['range']) , "durability": int(row['durability']), "cooldown": float(row['rechargeTime']), "speed": int(row['weaponSpeed']) },
                    "acc": float(row['acceleration']),"speed": int(row['speed']), "jumpPower": float(row['jumpPower']),  "maxvie": int(row['vie']) }
                StatsPlayers.append(StatsPersonnage)
            
    return StatsPlayers

def ReadUpStatsPlayers():
    """Read the Upgrade Stats of Caracters
    li les stats d'amelioration des personnage"""
    
    UpStatsPlayers = []
    with open("FichiersJeu\InfoJoueur\StatsPersonnages.csv", 'r', newline='') as csvStat:
        reader = csv.DictReader(csvStat, delimiter=';')
        for row in reader:
            if "Up" in row['Personages']:
                StatsPersonnage = { "name": row['name'], "price": int(row['price']) ,"vie": int(row['vie']), 
                    "regen": {"timer": 0, "cooldown": float(row['regenCooldown']), "eficiency": float(row['regenEficiency']) },
                    "weapon": {"name": row['weaponName'], "price": int(row['WeaponPrice']), "damage": float(row['damage']), "range": int(row['range']) , "durability": int(row['durability']), "cooldown": float(row['rechargeTime']), "speed": float(row['weaponSpeed']) },
                    "acc": float(row['acceleration']),"speed": float(row['speed']), "jumpPower": float(row['jumpPower']),  "maxvie": int(row['vie']) }
                UpStatsPlayers.append(StatsPersonnage)
            
    return UpStatsPlayers
    


def ReadInventaire():
    """Read the level of the Cracters and Caracters Weapons
    li les niveau des personnage et des armes"""

    inventaire = {}
    with open("FichiersJeu\InfoJoueur\InfoGen.csv", 'r', newline='') as csvInfo:
        reader = csv.reader(csvInfo, delimiter=':')
        for row in reader:
            if "Personnage" in row[0]:
                inventaire.update({row[0]:[ True if row[1] == "True" else False, int(row[2]), int(row[3])]})

    return inventaire

