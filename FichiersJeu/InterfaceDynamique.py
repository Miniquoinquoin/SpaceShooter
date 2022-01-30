"""Fichier contenant l'ensemble des partition du jeu menu/game/shop ..."""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
import FichiersJeu.Interface.Entites.Menu as Menuf
import FichiersJeu.Joueur.Monstres as Monstref


HAUTEUR = 720
LONGEUR = 1240
HAUTEUR_SOL = 604

EZ.creation_fenetre(LONGEUR, HAUTEUR, "Prototype 1")
Joueur1 = CJ.Joueur("Bob", 0)
Menu1 = Menuf.Menu(LONGEUR, HAUTEUR)
Joueur1.charge()
MonstreTest = Monstref.Monstre("Amalgam_Sprite", 5, Joueur1.x)


def menu():


    play = True
    EZ.reglage_fps(60)

    while play:
        Menu1.displayMenu(Joueur1.chargesAvant)

        evenement = EZ.recupere_evenement()
        if evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            if 465 < EZ.souris_x() < 775 and 550 < EZ.souris_y() < 670:
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
        Game.displayFond(Joueur1.stats["acc"],Joueur1.stats["speed"])
        Joueur1.display()
        Joueur1.move_info["speed"] = Game.decalage # Donne la vitesse du joueur generer par le fond a joueur

        MonstreTest.display(Game.decalage)
        
        if not(Joueur1.move_info["saut"]): #temps de saut
            Game.move_info["saut"] = False

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
                if not(Joueur1.move_info["saut"]):
                    Joueur1.timer_saut()
                    Game.move_info["saut"] = True
                    Joueur1.move_info["saut"] = True

            elif EZ.touche() == "return": #Corespond a la touche entre
                Joueur1.shoot()
        
        elif evenement == "TOUCHE_RELACHEE":
            if EZ.touche() == "d":
                Joueur1.move_info["right"] = False
                Game.move_info["right"] = False

            
            elif EZ.touche() == "a":    #Detecte en qwerty donc == d
                Joueur1.move_info["left"] = False
                Game.move_info["left"] = False

        if evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            Joueur1.shoot()
                

        EZ.mise_a_jour()
        EZ.frame_suivante()
