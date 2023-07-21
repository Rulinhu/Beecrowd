q = int(input())

total = 0

for i in range(q):
	t, v = map(int, input().split())
	
	total += t * v
	
print(total)