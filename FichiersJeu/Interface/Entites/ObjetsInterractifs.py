"""Fichier contenant l'ensemble des objet interactif du jeux"""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.InterfaceDynamique as ID


class ObjetInt:

    def __init__(self, name, xLeft, yTop, longeur = 0, hauteur = 0):
        self.name = name
        self.x = xLeft
        self.y = 1280
        self.hitbox = [longeur, hauteur]
        self.charges = None


    def display(self, coordofictive):
        """affiche l'objet"""

        if self.charges == None:
            self.charge()

        self.zoneHitBox()
        EZ.trace_image(self.charges, int(self.x - coordofictive), self.y)
        print(f"Coordo {self.name} : {self.x - coordofictive}")

    def zoneHitBox(self):
        """Definit la zone ou l'objet ne peut pas être traferser en donnant les 4 point du carre de la hitbox"""

        self.zoneHitBoxlist = [[self.x, self.y], [self.x + self.hitbox[0], self.y], [self.x + self.hitbox[0], self.y + self.hitbox[1]], [self.x, self.y + self.hitbox[1] ]]


class Border(ObjetInt):

    def __init__(self, name, xLeft, yTop):
        super().__init__(name, xLeft, yTop)
        self.hitbox = [223, ID.HAUTEUR]
        self.y = ID.HAUTEUR

    def charge(self):
        """Charge l'image de la bordur"""

        self.charges = EZ.charge_image("FichiersJeu\Interface\Entites\Items\Objet\BorderBox.png")



    