"""Fichier avec les proprieter des monstres"""

import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.InterfaceDynamique as ID
import FichiersJeu.Interface.Decor as Decor

class Monstre:

    def __init__(self, name, xPlayer, Xspawn = 0):

        self.name = name

        self.stats = {"vie": 100, "damage": 2, "range": 300 ,"speed": 3, "jumpPower": 1 , "maxvie": 100}
        self.baseDamage = self.stats["damage"]
        self.hitbox = [50, 100] #Modifier au moment du chargement du monstre

        self.charges = None
        self.lastchargesRight = [0, 0, 10] # [Etape du gif originale, repetiton, nombre de repetition avant changement]
        self.lastchargesLeft = [0, 0, 10] # [Etape du gif originale, repetiton, nombre de repetition avant changement]

        self.move_info = {"right": True, "left": False}
        self.x = Xspawn
        
        self.xPlayer = xPlayer + 30 # Point que va suivre le monstre

        self.cooldwon = [EZ.clock(), 1] # cooldown entre les attaque du monstre
        self.effect = {"boostDamage": False, "cooldownBoostDamage": [0, 5]} # cooldown [temps du dernier buff, durer du buff]


    def charge(self):
        """Charge le monstre en fonction de son nom"""

        if self.name == "Amalgam_Sprite":
            self.chargesRight = [EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-0.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-1.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-2.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-3.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-4.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-5.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-6.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite1\Amalgam_Sprite1-7.png")]
            self.chargesLeft = [EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-0.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-1.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-2.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-3.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-4.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-5.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-6.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Amalgam_Sprite\Amalgam_Sprite2\Amalgam_Sprite2-7.png")]
            self.hitbox = [93, 90]
            self.stats = {"vie": 100, "damage": 1, "range": 300 ,"speed": 3, "jumpPower": 1 , "maxvie": 100}

        elif self.name == "Adept_Sprite":
            self.chargesRight = [EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Adept_Sprite\Adept_Sprite1\Adept_Sprite1-0.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Adept_Sprite\Adept_Sprite1\Adept_Sprite1-1.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Adept_Sprite\Adept_Sprite1\Adept_Sprite1-2.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Adept_Sprite\Adept_Sprite1\Adept_Sprite1-3.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Adept_Sprite\Adept_Sprite1\Adept_Sprite1-4.png")]
            self.chargesLeft = [EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Adept_Sprite\Adept_Sprite2\Adept_Sprite2-0.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Adept_Sprite\Adept_Sprite2\Adept_Sprite2-1.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Adept_Sprite\Adept_Sprite2\Adept_Sprite2-2.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Adept_Sprite\Adept_Sprite2\Adept_Sprite2-3.png"), EZ.charge_image("FichiersJeu\Interface\Entites\Items\Monstres\Adept_Sprite\Adept_Sprite2\Adept_Sprite2-4.png")]
            self.hitbox = [81, 58]
            self.stats = {"vie": 100, "damage": 1, "range": 300 ,"speed": 3, "jumpPower": 1 , "maxvie": 100}


        self.charges = self.chargesRight[self.lastchargesRight[0]]
        self.y = ID.HAUTEUR_SOL - self.hitbox[1]


    def display(self, vitesseFond):
        """Affiche le monstre"""

        if self.charges == None:
            self.charge()

        self.move(vitesseFond)
        EZ.trace_image(self.charges, self.x, self.y)
        Decor.barre_vie_montre(self.x, self.y - 20, self.stats["vie"], self.stats["maxvie"],self.hitbox[0])
        

    
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
        self.zoneHitBox()

    
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

    def __init__(self, name, xPlayer, Xspawn, type, range = 250, power = 20):
        super().__init__(name, xPlayer, Xspawn)

        """ type: "HEAL" / "STRENGTH" range = rayon cooldown: [derniere utilisation, cooldown]"""
        self.power = {"type": type, "range": range, "power": power, "cooldown": [EZ.clock(),10]}  
        self.zonePowerlist = [[0, 0], [0,0], [0,0], [0,0]]

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