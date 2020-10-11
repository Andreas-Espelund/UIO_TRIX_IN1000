def likeVedSiden(liste):
    n1 = liste[0]
    n2 = liste[1]
    i = 2
    result = False
    for i in range(2,int(len(liste))):
        if n1+n2 == liste[i]:
            print(n1,n2,liste[i])
            result = True
        n1 = n2
        n2 = i
    return result

numbers =[1,4,5,8,9,8,1,1,2]
print(likeVedSiden(numbers))
