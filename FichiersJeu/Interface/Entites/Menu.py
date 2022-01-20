"""Fichier contenant l'ensemble des menu du jeu"""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.CaracteristiqueJoueur as CJ
import FichiersJeu.Interface.Entites.Bouton as Bouton


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
    
    def chargeFond(self):
        """Charge l'image du fond"""

        self.chargesFond = EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Fond\Fond_menu.png")

    def displayFond(self):
        """Trace le fond du menu"""

        if self.chargesFond == None:
            self.chargeFond()

        EZ.trace_image(self.chargesFond ,0,0)
    
    def displayPlayer(self,image,longeur = 1240, hauteur = 720):
        """Trace le personnage"""

        EZ.trace_image(image, longeur, hauteur)
    
    def displayBoutonPlay(self):

        Bouton.BoutonPlayMenu(800, 550)

    
    def displayMenu(self, personnage, longeur = 0, hauteur = 0):
        """Trace le Menu"""

        self.displayFond()
        self.displayPlayer(personnage, longeur, hauteur)
        self.displayBoutonPlay()


