from student import Student

studenter = {}

studenter["ole"] = Student("Ole","olelie",99432312)
studenter["petter"] = Student("Petter","pethen",45334499)
studenter["stine"] = Student("Stine","stigru",49239800)

def hentInfo(navn):
    if navn in studenter:
        print("-----------------------")
        studenter[navn].printInfo()
        print("-----------------------")

    else:
        print(navn,"finnes ikke i systemet")
        valg = input(f"Ønsker du å legge til {navn}? (y/n): \n>")
        if valg == "y":
            brukernavn = input("Velg brukernavn: \n>")
            telefonnummer = input("Velg telefonnummer: \n>")
            studenter[navn] = Student(navn,brukernavn,telefonnummer)
            print("Vellykket!",navn,"er lagt til!")


inp = input("Skriv inn navn, skriv inn 'q' for å avslutte: \n>").lower()
while inp != "q":
    hentInfo(inp)
    inp = input("Skriv inn navn, skriv inn 'q' for å avslutte: \n>").lower()
