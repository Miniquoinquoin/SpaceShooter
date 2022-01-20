"""Fichier Contenant la Base des fonctionaliter du Joueur"""

from re import X
import FichiersJeu.Interface.EZ as EZ

class Joueur:
    """Class joueur"""

    def __init__(self, name, level, stats = {"vie": 100, "damage": 10, "speed": 3 }, equipement = None):
        """Initialisation de Joueur

        Args:
            name (str): nom du joueur
            level (int): level du joueur
            stats (liste): toutes les stats du joueur [heal,dammage,speed]
            equipement (liste): Toutes ces objet [weapon, shield]
        """
        self.name = name
        self.level = level
        self.stats = stats
        self.equipement = equipement
        self.x = 1240//2
        self.y = 300
        self.move_info = {"right": False, "left": False}

        self.charges = None  #Si l'image est chargé ou non

    def charge(self):
        """Foncton qui charge l'image du personage"""
        self.chargesAvant = EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A1.png")
        self.chargesDroite = EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A7.png")
        self.chargesGauche = EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A4.png")


    def display(self):
        """Fonction qui trace le Joueur

        Args:
            x (int): x du joueur
            y (int): y du joueur
        """

        if self.charges == None:
            self.charge()
        
        self.move()

        EZ.trace_image(self.charges, self.x, self.y)

    def moveRight(self):
        """Deplace le joueur vers la droite"""
        self.x += self.stats["speed"]

    
    def moveLeft(self):
        """Deplace le joueur vers la Gauche"""
        self.x -= self.stats["speed"]
    
    def move(self):

        if self.move_info["right"] == True:
            self.moveRight()
            self.charges = self.chargesDroite

        
        elif self.move_info["left"] == True:
            self.moveLeft()
            self.charges = self.chargesGauche
        
        else:
            self.charges = self.chargesAvant
        

        
        

    


        



    







    



