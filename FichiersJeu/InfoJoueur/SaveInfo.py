"""Fichier qui Savegarde les Info / File that save Infos"""

import csv

def Save(gold, inventaire):
    """Save parti in InfoGen
    Savegarde la partie dans InfoGen

    Args:
        gold (int): nomber of gold / nombres d'or
        inventaire (dict): stuf of player / inventaire du joueur {Personage1: [Have ?, level, WeaponLevel]}
    """
    with open('FichiersJeu\InfoJoueur\InfoGen.csv', 'w', newline='') as csvfile:
        Writer = csv.writer(csvfile, delimiter=':')
        Writer.writerow(['Gold'] + [str(gold)])

        for key in inventaire:
            Writer.writerow([key] + [inventaire[key][0]] + [inventaire[key][1]] + [inventaire[key][2]])

def SaveGold(gold):
    """Save gold in InfoGen
    Savegarde l'or dans InfoGen

    Args:
        gold (int): nomber of gold / nombres d'or
    """
    with open("FichiersJeu\InfoJoueur\InfoGen.csv", 'r') as csvInfo:
        reader = csv.reader(csvInfo, delimiter=':')
        File = []
        for row in reader:
            if row[0] == 'Gold':
                row[1] = row[1].replace(row[1], str(gold))
                
            File.append(row)
    
    with open("FichiersJeu\InfoJoueur\InfoGen.csv", 'w', newline='') as csvInfo:
        Writer = csv.writer(csvInfo, delimiter=':')
        for row in File:
            Writer.writerow(row)

def BuyCracters(numCaracters):
    """chage etats of Caracters in InfoGen
    Change l'etat des personnages dans InfoGen

    Args:
        numCaracters (int): number of caracters / nombre de personnages
    """
    with open("FichiersJeu\InfoJoueur\InfoGen.csv", 'r') as csvInfo:
        reader = csv.reader(csvInfo, delimiter=':')
        File = []
        for row in reader:
            if row[0] == 'Personnage' + str(numCaracters):
                row[1] = row[1].replace(row[1], "True")
                
            File.append(row)
    
    with open("FichiersJeu\InfoJoueur\InfoGen.csv", 'w', newline='') as csvInfo:
        Writer = csv.writer(csvInfo, delimiter=':')
        for row in File:
            Writer.writerow(row)