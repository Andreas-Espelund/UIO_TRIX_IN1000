class Person:
    def __init__(self, navn):
        self._navn = navn

    def hentNavn(self):
        return self._navn


class Personsystem:
    def __init__(self):
        self._personer = []

    def leggTilPerson(self,person):
        self._personer.append(person)

    def finnPerson(self,navn):
        for person in self._personer:
            if person.hentNavn() == navn:
                return person

system = Personsystem()

personer = [Person("Ole"),Person("Frank"),Person("Monika"),Person("Guri"),Person("Morten")]

for person in personer:
    system.leggTilPerson(person)

person = system.finnPerson("Ole")

print(person.hentNavn())
