while True:
	try:
		v, t = map(int, input().split())
		
		t = t*2 * v
		
		print(t)
		
	except EOFError:
		break