lista = input().split(" ")

temp = 0
a = int(lista[0])
n = int(lista[-1])

for i in range(n):
    temp = temp + i + a

print(temp)