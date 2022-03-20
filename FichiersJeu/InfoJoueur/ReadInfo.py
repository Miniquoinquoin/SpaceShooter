"""Fichier qui li le csv et return les info"""

import csv

def ReadGold():

    with open("FichiersJeu\InfoJoueur\InfoGen.csv", 'r', newline='') as csvInfo:
        reader = csv.reader(csvInfo, delimiter=':')
        for row in reader:
            if row[0] == 'Gold':
                return row[1]