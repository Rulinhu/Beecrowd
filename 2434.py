q, sal = map(int, input().split())

menor = sal

for i in range(q):
	val = int(input())
	
	sal = sal + val
	
	if menor > sal:
		menor = sal
		
print(menor)