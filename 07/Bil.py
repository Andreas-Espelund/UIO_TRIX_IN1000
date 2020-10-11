'''
a) Skriv en klasse med navn 'Bil':

b) Bilen skal ha variabelen eier. Denne skal være en tekst streng.

c) Sett eier verdien i en konstruktør (init-metode).

d) Skriv en metode for å skrive ut navnet til eieren.

e) Test klassen din ved å opprette to Bil-objekter med forskjellige
eiere og skrive ut navnet på eieren av det siste objektet du opprettet.
'''

class Bil:
    def __init__(self,eier):
        self._eier = eier
    def skrivUt(self):
        print(self._eier)
