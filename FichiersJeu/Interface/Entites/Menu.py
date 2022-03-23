"""Fichier contenant l'ensemble des menu du jeu"""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
import FichiersJeu.Interface.Animation as Anim
import FichiersJeu.Interface.Decor as Decor



class Interface:
    """Class mere de toute les interface"""

    def __init__(self, longeur, hauteur):
        self.longeur = longeur
        self.hauteur = hauteur
        


class Menu(Interface):
    """Class du menu de base"""

    def __init__(self, longeur, hauteur):
        super().__init__(longeur, hauteur)

        self.chargesFond = None
        self.longeur = longeur
        self.hauteur = hauteur


    def displayFond(self):
        """Trace le fond du menu"""

        if self.chargesFond == None:
            self.chargeFond()

        EZ.trace_image(self.chargesFond ,0,0)
    

    def displayPlayer(self,image):
        """Trace le personnage"""

        EZ.trace_image(EZ.transforme_image(image,0,2), self.longeur//2-144, self.hauteur//2-144) # -144 pour le centrer, 48*6 / 2


class MenuPricipale(Menu):

    def __init__(self, longeur, hauteur):
        super().__init__(longeur, hauteur)
        self.etapeAnimationFond = 0 # etape de l'animation du fond
        
    def chargeFond(self):
        """Charge l'image du fond"""

        self.chargesFond = EZ.charge_image("FichiersJeu\Interface\Entites\Fond\Fond_menu2.png")

    def displayAnimationFond(self):
        """Trace l'animation de fond du menu"""
        Anim.traceAnimationFondMenuP(self.longeur, self.hauteur, self.etapeAnimationFond)
        if self.etapeAnimationFond < self.hauteur * 2:
            self.etapeAnimationFond += 1
        
        else:
            self.etapeAnimationFond = 0
    
    def displayMenu(self, personnage, gold):
        """Trace le Menu"""

        self.displayAnimationFond()
        self.displayFond() # Les boutton de l'interface
        self.displayPlayer(personnage)
        Decor.nombreDeGold(900, 10, gold)

class MenuDeath(Menu):

    def __init__(self, longeur, hauteur):
        super().__init__(longeur, hauteur)

    def chargeFond(self):
        """Charge l'image du fond"""

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
        """Charge l'image du fond"""

        self.chargesFond = EZ.charge_image("FichiersJeu\Interface\Entites\Fond\MenuGame.png")


class SousMenu(Menu):

    def __init__(self, longeur, hauteur):
        super().__init__(longeur, hauteur)
        self.tailleOmbrePolice = 3 # Size of the Shadow of the fonts / Taille de l'ombre de la police
        self.yDebutWidget = self.hauteur//6 # y Start of the widget / y de début du Widget
        self.hauteurWidget = int(3 * self.hauteur/4) # height of the widget / Hauteur du widget
        self.couleurBorder = (100, 100, 110) # color of the border / couleur de la bordure
        self.couleurFond = (210, 210, 230) # color of the background / couleur du fond

        #Police
        self.police = EZ.charge_police(50, "FichiersJeu\Interface\Entites\Police\CourageRoad.ttf", True)

    def chargeFond(self):
        """charge l'image du fond"""

        self.chargesFond = EZ.charge_image("FichiersJeu\Interface\Entites\Fond\FondSousMenu.png")


    def traceTitre(self, texte):
        """Draw the title of the subMenu
        trace le titre du sous-Menu

        Args:
            texte (str): Texte to drawn / texte a afficher
        """

        CoordonneesFonts = [self.longeur//2 - EZ.dimension(EZ.image_texte(texte, self.police, 0, 0, 0))[0], self.yDebutWidget- EZ.dimension(EZ.image_texte(texte, self.police, 0, 0, 0))[1]] # [x, y]

        EZ.trace_image(EZ.image_texte(texte, self.police, 0, 0, 0), CoordonneesFonts[0] + self.tailleOmbrePolice , CoordonneesFonts[1] + self.tailleOmbrePolice)
        EZ.trace_image(EZ.image_texte(texte, self.police, 255, 255, 255), CoordonneesFonts[0], CoordonneesFonts[1])

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
        if longueur < self.longeur:
            Decor.traceCadre(self.longeur//2 - longueur//2, self.yDebutWidget, longueur, self.hauteurWidget, 3, 2, self.couleurFond, self.couleurBorder)

        else:
            Decor.traceCadre(50, self.yDebutWidget, longueur, self.hauteurWidget, 3, 2, self.couleurFond, self.couleurBorder)
    

class Personnages(SousMenu):
    """Player Menu class / Class du Menu des personnages"""

    def __init__(self, longeur, hauteur, Inventaire = {}):
        super().__init__(longeur, hauteur)
        self.hauteurCardreJoueur = int(3 * self.hauteurWidget/4)
        self.largeurCadre = 300
        self.yDebutCadre = (self.hauteurWidget - self.hauteurCardreJoueur)//2 + self.yDebutWidget

        self.couleurFondCadreAchete = (200, 50, 50) 
        self.couleurBordureCadreAchete = (150, 0, 0) 

        self.couleurFondCadreEquipe = (50, 200, 50) 
        self.couleurBordureCadreEquipe = (0, 150, 0)

        self.chargesPersonnage = None

    
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
    
    def chargePersonnage(self):
        """load Caracters
        Charges les personnages
        """

        self.chargesPersonnage = {"Personnage1": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A2.png"), 0, 3),
    "Personnage2": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso2\Perso2A2.png"), 0, 3), 
    "Personnage3": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso3\Perso3A2.png"), 0, 3), 
    "Personnage4": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso4\Perso4A2.png"), 0, 3), 
    "Personnage5": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso5\Perso5A2.png"), 0, 3),
    "Personnage6": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso6\Perso6A2.png"), 0, 3),
    "Personnage7": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso7\Perso7A2.png"), 0, 3), 
    "Personnage8": EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso8\Perso8A2.png"), 0, 3) }





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

        else:
            Decor.traceCadre(x, self.yDebutCadre, self.largeurCadre, 3* self.hauteurCardreJoueur//4, 3, 2, self.couleurFondCadreAchete, self.couleurBordureCadreAchete)
            Decor.traceCadre(x, self.yDebutCadre + 3 *self.hauteurCardreJoueur//4, 300, self.hauteurCardreJoueur//4, 3, 2, self.couleurBordureCadreAchete, self.couleurBordureCadreAchete) # Haut du cadre

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
            xStart += self.largeurCadre//0.7
        
    
    def traceMenuPersonnages(self, x):
        """Drawn all the Menu of Caracters
        Trace tout le Menu des Personnages

        Args:
            x (int): x gap of widget / x du debut des Cadres
        """

        self.displayFond()
        self.traceFlecheRetour()
        self.TraceWidget(1200)
        self.traceTitre("PERSONNAGES")
        self.traceAllPersonnages(x + 100 )




class Game(Interface):

    def __init__(self, longeur, hauteur):
        super().__init__(longeur, hauteur)

        self.chargesFond = None
        self.decal = 0 # decalage de l'image 2
        self.decalage = 0     # decalage effectué
        self.CoordonnerFictive = 0 # Calcule le decalage total depuis le debut de la Game pour crée une impression de coordoner dans une map

        self.move_info = {"right": False, "left": False, "saut": False, "inertie": 0}
        self.move_possible = {"right": True, "left": True}  #Donne les deplacement que le joueur peux effectuer (permet d'interfire certain deplacement)
        self.contact = False


    def chargeFond(self):
        """Charge l'image du fond"""

        self.chargesFond = EZ.charge_image("FichiersJeu\Interface\Entites\Fond\FondGame.png")
    
    def displayFond(self, acc, vitesse):
        """Trace le fond du jeu"""

        LARGEUR_FOND = 2040

        if self.chargesFond == None:
            self.chargeFond()
        
        self.move(acc,vitesse)

        while not(0 <= self.decal <= LARGEUR_FOND):
            if self.decal > LARGEUR_FOND:
                self.decal -= LARGEUR_FOND

            elif self.decal < 0:
                self.decal += LARGEUR_FOND
        

        decal_x = [self.decal - LARGEUR_FOND, self.decal]

        for fond in range(2):
            EZ.trace_image(self.chargesFond ,decal_x[fond],0)

        
    

    def move(self, acc, vitesse):

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