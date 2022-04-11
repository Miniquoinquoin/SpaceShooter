"""Fichier contenant la classe Equipement"""

import FichiersJeu.Interface.Decor as Decor
import FichiersJeu.Interface.EZ as EZ

class Equipement:
    """Class for the equipment
    classe pour les équipements"""

    def __init__(self, nom, type):
        """Constructor for the equipment
        constructeur pour les équipements"""
        self.nom = nom
        self.type = type #shield, grenade, potion
        self.chargeImage()
    
    def chargeImage(self):
        """Charge the image of the equipment
        charge l'image de l'équipement"""

        if self.type == "shield":
            self.chargesImage = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Equipement\Bouclier.png"),0,0.4)
        
        elif self.type == "grenade":
            self.chargesImage = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Equipement\Grenade.png"),0,0.4)
        
        elif self.type == "potion":
            self.chargesImage = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Equipement\Potion.png"),0,0.4)

    
    def traceInfoEquipement(self,x,y):
        """Trace the equipment info at the right top in game
        trace les infos de l'équipement en haut à droite dans le jeu"""

        Decor.traceCadre(x,y,100,100,5,0,(33,47,61),(128,139,151))
        EZ.trace_image(self.chargesImage,x+10,y+10)



class Bouclier(Equipement):
    """Class for the shield
    classe pour le bouclier"""
    
    def __init__(self, durability):
        """Constructor for the shield
        constructeur pour le bouclier"""
        super().__init__("Bouclier", "shield")
        self.chargeImage()
        self.durability = durability
    
    def use(self):
        """Use the shield
        utilise le bouclier"""

        self.durability -= 1
    
    def getDurability(self):
        """Get the shield durability
        obtient la durabilité du bouclier"""
            
        return self.durability #return the shield durability
    
    def isBroken(self):
        """Check if the shield is broken
        vérifie si le bouclier est cassé"""

        if self.durability <= 0:
            return True
        else:
            return False
    
