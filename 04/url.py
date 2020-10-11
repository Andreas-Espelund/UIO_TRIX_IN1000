'''
denne funksjonen tar inn ei nettside og returnerer en url.
eks: NRK, returnerer www.NRK.no
'''

def url(nettsted):
    return "www."+nettsted+".no"

print(url(input("Skriv inn nettside: ")))
