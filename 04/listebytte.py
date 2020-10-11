'''
Navn: listebytte.py

a) Lag et program som inneholder en heltallsliste
b) Finn minste verdi i listen
c) Finn største verdi i listen
d) Bytt plass på verdiene
e) Print listen både før og etter at du bytter plass på verdiene for å se at det blir riktig

Hvordan løste du oppgaven?
'''
tall = [10,5,1,7,8,3,2]


minst = tall[0]
storst = tall[0]
minstePlass = 0
storstePlass = 0

i = 1

while i < len(tall):
    if tall[i] < minst:
        minst = tall[i]
        minstePlass = i
    if tall[i] > storst:
        storst = tall[i]
        storstePlass = i
    i += 1
print(f'Det minste tallet er {minst}.')
print(f'Det største tallet er {storst}.')

print(f'Liste før endring: {tall}')

tmp = tall[minstePlass]
tall[minstePlass] = tall[storstePlass]
tall[storstePlass] = tmp

print(f'Liste etter endring: {tall}.')
