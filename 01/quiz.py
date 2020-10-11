#få brukerinput
print("Hva heter hovedstaden i Marokko?")
fasit = "Rabat"
svar = input("Svar: ")
if svar == fasit:
    print("Helt riktig!")
#elif statement tar høyde for at brukeren ikke skriver med stor bokstav i navnet
elif svar =="rabat":
    print("Helt riktig!")
else:
    print("Det er dessverre feil! Riktig svar er",fasit)
