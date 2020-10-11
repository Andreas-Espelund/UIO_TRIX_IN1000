prisListe = [
    {"salat" : 12, "fisk" : 99, "melk" : 12, "brod" :12},
    {"salat" : 22, "fisk" : 60, "melk" : 18, "brod" :21},
    {"salat" : 8, "fisk" : 120, "melk" : 10, "brod" :19},
    {"salat" : 18, "fisk" : 40, "melk" : 30, "brod" :59},
    {"salat" : 15, "fisk" : 200, "melk" : 40, "brod" :9},
    ]

butikker = ["Rema1000", "Meny", "Kiwi","Spar", "Joker"]


def finnbutikk(handleListe,butikker,prisListe):
    minstepris = 1000
    butikkIndex = 0
    teller = 0
    for butikk in prisListe:
        butikkpris = 0
        for vare in butikk:
            if (vare in handleListe):
                butikkpris += butikk[vare]
        if butikkpris < minstepris:
            minstepris = butikkpris
            butikkIndex = teller
        teller += 1

    return butikker[butikkIndex]


handleListe =['salat','melk','brod']

print(finnbutikk(handleListe,butikker,prisListe))
