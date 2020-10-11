'''
Trix oppgav 04.21

I denne oppgaven skal du lage et spill for to, der en spiller skal gjemme
en skatt i et todimensjonalt skattekart, og den andre spilleren skal
gjette hvor skatten er.
'''
import time
# Funksjonen vanskelighetsgrad gir brukeren valget mellom tre ulike størrelsar på
# spelebrettet.Funskjonen returnerer stoerrelse
def vanskelighetsgrad():
    inp = input("Velg vanskelighetsgrad (1/2/3):")
    ver = False

    while ver == False:
        try:
            grad = int(inp)
        except:
                inp = input("Velg vanskelighetsgrad (1/2/3):")
        else:
            if grad == 1 or 2 or 3:
                ver = True
            else:
                inp = input("Velg vanskelighetsgrad (1/2/3):")

    if grad is 1:
        stoerrelse = 3
        print("Kids mode aktivert!")
    elif grad is 2:

        stoerrelse = 5
        print("Medium vanskelighetsgrad!")
    else:
        stoerrelse = 8
        print("Expert mode aktivert!")
    return stoerrelse

#funksjonen lagKart lagar genererer spelebrettet ved hjelp av ei nøsta liste
#ved hjelp av stoerrelse
def lagKart():
    global skattekart
    global stoerrelse

    skattekart = []
    stoerrelse = vanskelighetsgrad()

    for e in range(stoerrelse):
        a = []
        for e in range(stoerrelse):
            a.append("O ")
        skattekart.append(a)

#printMap skriver ut den nøsta lista skattekart, men den printar kvart element
#for seg, uten ""
def printMap():
    print("")

    for e in skattekart:
        for f in e:
            print (f, end="") # Parameteret end="" soerger for at vi ikke faar linjeskift enda
        print("")
    print("")

# Listene under inneholder grafiske elementer som kan printes til brukeren
pict = [
"****************************************************************",
"( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)",
"                █───▄▀█▀▀█▀▄▄───▐█──────▄▀█▀▀█▀▄▄               ",
"               █───▀─▐▌──▐▌─▀▀──▐█─────▀─▐▌──▐▌─█▀              ",
"              ▐▌──────▀▄▄▀──────▐█▄▄──────▀▄▄▀──▐▌              ",
"              █────────────────────▀█────────────█              ",
"             ▐█─────────────────────█▌───────────█              ",
"             ▐█─────────────────────█▌───────────█              ",
"              █───────────────█▄───▄█────────────█              ",
"              ▐▌───────────────▀███▀────────────▐▌              ",
"               █──────────▀▄───────────▄▀───────█               ",
"                █───────────▀▄▄▄▄▄▄▄▄▄▀────────█                ",
"( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)",
"****************************************************************"
]
myGod = [
"       ▄▀▀▀▀▀▀▀▀▀▀▄▄",
"    ▄▀▀░░░░░░░░░░░░░▀▄",
"  ▄▀░░░░░░░░░░░░░░░░░░▀▄",
"  █░░░░░░░░░░░░░░░░░░░░░▀▄",
" ▐▌░░░░░░░░▄▄▄▄▄▄▄░░░░░░░▐▌",
" █░░░░░░░░░░░▄▄▄▄░░▀▀▀▀▀░░█",
"▐▌░░░░░░░▀▀▀▀░░░░░▀▀▀▀▀░░░▐▌",
"█░░░░░░░░░▄▄▀▀▀▀▀░░░░▀▀▀▀▄░█",
"█░░░░░░░░░░░░░░░░▀░░░▐░░░░░▐▌",
"▐▌░░░░░░░░░▐▀▀██▄░░░░░░▄▄▄░▐▌",
" █░░░░░░░░░░░▀▀▀░░░░░░▀▀██░░█",
" ▐▌░░░░▄░░░░░░░░░░░░░▌░░░░░░█",
"  ▐▌░░▐░░░░░░░░░░░░░░▀▄░░░░░█",
"   █░░░▌░░░░░░░░▐▀░░░░▄▀░░░▐▌",
"   ▐▌░░▀▄░░░░░░░░▀░▀░▀▀░░░▄▀",
"   ▐▌░░▐▀▄░░░░░░░░░░░░░░░░█",
"   ▐▌░░░▌░▀▄░░░░▀▀▀▀▀▀░░░█",
"   █░░░▀░░░░▀▄░░░░░░░░░░▄▀",
"  ▐▌░░░░░░░░░░▀▄░░░░░░▄▀",
" ▄▀░░░▄▀░░░░░░░░▀▀▀▀█▀",
"▀░░░▄▀░░░░░░░░░░▀░░░▀▀▀▀▄▄▄▄▄",
""
]
obama = [
"░░█▀░░░░░░░░░░░▀▀███████░░░░░",
"░░█▌░░░░░░░░░░░░░░░▀██████░░░",
"░█▌░░░░░░░░░░░░░░░░███████▌░░",
"░█░░░░░░░░░░░░░░░░░████████░░",
"▐▌░░░░░░░░░░░░░░░░░▀██████▌░░",
"░▌▄███▌░░░░▀████▄░░░░▀████▌░░",
"▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░",
"▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌",
"▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌",
"▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌",
"░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░",
"░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░",
"░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░",
"░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░",
"░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░",
"░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░",
"░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░",
"░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░",
"░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░",
"▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░",
"░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄",
"░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░",
"░░▄▌████████▄▄▄███████▌░░░░░▄",
"░▄▀░██████████████████▌▀▄░░░░",
"▀░░░█████▀▀░░░▀███████░░░▀▄░░",
"░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░",
"░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀",
"░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░",
"░╔╗║░╔═╗░═╦═░░░░░╔╗░░╔═╗░╦═╗░",
"░║║║░║░║░░║░░░░░░╠╩╗░╠═╣░║░║░",
"░║╚╝░╚═╝░░║░░░░░░╚═╝░║░║░╩═╝░"
]
impossible = [
"──────────────────────────────────",
"───────▄██████████████████▄───────",
"────▄███████████████████████▄─────",
"───███████████████████████████────",
"──█████████████████████████████───",
"─████████████▀─────────▀████████──",
"██████████▀───────────────▀██████─",
"███████▀────────────────────█████▌",
"██████───▄▀▀▀▀▄──────▄▀▀▀▀▄──█████",
"█████▀──────────────────▄▄▄───████",
"████────▄█████▄───────▄█▀▀▀█▄──██▀",
"████──▄█▀────▀██─────█▀────────█▀─",
"─▀██───────────▀────────▄███▄──██─",
"──██───▄▄██▀█▄──▀▄▄▄▀─▄██▄▀────███",
"▄███────▀▀▀▀▀──────────────▄▄──██▐",
"█▄▀█──▀▀▀▄▄▄▀▀───────▀▀▄▄▄▀────█▌▐",
"█▐─█────────────▄───▄──────────█▌▐",
"█▐─▀───────▐──▄▀─────▀▄──▌─────██▐",
"█─▀────────▌──▀▄─────▄▀──▐─────██▀",
"▀█─█──────▐─────▀▀▄▀▀─────▌────█──",
"─▀█▀───────▄────────────▄──────█──",
"───█─────▄▀──▄█████████▄─▀▄───▄█──",
"───█────█──▄██▀░░░░░░░▀██▄─█──█───",
"───█▄───▀▄──▀██▄█████▄██▀─▄▀─▄█───",
"────█▄────▀───▀▀▀▀──▀▀▀──▀──▄█────",
"─────█▄────────▄▀▀▀▀▀▄─────▄█─────",
"──────███▄──────────────▄▄██──────",
"─────▄█─▀█████▄▄────▄▄████▀█▄─────",
"────▄█───────▀▀██████▀▀─────█▄────",
"───▄█─────▄▀───────────▀▄────█▄───",
"──▄█─────▀───────────────▀────█▄──",
"──────────────────────────────────",
"▐▌▐█▄█▌▐▀▀█▐▀▀▌─█▀─█▀─▐▌▐▀█▐▀█─█─█",
"▐▌▐─▀─▌▐▀▀▀▐──▌─▀█─▀█─▐▌▐▀▄▐▀▄─█─█",
"▐▌▐───▌▐───▐▄▄▌─▄█─▄█─▐▌▐▄█▐─█─█▄█"
]

# grafikk printar valgt liste med grafiske element basert på parameter.
# Den bruker time.sleep for å printe linje for linje.
def grafikk(bilde):
    for elm in bilde:
        print(elm)
        time.sleep(0.03)

#verified sjekkar at brukeren skriver inn heiltal og at det ligg innafor
#størrelsen til spelebrettet
def verified(inp):
    ver = False

    while ver == False:
        try:
            output = int(inp)-1
        except:
            inp = input("Skriv inn x koordiant (kun tall): ")
        else:
            if output in range(stoerrelse):
                ver = True
            else:
                inp = input(f'Skriv inn x koordiant (1-{stoerrelse}):')
    return output

#setTarget lar spelar 1 velge kor skatten skal ligge på spelebrettet og
#viser spelaren brettet.
def setTarget():
    x = verified(input("Skriv inn x koordiant: "))
    y = verified(input("Skriv inn y koordiant: "))
    skattekart[x][y] = "X "

    global target
    target = str(x)+str(y)
    printMap()
    fortsett = input("Trykk en tast for å fortsette!")
    tomSkjerm()

#Funksjonen velkommen gir brukeren informasjon om spelet og reglane.
#den ber også om navn på bruker 1 og 2.
def velkommen():
    tomSkjerm()
    grafikk(pict)

    print(f'                    Velkommen til Skattejakt!')
    print("****************************************************************")
    print("Spiller 1 skal gjemme en skatt med koordianter (opp til 5,5)")
    print("Spiller 2 skal prøve å gjette hvor skatten er med koordianter")
    print("Spiller 2 har 3 forsøk på å gjette hvor skatten er")
    print("****************************************************************")
    print("Spillet er for to personer!")

    lagKart()
    global p1
    global p2
    p1=input("Navn på spiller 1: ").capitalize()
    p2=input("Navn på spiller 2: ").capitalize()

    print(f'{p2}, se bort mens {p1} gjemmer skatten')
    a = input("Trykk en tast for å starte!")
    tomSkjerm()

#tomSkjerm printer 100 tomme linjer for å fjerne annen informasjon som er
#på skjermen, dette gir en ryddigere bruker-interface.
def tomSkjerm():
    i = 0
    for i in range(100):
        print("")

#funksjonen takeGuess lar spiller 2 gjette koordianter
def takeGuess():
    global x
    global y

    x = verified(input("Skriv inn x koordiant: "))
    y = verified(input("Skriv inn y koordiant: "))
    skattekart[x][y] = "X "
    global guess
    guess = str(x)+str(y)

#Denne funksjonen kaller på takeGuess og sjekker om det er rett, og teller
#antall gjetninger. Spillerene får beskjed om hvem som vant og tapte.
def spiller2():
    print(f'Gjør deg klar {p2}')
    fortsett = input("Trykk en tast for å fortsette!")
    i = 0
    for i in range(3):
        takeGuess()

        if guess == target:
            tomSkjerm()
            print(f'Fulltreffer!')
            print("")
            print("******************")
            print(f'{p2} er vinneren!')
            print("******************")

            if stoerrelse is 1:
                grafikk(obama)
            elif stoerrelse is 2 or 3:
                grafikk(impossible)
            break
        else:
            skattekart[x][y]="# "
            tomSkjerm()
            igjen = 2-i
            skattekart[x][y]="# "

            if igjen == 0:
                grafikk(myGod)
                print("Bom! Ingen forsøk igjen!")
                print("")
                print("******************")
                print(f'{p1} er vinneren!')
                print("******************")
                break

            print(f'Bom! Du har {igjen} forsøk igjen.')
        i += 1

#Jeg kaller på alle funksjonene i en loop slik at spilleren kan spille på nytt
#dersom de ønsker det.
play = True
while play == True:
    velkommen()
    setTarget()
    tomSkjerm()
    spiller2()
    printMap()

    inp = input("Vil du fortsette å spille? (ja/nei): ").lower()

    if inp == "nei":
        tomSkjerm()
        play = False
