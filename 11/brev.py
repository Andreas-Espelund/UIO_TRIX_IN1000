'''
Fil: brev.py
a) Lag en klasse Brev med en konstruktør som tar inn avsender og mottaker.
Konstruktøren skal sette tre instansvariabler: avsender, mottaker og en tom liste.

b) Lag en metode i klassen som heter skrivLinje som tar i mot en tekststreng og lagrer den i listen vi laget som en instansvariabel.

c) Lag metoden lesBrev som printer ut brevets innhold, samt hilsen. Brevet skal være på formen gitt nedenfor.

d) Opprett et Brev-objekt. Legg til mottaker, avsender og minst to linjer tekst i objektet ved hjelp av skrivLinje-metoden. Kall deretter på lesBrev-metoden som printer ut resultatet til terminalen.

Formen på brevet som skal leveres:

Hei, !

første linje i brevet
andre linje i brevet
....

Hilsen fra

Eksempel på hvordan kjøring av programmet kan se ut:

Hei, Espen Askeladd!

Hvordan har du det?
Jeg har det bare bra!

Hilsen fra
Per Askeladd
'''

class Brev:
    def __init__(self,avsender,mottaker):
        self._avsender = avsender
        self._mottaker = mottaker
        self._liste =[]

    def skrivLinje(self,tekststreng):
        self._liste.append(tekststreng)

    def lesBrev(self):
        print("Hei, "+self._mottaker)

        print("")

        for line in self._liste:
            print(line)

        print("")
        print('Hilsen fra '+self._avsender)
