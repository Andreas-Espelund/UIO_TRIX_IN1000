class Plante:
    def __init__(self,maksgrense):
        self._vannbeholder = 0
        self._maksgrensevann = int(maksgrense)
        self._levende = True

    def vannPlante(self,vannCl):
        self._vannbeholder += vannCl

    def nyDag(self):
        self._vannbeholder -= 20
        if self._vannbeholder < 0:
            self._levende = False

    def levende(self):
        return self._levende


flor = Plante(40)
flor2 = Plante(90)

planteliste = [flor,flor2]

for elm in planteliste:
    
