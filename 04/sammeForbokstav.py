'''
Trix oppgave 04.22
'''

personer ={}

fortsett = True
while fortsett == True:
    navn = input("Skriv inn navn: ")
    alder = int(input("Alder: "))
    personer[navn] = alder
    if input("Vil du legge inn fler? (y/n): ").lower() == "n":
        fortsett = False

inp = input("Skriv inn en bokstav: ").lower()
sjekka = False

while sjekka == False:
    try:
        int(inp)
    except:
        if len(inp) is 1:
            sjekka = True
        else:
            inp = input("Skriv inn KUN en BOKSTAV: ").lower()
    else:
        inp = input("Skriv inn KUN en BOKSTAV: ").lower()
print(inp)

for names in personer:
    print(names)
