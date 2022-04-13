"""Fichier contenant la classe Equipement"""

import FichiersJeu.Interface.Decor as Decor
import FichiersJeu.Interface.EZ as EZ
import math

class Equipement:
    """Class for the equipment
    classe pour les équipements"""

    def __init__(self, nom, type, cooldown = 30):
        """Constructor for the equipment
        constructeur pour les équipements"""
        self.nom = nom
        self.type = type #shield, grenade, potion
        self.cooldown = {"cooldown": cooldown, "timer": 0, "printTimer": 0, "lastState": "usable"}
        self.largeur = 50
        self.hauteur = 50
        self.chargeImage()
    
    def chargeImage(self):
        """Charge the image of the equipment
        charge l'image de l'équipement"""

        if self.type == "shield":
            self.chargesImage = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Equipement\Bouclier.png"),0,0.17)
        
        elif self.type == "grenade":
            self.chargesImage = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Equipement\Grenade.png"),0,0.17)
            self.hitBox = [EZ.dimension(self.chargesImage)[0],EZ.dimension(self.chargesImage)[1]]

            self.numberPictureAnimation = 25
            self.chargesExplosion = [EZ.charge_image(f"FichiersJeu\Interface\Entites\Items\ImageInterface\Equipement\ExplosionGrenade\ExplosionGrenade_{n}.png") for n in range(self.numberPictureAnimation)]
            self.lastchargesExplosion = self.numberPictureAnimation
            self.hitBoxExplosion = [EZ.dimension(self.chargesExplosion[0])[0],EZ.dimension(self.chargesExplosion[0])[1]]

        
        elif self.type == "potion":
            self.chargesImage = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Equipement\Potion.png"),0,0.17)

    
    def traceInfoEquipement(self,x,y):
        """Trace the equipment info at the right top in game
        trace les infos de l'équipement en haut à droite dans le jeu"""

        Decor.traceCadre(x,y,self.largeur,self.hauteur,2,0,(33,47,61),(128,139,151))

        if self.type == "shield" and self.durability[0] > 0:
            EZ.trace_image(self.chargesImage,x+8,y+4)
        
        elif self.type == "grenade" and self.usable:
            EZ.trace_image(self.chargesImage,x+8,y+4)
    
        elif self.type == "potion" and self.usable:
            EZ.trace_image(self.chargesImage,x+8,y+4)
        
        else:
            self.chekRepair()
            EZ.trace_image(EZ.image_texte(str(int(self.cooldown["printTimer"])),EZ.charge_police(40,"FichiersJeu\Interface\Entites\Police\JosefinSans-BoldItalic.ttf"),255,255,255),x+2 + self.largeur//2 - EZ.dimension(EZ.image_texte(str(int(self.cooldown["printTimer"])),EZ.charge_police(40,"FichiersJeu\Interface\Entites\Police\PermanentMarker-Regular.ttf"),255,255,255))[0]//2,y+7)


    def chekRepair(self):
        """Check if the equipment can be repaired and repair it if it can
        vérifie si l'équipement peut être réparé et le répare si c'est possible"""
        
        if self.cooldown["lastState"] == "usable":
            self.cooldown["timer"] = self.cooldown["cooldown"] + EZ.clock()
            self.cooldown["lastState"] = "cooldown"
        
        elif self.cooldown["timer"] <= EZ.clock(): # if the equipment is not usable and the timer is over / si l'équipement n'est pas utilisable et que le timer est écoulé
            self.repair()
        
        else:
            self.cooldown["printTimer"] = self.cooldown["timer"] - EZ.clock() # Calculate the timer before the equipment can be used again / calcule le timer avant que l'équipement puisse être utilisé à nouveau

    def repair(self):
        """start the Repair of the equipment
        démarre la réparation de l'équipement"""

        self.cooldown["lastState"] = "usable" # set the last state to usable / met le dernier état à utilisable


class Bouclier(Equipement):
    """Class for the shield
    classe pour le bouclier"""
    
    def __init__(self, durability, cooldown = 30):
        """Constructor for the shield
        constructeur pour le bouclier"""
        super().__init__("Bouclier", "shield", cooldown)
        self.chargeImage()
        self.durability = [durability, durability] # [durability, maxDurability]
    
    def use(self):
        """Use the shield
        utilise le bouclier"""

        self.durability[0] -= 1
    
    def getDurability(self):
        """Get the shield durability
        obtient la durabilité du bouclier"""
            
        return self.durability[0] #return the shield durability
    
    def isBroken(self):
        """Check if the shield is broken
        vérifie si le bouclier est cassé"""

        if self.durability[0] <= 0:
            return True
        else:
            return False
        
    def repair(self):
        """Repair the shield
        répare le bouclier"""

        super().repair()
        self.durability[0] = self.durability[1]
    


class Grenade(Equipement):
    """Class for the grenade
    classe pour la grenade"""

    def __init__(self, efficiency, hauteurSol ,cooldown = 5):
        """Constructor for the grenade
        constructeur pour la grenade"""
        super().__init__("Grenade", "grenade", cooldown)
        self.chargeImage()
        self.efficiency = efficiency
        self.usable = True
        self.timeShoot = [0.5, 0] # [TimeBeforGrenadeExplosion, TimeOnStartOfShoot]
        self.hauteurSol = hauteurSol
        self.y = 720 # y position of the grenade / position y de la grenade
        self.x = 0 # x position of the grenade / position x de la grenade
        self.zoneHitBox()

        self.SpeedShooter = 1 # speed of the shooter at the time of shooting / vitesse du tireur au moment du tir

        self.canExplode = False # check if the grenade can explode / vérifie si la grenade peut exploser
        self.DoDamage = False # check if the grenade must still do damage / vérifie si la grenade doit encore faire des dégâts
    
    def getEfficiency(self):
        """Get the grenade efficiency
        obtient l'efficacité de la grenade"""

        return self.efficiency
    

    def getDoDamage(self):
        """Return True if the grenade can do damage
        retourne True si la grenade peut faire des dégâts"""
    
        return self.DoDamage
    
    def SetDoDamage(self, value):
        """Set the grenade to do damage or not
        définit si la grenade fait des dégâts ou pas"""

        self.DoDamage = value

    
    def use(self, xShooter, yShooter, direction, hitBoxXShooter, SpeedShooter):
        """Use the grenade
        utilise la grenade"""

        self.usable = False
        self.shoot(xShooter, yShooter, direction, hitBoxXShooter, SpeedShooter)

    
    def shoot(self,xShooter, yShooter, direction, hitBoxXShooter, SpeedShooter):
        """Shoot the grenade
        tire la grenade
        
        Args:
            xShooter (int): x position of the shooter
            yShooter (int): y position of the shooter
            direction (str): direction of the shooter"""
    
        self.timeShoot[1] = EZ.clock()
        self.xShooter = xShooter
        self.yShooter = yShooter
        self.direction = direction
        self.hitBoxXShooter = hitBoxXShooter
        self.SpeedShooter = SpeedShooter
        self.decalxFond = 0
        self.y = yShooter

        self.canExplode = True

    


    
    def onShoot(self, decalxFond):
        """Calculate the position of the grenade
        calcule la position de la grenade"""

        ANGLE_START = 160 # angle of the grenade at the time of shooting / angle de la grenade au moment du tir

        if self.y + self.hitBox[1] <= self.hauteurSol:
            rapport = abs(self.SpeedShooter/4) + 1 # repport to calculate granade shooting distance / rapport pour calculer la distance de tir de la grenade
            angle = ANGLE_START - (ANGLE_START/(self.timeShoot[0])) * (EZ.clock() - self.timeShoot[1]) if  ANGLE_START - (ANGLE_START/(self.timeShoot[0])) * (EZ.clock() - self.timeShoot[1]) > 0 else 0  # Calculate the angle of the grenade on a parable / calcule l'angle de la grenade sur une parable
            
            hauteurDAjout = self.hauteurSol * ((ANGLE_START - angle)/ANGLE_START) + (self.yShooter - self.hitBox[1]) * (angle/ANGLE_START) # Calculate the height to add at the parable / calcule la hauteur à ajouter sur la parable
            self.y = hauteurDAjout - (math.sin(math.radians(angle))) * 58 * rapport # Calculate the position of the grenade on the y axis / calcule la position de la grenade sur l'axe des y --> 58 = HauteurDeTir(50)/sin(120°) (58 = distance between the top position and the end the explosion)
            self.decalxFond += decalxFond

            if self.direction == "right":
                self.x = -self.decalxFond + self.xShooter + self.hitBoxXShooter + self.hitBox[0] + (math.cos(math.radians(angle)) + 1 ) * 100 * rapport # Calculate the position of the grenade on the x axis / calcule la position de la grenade sur l'axe des x --> 133 = 200/1.5 (1.5 = distance between the start cos and the end cos / 200 = distance between the start position and the end the explosion)
            
            else:
                self.x = -self.decalxFond + self.xShooter - (math.cos(math.radians(angle)) + 1 ) * 100 * rapport # ^^^^

            EZ.trace_image(self.chargesImage,self.x,self.y)
        
        elif self.canExplode:
            self.explode()
            self.canExplode = False

    def explode(self):
        """Explode the grenade
        explose la grenade"""

        # Partie degat
        self.DoDamage = True
        self.zoneHitBox()
        

        # Partie animation
        self.lastchargesExplosion = 0
        
    def AnimationExplode(self, decalxFond):
        """Animation of the explosion
        animation de l'explosion"""

        if self.lastchargesExplosion < self.numberPictureAnimation:
            self.x -= decalxFond
            EZ.trace_image(self.chargesExplosion[self.lastchargesExplosion], self.x - self.hitBoxExplosion[0]//2, self.y - self.hitBoxExplosion[1] + self.hitBox[1])
            self.lastchargesExplosion += 1
        
            if self.lastchargesExplosion > self.numberPictureAnimation//2:
                self.DoDamage = False
        
    def zoneHitBox(self):
        """Return the coordinates of the corners of the hit box
        retourne les coordonnées des coins de la hit box"""

        self.zoneHitBoxlist = [[self.x, self.y], [self.x + self.hitBoxExplosion[0], self.y], [self.x + self.hitBoxExplosion[0], self.y + self.hitBoxExplosion[1]], [self.x, self.y + self.hitBoxExplosion[1] ]] # list of the coordinates of the corners of the hit box / liste des coordonnées des coins de la hit box --> [Haut Gauche / Haut Droit / Bas Droit / Bas Gauche]
    
    def isUsable(self):
        """Check if the grenade is usable
        vérifie si la grenade est utilisable"""

        return self.usable

    def repair(self):
        """Repair the grenade
        répare la grenade"""
    
        super().repair()
        self.usable = True






class Potion(Equipement):
    """Class for the potion
    classe pour la potion"""

    def __init__(self, efficiency,cooldown = 60):
        """Constructor for the potion
        constructeur pour la potion"""
        super().__init__("Potion", "potion", cooldown)
        self.usable = True
        self.efficiency = efficiency # efficiency of the potion / efficacité de la potion
    
    def getEfficiency(self):
        """Get the potion efficiency
        obtient l'efficacité de la potion"""
                
        return self.efficiency
    
    def use(self):
        """Use the potion
        utilise la potion"""

        self.usable = False
    

    def isUsable(self):
        """Check if the potion is usable
        vérifie si la potion est utilisable"""

        return self.usable
    
    def repair(self):
        """Repair the potion
        répare la potion"""

        super().repair()
        self.usable = True