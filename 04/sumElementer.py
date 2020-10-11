'''
Sjekker tallene i listen, se beskrivelse av funksjonen sammenlignSum
'''

liste =[8,3,4,7,9,8,1,1,2]

# sammenlignSum sjekker om summen av tall i og i+1 er lik i+2 i en liste
# viss det stemmer printes de tallene ut og returnerer True
def sammenlignSum(liste):
    result = False
    for i in range(len(liste)-2):
        if liste[i]+liste[i+1] == liste[i+2]:
            print(liste[i],liste[i+1],liste[i+2])
            result = True
    return result

sammenlignSum(liste)
