'''
Lag et program som ber om og leser inn to heltall.
Programmet skal deretter regne ut differansen mellom
de to tallene og skrive ut svaret.
'''
print("Oppgi veriden til x:")
x = int(input())
print("Oppgi verdien til y")
y = int(input())
# abs() gir absoluttveriden til x -y
resultat = abs(x - y)
print("differansen mellom x og y er",resultat,".")
