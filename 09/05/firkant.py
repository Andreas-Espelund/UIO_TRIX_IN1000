class Firkant:
    def __init__(self):
        self._venstre = None
        self._hoyre = None
        self._topp = None
        self._bunn = None 

    def hentInfo(self):
        print("Venstre:",self._venstre)
        print("Hoyre:",self._hoyre)
        print("Topp:",self._topp)
        print("Bunn:",self._bunn) 

    def leggTilSide(self,Side,retning):
        if retning == "venstre" and self._venstre == None:
            self._venstre = Side
        elif retning == "hoyre" and self._hoyre == None:
            self._hoyre = Side
        elif retning == "topp" and self._topp == None:
            self._topp = Side
        elif retning == "bunn" and self._bunn == None:
            self._bunn = Side

    def fjernSide(self,retning):
        if retning == "venstre":
            self._venstre = None
        elif retning == "hoyre":
            self._hoyre = None
        elif retning == "topp":
            self._topp = None
        elif retning == "bunn":
            self._bunn = None

    def erFirkant(self):
        return (self._venstre and self._hoyre and self._topp and self._bunn) is not None 

        