"""Fichier contenant les diferant proprieter des armes / attack"""

from unicodedata import name
import FichiersJeu.Interface.EZ as EZ
class Armes:

    def __init__(self, name, damage, ranges, durability, level = 1):
        self.name = name
        self.level = level
        self.damage = { "damage": damage, "basicDamage": damage}
        self.range = [ranges, 0] # [De base, pendant le tire]
        self.durability = [durability, durability] # [Durabiliter totale, duribiliter restante]
        self.hitbox = [50, 50] #Modifier pendant le chargement de l'image

        self.chargesB = None
        self.x = 1300
        self.y = 0
        self.hauteurTir = 50 # hauteur du tir entre le haut du personnage et l'arme / Height of the shot between the top of the character and the weapon
        self.RotationSpeed = [0,0] # vitesse de rotation de l'arme [degres par tick, degres actuel] / Rotation speed of the weapon [degrees per tick, current degrees]
        self.xSetup = 1300 #Position de l'amre lors du tirs permet de verifier si l'arme est toujours dans la porter de tire du joueur / Position of the weapon when the shot is fired to check if the weapon is still in the player's range
        
        self.direction = "right"
        self.inertie = 0

        self.Break = False # Definit si l'arme est casser ou non


    def charge(self):
        """load weapon
        charge l'arme
        """
        if self.name == "Hache":
            self.chargesB = EZ.transforme_image(EZ.charge_image(f"FichiersJeu\Interface\Entites\Items\Arme\Arme1\Arme1lvl{self.level}.png"),0,2)
            self.RotationSpeed = [5,0]

        elif self.name == "Dague":
            self.chargesB = EZ.transforme_image(EZ.charge_image(f"FichiersJeu\Interface\Entites\Items\Arme\Arme2\Arme2lvl{self.level}.png"),0,2)
            self.RotationSpeed = [10,0]

        elif self.name == "BouleElectrique":
            self.chargesB = EZ.transforme_image(EZ.charge_image(f"FichiersJeu\Interface\Entites\Items\Arme\Arme3\Arme3lvl{self.level}.png"),90,0.2)
            self.RotationSpeed = [5,0]
        
        elif self.name == "Epee":
            self.chargesB = EZ.transforme_image(EZ.charge_image(f"FichiersJeu\Interface\Entites\Items\Arme\Arme4\Arme4lvl{self.level}.png"),0,2)
            self.RotationSpeed = [5,0]
        
        elif self.name == "Flechette":
            self.chargesB = EZ.transforme_image(EZ.charge_image(f"FichiersJeu\Interface\Entites\Items\Arme\Arme5\Arme5lvl{self.level}.png"),0,1)
            self.hauteurTir = 70
            
        elif self.name == "Lance":
            self.chargesB = EZ.transforme_image(EZ.charge_image(f"FichiersJeu\Interface\Entites\Items\Arme\Arme6\Arme6lvl{self.level}.png"),0,0.5)
        
        elif self.name == "BouleDeFeu":
            self.chargesB = EZ.transforme_image(EZ.charge_image(f"FichiersJeu\Interface\Entites\Items\Arme\Arme7\Arme7lvl{self.level}.png"),180,0.5)
        
        elif self.name == "Shuriken":
            self.chargesB = EZ.transforme_image(EZ.charge_image(f"FichiersJeu\Interface\Entites\Items\Arme\Arme8\Arme8lvl{self.level}.png"),0,2)
            self.RotationSpeed = [15,0]
        

        
        self.hitbox = [EZ.dimension(self.chargesB)[0], EZ.dimension(self.chargesB)[1]]


    def display(self, vitesse, vitesseFond):
        """Trace l'amre

        Args:
            vitesse (int): vitesse de l'arme definit dans caracteristiqueJoueur
            vitesseFond (float): vittesse de deplacement du fond
        """
        if self.chargesB == None:
            self.charge()

        self.verifDurability()
        if not(self.Break):
            self.move(vitesse, vitesseFond, self.direction)
            self.zoneHitBox()

            self.trace_arme()
        
        else:
            self.y = 9999 # evite que l'arme cose des degat alors quel et pas afficher
            self.zoneHitBox()

    def trace_arme(self):
        """Trace l'arme"""
        EZ.trace_image(self.charges, self.x, self.y)


    def Setup(self, x, y, direction, inertie = 0):
        """Charge les info au moment du lancement de l'attack

        Args:
            x (int): cordonner x du joueur
            y (int): coordonne y du joueur
            direction (str): direction du joueur / dans le quel va aller l'arme
            inertie (float): vitesse du jouer
        """
        self.y = y + self.hauteurTir
        

        self.durability[1] = self.durability[0] # repart l'arme
        self.Break = False

        self.direction = direction
        self.inertie = inertie

        self.damage["damage"] = self.damage["basicDamage"] * (1+abs(inertie)/5)

        if direction == "right":
            self.range[1] = self.range[0] * (1 + inertie/10) # donne une range plus grand quand le joueur court / give a range bigger when the player is running
            self.RotationSpeed[1] = 0 if self.RotationSpeed[0] != 0 else 180 # Rotation de l'arme si l'arme a une rotation / rotate the weapon if the weapon has a rotation

            self.xSetup = x
            self.x = x
        
        else:
            self.range[1] = self.range[0] * (1 - inertie/10) # donne une range plus grand quand le joueur cour / give a range bigger when the player is running
            self.RotationSpeed[1] = -90 if self.RotationSpeed[0] != 0 else 0 # Rotation de l'arme si l'arme a une rotation / rotate the weapon if the weapon has a rotation

            self.xSetup = x - self.hitbox[0] # position de l'arme - self.hitbox[0] pour que l'arme soit a gauche du joueur / position of the weapon - self.hitbox[0] to make the weapon to the left of the player
            self.x = x - self.hitbox[0] #        ^^^^^^^^


    def move(self, vitesse, vitesseFond, direction):
        """Deplace l'arme

        Args:
            vitesse (int): vitesse de l'arme definie dans CaracteristiqueJoueur
            vitesseFond (float): vitesse de deplacement du fond
            direction (str): direction de l'arme
        """
        if direction == "right":
            self.x += vitesse - vitesseFond + self.inertie
            self.RotationSpeed[1] -= self.RotationSpeed[0]
            self.charges = EZ.transforme_image(self.chargesB, self.RotationSpeed[1], 1)

        else:
            self.x -= vitesse + vitesseFond - self.inertie
            self.RotationSpeed[1] += self.RotationSpeed[0]
            self.charges = EZ.transforme_image(self.chargesB, self.RotationSpeed[1], 1)

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
        if self.durability[1] <= 0 or not(self.xSetup - self.range[1] <= self.x <= self.xSetup + self.range[1]):
            self.Break = True

        else:
            self.Break = False
            
    


class ArmesAvecForme(Armes):

    def __init__(self, name, damage, ranges, durability):
        super().__init__(name, damage, ranges, durability)
        self.color = [0,0,0] #Couleur de l'arme
        self.forme = "DISQUE" #Forme de l'arme "DISQUE" / "CARRE"
        self.size = 10 # Rayon du disque pour un disque / Taille d'un coter pour un carré

    def charge(self):

        if self.name == "Ammonite_Sprite":
            self.color = [0, 200, 0]
            self.forme = "DISQUE"
            self.size = 7

    def trace_arme(self):
        """Trace l'arme"""

        if self.forme == "DISQUE":
            EZ.trace_disque(int(self.x), int(self.y), self.size, *self.color)
        
        elif self.forme == "CARRE":
            EZ.trace_rectangle_droit_v2(int(self.x - self.size/2), int(self.y - self.size/2), self.size, self.size, *self.color)
            

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



    