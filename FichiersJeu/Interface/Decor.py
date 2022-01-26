import EZ

def nombre_kills(x,y,LONGUEUR,LARGEUR):
    
    #Charge la police par défaut de taille 15
    police = EZ.charge_police(15)
    
    #trace le rectangle Gris clair
    EZ.trace_rectangle_droit(x,y,LONGUEUR+100,LARGEUR+17,191,201,202)

    #trace le texte "nombre de kills" + texte du résultat
    Image_texte_kills = EZ.image_texte("Nombre de kills :",police)
    Nombre_kills = EZ.image_texte("0",police)

    #trace la position du texte
    EZ.trace_image(Image_texte_kills,x+2,y+4)
    EZ.trace_image(Nombre_kills,x+90,y+4)

    EZ.mise_a_jour()

EZ.creation_fenetre(1240,720)
nombre_kills(10,10,0,0)
EZ.mise_a_jour()
EZ.attendre_action()
EZ.destruction_fenetre()