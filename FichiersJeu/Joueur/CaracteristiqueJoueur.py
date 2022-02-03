"""Fichier Contenant la Base des fonctionaliter du Joueur"""


import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.Equipement.Armes as Armef
import FichiersJeu.InterfaceDynamique as ID
import FichiersJeu.Interface.Decor as Decor


class Joueur:
    """Class joueur"""

    def __init__(self, name, level, personnage = 8, stats = {"vie": 100, "damage": 10, "range": 300 , "durability": 5,"acc": 1,"speed": 8, "jumpPower": 1,  "maxvie": 100 }, equipement = None):
        """Initialisation de Joueur

        Args:
            name (str): nom du joueur
            level (int): level du joueur
            personnage(str): nom du personnage
            stats (dic): toutes les stats du joueur {"vie": 100, "damage": 10, "acc": 1,"speed": 10, "jumpPower": 2 }
            equipement (dic): Toutes ces objet [weapon, shield]
        """
        self.name = name
        self.level = level
        self.personnage = personnage
        self.stats = stats
        self.equipement = equipement
        self.x = ID.LONGEUR//2
        self.y = 150  #Hauteur d'aparition du joueur
        self.y_sol = ID.HAUTEUR_SOL - 144 #Hauteur de marche du joueur 460 + 3* 48 = 604
        self.move_info = {"right": False, "left": False, "saut": False, "speed": 0} # Etats demander par les touche
        self.move_etat = {"right": False, "left": False} # Etats du joueur sur l'ecrant
        self.autoShoot = "right"

        self.timeSaut = EZ.clock() # temps du dernier saut / ici temps au lancement
        self.charges = None  #Si l'image est chargé ou non
        self.hitbox = [130, 144] # 120 car les personage on an moyenne 4 pixel de libre de chaque coter 

        # Dernier charge effectuer
        self.lastchargesRight = [0, 1, 0] # [0 = PasArrier / 1 = Pied coller / 2 = Pied avant, 0 = Pas arrier / 1 = Pied avant, repetiton]
        self.lastchargesLeft = [0, 1, 0] # [0 = PasArrier / 1 = Pied coller / 2 = Pied avant, 0 = Pas arrier / 1 = Pied avant, repetition]

    def charge(self):
        """Foncton qui charge l'image du personage"""


        if self.personnage == 1:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A2.png"), 0, 3)
            self.chargesRight = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A7.png"), 0, 3),EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A8.png"), 0, 3),EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A9.png"), 0, 3)]
            self.chargesLeft = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A4.png"), 0, 3),EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A5.png"), 0, 3),EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A6.png"), 0, 3)]


        elif self.personnage == 2:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso2\Perso2A2.png"), 0, 3)
            self.chargesRight = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso2\Perso2A7.png"), 0, 3),EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso2\Perso2A8.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso2\Perso2A9.png"), 0, 3)]
            self.chargesLeft = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso2\Perso2A4.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso2\Perso2A5.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso2\Perso2A6.png"), 0, 3)]

        elif self.personnage == 3:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso3\Perso3A2.png"), 0, 3)
            self.chargesRight = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso3\Perso3A7.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso3\Perso3A8.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso3\Perso3A9.png"), 0, 3)]
            self.chargesLeft = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso3\Perso3A4.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso3\Perso3A5.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso3\Perso3A6.png"), 0, 3)]

        elif self.personnage == 4:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso4\Perso4A2.png"), 0, 3)
            self.chargesRight = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso4\Perso4A7.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso4\Perso4A8.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso4\Perso4A9.png"), 0, 3)]
            self.chargesLeft = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso4\Perso4A4.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso4\Perso4A5.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso4\Perso4A6.png"), 0, 3)]

        elif self.personnage == 5:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso5\Perso5A2.png"), 0, 3)
            self.chargesRight = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso5\Perso5A7.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso5\Perso5A8.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso5\Perso5A9.png"), 0, 3)]
            self.chargesLeft = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso5\Perso5A4.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso5\Perso5A5.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso5\Perso5A6.png"), 0, 3)]

        elif self.personnage == 6:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso6\Perso6A2.png"), 0, 3)
            self.chargesRight = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso6\Perso6A7.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso6\Perso6A8.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso6\Perso6A9.png"), 0, 3)]
            self.chargesLeft = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso6\Perso6A4.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso6\Perso6A5.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso6\Perso6A6.png"), 0, 3)]

        elif self.personnage == 7:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso7\Perso7A2.png"), 0, 3)
            self.chargesRight = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso7\Perso7A7.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso7\Perso7A8.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso7\Perso7A9.png"), 0, 3)]
            self.chargesLeft = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso7\Perso7A4.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso7\Perso7A5.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso7\Perso7A6.png"), 0, 3)]
        
        elif self.personnage == 8:
            self.chargesAvant = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso8\Perso8A2.png"), 0, 3)
            self.chargesRight = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso8\Perso8A7.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso8\Perso8A8.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso8\Perso8A9.png"), 0, 3)]
            self.chargesLeft = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso8\Perso8A4.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso8\Perso8A5.png"), 0, 3), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso8\Perso8A6.png"), 0, 3)]

            self.arme = [{"arme": Armef.Shuriken("Shuriken", self.stats["damage"], self.stats["range"], self.stats["durability"]), "speed": 10} for nombre_arme in range(10)]  # {Type d'arme, vitesse de l'arme, [dernier tire de l'arme, temps de recharge]}
            self.last_arme = -1 # Dernier arme que le joueru a tire dans self.arme
            self.timeShoot = [EZ.clock(), 0.2] # [temps du dernier tire, cooldown]

        self.charges = True


    def display(self):
        """Fonction qui trace le Joueur

        Args:
            x (int): x du joueur
            y (int): y du joueur
        """

        if self.charges == None:
            self.charge()
        
        self.move()
        self.effet_saut()
        self.zoneHitBox()
        self.onShoot()

        EZ.trace_image(self.charges, self.x, self.y)
        if self.stats["vie"] >= 0:
            Decor.info_vie(20, 20, 100, self.stats["vie"], self.stats["maxvie"])

        else:
            Decor.info_vie(20, 20, 100, 0, self.stats["maxvie"])


    def moveRight(self):
        """Cree l'effet marcher vers la droite"""

        if self.lastchargesRight[2] >= 100//self.stats["speed"]:  # Time de marche pour eviter la marche trop rapide
            self.lastchargesRight[2] = 0

            if self.lastchargesRight[0] == 0:
                self.lastchargesRight[0] = 1
                return self.chargesRight[0]
            
            elif self.lastchargesRight[0] == 2:
                self.lastchargesRight[0] = 1
                return self.chargesRight[2]
            
            elif self.lastchargesRight[0] == 1:
                if self.lastchargesRight[1] == 0:
                    self.lastchargesRight = [2,1,self.lastchargesRight[2]]
                    return self.chargesRight[1]
                    
                elif self.lastchargesRight[1] == 1:
                    self.lastchargesRight = [0,0,self.lastchargesRight[2]]
                    return self.chargesRight[1]
        
        else:
            self.lastchargesRight[2] += 1
            return self.chargesRight[self.lastchargesRight[0]]

    def moveLeft(self):
        """Cree l'effet marcher vers la Gauche"""

        if self.lastchargesLeft[2] >= 100//self.stats["speed"]:  # Time de marche pour eviter la marche trop rapide
            self.lastchargesLeft[2] = 0

            if self.lastchargesLeft[0] == 0:
                self.lastchargesLeft[0] = 1
                return self.chargesLeft[0]
            
            elif self.lastchargesLeft[0] == 2:
                self.lastchargesLeft[0] = 1
                return self.chargesLeft[2]
            
            elif self.lastchargesLeft[0] == 1:
                if self.lastchargesLeft[1] == 0:
                    self.lastchargesLeft = [2,1,self.lastchargesLeft[2]]
                    return self.chargesLeft[1]
                    
                elif self.lastchargesLeft[1] == 1:
                    self.lastchargesLeft = [0,0,self.lastchargesLeft[2]]
                    return self.chargesLeft[1]
        
        else:
            self.lastchargesLeft[2] += 1
            return self.chargesLeft[self.lastchargesLeft[0]]



    def move(self):
        """Modifie l'aparence du personnage selon sa direction"""

        if not(self.move_info["saut"]):

            if self.move_info["right"] == True:
                self.charges = self.moveRight()
                self.move_etat = {"right": True, "left": False}

            
            elif self.move_info["left"] == True:
                self.charges = self.moveLeft()
                self.move_etat = {"right": False, "left": True}
            
            else:
                self.charges = self.chargesAvant
                self.move_etat = {"right": False, "left": False}
        
        else:

            if self.move_info["right"] == True:
                self.charges = self.chargesRight[0]
                self.move_etat = {"right": True, "left": False}

            
            elif self.move_info["left"] == True:
                self.charges = self.chargesLeft[0]
                self.move_etat = {"right": False, "left": True}
    

    
    def timer_saut(self):
        """Prend les seconde du debut du saut"""

        self.timeSaut = EZ.clock()

    
    def effet_saut(self):
        """Trajectoir du saut du joueur"""

        time = EZ.clock() - self.timeSaut
        if self.y < self.y_sol or time < 0.1:
            
            self.y = self.y_sol - (self.stats["jumpPower"] * 100)* (self.stats["speed"] * time - ((1 + self.stats["speed"]/50)**2) * 0.5 * 9.81 * time**2)
        
        else:
            self.move_info["saut"] = False
            self.y = self.y_sol


    def shoot(self):
        """Fait tirer le joueur"""

        if self.last_arme >= len(self.arme) - 1: # Permet de lancer une arme apres l'autre
            self.last_arme = 0
        
        else:
            self.last_arme += 1

        if EZ.clock() - self.timeShoot[0] > self.timeShoot[1]: # cooldown de l'arme
            self.timeShoot[0] = EZ.clock()

            if self.move_etat["right"]:
                self.arme[self.last_arme]["arme"].Setup(self.x + 72, self.y + 50, "right", self.move_info["speed"])
            
            elif self.move_etat["left"]:
                self.arme[self.last_arme]["arme"].Setup(self.x + 72, self.y + 50, "left", self.move_info["speed"])

            else:
                self.arme[self.last_arme]["arme"].Setup(self.x + 72, self.y + 50, self.autoShoot , self.move_info["speed"])
                



    def onShoot(self):
        """Deplace la balle pendant le tire"""
        for armes in range(len(self.arme)):
            self.arme[armes]["arme"].display(self.arme[armes]["speed"], self.move_info["speed"])

    def domage(self, domage):
        """S'inflige des degat

        Args:
            domage (int): degat qu'il s'inflige
        """

        self.stats["vie"] -= domage
    
        
    def zoneHitBox(self):
        """Definit la zone ou le joueur prend des degats en donnant les 4 point du carre de la hitbox"""
        if self.move_etat["right"]:
            self.zoneHitBoxlist = [[self.x + 20, self.y], [self.x + self.hitbox[0], self.y], [self.x + self.hitbox[0], self.y + self.hitbox[1]], [self.x + 20, self.y + self.hitbox[1] ]]

        elif self.move_etat["left"]:
            self.zoneHitBoxlist = [[self.x + 25, self.y], [self.x + self.hitbox[0] + 5, self.y], [self.x + self.hitbox[0] + 5, self.y + self.hitbox[1]], [self.x + 25, self.y + self.hitbox[1] ]]

        else:
            self.zoneHitBoxlist = [[self.x + 20, self.y], [self.x + self.hitbox[0] - 5, self.y], [self.x + self.hitbox[0] - 5, self.y + self.hitbox[1]], [self.x + 20, self.y + self.hitbox[1] ]]

        # self.traceHitbox()
        

    def traceHitbox(self):
        """Trace l'hitbox du joueur"""

        EZ.trace_segment(int(self.zoneHitBoxlist[0][0]),int(self.zoneHitBoxlist[0][1]), int(self.zoneHitBoxlist[1][0]), int(self.zoneHitBoxlist[1][1]))
        EZ.trace_segment(int(self.zoneHitBoxlist[1][0]),int(self.zoneHitBoxlist[1][1]), int(self.zoneHitBoxlist[2][0]), int(self.zoneHitBoxlist[2][1]))
        EZ.trace_segment(int(self.zoneHitBoxlist[2][0]),int(self.zoneHitBoxlist[2][1]), int(self.zoneHitBoxlist[3][0]), int(self.zoneHitBoxlist[3][1]))
        EZ.trace_segment(int(self.zoneHitBoxlist[3][0]),int(self.zoneHitBoxlist[3][1]), int(self.zoneHitBoxlist[0][0]), int(self.zoneHitBoxlist[0][1]))

    def death(self):
        """Suprime le joueur si il est mort

        Returns:
            bool: True if player haven't life, and False if player have life
        """

        return self.stats["vie"] <= 0

    


