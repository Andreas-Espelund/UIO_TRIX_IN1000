'''
Lag deretter et hovedprogram. Opprett et menneske objekt. 
Deretter skal du manipulere dette objektet. 
Gjør slik at personen du opprettet bytter navn, og har minst en fødselsdag. 
Deretter skal du lage enda et menneskeobjekt. Dette skal du gjøre med 
faaBarn(self, navn) metoden.

Til slutt skal du printe ut navnene på alle barna til personen
'''
from Menneske import Menneske

even = Menneske("Ola",25)
even.bytteNavn("Frank")
for i in range(5):
    even.foedselsdag()

even.faaBarn("Stine")

print(even.hentBarn())

