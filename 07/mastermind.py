'''
I denne øvelsen skal du lage en enkel versjon av MasterMind-spillet

Lag en klasse navned MasterMind. MasterMind har variabelen kode som skal lages I konstruktøren. Kode er en liste som består av fire tilfeldige heltaller (hint: bruk random.randint).
Lag en metode hent_bruker_gjett som ber brukeren om en kode (en streng som består av fire heltaller, for eksempel "1234"). Metoden skal konvertere denne streng til en liste med fire heltaller og returnere denne listen.
Lag en metode sjekk_gjett som tar en gjetteliste med fire tall og sammenligner den med den sanne kodelisten. Metoden skal produsere en liste som inneholder et tall hvis tallet var riktig, og "X" hvis tallet ble gjettet feil. For eksempel: hvis koden er [1, 2, 3, 4] og gjettelisten er [1, 2, 1, 2], resultatlisten skal være [1, 2, "X", "X"]
Lag en metode spill som kaller hent_bruker_gjett og sjekk_gjett i en løkke. Denne løkke skal kjøre så lenge brukeren ikke har gjettet riktig kode, og skrive ut resultaten fra sjekk_gjett hver gang. Når brukeren vinner, skriv ut hvor mange ganger de gjettet en kode.
'''
import random
class MasterMind:
    def __init__(self):
        self._kode = []
        for i in range(4):
            nummer = random.randrange(0,9)
            (self._kode).append(nummer)

    def hent_bruker_gjett(self,kode):
        gjett =[]
        for dig in kode:
            gjett.append(int(dig))

        return gjett

    def sjekkFasitKode(self):
        print(self._kode)

    def sjekk_gjett(self,gjetteliste):
        i = 0
        resultatliste =[]
        for num in gjetteliste:
            if num == self._kode[i]:
                resultatliste.append(num)
            else:
                resultatliste.append("X")
            i +=1
        return resultatliste
