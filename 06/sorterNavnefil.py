
fil = open("navn.txt")
personer=[]
hunder=[]
for elm in fil:
    type = elm.split(" ")
    type[1]=type[1].strip("\n")
    if type[0] == "P":
        personer.append(type[1])
    elif type[0] == "H":
        hunder.append(type[1])


print("Personer:")
for navn in personer:
    print(navn)

print("")

print("Hunder:")
for navn in hunder:
    print(navn)
