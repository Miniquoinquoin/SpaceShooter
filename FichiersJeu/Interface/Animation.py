"""Fichier qui gère les animation"""

import pygame
import pygame.gfxdraw
# import FichiersJeu.Interface.EZ as EZ
import EZ as EZ
import math


""" Effet Degat Joueur"""

MAX_INTENSITE = 50

def traceEffetDegatJoueurPartie1(raport ,longeurFenetre, hauteurFenetre, precision ,surface):
    """Fonction qui trace la partie 1 de l'effe tdegat joueur = coin superieur droit

    Args:
        intensite (int): intensiter de l'effet
        longeurFenetre (int): longeur de la fennetre
        hauteurFenetre (int): hauteur fenetre
        precision (int): espace entre les point du polynome
        surface (obj): surface sur laquelle l'effet va etre tracee 
    """
    longeur = longeurFenetre //2
    hauteur = hauteurFenetre //2
    
    AllPoint = [(longeur + longeur * raport * math.cos(math.radians(angle)) + longeur * (1 - raport), hauteur - hauteur * (1 - raport) - hauteur * math.sin(math.radians(angle)) * raport) for angle in range(0,91, precision)]
    AllPoint.append((longeurFenetre,0)) #Coin 
    pygame.gfxdraw.filled_polygon(surface, AllPoint, pygame.Color(255,0,0,int(64*raport)))


def traceEffetDegatJoueurPartie2(raport ,longeurFenetre, hauteurFenetre, precision ,surface):
    """Fonction qui trace la partie 2 de l'effe tdegat joueur = coin inferieur droit

    Args:
        intensite (int): intensiter de l'effet
        longeurFenetre (int): longeur de la fennetre
        hauteurFenetre (int): hauteur fenetre
        precision (int): espace entre les point du polynome
        surface (obj): surface sur laquelle l'effet va etre tracee 
    """
    longeur = longeurFenetre //2
    hauteur = hauteurFenetre //2
    
    AllPoint = [(longeur + longeur * raport * math.cos(math.radians(angle)) + longeur * (1 - raport), hauteur + hauteur * (1 - raport) - hauteur * math.sin(math.radians(angle)) * raport) for angle in range(270,361, precision)]
    AllPoint.append((longeurFenetre, hauteurFenetre)) #Coin 
    pygame.gfxdraw.filled_polygon(surface, AllPoint, pygame.Color(255,0,0,int(64*raport)))

def traceEffetDegatJoueurPartie3(raport ,longeurFenetre, hauteurFenetre, precision ,surface):
    """Fonction qui trace la partie 3 de l'effe tdegat joueur = coin inferieur gauche

    Args:
        intensite (int): intensiter de l'effet
        longeurFenetre (int): longeur de la fennetre
        hauteurFenetre (int): hauteur fenetre
        precision (int): espace entre les point du polynome
        surface (obj): surface sur laquelle l'effet va etre tracee 
    """
    longeur = longeurFenetre //2
    hauteur = hauteurFenetre //2
    
    AllPoint = [(longeur + longeur * raport * math.cos(math.radians(angle)) - longeur * (1 - raport), hauteur + hauteur * (1 - raport) - hauteur * math.sin(math.radians(angle)) * raport) for angle in range(180,271, precision)]
    AllPoint.append((0, hauteurFenetre)) #Coin 
    pygame.gfxdraw.filled_polygon(surface, AllPoint, pygame.Color(255,0,0,int(64*raport)))

def traceEffetDegatJoueurPartie4(raport ,longeurFenetre, hauteurFenetre, precision ,surface):
    """Fonction qui trace la partie 4 de l'effe tdegat joueur = coin superieure gauche

    Args:
        intensite (int): intensiter de l'effet
        longeurFenetre (int): longeur de la fennetre
        hauteurFenetre (int): hauteur fenetre
        precision (int): espace entre les point du polynome
        surface (obj): surface sur laquelle l'effet va etre tracee 
    """
    longeur = longeurFenetre //2
    hauteur = hauteurFenetre //2
    
    AllPoint = [(longeur + longeur * raport * math.cos(math.radians(angle)) - longeur * (1 - raport), hauteur - hauteur * (1 - raport) - hauteur * math.sin(math.radians(angle)) * raport) for angle in range(90,181, precision)]
    AllPoint.append((0, 0)) #Coin 
    pygame.gfxdraw.filled_polygon(surface, AllPoint, pygame.Color(255,0,0,int(64*raport)))

def traceEffetDegatJoueur(intensite, longeur, hauteur ,canvas = None):
    """Trace l'effet de degat du joueur

    Args:
        intensite (int): intensitee de l'effet
        longeur (int): longeur de la fenetre
        hauteur (int): hauteur de la fenetre 
        canvas (obj, optional): surface(image) sur laquelle l'effet est tracee. Defaults to None.
    """

    PRECISION = 15


    surface = EZ.__choix(canvas)
    raport = intensite/MAX_INTENSITE * 0.8
    traceEffetDegatJoueurPartie1(raport,longeur, hauteur, PRECISION ,surface)
    traceEffetDegatJoueurPartie2(raport,longeur, hauteur, PRECISION ,surface)
    traceEffetDegatJoueurPartie3(raport,longeur, hauteur, PRECISION ,surface)
    traceEffetDegatJoueurPartie4(raport,longeur, hauteur, PRECISION ,surface)

"""Effet Mort Joueur / Player death effect"""

def traceAnimationMort(longeur, hauteur, speed):
    """Draw the animation of the death of Player
    Trace l'animation de la mort du joueur

    Args:
        longeur (int): lenght of screen / Longeur de la Fenetre
        hauteur (int): height of screen / Hauteur de la Fenetre
        speed (int): speed of animation / vitesse de l'animation
    """


    fermeture = 0
    RedFullScreen = 4.4 * MAX_INTENSITE

    while fermeture <= RedFullScreen:
        traceEffetDegatJoueur(fermeture , longeur, hauteur)

        fermeture += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()

def traceAnimationArriverMenu(longeur, hauteur, speed):
    """Draw the animation of the arrival of the death menu
    Trace l'animation de l'arriver du menu de mort

    Args:
        longeur (int): lenght of screen / Longeur de la Fenetre
        hauteur (int): height of screen / Hauteur de la Fenetre
        speed (int): speed of animation / vitesse de l'animation
    """

    COULEUR = (0, 88, 207)
    DecalageFond = 0

    while DecalageFond - speed < hauteur:
        
        EZ.trace_rectangle_droit(0,0,longeur, DecalageFond, *COULEUR)
        DecalageFond += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()

def traceAnimationMortTexteEtWidget(longeur, hauteur, speed, longeurWidget, hauteurWidget):

    # Premier Partie / First Part

    DecalageWidget = 0
    x0 = longeur//2 - longeurWidget//2
    y0 = hauteur//2 - hauteurWidget//2
    COULEUR = (0, 216, 255)

    while DecalageWidget <= longeurWidget:

        raport = hauteurWidget / longeurWidget
        EZ.trace_triangle(x0, y0,x0 + DecalageWidget, y0, x0 , y0 + int(DecalageWidget * raport), *COULEUR)

        DecalageWidget += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()

    #Deuxieme Partie / Seconde Part
    DecalageWidget = 0  

    while DecalageWidget <= longeurWidget//2:

        raport = hauteurWidget / longeurWidget
        EZ.trace_triangle(x0 + longeurWidget, y0,x0, y0 + hauteurWidget, x0 + longeurWidget//2 + DecalageWidget, y0 + hauteurWidget//2 + int(DecalageWidget * raport), *COULEUR)

        DecalageWidget += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()
        



def traceAnimationMenuMort(longeur, hauteur, speed):

    traceAnimationMort(longeur, hauteur, speed)
    traceAnimationArriverMenu(longeur, hauteur, speed * 15)
    traceAnimationMortTexteEtWidget(longeur, hauteur, speed * 15, longeur - 200, 2 * hauteur//3)

EZ.creation_fenetre(1280, 720)

EZ.reglage_fps(60)

traceAnimationMenuMort(1280, 720, 3)

EZ.mise_a_jour()
EZ.attendre_action()
EZ.destruction_fenetre()