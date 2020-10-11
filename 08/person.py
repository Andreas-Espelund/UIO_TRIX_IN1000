
class Person:
	def __init__(self,name):
		self._name = name
		self._spouse = ""
	
	def myStatus(self):
		if self._spouse == "":
			print("ready to mingle")
		else:
			print(f"I'm married to {self._spouse}!")
	
	def wedding(self,spouse):
		self._spouse = spouse._name
		spouse._spouse = self._name

	
