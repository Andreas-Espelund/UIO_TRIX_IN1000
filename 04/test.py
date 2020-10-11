def setTarget():
    x =input("Skriv inn x koordiant: ")
    y =input("Skriv inn y koordiant: ")
    # skattekart[x][y] = "X "
    global target
    target = str(x)+str(y)

def takeGuess():
    x =input("Skriv inn x koordiant: ")
    y =input("Skriv inn y koordiant: ")
    # skattekart[x][y] = "X "
    global guess
    guess = str(x)+str(y)
setTarget()
takeGuess()
print(guess,target)
