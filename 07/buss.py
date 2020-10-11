'''
Buss med passasjerer

En buss har en makskapasitet, som er antall mulige sitte- og ståplasser.
Den kan ta opp en og en passasjer hvis bussen ikke er full, og
den kan slippe av en og en passasjer hvis bussen ikke er tom.

Skriv klassen Buss med konstruktør og tilhørende metoder.
Makskapasiteten gir vi når vi oppretter et Buss-objekt.

Skriv metodene erTom og erFull, som skal returnere True eller False
avhengig av om bussen er full eller ikke.

Skriv metodene plukkOpp og slippAv, som sjekker om bussen er tom eller full
og øker og reduserer antall passasjerer på bussen.

Lag også en metode som henter antall passasjerer på bussen, og skriver
ut antallet.


'''


class Buss:
    def __init__(self,makskapasitet):
        self._makskapasitet = makskapasitet
        self._antallPassasjerer = 0

    def erTom(self):
        return self._antallPassasjerer == 0

    def erFull(self):
        return self._antallPassasjerer == self._makskapasitet

    def plukkOpp(self,ant):
        for i in range(ant):
            if not self.erFull():
                self._antallPassasjerer += 1

    def slippAv(self,ant):
        for i in range(ant):
            if not self.erTom():
                self._antallPassasjerer -= 1

    def hentAntall(self):
        return self._antallPassasjerer
