'''
a) Lag en tom ordbok kalt bakeri.

b) Fyll bakeri-et med følgende varer, der navnet på bakervaren er nøkkelen, og dens tilhørende pris er verdien:

«Croissant» 25
«Grovbroed» 40
«Kneippbroed» 20
«Rosinbolle» 20
«Baguette» 10

c) Skriv ut hele ordboken.

d) Øk prisen på croissant til 30, uten å endre tidligere kode.

e) Skriv ut ordboken på nytt og sjekk at croissantens pris er endret riktig.
'''
bakeri = {
'Croissant' : 25,
'Grovbroed': 40,
'Kneippbroed' : 20,
'Rosinbolle' : 20,
'Baguette' : 10
}
print(bakeri)
bakeri['Croissant'] = 30
print(bakeri)
