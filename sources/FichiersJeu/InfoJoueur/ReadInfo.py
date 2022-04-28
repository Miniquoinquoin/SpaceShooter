"""Fichier qui li le csv et return les info"""

import csv

def ReadGold():

    with open("FichiersJeu\InfoJoueur\InfoGen.csv", 'r', newline='') as csvInfo:
        reader = csv.reader(csvInfo, delimiter=':')
        for row in reader:
            if row[0] == 'Gold':
                return int(row[1])


def ReadMap():
    """Return the hard map that the player have win
    return la map la plus difficile gagnee"""

    with open("FichiersJeu\InfoJoueur\InfoGen.csv", 'r', newline='') as csvInfo:
        reader = csv.reader(csvInfo, delimiter=':')
        for row in reader:
            if row[0] == 'Map':
                return row[1]

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


def ReadEquipement():
    """Read if the Equipement is buy or not
    li les equipement acheté ou pas"""
    
    equipement =  dict.fromkeys(["Shield", "Grenade", "Potion"], False)
    with open("FichiersJeu\InfoJoueur\InfoGen.csv", 'r', newline='') as csvInfo:
        reader = csv.reader(csvInfo, delimiter=':')
        for row in reader:
            for key in equipement:
                if key in row[0] and row[1] == "True":
                    equipement[key] = True
    
    return equipement



def ReadStatsEquipement():
    """Read the Stats of the Equipement
    li les stats des equipement
    
    return: dict {"name": [numberUpgrade,cooldown,eficiency, BonusRange(%)]}
    """

    statsEquipement = {}
    equipements = ["Shield", "Grenade", "Potion"]
    with open("FichiersJeu\InfoJoueur\InfoGen.csv", 'r', newline='') as csvInfo:
        reader = csv.reader(csvInfo, delimiter=':')
        for row in reader:
            for equipement in equipements:
                if equipement in row[0]:
                    statsEquipement.update({equipement:{"numberUpgrade": int(row[2]), "cooldown": int(row[3]), "eficiency": int(row[4]), "BonusRange": int(row[5]) if equipement == "Grenade" else 0}})
        
    return statsEquipement

