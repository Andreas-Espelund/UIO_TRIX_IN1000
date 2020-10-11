'''

a) Lag en tom liste oliste. Bruk en for-løkke for å legge til strengen "o" i denne listen 5 ganger.

b) Lag en tom liste stjerneliste og legg til strengen "*" 5 ganger på samme måte som i a.

c) Lag en tom liste rutenett. Legg oliste inn i rutenett med rutenett.append(oliste).

d) Legg stjerneliste inn i rutenett på samme måte. Legg deretter inn oliste en gang til.

e) Skriv ut rutenett[0], rutenett [1] og rutenett[2] på hver sin linje. Test programmet ditt.

f) Endre programmet slik at innholdet av rutenett skrives ut ved hjelp av en enkel for-løkke.
Test programmet på nytt.
'''

#Oppgave a)
oliste =[]
i = 0
for i in range (5):
    oliste.append("o")

#Oppgave b)
stjerneliste =[]
x = 0
for x in range(5):
    stjerneliste.append("*")

#Oppgave c)
rutenett=[]
rutenett.append(oliste)
rutenett.append(stjerneliste)
rutenett.append(oliste)

for a in range(3):
    print(rutenett[a])
