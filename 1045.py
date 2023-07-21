a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

if a < b:
	d = a
	a = b
	b = d
	
if b < c:
	d = b
	b = c
	c = d
	
if a < b:
	d = a
	a = b
	b = d

if a >= b + c:
	print("NAO FORMA TRIANGULO")
	
else:
	if a*a == b*b + c*c:
		print("TRIANGULO RETANGULO")
	
	if a*a > b*b + c*c:
		print("TRIANGULO OBTUSANGULO")
	
	if a*a < b*b + c*c:
		print("TRIANGULO ACUTANGULO")

	if a == b and b == c:
		print("TRIANGULO EQUILATERO")
	
	elif a == b or b == c or a == c:
		print("TRIANGULO ISOSCELES")