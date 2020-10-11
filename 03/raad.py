'''
Filnavn: raad.py

Du skal lage et program som først tar inn saldoen på din bankkonto
(NB: Det skal være mulig å ta inn et tall med desimaler).
Deretter skal man skrive inn en totalpris på en vare du har lyst til å kjøpe.
Programmet skal deretter gi tilbakemelding om du har råd eller ikke.
'''
saldo = float(input("Hva er saldoen på din bankkonto? \n>"))
varePris = float(input("Hva koster varen? \n>"))

if varePris <= saldo:
    print("Du har raad!")
else:
    print("Du har ikke raad.")
