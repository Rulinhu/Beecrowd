num = []

num = [0 for y in range(5)]

num[0] = int(input())
num[1] = int(input())
num[2] = int(input())
num[3] = int(input())
num[4] = int(input())

pares = 0
numeros = 5
i = 0

while numeros >= 1:
    if num[i] % 2 == 0:
        pares +=1
    numeros -= 1
    i += 1

print("%d valores pares" %pares)