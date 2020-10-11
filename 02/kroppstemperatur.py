'''
Hos friske mennesker varierer kroppstemperaturen vanligvis mellom 36.5 og
37.5 grader. Lag et program som avgjør om en persons kroppstemperatur ligger
henholdsvis under, innenfor eller over normal kroppstemperatur.
Programmet skal lese kroppstemperaturen fra terminal.
'''
inp = float(input("Oppgi korppstemperatur :\n> "))

kroppstemperatur = inp

if 36.5 < kroppstemperatur < 37.5:
    print("Kroppstemperatur er innenfor normalen.")
elif kroppstemperatur > 37.5:
    print("Kroppstemperatur er over normalen.")
else:
    print("Kroppstemperatur er under normalen")
