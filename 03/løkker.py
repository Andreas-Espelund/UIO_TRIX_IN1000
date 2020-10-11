'''
a) Print ut alle tallene mellom 0 og 10. Gjør dette med en for løkke

b) Print ut alle tallene mellom 0 og 10. Gjør dette med en while løkke

c Print ut alle elemetene i liste

liste = ["Sauer","er", "myke", "dyr."]

Hvordan løste du oppgaven?
'''
#a
for i in range(11):
    print(i)

#b
a = 0
while a <= 10:
    print(a)
    a += 1
liste = ["Sauer","er", "myke", "dyr."]
for ord in liste:
    print(ord)
    
