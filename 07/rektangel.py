
class Rektangel:

    def __init__(self,lengde,bredde):
        self._lengde=lengde
        self._bredde=bredde

    def oekLengde(self,oekning):
        self._lengde+=oekning

    def oekBredde(self,oekning):
        self._bredde+=oekning

    def reduserLengde(self,reduksjon):
        self._lengde-=reduksjon

    def reduserBredde(self,reduksjon):
        self._bredde-=reduksjon

    def areal(self):
        return self._lengde*self._bredde

    def omkrins(self):
        return 2*self._lengde + 2*self._bredde
