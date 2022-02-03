"""Fichier contenant l'ensemble des partition du jeu menu/game/shop ..."""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
import FichiersJeu.Interface.Entites.Menu as Menuf
import FichiersJeu.Joueur.Monstres as Monstref
import FichiersJeu.Interface.Decor as Decor
import FichiersJeu.Interface.Entites.ObjetsInterractifs as OI

import random


HAUTEUR = 720
LONGEUR = 1280
HAUTEUR_SOL = 604
TIMER_VAGUE = 2 #en seconde

EZ.creation_fenetre(LONGEUR, HAUTEUR, "Prototype 1")
Joueur1 = CJ.Joueur("Bob", 0)
MenuP = Menuf.MenuPricipale(LONGEUR, HAUTEUR)
MenuD = Menuf.MenuDeath(LONGEUR, HAUTEUR)
MenuG = Menuf.MenuGame(LONGEUR, HAUTEUR)
Border = [OI.Border("border1", -3000, HAUTEUR), OI.Border("border2", LONGEUR + 3000, HAUTEUR)]
Joueur1.charge()


def menu():


    play = True
    EZ.reglage_fps(60)

    while play:
        MenuP.displayMenu(Joueur1.chargesAvant)

        evenement = EZ.recupere_evenement()
        if evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            if 465 < EZ.souris_x() < 775 and 550 < EZ.souris_y() < 670:
                return "Game"

        if evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "p":
                if Joueur1.personnage < 8:
                    Joueur1.personnage += 1
                else:
                    Joueur1.personnage = 1
                Joueur1.charge()
                
        
        EZ.mise_a_jour()
        EZ.frame_suivante()

def menuDeath():

    play = True
    EZ.reglage_fps(60)
    MenuD.displayFond()

    while play:

        evenement = EZ.recupere_evenement()
        if evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            if 480 < EZ.souris_x() < 800 and 260 < EZ.souris_y() < 320:
                return "Game"

            elif 480 < EZ.souris_x() < 800 and 400 < EZ.souris_y() < 460:
                return "Menu"

            elif 480 < EZ.souris_x() < 800 and 540 < EZ.souris_y() < 600:
                EZ.destruction_fenetre()

        if evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return "Menu"
                
        
        EZ.mise_a_jour()
        EZ.frame_suivante()

def menuGame():
    """Fonction du menu en jeux"""

    MenuG.displayFond()

    EZ.reglage_fps(60)
    play = True

    while play:

        evenement = EZ.recupere_evenement()
        if evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            if 480 < EZ.souris_x() < 800 and 260 < EZ.souris_y() < 320:
                return "Run"

            elif 480 < EZ.souris_x() < 800 and 400 < EZ.souris_y() < 460:
                return "Game"

            elif 480 < EZ.souris_x() < 800 and 540 < EZ.souris_y() < 600:
                return "Menu"

        if evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return "Run"
            
    
        EZ.mise_a_jour()
        EZ.frame_suivante()


def Startwave(number):
    """Genere les monstre en début de vague"""

    return [Monstref.Monstre("Amalgam_Sprite", number, Joueur1.x, random.choice([random.randint(-1000, Joueur1.x - 250), random.randint(Joueur1.x + 250, LONGEUR + 1000)])) for monstre in range(5*number)]

def Verifzone(zone1, zone2):
    """Verifie si deux zone se touche

    Args:
        zone1 (objet): premier objet
        zone2 (objet): deuxieme objet

    Returns:
        bool: True si il se touche, sinon False
    """
    return ((zone1.zoneHitBoxlist[0][0] <= zone2.zoneHitBoxlist[0][0] <= zone1.zoneHitBoxlist[1][0]) or (zone1.zoneHitBoxlist[0][0] <= zone2.zoneHitBoxlist[1][0] <= zone1.zoneHitBoxlist[1][0])) and ((zone1.zoneHitBoxlist[0][1] <= zone2.zoneHitBoxlist[0][1] <= zone1.zoneHitBoxlist[3][1]) or (zone1.zoneHitBoxlist[0][1] <= zone2.zoneHitBoxlist[3][1] <= zone1.zoneHitBoxlist[3][1]) ) # verifie si des zonehitbox se touche
    

def VerifDegat(monstres, armes, Joueur):
    """ Fonction qui compare la position des different ellement et mets des degat si nessesaire
    
    Args:
        monstres(list): Liste de tout les monstre en vie
        armes(list): Arme du joueur
    
    """

    # Arme sur monstre
    for i,monstre in enumerate(monstres):
        for arme in armes:
            if Verifzone(monstre, arme["arme"]):
                monstre.domage(arme["arme"].damage["damage"])
                arme["arme"].use()

        if monstre.death():
            monstres.pop(i)

    # Monstres sur Joueur
        if Verifzone(Joueur, monstre):
            if monstre.attaque():
                Joueur.domage(monstre.stats["damage"])
    
    if Joueur.death():
        return monstres, False

    return monstres, True

def VerifContactX(objets, Fondjoueur):
    """Verifie si un objet et un contacte avec le joueur"""

    for objet in objets:
        if (objet.zoneHitBoxlist[0][0] > Fondjoueur.CoordonnerFictive and objet.zoneHitBoxlist[1][0] < Fondjoueur.CoordonnerFictive):
            Fondjoueur.decal += Fondjoueur.decalage


def autoShoot(monstres, joueur):
    """dit au joueur de quel coter il doit tirée quand il est a l'arret"""

    nearMonstre = [LONGEUR + 1001, "right"]

    for monstre in monstres:
        lengtMontre = joueur.x - monstre.x
        if abs(lengtMontre) < nearMonstre[0]:
            if lengtMontre >= 0:
                nearMonstre = [lengtMontre, "left"]

            elif lengtMontre < 0:
                nearMonstre = [-lengtMontre, "right"]
    
    return nearMonstre[1]


def game():
    """Fonction principale du jeux en partie"""
    EZ.reglage_fps()

    Game = Menuf.Game(LONGEUR, HAUTEUR)
    Joueur1.stats["vie"] = Joueur1.stats["maxvie"]

    vague = 0
    MonstreList = [] # List contenant l'ensemble des monstre en vie de la vague
    timeLastWave = [EZ.clock(), True] # [temps a la fin de la vague(0 mob), etats du timer( True = En game, False = Timer en cours)]
    
    inGame = True
    play = True
    while inGame:
        """Boucle avec menu"""
        while play:
            """Boucle pendant que le joueur joue"""
            #Zone de dispaly
            Game.displayFond(Joueur1.stats["acc"],Joueur1.stats["speed"])
            Decor.nombre_kills(LONGEUR - 124, 20, len(MonstreList))
            Joueur1.display()

            #Active l'autoshoot si le joueur ne bouge pas
            if not(Joueur1.move_etat["right"]) and not(Joueur1.move_etat["left"]):
                Joueur1.autoShoot = autoShoot(MonstreList, Joueur1)

            Joueur1.move_info["speed"] = Game.decalage # Donne la vitesse du joueur generer par le fond a joueur
            
            #Affiche tout les monstre de la partie
            for Monstre in MonstreList:
                Monstre.display(Game.decalage)

            #Affiche les Bordur
            for border in Border:
                border.display(Game.CoordonnerFictive + Joueur1.x)


            #verifie les degat entre tout les élement du plateau.
            MonstreList, play = VerifDegat(MonstreList, Joueur1.arme, Joueur1)
            VerifContactX(Border, Game)

            # Lance la prochaine vague
            if len(MonstreList) == 0:
                if timeLastWave[1]: # Permet de verifier si le timer entre vague a déjà été lancer
                    timeLastWave[0] = EZ.clock()
                    timeLastWave[1] = False
                
                if EZ.clock() - timeLastWave[0] >= TIMER_VAGUE:
                    vague += 1
                    MonstreList = Startwave(vague)  # Gener la nouvelle vague
                    timeLastWave[1] = True
            
            #Informe le fond sur l'etat du saut chez le joueur
            if not(Joueur1.move_info["saut"]):
                Game.move_info["saut"] = False
            
            #Donne les ordre en fonction des touche appuiyer
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

        Joueur1.move_info = {"right": False, "left": False, "saut": False, "speed": 0}
        Game.move_info = {"right": False, "left": False, "saut": False, "inertie": 0}
        if not(Joueur1.death()):
            demande = menuGame()
            if demande == "Game":
                return "Game"
            
            elif demande == "Menu":
                return "Menu"

            else:
                play = True

        else:
            Joueur1.display()
            return menuDeath()
            
        
        

