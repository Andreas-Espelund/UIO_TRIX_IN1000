'''
Navn: reverser_liste.py

Lag en liste med verdiene 1, 2, 3, 4, 5 og 6. Lag en algoritme som reverserer listen.
Forsøk å gjøre dette uten å bruke den innebygde funksjonen reversed. Gå deretter
gjennom listen med en while-løkke og print ut alle verdiene.

Hvordan løste du oppgaven?
'''
tall = [1,2,3,4,5,6]
tallReversert = []

i = 0
lengde = len(tall)
while i < lengde:
    tallReversert.append(tall[-1])
    tall.pop()
    i += 1

tall = tallReversert
print(tall)
