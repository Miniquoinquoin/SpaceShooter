"""Fichier contenant l'ensemble des partition du jeu menu/game/shop ..."""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
import FichiersJeu.Interface.Entites.Menu as Menuf
import FichiersJeu.Joueur.Monstres as Monstref
import FichiersJeu.Interface.Decor as Decor
import FichiersJeu.Interface.Entites.ObjetsInterractifs as OI

import csv
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
Border = [OI.Border("border1", -3000), OI.Border("border2", LONGEUR + 3000)]
Joueur1.charge()


def menu():


    play = True
    EZ.reglage_fps(60)

    while play:
        MenuP.displayMenu(Joueur1.chargesAvant)

        evenement = EZ.recupere_evenement()
        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return 0

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            if 465 < EZ.souris_x() < 775 and 550 < EZ.souris_y() < 670:
                return "Game"

        elif evenement == "TOUCHE_ENFONCEE":
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
        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return 0

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            if 480 < EZ.souris_x() < 800 and 260 < EZ.souris_y() < 320:
                return "Game"

            elif 480 < EZ.souris_x() < 800 and 400 < EZ.souris_y() < 460:
                return "Menu"

            elif 480 < EZ.souris_x() < 800 and 540 < EZ.souris_y() < 600:
                EZ.destruction_fenetre()
                return 0

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
        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return 0

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            if 480 < EZ.souris_x() < 800 and 260 < EZ.souris_y() < 320:   #Bouton rejouer
                return "Run"

            elif 480 < EZ.souris_x() < 800 and 400 < EZ.souris_y() < 460:    #Bonton recommencer
                return "Game"

            elif 480 < EZ.souris_x() < 800 and 540 < EZ.souris_y() < 600:    #Bouton Menu principale
                return "Menu"

        elif evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return "Run"
            
    
        EZ.mise_a_jour()
        EZ.frame_suivante()

def genratesMob(name, type = "COMMON"):
    """Genere un mob

    Args:
        name (str): Nom du monstre

    Returns:
        object: le monstre
    """
    
    BaseMonstre = ["Amalgam_Sprite"]
    WizzardMonstre = ["Adept_Sprite"]

    if type == "COMMON":
        if Joueur1.x - 250 <= Border[0].xFictif + Border[0].hitbox[0]:
            return Monstref.Monstre(name, Joueur1.x, random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif)))
        
        elif Joueur1.x + 250 >= Border[1].xFictif:
            return Monstref.Monstre(name, Joueur1.x, random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250))

        return Monstref.Monstre(name, Joueur1.x, random.choice([random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250), random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif))]))

    elif type == "STRENGTH" or type == "HEAL":
        if Joueur1.x - 250 <= Border[0].xFictif + Border[0].hitbox[0]:
            return Monstref.Wizard(name, Joueur1.x, random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif)), type)
        
        elif Joueur1.x + 250 >= Border[1].xFictif:
            return Monstref.Wizard(name, Joueur1.x, random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250), type)

        return Monstref.Wizard(name, Joueur1.x, random.choice([random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250), random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif))]), type)

    elif type == "SHOOTER":
        if Joueur1.x - 250 <= Border[0].xFictif + Border[0].hitbox[0]:
            return Monstref.MonstreShooter(name, Joueur1.x, 250,random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif)))
        
        elif Joueur1.x + 250 >= Border[1].xFictif:
            return Monstref.MonstreShooter(name, Joueur1.x, 250,random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250))

        return Monstref.MonstreShooter(name, Joueur1.x, 250,random.choice([random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250), random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif))]))





def Startwave(number):
    """Genere les monstres en début de vague

    Args:
        number (int): numero de la vague

    Returns:
        list: listMob: tout les mob de la vague , listWizzard: list de tout les sorcier (mob avec effet)
    """

    listMob = []
    listWizzard = []
    listShooter = []

    with open('FichiersJeu/InfoWave/names.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if row[f'type_wave_{number}'] == "COMMON":
                listMob += [genratesMob(row[f'name_wave_{number}'])for monstre in range(int(row[f'number_wave_{number}']))]

            elif row[f'type_wave_{number}'] == "STRENGTH" or row[f'type_wave_{number}'] == "HEAL":
                listWizzard += [genratesMob(row[f'name_wave_{number}'], row[f'type_wave_{number}'])for monstre in range(int(row[f'number_wave_{number}']))]

            elif row[f'type_wave_{number}'] == "SHOOTER":
                listShooter += [genratesMob(row[f'name_wave_{number}'], row[f'type_wave_{number}'])for monstre in range(int(row[f'number_wave_{number}']))]


            # print(row[f'name_wave_{number}'], row[f'number_wave_{number}'], row[f'type_wave_{number}'])
  

    listMob += listWizzard
    listMob += listShooter
    
    return listMob, listWizzard, listShooter

def Verifzone(zone1, zone2):
    """Verifie si deux zone se touche

    Args:
        zone1 (objet): premier objet
        zone2 (objet): deuxieme objet

    Returns:
        bool: True si il se touche, sinon False
    """
    return ((zone1.zoneHitBoxlist[0][0] <= zone2.zoneHitBoxlist[0][0] <= zone1.zoneHitBoxlist[1][0]) or (zone1.zoneHitBoxlist[0][0] <= zone2.zoneHitBoxlist[1][0] <= zone1.zoneHitBoxlist[1][0])) and ((zone1.zoneHitBoxlist[0][1] <= zone2.zoneHitBoxlist[0][1] <= zone1.zoneHitBoxlist[3][1]) or (zone1.zoneHitBoxlist[0][1] <= zone2.zoneHitBoxlist[3][1] <= zone1.zoneHitBoxlist[3][1]) ) # verifie si des zonehitbox se touche

def VerifzonePower(zonePower, zoneMonstre):
    """Verifie si deux zone se touche

    Args:
        zoneMonstre (objet): Monstre qui reçoit l'effet
        zonePower (objet): Sorcier qui done l'effet

    Returns:
        bool: True si il se touche, sinon False
    """
    return ((zonePower.zonePowerlist[0][0] <= zoneMonstre.zoneHitBoxlist[0][0] <= zonePower.zonePowerlist[1][0]) or (zonePower.zonePowerlist[0][0] <= zoneMonstre.zoneHitBoxlist[1][0] <= zonePower.zonePowerlist[1][0])) and ((zonePower.zonePowerlist[0][1] <= zoneMonstre.zoneHitBoxlist[0][1] <= zonePower.zonePowerlist[3][1]) or (zonePower.zonePowerlist[0][1] <= zoneMonstre.zoneHitBoxlist[3][1] <= zonePower.zonePowerlist[3][1]) ) # verifie si des zonePower touche un mob

def getNearSide(zone1, zone2):
    """Donne le coter le plus proche ou zone1 touche zone2

    Args:
        zone1 (objet): objet dont le coter proche sera donner
        zone2 (objet): autre objet
    
    Returns:
        str: Coté le plus proche
    """

    if (zone1.zoneHitBoxlist[1][0] - zone2.zoneHitBoxlist[0][0]) <= zone2.hitbox[0]:
        return "Right"
    
    return "Left"


def VerifDegat(monstres, armesJoueur, Joueur, Shooters = 0):
    """ Fonction qui compare la position des different ellement et mets des degat si nessesaire
    
    Args:
        monstres(list): Liste de tout les monstre en vie
        armes(list): Arme du joueur
    
    """

    # Arme sur monstre
    for i,monstre in enumerate(monstres):
        for arme in armesJoueur:
            if Verifzone(monstre, arme["arme"]):
                monstre.domage(arme["arme"].damage["damage"])
                arme["arme"].use()

        if monstre.death():
            monstres.pop(i)

    # Monstres sur Joueur
        if Verifzone(Joueur, monstre):
            if monstre.attaque():
                Joueur.domage(monstre.stats["damage"]) # Inflige les degat au joueur

    for shooter in Shooters:
        if Verifzone(Joueur, shooter.arme["arme"]):
            Joueur.domage(shooter.arme["arme"].damage["damage"])
            shooter.arme["arme"].use()

    
    if Joueur.death():
        return monstres, False

    return monstres, True

def VerifBuff(wizzards, monstres):
    
    for indiceWizzard, wizzard in enumerate(wizzards):
        
        if wizzard.death():
            wizzards.pop(indiceWizzard)
            continue

        if EZ.clock() >= wizzard.power["cooldown"][0] + wizzard.power["cooldown"][1]:
            for monstre in monstres:
                if VerifzonePower(wizzard, monstre):
                    if wizzard.power["type"] == "HEAL":
                        monstre.heal(wizzard.power["power"])
                    else:
                        monstre.effect["cooldownBoostDamage"][0] = EZ.clock()
    
            wizzard.power["cooldown"][0] = EZ.clock() # Mets a jour le temps du dernier buff
    
    return wizzards


def VerifContactX(objets, Fondjoueur,joueur):
    """Verifie si un objet et un contacte avec le joueur"""
    contact = False
    for objet in objets:
        if Verifzone(objet, joueur):
            coter = getNearSide(joueur, objet)

            #Empeche le joueur d'aller vers l'objet
            if coter == "Right":
                joueur.move_possible["right"] = False
                joueur.move_possible["left"] = True

                Fondjoueur.move_possible["right"] = False
                Fondjoueur.move_possible["left"] = True

            else:
                joueur.move_possible["right"] = True
                joueur.move_possible["left"] = False

                Fondjoueur.move_possible["right"] = True
                Fondjoueur.move_possible["left"] = False
                
            Fondjoueur.contact = True
            contact = True
        
    if not(contact):
        joueur.move_possible["right"] = True
        joueur.move_possible["left"] = True
        
        Fondjoueur.move_possible["right"] = True
        Fondjoueur.move_possible["left"] = True
        Fondjoueur.contact = False

        
            


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
    WizzardList = [] # List contenant l'ensemble des montre a effet
    ShooterList = [] # List contenant l'ensemble des montre qui tire
    timeLastWave = [EZ.clock(), True] # [temps a la fin de la vague(0 mob), etats du timer( True = En game, False = Timer en cours)]
    
    inGame = True
    play = True
    while inGame:
        """Boucle avec menu"""
        while play:
            """Boucle pendant que le joueur joue"""
            #Zone de dispaly
            Game.displayFond(Joueur1.stats["acc"],Joueur1.stats["speed"])

            #Affiche les Bordur
            for border in Border:
                border.display(Game.CoordonnerFictive + Joueur1.x)
            
            #Affiche le nombre de monstre restant
            Decor.nombre_kills(LONGEUR - 124, 20, len(MonstreList))

            #Affiche le joueur et sa vie
            Joueur1.display()

            #Active l'autoshoot si le joueur ne bouge pas
            if not(Joueur1.move_etat["right"]) and not(Joueur1.move_etat["left"]):
                Joueur1.autoShoot = autoShoot(MonstreList, Joueur1)

            Joueur1.move_info["speed"] = Game.decalage # Donne la vitesse du joueur generer par le fond a joueur

            for shooter in ShooterList:
                shooter.move_info["speed"] = Game.decalage # Donne la vitesse du joueur generer par le fond au montre

            
            #Affiche tout les monstre de la partie
            for Monstre in MonstreList:
                Monstre.display(Game.decalage)

            #verifie les degat entre tout les élement du plateau.
            MonstreList, play = VerifDegat(MonstreList, Joueur1.arme, Joueur1, ShooterList)
            VerifContactX(Border, Game, Joueur1)
            WizzardList = VerifBuff(WizzardList, MonstreList)

            # Lance la prochaine vague
            if len(MonstreList) == 0:
                if timeLastWave[1]: # Permet de verifier si le timer entre vague a déjà été lancer
                    timeLastWave[0] = EZ.clock()
                    timeLastWave[1] = False
                
                if EZ.clock() - timeLastWave[0] >= TIMER_VAGUE:
                    MonstreList, WizzardList , ShooterList = Startwave(vague)  # Gener la nouvelle vague
                    timeLastWave[1] = True
                    vague += 1
            
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

            elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
                Joueur1.shoot()

            elif evenement == "EXIT":
                EZ.destruction_fenetre()
                return 0
            
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
            
            elif not(demande):
                return 0

            else:
                play = True

        else:
            Joueur1.display()
            return menuDeath()
            
        
        

