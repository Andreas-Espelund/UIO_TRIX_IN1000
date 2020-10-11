matriseEn = [
[1,4,7],
[2,5,8],
[3,6,9]
]
def roterMatrise(matrise):
    matriseTo=[]
    for i in range(len(matrise)):
        matriseTo.append([])
        for j in range(len(matrise)):
            matriseTo[i].append(matrise[j][i])
    return matriseTo

matriseTo = roterMatrise(matriseEn)
for elm in matriseTo:
    print(elm)
