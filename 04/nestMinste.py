'''
I denne oppgaven skal du skrive en funksjon som returnerer det nest minste
tallet i en liste. Dette skal du gjøre uten å bruke min(). Om det minste tallet
finnes flere steder i den samme listen skal du returnere det nest minste tallet,
som ikke tilsvarer det minste. Altså [1,1,2,2,3,4,5] skal returnere 2.
'''
karakterar =[4,3,5,6,5,4,3,3,3,4,5,2,4,5,2,6]

def minsteTall(liste):
    minst=liste[0]
    for tall in liste:
        if tall < minst:
            minst = tall
    while(minst in liste):
        liste.remove(minst)

    minst=liste[0]
    for tall in liste:
        if tall < minst:
            minst = tall
    return minst

print(minsteTall(karakterar))
