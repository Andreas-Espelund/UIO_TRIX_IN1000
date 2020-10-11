class Hund:
    def __init__(self,alder,rase):
        self._alder = alder
        self._rase = rase

    def hentRase(self):
        return self._rase
    
    def settAlder(self,alder):
        self._alder = alder

    def hentAlder(self):
        return self._alder
    
