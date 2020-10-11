from blueberryPlant import BlueberryPlant

p1 = BlueberryPlant()

def choise():
    if input("Skriv inn 'y' for å bekrefte! \n>").lower()== "y":
        return True
    else:
        return False


while True:
    print("Plantens høyde er",p1.getHeight(),"cm")
    print("Planten har",p1.getBerries(),"bær")

    print("Ønsker du å vanne planten?")
    if choise():
        p1.water()

    print("Ønsker du å befrukte planten?")
    if choise():
        p1.fertillize()
    print("Ønsker du å plukke et bær?")
    if choise():
        p1.pickBerry()
