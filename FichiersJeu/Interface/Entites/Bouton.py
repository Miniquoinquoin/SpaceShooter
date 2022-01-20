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
    EZ.trace_image(EZ.image_texte("P", EZ.charge_police(147), 10, 20, 20), x + decal_x -2, y + decal_y -2)
    EZ.trace_image(EZ.image_texte("l", EZ.charge_police(145), 10, 20, 20), x + decal_x + 60 -2, y + decal_y -2)
    EZ.trace_image(EZ.image_texte("a", EZ.charge_police(145), 10, 20, 20), x + decal_x + 85 -2, y + decal_y -2)
    EZ.trace_image(EZ.image_texte("y", EZ.charge_police(145), 10, 20, 20), x + decal_x + 130 -2, y + decal_y -2)

    #Texte
    EZ.trace_image(EZ.image_texte("P", EZ.charge_police(130),255, 255, 255), x + decal_x, y + decal_y)
    EZ.trace_image(EZ.image_texte("l", EZ.charge_police(130),255, 255, 255), x + decal_x + 60, y + decal_y)
    EZ.trace_image(EZ.image_texte("a", EZ.charge_police(130),255, 255, 255), x + decal_x + 85, y + decal_y)
    EZ.trace_image(EZ.image_texte("y", EZ.charge_police(130),255, 255, 255), x + decal_x + 130, y + decal_y)