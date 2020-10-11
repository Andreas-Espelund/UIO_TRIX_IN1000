navn = input("Hva heter du? ").capitalize()
alder = int(input("Hva er din alder? "))


print("Hei, ",navn, ", fint navn!")


foerste_bokstav = navn[0]

if foerste_bokstav == "P":
    print("Navnet ditt starter med P, som Python!")
else:
    print("Jeg kjenner ingen ord som starter med ", foerste_bokstav)


alder_om_fem_aar = alder + 5

print("Om fem år skal du være", alder_om_fem_aar)


if alder >= 18:
    if alder < 100:
        drikke = "øl"
    else:
        drikke = "livets eliksir"
else:
    drikke = "brus"


print("Hei ", navn, ", har du lyst på ", drikke, "?")
