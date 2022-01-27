import EZ

def nombre_kills(x,y,nb_kills,LONGUEUR = 0,LARGEUR = 0):
    
    #Charge la police par défaut de taille 15
    police = EZ.charge_police(30)
    image_monstre = EZ.transforme_image(EZ.charge_image("monstre.png"),0,0.5)
    
    #trace le rectangle Gris clair
    EZ.trace_rectangle_droit(x-2,y-2,LONGUEUR+104,LARGEUR+54)
    EZ.trace_rectangle_droit(x,y,LONGUEUR+100,LARGEUR+50,191,201,202)

    #trace le texte "nombre de kills" + texte du résultat
    
    Nombre_kills = EZ.image_texte(str(nb_kills),police)

    #trace la position du texte
    EZ.trace_image(image_monstre,x+40,y)
    EZ.trace_image(Nombre_kills,x+16,y+17)

    EZ.mise_a_jour()

EZ.creation_fenetre(1240,720)
nombre_kills(100,100,80)
EZ.mise_a_jour()
EZ.attendre_action()
EZ.destruction_fenetre()