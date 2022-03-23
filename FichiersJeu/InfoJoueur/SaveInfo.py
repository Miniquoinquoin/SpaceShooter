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