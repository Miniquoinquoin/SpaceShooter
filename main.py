"""Fichier principale du projet"""

from ctypes import sizeof
import FichiersJeu.Interface.EZ as EZ
# import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
# import FichiersJeu.Interface.Entites.Menu as Menuf
import FichiersJeu.InterfaceDynamique as ID

HAUTEUR = 720
LONGEUR = 1280

EZ.creation_fenetre(LONGEUR, HAUTEUR, "Prototype 1")

def Shooter():


    demande = ID.menu()
    play = True
    while play:

        if demande == "Menu":
            demande = ID.menu()
            
        if demande == "Game":
            demande = ID.game()

Shooter()

EZ.attendre_action()
EZ.destruction_fenetre()
