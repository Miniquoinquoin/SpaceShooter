"""Fichier Contenant la Base des fonctionaliter du Joueur"""


import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Joueur.Equipement.Armes as Armef
import FichiersJeu.Joueur.Equipement.Equipement as Equipement
import FichiersJeu.InterfaceDynamique as ID
import FichiersJeu.Interface.Decor as Decor
import FichiersJeu.Interface.Animation as Anim

import FichiersJeu.InfoJoueur.ReadInfo as Reader



class Joueur:
    """Class joueur"""

    def __init__(self, name, level, personnage = 1, stats = None):
        """Initialisation de Joueur

        Args:
            name (str): nom du joueur
            level (int): level du joueur
            personnage(str): nom du personnage
            stats (dic): toutes les stats du joueur {"vie": 100, "damage": 10, "acc": 1,"speed": 10, "jumpPower": 2 }
            equipement (list): Toutes ces objet [grenade, shield,...]
        """
        self.name = name
        self.level = level # Character level / Niveau du personnage
        self.personnage = personnage # Player Number / numeros du joueur
        self.stats = stats if stats != None else self.CalculateStats() # If stats == None, read stats from file / si stats == None, lire les stats du fichier

        self.equipement = {'shield': None, 'grenade': None, 'potion': None} # Equipment of the player / équipement du joueur
        self.x = ID.LONGEUR//2 - 65 # X position of the player / position en x du joueur - 65 pour centrer le joueur (65 = hitbox[0]/2)
        self.y = 150  # height player spawn / Hauteur d'aparition du joueur --> = y_sol (saut)
        self.y_sol = 0 #Hauteur de marche du joueur - 3* 48
        self.move_info = {"right": False, "left": False, "saut": False, "speed": 0} # Etats demander par les touche
        self.move_etat = {"right": False, "left": False} # Etats du joueur sur l'ecrant
        self.move_possible = {"right": True, "left": True}  #Donne les deplacement que le joueur peux effectuer (permet d'interdire certain deplacement)
        self.autoShoot = "right"

        self.timeSaut = EZ.clock() # temps du dernier saut / ici temps au lancement
        self.charges = None  #Si l'image est chargé ou non
        self.hitbox = [130, 144] # 130 car les personage on an moyenne 7 pixel de libre de chaque coter 

        # Dernier charge effectuer
        self.lastchargesRight = [0, 1, 0] # [0 = PasArrier / 1 = Pied coller / 2 = Pied avant, 0 = Pas arrier / 1 = Pied avant, repetiton]
        self.lastchargesLeft = [0, 1, 0] # [0 = PasArrier / 1 = Pied coller / 2 = Pied avant, 0 = Pas arrier / 1 = Pied avant, repetition]
        self.lastchargesEffetDomage = [2 * Anim.MAX_INTENSITE, "health"]  # [intensiter, type: "health" ou "shield"]

        self.chargeSon() # Load the sounds of the player / charge les sons du joueur


    def charge(self):
        """Foncton qui charge l'image du personage"""

        self.CalculateStats()

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

        # Load weapon / charge l'arme
        self.weaponLevel = Reader.ReadInventaire()[f"Personnage{self.personnage}"][2]
        self.arme = [{"arme": Armef.Armes(self.stats['weapon']['name'], self.stats['weapon']["damage"], self.stats['weapon']["range"], self.stats['weapon']["durability"], self.weaponLevel), "speed": self.stats['weapon']['speed']} for nombre_arme in range(10)]  # {Type d'arme, vitesse de l'arme, [dernier tire de l'arme, temps de recharge]}    
        self.last_arme = -1 # last weapon that the player shot in self.arme / Dernier arme que le joueur a tire dans self.arme
        self.timeShoot = [EZ.clock(), self.stats['weapon']['cooldown']] # [temps du dernier tire, cooldown]

        self.charges = True


    def chargeSon(self):
        """Charge the sound of the player
        charge le son du joueur"""

        self.sound = {"damage": EZ.charge_son("FichiersJeu\son\Bruitage\Degat.wav"), "lancer": EZ.charge_son("FichiersJeu\son\Bruitage\Lancer.wav"), "saut": EZ.charge_son("FichiersJeu\son\Bruitage\saut.wav"), "mort": EZ.charge_son("FichiersJeu\son\Bruitage\mort.wav") }

    def setHauteurSol(self, hauteur):
        """Set y_sol to the height of the ground
        définie la hauteur du sol
        """
        self.y_sol = hauteur - 144
        self.hauteurSol = hauteur
    
    def setEquipement(self, equipements):
        """Set the equipment of the player
        définie l'équipement du joueur

        Args:
            equipements (list): list of the equipment of the player can be : 'shield', 'grenade' and 'potion'/ liste des équipements du joueur peut être : 'shield', 'grenade' et 'potion'
        """

        EquipementStats = Reader.ReadStatsEquipement()
        for equipement in equipements:
            if equipement == 'Shield':
                self.equipement['shield'] = Equipement.Bouclier(EquipementStats[equipement]["eficiency"], EquipementStats[equipement]["cooldown"]) # number of hits before the shield is destroyed / nombre de coups avant que le bouclier soit détruit
            
            elif equipement == 'Grenade':
                self.equipement['grenade'] = Equipement.Grenade(EquipementStats[equipement]["eficiency"], self.hauteurSol, EquipementStats[equipement]["cooldown"], EquipementStats[equipement]["BonusRange"]) # grenade damage *13 because she hit 25(numberofpicture)/2  / dégats de la grenade
            
            elif equipement == 'Potion':
                self.equipement['potion'] = Equipement.Potion(EquipementStats[equipement]["eficiency"], EquipementStats[equipement]["cooldown"]) # potion heal / soin de la potion
        
    def CalculateStats(self):
        """Calculate the stats of the player in terms of the level of the player
        Calcul les stats du joueur en fonction du niveau du joueur"""

        BaseStats = Reader.ReadStatsPlayers()[self.personnage - 1]
        UpStats = Reader.ReadUpStatsPlayers()[self.personnage - 1]
        self.level = Reader.ReadInventaire()[f"Personnage{self.personnage}"][1] -1 # -1 because the level is starting at 1 and not 0 / -1 car le niveau commence à 1 et pas 0
        self.weaponLevel = Reader.ReadInventaire()[f"Personnage{self.personnage}"][2]  -1 # -1 because the level is starting at 1 and not 0 / -1 car le niveau commence à 1 et pas 0
        self.stats = { "name": BaseStats['name'], "price": BaseStats['price'] ,"vie": BaseStats['vie'] + self.level * UpStats['vie'], 
                    "regen": {"timer": 0, "cooldown": BaseStats['regen']['cooldown'] + self.level * UpStats['regen']['cooldown'], "eficiency": BaseStats['regen']['eficiency'] + self.level * UpStats['regen']['eficiency']},
                    "weapon": {"name": BaseStats['weapon']['name'], "price": BaseStats['weapon']['price'], "damage": BaseStats['weapon']['damage']  + self.weaponLevel * UpStats['weapon']['damage'], "range": BaseStats['weapon']['range'] + self.weaponLevel * UpStats['weapon']['range'], "durability": BaseStats['weapon']['durability'] + self.weaponLevel * UpStats['weapon']['durability'], "cooldown": BaseStats['weapon']['cooldown'] + self.weaponLevel * UpStats['weapon']['cooldown'], "speed": BaseStats['weapon']['speed'] + self.weaponLevel * UpStats['weapon']['speed']},
                    "acc": BaseStats['acc'] + self.level * UpStats['acc'],"speed": BaseStats['speed'] + self.level * UpStats['speed'], "jumpPower": BaseStats['jumpPower'] + self.level * UpStats['jumpPower'],  "maxvie": BaseStats['vie'] + self.level * UpStats['vie'] }



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
        self.effetRegen()
        self.effetDomage(5)
        self.zoneHitBox()
        self.onShoot()
        self.TraceEquipement()

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

            if self.move_info["right"] == True and self.move_possible["right"]:
                self.charges = self.moveRight()
                self.move_etat = {"right": True, "left": False}

            
            elif self.move_info["left"] == True and self.move_possible["left"]:
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
        EZ.joue_son(self.sound["saut"])

    
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
            EZ.joue_son(self.sound["lancer"])

            if self.move_etat["right"]:
                self.arme[self.last_arme]["arme"].Setup(self.x + 72, self.y, "right", self.move_info["speed"])
            
            elif self.move_etat["left"]:
                self.arme[self.last_arme]["arme"].Setup(self.x + 72, self.y, "left", self.move_info["speed"])

            else:
                self.arme[self.last_arme]["arme"].Setup(self.x + 72, self.y, self.autoShoot , self.move_info["speed"])
                



    def onShoot(self):
        """Deplace la balle pendant le tire"""
        for armes in range(len(self.arme)):
            self.arme[armes]["arme"].display(self.arme[armes]["speed"], self.move_info["speed"], self.stats["vie"])

    def effetDomage(self, speed):
        """Cree l'effet de degat du joueur"""

        if self.lastchargesEffetDomage[0] + speed < 2 * Anim.MAX_INTENSITE: # *2 : Arriver de l'effet / Aténuation de l'effet

            self.lastchargesEffetDomage[0] += speed

            if self.lastchargesEffetDomage[0] <= Anim.MAX_INTENSITE:
                Anim.traceEffetDegatJoueur(self.lastchargesEffetDomage[0], ID.LONGEUR, ID.HAUTEUR, None, (255,0,0) if self.lastchargesEffetDomage[1] == "health" else (0,0,255))
            
            else:
                Anim.traceEffetDegatJoueur( Anim.MAX_INTENSITE + (Anim.MAX_INTENSITE - self.lastchargesEffetDomage[0]), ID.LONGEUR, ID.HAUTEUR,None, (255,0,0) if self.lastchargesEffetDomage[1] == "health" else (0,0,255))

    def domage(self, domage):
        """S'inflige des degat

        Args:
            domage (int): degat qu'il s'inflige
        """

        if self.equipement["shield"] != None and not(self.equipement["shield"].isBroken()):
            self.equipement["shield"].use()
            self.lastchargesEffetDomage[1] = "shield"
                
        else:
            self.stats["vie"] -= domage
            EZ.joue_son(self.sound["damage"])
            self.stats["regen"]["timer"] = EZ.clock()
            self.lastchargesEffetDomage[1] = "health"

        self.lastchargesEffetDomage[0] = 0 if self.lastchargesEffetDomage[0] >= 2 * Anim.MAX_INTENSITE else  2 * Anim.MAX_INTENSITE - self.lastchargesEffetDomage[0] if self.lastchargesEffetDomage[0] > Anim.MAX_INTENSITE else self.lastchargesEffetDomage[0]
    
        
    def zoneHitBox(self):
        """Definit la zone ou le joueur prend des degats en donnant les 4 point du carre de la hitbox"""
        if self.move_etat["right"]:
            self.zoneHitBoxlist = [[self.x + 20, self.y], [self.x + self.hitbox[0], self.y], [self.x + self.hitbox[0], self.y + self.hitbox[1]], [self.x + 20, self.y + self.hitbox[1] ]]       # [Haut Gauche / Haut Droit / Bas Droit / Bas Gauche]

        elif self.move_etat["left"]:
            self.zoneHitBoxlist = [[self.x + 25, self.y], [self.x + self.hitbox[0] + 5, self.y], [self.x + self.hitbox[0] + 5, self.y + self.hitbox[1]], [self.x + 25, self.y + self.hitbox[1] ]]

        else:
            self.zoneHitBoxlist = [[self.x + 20, self.y], [self.x + self.hitbox[0] - 5, self.y], [self.x + self.hitbox[0] - 5, self.y + self.hitbox[1]], [self.x + 20, self.y + self.hitbox[1] ]]

        # self.traceHitbox()
        

    def traceHitbox(self):
        """Trace l'hitbox du joueur"""

        EZ.trace_segment(int(self.zoneHitBoxlist[0][0]),int(self.zoneHitBoxlist[0][1]), int(self.zoneHitBoxlist[1][0]), int(self.zoneHitBoxlist[1][1]))     #Haut    
        EZ.trace_segment(int(self.zoneHitBoxlist[1][0]),int(self.zoneHitBoxlist[1][1]), int(self.zoneHitBoxlist[2][0]), int(self.zoneHitBoxlist[2][1]))     #Droit
        EZ.trace_segment(int(self.zoneHitBoxlist[2][0]),int(self.zoneHitBoxlist[2][1]), int(self.zoneHitBoxlist[3][0]), int(self.zoneHitBoxlist[3][1]))     #Bas
        EZ.trace_segment(int(self.zoneHitBoxlist[3][0]),int(self.zoneHitBoxlist[3][1]), int(self.zoneHitBoxlist[0][0]), int(self.zoneHitBoxlist[0][1]))     #Gauche

    def death(self):
        """Informe si le joueur est mort
            Communicate if the Player are dead
            

        Returns:
            bool: True if player haven't life, and False if player have life
        """
        if self.stats["vie"] <= 0:
            EZ.joue_son(self.sound["mort"])
        return self.stats["vie"] <= 0
    
    def resetStats(self):
        """Put back the stats of the player, to the started stats
            Remets les stats du joueur à celle du debut
        
        """

        self.stats["vie"] = self.stats["maxvie"]

        #Effect / Effet
        self.lastchargesEffetDomage[0] = 2 * Anim.MAX_INTENSITE

        #Equipement
        for equipement in self.equipement:
            if self.equipement[equipement] != None:
                self.equipement[equipement].repair()
        

    def effetRegen(self):
        """
        Heal the player if possible (timer)
        Regenère les pv du joueur si possible"""

        if EZ.clock() - self.stats["regen"]["timer"] >= self.stats["regen"]["cooldown"]: # verifie le cooldown
            if self.stats["vie"] + self.stats["regen"]["eficiency"] < self.stats["maxvie"]: # verifie si le joueur peut etre regen sans depanser maxvie
                self.stats["vie"] += self.stats["regen"]["eficiency"]
            
            elif self.stats["vie"] < self.stats["maxvie"]: # verifie si le joueur et proche de la vie max
                self.stats["vie"] = self.stats["maxvie"]


    def UsePotion(self):
        """Use a potion if possible
        Utilise une potion si possible"""

        if self.equipement["potion"] != None and self.equipement["potion"].isUsable():
            self.equipement["potion"].use()
            self.stats["vie"] += self.equipement["potion"].getEfficiency() if self.equipement["potion"].getEfficiency() + self.stats["vie"] <= self.stats["maxvie"] else self.stats["maxvie"] - self.stats["vie"]
    
    def RepaireShield(self):
        """Break the shield for start the cooldown repair shield
        Détruit le bouclier pour commencer le cooldown de réparation du bouclier"""

        if self.equipement["shield"] != None:
            self.equipement["shield"].broke()
    
    def UseGrenade(self):
        """Use a grenade if possible
        Utilise une grenade si possible"""

        if self.equipement["grenade"] != None and self.equipement["grenade"].isUsable():
            self.equipement["grenade"].use(self.x, (self.y + self.hitbox[1]//3), "right" if self.move_etat["right"] else "left", self.hitbox[0], self.move_info["speed"]) 
    
    def TraceEquipement(self):
        """Draw the equipment of the player
        Trace les équipements du joueur"""
        
        yStart = 100
        if self.equipement["shield"] != None:
            self.equipement["shield"].traceInfoEquipement(1200, yStart)
            yStart += self.equipement["shield"].hauteur + 10

        if self.equipement["grenade"] != None:
            self.equipement["grenade"].traceInfoEquipement(1200, yStart)
            yStart += self.equipement["grenade"].hauteur + 10

            self.equipement['grenade'].onShoot(self.move_info["speed"])
            self.equipement['grenade'].AnimationExplode(self.move_info["speed"])
        
        if self.equipement["potion"] != None:
            self.equipement["potion"].traceInfoEquipement(1200, yStart)
            
