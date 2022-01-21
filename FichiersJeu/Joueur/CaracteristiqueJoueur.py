"""Fichier Contenant la Base des fonctionaliter du Joueur"""


from pygame import time
import FichiersJeu.Interface.EZ as EZ

class Joueur:
    """Class joueur"""

    def __init__(self, name, level, personnage = "Perso1", stats = {"vie": 100, "damage": 10, "speed": 5 }, equipement = None):
        """Initialisation de Joueur

        Args:
            name (str): nom du joueur
            level (int): level du joueur
            personnage(str): nom du personnage
            stats (dic): toutes les stats du joueur [heal,dammage,speed]
            equipement (dic): Toutes ces objet [weapon, shield]
        """
        self.name = name
        self.level = level
        self.personnage = personnage
        self.stats = stats
        self.equipement = equipement
        self.x = 1240//2
        self.y = 470  #Hauteur de base du joueur
        self.y_base = 470
        self.move_info = {"right": False, "left": False, "saut": False}

        self.timeSaut = EZ.clock()
        self.charges = None  #Si l'image est chargé ou non

    def charge(self):
        """Foncton qui charge l'image du personage"""

        if self.personnage == "Perso1":
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A1.png"), 0, 3)
            self.chargesDroite = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A7.png"), 0, 3)
            self.chargesGauche = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A4.png"), 0, 3)


    def display(self):
        """Fonction qui trace le Joueur

        Args:
            x (int): x du joueur
            y (int): y du joueur
        """

        if self.charges == None:
            self.charge()
        
        self.move()
        self.effet_saut()

        EZ.trace_image(self.charges, self.x, self.y)

    """
    def moveRight(self):
        Deplace le joueur vers la droite
        self.x += self.stats["speed"]

    
    def moveLeft(self):
        Deplace le joueur vers la Gauche
        self.x -= self.stats["speed"]
    """

    def move(self):
        """Modifie l'aparence du personnage selon sa direction"""

        if self.move_info["right"] == True:
            #self.moveRight()
            self.charges = self.chargesDroite

        
        elif self.move_info["left"] == True:
            #self.moveLeft()
            self.charges = self.chargesGauche
        
        else:
            if not(self.move_info["saut"]):
                self.charges = self.chargesAvant
    
    def timer_saut(self):
        """Prend les seconde du debut du saut"""

        self.timeSaut = EZ.clock()

    
    def effet_saut(self):
        """Trajectoir du saut du joueur"""

        time = EZ.clock() - self.timeSaut
        if self.y <= self.y_base or time < 1:
            
            self.y = self.y_base - 120 * self.stats["speed"] * time + 0.5 * (9.81 * 80) * time**2

    
        
        

    


        



    







    



