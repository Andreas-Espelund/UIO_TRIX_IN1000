# Trix oppgave 02.16 Skatt i Ruritania
def header():
    print(58*"*")
    print("** Velkommen til Ruritania's Nasjonale Skattemyndighet! **")
    print(58*"*")
header()
inntekt = float(input("Skriv inn din inntekt: "))
inntektsgrense = 10000

if inntekt < inntektsgrense:
    skatt= inntekt*0.1
else:
    skatt=inntektsgrense*0.1+(inntekt-inntektsgrense)*0.3
print(f'Du må betale {skatt:.2f} kr i skatt')
