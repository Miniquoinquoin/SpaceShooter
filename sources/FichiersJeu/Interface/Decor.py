import FichiersJeu.Interface.EZ as EZ
import FichiersJeu.Interface.Entites.Bouton as Btn

# permet de charger l'image une seul fois
image_monstre = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\monstre.png"),0,0.5)
image_wave = [EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Wave\I.png"),0,0.5),EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Wave\V.png"),0,0.5), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Wave\X.png"),0,0.5), EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\Wave\L.png"),0,0.5)] 


def nombre_romain(nombre):
    """Function that transforme the number on roman number
    fonction qui transforme nombre en chiffre romain"""

    #dictionnaire des chiffres romains
    romain = {50:image_wave[3], 40:(image_wave[2] , image_wave[3]), 10:image_wave[2], 9:(image_wave[0] , image_wave[2]), 5:image_wave[1], 4:(image_wave[0] , image_wave[1]), 1:image_wave[0]}

    #liste des chiffres romains
    liste_romain = []

    #tant que le nombre n'est pas nul
    while nombre!=0:
        #on regarde quel chiffre romain correspond le plus au nombre
        for i in romain:
            if nombre >= i:
                #on ajoute le chiffre romain
                if type(romain[i]) != tuple:
                    liste_romain.append(romain[i])
                else:
                    liste_romain.append(romain[i][0])
                    liste_romain.append(romain[i][1])
                #on enleve le chiffre romain de la valeur
                nombre-=i
                #on sort de la boucle
                break
    #on retourne la liste des chiffres romains
    return liste_romain

def saveNumberRoman(nombre, couleurFond = (255,255,255)):
    """Fonction that save the roman number of the wave
    fonction qui sauvegarde le nombre romain de la vague"""
    
    suiteImage = nombre_romain(nombre)
    decalx = 100 - len(suiteImage)*20
    image = EZ.creation_image(200, 46)
    EZ.trace_rectangle_droit_v2(0,0,200,50,*couleurFond, canvas=image)
    for i in suiteImage:
        if i == image_wave[0]:
            EZ.trace_image(i,decalx,0,255, image)
        
        elif i == image_wave[1]:
            decalx -= 10
            EZ.trace_image(i,decalx,10,255, image)

        else:
            EZ.trace_image(i,decalx,10,255, image)
        decalx += EZ.dimension(i)[0] - 5
    

    return image


def display_coeur(x,y,taille,vie,vie_max):
    
    """Trace coeur d'une couleur variant en fonction de la vie

    Args:
        x ([int]): [Coordonées x coin haut gauche]
        y ([int]): [Coordonées y coin haut gauche]
        taille (int, optional): [Taille en pixel x pixel de l'image]. Defaults to 50.
        vie (int, optional): [vie actuelle du joueur]. Defaults to 20.
        vie_max (int, optional): [vie maximum actuelle du joueur]. Defaults to 20.
    """

    #trace coeur à couleur changeante

    EZ.trace_triangle(x+int(taille/2),y+int(1.75*taille/2),x+int(taille/2*0.25+taille/100),y+int(taille/2),x+int(taille/2*1.75-taille/100),y+int(taille/2),int(-255/vie_max*vie+255),int(255/vie_max*vie),0)   
    for i in range(int(35*taille/100),int(65*taille/100)+1,int(30*taille/100)):
        EZ.trace_disque(x+i,y+int(taille/2-taille/12.5),int(23*taille/2/50),int(-255/vie_max*vie+255),int(255/vie_max*vie),0)     
      
def info_vie(x,y,taille=50,vie=20,vie_max=20,barre=True):
    """Trace icone de vie du joueur + barre de vie

    Args:
        x ([int]): [Coordonées x coin haut gauche]
        y ([int]): [Coordonées y coin haut gauche]
        taille (int, optional): [Taille en pixel x pixel de l'image]. Defaults to 50.
        vie (int, optional): [vie actuelle du joueur]. Defaults to 20.
        vie_max (int, optional): [vie maximum actuelle du joueur]. Defaults to 20.
    """
   
    #trace le disque gris
    EZ.trace_disque(x+int(taille/2),y+int(taille/2),int(taille/2),50,50,50) 

    #Afficher la barre ou non
    if barre:
        #contour barre de vie
        EZ.trace_rectangle_droit_v2(x+19*taille/20,y+7*taille/20,taille*1.9,3*taille/10,50,50,50)
        
        #barre de vie à couleur changeante
        EZ.trace_rectangle_droit_v2(x+4*taille/5,y+4*taille/10,taille*2,2*taille/10,30,30,30)
        EZ.trace_rectangle_droit_v2(x+4*taille/5,y+4*taille/10,taille*2*vie/vie_max,2*taille/10,int(-255/vie_max*vie+255),int(255/vie_max*vie),0)

    #affiche le coeur
    display_coeur(x,y,taille,vie,vie_max)

    #trace le nombre de points de vie
        #2 chiffres
    if 10<=vie<100:
        EZ.trace_image(EZ.image_texte(str(int(vie)),EZ.charge_police(int(taille/1.5),None),255,255,255),x+taille/4,y+taille/4)
        #1 chiffres
    elif vie<10:
        EZ.trace_image(EZ.image_texte(str(int(vie)),EZ.charge_police(int(taille/1.5),None),255,255,255),x+3*taille/8,y+taille/4)
        #3 chiffres
    else:
        EZ.trace_image(EZ.image_texte(str(int(vie)),EZ.charge_police(int(taille/1.75),None),255,255,255),x+17*taille/100,y+taille/4)
           
def monster_left(x,y,nb_kills):
    """Function that display the number of monster left
    fonction qui affiche le nombre de monstre restant"""
    
    #trace le rectangle Gris clair
    EZ.trace_rectangle_droit_v2(x-2,y-2,104,54)
    EZ.trace_rectangle_droit_v2(x,y,100,50,191,201,202)

    #trace la position du texte
    EZ.trace_image(image_monstre,x+40,y)
    EZ.trace_image(EZ.image_texte(str(nb_kills),EZ.charge_police(30)),x+16,y+17)

def wave_number(x,y,nb_wave):
    """Function that display the number of the wave
    fonction qui affiche le nombre de la vague"""
    
    pass


def barre_vie_montre(x,y,vie,maxvie,zoom):
    """Fonction qui trace la barre de vie du monstre 

    Args:
        x (int): absice du debut de la barre
        y (y): orrdoner du haut de la barre
        vie (int): vie du monstre
        maxvie (int): vie du monstre quand il spawn
        zoom (float): largeur du monstre
    """
    EZ.trace_rectangle_droit_v2(x, y, int(1 * zoom), int(0.1 * zoom), 200, 200, 200) # Fond gris
    EZ.trace_rectangle_droit_v2(x, y, int(vie/maxvie * zoom), int(0.1 * zoom),int(-255/maxvie*vie+255),int(255/maxvie*vie),0)


def nombreDeGold(x, y, gold):
    """Draw the number of gold in the Main Menu
    Trace le nombre d'or dans le menu principale
    """

    COULEUR_FOND = (100, 100, 100)
    COULEUR_POLICE = (255, 255, 255)

    HAUTEUR = 80

    Btn.Bouton(x, y, 200, HAUTEUR, "", COULEUR_POLICE, COULEUR_FOND, 1, 0)
    image = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\ImageInterface\gold.png"),0, 0.07)
    EZ.trace_image(image ,x + 10, y + HAUTEUR//2 - EZ.dimension(image)[1]//2)

    texte = EZ.image_texte('{:,}'.format(gold).replace(',', ' '),EZ.charge_police(int(70 * 1/(len(str(gold))/3)) if len(str(gold)) > 2 else 70, "FichiersJeu\Interface\Entites\Police\Handwritingg _3.ttf", True), *COULEUR_POLICE)
    EZ.trace_image(texte, x + 20 + EZ.dimension(image)[0], y + HAUTEUR//2 - EZ.dimension(texte)[1]//2)


def traceCadre(x, y, longueur, hauteur, tailleBordure, tailleOmbreBordure, couleurFond, couleurBordure):
    """Draw a framework
    Trace un cadre

    Args:
        x (int): x start of the framework / x de depart du cadre
        y (int): y start of the framework / y de depart du cadre
        longueur (int): lenght of the framework / longueur du cadre
        hauteur (int): height of the framework / hauteur du cadre
        tailleBordure (int): border size / taille de la bordure
        tailleOmbreBordure (int): Shadow size of the border / taille de l'ombre de la bordure
        couleurFond (tuple): background color of the framework / couleur de fond du cadre
        couleurBordure (tuple): Border color of the framework / couleur des bordure du cadre
    """


    EZ.trace_rectangle_droit_v2(x, y, longueur, hauteur, *couleurFond)
    
    #Bordure
    EZ.trace_rectangle_droit_v2(x,y, longueur + tailleOmbreBordure, tailleBordure, *couleurBordure) #Haut
    EZ.trace_rectangle_droit_v2(x,y + hauteur, longueur + tailleOmbreBordure + tailleBordure, tailleBordure + tailleOmbreBordure, *couleurBordure) #Bas
    EZ.trace_rectangle_droit_v2(x,y, tailleBordure, hauteur + tailleOmbreBordure, *couleurBordure) #Gauche
    EZ.trace_rectangle_droit_v2(x + longueur,y, tailleBordure + tailleOmbreBordure, hauteur + tailleOmbreBordure, *couleurBordure) #Droite

def traceFlecheRetour(x, y, zoom):
    """Draw the back arrow
    Trace la flèche retour
    """

    EZ.trace_rectangle_droit_v2(x, y + int(35 * zoom), int(70 * zoom), int(10 * zoom), 255, 255, 255) # Rectangle

    EZ.trace_triangle(x, y + int(40 * zoom), x + int(30 * zoom), y, x - int(10 * zoom), y + int(40 * zoom), 255, 255, 255) #Haut
    EZ.trace_triangle(x, y + int(40 * zoom), x + int(30 * zoom), y + int(70 * zoom), x + int(30 * zoom), y + int(80 * zoom), 255, 255, 255) # Bas
    EZ.trace_triangle(x, y + int(40 * zoom), x - int(10 * zoom), y + int(40 * zoom), x + int(30 * zoom), y + int(80 * zoom), 255, 255, 255) # Bas
    EZ.trace_triangle(x, y + int(40 * zoom), x + int(30 * zoom), y, x + int(30 * zoom), y + int(10 * zoom), 255, 255, 255) #Haut


def traceFlecheAmelioration(x, y, zoom):
    """Draw the upgrade arrow
    Trace la flèche d'amélioration
    """

    EZ.trace_rectangle_droit_v2(x, y + int(35 * zoom), int(70 * zoom), int(10 * zoom), 0, 0, 0) # Rectangle

    EZ.trace_triangle(x + int(70 * zoom), y + int(40 * zoom), x + int(40 * zoom), y, x + int(80 * zoom), y + int(40 * zoom),  0, 0, 0) #Haut
    EZ.trace_triangle(x + int(70 * zoom), y + int(40 * zoom), x + int(40 * zoom), y + int(70 * zoom), x + int(40 * zoom), y + int(80 * zoom),  0, 0, 0) # Bas
    EZ.trace_triangle(x + int(70 * zoom), y + int(40 * zoom), x + int(80 * zoom), y + int(40 * zoom), x + int(40 * zoom), y + int(80 * zoom),  0, 0, 0) # Bas
    EZ.trace_triangle(x + int(70 * zoom), y + int(40 * zoom), x + int(40 * zoom), y, x + int(40 * zoom), y + int(10 * zoom),  0, 0, 0) #Haut

def TraceTextArea(x, y, texte, police, couleur = (0,0,0),delimiteur="|"):
    """Draw a text area
    Trace une zone de texte

    Args:
        x (int): x start of the framework / x de depart du cadre
        y (int): y start of the framework / y de depart du cadre
        longueur (int): lenght of the framework / longueur du cadre
        hauteur (int): height of the framework / hauteur du cadre
        texte (str): text to display / texte a afficher
        police (str): font / police
        delimiteur (str): delimiter / delimiteur
    """

    texte = texte.split(delimiteur)
    for i in range(len(texte)):
        texte[i] = EZ.image_texte(texte[i], police, *couleur)
        EZ.trace_image(texte[i], x, y + i * (EZ.dimension(texte[i])[1]/0.9))

def BareParametre(x,y,longeur, hauteur, etatsSon):
    """Draw the settings menu
    Trace le menu des paramètres

    Args:
        x (int): x start of the framework / x de depart du cadre
        y (int): y start of the framework / y de depart du cadre
        longueur (int): lenght of the framework / longueur du cadre
        hauteur (int): height of the framework / hauteur du cadre
        etatsSon (bool): state of the sound / etat du son
    """

    TAILLE_BOUTON = hauteur * 4/5

    #Trace du cadre
    traceCadre(x, y, longeur, hauteur, 3, 0, (150,150,150), (0,0,0))

    #Trace du texte
    EZ.trace_image(EZ.image_texte("Music", EZ.charge_police(30,"FichiersJeu\Interface\Entites\Police\RobotoMono-VariableFont_wght.ttf"),255,255,255), x + 20, y + int(hauteur/2) - int(EZ.dimension(EZ.image_texte("Music", EZ.charge_police(30,"FichiersJeu\Interface\Entites\Police\RobotoMono-VariableFont_wght.ttf"),255,255,255))[1]/2))

    #Trace des boutons
    EZ.trace_rectangle_droit_v2(x + longeur - TAILLE_BOUTON//0.9, y + hauteur//2 - TAILLE_BOUTON//2, TAILLE_BOUTON, TAILLE_BOUTON, 0 if etatsSon else 255, 200 if etatsSon else 0, 0)



def bareDechargement(x, y, longueur, hauteur, pourcentage):
    """Draw a loading bar
    Trace une bare de chargement

    Args:
        x (int): x start of the loading bar / x de depart de la bare de chargement
        y (int): y start of the loading bar / y de depart de la bare de chargement
        longueur (int): lenght of the loading bar / longueur de la bare de chargement
        hauteur (int): height of the loading bar / hauteur de la bare de chargement
        pourcentage (int): percentage of the loading bar / pourcentage de la barre de chargement
    """

    EZ.trace_rectangle_droit_v2(x, y, longueur, hauteur, 0, 0, 0) # Rectangle

    EZ.trace_rectangle_droit_v2(x + 2, y + 2, longueur * pourcentage/100 - 4 if pourcentage != 0 else 0, hauteur - 4 , 0, 200, 0) # Rectangle of loading / Rectangle de chargement

    EZ.mise_a_jour()


def FondChargement(longueur, hauteur):
    """Draw the background of the load time
    Trace le fond du temps de chargement"""

    EZ.trace_rectangle_droit_v2(0,0,longueur,hauteur,0,0,250)

    image = EZ.transforme_image(EZ.charge_image("FichiersJeu\Interface\Entites\Items\Personnages\Perso1\Perso1A2.png"), 0, 3)
    EZ.trace_image(EZ.transforme_image(image,0,2), longueur//2-144, hauteur//3-144) # -144 pour le centrer, 48*6 / 2
    
