from sokk import Sokk
from sokk import Skuff

sok1 = Sokk("hoyre")
sok2 = Sokk("venstre")
sok3 = Sokk("venstre")
sok4 = Sokk("hoyre")


soks = [sok1,sok2,sok3,sok4]
drawer = Skuff()

for elm in soks:
    drawer.settInnSokk(elm)

drawer.sjekkStatus()

