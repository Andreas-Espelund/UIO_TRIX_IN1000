import random
from side import Side
from firkant import Firkant

def lagSider(antall):
    sider = {}
    farger = ["blå","rød","grønn","gul","oransje","hvit"]
    for i in range(antall):
        farge = farger[random.randint(0,5)]
        lengde = random.randint(1,5)
        side = Side(lengde,farge)
        sider[i] = side

    return sider

def lagFirkant():
    retninger = ["venstre","hoyre","topp","bunn"]
    sider = lagSider(4)
    nyFirkant = Firkant()
    i = 0
    for side in sider:
        retning = retninger[i]
        nySide = sider[side]
        nyFirkant.leggTilSide(nySide,retning)
        i += 1
    return nyFirkant

def flereFirkanter(antall):
    objekter={}
    for i in range(antall):
        nyFirkant = lagFirkant()
        objekter[i] = nyFirkant
    return objekter

def sjekkFirkanter(firkanter):
    status = None
    for obj in firkanter:
        firkant = firkanter[obj]
        status = firkant.erFirkant()

    return status

def lesAvFirkanter(ordbok):
    for obj in ordbok:
        print("")
        print("Firkant:")
        ordbok[obj].hentInfo()

def hovedprogram():
    firkantOrdbok = flereFirkanter(10)
    print("Er alle firkanter: ")
    print(sjekkFirkanter(firkantOrdbok))
    print("")
    print("Sideinfo: ")
    lesAvFirkanter(firkantOrdbok)

hovedprogram()

