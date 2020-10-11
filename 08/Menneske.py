class Menneske:
    def __init__(self,navn,alder):
        self._navn = navn
        self._alder = alder
        self._erForelder = False
        self._barn =[]

    def foedselsdag(self):
        self._alder += 1

    def bytteNavn(self,nyttNavn):
        self._navn = nyttNavn
    def faaBarn(self,navn):
        self._erForelder = True
        barn = Menneske(navn,0)
        self._barn.append(barn)

    def hentBarn(self):
        return self._barn

