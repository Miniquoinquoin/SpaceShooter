"""Fichier avec les proprieter des monstres"""

import random
import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.InterfaceDynamique as ID
import FichiersJeu.Interface.Decor as Decor
import FichiersJeu.Joueur.Equipement.Armes as Armef

class Monstre:

    def __init__(self, name, xPlayer, hauteurSol ,Xspawn = 0):

        self.name = name

        self.stats = {"vie": 100, "damage": 2, "speed": 3, "jumpPower": 1 , "maxvie": 100}
        self.baseDamage = self.stats["damage"]
        self.hitbox = [50, 100] #Modifier au moment du chargement du monstre

        self.charges = None
        self.lastchargesRight = [0, 0, 10] # [Etape du gif originale, repetiton, nombre de repetition avant changement]
        self.lastchargesLeft = [0, 0, 10] # [Etape du gif originale, repetiton, nombre de repetition avant changement]

        self.move_info = {"right": True, "left": False}
        self.vitesseFond = 0 # Vitesse de déplacement du fond
        self.x = Xspawn
        self.hauteurSol = hauteurSol
        self.y = 0 # Position y of the monstre / Position y du monstre
        
        self.xPlayer = xPlayer + 30 # Point que va suivre le monstre

        self.cooldwon = [EZ.clock(), 1] # cooldown entre les attaque du monstre
        self.effect = {"boostDamage": False, "cooldownBoostDamage": [0, 5]} # cooldown [temps du dernier buff, durer du buff]


    def __charge(self,nb_image):
        """Charges les image du monstre et definit sa taille"""  

        self.chargesRight = [EZ.charge_image(f"FichiersJeu/Interface/Entites/Items/Monstres/{self.name}/base/{self.name}_{image}.png") for image in range(nb_image)]
        self.chargesLeft = [EZ.charge_image(f"FichiersJeu/Interface/Entites/Items/Monstres/{self.name}/reverse/{self.name}_reverse_{image}.png") for image in range(nb_image)]
        self.hitbox = [EZ.dimension(self.chargesRight[0])[0], EZ.dimension(self.chargesRight[0])[1]]

    def charge(self):
        """Charge le monstre avec ces stats en fonction de son nom"""

        if self.name == "Amalgam_Sprite":
            self.__charge(8)
            self.setSpeedEffect(2)
            self.stats = {"vie": 100, "damage": 1,"speed": 3, "jumpPower": 1 , "maxvie": 100}

        elif self.name == "Adept_Sprite":
            self.__charge(5)
            self.setSpeedEffect(3)
            self.stats = {"vie": 100, "damage": 1,"speed": 3, "jumpPower": 1 , "maxvie": 100}

        elif self.name == "ArchMage_Sprite":
            self.__charge(5)
            self.setSpeedEffect(3)
            self.stats = {"vie": 100, "damage": 1,"speed": 3, "jumpPower": 1 , "maxvie": 100}
        
        elif self.name == "Ammonite_Sprite":
            self.__charge(6)
            self.setSpeedEffect(5)
            self.stats = {"vie": 50, "damage": 1,"speed": 3, "jumpPower": 1 , "maxvie": 50}
        


        self.y = self.hauteurSol - self.hitbox[1]
        self.charges = self.chargesRight[self.lastchargesRight[0]]

    def display(self, vitesseFond):
        """Affiche le monstre"""

        if self.charges == None:
            self.charge()

        self.move(vitesseFond)
        EZ.trace_image(self.charges, self.x, self.y)
        Decor.barre_vie_montre(self.x, self.y - 20, self.stats["vie"], self.stats["maxvie"],self.hitbox[0])

    
    def setSpeedEffect(self, value):
        """Change la vitesse de transition des image du gif"""

        self.lastchargesRight[2] = value
        self.lastchargesLeft[2] = value

        

    
    def moveEffectRight(self):
        """Cree l'effet de vie du monstre vers la droite"""

        if self.lastchargesRight[1] >= self.lastchargesRight[2]:
            self.lastchargesRight[1] = 0
            if self.lastchargesRight[0] >= len(self.chargesRight):
                self.lastchargesRight[0] = 0

            self.charges = self.chargesRight[self.lastchargesRight[0]]
            self.lastchargesRight[0] += 1

        else:
            self.lastchargesRight[1] += 1

    
    def moveEffectLeft(self):
        """Cree l'effet de vie du monstre vers la droite"""
        
        if self.lastchargesLeft[1] >= self.lastchargesLeft[2]:
            self.lastchargesLeft[1] = 0
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
        

        if self.x < self.xPlayer - 20: # -20 : evite que le montres reste sur le joueur est fait plein de droit gauche
            self.move_info["right"] = True
            self.move_info["left"] = False
        
        elif self.x > self.xPlayer + 20: # +20: Meme raison
            self.move_info["left"] = True 
            self.move_info["right"] = False

        self.moveX(vitesseFond)
        self.moveEffect()

        self.zoneHitBox()
        self.vitesseFond = vitesseFond

    
    def domage(self, domage):
        """S'inflige des degat

        Args:
            domage (int): degat qu'il s'inflige
        """

        self.stats["vie"] -= domage

    def heal(self, heal):
        """Ce soigne de heal

        Args:
            heal (int): pv qu'il se soigne
        """
        if self.stats["vie"] + heal <= self.stats["maxvie"]:
            self.stats["vie"] += heal

        else:
            self.stats["vie"] = self.stats["maxvie"]



    def zoneHitBox(self):
        """Definit la zone ou le monstre prend des degats en donnant les 4 point du carre de la hitbox"""

        self.zoneHitBoxlist = [[self.x, self.y], [self.x + self.hitbox[0], self.y], [self.x + self.hitbox[0], self.y + self.hitbox[1]], [self.x, self.y + self.hitbox[1] ]]     # [Haut Gauche / Haut Droit / Bas Droit / Bas Gauche]
        # self.traceHitbox()

    def traceHitbox(self):
        """Trace l'hitbox du joueur"""

        EZ.trace_segment(int(self.zoneHitBoxlist[0][0]),int(self.zoneHitBoxlist[0][1]), int(self.zoneHitBoxlist[1][0]), int(self.zoneHitBoxlist[1][1]))     #Haut
        EZ.trace_segment(int(self.zoneHitBoxlist[1][0]),int(self.zoneHitBoxlist[1][1]), int(self.zoneHitBoxlist[2][0]), int(self.zoneHitBoxlist[2][1]))     #Droit
        EZ.trace_segment(int(self.zoneHitBoxlist[2][0]),int(self.zoneHitBoxlist[2][1]), int(self.zoneHitBoxlist[3][0]), int(self.zoneHitBoxlist[3][1]))     #Bas
        EZ.trace_segment(int(self.zoneHitBoxlist[3][0]),int(self.zoneHitBoxlist[3][1]), int(self.zoneHitBoxlist[0][0]), int(self.zoneHitBoxlist[0][1]))     #Gauche

    def death(self):
        """Suprime le monstre si il est mort

        Returns:
            bool: True if monstre haven't life, and False if monstre have life
        """

        return self.stats["vie"] <= 0

    def attaque(self):
        """Donne l'autorisation au monstre d'attaquer

        Returns:
            bool: True si cooldown respecter
        """
        if EZ.clock() - self.cooldwon[0] >= self.cooldwon[1]:
            self.cooldwon[0] = EZ.clock()
            self.boostAttack()
            return True
        
        return False

    def boostAttack(self):
        """Booste l'attaque du monstre si effet = True

        Args:
            effet (bool): True attaque du monstre booste / False attaque de base

        """

        self.stats["damage"] = self.baseDamage

        if self.effect["cooldownBoostDamage"][0] + self.effect["cooldownBoostDamage"][1] >= EZ.clock():
            self.stats["damage"] *= 1.25

 


        
        
class Wizard(Monstre):
    """Monstre avec des effet/ buff autour d'eux"""

    def __init__(self, name, xPlayer, HauteurSol, Xspawn, type, range = 250, power = 20, cooldown = 10):
        super().__init__(name, xPlayer, HauteurSol, Xspawn)

        """ type: "HEAL" / "STRENGTH" range = rayon cooldown: [derniere utilisation, cooldown]"""
        self.power = {"type": type, "range": range, "power": power, "cooldown": [EZ.clock() - random.randint(0, cooldown - 1),cooldown]}  # [type, range, power, cooldown] 
        self.zonePowerlist = [[0, 0], [0,0], [0,0], [0,0]] # [Haut Gauche / Haut Droit / Bas Droit / Bas Gauche]

    def display(self, vitesseFond):
        super().display(vitesseFond)

        if self.power["type"] == "HEAL":
            self.HealEffect()
        
        elif self.power["type"] == "STRENGTH":
            self.StrenghEffect()
    
    
    
    def move(self, vitesseFond):

        super().move(vitesseFond)
        self.zonePower()
    


    def zonePower(self):
        """Definit la zone ou le monstre donnera l'effet"""
    
        self.zonePowerlist = [[self.x - self.power["range"] , self.y - self.power["range"]], 
        [self.x + self.hitbox[0] + self.power["range"], self.y - self.power["range"]],
        [self.x + self.hitbox[0] + self.power["range"], self.y + self.hitbox[1] + self.power["range"]], 
        [self.x - self.power["range"], self.y + self.hitbox[1] + self.power["range"]]]     # [Haut Gauche / Haut Droit / Bas Droit / Bas Gauche]


    def traceZonePower(self):
        """Trace l'hitbox du joueur"""

        EZ.trace_segment(int(self.zonePowerlist[0][0]),int(self.zonePowerlist[0][1]), int(self.zonePowerlist[1][0]), int(self.zonePowerlist[1][1]))     #Haut
        EZ.trace_segment(int(self.zonePowerlist[1][0]),int(self.zonePowerlist[1][1]), int(self.zonePowerlist[2][0]), int(self.zonePowerlist[2][1]))     #Droit
        EZ.trace_segment(int(self.zonePowerlist[2][0]),int(self.zonePowerlist[2][1]), int(self.zonePowerlist[3][0]), int(self.zonePowerlist[3][1]))     #Bas
        EZ.trace_segment(int(self.zonePowerlist[3][0]),int(self.zonePowerlist[3][1]), int(self.zonePowerlist[0][0]), int(self.zonePowerlist[0][1]))     #Gauche

    def HealEffect(self):
        """Trace l'effet de la zone de heal"""
        DURER_DEFFET = 1 # Durer de l'effet
        NOMBRE_DISQUE = 2 # Varie les nuance

        TimeSpent = EZ.clock() - self.power["cooldown"][0]
        if TimeSpent <= DURER_DEFFET:
            SetRadius = TimeSpent * self.power["range"]/DURER_DEFFET
            Radius = SetRadius
            for disque in range(1, NOMBRE_DISQUE + 1):
                Radius = (NOMBRE_DISQUE + 2 - disque) * SetRadius/(NOMBRE_DISQUE + 1)
                EZ.trace_disque(int(self.x + self.hitbox[0]//2), int(self.y + self.hitbox[1]//2), int(Radius), 0, int(100 + disque * (100/(NOMBRE_DISQUE + 1))), 0, int(100 - disque * (100/(NOMBRE_DISQUE + 1))))

    def StrenghEffect(self):
        """Trace l'effet de la zone de force"""
        DURER_DEFFET = 1 # Durer de l'effet
        NOMBRE_DISQUE = 2 # Varie les nuance

        TimeSpent = EZ.clock() - self.power["cooldown"][0]
        if TimeSpent <= DURER_DEFFET:
            SetRadius = TimeSpent * self.power["range"]/DURER_DEFFET
            Radius = SetRadius
            for disque in range(1, NOMBRE_DISQUE + 1):
                Radius = (NOMBRE_DISQUE + 2 - disque) * SetRadius/(NOMBRE_DISQUE + 1)
                EZ.trace_disque(int(self.x + self.hitbox[0]//2), int(self.y + self.hitbox[1]//2), int(Radius), int(100 + disque * (100/(NOMBRE_DISQUE + 1))), 0, 0, int(100 - disque * (100/(NOMBRE_DISQUE + 1))))



class MonstreShooter(Monstre):

    def __init__(self, name, HauteurSol, xPlayer, range, Xspawn=0):
        super().__init__(name, xPlayer, HauteurSol, Xspawn)

        self.arme = {"arme": Armef.ArmesAvecForme(self.name, self.stats["damage"], range, 1), "speed": 15}  # {Type d'arme, vitesse de l'arme, [dernier tire de l'arme, temps de recharge]}
        self.timeShoot = [EZ.clock(), 4] # [temps du dernier tire, cooldown]
    

    def shoot(self):
        """Fait tirer le Montre"""

        if self.move_info["right"]:
            self.arme["arme"].Setup(self.x + self.hitbox[0]//2, self.y + self.hitbox[1]//2, "right")
        
        elif self.move_info["left"]:
            self.arme["arme"].Setup(self.x + self.hitbox[0]//2, self.y + self.hitbox[1]//2, "left")
            
    def display(self, vitesseFond):
        super().display(vitesseFond)
        self.onShoot()


    def onShoot(self):
        """Deplace la balle pendant le tire"""
        self.arme["arme"].display(self.arme["speed"], self.vitesseFond)

        if EZ.clock() - self.timeShoot[0] > self.timeShoot[1]: # cooldown de l'arme
            self.timeShoot[0] = EZ.clock()
            self.shoot()

