'''
b) Skriv en funksjon antall_forekomster som tar imot en liste og et heltall.
Funksjonen skal finne ut hvor mange ganger tallet som tas imot forekommer i
listen og returnere antallet forekomster.

c) Skriv en funksjon flest_forekomster som tar imot en liste og finner og
returnerer det tallet som forekommer flest ganger. Du trenger ikke ta høyde
for at flere tall kan forekomme like ofte.

d) Test begge funksjonene dine!

'''
f = open("tall.txt")
talliste =[]
for line in f:
    talliste.append(int(line.strip("\n")))
f.close()

def antall_forekomster(liste,heltall):
    teller = 0
    for elm in liste:
        if elm == heltall:
            teller += 1
    return teller

def flest_forekomster(liste):
    flest = liste[0]
    i = 0
    for elm in liste:
        if liste.count(elm) > liste.count(flest):
            flest = liste[i]
        i +=1
    return flest

print(f'Tallet 2 forekommer {antall_forekomster(talliste,2)} ganger.')
print(f'Tallet {flest_forekomster(talliste)} har flest forekomster.')
