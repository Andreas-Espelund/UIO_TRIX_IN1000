class Person:
    def __init__(self,navn,adresse,postnummerOgSted,land,tlfNummer,twitterBrukernavn):
        self._navn = navn
        self._adresse = adresse
        self._postnummerOgSted = postnummerOgSted
        self._land = land
        self._tlfNummer = tlfNummer
        self._twitterBrukernavn = twitterBrukernavn

    def skrivUt(self):
        print(self._navn)
        print(self._adresse)
        print(self._postnummer)
        print(self._tlfNummer)
        print(self._twitterBrukernavn)

    def endreNavn(self,nyttNavn):
        self._navn = nyttNavn

    def endreAdresse(self,nyAdresse):
        self._adresse = nyAdresse

    def endrePostNr(self,nyttPostNr):
        self._postnummerOgSted = nyttPostNr

    def endreLand(self,nyttLand):
        self._land = nyttLand

    def endreTlfNummer(self,nyttNr):
        self._tlfNummer = nyttNr

    def endreTwitter(self,nyttBrukernavn):
        self._twitterBrukernavn = nyttBrukernavn

    def hentNavn(self):
        return self._navn

    def hentAdresse(self):
        return self._adresse

    def hentPostNr(self):
        return self._postnummerOgSted

    def hentLand(self):
        return self._land

    def hentTlfNummer(self):
        return self._tlfNummer

    def hentTwitter(self):
        return self._twitterBrukernavn


def lesInnFil(filnavn):
    fil = open(filnavn)
    brukerinfo=[]
    for linje in fil:
        brukerinfo.append(linje)

    nyPerson = Person(brukerinfo[0],brukerinfo[1],brukerinfo[2],brukerinfo[3],brukerinfo[4],brukerinfo[5])
    fil.close()
    return nyPerson

def lagrePerson(person):
    fil = open("Person.txt","w")

    fil.write(person.hentNavn())

    fil.write(person.hentAdresse())

    fil.write(person.hentPostNr())

    fil.write(person.hentLand())

    fil.write(person.hentTlfNummer())
    fil.close()

def skriv(person):
    print(person.hentNavn())

    print(person.hentAdresse())

    print(person.hentPostNr())

    print(person.hentLand())

    print(person.hentTlfNummer())

    print(person.hentTwitter())



def hovedprogram():
    person = lesInnFil("Person.txt")
    person.endreNavn("Andreas Espelund")
    person.endreTwitter("@donaldTrump")
    lagrePerson(person)
    skriv(person)
hovedprogram()
