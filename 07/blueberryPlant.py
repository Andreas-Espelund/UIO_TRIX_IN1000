'''
Design et program med en eller flere klasser basert på følgende beskrivelse:

Programmet representerer blåbærplanter. En blåbærplante har en størrelse (cm) og kan bære noen blåbær.
Et blåbær har bare et vekt som er alltid 0.3 gram. Når planten blir vannet vokser den 3 cm, og når planten befruktes
 produserer den 5 nye bær. Det er også mulig å plukke blåbærene (et bær hver gang).

Skriv også litt kode som viser hvordan du kan bruke klassen(e) i programmet ditt.

'''

class BlueberryPlant:
    def __init__(self):
        self._berries = 0
        self._height = 0

    def water(self):
        self._height += 3

    def fertillize(self):
        self._berries += 5

    def pickBerry(self):
        self._berries -= 1

    def getHeight(self):
        return self._height

    def getBerries(self):
        return self._berries
        
