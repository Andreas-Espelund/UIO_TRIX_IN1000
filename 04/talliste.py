'''
Navn: talliste.py

a) Lag et program med en while-løkke som ber bruker taste inn fem heltall og
lagrer disse i en liste kalt tall (husk: int(...)).

b) Sum av liste: Utvid programmet slik at det regner ut summen av tallene ved
hjelp av en løkke, og skriver ut resultatet.

c) Lave verdier: Legg til programkode som skriver ut alle verdiene i listen
som er mindre enn 10.

d) Søk: Legg til programkode som skriver ut en beskjed om verdien 5
finnes eller ikke finnes i listen.
'''
liste =[]
i = 0
while i < 5:
    liste.append(int(input("Skriv inn et heltall: ")))
    i += 1
print(liste)

a = 0
sum = 0
for elm in liste:
    sum = sum + liste[a]
print(f'Summen av tallene i listen er {sum}')

print("Tall som er større enn 10 i listen:")
for num in liste:
    if num > 10:
        print(num)

if 5 in liste:
    print("Tallet 5 er i listen")
else:
    print("Tallet 5 er ikke i listen")
