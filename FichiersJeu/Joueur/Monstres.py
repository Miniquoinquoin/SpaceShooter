"""Fichier avec les proprieter des monstres"""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.InterfaceDynamique as ID

class Monstre:

    def __init__(self, name, level, xPlayer):

        self.name = name
        self.level = level

        self.stats = {"vie": 100*(level//10)**2, "damage": 10*(level//10)**2, "range": 300 ,"speed": 3, "jumpPower": 1 }
        self.hitbox = [50, 100] #Modifier au moment du chargement du monstre

        self.charges = None
        self.lastchargesRight = [0, 0, 10] # [Etape du gif originale, repetiton, nombre de repetition avant changement]
        self.lastchargesLeft = [0, 0, 10] # [Etape du gif originale, repetiton, nombre de repetition avant changement]

        self.move_info = {"right": True, "left": False}
        self.x = 0
        self.y = ID.HAUTEUR_SOL - self.hitbox[1]
        self.xPlayer = xPlayer


    def charge(self):
        """Charge le monstre en fonction de son nom"""

        if self.name == "Amalgam_Sprite":
            self.chargesRight = [EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-0.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-1.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-2.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-3.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-4.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-5.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-6.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-7.png")]
            self.chargesLeft = [EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-0.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-1.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-2.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-3.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-4.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-5.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-6.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-7.png")]
            self.hitbox = [93, 90]
            self.charges = self.chargesRight[self.lastchargesRight[0]]

    def display(self, vitesseFond):
        """Affiche le monstre"""

        if self.charges == None:
            self.charge()

        self.move(vitesseFond)
        EZ.trace_image(self.charges, self.x, self.y)

    
    def moveEffectRight(self):
        """Cree l'effet de vie du monstre vers la droite"""

        if self.lastchargesRight[1] >= self.lastchargesRight[2]:
            if self.lastchargesRight[0] >= len(self.chargesRight):
                self.lastchargesRight[0] = 0

            self.charges = self.chargesRight[self.lastchargesRight[0]]
            self.lastchargesRight[0] += 1

        else:
            self.lastchargesRight[1] += 1

    
    def moveEffectLeft(self):
        """Cree l'effet de vie du monstre vers la droite"""
        
        if self.lastchargesLeft[1] >= self.lastchargesLeft[2]:
            if self.lastchargesLeft[0] >= len(self.chargesRight):
                self.lastchargesLeft[0] = 0

            self.charges = self.chargesLeft[self.lastchargesLeft[0]]
            self.lastchargesLeft[0] += 1

        else:
            self.lastchargesLeft[1] += 1

    def moveEffect(self):
        """Donne le bonne effet au monstre suivant si il va a droite ou a gauche"""

        if self.move_info["right"]:
            self.moveEffectRight()
            
        elif self.move_info["left"]:
            self.moveEffectLeft()

    def moveX(self, vitesseFond):
        """Deplace le monstre

        Args:
            vitesseFond (float): deplacement du fond
        """

        if self.move_info["right"]:
            self.x += self.stats["speed"] - vitesseFond

        elif self.move_info["left"]:
            self.x -= self.stats["speed"] + vitesseFond



    def move(self, vitesseFond):
        """Deplace le monstre en fonction de la position du joueur

        Args:
            vitesseFond (float): deplacement du fond
        """
        

        if self.x < self.xPlayer:
            self.move_info["right"] = True
            self.move_info["left"] = False
        
        elif self.x > self.xPlayer:
            self.move_info["left"] = True
            self.move_info["right"] = False

        self.moveX(vitesseFond)
        self.moveEffect()




        
        



# class Monstre_sol(Monstre):

#     def __init__(self, name, level):
#         super().__init__(name, level)

    
    
            

