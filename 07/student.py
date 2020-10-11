
class Student:

    def __init__(self,navn):
        self._navn = navn
        self._score = 0
        self._antDeltatt = 0

    def leggTilQuizScore(self,poeng):
        self._score += poeng
        self._antDeltatt += 1

    def gjennomsnittligScore(self):
        return self._score/self._antDeltatt

    def utskrift(self):
        print(f'Navn: {self._navn} Total score: {self._score}  Antall quizzer: {self._antDeltatt}')
