'''
Navn: string_liste.py

a) Lag en liste som inneholder tekststrenger.
b) Lag en løkke som går like mange ganger som listen er lang.
(Hint: Bruk en teller i en løkke).
c) Les inn tekst fra brukeren og lagre det i listen.
Skriv ut listen for å se om programmet fungerer.
'''
gjesteliste = ["Johan", "Aleksander","Håkon","Peder","Jakob","Olaf"]
i = 0
for i in range(len(gjesteliste)):
    i += 1
    gjesteliste.append(input("Legg til et navn: ").capitalize())

print(gjesteliste)
