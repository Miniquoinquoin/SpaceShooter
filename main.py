"""Fichier principale du projet"""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ

HAUTEUR = 720
LONGEUR = 1240

EZ.creation_fenetre(LONGEUR, HAUTEUR, "Prototype 1")
Joueur1 = CJ.Joueur("Bob", 0)


play = True
while play:
    EZ.trace_rectangle_droit(0, 0, LONGEUR, HAUTEUR)
    Joueur1.display()
    
    evenement = EZ.recupere_evenement()
    if evenement == "TOUCHE_ENFONCEE":
        if EZ.touche() == "s":
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

EZ.attendre_action()
EZ.destruction_fenetre()


