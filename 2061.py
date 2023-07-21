i, a = map(int, input().split())

for w in range(a):
	af = input()
	
	if af == "clicou":
		i -= 1
	else:
		i += 1
		
print(i)