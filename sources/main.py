"""Fichier principale du projet"""

import FichiersJeu.Interface.EZ as EZ
# import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
# import FichiersJeu.Interface.Entites.Menu as Menuf 
import FichiersJeu.InterfaceDynamique as ID

#Csv
import FichiersJeu.InfoJoueur.ReadInfo as Reader
import FichiersJeu.InfoJoueur.SaveInfo as Writer

HAUTEUR = 720
LONGEUR = 1280

EZ.creation_fenetre(LONGEUR, HAUTEUR, "Space Shooter", "FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A1.png")

def Shooter():
    inventaire = Reader.ReadInventaire()  
    gold = Reader.ReadGold() # Read gold from csv InfoGen / li l'or depuis le fichier InfoGen

    demande = "Menu"
    play = True
    while play:

        if demande == "Menu":
            demande, infoGame = ID.menu(gold, inventaire)
           
        gold = int(Reader.ReadGold()) # Read gold from csv InfoGen / li l'or depuis le fichier InfoGen
            
        if demande == "Game":
            demande = ID.game(infoGame['map'], infoGame['mode'])


        if not(demande):
            break

Shooter()


