from brev import Brev

dokument = Brev('Andreas','Kong Harald')

dokument.skrivLinje("Sjallabais!")
dokument.skrivLinje("Hvordan går det med deg i dag?")
dokument.skrivLinje("God bedring!")


dokument.lesBrev()
