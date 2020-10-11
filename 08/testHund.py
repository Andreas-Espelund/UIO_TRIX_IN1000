from Hund import Hund

print(Hund(10,"Puddel").hentRase())

print(Hund(12,"Labrador").hentRase())

litenValp = Hund(4,"Chihuahua")

litenValp.settAlder(10)
storValp = litenValp

storValp.settAlder(12)
litenValp = Hund(2,"Labrador")

print(storValp.hentRase())

