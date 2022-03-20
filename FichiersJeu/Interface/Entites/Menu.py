"""Fichier contenant l'ensemble des menu du jeu"""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
import FichiersJeu.Interface.Entites.Bouton as Bouton
import FichiersJeu.Interface.Animation as Anim




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

        
    def chargeFond(self):
        """Charge l'image du fond"""

        self.chargesFond = EZ.charge_image("FichiersJeu\Interface\Entites\Fond\Fond_menu2.png")
    
    def displayBoutonPlay(self):

        Bouton.BoutonPlayMenu(465, 550)

    
    def displayMenu(self, personnage):
        """Trace le Menu"""

        self.displayFond()
        self.displayPlayer(personnage)
        self.displayBoutonPlay()

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