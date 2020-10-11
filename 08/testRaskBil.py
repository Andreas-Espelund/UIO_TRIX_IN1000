from RaskBil import RaskBil
aston = RaskBil("aston martin","ZZ 52321","Doris","El-bil","253kmh")
bentley = RaskBil("bently","BE 33499","Michael","Bensin","201kmh")
rolls = RaskBil("rolls royce","DP 44355","Alfred","Diesel","198kmh")

biler =[aston,bentley,rolls]

for elm in biler:
	elm.skrivInfo()

