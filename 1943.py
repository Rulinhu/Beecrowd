pos = int(input())

top = (1, 3, 5, 10, 25, 50, 100)

for i in top:
	if i >= pos:
		i = top.index(i)
		pos = top[i]
		break
		
print("Top %d" %pos)