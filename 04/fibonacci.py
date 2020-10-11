'''
I matematikk er et fibonaccitall eller et Fibonacci-tall et tall i den uendelige følgen

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
Følgen kalles for Fibonacci-følgen. Bortsett fra de to første startverdiene
0 og 1 framkommer leddene i følgen ved å summere de to forrige leddene.
Er du interessert kan du få mer informasjon her.

I denne oppgaven skal du finne alle Fibonacci nummerne gitt opptil et gitt tall.
Det vil si at du skal finne alle Fibonacci-tallene som er lavere enn det tallet du gir.

Skriv funksjonen finnAlleFibTall som tar inn et tall og returnerer en liste med
alle Fibonacci-tallene som har lavere verdi enn tallet som tas inn. Gitt verdien 11,
skal funksjonen altså returnere [0,1,1,2,3,5,8].

Skriv funksjonen laBrukerSkriveInnTall som lar brukeren skrive inn et tall, tallet skal returneres.

Skriv ferdig programmet slik at programmet ber brukeren om informasjon.
Programmet skal så kjøre finnAlleFibTall med returverdien fra laBrukerSkriveInnTall.
Her kan du bruke en for-løkke.

Hvordan løste du oppgaven?
'''


def finnAlleFibTall(limit):
    forrige = 0
    current = 1
    while current <= limit:
        nytt = current + forrige
        forrige = current
        current = nytt
        print(forrige)

def laBrukerSkriveInnTall():
    inp = input("Skriv inn et tall\n>")
    grensetall = verifisert(inp)
    return grensetall



def verifisert(inp):
    ver = False
    while ver == False:
        try:
            grensetall = int(inp)
        except:
            inp = input("Skriv inn et tall (ikke bokstaver)!\n>")
        else:
            ver = True
    return grensetall

input = laBrukerSkriveInnTall()
finnAlleFibTall(input)
