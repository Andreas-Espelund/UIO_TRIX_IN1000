'''
Navn: forekommer.py

a) Lag et program med en funksjon forekommer. Funksjonen skal sjekke forekomster
av tegn i en tekst og returnere True hvis tegnet forekommer i tekststrengen.
Hvis tegnet ikke forekommer i tekststrengen skal funksjonen returnere False.
Funksjonen skal ta inn to parametere: et tegn og en tekststreng.

Test programmet ditt med følgende funksjonskall (skal returnere True):
'''

def forekommer(streng,tegn):
    res = False
    for elm in streng:
        if elm == tegn:
            res = True
    return res

print(forekommer("andreas","a"))


def utenRepetisjon(streng):
    nyTekst = ""
    for i in range (len(streng)):
        if not forekommer(streng[0:i],streng[i]):
            nyTekst += streng[i]
    return nyTekst

print(utenRepetisjon("andreas"))



def antallForskjellige(streng):
    return len(utenRepetisjon(streng))

print(antallForskjellige("aababbabbac"))
