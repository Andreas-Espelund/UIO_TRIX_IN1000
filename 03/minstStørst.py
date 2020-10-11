liste = [6,-4,7,-2,8,-3,9,-11]

minst = liste[0]
for tall in liste:
    if tall < minst:
        minst = tall
print(minst)

størst = liste[0]
for tall1 in liste:
    if tall1 > størst:
        tall1 = størst
print(størst)
