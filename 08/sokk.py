class Sokk:

    def __init__(self,orient):
        self._orient = orient

    def hentSide(self):
        return self._orient

class Skuff:
    def __init__(self):
        self._mineSokker=[]

    def settInnSokk(self,sokk):
       (self._mineSokker).append(sokk)

    def sjekkStatus(self):
        v = 0
        h = 0
        for elm in self._mineSokker:
            if elm._orient == "venstre":
                v +=1
            else:
                h +=1

        if v == h:
            print("Alt i orden")
        else:
            print("Ulikt antall hoyre- og venstresokker")

