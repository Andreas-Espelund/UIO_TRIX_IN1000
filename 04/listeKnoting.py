'''
I denne oppgaven skal du manipulere og jobbe med lister.

Skriv en funksjon vanligKonkat som konkatenerer to lister.
Dersom du har to lister: [a, b, c] og [1, 2, 3], skal listen som funksjonen
returnerer se slik ut: [a, b, c, 1, 2, 3]. Ikke bruk den innebygde concat-funksjonen.

Skriv funksjonen annenhverKonkat som konkatenerer to lister slik:
gitt [a, b, c] og [1, 2, 3] så skal funksjonen returnere listen: [a, 1, b, 2, c, 3].

Skriv funksjonen listesum som returnerer summen av alle tallene i en liste.
Dvs. listen [5, 3, 10] skal returnere 18.

Skriv en funksjon tallTilListe som returnerer en liste med siffer gitt et tall.
Dvs. tallet 895 skal returnere listen [8, 9, 5].

Utfordring! Skriv en funksjon erPalindrom som sjekker om et ord er et palindrom
(et ord som gir samme resultat enten det leses fra høyre eller venstre).




talliste =[1,2,3]
bokstavListe =['a','b','c']
kokListe = bokstavListe + talliste
print(kokListe)

nyListe=[]
def annenhverKonkat(liste1,liste2):
    i = 0
    for i in range(len(bokstavListe)):
        nyListe.append(liste1[i])
        nyListe.append(liste2[i])
        i += 1
    print(nyListe)

def listesum(liste):
    sum = 0
    for elm in liste:
        sum = sum + elm
    print(f'Summen av talla i lista er {sum}.')

listeMedTall=[]
def tallTilListe(tall):
    i = 0
    for i in range(len(str(tall))):
        num = str(tall)[i]
        listeMedTall.append(int(num))
        i += 1
    print(listeMedTall)


listesum(talliste)
annenhverKonkat(bokstavListe,talliste)
tallTilListe(5423)
