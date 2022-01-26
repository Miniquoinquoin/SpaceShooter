"""Fichier contenant les diferant proprieter des armes / attack"""

from re import S
import FichiersJeu.Interface.EZ as EZ
class Armes:

    def __init__(self, name, damage, ranges, hitbox):
        self.name = name
        self.damage = damage
        self.range = [ranges, 0] # [De base, pendant le tire]
        self.hitbox = hitbox

        self.charges = None
        self.x = 1300
        self.y = 0
        self.xSetup = 1300
        
        self.direction = "right"
        self.inertie = 0



    def display(self, vitesse, vitesseFond):
        """Trace l'arme"""
        if self.charges == None:
            self.charge()

        if self.xSetup - self.range[1] <= self.x <= self.xSetup + self.range[1]:
            self.move(vitesse, vitesseFond, self.direction)

            EZ.trace_image(self.charges, self.x, self.y)


    def Setup(self, x, y, direction, inertie):
        """Charge les info au moment du lancement de l'attack

        Args:
            x (int): cordonner x du joueur
            y (int): coordonne y du joueur
        """
        self.x = x
        self.y = y
        self.xSetup = x

        self.direction = direction
        self.inertie = inertie

        if direction == "right":
            self.range[1] = self.range[0] * (1 + inertie/10)
        
        else:
            self.range[1] = self.range[0] * (1 - inertie/10)


    def move(self, vitesse, vitesseFond, direction):
        """Deplace le shuriken"""
        if direction == "right":
            self.x += vitesse - vitesseFond + self.inertie

        else:
            self.x -= vitesse + vitesseFond - self.inertie

        self.xSetup -= vitesseFond
            
        

            
    

class Shuriken(Armes):

    def __init__(self, name, damage, ranges, hitbox):
        super().__init__(name, damage, ranges, hitbox)

    
    def charge(self):
        """Charge l'image du shuriken"""
        self.charges = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Arme\Arme2\Arme2.png"),0,2)
        self.speed = 10
    
    