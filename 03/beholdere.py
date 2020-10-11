aviser = ["Aftenposten", "VG", "Morgenbladet", "Dagbladet", "Klassekampen"]

kalleNavn = {"Roger" : "Roggis", "Magnus" : "Kluten", "Stine" : "Lappen",
"Ingeborg" : "Skruen"}

parTall = {10, 8, 6, 4, 2, 0}

def utskrift(liste):
    for element in liste:
        print(element)

print("-------------")
utskrift(aviser)
print("-------------")
utskrift(kalleNavn)
print("-------------")
utskrift(kalleNavn.values())
print("-------------")
utskrift(parTall)
print("-------------")
