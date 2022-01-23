"""Fichier Contenant la Base des fonctionaliter du Joueur"""


from cmath import pi
from pygame import time
import FichiersJeu.Interface.EZ as EZ

class Joueur:
    """Class joueur"""

    def __init__(self, name, level, personnage = 1, stats = {"vie": 100, "damage": 10, "acc": 1,"speed": 8, "jumpPower": 1 }, equipement = None):
        """Initialisation de Joueur

        Args:
            name (str): nom du joueur
            level (int): level du joueur
            personnage(str): nom du personnage
            stats (dic): toutes les stats du joueur {"vie": 100, "damage": 10, "acc": 1,"speed": 10, "jumpPower": 2 }
            equipement (dic): Toutes ces objet [weapon, shield]
        """
        self.name = name
        self.level = level
        self.personnage = personnage
        self.stats = stats
        self.equipement = equipement
        self.x = 1240//2
        self.y = 200  #Hauteur de base du joueur
        self.y_sol = 470
        self.move_info = {"right": False, "left": False, "saut": False}

        self.timeSaut = EZ.clock()
        self.charges = None  #Si l'image est chargé ou non

        # Dernier charge effectuer
        self.lastchargesRight = [0, 1, 0] # [0 = PasArrier / 1 = Pied coller / 2 = Pied avant, 0 = Pas arrier / 1 = Pied avant, repetiton(0, 5)]
        self.lastchargesLeft = [0, 1, 0] # [0 = PasArrier / 1 = Pied coller / 2 = Pied avant, 0 = Pas arrier / 1 = Pied avant, repetition(0,5)]

    def charge(self):
        """Foncton qui charge l'image du personage"""

        if self.personnage == 1:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A2.png"), 0, 3)
            self.chargesRight = [EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A7.png"), 0, 3),EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A8.png"), 0, 3),EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A9.png"), 0, 3)]
            self.chargesLeft = [EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A4.png"), 0, 3),EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A5.png"), 0, 3),EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A6.png"), 0, 3)]

        elif self.personnage == 2:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso2\Perso2A2.png"), 0, 3)
            self.chargesRight = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso2\Perso2A7.png"), 0, 3)
            self.chargesLeft = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso2\Perso2A4.png"), 0, 3)

        elif self.personnage == 3:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso3\Perso3A2.png"), 0, 3)
            self.chargesRight = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso3\Perso3A7.png"), 0, 3)
            self.chargesLeft = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso3\Perso3A4.png"), 0, 3)

        elif self.personnage == 4:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso4\Perso4A2.png"), 0, 3)
            self.chargesRight = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso4\Perso4A7.png"), 0, 3)
            self.chargesLeft = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso4\Perso4A4.png"), 0, 3)

        elif self.personnage == 5:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso5\Perso5A2.png"), 0, 3)
            self.chargesRight = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso5\Perso5A7.png"), 0, 3)
            self.chargesLeft = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso5\Perso5A4.png"), 0, 3)

        elif self.personnage == 6:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso6\Perso6A2.png"), 0, 3)
            self.chargesRight = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso6\Perso6A7.png"), 0, 3)
            self.chargesLeft = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso6\Perso6A4.png"), 0, 3)

        elif self.personnage == 7:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso7\Perso7A2.png"), 0, 3)
            self.chargesRight = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso7\Perso7A7.png"), 0, 3)
            self.chargesLeft = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso7\Perso7A4.png"), 0, 3)
        
        elif self.personnage == 8:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso8\Perso8A2.png"), 0, 3)
            self.chargesRight = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso8\Perso8A7.png"), 0, 3)
            self.chargesLeft = EZ.transforme_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Items\Personnages\Perso8\Perso8A4.png"), 0, 3)




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

    def moveRight(self):
        """Cree l'effet marcher vers la droite"""

        if self.lastchargesRight[2] >= 100//self.stats["speed"]:  # Time de marche pour eviter la marche trop rapide
            self.lastchargesRight[2] = 0

            if self.lastchargesRight[0] == 0:
                self.lastchargesRight[0] = 1
                return self.chargesRight[0]
            
            elif self.lastchargesRight[0] == 2:
                self.lastchargesRight[0] = 1
                return self.chargesRight[2]
            
            elif self.lastchargesRight[0] == 1:
                if self.lastchargesRight[1] == 0:
                    self.lastchargesRight = [2,1,self.lastchargesRight[2]]
                    return self.chargesRight[1]
                    
                elif self.lastchargesRight[1] == 1:
                    self.lastchargesRight = [0,0,self.lastchargesRight[2]]
                    return self.chargesRight[1]
        
        else:
            self.lastchargesRight[2] += 1
            return self.chargesRight[self.lastchargesRight[0]]

    def moveLeft(self):
        """Cree l'effet marcher vers la droite"""

        if self.lastchargesLeft[2] >= 100//self.stats["speed"]:  # Time de marche pour eviter la marche trop rapide
            self.lastchargesLeft[2] = 0

            if self.lastchargesLeft[0] == 0:
                self.lastchargesLeft[0] = 1
                return self.chargesLeft[0]
            
            elif self.lastchargesLeft[0] == 2:
                self.lastchargesLeft[0] = 1
                return self.chargesLeft[2]
            
            elif self.lastchargesLeft[0] == 1:
                if self.lastchargesLeft[1] == 0:
                    self.lastchargesLeft = [2,1,self.lastchargesLeft[2]]
                    return self.chargesLeft[1]
                    
                elif self.lastchargesLeft[1] == 1:
                    self.lastchargesLeft = [0,0,self.lastchargesLeft[2]]
                    return self.chargesLeft[1]
        
        else:
            self.lastchargesLeft[2] += 1
            return self.chargesLeft[self.lastchargesLeft[0]]



    def move(self):
        """Modifie l'aparence du personnage selon sa direction"""

        if not(self.move_info["saut"]):

            if self.move_info["right"] == True:
                #self.moveRight()
                self.charges = self.moveRight()

            
            elif self.move_info["left"] == True:
                #self.moveLeft()
                self.charges = self.moveLeft()
            
            else:
                self.charges = self.chargesAvant
        
        else:

            if self.move_info["right"] == True:
                #self.moveRight()
                self.charges = self.chargesRight[0]

            
            elif self.move_info["left"] == True:
                #self.moveLeft()
                self.charges = self.chargesLeft[0]

    
    def timer_saut(self):
        """Prend les seconde du debut du saut"""

        self.timeSaut = EZ.clock()

    
    def effet_saut(self):
        """Trajectoir du saut du joueur"""

        time = EZ.clock() - self.timeSaut
        if self.y < self.y_sol or time < 0.1:
            
            self.y = self.y_sol - (self.stats["jumpPower"] * 100)* (self.stats["speed"] * time - ((1 + self.stats["speed"]/50)**2) * 0.5 * 9.81 * time**2)
        
        else:
            self.move_info["saut"] = False
            self.y = self.y_sol

    
        
        

    


        



    







    



