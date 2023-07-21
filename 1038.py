cod, quant = input().split()

cod = int(cod)
quant = int(quant)

if cod == 1:
	total = quant * 4
	
if cod == 2:
	total = quant * 4.50
	
if cod == 3:
	total = quant * 5
	
if cod == 4:
	total = quant * 2
	
if cod == 5:
	total = quant * 1.50

print("Total: R$ %0.2f" %total)