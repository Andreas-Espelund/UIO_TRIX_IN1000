'''
En lenkeliste er en datastruktur der elementene i listen lagres av noder som ligger spredt i minnet, og disse nodene er koblet sammen med pekere.
Dette er en viktig datastruktur å gjøre seg kjent med videre i programmeringsverden. Se mer informasjon her.

I denne oppgaven skal vi lage vår egen datastruktur som holder styr på en gruppe tall. Vi skal bruke noder til å lage vår egen lenkeliste med stigende tall.

Lag klassen Node som skal ha en variabel nesteNode. Noden tar inn et tall som parameter til konstruktøren.
Lag klassen Lenkeliste som har en variabel forsteNode.
Skriv funksjonen leggTilNode i LenkeListe klassen som tar inn en node og legger den inn på riktig plass i listen. Her er det lurt å tegne!
Skriv funksjonen printLenkeliste i LenkeListe som printer ut alle tallene fra start til slutt av lenkelisten.
Hvordan løste du oppgaven?
'''
import random

class Node:
    neste = None
    def __init__(self,nytt):
        self.tall = nytt


class LenkeListe:
    forsteNode = None
    def __init__(self):
        pass

    def leggTilNode(self,node):
        if self.forsteNode == None:
            self.forsteNode = node
            return

        jobbnode = self.forsteNode

        harPlassertNode = False

        while harPlassertNode == False:
            if jobbnode.tall > node.tall:
                node.neste = jobbnode
                jobbnode.neste = node
                return

            if jobbnode.neste == None:
                jobbnode.neste = node
                return
            if jobbnode.neste.tall > node.tall:

                tmpNode = jobbnode.neste
                jobbnode.neste = node
                node.neste = tmpNode
                harPlassertNode = True

            jobbnode = jobbnode.neste


    def printer(self):
        jobbnode = self.forsteNode

        while jobbnode is not None:
            print(jobbnode.tall)
            jobbnode = jobbnode.neste

minLenkeliste = LenkeListe()
for i in range(20):
    tall = random.randint(0,10)
    minNode = Node(tall)
    minLenkeliste.leggTilNode(minNode)

minLenkeliste.printer()
