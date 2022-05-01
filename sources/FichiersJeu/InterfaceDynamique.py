"""Fichier contenant l'ensemble des partition du jeu menu/game/shop ..."""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
import FichiersJeu.Interface.Entites.Menu as Menuf
import FichiersJeu.Joueur.Monstres as Monstref
import FichiersJeu.Interface.Decor as Decor
import FichiersJeu.Interface.Entites.ObjetsInterractifs as OI

import FichiersJeu.InfoJoueur.ReadInfo as Reader
import FichiersJeu.InfoJoueur.SaveInfo as Writer

import Outiles.PerfCompteur as Perfcompteur
Perfcompt = Perfcompteur.TimeDistribution()


import csv
import random


HAUTEUR = 720
LONGEUR = 1280
TIMER_VAGUE = 2 #en seconde

ZOOM_CARTE = 0.5

PRIX_EQUIPEMENT = {"Shield": 10000, "Grenade": 2500, "Potion": 5000} # price of the different equipement / prix des differents equipements


"""Part of the start load
Partie du chargement de la partie"""

EZ.creation_fenetre(LONGEUR, HAUTEUR, "Chargement")
Decor.FondChargement(LONGEUR,HAUTEUR)

# Joueur

TAILLE_BARRE_DE_CHARGEMENT = (LONGEUR//2, HAUTEUR//6)
COORDONNEES_BARRE_DE_CHARGEMENT = (LONGEUR//2 - TAILLE_BARRE_DE_CHARGEMENT[0]//2, 2 * HAUTEUR//3 - TAILLE_BARRE_DE_CHARGEMENT[1]//2)

Decor.bareDechargement(COORDONNEES_BARRE_DE_CHARGEMENT[0], COORDONNEES_BARRE_DE_CHARGEMENT[1], 
                        TAILLE_BARRE_DE_CHARGEMENT[0],TAILLE_BARRE_DE_CHARGEMENT[1], 0)
Joueur1 = CJ.Joueur("Bob",0,)

Decor.bareDechargement(COORDONNEES_BARRE_DE_CHARGEMENT[0], COORDONNEES_BARRE_DE_CHARGEMENT[1], 
                        TAILLE_BARRE_DE_CHARGEMENT[0],TAILLE_BARRE_DE_CHARGEMENT[1], 10)

# Menu de selection
MenuP = Menuf.MenuPricipale(LONGEUR, HAUTEUR)
MenuPerso = Menuf.Personnages(LONGEUR, HAUTEUR, "Personnages")

MenuMode = Menuf.Mode(LONGEUR, HAUTEUR, "Mode")
MenuMap = Menuf.Infini(LONGEUR, HAUTEUR, "Map") # Menu to choice the map of the game in infini mode

Decor.bareDechargement(COORDONNEES_BARRE_DE_CHARGEMENT[0], COORDONNEES_BARRE_DE_CHARGEMENT[1], 
                        TAILLE_BARRE_DE_CHARGEMENT[0],TAILLE_BARRE_DE_CHARGEMENT[1], 30)

MenuCarte = Menuf.MenuMap(LONGEUR, HAUTEUR, ZOOM_CARTE) # Menu to choice the map of the game in campagne mode

Decor.bareDechargement(COORDONNEES_BARRE_DE_CHARGEMENT[0], COORDONNEES_BARRE_DE_CHARGEMENT[1], 
                        TAILLE_BARRE_DE_CHARGEMENT[0],TAILLE_BARRE_DE_CHARGEMENT[1], 70)

MenuShop = Menuf.Shop(LONGEUR, HAUTEUR, "Shop")
MenuShopUpgrade = Menuf.ShopUpgradePersonnageSlide(LONGEUR, HAUTEUR, "Shop")
MenuShopUpgradeWeaponSlide = Menuf.ShopUpgradeArmeSlide(LONGEUR, HAUTEUR, "Shop")

Decor.bareDechargement(COORDONNEES_BARRE_DE_CHARGEMENT[0], COORDONNEES_BARRE_DE_CHARGEMENT[1], 
                        TAILLE_BARRE_DE_CHARGEMENT[0],TAILLE_BARRE_DE_CHARGEMENT[1], 90)

MenuEquipement = Menuf.BuyEquipement(LONGEUR, HAUTEUR, "Equipement")

#In game
MenuD = Menuf.MenuDeath(LONGEUR, HAUTEUR)
MenuG = Menuf.MenuGame(LONGEUR, HAUTEUR)

#Objects
Border = [OI.Border("border1", -3000), OI.Border("border2", LONGEUR + 3000)]

Decor.bareDechargement(COORDONNEES_BARRE_DE_CHARGEMENT[0], COORDONNEES_BARRE_DE_CHARGEMENT[1], 
                        TAILLE_BARRE_DE_CHARGEMENT[0],TAILLE_BARRE_DE_CHARGEMENT[1], 95)

Joueur1.charge()

Decor.bareDechargement(COORDONNEES_BARRE_DE_CHARGEMENT[0], COORDONNEES_BARRE_DE_CHARGEMENT[1], 
                        TAILLE_BARRE_DE_CHARGEMENT[0],TAILLE_BARRE_DE_CHARGEMENT[1], 100)



"""Part of menus
Partie des menus"""

def menu(gold, inventaire):
    """function of main menu
    fonction du menu principal"""


    play = True
    leave = False
    infoGame = {"map": "Terre", "mode": "Infini"}
    EZ.reglage_fps(30)

    while play:
        gold = Reader.ReadGold()
        inventaire = Reader.ReadInventaire()
        MenuP.displayMenu(Joueur1.chargesAvant, gold)

        evenement = EZ.recupere_evenement()
        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return 0, infoGame

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            if 435 < EZ.souris_x() < 845 and 595 < EZ.souris_y() < 710: # Bouton Play / Play button
                return "Game", infoGame
            
            elif 950 < EZ.souris_x() < 1200 and 575 < EZ.souris_y() < 700: # Bouton Shop / Shop button
                leave = menuShop()
                if type(leave) == str:
                    demande = leave
                    leave = False
                    if demande == "Joueur":
                        MenuShopUpgrade.TrieInventaire(inventaire)
                        leave = menuShopUpgrade(gold)
                    
                    elif demande == "Armes":
                        MenuShopUpgradeWeaponSlide.TrieInventaire(inventaire)
                        leave = menuShopUpgradeWeaponSlide(gold)

                    elif demande == "Equipement":
                        print("Equipement")




            
            elif 80 < EZ.souris_x() < 330 and 575 < EZ.souris_y() < 700: # Bouton Mode / Game mode button
                leave = menuMode()
                if type(leave) == str:
                    demande = leave
                    if demande == "Campagne":
                        infoGameTemp = menuCarte(infoGame)
                        

                    elif demande == "Infini":
                        infoGameTemp = menuInfini(infoGame)
                    
                    if infoGameTemp == True:
                        leave = True
                    
                    elif infoGameTemp == False:
                        leave = False
                    
                    else:
                        infoGame = infoGameTemp
                        leave = False
                        
                        

            elif 1060 < EZ.souris_x() < 1260 and 260 < EZ.souris_y() < 340: # Bouton Personnages / Player button
                MenuPerso.TrieInventaire(inventaire)
                leave = menuPerso(gold)
                
            elif 1060 < EZ.souris_x() < 1260 and 380 < EZ.souris_y() < 460: # Bouton Equipement / equipments button
                leave = menuEquipement(gold)

            elif 30 < EZ.souris_x() < 110 and 10 < EZ.souris_y() < 90: # Bouton Equipement / equipments button
                print("En phase devloppement")

            elif 1170 < EZ.souris_x() < 1250 and 10 < EZ.souris_y() < 90: # Bouton Equipement / equipments button
                EZ.destruction_fenetre()
                return 0, infoGame

        if leave:
            return 0, infoGame
        
        EZ.mise_a_jour()
        EZ.frame_suivante()

def menuDeath(gold, kill, wave):
    """function of death menu
    fonction du menu de mort"""

    play = True
    EZ.reglage_fps(60)
    MenuD.displayFond(LONGEUR, HAUTEUR, gold, kill, wave, Joueur1.chargesAvant)

    while play:

        evenement = EZ.recupere_evenement()
        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return 0

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            if 910 < EZ.souris_x() < 1220 and 615 < EZ.souris_y() < 705:
                return "Game"

            elif 490 < EZ.souris_x() < 790 and 615 < EZ.souris_y() < 705:
                return "Menu"

            elif  60 < EZ.souris_x() < 370 and 615 < EZ.souris_y() < 705:
                EZ.destruction_fenetre()
                return 0

        if evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return "Menu"
                
        
        EZ.mise_a_jour()
        EZ.frame_suivante()

def menuGame():
    """ function of game menu ( press escape to go in menuGame )
    Fonction du menu en jeux ( appuyer sur echape pour venir au menuGame )"""

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

def menuPerso(gold):
    """Function of player menu for selecting caracter
    Fonction du menu de selection de personnage"""


    x = 100
    xLast = 0
    click = False

    perso = True
    leave = False
    while perso:
        MenuPerso.traceMenuPersonnages(x)

        evenement = EZ.recupere_evenement()

        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True

        if evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            click = True
            xLast = EZ.souris_x()

            if 0 < EZ.souris_x() < 60 and 0 < EZ.souris_y() < 70:
                return False 

            elif MenuPerso.yDebutCadre < EZ.souris_y() < MenuPerso.yDebutCadre + MenuPerso.hauteurCardreJoueur: # look if the click is in the Players frame area / regarde si le click se trouve dans la zone des cadres Joueurs
                xSouris = EZ.souris_x()

                for cadre in range(len(MenuPerso.chargesPersonnage)):
                    if cadre * MenuPerso.largeurCadrePlusEspace + x < xSouris < cadre * MenuPerso.largeurCadrePlusEspace + x + MenuPerso.largeurCadre: # check if the click is in a box / verifie si le click est dans un cadre
                        if MenuPerso.infoPersonnages[f"Personnage{cadre + 1}"][0] == True:
                            Joueur1.personnage = cadre + 1
                            Joueur1.charge()
                            return False
                        
                        else:
                            leave = menuBuyPerso(gold, cadre)

                            if leave == "Menu":
                                return False
                            


                

        
        elif evenement == "SOURIS_BOUTON_GAUCHE_RELACHE":
            click = False
        
        if click and evenement == "SOURIS_MOUVEMENT":
            decalage = xLast - EZ.souris_x()
            if -MenuPerso.largeurAllCadre + LONGEUR - 100 + decalage <= x <= 100  + decalage: 
                x -= decalage
                xLast = EZ.souris_x()

        if leave:
            return True

        EZ.mise_a_jour()
        EZ.frame_suivante()


def menuBuyPerso(gold, numPerso):
    """Function of the menu to buy a character and see the stats of the character
    Fonction du menu d'achat d'un personnage et de voir les stats du personnage"""


    statsPerso = Reader.ReadStatsPlayers()[numPerso]
    MenuBuyPerso = Menuf.BuyPersonnage(LONGEUR, HAUTEUR, numPerso ,statsPerso['name'], statsPerso)

    play = True
    while play:
        MenuBuyPerso.DisplayMenu()

        evenement = EZ.recupere_evenement()

        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True
        
        elif evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":

            if 0 < EZ.souris_x() < 60 and 0 < EZ.souris_y() < 70:
                return False 

            elif 980 <= EZ.souris_x() < 1180 and 560 < EZ.souris_y() < 640: # Button Buy / Bouton Achat
                if gold >= statsPerso['price']:
                    gold -= statsPerso['price']
                    Joueur1.personnage = numPerso + 1
                    Joueur1.charge()
                    Writer.SaveGold(gold)
                    Writer.BuyCracters(numPerso + 1)
                    return "Menu"
                else:
                    print("Pas assez d'argent")

        EZ.mise_a_jour()
        EZ.frame_suivante()


def menuMode():
    """Function of the menu to select the mode of the game
    Fonction du menu de selection du mode de jeux"""

    MenuMode.DisplayMenu()

    play = True

    while play:

        evenement = EZ.recupere_evenement()
        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True

        elif evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False


        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":

            if 0 < EZ.souris_x() < 60 and 0 < EZ.souris_y() < 70:
                return False 

            elif 100 < EZ.souris_x() < 1180 and 170 < EZ.souris_y() < 380:   #Bouton Campagne
                return "Campagne"

            elif 100 < EZ.souris_x() < 1180 and 400 < EZ.souris_y() < 610: # Bouton Infini
                return "Infini"

        elif evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False
            
    
        EZ.mise_a_jour()
        EZ.frame_suivante()


def menuInfini(infoGame):
    """Function of the Menu Infini for choses the map
    Fonction du menu Infini pour choisir la carte"""


    infoGame['mode'] = "Infini"
    x = 100
    xLast = 0
    click = False

    perso = True
    leave = False
    while perso:
        MenuMap.displayMenu(x)

        evenement = EZ.recupere_evenement()

        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True

        elif evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False


        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            click = True
            xLast = EZ.souris_x()

            if 0 < EZ.souris_x() < 60 and 0 < EZ.souris_y() < 70:
                return infoGame 

            elif MenuMap.yDebutCadre < EZ.souris_y() < MenuMap.yDebutCadre + MenuMap.hauteurCadre: # look if the click is in a frame area / regarde si le click se trouve dans la zone des cadres
                xSouris = EZ.souris_x()

                for cadre, map in enumerate(MenuMap.chargesMap):
                    if cadre * MenuMap.largeurCadrePlusEspace + x < xSouris < cadre * MenuMap.largeurCadrePlusEspace + x + MenuMap.largeurCadre: # check if the click is in a box / verifie si le click est dans un cadre
                        infoGame['map'] = map
                        return infoGame
                    
                            


                

        
        elif evenement == "SOURIS_BOUTON_GAUCHE_RELACHE":
            click = False
        
        if click and evenement == "SOURIS_MOUVEMENT":
            decalage = xLast - EZ.souris_x()
            if -MenuMap.largeurAllCadre + LONGEUR - 100 + decalage <= x <= 100  + decalage: 
                x -= decalage
                xLast = EZ.souris_x()

        if leave:
            return True

        EZ.mise_a_jour()
        EZ.frame_suivante()


def menuShop():
    """Function of the menu to select the mode of the game
    Fonction du menu de selection du mode de jeux"""

    MenuShop.DisplayMenu()

    play = True
    while play:

        evenement = EZ.recupere_evenement()
        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True

        elif evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False


        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":

            if 0 < EZ.souris_x() < 60 and 0 < EZ.souris_y() < 70:
                return False 

            elif 100 < EZ.souris_x() < 1180 and 170 < EZ.souris_y() < 380:   #Bouton pour améliorer le niveau du personnage et de son arme 
                return "Joueur"


            elif 100 < EZ.souris_x() < 1180 and 400 < EZ.souris_y() < 610: #Bouton pour améliorer le niveau du personnage et de son arme 
                return "Armes"

        elif evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False
            
    
        EZ.mise_a_jour()
        EZ.frame_suivante()



def menuShopUpgrade(gold):
    """Function of player menu for selecting caracter
    Fonction du menu de selection de personnage"""


    x = 100
    xLast = 0
    click = False
    leave = False

    perso = True
    while perso:
        MenuShopUpgrade.traceMenuShopUpgrade(x)

        evenement = EZ.recupere_evenement()

        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True

        if evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            click = True
            xLast = EZ.souris_x()

            if 0 < EZ.souris_x() < 60 and 0 < EZ.souris_y() < 70:
                return False 

            elif MenuShopUpgrade.yDebutCadre < EZ.souris_y() < MenuShopUpgrade.yDebutCadre + MenuShopUpgrade.hauteurCardreJoueur: # look if the click is in the Players frame area / regarde si le click se trouve dans la zone des cadres Joueurs
                xSouris = EZ.souris_x()

                for cadre in range(len(MenuShopUpgrade.chargesPersonnage)):
                    if cadre * MenuShopUpgrade.largeurCadrePlusEspace + x < xSouris < cadre * MenuShopUpgrade.largeurCadrePlusEspace + x + MenuShopUpgrade.largeurCadre: # check if the click is in a box / verifie si le click est dans un cadre
                        leave = menuShopUpgradePersonnage(gold, int(MenuShopUpgrade.getListPersonnage()[cadre].split("Personnage")[-1])-1)
                            


                

        
        elif evenement == "SOURIS_BOUTON_GAUCHE_RELACHE":
            click = False
        
        if click and evenement == "SOURIS_MOUVEMENT":
            decalage = xLast - EZ.souris_x()
            if -MenuShopUpgrade.largeurAllCadre + LONGEUR - 100 + decalage <= x <= 100  + decalage: 
                x -= decalage
                xLast = EZ.souris_x()
        
        if leave:
            return True

        EZ.mise_a_jour()
        EZ.frame_suivante()




def menuShopUpgradePersonnage(gold, numPerso):
    """Function for the menu of upgrade of the character
    Fonction du menu d'amelioration du personnage"""

    statsPerso = Reader.ReadStatsPlayers()[numPerso]
    statsUpPerso = Reader.ReadUpStatsPlayers()[numPerso]
    MenuUpPerso = Menuf.ShopUpgradePersonnage(LONGEUR, HAUTEUR, numPerso ,statsPerso['name'], statsPerso, statsUpPerso)

    play = True
    while play:
        MenuUpPerso.DisplayMenu()
        CharactersLevel = Reader.ReadInventaire()[f"Personnage{numPerso +1}"][1]
        MenuUpPerso.SetCarcatersLevel(CharactersLevel)

        evenement = EZ.recupere_evenement()

        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True
        
        elif evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":

            if 0 < EZ.souris_x() < 60 and 0 < EZ.souris_y() < 70:
                return False 

            elif 980 <= EZ.souris_x() < 1180 and 560 < EZ.souris_y() < 640: # Button Buy / Bouton Achat
                if gold >= statsUpPerso['price'] * CharactersLevel:
                    gold -= statsUpPerso['price'] * CharactersLevel

                    Writer.SaveGold(gold)
                    Writer.UpCaracter(numPerso + 1)
                    Joueur1.CalculateStats()

                else:
                    print("Pas assez d'argent")

        EZ.mise_a_jour()
        EZ.frame_suivante()



def menuShopUpgradeWeaponSlide(gold):
    """Function of menu for selecting weapon
    Fonction du menu de selection de l'arme"""


    x = 100
    xLast = 0
    click = False
    leave = False
    

    perso = True
    while perso:
        MenuShopUpgradeWeaponSlide.SetlevelWeapon()
        MenuShopUpgradeWeaponSlide.traceMenuShopUpgrade(x)

        evenement = EZ.recupere_evenement()

        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True

        if evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            click = True
            xLast = EZ.souris_x()

            if 0 < EZ.souris_x() < 60 and 0 < EZ.souris_y() < 70:
                return False 

            elif MenuShopUpgradeWeaponSlide.yDebutCadre < EZ.souris_y() < MenuShopUpgradeWeaponSlide.yDebutCadre + MenuShopUpgradeWeaponSlide.hauteurCardreJoueur: # look if the click is in the Players frame area / regarde si le click se trouve dans la zone des cadres Joueurs
                xSouris = EZ.souris_x()

                for cadre in range(len(MenuShopUpgradeWeaponSlide.chargesWeapons)):
                    if cadre * MenuShopUpgradeWeaponSlide.largeurCadrePlusEspace + x < xSouris < cadre * MenuShopUpgradeWeaponSlide.largeurCadrePlusEspace + x + MenuShopUpgradeWeaponSlide.largeurCadre: # check if the click is in a box / verifie si le click est dans un cadre
                        leave = menuShopUpgradeWeapon(gold, int(MenuShopUpgradeWeaponSlide.getListPersonnage()[cadre].split("Personnage")[-1])-1)
                            

        
        elif evenement == "SOURIS_BOUTON_GAUCHE_RELACHE":
            click = False
        
        if click and evenement == "SOURIS_MOUVEMENT":
            decalage = xLast - EZ.souris_x()
            if -MenuShopUpgradeWeaponSlide.largeurAllCadre + LONGEUR - 100 + decalage <= x <= 100  + decalage: 
                x -= decalage
                xLast = EZ.souris_x()
        
        if leave:
            return True

        EZ.mise_a_jour()
        EZ.frame_suivante()


def menuShopUpgradeWeapon(gold, numPerso):
    """Function for the menu of upgrade of the weapon
    Fonction du menu d'amelioration de l'arme"""


    statsPerso = Reader.ReadStatsPlayers()[numPerso]
    statsUpPerso = Reader.ReadUpStatsPlayers()[numPerso]
    MenuUpWeapon = Menuf.ShopUpgradeWeapon(LONGEUR, HAUTEUR, numPerso ,statsPerso['name'], statsPerso, statsUpPerso, MenuShopUpgradeWeaponSlide.getNumberOfUpgrade(f"Personnage{numPerso +1}"))

    play = True
    while play:
        weaponLevel = Reader.ReadInventaire()[f"Personnage{numPerso +1}"][2]
        MenuUpWeapon.SetWeaponLevel(weaponLevel)
        MenuUpWeapon.DisplayMenu()

        evenement = EZ.recupere_evenement()

        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True
        
        elif evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":

            if 0 < EZ.souris_x() < 60 and 0 < EZ.souris_y() < 70:
                return False 

            elif 980 <= EZ.souris_x() < 1180 and 560 < EZ.souris_y() < 640: # Button Buy / Bouton Achat
                if gold >= statsUpPerso['price'] * weaponLevel and weaponLevel < MenuShopUpgradeWeaponSlide.getNumberOfUpgrade(f"Personnage{numPerso +1}"):
                    gold -= statsUpPerso['price'] * weaponLevel

                    Writer.SaveGold(gold)
                    Writer.UpWeapon(numPerso +1, weaponLevel +1)
                    Joueur1.CalculateStats()
                    Joueur1.charge()
                
                elif weaponLevel >= MenuShopUpgradeWeaponSlide.getNumberOfUpgrade(f"Personnage{numPerso +1}"):
                    print("Vous avez atteint le nombre maximum d'ameliorations")

                else:
                    print("Pas assez d'argent")

        EZ.mise_a_jour()
        EZ.frame_suivante()


def menuEquipement(gold):
    """Function of the Menu Equipement for choice what equipement to buy
    Fonction du menu d'équipement pour choisir quel équipement acheter"""


    x = 100
    xLast = 0
    click = False

    play = True
    leave = False
    while play:
        MenuEquipement.displayMenu(x)

        evenement = EZ.recupere_evenement()

        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True

        elif evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False


        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            click = True
            xLast = EZ.souris_x()

            if 0 < EZ.souris_x() < 60 and 0 < EZ.souris_y() < 70:
                return False 

            elif MenuEquipement.yDebutCadre < EZ.souris_y() < MenuEquipement.yDebutCadre + MenuEquipement.hauteurCadre: # look if the click is in a frame area / regarde si le click se trouve dans la zone des cadres
                xSouris = EZ.souris_x()

                for cadre, equipement in enumerate(MenuEquipement.chargesEquipement):
                    if cadre * MenuEquipement.largeurCadrePlusEspace + x < xSouris < cadre * MenuEquipement.largeurCadrePlusEspace + x + MenuEquipement.largeurCadre: # check if the click is in a box / verifie si le click est dans un cadre
                        leave = menuBuyEquipement(gold, equipement, MenuEquipement.chargesEquipement[equipement])
                        
                    

        
        elif evenement == "SOURIS_BOUTON_GAUCHE_RELACHE":
            click = False
        
        if click and evenement == "SOURIS_MOUVEMENT":
            decalage = xLast - EZ.souris_x()
            if -MenuEquipement.largeurAllCadre + LONGEUR - 100 + decalage <= x <= 100  + decalage: 
                x -= decalage
                xLast = EZ.souris_x()

        if leave:
            return True

        EZ.mise_a_jour()
        EZ.frame_suivante()


def menuBuyEquipement(gold, equipement, equipementPicture):
    """Function of the menu to buy a equipement
    Fonction du menu d'achat d'un équipement"""

    MenuBuyEquipement = Menuf.InfoEquipement(LONGEUR, HAUTEUR, equipement, equipement, equipementPicture, PRIX_EQUIPEMENT[equipement])

    leave = False
    play = True
    while play:
        MenuBuyEquipement.DisplayMenu()

        evenement = EZ.recupere_evenement()

        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True
        
        elif evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":

            if 0 < EZ.souris_x() < 60 and 0 < EZ.souris_y() < 70:
                return False 

            elif 980 <= EZ.souris_x() < 1180 and 560 < EZ.souris_y() < 640: # Button Buy / Bouton Achat
                if gold >= PRIX_EQUIPEMENT[equipement] :
                    gold -= PRIX_EQUIPEMENT[equipement]
                    Writer.SaveGold(gold)
                    Writer.BuyEquipement(equipement)
                    return False
                
                elif Reader.ReadEquipement()[equipement]:
                    print("Vous avez déjà acheté cet équipement")

                else:
                    print("Pas assez d'argent")
            
            elif 100 <= EZ.souris_x() < 350 and 560 < EZ.souris_y() < 640 and Reader.ReadEquipement()[equipement]: # Button Upgrade / Bouton Amelioration
                leave = menuUpgradeEquipement(gold, equipement, equipementPicture)

        if leave:
            return True

        EZ.mise_a_jour()
        EZ.frame_suivante()


def menuUpgradeEquipement(gold, equipement, equipementPicture):
    """Function of the menu to upgrade a equipement
    Fonction du menu d'amelioration d'un équipement"""

    MenuUpgradeEquipement = Menuf.UgradeEquipement(LONGEUR, HAUTEUR, equipement, equipementPicture, PRIX_EQUIPEMENT[equipement]//2)

    play = True
    while play:
        MenuUpgradeEquipement.DisplayMenu()
        
        evenement = EZ.recupere_evenement()

        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True
        
        elif evenement == "TOUCHE_ENFONCEE":
            if EZ.touche() == "escape":
                return False

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":

            if 0 < EZ.souris_x() < 60 and 0 < EZ.souris_y() < 70:
                return False 

            if equipement == "Grenade":

                if 1156 <= EZ.souris_x() < 1206 and 170 < EZ.souris_y() < 314: # Button Damage / Bouton Dommage
                    if gold >= PRIX_EQUIPEMENT[equipement]//2 * Reader.ReadStatsEquipement()[equipement]['numberUpgrade']:
                        gold -= PRIX_EQUIPEMENT[equipement]//2 * Reader.ReadStatsEquipement()[equipement]['numberUpgrade']
                        Writer.SaveGold(gold)
                        Writer.UpEquipement(equipement, "eficiency", Reader.ReadStatsEquipement()[equipement]['eficiency'] * 0.1)
                    
                    else:
                        print("Pas assez d'argent")

                elif 1156 <= EZ.souris_x() < 1206 and 330 < EZ.souris_y() < 474: # Button Cooldown / Bouton Cooldown
                    if gold >= PRIX_EQUIPEMENT[equipement]//2 * Reader.ReadStatsEquipement()[equipement]['numberUpgrade']:
                        gold -= PRIX_EQUIPEMENT[equipement]//2 * Reader.ReadStatsEquipement()[equipement]['numberUpgrade']
                        Writer.SaveGold(gold)
                        Writer.UpEquipement(equipement, "cooldown", -(Reader.ReadStatsEquipement()[equipement]['cooldown'] * 0.1) )

                    else:
                        print("Pas assez d'argent")

                elif 1156 <= EZ.souris_x() < 1206 and 490 < EZ.souris_y() < 634: # Button Bonus range / Bouton Bonus Range
                    if gold >= PRIX_EQUIPEMENT[equipement]//2 * Reader.ReadStatsEquipement()[equipement]['numberUpgrade']:
                        gold -= PRIX_EQUIPEMENT[equipement]//2 * Reader.ReadStatsEquipement()[equipement]['numberUpgrade']
                        Writer.SaveGold(gold)
                        Writer.UpEquipement(equipement, "BonusRange", 10)

                    else:
                        print("Pas assez d'argent")

            else:
                
                if 1156 <= EZ.souris_x() < 1206 and 170 < EZ.souris_y() < 386: # Button Damage / Bouton Dommage
                    if gold >= PRIX_EQUIPEMENT[equipement]//2 * Reader.ReadStatsEquipement()[equipement]['numberUpgrade']:
                        gold -= PRIX_EQUIPEMENT[equipement]//2 * Reader.ReadStatsEquipement()[equipement]['numberUpgrade']
                        Writer.SaveGold(gold)
                        Writer.UpEquipement(equipement, "eficiency", Reader.ReadStatsEquipement()[equipement]['eficiency'] * 0.1 if not(equipement == "Shield") else 1)

                    else:
                        print("Pas assez d'argent")


                elif 1156 <= EZ.souris_x() < 1206 and 410 < EZ.souris_y() < 626: # Button Cooldown / Bouton Cooldown
                    if gold >= PRIX_EQUIPEMENT[equipement]//2 * Reader.ReadStatsEquipement()[equipement]['numberUpgrade']:
                        gold -= PRIX_EQUIPEMENT[equipement]//2 * Reader.ReadStatsEquipement()[equipement]['numberUpgrade']
                        Writer.SaveGold(gold)
                        Writer.UpEquipement(equipement, "cooldown", -(Reader.ReadStatsEquipement()[equipement]['cooldown'] * 0.1) )

                    else:
                        print("Pas assez d'argent")
        

        EZ.mise_a_jour()
        EZ.frame_suivante()


def menuCarte(infoGame):
    """Function of the menu to choose a map in campaign mode
    Fonction du menu de choix de carte en mode campagne"""

    infoGame["mode"] = "Campagne"

    TAILLE_IMAGE = MenuCarte.getTailleFond()[0]
    TAILLE_BOUTON = MenuCarte.getTailleBouton()
    COORDONNER_BOUTON = MenuCarte.getCoordonnerBouton()

    x = 0
    xLast = x

    y = -2000
    yLast = y

    click = False


    play = True
    while play:
        MenuCarte.displayFond(x,y)

        evenement = EZ.recupere_evenement()

        if evenement == "EXIT":
            EZ.destruction_fenetre()
            return True

        elif evenement == "SOURIS_BOUTON_GAUCHE_ENFONCE":
            click = True
            xLast = EZ.souris_x()
            yLast = EZ.souris_y()
        
            for map in COORDONNER_BOUTON:
                if COORDONNER_BOUTON[map][0] + x < xLast < COORDONNER_BOUTON[map][0] + TAILLE_BOUTON[0] + x and COORDONNER_BOUTON[map][1] + y < yLast < COORDONNER_BOUTON[map][1] + TAILLE_BOUTON[1] + y: # Check if the mouse is on a button / Check si la souris est sur un bouton
                    infoGame["map"] = map
                    return infoGame
                
                if map == Reader.ReadMap():
                    break



        elif evenement == "SOURIS_BOUTON_GAUCHE_RELACHE":
            click = False
            
        if click and evenement == "SOURIS_MOUVEMENT":
            x -= xLast - EZ.souris_x()
            y -= yLast - EZ.souris_y()
            xLast = EZ.souris_x()
            yLast = EZ.souris_y()
        

        

        # Verifie que l'image ne sort pas de l'ecran
        if y > 0:
            y = 0

        elif y < -TAILLE_IMAGE + HAUTEUR:
            y = -TAILLE_IMAGE + HAUTEUR
        
        if x > 0:
            x = 0

        elif x + TAILLE_IMAGE - LONGEUR < 0:
            x = LONGEUR - TAILLE_IMAGE

        


        EZ.mise_a_jour()
        EZ.frame_suivante()






"""Start of game part
Début de la partie jeu"""


def genratesMob(name, hauteurSol,type = "COMMON"):
    """generate a mob
    Genere un mob

    Args:
        name (str): Name of monster / Nom du monstre

    Returns:
        object: the monster /le monstre
    """
    

    if type == "COMMON":
        if Joueur1.x - 250 <= Border[0].xFictif + Border[0].hitbox[0]:
            return Monstref.Monstre(name, Joueur1.x, hauteurSol, random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif)))
        
        elif Joueur1.x + 250 >= Border[1].xFictif:
            return Monstref.Monstre(name, Joueur1.x , hauteurSol, random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250))

        return Monstref.Monstre(name, Joueur1.x, hauteurSol, random.choice([random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250), random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif))]))

    elif type == "STRENGTH" or type == "HEAL":
        if Joueur1.x - 250 <= Border[0].xFictif + Border[0].hitbox[0]:
            return Monstref.Wizard(name, Joueur1.x, hauteurSol, random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif)), type)
        
        elif Joueur1.x + 250 >= Border[1].xFictif:
            return Monstref.Wizard(name, Joueur1.x, hauteurSol, random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250), type)

        return Monstref.Wizard(name, Joueur1.x, hauteurSol, random.choice([random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250), random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif))]), type)

    elif type == "SHOOTER":
        if Joueur1.x - 250 <= Border[0].xFictif + Border[0].hitbox[0]:
            return Monstref.MonstreShooter(name, Joueur1.x, hauteurSol,random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif)))
        
        elif Joueur1.x + 250 >= Border[1].xFictif:
            return Monstref.MonstreShooter(name, Joueur1.x, hauteurSol,random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250))

        return Monstref.MonstreShooter(name, Joueur1.x, hauteurSol,random.choice([random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250), random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif))]))
    
    elif type == "BOSS_COMMON":
        if Joueur1.x - 250 <= Border[0].xFictif + Border[0].hitbox[0]:
            return Monstref.Boss(name, Joueur1.x, hauteurSol,random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif)))
        
        elif Joueur1.x + 250 >= Border[1].xFictif:
            return Monstref.Boss(name, Joueur1.x, hauteurSol,random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250))

        return Monstref.Boss(name, Joueur1.x, hauteurSol,random.choice([random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250), random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif))]))

    elif type == "BOSS_STILL":
        if Joueur1.x - 250 <= Border[0].xFictif + Border[0].hitbox[0]:
            return Monstref.BossShooter(name, Joueur1.x, hauteurSol,random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif)))
        
        elif Joueur1.x + 250 >= Border[1].xFictif:
            return Monstref.BossShooter(name, Joueur1.x, hauteurSol,random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250))

        return Monstref.BossShooter(name, Joueur1.x, hauteurSol,random.choice([random.randint(int(Border[0].xFictif), int(Joueur1.x) - 250), random.randint(int(Joueur1.x) + 250, int(Border[1].xFictif))]))




def Startwave(number, hauteurSol, mode, map= "Mars"):
    """ generate the monsters of the wave
    Genere les monstres en début de vague

    Args:
        number (int): number of wave / numero de la vague
        hauteurSol (int): height of the ground / hauteur du sol
        mode (str): mode of the game / mode de jeux "Infini" ou "Campagne"
        map (str): name of the map / nom de la carte

    Returns:
        list:   listMob: list all mob of the wave / liste de tout les mob de la vague , 
                listWizzard: list of all wizzard (mob with effect) / liste de tout les sorcier (mob avec effet), 
                listShooter: list of all shooter mob / liste de tout les monstres qui tirs
    """

    listMob = []
    listWizzard = []
    listShooter = []

    if mode == "Campagne":

        with open(f'FichiersJeu/InfoWave/Mob{map}.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                if row[f'type_wave_{number}'] == "COMMON" or row[f'type_wave_{number}'] == "BOSS_COMMON":
                    listMob += [genratesMob(row[f'name_wave_{number}'],hauteurSol, row[f'type_wave_{number}'])for monstre in range(int(row[f'number_wave_{number}']))]

                elif row[f'type_wave_{number}'] == "STRENGTH" or row[f'type_wave_{number}'] == "HEAL":
                    listWizzard += [genratesMob(row[f'name_wave_{number}'], hauteurSol, row[f'type_wave_{number}'])for monstre in range(int(row[f'number_wave_{number}']))]

                elif row[f'type_wave_{number}'] == "SHOOTER" or row[f'type_wave_{number}'] == "BOSS_STILL":
                    listShooter += [genratesMob(row[f'name_wave_{number}'], hauteurSol, row[f'type_wave_{number}'])for monstre in range(int(row[f'number_wave_{number}']))]
                


                # print(row[f'name_wave_{number}'], row[f'number_wave_{number}'], row[f'type_wave_{number}'])
    
    elif mode == "Infini":
        EnTete = ['Map']
        for maptemp in MenuMap.getMapName():
            EnTete.append(f'{maptemp}Name')
            EnTete.append(f'{maptemp}Dificulty')
            EnTete.append(f'{maptemp}Type')

        AllMob = {"COMMON": [], "STRENGTH": [], "HEAL": [], "SHOOTER": []}
        with open(f'FichiersJeu\InfoWave\AllMobe.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';', fieldnames=EnTete)

            lastType = "COMMON"
            for row in reader:
                if row[f'{map}Name'] != '' and row[f'{map}Name'] != 'Name' and row[f'{map}Name'] != map and (row[f'{map}Type'] in AllMob.keys() or lastType in AllMob.keys()): # Si la ligne n'est pas vide 
                    AllMob[row[f'{map}Type']].append(row[f'{map}Name']) if row[f'{map}Type'] != '' else AllMob[lastType].append(row[f'{map}Name'])
                lastType = row[f'{map}Type']


        for monstre in range(number*5 + 1): # load the wave / charge la vague
            typeMob = random.choice(list(AllMob.keys()))

            if AllMob[typeMob] != []: # if there is a mob of this type / si il y a un mob de ce type
                mob = random.choice(AllMob[typeMob])

            else: # if there is no mob of this type / si il n'y a pas de mob de ce type
                continue

            if typeMob == "COMMON":
                listMob += [genratesMob(mob, hauteurSol)]
            
            elif typeMob == "STRENGTH" or typeMob == "HEAL":
                listWizzard += [genratesMob(mob, hauteurSol, typeMob)]
            
            elif typeMob == "SHOOTER":
                listShooter += [genratesMob(mob, hauteurSol, typeMob)]
            
  

    listMob += listWizzard
    listMob += listShooter
    
    return listMob, listWizzard, listShooter

def Verifzone(zone1, zone2):
    """ check if 2 zone are in the same zone
    Verifie si deux zone se touche

    Args:
        zone1 (objet): premier objet
        zone2 (objet): deuxieme objet

    Returns:
        bool: True si il se touche, sinon False
    """
    return ((((zone1.zoneHitBoxlist[0][0] <= zone2.zoneHitBoxlist[0][0] <= zone1.zoneHitBoxlist[1][0]) or (zone1.zoneHitBoxlist[0][0] <= zone2.zoneHitBoxlist[1][0] <= zone1.zoneHitBoxlist[1][0])) and (zone1.zoneHitBoxlist[0][1] <= zone2.zoneHitBoxlist[0][1] <= zone1.zoneHitBoxlist[3][1])) or (((zone1.zoneHitBoxlist[0][0] <= zone2.zoneHitBoxlist[0][0] <= zone1.zoneHitBoxlist[1][0]) or (zone2.zoneHitBoxlist[0][0] <= zone1.zoneHitBoxlist[1][0] <= zone2.zoneHitBoxlist[1][0])) and ((zone2.zoneHitBoxlist[0][1] <= zone1.zoneHitBoxlist[0][1] <= zone2.zoneHitBoxlist[3][1]) or (zone2.zoneHitBoxlist[0][1] <= zone1.zoneHitBoxlist[3][1] <= zone2.zoneHitBoxlist[3][1])) )) # verifie si des zonehitbox se touche

def VerifzonePower(zonePower, zoneMonstre):
    """ check if 2 zone are in the same zone for power
    Verifie si deux zone se touche pour les effet de pouvoir

    Args:
        zoneMonstre (objet): Monstre qui reçoit l'effet
        zonePower (objet): Sorcier qui done l'effet

    Returns:
        bool: True si il se touche, sinon False
    """
    return ((zonePower.zonePowerlist[0][0] <= zoneMonstre.zoneHitBoxlist[0][0] <= zonePower.zonePowerlist[1][0]) or (zonePower.zonePowerlist[0][0] <= zoneMonstre.zoneHitBoxlist[1][0] <= zonePower.zonePowerlist[1][0])) and ((zonePower.zonePowerlist[0][1] <= zoneMonstre.zoneHitBoxlist[0][1] <= zonePower.zonePowerlist[3][1]) or (zonePower.zonePowerlist[0][1] <= zoneMonstre.zoneHitBoxlist[3][1] <= zonePower.zonePowerlist[3][1]) ) # verifie si des zonePower touche un mob

def getNearSide(zone1, zone2):
    """ get the near side where zone1 touch zone2
    Donne le coter le plus proche ou zone1 touche zone2

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
    """ function to check if the player is hit by the monsters and if monstre is hit by the player
    Fonction qui compare la position des different ellement et mets des degat si nessesaire
    
    Args:
        monstres(list): Liste de tout les monstre en vie
        armes(list): Arme du joueur
    
    """
    mobKill = 0 # monstre kill in function / monstre tué dans la fonction
    # Arme sur monstre
    for i,monstre in enumerate(monstres):
        for arme in armesJoueur:
            if Verifzone(monstre, arme["arme"]):
                monstre.domage(arme["arme"].damage["damage"])
                arme["arme"].use()
            
        if Joueur.equipement["grenade"] != None and Joueur.equipement["grenade"].getDoDamage() and Verifzone(monstre, Joueur.equipement["grenade"]):
            monstre.domage(Joueur.equipement["grenade"].getEfficiency())

        if monstre.death():
            monstres.pop(i)
            mobKill += 1

    # Monstres sur Joueur
        if Verifzone(Joueur, monstre):
            if monstre.attaque() and monstre.stats["damage"] != 0:
                Joueur.domage(monstre.stats["damage"])  # Inflige les degat au joueur

    for shooter in Shooters:
        if Verifzone(Joueur, shooter.arme["arme"]):
            Joueur.domage(shooter.arme["arme"].damage["damage"])
            shooter.arme["arme"].use()

    
    if Joueur.death():
        return monstres, False, mobKill

    return monstres, True, mobKill

def VerifBuff(wizzards, monstres):
    """function to check if the wizzard give buff to the near monsters
    Fonction qui verifie si les sorciers donne un buff aux monstre"""
    
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
    """ check if the player is in contact with an object
    Verifie si un objet et un contacte avec le joueur"""
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
    """ say to the player where i must shoot when he is stop
    dit au joueur de quel coter il doit tirée quand il est a l'arret"""

    nearMonstre = [LONGEUR + 1001, "right"]

    for monstre in monstres:
        lengtMontre = joueur.x - monstre.x
        if abs(lengtMontre) < nearMonstre[0]:
            if lengtMontre >= 0:
                nearMonstre = [lengtMontre, "left"]

            elif lengtMontre < 0:
                nearMonstre = [-lengtMontre, "right"]
    
    return nearMonstre[1]


def game(map, mode, limiteWave = -1):
    """ function that manage the game
    fonction qui gere le jeu
    
    Args:
        map (str): name of the map
        mode (str): name of the mode
        limiteWave (int): number of wave to play
        
    Returns:
        int/str: 1 if the player win, 0 if the player loose or quit, "Menu" if the player want to go to the menu", "Game" if the player want to replay the game
        
        
        
        """
    EZ.reglage_fps()

    Game = Menuf.Game(LONGEUR, HAUTEUR)
    Game.setMap(map)
    Joueur1.setHauteurSol(Game.hauteurSol)
    Joueur1.setEquipement([equipements for equipements in Reader.ReadEquipement() if Reader.ReadEquipement()[equipements]])
    Joueur1.resetStats()

    vague = 0
    Game.saveNumeroVague(vague)
    MonstreList = [] # List contenant l'ensemble des monstre en vie de la vague
    WizzardList = [] # List contenant l'ensemble des montre a effet
    ShooterList = [] # List contenant l'ensemble des montre qui tire
    timeLastWave = [EZ.clock(), True] # [temps a la fin de la vague(0 mob), etats du timer( True = En game, False = Timer en cours)]

    mobKill = 0 #Computer of mob killed / Compteur de mob tué

    
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
            
            #Affiche le nombre de monstre restant et le numero de la vague
            Game.displayNumeroVague()
            Decor.monster_left(LONGEUR - 124, 20, len(MonstreList))

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
            MonstreList, play, tmp_mobKill = VerifDegat(MonstreList, Joueur1.arme, Joueur1, ShooterList)
            mobKill += tmp_mobKill
            VerifContactX(Border, Game, Joueur1)
            WizzardList = VerifBuff(WizzardList, MonstreList)

            # Lance la prochaine vague
            if len(MonstreList) == 0:
                if timeLastWave[1]: # Permet de verifier si le timer entre vague a déjà été lancer
                    timeLastWave[0] = EZ.clock()
                    timeLastWave[1] = False
                
                if EZ.clock() - timeLastWave[0] >= TIMER_VAGUE:
                    MonstreList, WizzardList , ShooterList = Startwave(vague, Game.hauteurSol, mode, map)  # Gener la nouvelle vague
                    timeLastWave[1] = True
                    vague += 1
                    Game.saveNumeroVague(vague)
            
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
                
                elif EZ.touche() == "q": # Detection en qwerty donc == a : Utilise la potion de soin
                    Joueur1.UsePotion()
            
                elif EZ.touche() == "e": # Lance la grenade
                    Joueur1.UseGrenade()

                elif EZ.touche() == "w": # Detection en qwerty donc == z: Lance la reparation du bouclier
                    Joueur1.RepaireShield()

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

        #Gold generate / Or generer 
        gold = mobKill + (vague - 1) * 10

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
            Writer.SaveGold(gold + Reader.ReadGold())
            return menuDeath(gold, mobKill, vague)
            
        
        

