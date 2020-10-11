class Vare:
    def __init__(self,beskrivelse):
        self._beskrivelse = beskrivelse
        self._hoyesteBud = 0

    def by(self,pris):
        if pris > self._hoyesteBud:
            self._hoyesteBud = pris

    def seBud(self):
        if self._hoyesteBud == 0:
            print("Ingen har budd paa denne varen enda.")
        return self._hoyesteBud

