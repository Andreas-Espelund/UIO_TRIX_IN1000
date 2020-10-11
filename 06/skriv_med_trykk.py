'''

'''

def medTrykk(streng):
    return streng+"!"

for i in range(5):
    inp = input("Skriv et kraftuttrykk: ").capitalize()
    if inp == "Nei":
        break
    print(medTrykk(inp))
