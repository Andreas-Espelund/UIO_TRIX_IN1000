#Oppgave a)
def sifferTeller(tall):
    tall = str(tall)
    lengde = len(tall)
    return lengde

print(sifferTeller(104))


# oppgave b)
def likeBokstaver(bokstav,ord):
    count = 0
    for tegn in ord:
        if tegn == bokstav:
            count +=1
    return count

print(likeBokstaver("n","brannmann"))


# oppgave c)
def sammenligner(tall,streng):
    lengde = len(streng)
    if lengde > tall:
        return True
    else:
        return False

print(sammenligner(5,"andreas"))
