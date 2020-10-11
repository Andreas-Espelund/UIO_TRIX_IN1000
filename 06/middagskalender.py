'''
Lag en funksjon lesInnMatFil som leser inn en fil med et filnavn som er gitt som parameter.
I første omgang bryr vi oss kun om å lese inn navnene på matrettene,
lagre disse i din valgte datastruktur - du skal returnere denne datastrukturen.

Lag en funksjon velgMatretter som tar et tall, n, som parameter og returner n matretter
fra listen. Merk: du ønsker å velge ut matretter tilfeldig, ellers blir det meget ensformig.

Lag en funksjon skrivMatretterTilFil som skriver matrettene som er valgt
til en fil (eksempel: matplan.txt).
'''

def lesInnMatFil(filnavn):
    f = open(filnavn)
    data=[]
    for elm in f:
        ny = elm.split(",")
        data.append(ny[0])
    return data

lesInnMatFil("matliste.txt")
import random

def velgMatretter(n):
    liste = lesInnMatFil("matliste.txt")
    valg =[]
    for i in range(n):
        valg.append(random.choice(liste))
    return valg

def skrivMatretterTilFil(liste):
    out = open("randomMat.txt","w")
    for elm in liste:
        out.write(f'{elm}\n')

matretter = velgMatretter(5)

# skrivMatretterTilFil(matretter)

for i in range(15):
    print(velgMatretter(i))
