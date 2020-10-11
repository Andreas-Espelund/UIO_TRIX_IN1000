class Rorbu:
	def __init__(self):
		self._gjester = []

	def nyGjest(self,gjest):
		self._gjester.append(gjest)

		for elm in self._gjester:
			elm.underhold(1)

	def fortellVits(self,num):
		for elm in self._gjester:
			elm.underhold(num)

	def hvorMorsomtHarViDet(self):
		total = 0
		for elm in self._gjester:
			total += elm.hentUnderholdningsverdi()
		avg = total/len(self._gjester)

		if avg < 200:
			print("Kjedelig kveld.")
		elif avg < 400:
			print("Dette var jo litt kjekt!")
		elif avg < 600:
			print("Dette var artig!")
		else:
			print("Dra på Lopphavet - bi dæ godtar no så gyt e!")
