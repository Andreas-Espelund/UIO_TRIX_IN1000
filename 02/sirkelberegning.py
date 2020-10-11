import math
radius = float(input("Skriv inn sirkelens radius: "))
diameter = radius*2
Areal = math.pi*radius*radius
Omkrets = diameter * math.pi
print(f'Diameter:{diameter:10.2f}')
print(f'Areal:{Areal:13.2f}')
print(f'Omkret;{Omkrets:12.2f}')
