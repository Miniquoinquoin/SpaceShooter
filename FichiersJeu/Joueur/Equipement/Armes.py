"""Fichier contenant les diferant proprieter des armes / attack"""

from re import S
import FichiersJeu.Interface.EZ as EZ
class Armes:

    def __init__(self, name, damage, ranges):
        self.name = name
        self.damage = damage
        self.range = [ranges, 0] # [De base, pendant le tire]
        self.durability = [3, 0]
        self.hitbox = [50, 50] #Modifier pendant le chargement de l'image

        self.charges = None
        self.x = 1300
        self.y = 0
        self.xSetup = 1300
        
        self.direction = "right"
        self.inertie = 0

        self.Break = False # Definit si l'arme est casser ou non



    def display(self, vitesse, vitesseFond):
        """Trace l'amre

        Args:
            vitesse (int): vitesse de l'arme definit dans caracteristiqueJoueur
            vitesseFond (float): vittesse de deplacement du fond
        """
        if self.charges == None:
            self.charge()

        self.verifDurability()
        if self.xSetup - self.range[1] <= self.x <= self.xSetup + self.range[1] and not(self.Break):
            self.move(vitesse, vitesseFond, self.direction)
            self.zoneHitBox()

            EZ.trace_image(self.charges, self.x, self.y)
        
        else:
            self.y = 9999 # evite que l'arme cose des degat alors quel et pas afficher
            self.zoneHitBox()

        


    def Setup(self, x, y, direction, inertie):
        """Charge les info au moment du lancement de l'attack

        Args:
            x (int): cordonner x du joueur
            y (int): coordonne y du joueur
            direction (str): direction du joueur / dans le quel va aller l'arme
            inertie (float): vitesse du jouer
        """
        self.x = x
        self.y = y
        self.xSetup = x

        self.durability[1] = self.durability[0] # repart l'arme
        self.Break = False

        self.direction = direction
        self.inertie = inertie

        if direction == "right":
            self.range[1] = self.range[0] * (1 + inertie/10) # donne une range plus grand quand le joueur court
        
        else:
            self.range[1] = self.range[0] * (1 - inertie/10) # donne une range plus grand quand le joueur cour


    def move(self, vitesse, vitesseFond, direction):
        """Deplace l'arme

        Args:
            vitesse (int): vitesse de l'arme definie dans CaracteristiqueJoueur
            vitesseFond (float): vitesse de deplacement du fond
            direction (str): direction de l'arme
        """
        if direction == "right":
            self.x += vitesse - vitesseFond + self.inertie

        else:
            self.x -= vitesse + vitesseFond - self.inertie

        self.xSetup -= vitesseFond
    

    def zoneHitBox(self):
        """Definit la zone ou le monstre prend des degats en donnant les 4 point du carre de la hitbox"""

        self.zoneHitBoxlist = [[self.x, self.y], [self.x + self.hitbox[0], self.y], [self.x + self.hitbox[0], self.y + self.hitbox[1]], [self.x, self.y + self.hitbox[1] ]]

    def use(self):
        """Utilise l'arme lui retire 1 de dura"""

        self.durability[1] -= 1
    


    def verifDurability(self):
        """Verifie sur l'arme est casser


        Returns:
            bool: True si arme encore utilisable False si arme casser
        """
        if self.durability[1] <= 0:
            self.Break = True

        else:
            self.Break = False
            
    

class Shuriken(Armes):

    def __init__(self, name, damage, ranges, durability):
        super().__init__(name, damage, ranges)
        self.durability = [durability, durability] # [Durabiliter totale, duribiliter restante]


    def charge(self):
        """Charge l'image du shuriken"""
        self.charges = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Arme\Arme2\Arme2.png"),0,2)
        self.hitbox = [48, 48]





    