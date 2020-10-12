class Dvd: 
    def __init__(self,tittel,produsent,utgaveNummer):
        self._tittel = tittel
        self._produsent = produsent 
        self._utgaveNummer = utgaveNummer

    def __str__(self):
        return self._tittel

    def __eq__(self,andre):
        return (self._tittel == andre._tittel) and (self._produsent == andre._produsent)\
            and (self._utgaveNummer == andre._utgaveNummer)

'''
TEST av Dvd klassen 
'''

minDvd = Dvd("starwars","disney","1st edition")

annenDvd = Dvd("starwars","disney","1st edition")

print(minDvd == annenDvd)

print(minDvd)

print(annenDvd)