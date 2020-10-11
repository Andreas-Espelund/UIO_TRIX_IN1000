from bokhylle import Bokhylle
from bok import Bok

norsk = Bok("NorskBok","Gislaug","2020")
historie = Bok("HistorieWW2","Cecilie","2010")

minHylle = Bokhylle(5)
minHylle.leggTilBok(norsk)
minHylle.leggTilBok(historie)

out = minHylle.finnBok("NorskBok","2020")
out.printBok()



