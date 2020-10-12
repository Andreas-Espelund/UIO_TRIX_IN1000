from Rorbu import Rorbu
from Gjest import Gjest



def fyllPåGjester(rorbu,antall):
    gjester={}

    for i in range(antall):
        gjester[i]=Gjest()
        rorbu.nyGjest(gjester[i])



def hovedprogram():
    rb1 = Rorbu()
    rb2 = Rorbu()

    rb2 = rb1 

    fyllPåGjester(rb1,50)
    fyllPåGjester(rb2,75)

    assert rb1.hentAntallGjester() == 125, "Feil antall gjester!"

    rb1.fortellVits(100)
    rb2.fortellVits(200)
    rb1.fortellVits(300)
    rb2.fortellVits(100)

    rb1.hvorMorsomtHarViDet()
    
hovedprogram()



