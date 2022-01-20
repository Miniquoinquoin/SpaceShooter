"""Fichier contenant l'ensemble des partition du jeu menu/game/shop ..."""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
import FichiersJeu.Interface.Entites.Menu as Menuf


HAUTEUR = 720
LONGEUR = 1240

EZ.creation_fenetre(LONGEUR, HAUTEUR, "Prototype 1")
Joueur1 = CJ.Joueur("Bob", 0)
Menu1 = Menuf.Menu(LONGEUR, HAUTEUR)
Joueur1.charge()


def menu():


    play = True
    while play:
        Menu1.displayMenu(Joueur1.chargesAvant)



play = True
while play:
    Menu1.displayMenu(Joueur1.chargesAvant)
    Joueur1.display()
    
    evenement = EZ.recupere_evenement()
    if evenement == "TOUCHE_ENFONCEE":
        if EZ.touche() == "escape":
            play = False

        if EZ.touche() == "d":
            Joueur1.move_info["right"] = True
        
        elif EZ.touche() == "a":  #Detecte en qwerty donc == d
            Joueur1.move_info["left"] = True
    
    elif evenement == "TOUCHE_RELACHEE":
        if EZ.touche() == "d":
            Joueur1.move_info["right"] = False
        
        elif EZ.touche() == "a":    #Detecte en qwerty donc == d
            Joueur1.move_info["left"] = False
            

    EZ.mise_a_jour()
