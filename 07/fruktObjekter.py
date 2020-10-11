from frukt import Frukt

ananas = Frukt("ananas",87,"ja")
appelsin = Frukt("appelsin",88,"ja")

aprikos = Frukt("aprikos",87,"ja")
banan = Frukt("banan",76,"ja")

druer = Frukt("druer",82,"ja")
grapefrukt = Frukt("grapefrukt",89,"ja")

kiwi = Frukt("kiwi",84,"ja")
kirsebær = Frukt("kirsebær",83,"ja")

trollhegg = Frukt("trollhegg",None,"nei")
slyngsøtvier = Frukt("slyngsøtvier",None,"nei")

fruktListe=[ananas,appelsin,aprikos,banan,druer,grapefrukt,kiwi,kirsebær,
trollhegg,slyngsøtvier]

spiseligeVannFrukter=[]

for elm in fruktListe:
    if elm.hentVannPr100() is not None:
        if elm.hentVannPr100()>85 and elm.erSpiselig():
            spiseligeVannFrukter.append(elm.hentNavn())


print(spiseligeVannFrukter)
