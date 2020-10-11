
bok = {
"Arne": 22334455,
"Lisa": 95959595,
"Jonas": 97959795,
"Peder": 12345678
}

def leggTil():
    inp = input("Legge til? (y/n)")
    if inp == "y":
        bok[navn] = int(input("Oppgi nummer:"))
        print(f'{navn} er lagt til!')
    elif inp == "n":
        print(f'{navn} blir ikke lagt til.')
    else:
        print("Beklager, jeg forstod ikke.")

navn = input("Skriv inn navn: ").capitalize()

if navn in bok:
    nummer = bok[navn]
    print(f'Nummeret til {navn} er {nummer}')
else:
    print(f'{navn} er ikke registrert.')
    leggTil()
