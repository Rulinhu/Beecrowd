a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

if a < b + c and c < b + c and b < a + c:
	perimetro = a + b + c
	print("Perimetro = %0.1f" %perimetro)
	
else:
	area = ((a + b) * c) / 2
	print("Area = %0.1f" %area)