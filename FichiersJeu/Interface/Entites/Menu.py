"""Fichier contenant l'ensemble des menu du jeu"""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
import FichiersJeu.Interface.Animation as Anim

import FichiersJeu.Interface.Decor as Decor
import FichiersJeu.Interface.Entites.Bouton as Btn

import Outiles.PerfCompteur as Perfcompteur
Perfcompt = Perfcompteur.TimeDistribution()



class Interface:
    """parent class for all the interface
    Class mere de toute les interface"""

    def __init__(self, longeur, hauteur):
        self.longeur = longeur
        self.hauteur = hauteur
        


class Menu(Interface):
    """Basic class for all the menu
    Class du menu de base"""

    def __init__(self, longeur, hauteur):
        super().__init__(longeur, hauteur)

        self.chargesFond = None
        self.longeur = longeur
        self.hauteur = hauteur


    def displayFond(self):
        """Display the background
        Trace le fond du menu"""

        if self.chargesFond == None:
            self.chargeFond()

        EZ.trace_image(self.chargesFond ,0,0)
    

    def displayPlayer(self,image):
        """Trace le personnage"""

        EZ.trace_image(EZ.transforme_image(image,0,2), self.longeur//2-144, self.hauteur//2-144) # -144 pour le centrer, 48*6 / 2


class MenuPricipale(Menu):
    """class of the main menu
    Classe du menu principal"""

    def __init__(self, longeur, hauteur):
        super().__init__(longeur, hauteur)
        self.etapeAnimationFond = 0 # etape de l'animation du fond
        
    def chargeFond(self):
        """ load the background image
        Charge l'image du fond"""

        self.chargesFond = EZ.charge_image("FichiersJeu\Interface\Entites\Fond\Fond_menu2.png")

    def displayAnimationFond(self):
        """Trace l'animation de fond du menu"""
        Anim.traceAnimationFondMenuP(self.longeur, self.hauteur, self.etapeAnimationFond)
        if self.etapeAnimationFond < self.hauteur * 2:
            self.etapeAnimationFond += 1
        
        else:
            self.etapeAnimationFond = 0
    
    def displayMenu(self, personnage, gold):
        """ draw the menu
        Trace le Menu"""

        self.displayAnimationFond()
        self.displayFond() # Les boutton de l'interface
        self.displayPlayer(personnage)
        Decor.nombreDeGold(900, 10, gold)

class MenuDeath(Menu):
    """player death menu"
    Menu de mort du joueur"""

    def __init__(self, longeur, hauteur):
        super().__init__(longeur, hauteur)

    def chargeFond(self):
        """ load the background image
        Charge l'image du fond"""

        self.chargesFond = EZ.charge_image("FichiersJeu\Interface\Entites\Fond\FondMort.png")

    def displayFond(self, longeur, hauteur, gold, kill, wave, player):
        """Drawn the animation of Death Menu
        Trace l'animation du menu de la mort du joueur
        """
        Anim.traceAnimationMenuMort(longeur, hauteur, 3, gold, kill, wave, player)


class MenuGame(Menu):

    def __init__(self, longeur, hauteur):
        super().__init__(longeur, hauteur)

    def chargeFond(self):
        """ load the background image
        Charge l'image du fond"""

        self.chargesFond = EZ.charge_image("FichiersJeu\Interface\Entites\Fond\MenuGame.png")


class SousMenu(Menu):
    """class for all the submenu
    Classe pour tout les sous menu"""

    def __init__(self, longeur, hauteur, texte):
        super().__init__(longeur, hauteur)
        self.tailleOmbrePolice = 3 # Size of the Shadow of the fonts / Taille de l'ombre de la police
        self.yDebutWidget = self.hauteur//6 # y Start of the widget / y de début du Widget
        self.hauteurWidget = int(3 * self.hauteur/4) # height of the widget / Hauteur du widget
        self.couleurBorder = (100, 100, 110) # color of the border / couleur de la bordure
        self.couleurFond = (210, 210, 230) # color of the background / couleur du fond

        #Police
        self.texte = texte
        self.police = EZ.charge_police(50, "FichiersJeu\Interface\Entites\Police\CourageRoad.ttf", True)
        self.coordonneesFonts = [self.longeur//2 - EZ.dimension(EZ.image_texte(texte, self.police, 0, 0, 0))[0], self.yDebutWidget- EZ.dimension(EZ.image_texte(texte, self.police, 0, 0, 0))[1]] # [x, y]
        
        self.chargesPersonnage = None



    def chargeFond(self):
        """ load the background image
        charge l'image du fond"""

        self.chargesFond = EZ.charge_image("FichiersJeu\Interface\Entites\Fond\FondSousMenu.png")


    def traceTitre(self):
        """Draw the title of the subMenu
        trace le titre du sous-Menu

        Args:
            texte (str): Texte to drawn / texte a afficher
        """


        EZ.trace_image(EZ.image_texte(self.texte, self.police, 0, 0, 0), self.coordonneesFonts[0] + self.tailleOmbrePolice , self.coordonneesFonts[1] + self.tailleOmbrePolice)
        EZ.trace_image(EZ.image_texte(self.texte, self.police, 255, 255, 255), self.coordonneesFonts[0], self.coordonneesFonts[1])

    def traceFlecheRetour(self):
        """Draw the back arrow
        Trace la flèche retour
        """

        Decor.traceFlecheRetour(20, 20, 0.5)


    def TraceWidget(self, longueur):
        """Drawn the widget of the subMenu
        trace le widget(interface centré) du sous-Menu

        longueur (int): lenght of the widget / longueur du widget
        """
        
        Decor.traceCadre(self.longeur//2 - longueur//2, self.yDebutWidget, longueur, self.hauteurWidget, 3, 2, self.couleurFond, self.couleurBorder)
        
        self.traceTitre()
        self.traceFlecheRetour()

    def chargePersonnage(self):
        """load Caracters
        Charges les personnages
        """

        self.chargesPersonnage = {"Personnage1": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A2.png"), 0, 5),
        "Personnage2": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso2\Perso2A2.png"), 0, 5), 
        "Personnage3": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso3\Perso3A2.png"), 0, 5), 
        "Personnage4": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso4\Perso4A2.png"), 0, 5), 
        "Personnage5": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso5\Perso5A2.png"), 0, 5),
        "Personnage6": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso6\Perso6A2.png"), 0, 5),
        "Personnage7": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso7\Perso7A2.png"), 0, 5), 
        "Personnage8": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso8\Perso8A2.png"), 0, 5) }

    

class Personnages(SousMenu):
    """Player Menu class 
    Class du Menu des personnages"""

    def __init__(self, longeur, hauteur, texte, Inventaire = {}):
        super().__init__(longeur, hauteur, texte)
        self.hauteurCardreJoueur = int(3 * self.hauteurWidget/4)
        self.largeurCadre = 300
        self.largeurCadrePlusEspace = self.largeurCadre//0.9 # largeur du cadare plus l'espace qu'il laisse après lui pour ne pas être coller au prochain
        self.yDebutCadre = (self.hauteurWidget - self.hauteurCardreJoueur)//2 + self.yDebutWidget

        self.couleurFondCadreAchete = (200, 50, 50) 
        self.couleurBordureCadreAchete = (150, 0, 0) 

        self.couleurFondCadreEquipe = (50, 200, 50) 
        self.couleurBordureCadreEquipe = (0, 150, 0)


        self.policeCadre = EZ.charge_police(60, "FichiersJeu\Interface\Entites\Police\PermanentMarker-Regular.ttf", True)

    def chargePersonnage(self):
        super().chargePersonnage()

        self.largeurAllCadre = self.largeurCadrePlusEspace * len(self.chargesPersonnage)

    
    def TrieInventaire(self, Inventaire):
        """sort iventory to return Caracters infomartion
        Trie Inventaire et renvoie les inforamtion sur les personnages

        Args:
            Inventaire (dict): dictionary of inventoty / dictionnaire de l'inventaire
        """

        Personnages = {}
        for keys in Inventaire:
            if "Personnage" in keys:
                Personnages.update({keys: Inventaire[keys]})
        
        self.infoPersonnages = Personnages
    



    def TraceWidget(self, x):
        """Drawn the widget of the Caracters Menu
        trace le widget du Menu Personnages

        x (int): offset of the Caracters frame / decalage des Cadre des personnages
        """

        if x + 150 >= 100:
            Decor.traceCadre(x - 50, self.yDebutWidget, self.longeur + 150, self.hauteurWidget, 3, 2, self.couleurFond, self.couleurBorder)
        
        elif x < -(len(self.chargesPersonnage) * self.largeurCadrePlusEspace - self.longeur):
            Decor.traceCadre(-10, self.yDebutWidget, 20 + (x + len(self.chargesPersonnage) * self.largeurCadrePlusEspace), self.hauteurWidget, 3, 2, self.couleurFond, self.couleurBorder)
        
        else:
            Decor.traceCadre(-10, self.yDebutWidget, self.longeur + 20, self.hauteurWidget, 3, 2, self.couleurFond, self.couleurBorder)
        
        self.traceTitre()
        self.traceFlecheRetour()







    def traceCadreJoueur(self, x, etat):
        """Draw the frame for Caracters
        Trace le Cadre des Personnages

        Args:
            x (int): x start of frame / x début du Cadre
            etat (str): False: Caracters can by buy / Le personnages peut être acheter
                        True: Caracters can by play / Le personnages peut être jouer 
        """

        if etat:
            Decor.traceCadre(x, self.yDebutCadre, self.largeurCadre, 3 *self.hauteurCardreJoueur//4, 3, 2, self.couleurFondCadreEquipe, self.couleurBordureCadreEquipe) # Haut du cadre
            Decor.traceCadre(x, self.yDebutCadre + 3 *self.hauteurCardreJoueur//4, 300, self.hauteurCardreJoueur//4, 3, 2, self.couleurBordureCadreEquipe, self.couleurBordureCadreEquipe) # Haut du cadre

            coordonneesFonts = [x + self.largeurCadre//2 - EZ.dimension(EZ.image_texte("Select", self.policeCadre, 0, 0, 0))[0]//2, self.yDebutCadre + 7 *self.hauteurCardreJoueur//8 - EZ.dimension(EZ.image_texte("Select", self.policeCadre, 0, 0, 0))[1]//2] # [x, y]
            EZ.trace_image(EZ.image_texte("Select", self.policeCadre, 0, 0, 0), coordonneesFonts[0] + self.tailleOmbrePolice , coordonneesFonts[1] + self.tailleOmbrePolice)
            EZ.trace_image(EZ.image_texte("Select", self.policeCadre, 255, 255, 255), coordonneesFonts[0], coordonneesFonts[1])


        else:
            Decor.traceCadre(x, self.yDebutCadre, self.largeurCadre, 3* self.hauteurCardreJoueur//4, 3, 2, self.couleurFondCadreAchete, self.couleurBordureCadreAchete)
            Decor.traceCadre(x, self.yDebutCadre + 3 *self.hauteurCardreJoueur//4, 300, self.hauteurCardreJoueur//4, 3, 2, self.couleurBordureCadreAchete, self.couleurBordureCadreAchete) # Haut du cadre
            
            coordonneesFonts = [x + self.largeurCadre//2 - EZ.dimension(EZ.image_texte("Buy", self.policeCadre, 0, 0, 0))[0]//2,  self.yDebutCadre + 7 *self.hauteurCardreJoueur//8 - EZ.dimension(EZ.image_texte("Select", self.policeCadre, 0, 0, 0))[1]//2] # [x, y]
            EZ.trace_image(EZ.image_texte("Buy", self.policeCadre, 0, 0, 0), coordonneesFonts[0] + self.tailleOmbrePolice , coordonneesFonts[1] + self.tailleOmbrePolice)
            EZ.trace_image(EZ.image_texte("Buy", self.policeCadre, 255, 255, 255), coordonneesFonts[0], coordonneesFonts[1])



    def traceAllPersonnages(self, x):
        """Drawn all the Caracters and their frames
        Trace tout des personnages et leur cadre

        Args:
            x (int): x start of frames / x du debut des Cadres
        """

        if self.chargesPersonnage == None:
            self.chargePersonnage()

        xStart = x
        for infoPersonnage, ImagePeronnage in zip(self.infoPersonnages,self.chargesPersonnage):
            self.traceCadreJoueur(xStart, self.infoPersonnages[infoPersonnage][0])
            EZ.trace_image(self.chargesPersonnage[ImagePeronnage], xStart + self.largeurCadre//2 - EZ.dimension(self.chargesPersonnage[ImagePeronnage])[0]//2, self.yDebutCadre + 20)
            xStart += self.largeurCadrePlusEspace
        
    
    def traceMenuPersonnages(self, x):
        """Drawn all the Menu of Caracters
        Trace tout le Menu des Personnages

        Args:
            x (int): x gap of widget / x du debut des Cadres
        """

        # Perfcompt.newElement("Fond")
        self.displayFond()
        # Perfcompt.EndElement()

        # Perfcompt.newElement("Widget")
        self.TraceWidget(x)
        # Perfcompt.EndElement()


        # Perfcompt.newElement("Personnages")
        self.traceAllPersonnages(x)
        # Perfcompt.EndElement()

        # Perfcompt.calculate()
        # Perfcompt.clear()


class StatsPersonnage(SousMenu):
    """Class to display the Stats of a Caracter and is price
    Classe pour afficher les stats d'un personnage et son prix"""

    def __init__(self, longeur, hauteur, numPerso,texte, stats):
        super().__init__(longeur, hauteur, texte)
        self.stats = stats
        self.numPerso = numPerso

        self.largeurWidget = self.longeur - 100

        self.hauteurCardreInfo = int(3 * self.hauteurWidget/5)
        self.yDebutCadre = (self.hauteurWidget - self.hauteurCardreInfo)//4 + self.yDebutWidget
        self.largeurCadre = 400

        self.couleurBorderCadre = (140, 140, 140) # external color of frames info / Couleur externe des cadre info
        self.couleurFondCadre = (180, 180, 180) # Background color of frames info / Fond des cadre info

        self.policeCadre = EZ.charge_police(40, "FichiersJeu\Interface\Entites\Police\JosefinSans-BoldItalic.ttf", True)

    def traceCadreInfo(self):
        """Drawn the frames for Caracters info
        Trace les Cadre pour les info du personnages
        """
        
        for Cadre in range(1, 3):
            xCadre = Cadre * self.largeurWidget//2.5 - 150
            Decor.traceCadre(xCadre, self.yDebutCadre, self.largeurCadre, self.hauteurCardreInfo, 2, 3, self.couleurFondCadre, self.couleurBorderCadre) # Background / Fond

            if Cadre == 1:
                #Stats arme
                EZ.trace_image(EZ.image_texte(f"Damage: {self.stats['damage']}", self.policeCadre), xCadre + 10, self.yDebutCadre + self.hauteurCardreInfo - 160)
                EZ.trace_image(EZ.image_texte(f"Range: {self.stats['range']}", self.policeCadre), xCadre + 10, self.yDebutCadre + self.hauteurCardreInfo - 110)
                EZ.trace_image(EZ.image_texte(f"Durability: {self.stats['durability']}", self.policeCadre), xCadre + 10, self.yDebutCadre + self.hauteurCardreInfo - 60)


            elif Cadre == 2:
                #Stats Joueur
                EZ.trace_image(EZ.image_texte(f"Heal: {self.stats['vie']}", self.policeCadre), xCadre + 10, self.yDebutCadre + 10)
                EZ.trace_image(EZ.image_texte(f"Regen Time: {self.stats['regen']['cooldown']}", self.policeCadre), xCadre + 10, self.yDebutCadre + 60)
                EZ.trace_image(EZ.image_texte(f"Regen Power: {float(self.stats['regen']['eficiency']) * 10} ", self.policeCadre), xCadre + 10, self.yDebutCadre + 110)
                EZ.trace_image(EZ.image_texte(f"Speed: {self.stats['speed']}", self.policeCadre), xCadre + 10, self.yDebutCadre + 160)
                EZ.trace_image(EZ.image_texte(f"Acc: {self.stats['acc']}", self.policeCadre), xCadre + 10, self.yDebutCadre + 210)
                EZ.trace_image(EZ.image_texte(f"Jump Power: {self.stats['jumpPower']}", self.policeCadre), xCadre + 10, self.yDebutCadre + 260)

    

    def tracePrix(self):
        """Draw the price of the Caracters
        Trace le prix du Personnage
        """
        Decor.nombreDeGold(self.longeur - self.largeurWidget, self.yDebutWidget + self.hauteurWidget - 100, self.stats['price'])
    
    def traceBouttonBuy(self):
        """Draw the buy button
        Trace le bouton play
        """

        Btn.Bouton(self.largeurWidget - 200, self.yDebutWidget + self.hauteurWidget - 100, 200, 80, "Buy", (255, 255, 255), (0, 128, 64), 1, 3)

    def traceJoueur(self):
        """Draw the player
        Trace le joueur
        """

        if self.chargesPersonnage == None:
            self.chargePersonnage()

        EZ.trace_image(self.chargesPersonnage[f"Personnage{self.numPerso + 1}"], (self.largeurWidget//3) - 80 - EZ.dimension(self.chargesPersonnage[f"Personnage{self.numPerso}"])[0], self.yDebutCadre + self.hauteurCardreInfo - EZ.dimension(self.chargesPersonnage[f"Personnage{self.numPerso}"])[1])
        


        

    def DisplayMenu(self):
        """Display all the Menu
        Trace tout le Menu
        """

        self.displayFond()
        self.TraceWidget(self.largeurWidget)
        self.traceCadreInfo()
        self.tracePrix()
        self.traceBouttonBuy()

        self.traceJoueur()

class Mode(SousMenu):
    """Class to choice the game mode
    class pour choisir le mode de jeu"""

    def __init__(self, longeur, hauteur, texte):
        super().__init__(longeur, hauteur, texte)
        self.largeurWidget = self.longeur - 100
        self.couleurBorderCadre = (140, 140, 140) # external color of frames info / Couleur externe des cadre info
        self.couleurFondCadre = (180, 180, 180) # Background color of frames info / Fond des cadre info


        self.chargesBouton = [EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Mode\BoutonCampagne.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Mode\BoutonInfini.png")]

    def traceImage(self):
        """Draw the images of button mode
        Trace les images des boutons mode
        """

        Decor.traceCadre(self.largeurWidget//2 - EZ.dimension(self.chargesBouton[0])[0]//2 - 3 + 50, self.yDebutWidget + self.hauteurWidget//3 - EZ.dimension(self.chargesBouton[0])[1]//2 - 25, EZ.dimension(self.chargesBouton[0])[0] + 3, EZ.dimension(self.chargesBouton[0])[1], 3, 2, self.couleurFondCadre, self.couleurBorderCadre) # Background / Fond
        EZ.trace_image(self.chargesBouton[0], self.largeurWidget//2 - EZ.dimension(self.chargesBouton[0])[0]//2 + 50, self.yDebutWidget +  1 * self.hauteurWidget//3 - EZ.dimension(self.chargesBouton[0])[1]//2 - 25)

        Decor.traceCadre(self.largeurWidget//2 - EZ.dimension(self.chargesBouton[1])[0]//2 - 3 + 50, self.yDebutWidget + 2 * self.hauteurWidget//3 - EZ.dimension(self.chargesBouton[1])[1]//2 + 25, EZ.dimension(self.chargesBouton[1])[0] + 3, EZ.dimension(self.chargesBouton[1])[1], 3, 2, self.couleurFondCadre, self.couleurBorderCadre) # Background / Fond
        EZ.trace_image(self.chargesBouton[1], self.largeurWidget//2 - EZ.dimension(self.chargesBouton[1])[0]//2 + 50, self.yDebutWidget + 2 * self.hauteurWidget//3 - EZ.dimension(self.chargesBouton[0])[1]//2 + 25)
    
    def DisplayMenu(self):
        """Display all the Menu
        Trace tout le Menu
        """

        self.displayFond()
        self.TraceWidget(self.largeurWidget)
        self.traceImage()


        


class Game(Interface):
    """Class to display the Game and manage it
    Classe pour afficher le jeu et le gérer"""

    def __init__(self, longeur, hauteur):
        super().__init__(longeur, hauteur)

        self.chargesFond = None
        self.decal = 0 # decalage de l'image 2
        self.decalage = 0     # decalage effectué
        self.CoordonnerFictive = 0 # Calcule le decalage total depuis le debut de la Game pour crée une impression de coordoner dans une map

        self.move_info = {"right": False, "left": False, "saut": False, "inertie": 0}
        self.move_possible = {"right": True, "left": True}  #Donne les deplacement que le joueur peux effectuer (permet d'interfire certain deplacement)
        self.contact = False

        self.map = "Mars"
        self.largeurFond = 2400 # map width / Largeur de la map
        self.hauteurSol = 604 # ground height / Hauteur du sol

    def setMap(self, map):
        """Set the map
        Defini la map"""
        self.map = map
        self.chargeFond()

    def chargeFond(self):
        """ Load the background image
        Charge l'image du fond"""

        if self.map == "Mars":
            self.chargesFond = EZ.charge_image("FichiersJeu\Interface\Entites\Fond\FondMap\Mars.png")
            self.largeurFond = 2400
            self.hauteurSol = 604
        
        elif self.map == "Terre":
            self.chargesFond = EZ.charge_image("FichiersJeu\Interface\Entites\Fond\FondMap\Terre.jpg")
            self.largeurFond = 5000
            self.hauteurSol = 620
    
    def displayFond(self, acc, vitesse):
        """ display the background image
        Trace le fond du jeu"""


        if self.chargesFond == None:
            self.chargeFond()
        
        self.move(acc,vitesse)

        while not(0 <= self.decal <= self.largeurFond):
            if self.decal > self.largeurFond:
                self.decal -= self.largeurFond

            elif self.decal < 0:
                self.decal += self.largeurFond
        

        decal_x = [self.decal - self.largeurFond, self.decal]

        for fond in range(2):
            EZ.trace_image(self.chargesFond ,decal_x[fond],0)


        
    

    def move(self, acc, vitesse):
        """Move the background image for give on the player a movement
        Deplace l'image du fond pour donner au joueur un mouvement"""

        if not(self.contact):
            if not(self.move_info["saut"]):

                if self.move_info["right"] == True:
                    if (self.decalage + acc) <= vitesse:
                        self.decalage += acc
                    
                    elif self.decalage > vitesse:
                        self.decalage -= 1
                    

                
                elif self.move_info["left"] == True:
                    if (self.decalage - acc) >= -vitesse:
                        self.decalage -= acc

                    elif self.decalage < -vitesse:
                        self.decalage += 1

                else:
                    # vitesse de d'arret

                    # Gauche
                    if self.decalage < -1:
                        self.decalage += 1

                    elif self.decalage < 0:
                        self.decalage -= self.decalage

                    # Droite
                    elif self.decalage > 1:
                        self.decalage -= 1 

                    elif self.decalage > 0:
                        self.decalage -= self.decalage
                        




            else:
                if self.move_info["right"] == True:
                    if (self.decalage + acc * 0.5) <= vitesse * 1.1:
                        self.decalage += acc * 0.5
                    

                
                elif self.move_info["left"] == True:
                    if (self.decalage - acc * 0.5) >= -vitesse * 1.1:
                        self.decalage -= acc * 0.5
                
            

        else: # Si le joueur est en contacte d'un objet

            if self.move_info["right"] and self.move_possible["right"] and self.decalage >= 0:
                if (self.decalage + acc) <= vitesse:
                    self.decalage += acc
                
                elif self.decalage > vitesse:
                    self.decalage -= 1
                

            
            elif self.move_info["left"] and self.move_possible["left"] and self.decalage <= 0:
                if (self.decalage - acc) >= -vitesse:
                    self.decalage -= acc

                elif self.decalage < -vitesse:
                    self.decalage += 1

            else:
                self.decalage = 0


        self.decal -= self.decalage # Le fond bouge dans le sens inverse
        self.CoordonnerFictive += self.decalage
    
    def saveNumeroVague(self, numero):
        """Save the number of the wave
        sauvegarde le numero de la vague"""

        self.numVague = Decor.saveNumberRoman(numero, (200,200,200))
    
    def displayNumeroVague(self):
        """Display the number of the wave
        Affiche le numero de la vague"""

        X = self.longeur - self.longeur//4
        Y = 20

        if self.numVague != None:
            Decor.traceCadre(X, Y, 204, 50, 2, 0, (200,200,200), (0,0,0))
            EZ.trace_image(self.numVague, X + 2, Y + 2)