n1 = int(input())
n2 = int(input())
soma = 0

if n1 < n2:
	temp = n1
	n1 = n2
	n2 = temp
	
for i in range(n2 + 1, n1):
	if i % 2 != 0:
		soma += i
		
print(soma)