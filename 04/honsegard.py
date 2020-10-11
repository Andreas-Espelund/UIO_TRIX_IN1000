'''
Filnavn: honsegard.py

Du skal skrive et program som simulerer netter i en hønsegården.
Hva som skjer, avhenger av om reven kommer, og om bonden sover eller ei.

Først skal programmet skal lese inn fra terminal hvor mange høner som i bor i gården.
Så lenge det er høner i hønsegården skal programmet kjøre.

Hver natt skal bruken svare på om reven kommer og om bonden sover.
Dette er de de forskjellige tingene som kan skje iløpet av en natt.

Dersom reven kommer og bonden sover, blir én høne spist av reven.

Dersom reven kommer og bonden ikke sover, blir ingen høner spist, og bonden
selger reveskinnet for 190 kr.


Dersom reven ikke kommer, skjer ingenting.
Eksempel på kjøring:
'''

def sjekkInt(tall):
    while tall.isdigit() == False:
        tall = input("Skriv inn tall: ")
    return int(tall)

def sjekkStr(inp):
    while inp.isalpha()==False:
        inp = input("Ugyldig input. Kun bokstaver! :")
    if inp == "ja" or inp == "nei":
        return inp
    else:
        inp = input("Vennligst tast inn 'ja' eller 'nei'")
        sjekkStr(inp)

def natt(antall):
    if sjekkStr(input("Sover bonden? ")) == "ja":
        soverBonde = True
    else:
        soverBonde = False
    if sjekkStr(input("Kommer reven?")) == "ja":
        kommerReven = True
    else:
        kommerReven = False


    if (kommerReven and soverBonde) == True:
        antall -= 1
    elif (kommerReven and (not soverBonde)) == True:
        print("Bonden selger et reveskinn og tjener 190kr. ")
    return antall





antall = sjekkInt(input("Skriv inn antall høns: "))

while antall > 0:
    antall = natt(antall)
    print(f"Det er {antall} hoens i gaarden.")
