class Dag:
    def __init__(self,dato,nedbor):
        self._dato = dato
        self._nedbor = nedbor

    def hentNedbor(self):
        return int(float(self._nedbor))

    def hentMaaned(self):
        biter = self._dato.split()
        maaned = biter[1]
        return maaned

    def __str__(self):
        return self._dato+":"+str(self._nedbor)



def lesFraFil(filnavn):
    datoer=[]

    fil = open(filnavn)

    for linje in fil:
        biter = linje.strip("\n").split("-")
        dato = biter[0]
        nedbor = biter[1].replace(",",".")
        nedbor = nedbor.replace("mm","")
        dag = Dag(dato,nedbor)
        datoer.append(dag)
    return datoer

def dagMax(dager):
    max = dager[0]
    for dag in dager:
        if dag.hentNedbor() > max.hentNedbor():
            max = dag
    return max

def tilsammen(dager):
    sum = 0

    for dag in dager:
        sum += dag.hentNedbor()

    return sum

def besteMaaned(dager):
    nulldager = []
    maks = dager[0].hentMaaned()
    for dag in dager:
        if dag.hentNedbor() == 0:
            nulldager.append(dag.hentMaaned())
            if nulldager.count(dag.hentMaaned()) > nulldager.count(maks):
                maks = dag.hentMaaned()

    return maks


dagListe = lesFraFil("Nedborsmengder.txt")

print(dagMax(dagListe))
print(tilsammen(dagListe))
print(besteMaaned(dagListe))
