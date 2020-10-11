'''
Dette programmet sammenligner to tekststrenger streng1 og streng2. Det
sjekker om alle bokstavene som er i streng1 også er å finne i streng2. Dersom
dette er tilfelle printes det ut true, viss ikke printes false.
'''
#strsjekk krever at brukeren skriver inn bokstaver i streng1 og streng2
def strsjekk(inp):
    while inp.isalpha() == False:
        inp = input("Skriv inn ord: ")
    return inp
#strengTilListe legger alle bokstavene i en streng til i en liste
def strengTilListe(streng,liste):
    for bokstav in streng:
        liste.append(bokstav)
    return liste
#sammenlig sammenligner innholdet i streng1 og streng2 og returnerer True eller False
def sammenlign(streng1,streng2):
    liste1=[]
    liste2=[]
    strengTilListe(streng1,liste1)
    strengTilListe(streng2,liste2)

    for elm in liste1:
        if elm in liste2:
            liste2.remove(elm)
            output = True
        else:
            output = False
            break

    return output

streng1 = strsjekk(input("Skriv inn ord: "))
streng2 = strsjekk(input("skriv inn ord: "))
print(sammenlign(streng1,streng2))
