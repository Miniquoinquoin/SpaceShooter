"""Fichier qui gère les animation"""

import pygame
import pygame.gfxdraw
import FichiersJeu.Interface.EZ as EZ
import math

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

    assert intensite <= MAX_INTENSITE

    surface = EZ.__choix(canvas)
    raport = intensite/MAX_INTENSITE * 0.8
    traceEffetDegatJoueurPartie1(raport,longeur, hauteur, PRECISION ,surface)
    traceEffetDegatJoueurPartie2(raport,longeur, hauteur, PRECISION ,surface)
    traceEffetDegatJoueurPartie3(raport,longeur, hauteur, PRECISION ,surface)
    traceEffetDegatJoueurPartie4(raport,longeur, hauteur, PRECISION ,surface)
    