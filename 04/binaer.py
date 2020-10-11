'''

Navn: binaer.py

Skriv et program som leser inn et tall og skriver ut de binære siffrene i tallet.
For å gjøre dette kan du ta tallet og skrive ut resultatet du får av operasjonen
tall % 2, så kan du erstatte tallet med tall // 2. Altså heltallsdivisjonen av tallet delt på to.

Fortsett til tallet er 0. Hvis brukeren gir tallet 27 vil altså svaret bli:

1
1
0
1
1
'''
num = int(input("Skriv inn tall: "))

while num != 0:
    print(num%2)
    num = num// 2
