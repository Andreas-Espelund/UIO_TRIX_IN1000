from mastermind import MasterMind

def taInput():
    inp = input("Skriv inn fire tall (eks.1234): ")

    sjekka = False
    while sjekka == False:
        if inp.isdigit() and (len(inp)==4):
            sjekka = True

        else:
            print("Ugyldig input! Skriv inn 4 tall!")
            inp = input("Skriv inn fire tall (eks.1234):  ")

    return inp


def spill():
    game = MasterMind()

    count = 0
    resultat = ["X","X","X","X"]
    while "X" in resultat:
        brukerGjett = game.hent_bruker_gjett(taInput())

        resultat = game.sjekk_gjett(brukerGjett)

        print(resultat)
        count += 1

    print("Gratulerer! Du klarte det på",count,"forsøk!")
spill()
