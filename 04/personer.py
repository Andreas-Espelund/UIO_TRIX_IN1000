'''
Skriv et program der du lager en tom ordbok personer.

Skriv en while-løkke som tar input fra brukeren så lenge den svarer "y" på
spørsmål om å fortsette input. Brukeren skal oppgi to ting hver gang: Et navn og en alder.
For hver gang skal navn og alder inn i personer.

Når brukeren ikke lenger taster y skal programmet gå videre og spørre brukeren om å
oppgi en bokstav. Bruk en løkke for å fortsette å be om input frem til det blir oppgitt
gyldig input (En streng som er nøyaktig ett tegn langt).

Bruk en for-løkke for å gå gjennom nøklene i ordboken. For hver nøkkel skal
du se om den første bokstaven tilsvarer bokstaven brukeren oppgav. Isåfall
skal du skrive ut navn og alder på personen.

Hint: Når du sjekker bokstavene mot hverandre kan det lønne seg å bruke
funksjonen .lower(), som konverterer strenger til liten bokstav.

Ekstrautfordring: Kan du sørge for at brukeren blir bedt om å oppgi
alder frem til den har oppgitt en gyldig verdi (heltall)?

Hvordan løste du oppgaven?
'''

personer = {}
print("Legg til navn og alder på dine venner!")
def verStr(streng):
    while streng.isalpha()  == False:
        streng = input("Skriv inn navn: (KUN bokstaver)")
    return streng


def verInt(tall):
    while tall.isdigit() == False:
        tall = input("Skriv inn alder (KUN tall): ")
    return tall


while input("Fortsette? (y/n): ").lower() == "y":
    navn = verStr(input("Skriv inn navn: "))
    alder = verInt(input("Skriv inn alder: "))
    if navn in personer.keys():
        print(f'Oh no! {navn.capitalize()} has become age fluid!')
    personer[navn.lower()] = alder

valg = verStr(input("Velg en bokstav for å printe alle navenen med den forbokstaven! \n>"))

while int(len(valg)) != 1:
    valg = verStr(input("Oppgi EN bokstav: "))


for name in personer:
    if name[0].lower() == valg.lower():
        print(f'{name.capitalize()} er {personer[name]} år gammel.')
for name in personer:
    if name[0].lower() != valg.lower():
        print(f'{valg} er ikke forbokstav i noen sitt navn')
