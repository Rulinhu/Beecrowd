x = 1

while x != 0:
	x, m = map(int, input().split())
	
	if x == 0:
		break
	
	m = x * m
	print(m)