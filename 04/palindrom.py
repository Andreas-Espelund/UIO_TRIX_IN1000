'''
Utfordring! Skriv en funksjon erPalindrom som sjekker om et ord er et palindrom
(et ord som gir samme resultat enten det leses fra høyre eller venstre).
'''


def erPalindrom(ord):
    rev = ord [::-1]
    if ord == rev:
        print(f'{ord} er et palindrom.')
    else:
        print(f'{ord} er ikke et palindrom.')

erPalindrom(input('Skriv inn et ord: '))
