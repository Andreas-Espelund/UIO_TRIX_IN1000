passasjerer = 0
#Første stopp
inp = input("Stasjon 1! Hvor mange går på bussen?")
nye = int(inp)

if passasjerer + nye >= 30:
    print(f'Bussen er full! {passasjerer+nye-30} må gå til fots')
    passasjerer = 30
else:
    print(f'{nye} passasjerer går på bussen')
    passasjerer += nye
#Første stopp
inp = input("Stasjon 2! Hvor mange går på bussen?")
nye = int(inp)

if passasjerer + nye >= 30:
    print(f'Bussen er full! {passasjerer+nye-30} må gå til fots')
    passasjerer = 30
else:
    print(f'{nye} passasjerer går på bussen')
    passasjerer += nye

#Tredje stopp

inp = input("Stasjon 3! Hvor mange går på bussen?")
nye = int(inp)

if passasjerer + nye >= 30:
    print(f'Bussen er full! {passasjerer+nye-30} må gå til fots')
    passasjerer = 30
else:
    print(f'{nye} passasjerer går på bussen')
    passasjerer += nye
print(f'Bussen er fremme med {passasjerer} passasjerer om bord.')
