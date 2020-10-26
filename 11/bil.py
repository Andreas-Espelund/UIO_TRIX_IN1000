class Bil:
    def __init__(self,farge,merke):
        self._farge = farge
        self._merke = merke
        self._eier = None

    def settEier(self,person):
        self._eier = person

    def hentEier(self):
        return self._eier

    def hentNavn(self):
        return self._merke
