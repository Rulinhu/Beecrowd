n = []
for i in range(int(input())):
    n.append(int(input()))

marcado = 0
quan = 0

for i in n:
    if i != marcado:
        marcado = i
        quan +=1

print(quan)