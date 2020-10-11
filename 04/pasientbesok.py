

#sjekk dato lar kun brukeren skrive inn tall mellom 1 og 31
def sjekkDato(input):

    while input.isdigit() == False:
        if int(input) in range(1,32):
            dato = int(input)
            sjekka = True
        else:
            input = input("Velg dato (1-31)")
    return dato

print(maxBesok(listeTo))
print(minBesokt(listeTo))
print(alleBesok(listeTo))
print(hvemVarPaaDato(listeTo,(input("Velg dato (1-31): "))))
