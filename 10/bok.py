class Bok:
    def __init__(self,forfatter,navn,aar):
        self._forfatter = forfatter
        self._navn = navn
        self._aar = aar

    def printBok(self):
        print(self._navn,",",self._forfatter,",",str(self._aar))
class Bokhylle:
        def __init__(self):
            self._boker = []
            self._kapasitet = 30

        def erDetPlass(self):
            return len(self._boker) < self._kapasitet

        def leggTilBok(self,bok):
            self._boker.append(bok)

        def finnBok(self,navn,aar):
            for bok in self._boker:
                if (bok._navn == navn) and (self._aar == aar):
                    return bok

        def printHylle(self):
            for bok in self._boker:
                bok.printBok()

class Bibliotek:
    def __init__(self):
        self._bokhyller = []


    def finnBokIBib(self,forfatter,aar):
        bok = None
        for hylle in self._bokhyller:
            bok = hylle.finnBok(forfatter,aar)

        return bok is not None

    def utvidBib(self):
        nyHylle = Bokhylle()
        self._bokhyller.append(nyHylle)
        return nyHylle


    def leggTilBokIBib(self,bok):
        lagtTil = FalseminHylle = Bokhylle()
        for hylle in self._bokhyller:
            if hylle.erDetPlass():
                hylle.leggTilBok(bok)
                lagtTil = True

        if lagtTil == False:
            nyHylle = self.utvidBib()
            nyHylle.leggTilBok(bok)

    def printBib(self):
        for hylle in self._bokhyller:
            hylle.printHylle()


minBib = Bibliotek()

for i in range(60):
    minBok = Bok("Gislaug","Skaldekvad frå Nordfjord",1969)
    minBib.leggTilBokIBib(minBok)

minBib.printBib()
