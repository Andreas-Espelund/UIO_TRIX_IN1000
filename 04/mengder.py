'''
Du er gitt denne listen med navn bokstaver, men du ønsker ikke å ha de samme
verdiene flere ganger. Derfor skal du overføre alle elementene til en mengde (set).
Du kan bruke mittSett.add() for å legge til elementer i mengden. Hva skjer når
man setter inn «a» for andre gang?
'''

bokstaver = ["a", "a", "b", "c"]
mittSett = {bokstaver[0]}

for elm in bokstaver:
    mittSett.add(elm)

print(mittSett)
