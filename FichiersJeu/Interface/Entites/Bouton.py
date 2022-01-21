"""Fichier contenant l'ensemble bouton"""

import FichiersJeu.Interface.EZ as EZ

def BoutonPlayMenu(x, y,longeur = 1240, hauteur = 720):
    """Trace le bouton play sur le menu

    Args:
        longeur (int, optional): longeur de la fenetre. Defaults to 1240.
        hauteur (int, optional): hauteur de la fenetre. Defaults to 720.
    """
    EZ.trace_image(EZ.charge_image("..\Jeu-Dzarian-Miniquoinquoin\FichiersJeu\Interface\Entites\Fond\BoutonPlay.png"),x,y)
    