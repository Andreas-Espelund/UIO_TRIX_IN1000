'''
e) Lag tre nye Student-objekter, ved navn "Joakim", "Kristin" og "Dag".

f) Kall så metoden leggTilQuizScore på alle studentene minst to ganger hver.

g) Print ut alle studentene sin totale score og gjennomsnittelige score.
'''
from student import Student

stud1 = Student("Joakim")
stud2 = Student("Kristin")
stud3 = Student("Dag")

stud1.leggTilQuizScore(7)
stud1.leggTilQuizScore(8)

stud2.leggTilQuizScore(3)
stud2.leggTilQuizScore(7)
stud2.leggTilQuizScore(8)

stud3.leggTilQuizScore(9)
stud3.leggTilQuizScore(7)


print("***")
stud1.utskrift()
print(stud1.gjennomsnittligScore())

print("***")
stud2.utskrift()
print(stud2.gjennomsnittligScore())

print("***")
stud3.utskrift()
print(stud3.gjennomsnittligScore())

print("***")
