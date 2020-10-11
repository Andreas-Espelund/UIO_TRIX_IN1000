'''
Navn: kvadratet_liste.py

a) Lag en liste med tallene 1, 2, 3, 4 og 5.

b) Finn kvadratet av hvert tall, og sett det inn på dens tidligere plass i listen.

Hint: Kvadratet av 2 finner du ved å gange 2 * 2 = 4.
'''
tall = [1,2,3,4,5]
i=0
for num in tall:
    new = tall[i]**2
    tall[i]=new
    i +=1
print(tall)
