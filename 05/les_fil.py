fil = open("navn.txt","r")

liste =[]

for linje in fil:
    liste.append(linje)

print(liste)
