a = 22
b = 543
c = 8632
sisteA = a%10
sisteB = b%10
sisteC = c%10

if sisteA == sisteB:
    print(a)
    print(b)
    if sisteA == sisteC:
        print(c)
elif sisteA == sisteC:
    print (a)
    print (c)
elif sisteB == sisteC:
    print(b)
    print(c)
    
