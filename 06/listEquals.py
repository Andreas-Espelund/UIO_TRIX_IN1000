'''

'''
nummer1 =[1,4,9,16,9,7,4,9,11]
nummer2 =[11,11,7,9,16,4,1]

def equals(liste_en, liste_to):

    i =0
    for elm in liste_en:
        if elm != liste_to[i]:
            return False
        i +=1
    return True


def fjernDuplikat(liste):
    nyListe = set()
    for elm in liste:
        if elm not in nyListe:
            nyListe.add(elm)
    return nyListe


def sameSet(liste_a,liste_b):
    liste_a = fjernDuplikat(liste_a)
    liste_b = fjernDuplikat(liste_b)

    for elm in liste_a:
        if elm not in liste_b:
            return False
    return True


print(equals(nummer1,nummer2))

print(sameSet(nummer1,nummer2))
