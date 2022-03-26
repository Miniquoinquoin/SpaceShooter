"""Fichier contenant l'ensemble bouton"""

import FichiersJeu.Interface.EZ as EZ

def Bouton(x,y,longeur, hauteur,Text,couleurText = (255,255,255), couleurFond = (0, 0,0), tailleBorder = 3, tailleOmbre =3):
    """Drawn a button 

    Args:
        x (int): Coordinate x
        y (int): Coordinate y / Coordonner y
        longeur (int): lenght of the button / longeur du bouton
        hauteur (int): height of the button / hauteur du bouton
        Text (str): Text in the button / Texte dans le bouton
        couleurText (tuple, optional): color of the Text of the Button / Couleur du Texte du bouton. Defaults to (255,255,255).
        couleurFond (tuple, optional): color of the button / Couleur du bouton. Defaults to (0, 0,0).
    """

    EZ.trace_rectangle_droit_v2(x, y, longeur + tailleOmbre, hauteur + tailleOmbre) # Crée les bordure
    EZ.trace_rectangle_droit_v2(x + tailleBorder, y + tailleBorder, longeur - 2*tailleBorder, hauteur - 2*tailleBorder, *couleurFond)
    texte = EZ.image_texte(Text,EZ.charge_police(70, "FichiersJeu\Interface\Entites\Police\Handwritingg _3.ttf", True), *couleurText)
    EZ.trace_image(texte, x + longeur//2 - EZ.dimension(texte)[0]//2, y + hauteur//2 - EZ.dimension(texte)[1]//2)



