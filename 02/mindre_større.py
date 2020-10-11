'''
Lag et program som tar inn et tall fra brukeren og skriver ut
om tallet er mindre eller større enn 10.
'''

tall = int(input("Tast inn et tall:"))

if tall < 10:
     print("Tallet er mindre enn 10")
elif 20 >= tall >= 10:
    print("Tallet er mellom 10 og 20")
elif tall> 20:
    print("Tallet er større enn 20")
