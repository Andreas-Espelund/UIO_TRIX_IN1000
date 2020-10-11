from Rorbu import Rorbu
from Gjest import Gjest

bua = Rorbu()

for i in range(100):
	pers = Gjest()
	bua.nyGjest(pers)
	

bua.fortellVits(200)
bua.hvorMorsomtHarViDet()
bua.fortellVits(1000)
bua.hvorMorsomtHarViDet()

