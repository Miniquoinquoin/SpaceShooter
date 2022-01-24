"""Fichier contenant les diferant proprieter des armes / attack"""

import FichiersJeu.Interface.EZ as EZ
class Armes:

    def __init__(self, name, damage, ranges, hitbox):
        self.name = name
        self.damage = damage
        self.range = ranges
        self.hitbox = hitbox

        self.charges = None
        self.x = 1300
        self.y = 0
        self.direction = "right"



    def display(self, vitesse, vitesseFond):
        """Trace l'arme"""
        if self.charges == None:
            self.charge()

        self.move(vitesse, vitesseFond, self.direction)

        EZ.trace_image(self.charges, self.x, self.y)


    def Setup(self, x, y, direction):
        """Charge les info au moment du lancement de l'attack

        Args:
            x (int): cordonner x du joueur
            y (int): coordonne y du joueur
        """
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, vitesse, vitesseFond, direction):
        """Deplace le shuriken"""
        if direction == "right":
            self.x += vitesse - vitesseFond
            print(vitesse - vitesseFond)
        else:
            self.x -= vitesse + vitesseFond
            print(vitesse + vitesseFond)
        

            
    

class Shuriken(Armes):

    def __init__(self, name, damage, ranges, hitbox):
        super().__init__(name, damage, ranges, hitbox)

    
    def charge(self):
        """Charge l'image du shuriken"""
        self.charges = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Arme\Arme2\Arme2.png"),0,2)
        self.speed = 10
    
    