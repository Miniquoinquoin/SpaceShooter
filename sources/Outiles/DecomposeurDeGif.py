"""Permet de décomposer un/des gif choisie

Fait par Heilmann Jonathan le 08/03/2022 (Durer: 5h)
"""

from PIL import Image  #bibliothèque pilow
import os

from tkinter.filedialog import askopenfilenames


def decompose_gif(gif):

    nameFile = str(gif).split("/")[-1].split(".")[0] #Permet de recuperer le nom du fichier en retirant le chemin et l'extention
    pathFile = str(gif).split(".")[0] #Permet de recuperer le chemin du fichier sans l'extention
    pathDirectory = pathFile[0: pathFile.find(nameFile) - 1] if nameFile not in pathFile[pathFile.find(nameFile) + len(nameFile):] else pathFile[0: pathFile.find(nameFile) + len(nameFile)] #Donne le chemin du dossier parent
    DirectoryName = pathDirectory.split("/")[-1]


    if DirectoryName == nameFile:
        os.mkdir(pathDirectory + "/base")
        os.mkdir(pathDirectory + "/reverse")
        pathFile = pathDirectory

    elif not(nameFile in os.listdir(pathDirectory)):
        os.mkdir(pathFile)
        os.mkdir(pathFile + "/base")
        os.mkdir(pathFile + "/reverse")


    print(DirectoryName , nameFile)

    n = 0
    with Image.open(gif) as im:
        
        try:
            while n<100: #Evite la création d'image à l'infinie si bug, qu'on pourait avoir avec une boucle infinie, a augmenté si le gif est composer de plus de 100 images 
                im.seek(n)
                im.save(f"{pathFile}/base/{nameFile}_{n}.png")
                imageFlip = im.transpose(Image.FLIP_LEFT_RIGHT)
                imageFlip.save(f"{pathFile}/reverse/{nameFile}_reverse_{n}.png")
                n += 1

        except EOFError:
            pass  # fin de la sequence d'image


if __name__ == "__main__":        
    folders = askopenfilenames(title = 'Choisir un gif')
    for folder in folders:
        decompose_gif(folder)