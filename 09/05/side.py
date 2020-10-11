class Side:
    def __init__(self,lengde,farge):
        self._lengde = lengde 
        self._farge = farge

    def __str__(self):
        utskrift = self._farge+","+str(self._lengde)
        return utskrift

    def hentFarge(self):
         return self._farge

    def hentLengde(self):
         return self._lengde 



        