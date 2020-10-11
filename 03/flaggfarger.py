'''
Denne ordboken har navn på land som nøkkelverdier og fargene på flagget til
landene som innholdsverdier. Det er denne du skal bruke i oppgavene under.

OBS! Merk at vi kan skrive ordbøker og lister over flere linjer, så lenge
vi passer på komma og avsluttende "]" eller "}", som i flaggOrdbok over.

Skriv ut hele flaggOrdbok.

Legg til et nytt land i ordboken.

Skriv en prosedyre som ber om et navn som input, og skriver ut fargene på
landets flagg.
'''
flaggOrdbok = {"norge" : ["rødt", "hvitt", "blått"],
"sverige" : ["blått", "gult"],
"danmark" : ["rødt", "hvitt"],
"finland" : ["hvitt", "blått"],
"japan" : ["rødt", "hvitt"],
"gabon" : ["grønt", "gult", "blått"],
"storbritannia" : ["rødt", "blått", "hvitt"],
"chile" : ["blått", "hvitt", "rødt"]
}

print(flaggOrdbok)

flaggOrdbok["usa"] = ['rødt','hvitt','blått']

def flaggFarger():
    land = input("Oppgi land: ").lower()
    farger = flaggOrdbok[land]
    print(farger)
flaggFarger()
