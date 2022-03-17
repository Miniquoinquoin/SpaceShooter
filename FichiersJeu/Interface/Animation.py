"""Fichier qui gère les animation"""

from pickletools import long1
import pygame
import pygame.gfxdraw
import FichiersJeu.Interface.EZ as EZ
# import EZ as EZ
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

    + Drawn the back decoration / trace des forme claire dans le fond pour décorer

    Args:
        longeur (int): lenght of screen / Longeur de la Fenetre
        hauteur (int): height of screen / Hauteur de la Fenetre
        speed (int): speed of animation / vitesse de l'animation
    """

    COULEUR = (0, 88, 207)
    COULEUR_FORME = (0, 70, 170)
    TEMPS_FORME = 500 # Temps qu'on les forme de deco pour se tracer / Time for drawn shapes
    tpsForme = 0 #temps utiliser pour le traçage des forme / Time use by shapes to drawn
    DecalageFond = 0

    while DecalageFond - speed < hauteur:
        
        EZ.trace_rectangle_droit(0,0,longeur, DecalageFond, *COULEUR)
        DecalageFond += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()
    
    while tpsForme - speed <= TEMPS_FORME:
        EZ.trace_disque(longeur//3, hauteur, int(tpsForme * ((longeur/7) / TEMPS_FORME)), *COULEUR_FORME)
        EZ.trace_disque(2 * longeur//3, hauteur//3, int(tpsForme * ((longeur/6) / TEMPS_FORME)), *COULEUR_FORME)
        EZ.trace_disque(0, hauteur//3, int(tpsForme * ((longeur/5) / TEMPS_FORME)), *COULEUR_FORME)
        EZ.trace_disque(7 * longeur//8, 3 * hauteur//4, int(tpsForme * ((longeur/10) / TEMPS_FORME)), *COULEUR_FORME)

        tpsForme += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()


def traceAnimationMortTexteEtWidget(longeur, hauteur, speed, longeurWidget, hauteurWidget):
    """Drawn the animation that write "GAME" and the interface which the score will be display
    Trace L'animation qui écrit "GAME" et l'interface ou sur laquelle le score sera afficher


    Args:
        longeur (int): lenght of screen
        hauteur (int): height of screen 
        speed (int): speed of animation / Vitesse de l'animation
        longeurWidget (int): lenght of widget
        hauteurWidget (int): lenght of widget 
    """

    # Premier Partie / First Part

    DecalageWidget = 0
    x0 = longeur//2 - longeurWidget//2
    y0 = hauteur//2 - hauteurWidget//2
    COULEURFOND = (210, 210, 230)
    COULEURBORDER = (100, 100, 110)
    TAILLE_BORDER = 2

    #Police
    Fonts = EZ.charge_police(50, "FichiersJeu\Interface\Entites\Police\CourageRoad.ttf", True)
    CoordonneesFonts = [longeur//2 - EZ.dimension(EZ.image_texte("GAME", Fonts, 0, 0, 0))[0], y0 - EZ.dimension(EZ.image_texte("GAME", Fonts, 0, 0, 0))[1]] # [x, y]
    TAILLE_OMBRE = 3

    
    TEXTE = "GAME"
    DrawnFont = 0

    while DecalageWidget <= longeurWidget:

        raport = hauteurWidget / longeurWidget
        EZ.trace_triangle(x0, y0,x0 + DecalageWidget, y0, x0 , y0 + int(DecalageWidget * raport), *COULEURFOND)
        EZ.trace_rectangle_droit(x0, y0, DecalageWidget, TAILLE_BORDER, *COULEURBORDER)
        EZ.trace_rectangle_droit(x0, y0, TAILLE_BORDER, int(DecalageWidget * raport), *COULEURBORDER)

        if DrawnFont == 0 and DecalageWidget >= longeurWidget/2:
            EZ.trace_image(EZ.image_texte(TEXTE[0], Fonts, 0, 0, 0), CoordonneesFonts[0] + TAILLE_OMBRE, CoordonneesFonts[1] + TAILLE_OMBRE)
            EZ.trace_image(EZ.image_texte(TEXTE[0], Fonts, 255, 255, 255), CoordonneesFonts[0], CoordonneesFonts[1])
            DrawnFont = 1
        
        elif DrawnFont == 1 and DecalageWidget >= longeurWidget - speed:
            EZ.trace_image(EZ.image_texte(TEXTE[0:2], Fonts, 0, 0, 0), CoordonneesFonts[0] + TAILLE_OMBRE, CoordonneesFonts[1] + TAILLE_OMBRE)
            EZ.trace_image(EZ.image_texte(TEXTE[0:2], Fonts, 255, 255, 255), CoordonneesFonts[0], CoordonneesFonts[1])
            DrawnFont = 2



        DecalageWidget += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()

    #Deuxieme Partie / Seconde Part
    DecalageWidget = 0  

    while DecalageWidget <= longeurWidget//2:

        raport = hauteurWidget / longeurWidget
        EZ.trace_triangle(x0 + longeurWidget, y0,x0, y0 + hauteurWidget, x0 + longeurWidget//2 + DecalageWidget, y0 + hauteurWidget//2 + int(DecalageWidget * raport), *COULEURFOND)

        if DrawnFont == 2 and DecalageWidget >= longeurWidget/4:
            EZ.trace_image(EZ.image_texte(TEXTE[0:3], Fonts, 0, 0, 0), CoordonneesFonts[0] + TAILLE_OMBRE, CoordonneesFonts[1] + TAILLE_OMBRE)
            EZ.trace_image(EZ.image_texte(TEXTE[0:3], Fonts, 255, 255, 255), CoordonneesFonts[0], CoordonneesFonts[1])
            DrawnFont = 3

        elif DrawnFont == 3 and DecalageWidget >= longeurWidget/2 - speed:
            EZ.trace_image(EZ.image_texte(TEXTE, Fonts, 0, 0, 0), CoordonneesFonts[0] + TAILLE_OMBRE, CoordonneesFonts[1] + TAILLE_OMBRE)
            EZ.trace_image(EZ.image_texte(TEXTE, Fonts, 255, 255, 255), CoordonneesFonts[0], CoordonneesFonts[1])
            DrawnFont = 4

        DecalageWidget += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()
        
    EZ.trace_rectangle_droit(x0 + longeurWidget, y0, TAILLE_BORDER * 3, hauteurWidget, *COULEURBORDER)
    EZ.trace_rectangle_droit(x0, y0 + hauteurWidget, longeurWidget + TAILLE_BORDER * 3, TAILLE_BORDER * 3, *COULEURBORDER)

def tracePlayerAnimationMort(longeur, hauteur, longeurWidget, hauteurWidget):

    x0 = longeur//2 - longeurWidget//2
    y0 = hauteur//2 - hauteurWidget//2
    DECAL_X = longeurWidget//20
    DECAL_Y = hauteurWidget//2 - EZ.dimension(EZ.transforme_image( EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A2.png"),0,2))[0]


    EZ.trace_image(EZ.transforme_image( EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A2.png"),0,5), x0 + DECAL_X , y0 + DECAL_Y)

def traceFondInfoScore(longeur, hauteur, speed, longeurWidget, hauteurWidget):

    COULEUR_MARQUER = (140, 140, 140)
    COULEUR_LEGERE = (180, 180, 180)
    TAILLE_BODER = 3
    
    DecalageFond = 0
    x0 = longeur//2 - longeurWidget//2
    y0 = hauteur//2 - hauteurWidget//2
    y1 = y0 + hauteurWidget//6
    x= []

    DebutPlageScore = x0 + longeurWidget//3
    PlageScore = longeurWidget - longeurWidget//3
    HauteurFond = 2 * hauteurWidget/3
    HauteurFondClair = 3 * HauteurFond//4
    HauteurFondSombre = HauteurFond//4


    #Police
    Fonts = EZ.charge_police(50, "FichiersJeu\Interface\Entites\Police\CourageRoad.ttf", True)
    CoordonneesFonts = [longeur//2 + EZ.dimension(EZ.image_texte("   ", Fonts, 0, 0, 0))[0], y0 - EZ.dimension(EZ.image_texte("OVER", Fonts, 0, 0, 0))[1]] # [x, y]
    TAILLE_OMBRE = 3

    
    TEXTE = "OVER"
    DrawnFont = 0

    for xStart in range(3):
        x.append(DebutPlageScore + xStart * PlageScore//3)


    while DecalageFond - speed <= HauteurFondClair:

        for rectangle in range(3):
            EZ.trace_rectangle_droit(x[rectangle],y1, PlageScore//3 - 20, DecalageFond, *COULEUR_LEGERE)
            EZ.trace_rectangle_droit(x[rectangle],y1, PlageScore//3 - 20, TAILLE_BODER, *COULEUR_MARQUER)
            EZ.trace_rectangle_droit(x[rectangle],y1, TAILLE_BODER, DecalageFond, *COULEUR_MARQUER)
            EZ.trace_rectangle_droit(x[rectangle] + PlageScore//3 - 20,y1, TAILLE_BODER, DecalageFond, *COULEUR_MARQUER)
            



        if DrawnFont == 0 and DecalageFond >= (HauteurFondClair) * 1/4:
            EZ.trace_image(EZ.image_texte(TEXTE[0], Fonts, 0, 0, 0), CoordonneesFonts[0] + TAILLE_OMBRE, CoordonneesFonts[1] + TAILLE_OMBRE)
            EZ.trace_image(EZ.image_texte(TEXTE[0], Fonts, 255, 255, 255), CoordonneesFonts[0], CoordonneesFonts[1])
            DrawnFont = 1
        
        elif DrawnFont == 1 and DecalageFond >= (HauteurFondClair) * 2/4:
            EZ.trace_image(EZ.image_texte(TEXTE[0:2], Fonts, 0, 0, 0), CoordonneesFonts[0] + TAILLE_OMBRE, CoordonneesFonts[1] + TAILLE_OMBRE)
            EZ.trace_image(EZ.image_texte(TEXTE[0:2], Fonts, 255, 255, 255), CoordonneesFonts[0], CoordonneesFonts[1])
            DrawnFont = 2

        elif DrawnFont == 2 and DecalageFond >= (HauteurFondClair) * 3/4:
            EZ.trace_image(EZ.image_texte(TEXTE[0:3], Fonts, 0, 0, 0), CoordonneesFonts[0] + TAILLE_OMBRE, CoordonneesFonts[1] + TAILLE_OMBRE)
            EZ.trace_image(EZ.image_texte(TEXTE[0:3], Fonts, 255, 255, 255), CoordonneesFonts[0], CoordonneesFonts[1])
            DrawnFont = 3

        elif DrawnFont == 3 and DecalageFond >= (HauteurFondClair) - speed:
            EZ.trace_image(EZ.image_texte(TEXTE, Fonts, 0, 0, 0), CoordonneesFonts[0] + TAILLE_OMBRE, CoordonneesFonts[1] + TAILLE_OMBRE)
            EZ.trace_image(EZ.image_texte(TEXTE, Fonts, 255, 255, 255), CoordonneesFonts[0], CoordonneesFonts[1])
            DrawnFont = 4
        
        DecalageFond += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()
    

    DecalageFond = 0

    while DecalageFond - speed <= HauteurFondSombre:

        for rectangle in range(3):
            EZ.trace_rectangle_droit(x[rectangle],y1 + HauteurFondClair, PlageScore//3 - 20 + TAILLE_BODER, DecalageFond, *COULEUR_MARQUER)
            
        DecalageFond += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()


def traceAnimationMenuMort(longeur, hauteur, speed):

    LONGEUR_WIDGET = longeur - 200
    HAUtEUR_WIDGET = 2 * hauteur//3

    traceAnimationMort(longeur, hauteur, speed)
    traceAnimationArriverMenu(longeur, hauteur, speed * 15)
    traceAnimationMortTexteEtWidget(longeur, hauteur, speed * 15, LONGEUR_WIDGET, HAUtEUR_WIDGET)
    tracePlayerAnimationMort(longeur, hauteur, LONGEUR_WIDGET, HAUtEUR_WIDGET)
    traceFondInfoScore(longeur, hauteur, speed * 5, LONGEUR_WIDGET, HAUtEUR_WIDGET)

# EZ.creation_fenetre(1280, 720)

# EZ.reglage_fps(60)

# traceAnimationMenuMort(1280, 720, 3)

# EZ.mise_a_jour()
# EZ.attendre_action()
# EZ.destruction_fenetre()