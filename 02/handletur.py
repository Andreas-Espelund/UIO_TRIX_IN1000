brød = 20
melk = 15
ost = 40
youghurt = 12
pose = 2

print("Hei! Velkommen til IFI - Butikken!")
brødT = brød * int(input("Hvor mange børd vil du ha? "))
melkT = melk * int(input("Hvor mange melk vil du ha?"))
ostT = ost * int(input("Hvor mange ost vil du ha?"))
youghurtT = youghurt * int(input("Hvor mange youghurt vil du ha?"))
total = brødT+melkT+ostT+youghurtT

print(f'Du skal betale {total}kr.')
