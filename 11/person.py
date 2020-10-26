'''
Person klasse
'''

class Person:
    def __init__(self, navn):
        self._mineBiler = [] # Biler personen eier
        self._laanteBiler = [] # Biler som personen laaner, men noen andre eier
        self._navn = navn
    # Flere variable og nyttefunksjoner?

    def __str__(self):
        streng = ""
        for bil in self._mineBiler:
            streng += bil.hentNavn() +" (Eier: "+bil.hentEier().hentNavn()+")"+ ", "

        for bil in self._laanteBiler:
            streng += bil.hentNavn() +" (Eier: "+bil.hentEier().hentNavn()+")"+ ", "
        return self._navn + " disponerer: " + streng

    def hentNavn(self):
        return self._navn

    def kjopBil(self,bil):
        self._mineBiler.append(bil)
        bil.settEier(self)

    def laanBil(self,bil):
        bil.hentEier().fjernBil(bil)
        self._laanteBiler.append(bil)

    def fjernBil(self,bil):
        self._mineBiler.remove(bil)
