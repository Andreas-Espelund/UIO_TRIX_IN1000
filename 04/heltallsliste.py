'''
Navn: heltallsliste.py

a) Lag fem heltallsvariabler som inneholer verdiene 0,1,2,3,4.
b) Skriv ut verdiene av variablene.
c) Lag en tom liste som heter tall.
d) Legg tallene 0 til 4 inn i listen ved hjelp av en løkke.
e) Skriv ut variablene i listen ved hjelp av en løkke.
'''
Tall0 = 0
Tall1 = 1
Tall2 = 2
Tall3 = 3
Tall4 = 4
print(Tall0,Tall1,Tall2,Tall3,Tall4)
tall = []

count = 0
while count < 5:
    tall.append(count)
    count += 1

for elm in tall:
    print(elm)
