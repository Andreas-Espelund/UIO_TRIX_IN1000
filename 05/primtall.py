'''
Dette programmet tar imot et tall fra brukeren og printer alle printallene som
er mindre.
'''
#intSjek lar brukeren kun skrive inn tall
def intSjekk(num):
    while num.isdigit() == False:
        num = input("Ugyldig! Skriv inn et TALL: ")
    return num

tall = int(intSjekk(input("Skriv inn et tall: ")))

#printPrimtall sjekker om tallet n kan deles på noe annent enn seg selv og 1
def printPrimtall(n):
    count = n-1
    erPrimtall = True

    while count > 1:
        if n % count == 0:
            erPrimtall = False
        count -= 1
    if erPrimtall:
        print(f'{n} er primtall')

#while løkken sjekker alle tallene som er mindre enn tall untatt 1
while tall > 1:
    printPrimtall(tall)
    tall -= 1
