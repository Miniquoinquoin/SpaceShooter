import EZ

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
        EZ.trace_rectangle_droit(x+19*taille/20,y+7*taille/20,taille*1.9,3*taille/10,50,50,50)
        
        #barre de vie à couleur changeante
        EZ.trace_rectangle_droit(x+4*taille/5,y+4*taille/10,taille*2,2*taille/10,30,30,30)
        EZ.trace_rectangle_droit(x+4*taille/5,y+4*taille/10,taille*2*vie/vie_max,2*taille/10,int(-255/vie_max*vie+255),int(255/vie_max*vie),0)

    #affiche le coeur
    display_coeur(x,y,taille,vie,vie_max)

    #trace le nombre de points de vie
        #2 chiffres
    if 10<=vie<100:
        EZ.trace_image(EZ.image_texte(str(vie),EZ.charge_police(int(taille/1.5),None),255,255,255),x+taille/4,y+taille/4)
        #1 chiffres
    elif vie<10:
        EZ.trace_image(EZ.image_texte(str(vie),EZ.charge_police(int(taille/1.5),None),255,255,255),x+3*taille/8,y+taille/4)
        #3 chiffres
    else:
        EZ.trace_image(EZ.image_texte(str(vie),EZ.charge_police(int(taille/1.75),None),255,255,255),x+17*taille/100,y+taille/4)
           
    EZ.mise_a_jour()

EZ.creation_fenetre(1240,720)
info_vie(0,0,100,200,200)
EZ.mise_a_jour()
EZ.attendre_action()
EZ.destruction_fenetre()