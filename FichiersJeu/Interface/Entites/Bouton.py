"""Fichier contenant l'ensemble bouton"""

import FichiersJeu.Interface.EZ as EZ

def BoutonPlayMenu(x, y,longeur = 1240, hauteur = 720):
    """Trace le bouton play sur le menu

    Args:
        longeur (int, optional): longeur de la fenetre. Defaults to 1240.
        hauteur (int, optional): hauteur de la fenetre. Defaults to 720.
    """
    #Fond
    EZ.trace_rectangle_droit(x, y, 400, 130, 20, 196, 20)

    #Cadre
    EZ.trace_rectangle_droit(x, y, 3, 130)
    EZ.trace_rectangle_droit(x, y + 130, 403, 3)
    EZ.trace_rectangle_droit(x, y, 400, 3)
    EZ.trace_rectangle_droit(x + 400, y, 3, 130)

    #Decal texte
    decal_x = 100
    decal_y = 20

    #Ombre
    EZ.trace_image(EZ.image_texte("P", EZ.charge_police(140)), x + decal_x, y + decal_y)
    EZ.trace_image(EZ.image_texte("l", EZ.charge_police(140)), x + decal_x + 55, y + decal_y)
    EZ.trace_image(EZ.image_texte("a", EZ.charge_police(140)), x + decal_x + 80, y + decal_y)
    EZ.trace_image(EZ.image_texte("y", EZ.charge_police(140)), x + decal_x + 125, y + decal_y)

    #Texte
    EZ.trace_image(EZ.image_texte("P", EZ.charge_police(130),255, 255, 255), x + decal_x, y + decal_y)
    EZ.trace_image(EZ.image_texte("l", EZ.charge_police(130),255, 255, 255), x + decal_x + 55, y + decal_y)
    EZ.trace_image(EZ.image_texte("a", EZ.charge_police(130),255, 255, 255), x + decal_x + 80, y + decal_y)
    EZ.trace_image(EZ.image_texte("y", EZ.charge_police(130),255, 255, 255), x + decal_x + 125, y + decal_y)