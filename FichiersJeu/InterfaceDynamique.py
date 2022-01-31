"""Fichier contenant l'ensemble des partition du jeu menu/game/shop ..."""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
import FichiersJeu.Interface.Entites.Menu as Menuf
import FichiersJeu.Joueur.Monstres as Monstref
import FichiersJeu.Interface.Decor as Decor

import random


HAUTEUR = 720
LONGEUR = 1280
HAUTEUR_SOL = 604

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

def Startwave(number):
    """Genere les monstre en début de vague"""

    return [Monstref.Monstre("Amalgam_Sprite", 15, Joueur1.x, random.randint(-1000, LONGEUR + 1000)) for monstre in range(5*number)]


def VerifDegat(monstres, armes, Joueur):
    """ Fonction qui compare la position des different ellement et mets des degat si nessesaire
    
    Args:
        monstres(list): Liste de tout les monstre en vie
        armes(list): Arme du joueur
    
    """

    # Arme sur monstre
    for i,monstre in enumerate(monstres):
        for arme in armes:
            if ((monstre.zoneHitBoxlist[0][0] <= arme["arme"].zoneHitBoxlist[0][0] <= monstre.zoneHitBoxlist[1][0]) or (monstre.zoneHitBoxlist[0][0] <= arme["arme"].zoneHitBoxlist[1][0] <= monstre.zoneHitBoxlist[1][0])) and ((monstre.zoneHitBoxlist[0][1] <= arme["arme"].zoneHitBoxlist[0][1] <= monstre.zoneHitBoxlist[3][1]) or (monstre.zoneHitBoxlist[0][1] <= arme["arme"].zoneHitBoxlist[3][1] <= monstre.zoneHitBoxlist[3][1]) ): # verifie si des zonehitbox se touche
                monstre.domage(arme["arme"].damage)
                arme["arme"].use()

        if monstre.death():
            monstres.pop(i)

    # Monstres sur Joueur
    for monstre in monstres:
        if ((Joueur.zoneHitBoxlist[0][0] <= monstre.zoneHitBoxlist[0][0] <= Joueur.zoneHitBoxlist[1][0]) or (Joueur.zoneHitBoxlist[0][0] <= monstre.zoneHitBoxlist[1][0] <= Joueur.zoneHitBoxlist[1][0])) and ((Joueur.zoneHitBoxlist[0][1] <= monstre.zoneHitBoxlist[0][1] <= Joueur.zoneHitBoxlist[3][1]) or (Joueur.zoneHitBoxlist[0][1] <= monstre.zoneHitBoxlist[3][1] <= Joueur.zoneHitBoxlist[3][1]) ): # verifie si des zonehitbox se touche
            if monstre.attaque():
                Joueur.domage(monstre.stats["damage"])
    
    if Joueur.death():
        return monstres, False

    return monstres, True



def game():
    EZ.reglage_fps()
    Game = Menuf.Game(LONGEUR, HAUTEUR)
    play = True
    MonstreList = Startwave(1)
    
    while play:

        #Zone de dispaly
        Game.displayFond(Joueur1.stats["acc"],Joueur1.stats["speed"])
        Decor.nombre_kills(LONGEUR - 124, 20, len(MonstreList))
        Joueur1.display()


        Joueur1.move_info["speed"] = Game.decalage # Donne la vitesse du joueur generer par le fond a joueur

        for Monstre in MonstreList:
            Monstre.display(Game.decalage)

        MonstreList, play = VerifDegat(MonstreList, Joueur1.arme, Joueur1)
        
        
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
    
    EZ.trace_image(EZ.charge_image("FichiersJeu\Interface\Entites\Fond\FondMort2.png"),0, 0)
    EZ.mise_a_jour()
