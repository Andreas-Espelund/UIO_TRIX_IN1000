from bil import Bil
from person import Person

per = Person("Per")
ola = Person("Ola")

porche = Bil("Gul","Porche")
lambo = Bil("Rød","Lambo")
aston = Bil("Sølv","Aston Martin")
ferrarri = Bil("Grønn","Ferrarri")

per.kjopBil(porche)
per.kjopBil(lambo)
ola.kjopBil(aston)
ola.kjopBil(ferrarri)

per.laanBil(aston)
ola.laanBil(lambo)

print(ola)
print(per)
