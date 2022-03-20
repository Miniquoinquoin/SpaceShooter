"""Fichier qui Savegarde les Info / File that save Infos"""

import csv

def Save(gold):
    with open('FichiersJeu\InfoJoueur\InfoGen.csv', 'w', newline='') as csvfile:
        Writer = csv.writer(csvfile, delimiter=':')
        Writer.writerow(['Gold'] + [str(gold)])