class  Bokhylle:
    def __init__(self,maksantall):
        self._maksantall = maksantall
        self._boker=[]

    def leggTilBok(self,bok):
        if self.erDetPlass():
            self._boker.append(bok)
            return True
        else:
            return False
    
    def erDetPlass(self):
        if len (self._boker) < self._maksantall:
            return True
        else:
            return False

    def finnBok(self,navn,aar):
        for bok in self._boker:
            if bok.hentNavn() == navn and bok.hentUtgivelsesaar() == aar:
                return bok 
            



