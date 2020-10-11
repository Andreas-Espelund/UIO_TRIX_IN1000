class Bok:
    def __init__(self,navn,forfatter,utgivelsesaar):
        self._navn = navn
        self._forfatter = forfatter
        self._utgivelsesaar = utgivelsesaar
    
    def hentNavn(self):
        return self._navn

    def hentUtgivelsesaar(self):
        return self._utgivelsesaar

    def hentForfatter(self):
        return self._forfatter

    def printBok(self):
        print(self._navn)
        print(self._forfatter)
        print(self._utgivelsesaar)

    
