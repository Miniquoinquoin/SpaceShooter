"""Fichier contenant les diferant proprieter des armes / attack"""

class Armes:

    def __init__(self, name, damage, ranges, hitbox):
        self.name = name
        self.damage = damage
        self.range = ranges
        self.hitbox = hitbox

        