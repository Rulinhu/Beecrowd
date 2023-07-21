v = float(input())

if v <= 25 and v >= 0:
	print("Intervalo [0,25]")
	
if v <= 50 and v >25:
	print("Intervalo (25,50]")
		
if v <= 75 and v > 50:
	print("Intervalo (50,75]")
	
if v <= 100 and v > 75:
	print("Intervalo (75,100]")
	
if v < 0 or v > 100:
	print("Fora de intervalo")