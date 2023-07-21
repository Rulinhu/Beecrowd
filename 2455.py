p1, c1, p2, c2 = map(int, input().split())

e = (p1 * c1) - (p2 * c2)

if e == 0:
	print("0")
elif e > 0:
	print("-1")
else:
	print("1")