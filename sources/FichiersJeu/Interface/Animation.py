"""Fichier qui gère les animation"""

import pygame
import pygame.gfxdraw
import FichiersJeu.Interface.EZ as EZ
import math
import FichiersJeu.Interface.Entites.Bouton as Btn

#Import de modification
# import Entites.Bouton as Btn
# import EZ as EZ

""" Effet Degat Joueur"""

MAX_INTENSITE = 50

def traceEffetDegatJoueurPartie1(raport ,longeurFenetre, hauteurFenetre, precision ,surface, couleur = (255,0,0)):
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
    pygame.gfxdraw.filled_polygon(surface, AllPoint, pygame.Color(couleur[0],couleur[1],couleur[2],int(64*raport)))


def traceEffetDegatJoueurPartie2(raport ,longeurFenetre, hauteurFenetre, precision ,surface, couleur = (255,0,0)):
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
    pygame.gfxdraw.filled_polygon(surface, AllPoint, pygame.Color(couleur[0],couleur[1],couleur[2],int(64*raport)))

def traceEffetDegatJoueurPartie3(raport ,longeurFenetre, hauteurFenetre, precision ,surface, couleur = (255,0,0)):
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
    pygame.gfxdraw.filled_polygon(surface, AllPoint, pygame.Color(couleur[0],couleur[1],couleur[2],int(64*raport)))

def traceEffetDegatJoueurPartie4(raport ,longeurFenetre, hauteurFenetre, precision ,surface, couleur = (255,0,0)):
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
    pygame.gfxdraw.filled_polygon(surface, AllPoint, pygame.Color(couleur[0],couleur[1],couleur[2],int(64*raport)))

def traceEffetDegatJoueur(intensite, longeur, hauteur ,canvas = None, couleur = (255,0,0)):
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
    traceEffetDegatJoueurPartie1(raport,longeur, hauteur, PRECISION ,surface, couleur)
    traceEffetDegatJoueurPartie2(raport,longeur, hauteur, PRECISION ,surface, couleur)
    traceEffetDegatJoueurPartie3(raport,longeur, hauteur, PRECISION ,surface, couleur)
    traceEffetDegatJoueurPartie4(raport,longeur, hauteur, PRECISION ,surface, couleur)

"""Effet Mort Joueur / Player death effect"""

#Fond
COULEUR = (0, 88, 207)
COULEUR_FORME = (0, 70, 170)

#Interface
COULEUR_BORDER = (100, 100, 110)
TAILLE_BORDER = 2
TAILLE_OMBRE = 3 # Ombre de la police
COULEUR_MARQUER = (140, 140, 140) #Couleur externe des rectangle stats
COULEUR_LEGERE = (180, 180, 180) # Couleur interne des rectangle stats
COULEURFOND = (210, 210, 230) # Couleur de fond du rectangle principale

COULEUR_POLICE_SCORE = (20, 20, 20)
ESPACE_POLICE_SCORE = 50 # espace entre le chifre de uniter et le cotre droit du cadra stats

TAILLE_BOUTON = [300, 90] # Taille des bouton [x, y]

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


    TEMPS_FORME = 500 # Temps qu'on les forme de deco pour se tracer / Time for drawn shapes
    tpsForme = 0 #temps utiliser pour le traçage des forme / Time use by shapes to drawn
    DecalageFond = 0

    while DecalageFond - speed < hauteur:
        
        EZ.trace_rectangle_droit_v2(0,0,longeur, DecalageFond, *COULEUR)
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


    #Police
    Fonts = EZ.charge_police(50, "FichiersJeu\Interface\Entites\Police\CourageRoad.ttf", True)
    CoordonneesFonts = [longeur//2 - EZ.dimension(EZ.image_texte("GAME", Fonts, 0, 0, 0))[0], y0 - EZ.dimension(EZ.image_texte("GAME", Fonts, 0, 0, 0))[1]] # [x, y]
  

    
    TEXTE = "GAME"
    DrawnFont = 0

    while DecalageWidget <= longeurWidget:

        raport = hauteurWidget / longeurWidget
        EZ.trace_triangle(x0, y0,x0 + DecalageWidget, y0, x0 , y0 + int(DecalageWidget * raport), *COULEURFOND)
        EZ.trace_rectangle_droit_v2(x0, y0, DecalageWidget, TAILLE_BORDER, *COULEUR_BORDER)
        EZ.trace_rectangle_droit_v2(x0, y0, TAILLE_BORDER, int(DecalageWidget * raport), *COULEUR_BORDER)

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
        
    EZ.trace_rectangle_droit_v2(x0 + longeurWidget, y0, TAILLE_BORDER * 3, hauteurWidget, *COULEUR_BORDER)
    EZ.trace_rectangle_droit_v2(x0, y0 + hauteurWidget, longeurWidget + TAILLE_BORDER * 3, TAILLE_BORDER * 3, *COULEUR_BORDER)

def tracePlayerAnimationMort(longeur, hauteur, longeurWidget, hauteurWidget, player):

    x0 = longeur//2 - longeurWidget//2
    y0 = hauteur//2 - hauteurWidget//2
    DECAL_X = longeurWidget//20
    DECAL_Y = hauteurWidget//2 - EZ.dimension(EZ.transforme_image(player,0,2))[1]//2


    EZ.trace_image(EZ.transforme_image( player,0,2), x0 + DECAL_X , y0 + DECAL_Y)

def traceFondInfoScore(longeur, hauteur, speed, longeurWidget, hauteurWidget):
    """Drawn the form of the fond, of stats
    Trace le fond des stats

    Args:
        longeur (int): lenght of screen / longeur de la fenetre
        hauteur (int): height of screen / hauteur de la fenetre
        speed (int): speed of animation
        longeurWidget (int): lenght of widget
        hauteurWidget (int): height of widget
    """
    
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

    
    TEXTE = "OVER"
    DrawnFont = 0

    for xStart in range(3):
        x.append(DebutPlageScore + xStart * PlageScore//3)


    while DecalageFond - speed <= HauteurFondClair:

        for rectangle in range(3):
            EZ.trace_rectangle_droit_v2(x[rectangle],y1, PlageScore//3 - 20, DecalageFond, *COULEUR_LEGERE) #Fond clair
            EZ.trace_rectangle_droit_v2(x[rectangle],y1, PlageScore//3 - 20, TAILLE_BORDER, *COULEUR_MARQUER) # Haut
            EZ.trace_rectangle_droit_v2(x[rectangle],y1, TAILLE_BORDER, DecalageFond, *COULEUR_MARQUER) # Gauche
            EZ.trace_rectangle_droit_v2(x[rectangle] + PlageScore//3 - 20,y1, TAILLE_BORDER, DecalageFond, *COULEUR_MARQUER) # Droite
            



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
            EZ.trace_rectangle_droit_v2(x[rectangle],y1 + HauteurFondClair, PlageScore//3 - 20 + TAILLE_BORDER, DecalageFond, *COULEUR_MARQUER)
            
        DecalageFond += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()


def traceInfoScore(longeur, hauteur, speed, longeurWidget, hauteurWidget, gold, kill, wave):
    """Drawn the form of the fond, of stats
    Trace le fond des stats

    Args:
        longeur (int): lenght of screen / longeur de la fenetre
        hauteur (int): height of screen / hauteur de la fenetre
        speed (int): speed of animation
        longeurWidget (int): lenght of widget
        hauteurWidget (int): height of widget
        gold (int): gold win in game
        kill (int): monstre kill in the game
        wave (int): Player's Death Wave
    """
    
    x0 = longeur//2 - longeurWidget//2
    y0 = hauteur//2 - hauteurWidget//2
    y1 = y0 + hauteurWidget//6

    xPicture= []
    yPicture = []

    xValue = []
    yValue = []

    xFondValeur = []

    DebutPlageScore = x0 + longeurWidget//3
    PlageScore = longeurWidget - longeurWidget//3
    HauteurFond = 2 * hauteurWidget/3
    HauteurFondClair = 3 * HauteurFond//4
    HauteurFondSombre = HauteurFond//4

    for xStart in range(3):
        xFondValeur.append(DebutPlageScore + xStart * PlageScore//3)


    Picture = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\gold.png"),0, 0.25), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\monstreScore.png"), 0, 1.2), EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Vague.png")]
    
    Fonts = EZ.charge_police(70, "FichiersJeu\Interface\Entites\Police\Handwritingg _3.ttf", True)
    Value = [gold, kill, wave]
    NombreAfficher = [0 for valeur in range(len(Value))]
    maxValeur = Value.index(max(Value))

    zomm = 0
    while zomm <= 50:
        for picture in range(len(Picture)):
            EZ.trace_rectangle_droit_v2(xFondValeur[picture],y1, PlageScore//3 - 20, HauteurFondClair, *COULEUR_LEGERE) # Fond Clair
            xPicture.append(DebutPlageScore + picture * PlageScore//3 + PlageScore//6 - EZ.dimension(Picture[picture])[0]//2) #debut partie score + decage de la partie + 1/2 d'une partie - 1/2 Taile X image 
            yPicture.append(y1 + HauteurFondClair//2 - EZ.dimension(Picture[picture])[1]//2 ) 
            EZ.trace_image(EZ.transforme_image(Picture[picture],0,zomm/50),xPicture[picture], yPicture[picture])
    
        zomm += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()

    for value in range(3):
        xValue.append(DebutPlageScore + value * PlageScore//3 + (PlageScore//3 - ESPACE_POLICE_SCORE) - EZ.dimension(EZ.image_texte(str(Value[value]), Fonts, 0, 0, 0))[0])
        yValue.append(y1 + HauteurFondClair + HauteurFondSombre//2 - EZ.dimension(EZ.image_texte("0", Fonts, 0, 0, 0))[1]//3 )



    while NombreAfficher[maxValeur] <= Value[maxValeur]:
        
        for value in range(3):

            NombreAfficher[value] += speed/10 * (1 - NombreAfficher[value]/(Value[value]*1.01) if Value[value] > 0 else 1) * math.sqrt(Value[value]) # Donne l'effet de ralentissement plus on s'aproche du resultat / give a slow effet more the value are near of the resulta 

            EZ.trace_rectangle_droit_v2(xFondValeur[value],y1 + HauteurFondClair, PlageScore//3 - 20 + TAILLE_BORDER, HauteurFondSombre, *COULEUR_MARQUER)
            EZ.trace_image(EZ.image_texte(str(int(NombreAfficher[value])) if NombreAfficher[value] < Value[value] else str(Value[value]),Fonts,*COULEUR_POLICE_SCORE),xValue[value], yValue[value])



        EZ.mise_a_jour()
        EZ.frame_suivante()        


def traceAnimationBouton(longeur, hauteur, speed):
    """Drawn the button of the Death Menu

    Args:
        longeur (int): lenght of th screen
        hauteur (int): lenght of the screen
        speed (int): speed of the animation
    """


    zoom = 10
    while zoom - speed < 100:

        Btn.Bouton(longeur//6 - TAILLE_BOUTON[0]//2, hauteur - hauteur//12 - TAILLE_BOUTON[1]//2, int(TAILLE_BOUTON[0] * zoom/100), int(TAILLE_BOUTON[1] * zoom/100), "", (255, 255, 255), (128, 64, 0))
        Btn.Bouton( 3 *longeur//6 - TAILLE_BOUTON[0]//2, hauteur - hauteur//12 - TAILLE_BOUTON[1]//2, int(TAILLE_BOUTON[0] * zoom/100), int(TAILLE_BOUTON[1] * zoom/100), "", (255, 255, 255), (64, 0, 128))
        Btn.Bouton( 5 * longeur//6 - TAILLE_BOUTON[0]//2, hauteur - hauteur//12 - TAILLE_BOUTON[1]//2, int(TAILLE_BOUTON[0] * zoom/100), int(TAILLE_BOUTON[1] * zoom/100), "", (255, 255, 255), (0, 113, 29))

        zoom += speed

        EZ.mise_a_jour()
        EZ.frame_suivante()
        
    Btn.Bouton(longeur//6 - TAILLE_BOUTON[0]//2, hauteur - hauteur//12 - TAILLE_BOUTON[1]//2, TAILLE_BOUTON[0], TAILLE_BOUTON[1], "Rage quit", (255, 255, 255), (128, 64, 0))
    Btn.Bouton( 3 *longeur//6 - TAILLE_BOUTON[0]//2, hauteur - hauteur//12 - TAILLE_BOUTON[1]//2, TAILLE_BOUTON[0], TAILLE_BOUTON[1], "Menu", (255, 255, 255), (64, 0, 128))
    Btn.Bouton( 5 * longeur//6 - TAILLE_BOUTON[0]//2, hauteur - hauteur//12 - TAILLE_BOUTON[1]//2, TAILLE_BOUTON[0], TAILLE_BOUTON[1], "Replay", (255, 255, 255), (0, 113, 29))

    EZ.mise_a_jour()
    EZ.frame_suivante()


def traceAnimationMenuMort(longeur, hauteur, speed, gold, kill, wave, player):
    """Drawn the Annimation of Death Menu
    Trace l'animation du menu de la mort

    Args:
        longeur (int): lenght of the screen / longeur de la fenetre
        hauteur (int): height of the screen / hauteur de la fenetre
        speed (int): speed of the animation / vitesse de l'animation
        gold (int): value of gold win / valeur de leur ganier
        kill (int): mob killed / mob tué
        wave (int): wave killed / vague tué
    """

    LONGEUR_WIDGET = longeur - 200
    HAUTEUR_WIDGET = 2 * hauteur//3

    traceAnimationMort(longeur, hauteur, speed)
    traceAnimationArriverMenu(longeur, hauteur, speed * 15)
    traceAnimationMortTexteEtWidget(longeur, hauteur, speed * 15, LONGEUR_WIDGET, HAUTEUR_WIDGET)
    tracePlayerAnimationMort(longeur, hauteur, LONGEUR_WIDGET, HAUTEUR_WIDGET, player)
    traceFondInfoScore(longeur, hauteur, speed * 5, LONGEUR_WIDGET, HAUTEUR_WIDGET)
    traceInfoScore(longeur, hauteur, speed, LONGEUR_WIDGET, HAUTEUR_WIDGET, gold, kill, wave)
    traceAnimationBouton(longeur, hauteur, speed * 3)



"""Animation fond Menu Principale / Backgroud animation of the Main Menu """

def traceAnimationFondMenuP(longeur, hauteur, etape):
    """Backgroud animation of the Main Menu
    Animation du menu principale

    Args:
        longeur (int): lenght of the screen / longueur de l'ecran
        hauteur (int): height of the screen / hauteur de l'ecran
        etape (int): step of the animation / etape de l'animation
    """

    EZ.trace_rectangle_droit_v2(0, 0, longeur, hauteur, *COULEUR)

    #Disque:
    EZ.trace_disque(longeur//2, hauteur//2, etape, *COULEUR_FORME) # Disque foncé
    
    if etape >= hauteur: 
        EZ.trace_disque(longeur//2, hauteur//2, etape - hauteur, *COULEUR) # Disque Claire

