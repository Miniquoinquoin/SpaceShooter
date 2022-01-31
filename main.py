"""Fichier principale du projet"""

import FichiersJeu.Interface.EZ as EZ
# import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
# import FichiersJeu.Interface.Entites.Menu as Menuf
import FichiersJeu.InterfaceDynamique as ID

HAUTEUR = 720
LONGEUR = 1280

EZ.creation_fenetre(LONGEUR, HAUTEUR, "Prototype 1")

ID.menu()

ID.game()

EZ.attendre_action()
EZ.destruction_fenetre()

