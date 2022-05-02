"""Fichier avec les proprieter des monstres"""

import random
import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.InterfaceDynamique as ID
import FichiersJeu.Interface.Decor as Decor
import FichiersJeu.Joueur.Equipement.Armes as Armef

class Monstre:

    def __init__(self, name, xPlayer, hauteurSol ,Xspawn = 0):

        self.name = name

        self.stats = {"vie": 100, "damage": 0, "speed": 3, "maxvie": 100}
        self.baseDamage = self.stats["damage"] # base damage for boost / degat de base pour les boosts
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


    def __charge(self,nb_image, zoom = 1, reverse = False):
        """ Load the monster images and is hitbox
        Charges les image du monstre et definit sa taille
        
        nb_image : number of picture / nombre d'image du monstre
        zoom : zoom of the picture / zoom de l'image
        reverse : if the picture must be flip / si l'image doit etre inversé"""  

        self.chargesRight = [EZ.transforme_image(EZ.charge_image(f"FichiersJeu/Interface/Entites/Items/Monstres/{self.name}/base/{self.name}_{image}.png"),0,zoom) for image in range(nb_image)]
        self.chargesLeft = [EZ.transforme_image(EZ.charge_image(f"FichiersJeu/Interface/Entites/Items/Monstres/{self.name}/reverse/{self.name}_reverse_{image}.png"),0, zoom) for image in range(nb_image)]
        self.hitbox = [EZ.dimension(self.chargesRight[0])[0], EZ.dimension(self.chargesRight[0])[1]]

        if reverse:
            temp = self.chargesRight
            self.chargesRight = self.chargesLeft
            self.chargesLeft = temp

    def charge(self):
        """ Load the monster images and is stats
        Charge le monstre avec ces stats en fonction de son nom

        For all the monsters: name, number of picture, number of repetition before change
        Pour chaque Monstre : nom du monstre, nombre d'image, nombre de repetition avant changement, stats du Monstre"""

        print(self.name)

        # Map : Terre
        if self.name == "Bolt_Sprite" or self.name == "NutTroop_Sprite":
            self.__charge(6,2)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}
            self.hauteurSol += 10 # Move the monster down / Déplace le monstre vers le bas
        
        elif self.name == "NutArcher_Sprite" or self.name == "BoltArcher_Sprite":
            self.__charge(6,2)
            self.setSpeedEffect(2)
            self.stats = {"type": "SHOOTER", "vie": 50, "damage": 0, "shootDamage": 5, "range": 250, "cooldown": 3, "speed": 4, "maxvie": 50}
            self.hauteurSol += 10 # Move the monster down / Déplace le monstre vers le bas

            self.arme = {"arme": Armef.ArmesAvecForme(self.name, self.stats["shootDamage"], self.stats["range"], 1), "speed": 15}  # {Type d'arme, vitesse de l'arme} / {Weapon, speed}

        elif self.name == "KingToad_Sprite":
            self.__charge(27)
            self.setSpeedEffect(2)
            self.stats = {"type": "SHOOTER", "vie": 50, "damage": 0, "shootDamage": 5, "range": 250, "cooldown": 3, "speed": 4, "maxvie": 50}
            self.hauteurSol += 15 # Move the monster down / Déplace le monstre vers le bas

            self.arme = {"arme": Armef.ArmesAvecForme(self.name, self.stats["shootDamage"], self.stats["range"], 1), "speed": 15}  # {Type d'arme, vitesse de l'arme} / {Weapon, speed}

        elif self.name == "Rocky_Sprite":
            self.__charge(4)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        
        elif self.name == "NutMage_Sprite1":
            self.__charge(7,2)
            self.setSpeedEffect(2)
            self.stats = {"type": "HEAL", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}


        elif self.name == "Dolphin_Sprite":
            self.__charge(6,2)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_COMMON", "vie": 1000, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 1000}
            self.hauteurSol += 50 # Move the monster down / Déplace le monstre vers le bas
        
        elif self.name == "Manmo_Sprite":
            self.__charge(10)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}
            self.hauteurSol += 20 # Move the monster down / Déplace le monstre vers le bas
        
        elif self.name == "Magmaite_Sprite" or self.name == "Vulcan_Sprite":
            self.__charge(8,2)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_STILL", "vie": 50, "damage": 0, "shootDamage": 5, "range": 500, "cooldown": 3, "speed": 0, "maxvie": 50}
            self.hauteurSol += 15 # Move the monster down / Déplace le monstre vers le bas

            self.arme = {"arme": Armef.ArmesAvecForme(self.name, self.stats["shootDamage"], self.stats["range"], 1), "speed": 15}  # {Type d'arme, vitesse de l'arme} / {Weapon, speed}



        # Map : Mars
        elif self.name == "Amalgam_Sprite":
            self.__charge(8)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Adept_Sprite":
            self.__charge(5)
            self.setSpeedEffect(3)
            self.stats = {"type": "HEAL", "vie": 100, "damage": 1, "cooldown": 1, "speed": 2, "maxvie": 100}

        elif self.name == "ArchMage_Sprite":
            self.__charge(5)
            self.setSpeedEffect(3)
            self.stats = {"type": "STRENGTH", "vie": 100, "damage": 1, "cooldown": 1, "speed": 2, "maxvie": 100}
        
        elif self.name == "Ammonite_Sprite":
            self.__charge(6)
            self.setSpeedEffect(5)
            self.stats = {"type": "SHOOTER", "vie": 50, "damage": 0, "shootDamage": 5, "range": 250, "cooldown": 3, "speed": 4, "maxvie": 50}

            self.arme = {"arme": Armef.ArmesAvecForme(self.name, self.stats["shootDamage"], self.stats["range"], 1, (0,200,0)), "speed": 15}  # {Type d'arme, vitesse de l'arme} / {Weapon, speed}

        
        elif self.name == "Gonger_Sprite":
            self.__charge(6,1.5)
            self.setSpeedEffect(5)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "RedDrake_Sprite" or self.name == "Spiker_Sprite":
            self.__charge(30)
            self.setSpeedEffect(2)
            self.stats = {"type": "SHOOTER", "vie": 50, "damage": 0, "shootDamage": 5, "range": 250, "cooldown": 3, "speed": 4, "maxvie": 50}

            self.arme = {"arme": Armef.ArmesAvecForme(self.name, self.stats["shootDamage"], self.stats["range"], 1), "speed": 15}  # {Type d'arme, vitesse de l'arme} / {Weapon, speed}

        elif self.name == "Shroom_Sprite":
            self.__charge(8)
            self.setSpeedEffect(5)
            self.stats = {"type": "BOSS_STILL", "vie": 50, "damage": 0, "shootDamage": 5, "range": 250, "cooldown": 3, "speed": 4, "maxvie": 50}

        # Map : Gluton
        elif self.name == "Berserker_Sprite":
            self.__charge(24,2)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "CharybScylla_Sprite":
            self.__charge(18, 1, True)
            self.setSpeedEffect(2)
            self.stats = {"type": "SHOOTER", "vie": 50, "damage": 0, "shootDamage": 5, "range": 250, "cooldown": 3, "speed": 4, "maxvie": 50}
            self.hauteurSol += 10 # Move the monster down / Déplace le monstre vers le bas

            self.arme = {"arme": Armef.Armes("BouleDeFeuMini", self.stats["shootDamage"], self.stats["range"], 1), "speed": 15}  # {Type d'arme, vitesse de l'arme} / {Weapon, speed}

        elif self.name == "IceToad_Sprite":
            self.__charge(27)
            self.setSpeedEffect(2)
            self.stats = {"type": "SHOOTER", "vie": 50, "damage": 0, "shootDamage": 5, "range": 250, "cooldown": 3, "speed": 4, "maxvie": 50}
            self.hauteurSol += 15 # Move the monster down / Déplace le monstre vers le bas

            self.arme = {"arme": Armef.ArmesAvecForme(self.name, self.stats["shootDamage"], self.stats["range"], 1), "speed": 15}  # {Type d'arme, vitesse de l'arme} / {Weapon, speed}

        elif self.name == "Drak_Sprite" or self.name == "LizardMan_Sprite" or self.name == "Newt_Sprite":
            self.__charge(8)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}
            self.hauteurSol += 15 # Move the monster down / Déplace le monstre vers le bas


        elif self.name == "Elder_Sprite":
            self.__charge(8)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_STILL", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}
        



        # Map : Volcano
        elif self.name == "BarbBulb_Sprite":
            self.__charge(40,1.5)
            self.setSpeedEffect(2)
            self.stats = {"type": "HEAL", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Sleepy_Sprite" or self.name == "Hopper_Sprite":
            self.__charge(7)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "MadGong_Sprite":
            self.__charge(31)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Roach_Sprite" or self.name == "GiantRoach_Sprite":
            self.__charge(7)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "TarMan_Sprite" or self.name == "LavaMan_Sprite" or self.name == "ToxicMan_Sprite":
            self.__charge(8,2)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}


        elif self.name == "Chimera_Sprite":
            self.__charge(18)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Golem_Sprite":
            self.__charge(4)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}
        


        # Map : Forestia  
        elif self.name == "Angler_Sprite":
            self.__charge(36)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}
            self.hauteurSol += 25 # Move the monster down / Déplace le monstre vers le bas

        elif self.name == "PainWeed_Sprite" or self.name == "RankWeed_Sprite" or self.name == "VileWeed_Sprite":
            self.__charge(8,1.2)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}
            self.hauteurSol += 10 # Move the monster down / Déplace le monstre vers le bas

        elif self.name == "VileWeed_Sprite":
            self.__charge(8)
            self.setSpeedEffect(2)
            self.stats = {"type": "HEAL", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}
        
        elif self.name == "Cacti_Sprite":
            self.__charge(8,1.3)
            self.setSpeedEffect(2)
            self.stats = {"type": "HEAL", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Codger_Sprite":
            self.__charge(5)
            self.setSpeedEffect(2)
            self.stats = {"type": "STRENGTH", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "FoulWeed_Sprite":
            self.__charge(7)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Gonghead_Sprite":
            self.__charge(31,2)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Mutant_Sprite":
            self.__charge(8,1.5,True)
            self.setSpeedEffect(2)
            self.stats = {"type": "STRENGTH", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Slasher_Sprite" or self.name == "Ripper_Sprite":
            self.__charge(12)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "TankBot_Sprite" or self.name == "HyperBot_Sprite" or self.name == "ArmorBot_Sprite" or self.name == "ProtoBot_Sprite":
            self.__charge(6,2,True)
            self.setSpeedEffect(2)
            self.stats = {"type": "SHOOTER", "vie": 50, "damage": 0, "shootDamage": 5, "range": 250, "cooldown": 3, "speed": 4, "maxvie": 50}

            self.arme = {"arme": Armef.ArmesAvecForme(self.name, self.stats["shootDamage"], self.stats["range"], 1), "speed": 15}  # {Type d'arme, vitesse de l'arme} / {Weapon, speed}

        elif self.name == "Plant42_Sprite" or self.name == "Audrey_Sprite1":
            self.__charge(6)
            self.setSpeedEffect(2)
            self.stats = {"type": "SHOOTER_STILL", "vie": 50, "damage": 0, "shootDamage": 5, "range": 250, "cooldown": 3, "speed": 4, "maxvie": 50}

            self.arme = {"arme": Armef.ArmesAvecForme(self.name, self.stats["shootDamage"], self.stats["range"], 1), "speed": 15}  # {Type d'arme, vitesse de l'arme} / {Weapon, speed}


        elif self.name == "Gazer_Sprite":
            self.__charge(24)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "ManTrap_Sprite":
            self.__charge(7)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "MyriaIIIBoss_Sprite":
            self.__charge(8)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_STILL", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Nue_Sprite":
            self.__charge(11)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_STILL", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Insector_Sprite" or self.name == "FlyMan_Sprite":
            self.__charge(20)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}




        # Map : Dead Zone
        elif self.name == "Bat_Sprite" :
            self.__charge(4,2)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "PipeBomb_Sprite" or self.name == "Bomber_Sprite" or self.name == "BombSeed_Sprite":
            self.__charge(3,2)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "DeathBot_Sprite" or self.name == "MultiBot_Sprite":
            self.__charge(24,1.5)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "MistMan_Sprite" or self.name == "Armor_Sprite":
            self.__charge(8,1.5)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}


        elif self.name == "DragonZombie_Sprite":
            self.__charge(8)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Phantom_Sprite" or self.name == "Reaper_Sprite" or self.name == "Revenant_Sprite":
            self.__charge(8)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_STILL", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Vampire_Sprite":
            self.__charge(16)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_STILL", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}


        
        # Map : Candya

        elif self.name == "Scorpion_Sprite" or self.name == "GiantCrab_Sprite":
            self.__charge(10)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Gooey_Sprite" or self.name == "GooKing_Sprite" or self.name == "GooTitan_Sprite" or self.name == "EyeGoo_Sprite" or self.name == "MageGoo_Sprite" or self.name == "PuffGoo_Sprite":
            self.__charge(11, 2)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Thunder_Sprite" or self.name == "Volt_Sprite":
            self.__charge(16)
            self.setSpeedEffect(2)
            self.stats = {"type": "COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "HugeSlug_Sprite":
            self.__charge(6)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_COMMON", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}

        elif self.name == "Sample4_Sprite":
            self.__charge(30)
            self.setSpeedEffect(2)
            self.stats = {"type": "BOSS_STILL", "vie": 100, "damage": 1, "cooldown": 1,"speed": 3, "maxvie": 100}








        self.y = self.hauteurSol - self.hitbox[1]
        self.charges = self.chargesRight[self.lastchargesRight[0]]

        self.baseDamage = self.stats["damage"]
        self.cooldwon = [EZ.clock(), 1]

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
        
        else:
            self.x -= vitesseFond



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
    """ Monstre with effect around it
    Monstre avec des effet/ buff autour d'eux"""

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
        """ Set the area of the power
        Definit la zone ou le monstre donnera l'effet"""
    
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
        """ Draw the strength effect
        Trace l'effet de la zone de force"""
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

    def __init__(self, name, xPlayer, HauteurSol, Xspawn=0):
        super().__init__(name, xPlayer, HauteurSol, Xspawn)
        super().charge()

        self.range = self.stats["range"] # Rayon de tir / range of monster
        
        self.timeShoot = self.cooldwon # [temps du dernier tire, cooldown] / [time of last shoot, cooldown]

        self.lastMove = {"right": True, "left": False} # Direction vers laquelle le monstre regarde / direction of the monster
    

    def shoot(self):
        """ Do the shoot
        Fait tirer le Montre"""

        if self.move_info["right"] or self.lastMove["right"]:
            self.arme["arme"].Setup(self.x + self.hitbox[0]//2, self.y + self.hitbox[1]//2, "right")
        
        elif self.move_info["left"] or self.lastMove["left"]:
            self.arme["arme"].Setup(self.x + self.hitbox[0]//2, self.y + self.hitbox[1]//2, "left")
            
    def display(self, vitesseFond):
        super().display(vitesseFond)
        self.onShoot()


    def onShoot(self):
        """Move the bullet during the shoot
        Deplace la balle pendant le tire"""
        self.arme["arme"].display(self.arme["speed"], self.vitesseFond, self.stats["vie"])

        if EZ.clock() - self.timeShoot[0] > self.timeShoot[1]: # cooldown de l'arme
            self.timeShoot[0] = EZ.clock()
            self.shoot()


    def move(self, vitesseFond):
        """ Move the monster in function of the player
        Deplace le monstre en fonction de la position du joueur

        Args:
            vitesseFond (float): deplacement du fond
        """
        

        if self.x < self.xPlayer - self.range + 50: # + 50 pour eviter de ne pas toucher le joueur / + 50 to avoid to touch the player
            self.move_info["right"] = True
            self.move_info["left"] = False

            self.lastMove["right"] = True
            self.lastMove["left"] = False
        
        elif self.x > self.xPlayer + self.range - 50: # - 50 pour eviter de ne pas toucher le joueur / - 50 to avoid to touch the player
            self.move_info["left"] = True 
            self.move_info["right"] = False

            self.lastMove["left"] = True
            self.lastMove["right"] = False
        

        else:
            self.move_info["left"] = False
            self.move_info["right"] = False

            if self.x < self.xPlayer:
                self.lastMove["right"] = True
                self.lastMove["left"] = False
            
            elif self.x > self.xPlayer:
                self.lastMove["left"] = True
                self.lastMove["right"] = False

        self.moveX(vitesseFond)
        self.moveEffect()

        self.zoneHitBox()
        self.vitesseFond = vitesseFond
    
    def moveEffect(self):

        if self.move_info["right"] or self.move_info["left"]:
            super().moveEffect()

        else:
            if self.lastMove["left"]:
                self.moveEffectLeft()
            
            elif self.lastMove["right"]:
                self.moveEffectRight()



class Boss(Monstre):
    """class of the boss (big and strong monster)
    Classe du boss (monstre fort et gros)"""

    def __init__(self, name, xPlayer, hauteurSol, Xspawn=0):
        super().__init__(name, xPlayer, hauteurSol, Xspawn)
        self.autoheal = {"cooldown": [0, 3], "heal": 2} # the boss will regen as player after a specific time[temps du dernier degat, cooldown] / Les boss regen comme les joueur après un certain temps [time of last heal, cooldown]
    
    def regen(self):
        """ Heal the boss
        Regen le boss"""
        if EZ.clock() - self.autoheal["cooldown"][0] > self.autoheal["cooldown"][1]:
            self.heal(self.autoheal["heal"])
        
    def domage(self, domage):
        super().domage(domage)
        self.autoheal["cooldown"][0] = EZ.clock()
    
    def display(self, vitesseFond):
        super().display(vitesseFond)
        self.regen()



class BossShooter(MonstreShooter, Boss):
    """class of the boss (big and strong monster) that shoot
    Classe du boss (monstre fort et gros) qui tire"""

    def __init__(self, name, xPlayer, HauteurSol, Xspawn=0):
        super().__init__(name, xPlayer, HauteurSol, Xspawn)
        self.autoheal = {"cooldown": [0, 3], "heal": 2} # the boss will regen as player after a specific time[temps du dernier degat, cooldown] / Les boss regen comme les joueur après un certain temps [time of last heal, cooldown]
        
        self.range = self.stats["range"] # Rayon de tir / range of monster
        
        self.timeShoot = self.cooldwon # [temps du dernier tire, cooldown] / [time of last shoot, cooldown]

        self.lastMove = {"right": True, "left": False} # Direction vers laquelle le monstre regarde / direction of the monster
    
    def display(self, vitesseFond):
        super().display(vitesseFond)