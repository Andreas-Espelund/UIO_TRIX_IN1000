'''
a) Lag et program som tar et tall som input fra bruker, og printer
alle tall fra 0 opp til dette tallet (hint: while ...).

b) Utvid programmet med en ny while-løkke som ber om input fra bruker
for hver "runde". Når brukeren taster tallet 10, skal programmet avsluttes.
'''
inp = int(input("Skriv inn et tall: "))
i = 0
while i < inp:
    nyInp = int(input("Skriv inn enda et tall: "))
    while nyInp == 10:
        exit()
    print(i)
    i += 1
