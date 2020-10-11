'''
a) Skriv en prosedyre velkommen som tar imot en variabel bruker som parameter
og skriver ut en velkomstmelding med dette navnet. Test prosedyren ved å be
bruker om en tekststreng brukernavn og kalle på velkommen med dette som parameter.

b) Skriv en funksjon strenginator(streng1, streng2) som legger sammen
(konkatenerer) to strenger med et mellomrom og returnerer den sammenslåtte strengen.
Kall på metoden med to strenger med verdi du velger selv og legg returverdien i en konkatenert.
 Skriv ut konkatenert til terminal.
'''
#Oppgave a)
def velkommen(navn):
    print(f'Hei {navn}! Velkommen til helvete!')

velkommen(input("Skriv inn ditt navn: ").capitalize())

#Oppgave b)
def strenginator(navn,etternavn):
    nyttNavn = navn + " " + etternavn
    return nyttNavn

konkatenert = strenginator(input("Fornavn: ").capitalize(),input("Etternavn:").capitalize())
print(konkatenert)
