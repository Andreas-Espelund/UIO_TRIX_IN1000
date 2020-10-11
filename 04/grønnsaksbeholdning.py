'''
Du driver en grønnsaksforretning og skal legge til grønnsaker i beholdningen.

a) Lag en tom ordbok beholdning.

b) Lag en løkke som kjører så lenge brukeren ønsker å fortsette å gi input.

c) Inne i løkken skal du be brukeren om å oppgi en grønnsak. Deretter skal brukeren oppgi en pris.
 Sjekk at brukeren oppgir et heltall! Hvis de oppgir gyldige verdier skal du legge til det brukeren
 har oppgitt i ordboken din, slik at grønnsaksstrengen blir en nøkkel og antallet blir den
 tilhørende verdien.

d) Når brukeren er ferdig med å oppgi grønnsaker skal du bruke en for-løkke for å skrive ut
beholdningen din. Skriv ut alle grønnsakene med tilhørende antall.

'''
beholdning = {}
def strSjekk(inp):
    ver1 = False
    while ver1 == False:
        if inp.isalpha():
            grønnsak = inp
            ver1 = True
        else:
            inp = input("Legg til grønnsak (Kun bokstaver): ").capitalize()

    return grønnsak

def intSjekk(inp):
    ver2 = False
    while ver2 == False:
        try:
            pris = int(inp)
        except:
            inp = input("Skriv inn pris (Kun heltall): ")
        else:
            ver2 = True
    return pris


add = True
while add == True:
    grønnsak = strSjekk(input("Legg til grønnsak: ").capitalize())
    pris = intSjekk(input("Skriv inn pris: "))

    beholdning[grønnsak] = pris
    valg = input("Trykk en tast for å fortsette, trykk 'F' for å fullføre: ").lower()

    if valg == "s":
        add = False

for item,pris in beholdning.items():
    print(f'{item} koster {pris} kroner.')
