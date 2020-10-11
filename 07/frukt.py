'''
Klassen Frukt har instansvariablene navn, vannmengde og spiselig.
Metodene er hentVannPr100, erSpiselig og hentNavn
'''

class Frukt:

    def __init__(self,navn,vannmengde,spiselig):
        self._navn = navn
        self._vannmengde = vannmengde
        self._spiselig = spiselig

    def hentVannPr100(self):
        return self._vannmengde

    def erSpiselig(self):
        if self._spiselig.lower() == "ja":
            return True
        return False


    def hentNavn(self):
        return self._navn
