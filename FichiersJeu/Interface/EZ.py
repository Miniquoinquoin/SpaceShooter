# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 21:07:27 2018

@author: Eric Caspar

v1.1 (du 12/08/2019)
v1.2 (du 08/09/2019) Ajout de la fonction affichage de texte.
v1.3 (du 10/09/2019) Ajout des reglage_fps et image suivante
v1.3.1 (du 18/09/2019) Nettoyage du code.
v1.4 (du 25/09/2019) Ajout de la fonction trace arc
v1.5 (du 30/09/2019) Ajout des fonctions permettant de tracer des éllipses.
v1.51 (du 1/10/2019 Correction d'un bug sur trace_secteur_angulaire (des segments en trop)
                    Modification de l'orientation des angles dans trace arc
v1.5.2 (du 10/10/2019) Correction de bugs
v1.5.3 (du 2/12/2019) Correction d'un bug sur les chemins
v1.6 (du 3/12/2019) Ajout de la rotation et du zoom d'une image
v1.6.1 (du 5/12/2019) Problème sur le chemin retour en arrière
v1.6.2 (du 21/12/2019) Ajout d'otions pour la recherche des chemins
v1.7 (du 11/03/2021) Ajout de fonctions pour avoir une vrai matrice de tupple pour cha
rger et sauvegarder une image
"""

"""
Liste des événements :
"RIEN"
"TOUCHE_ENFONCEE"
"TOUCHE_RELACHEE"
"SOURIS_MOUVEMENT"
"SOURIS_BOUTON_DROIT_ENFONCE"
"SOURIS_BOUTON_GAUCHE_ENFONCE"
"SOURIS_BOUTON_DROIT_RELACHE"
"SOURIS_BOUTON_GAUCHE_RELACHE"
"SOURIS_MOLETTE_HAUT"
"SOURIS_MOLETTE_BAS"
"EXIT"
"""

from tkinter import Canvas
import pygame
import time
import math
from pygame.locals import *
import pygame.gfxdraw
import os


global fenetre
global evenement
global clavier

global fps
global debut
mon_chemin = os.path.dirname(__file__)



def creation_fenetre(largeur=300,hauteur=200,nom="fenetre",icone=None):
    """Fonction qui initialise la partie graphique et crée une fenetre
    de taille donnée"""
    global fenetre
    global clavier
    global son
    if(icone!=None):
        image=charge_image(icone)
    else:
        image=creation_image(25,25)
        trace_rectangle_droit_v2(0,0,25,25,255,0,0,canvas=image)
    clavier={"q":"a",";":"m","a":"q","z":"w","w":"z","m":","}
    pygame.init()
    fenetre=pygame.display.set_mode((largeur,hauteur))
    pygame.display.set_caption(nom)
    pygame.display.set_icon(image)
    fenetre.fill([255,255,255])
    pygame.display.flip()

def test_fenetre():
    """ Test si la fentre est ouverte"""
    return pygame.display.get_init

def creation_image(longueur,hauteur):
    """Creation d'une image (Surface) que l'on peut modifier et sauvegarder"""
    if pygame.display.get_init==True:
        return pygame.Surface((longueur,hauteur)).convert_alpha()
    else:
       return pygame.Surface((longueur,hauteur))

def recupere_couleur_image(image,x,y):
    """Recupere une couleur à la position x et y"""
    return image.get_at((x,y))

def colorie_pixel_image(image,x,y,rouge,vert,bleu,transparence=255):
    """Equivalent à EZ.trace_point, sauf que la fenetre n'est plus la surface par défaut"""
    trace_point(x,y,rouge,vert,bleu,transparence,image)

def destruction_fenetre():
    """Fonction qui détruit la fenetre"""
    pygame.quit()

def __choix(canevas):
    """Fonction interne"""
    global fenetre
    if canevas==None:
        surface=fenetre
    else:
        surface=canevas
    return surface

def attendre(duree_en_mini_seconde=1000):
    """Fonction qui attend une duree en miniseconde"""
    pygame.time.wait(duree_en_mini_seconde)

def trace_point(x,y,rouge=0,vert=0,bleu=0,transparence=255,canvas=None):
    """Trace un point de coordonnées (x,y) par défaut la transparence est opaque et la couleur noire
    Si on donne une canvas (en réalité une surface) alors le dessin se fait sur le canvas et pas sur l'ecran"""
    surface=__choix(canvas)
    #surface.set_at((x,y),pygame.Color(rouge,vert,bleu,transparence))
    pygame.gfxdraw.pixel(surface,x,y,(rouge,vert,bleu,transparence))

def dimension(canvas=None):
    surface=__choix(canvas)
    return pygame.Surface.get_size(surface)

def trace_segment(xA,yA,xB,yB,rouge=0,vert=0,bleu=0,transparence=255,canvas=None):
    """Trace un segment [AB] de couleur donné (noir par defaut) par défaut il est aliasé
        Si on donne un canvas (en réalité une surface) alors le dessin se fait sur le canvas et pas sur l'ecran
    """
    surface=__choix(canvas)
    if yA==yB:
        pygame.gfxdraw.hline(surface,xA,xB,yA,(rouge,vert,bleu,transparence))
    elif xA==xB:
        pygame.gfxdraw.vline(surface,xA,yA,yB,(rouge,vert,bleu,transparence))
    else:
        pygame.gfxdraw.line(surface,xA,yA,xB,yB,(rouge,vert,bleu,transparence))

def trace_rectangle_droit(xA,yA,longueur,hauteur,rouge=0,vert=0,bleu=0,transparence=255,canvas=None):
    """Trace un rectangle dont les cotées sont verticaux ou horizantaux de couleur noir par défaut
        Si on donne un canvas alors le dessin se fait sur le canvas et pas sur l'ecran
    """
    surface=__choix(canvas)
    nouvelle_surface=pygame.Surface((longueur,hauteur))
    nouvelle_surface.set_alpha(transparence)
    nouvelle_surface.fill(pygame.Color(rouge,vert,bleu))
    surface.blit(nouvelle_surface,(xA,yA))

def trace_triangle(xA,yA,xB,yB,xC,yC,rouge=0,vert=0,bleu=0,transparence=255,canvas=None):
    """Trace un triangle dont les sommets sont données et de couleurs données par défaut la couleur est noire
        Si on donne un canvas alors le dessin se fait sur le canvas et pas sur l'ecran
    """
    surface=__choix(canvas)
    pygame.gfxdraw.filled_trigon(surface,xA,yA,xB,yB,xC,yC,pygame.Color(rouge,vert,bleu,transparence))

def trace_disque(x,y,rayon,rouge=0,vert=0,bleu=0,transparence=255,canvas=None):
    """Trace un disque dont le centre et le rayon sont données et de couleurs données par défaut la couleur est noire
        Si on donne un canvas alors le dessin se fait sur le canvas et pas sur l'ecran
    """
    surface=__choix(canvas)
    pygame.gfxdraw.filled_circle(surface,x,y,rayon,pygame.Color(rouge,vert,bleu,transparence))

def trace_cercle(x,y,rayon,rouge=0,vert=0,bleu=0,transparence=255,canvas=None):
    """Trace un cercle dont le centre et le rayon sont données et de couleurs données par défaut la couleur est noire
        Si on donne une canvas alors le dessin se fait sur le canvas et pas sur l'ecran
    """
    surface=__choix(canvas)
    pygame.gfxdraw.aacircle(surface,x,y,rayon,pygame.Color(rouge,vert,bleu,transparence))

def __trace_quart_secteur1(x,y,r1,r2,angle1,angle2,r,v,b,t,canvas=None):
    mini=int(math.cos(angle2)*r1)
    maxi=int(math.cos(angle1)*r2)
    for i in range(mini,maxi+1):
        if i==0:
            if (angle2>0 and math.fmod(angle2,2*math.pi) > math.pi/2 - 0.00001) or (angle2<0 and math.fmod(angle2,2*math.pi) < -3*math.pi/2 + 0.00001):
                trace_segment(x,y-r1,x,y-r2,r,v,b,t,canvas)
        else:
            if i<r1:
                hmin=int(max(math.sqrt(abs(r1*r1-i*i)),math.tan(angle1)*i))
            else:
                hmin=int(math.tan(angle1)*i)
            if(angle2%(2*math.pi)==math.pi/2 or angle2%(2*math.pi)==-3*math.pi/2):
                hmax=int(math.sqrt(abs(r2*r2-i*i)))
            else:
                hmax=int(min(math.sqrt(abs(r2*r2-i*i)),math.tan(angle2)*i))
            trace_segment(x+i,y-hmin,x+i,y-hmax,r,v,b,t,canvas)




def __trace_quart_secteur2(x,y,r1,r2,angle1,angle2,r,v,b,t,canvas=None):
    mini=int(math.cos(angle2)*r2)
    maxi=int(math.cos(angle1)*r1)
    for i in range(mini,maxi+1):
        if i==0:
            if (angle1>0 and math.fmod(angle1,2*math.pi) < math.pi/2 + 0.00001) or (angle1<0 and math.fmod(angle1,2*math.pi) < -3*math.pi/2 +  0.00001):
                trace_segment(x,y-r1,x,y-r2,r,v,b,t,canvas)
        else:
            if i>-r1:
                hmin=int(max(math.sqrt(abs(r1*r1-i*i)),math.tan(angle2)*i))
            else:
                hmin=int(math.tan(angle2)*(i))
            if(angle1%(2*math.pi)==math.pi/2 or angle1%(2*math.pi)==-3*math.pi/2):
                hmax=int(math.sqrt(abs(r2*r2-i*i)))
            else:
                hmax=int(min(math.sqrt(abs(r2*r2-i*i)),math.tan(angle1)*(i)))
            trace_segment(x+i,y-hmin,x+i,y-hmax,r,v,b,t,canvas)


def __trace_quart_secteur3(x,y,r1,r2,angle1,angle2,r,v,b,t,canvas=None):
    mini=int(math.cos(angle1)*r2)
    maxi=int(math.cos(angle2)*r1)
    for i in range(mini,maxi+1):
        if i==0:
            if (angle2>0 and math.fmod(angle2,2*math.pi) > 3*math.pi/2 - 0.00001) or (angle2<0 and math.fmod(angle2,2*math.pi) > -math.pi/2 - 0.00001):
                trace_segment(x,y+r1,x,y+r2,r,v,b,t,canvas)
        else:
            if i>-r1:
                hmin=int(max(math.sqrt(abs(r1*r1-i*i)),math.tan(angle1)*(-i)))
            else:
                hmin=int(math.tan(angle1)*(-i))
            if(angle2%(2*math.pi)==-math.pi/2 or angle2%(2*math.pi)==3*math.pi/2):
                hmax=int((math.sqrt(abs(r2*r2-i*i))))
            else:
                hmax=int(min(math.sqrt(abs(r2*r2-i*i)),math.tan(angle2)*(-i)))
            trace_segment(x+i,y+hmin,x+i,y+hmax,r,v,b,t,canvas)


def __trace_quart_secteur4(x,y,r1,r2,angle1,angle2,r,v,b,t,canvas=None):
    mini=int(math.cos(angle1)*r1)
    maxi=int(math.cos(angle2)*r2)
    for i in range(mini,maxi+1):
        if i==0:
            if r1!=0:
                if (angle1>0 and math.fmod(angle1,2*math.pi) < 3*math.pi/2 + 0.00001) or (angle1<0 and math.fmod(angle1,2*math.pi) < -math.pi/2 + 0.00001):
                    trace_segment(x,y+r1,x,y+r2,r,v,b,t,canvas)
        else:
            if i<r1:
                hmin=int(max(math.sqrt(abs(r1*r1-i*i)),-math.tan(angle2)*i))
            else:
                hmin=-int(math.tan(angle2)*i)
            if(angle1%(2*math.pi)==-math.pi/2 or angle1%(2*math.pi)==3*math.pi/2):
                hmax=int((math.sqrt(abs(r2*r2-i*i))))
            else:
                hmax=int(min(math.sqrt(abs(r2*r2-i*i)),math.tan(angle1)*(-i)))
            trace_segment(x+i,y+hmin,x+i,y+hmax,r,v,b,t,canvas)

def trace_secteur_angulaire(x,y,r1,r2,angle1,angle2,rouge=0,vert=0,bleu=0,transparence=255,canvas=None):
    """Trace un secteur angulaire délimité par deux rayons, Attention la fonction est lente
    Si on donne un canvas alors le dessin se fait sur le canvas et pas sur l'ecran"""
    mini,maxi=min(angle1,angle2),max(angle1,angle2)
    fonction=[__trace_quart_secteur1,__trace_quart_secteur2,__trace_quart_secteur3,__trace_quart_secteur4]
    if maxi-mini>=360:
        __trace_quart_secteur1(x,y,r1,r2,0,math.pi/2,rouge,vert,bleu,transparence,canvas)
        __trace_quart_secteur2(x,y,r1,r2,math.pi/2,math.pi,rouge,vert,bleu,transparence,canvas)
        __trace_quart_secteur3(x,y,r1,r2,math.pi,3*math.pi/2,rouge,vert,bleu,transparence,canvas)
        __trace_quart_secteur4(x,y,r1,r2,3*math.pi/2,2*math.pi,rouge,vert,bleu,transparence,canvas)
    else:
       depart=mini//90
       angle_debut=mini
       while True:
           if maxi<depart*90+90:
               fonction[depart%4](x,y,r1,r2,math.radians(angle_debut),math.radians(maxi),rouge,vert,bleu,transparence,canvas)
               return
           else:
               fonction[depart%4](x,y,r1,r2,math.radians(angle_debut),math.radians(depart*90+90),rouge,vert,bleu,transparence,canvas)
               angle_debut=depart*90+90
               depart+=1

def trace_arc(x,y,r,angle1,angle2,rouge=0,vert=0,bleu=0,transparence=255,canvas=None):
    """Trace un arc de cercle, de centre donné et entre deux angles donnés en degré
    Si on donne un canvas alors le dessin se fait sur le canvas et pas sur l'ecran"""
    surface=__choix(canvas)
    mini,maxi=min(-angle1,-angle2),max(-angle1,-angle2)
    pygame.gfxdraw.arc(surface,x,y,r,mini,maxi,(rouge,vert,bleu,transparence))

def trace_ellipse(x,y,rayon_horizontale,rayon_verticale,rouge=0,vert=0,bleu=0,transparence=255,canvas=None):
    """Trace une ellipse (un ovale) de centre (x,y) de rayon horizontale et verticale donnée.
    L'éllipse est droite"""
    surface=__choix(canvas)
    pygame.gfxdraw.aaellipse(surface,x,y,rayon_horizontale,rayon_verticale,(rouge,vert,bleu,transparence))

def trace_ellipse_pleine(x,y,rayon_horizontale,rayon_verticale,rouge=0,vert=0,bleu=0,transparence=255,canvas=None):
    """Trace l'intérieur d'une ellipse (un ovale) de centre (x,y) de rayon horizontale et verticale donnée.
    L'éllipse est droite"""
    surface=__choix(canvas)
    pygame.gfxdraw.filled_ellipse(surface,x,y,rayon_horizontale,rayon_verticale,(rouge,vert,bleu,transparence))


def charge_image(chemin,local = True):
    """Charge une image de chemin donné"""
    if not local :
        chemin = os.path.join(mon_chemin,chemin)

    if pygame.display.get_init==True:
        return pygame.image.load(chemin).convert_alpha()
    else:
        return pygame.image.load(chemin)

def charge_image_en_matrice(chemin,local = True):
    """Charge une image de chemin donné et reourne une matrice de tuplle(r,v,b)"""
    if not local :
        chemin = os.path.join(mon_chemin,chemin)

    if pygame.display.get_init==True:
        image = pygame.image.load(chemin).convert_alpha()
    else:
        image = pygame.image.load(chemin)
    l,h = dimension(image)
    tab = [l*[0] for _ in range(h)]
    for ligne in range(h) :
        for colonne in range(l) :
            tab[ligne][colonne] = recupere_couleur_image(image,colonne,ligne)
    return tab
    

def sauvegarde_image(image,chemin):
    """Sauvegarde une image dans le chemin donné"""
    pygame.image.save(image,chemin)
    
def sauvegarde_image_matrice(mat,chemin) :
    """Sauvegarde une image données sous forme de matrice dans le chemin donné"""
    image = creation_image(len(mat[0]),len(mat))
    for ligne in range(len(mat)) :
        for colonne in range(len(mat[0])) :
            colorie_pixel_image(image,colonne,ligne,mat[ligne][colonne][0],mat[ligne][colonne][1],mat[ligne][colonne][2])
    sauvegarde_image(image,chemin)
        

def trace_image(image,x,y,transparence=255,canvas=None):
    """Trace une image à la postion donnée attention si vous appliquez la transparence il ne faut pas que l'image soit trnaparente elle même
    Par défaut l'image se trace sur la fenetre graphique mais on peut la placer dans un canvas (surface)"""
    surface=__choix(canvas)
    if transparence<255:
        image2=pygame.Surface(image.get_size())
        image2.set_alpha(transparence)
        image2.blit(image,(0,0))
        surface.blit(image2,(x,y))
    else:
        surface.blit(image,(x,y))

def transforme_image(image,angle = 0,zoom = 1.0):
    """ Transforme une image soit avec une rotation soit/ou avec un zoom pour donner une nouvelle image"""
    return pygame.transform.rotozoom(image,angle,zoom)


def recupere_evenement():
    """ Recupère un evénement
    Liste des événements :
    "RIEN"
    "TOUCHE_ENFONCEE"
    "TOUCHE_RELACHEE"
    "SOURIS_MOUVEMENT"
    "SOURIS_BOUTON_DROIT_ENFONCE"
    "SOURIS_BOUTON_GAUCHE_ENFONCE"
    "SOURIS_BOUTON_DROIT_RELACHE"
    "SOURIS_BOUTON_GAUCHE_RELACHE"
    "SOURIS_MOLETTE_HAUT"
    "SOURIS_MOLETTE_BAS"
    "EXIT"
    """
    global evenement
    evenement=pygame.event.poll()
    if evenement==pygame.NOEVENT:
        return "RIEN"
    elif evenement.type==pygame.KEYDOWN:
        return "TOUCHE_ENFONCEE"
    elif evenement.type==pygame.KEYUP:
        return "TOUCHE_RELACHEE"
    elif evenement.type==pygame.MOUSEMOTION:
        return "SOURIS_MOUVEMENT"
    elif evenement.type==pygame.MOUSEBUTTONDOWN:
        if evenement.button==1:
            return "SOURIS_BOUTON_GAUCHE_ENFONCE"
        elif evenement.button==3:
            return "SOURIS_BOUTON_DROIT_ENFONCE"
        elif evenement.button==4:
            return "SOURIS_MOLETTE_HAUT"
        elif evenement.button==5:
            return "SOURIS_MOLETTE_BAS"
        else:
            return "RIEN"
    elif evenement.type==pygame.MOUSEBUTTONUP:
        if evenement.button==1:
            return "SOURIS_BOUTON_GAUCHE_RELACHE"
        elif evenement.button==3:
            return "SOURIS_BOUTON_DROIT_RELACHE"
        elif evenement.button==4:
            return "SOURIS_MOLETTE_HAUT"
        elif evenement.button==5:
            return "SOURIS_MOLETTE_BAS"
        else:
            return "RIEN"
    elif evenement.type==pygame.QUIT:
        return "EXIT"
    else:
        return "RIEN"

def souris_x():
    """Donne la position en x de la souris au moment où l'événement est récupéré"""
    global evenement
    return evenement.pos[0]

def souris_y():
    """Donne la position en y de la souris au moment où l'événement est récupéré"""
    global evenement
    return evenement.pos[1]

def coordonnees_souris():
    """Donne les coordonnees de la souris"""
    global evenement
    return evenement.pos[0],evenement.pos[1]

def touche():
    """Donne la touche appuyé au moment de la récupération de l'événement sous forme de chaine de caractère"""
    global evenement
    global clavier
    caractere=pygame.key.name(evenement.key)
    return clavier.get(caractere,caractere)

def donne_touche():
    """donne la touche enfoncée appuyé sur le boutton droit pour quitter"""
    if pygame.display.get_init()==True:
        while True:
            evenement=recupere_evenement()
            if evenement=="TOUCHE_ENFONCEE":
                print(touche())
            elif evenement=="SOURIS_BOUTON_DROIT_ENFONCE":
                return 1
    else:
        creation_fenetre(400,400)
        while True:
            evenement=recupere_evenement()
            if evenement=="TOUCHE_ENFONCEE":
                print(touche())
            elif evenement=="SOURIS_BOUTON_DROIT_ENFONCE":
                destruction_fenetre()
                return 1

def sauvegarde_fenetre():
    """retourne une image (surface) de l'écran """
    global fenetre
    return fenetre.copy()

def charge_musique(chemin=None,local = True):
    """ Charge une musique que l'on peut jouer avec la fonction musique on"""
    if not local :
        chemin = os.path.join(mon_chemin,chemin)
    if chemin!=None:
        pygame.mixer.music.load(chemin)

def musique_on(nb_boucles = -1):
    """ Joue la musique prealablement chargée"""
    pygame.mixer.music.play(nb_boucles)

def musique_pause():
    """ met en pause la musique"""
    pygame.mixer.music.pause()

def musique_fin_pause():
    """ Met fin à la pause de la musique"""
    pygame.mixer.music.unpause()

def musique_stop():
    """ Stop la musique"""
    pygame.mixer.music.stop()

def musique_volume(volume=0.5):
    """ Fixe un volume à la musique"""
    pygame.mixer.music.set_volume(volume)

def charge_son(chemin=None,local = True):
    """Charge un son qui peut être joué après"""
    if not local :
        chemin = os.path.join(mon_chemin,chemin)
    if chemin!=None:
        return pygame.mixer.Sound(chemin)

def joue_son(son=None):
    """Joue le son donné"""
    son.play()

def attendre_action():
    """Attend une action de la part du joueur"""
    attendre=True
    while attendre:
        evenement=recupere_evenement()
        attendre=(evenement!="SOURIS_BOUTON_GAUCHE_ENFONCE")and\
                (evenement!="SOURIS_BOUTON_GAUCHE_ENFONCE")and\
                (evenement!="TOUCHE_ENFONCE")and\
                (evenement!="EXIT")

def mise_a_jour():
    """Mise a jour de l ecran"""
    pygame.display.flip()

def clock():
    """Donne la duree en seconde"""
    return time.time()

def charge_police(taille=40,nom_police=None,local = True):
    """ definit la taille et le nom de la police"""
    if nom_police != None and not local :
        nom_police = os.path.join(mon_chemin,nom_police)
    return pygame.font.Font(nom_police,taille)

def image_texte(texte,police,r=0,g=0,b=0,antialiasing = True,tuple_fond=None):
    """retourne une image contenant le texte à afficher."""
    return police.render(texte,antialiasing,(r,g,b),tuple_fond)

def reglage_fps(n=60):
    """
    Le réglage donne le nombre maximum d'images à la seconde
    """
    global fps
    global debut
    fps = n
    debut = pygame.time.Clock()

def frame_suivante():
    """
    Attend le temps nécéssaire pour avoir le nombre d'image par seconde demandé
    entre deux appels.
    """
    global fps
    global debut
    debut.tick(fps)


def selectionne_partie_image(image,x,y,l,h) :
    """
    selectionne un morceau de l'image prechargee
    Attention modifier l'image decoupee modifie aussi l image d'origine donc il n'y a pas creation de memoire
    cepedant vous pouvez utiliser la fonction transformation dessus ou l afficher.
    
    """
    return image.subsurface(Rect(x,y,l,h))




    """Partie Heilmann Jonathan
    Fonction dont j'avais besion que EZ ne propose pas encore
    """

def trace_rectangle_droit_v2(xA,yA,longueur,hauteur,rouge=0,vert=0,bleu=0,transparence=255,canvas=None):
    """Trace un rectangle dont les cotées sont verticaux ou horizantaux de couleur noir par défaut
    Si on donne un canvas alors le dessin se fait sur le canvas et pas sur l'ecran

    Fonction simplement beaucoup plus performante
    """

    surface = __choix(canvas)
    pygame.gfxdraw.box(surface, pygame.Rect(xA, yA, longueur, hauteur), pygame.Color(rouge, vert, bleu, transparence))

def trace_polygonne(EnsemblePoint = [(0,0), (20, 20), (40, 40), (50, 95)], rouge=0,vert=0,bleu=0,transparence=255,canvas=None):
    """Trace un polygonne dont les point sont des tuple dans une list noir par défaut
    Si on donne un canvas alors le dessin se fait sur le canvas et pas sur l'ecran

    """

    surface = __choix(canvas)
    pygame.gfxdraw.filled_polygon(surface, EnsemblePoint, pygame.Color(rouge, vert, bleu, transparence))
    