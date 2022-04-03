"""Fichier contenant l'ensemble des objet interactif du jeux"""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.InterfaceDynamique as ID


class ObjetInt:

    def __init__(self, name, xLeft, longeur = 0, hauteur = 0):
        self.name = name
        self.x = xLeft
        self.y = 0
        self.hitbox = [longeur, hauteur]
        self.charges = None


    def display(self, coordofictive):
        """affiche l'objet"""

        self.xFictif = self.x - coordofictive

        if self.charges == None:
            self.charge()

        self.zoneHitBox()
        EZ.trace_image(self.charges, int(self.xFictif), self.y)
        # self.traceHitbox()

    def zoneHitBox(self):
        """Definit la zone ou l'objet ne peut pas être traferser en donnant les 4 point du carre de la hitbox"""

        self.zoneHitBoxlist = [[self.xFictif , self.y], [self.xFictif + self.hitbox[0], self.y], [self.xFictif + self.hitbox[0], self.y + self.hitbox[1]], [self.xFictif, self.y + self.hitbox[1] ]]

    def traceHitbox(self):
        """Trace l'hitbox du joueur"""

        EZ.trace_segment(int(self.zoneHitBoxlist[0][0]),int(self.zoneHitBoxlist[0][1]), int(self.zoneHitBoxlist[1][0]), int(self.zoneHitBoxlist[1][1]))
        EZ.trace_segment(int(self.zoneHitBoxlist[1][0]),int(self.zoneHitBoxlist[1][1]), int(self.zoneHitBoxlist[2][0]), int(self.zoneHitBoxlist[2][1]))
        EZ.trace_segment(int(self.zoneHitBoxlist[2][0]),int(self.zoneHitBoxlist[2][1]), int(self.zoneHitBoxlist[3][0]), int(self.zoneHitBoxlist[3][1]))
        EZ.trace_segment(int(self.zoneHitBoxlist[3][0]),int(self.zoneHitBoxlist[3][1]), int(self.zoneHitBoxlist[0][0]), int(self.zoneHitBoxlist[0][1]))


class Border(ObjetInt):

    def __init__(self, name, xLeft):
        super().__init__(name, xLeft)
        self.hitbox = [223, ID.HAUTEUR]

    def charge(self):
        """Charge l'image de la bordur"""

        self.charges = EZ.charge_image("FichiersJeu\Interface\Entites\Items\Objet\BorderBox.png")



    