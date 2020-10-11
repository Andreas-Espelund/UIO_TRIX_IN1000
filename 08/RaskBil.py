class RaskBil:
	def __init__(self,merke,regNr,navn,fuel,fart):
		self._merke = merke
		self._regNr = regNr
		self._navn = navn
		self._fuel = fuel
		self._fart = fart

	def skrivInfo(self):
		print("*****")
		print("Navn:",self._navn)
		print("Merke:",self._merke)
		print("RegNr:",self._regNr)
		print("Drifstoff:",self._fuel)
		print("Topphastighet:",self._fart)
	
