"""File that calculate the time distribution per lap
Fichier qui permet de calculer la repartition du temps par tour"""

import FichiersJeu.Interface.EZ as EZ


class TimeDistribution:

    def __init__(self) -> None:
        self.timeElement = []

    def newElement(self, name = "Name"):
        """Create a nex element
        Cree un nouvelle element

        Args:
            name (str, optional): name of element. Defaults to "Name".
        """

        self.timeElement.append([EZ.clock(), 0, name])

    def EndElement(self, nbElement = None):
        """Set time of end of element

        Args:
            nbElement (int, optional): element to set time end, if None it's the last element. Defaults to None.
        """

        if nbElement == None:
            self.timeElement[-1][1] = EZ.clock()
        
        else:
            self.timeElement[nbElement - 1][1] = EZ.clock()


    def calculate(self):
        """Calculate the time et proportion of all element
        Calcule le temps et proportion de tout les element
        """

        AllTime = []
        for element in self.timeElement:
            AllTime.append(element[1]- element[0])
        
        somme = 0
        for time in AllTime:
            somme += time
        
        for element, time in zip(self.timeElement, AllTime):
            print(f"{element[2]}: {int(time/somme * 100)} % ")
        

        print(f"All Time: {round(somme, 3)}")
        a = """
        
        
        
        
        
        
        """
        print(a)

    def clear(self):
        """Clear element
        Supprime tout les elements
        """

        self.timeElement = []