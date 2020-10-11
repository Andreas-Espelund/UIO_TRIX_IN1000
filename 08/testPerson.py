from person import Person


def hovedprogram():
	mrSmith = Person("Brad Pitt")
	msSmith = Person("Angelina Jolie")
	
	mrSmith.myStatus()

	mrSmith.wedding(msSmith)
	
	mrSmith.myStatus()


hovedprogram()

