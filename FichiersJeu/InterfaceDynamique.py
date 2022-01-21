"""Fichier contenant l'ensemble des partition du jeu menu/game/shop ..."""

from telnetlib import GA
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
    EZ.reglage_fps(60)

    while play:
        Menu1.displayMenu(Joueur1.chargesAvant)

        evenement = EZ.recupere_evenement()
        if evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            if 800 < EZ.souris_x() < 1200 and 550 < EZ.souris_y() < 680:
                play = False

        if evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "p":
                if Joueur1.personnage < 8:
                    Joueur1.personnage += 1
                else:
                    Joueur1.personnage = 1
                Joueur1.charge()
                
        
        EZ.mise_a_jour()
        EZ.frame_suivante()

def game():
    EZ.reglage_fps()
    Game = Menuf.Game(LONGEUR, HAUTEUR)
    play = True
    
    while play:
        Game.displayFond(Joueur1.stats["speed"])
        Joueur1.display()
        
        if EZ.clock() - Joueur1.timeSaut >= 1.5: #temps de saut
            Game.move_info["saut"] = False
            Joueur1.move_info["saut"] = False

        evenement = EZ.recupere_evenement()
        if evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                play = False

            if EZ.touche() == "d":
                Joueur1.move_info["right"] = True
                Game.move_info["right"] = True

            
            elif EZ.touche() == "a":  #Detecte en qwerty donc == d
                Joueur1.move_info["left"] = True
                Game.move_info["left"] = True
            
            elif EZ.touche() == "space":
                if EZ.clock() - Joueur1.timeSaut >= 1.5:
                    Joueur1.timer_saut()
                    Game.move_info["saut"] = True
                    Joueur1.move_info["saut"] = True
        
        elif evenement == "TOUCHE_RELACHEE":
            if EZ.touche() == "d":
                Joueur1.move_info["right"] = False
                Game.move_info["right"] = False

            
            elif EZ.touche() == "a":    #Detecte en qwerty donc == d
                Joueur1.move_info["left"] = False
                Game.move_info["left"] = False
                

        EZ.mise_a_jour()
        EZ.frame_suivante()
