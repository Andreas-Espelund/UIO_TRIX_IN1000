'''
I denne oppgaven skal du ta i bruk modulen ezgraphics.py, som kan lastes ned her.
Legg modulen i samme mappe som flere_sirkler.py før du begynner. Detaljer om bruk av
grafikkmodulen finner du på side 63-69 i boka Python for Everyone.

a) Importer ezgraphics-modulen. Lag et vindu og et kanvas du kan tegne på.

b) Tegn en sirkel med canvas.drawOval(). Sirkelen skal ha 20 som x- og y-posisjon,
og være 50 bred og 50 høy. Bruk win.wait() for å sørge for at vinduet holder seg åpent,
og test programmet.

c) Tegn enda en sirkel. Øk x-posisjon med 100, men la resten av verdiene være de samme som
i deloppgave c. Husk at win.wait() må være i slutten av programmet. Test programmet på nytt
for å se forskjellen mellom de to sirklene.

d) Tegn enda en sirkel. Øk igjen x-posisjonen med 100, men øk denne gangen også y-posisjon
med 20. Test på nytt.

e) Skriv en ny linje der du tegner en oval. Øk x- og y-posisjon som før. Du skal i tillegg
øke høyden  (den siste verdien) med 20, slik at du nå har en oval med verdiene 320, 60, 50, 70.
'''

from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()

canvas.drawOval(20,20,50,50)
