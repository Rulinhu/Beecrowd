num = []

num = [0 for i in range(5)]

num[0] = int(input())
num[1] = int(input())
num[2] = int(input())
num[3] = int(input())
num[4] = int(input())

valores = 5
par = 0
i = 0
impar = 0
positivo = 0
negativo = 0

while valores >= 1:

    if num[i] % 2 == 0 or (num[i] * (-1)) % 2 == 0:
        par += 1
    else:
        impar += 1
    if num[i] > 0:
        positivo += 1
    if num[i] < 0:
        negativo += 1

    i = i + 1
    valores -= 1

print("%d valor(es) par(es)" %par)
print("%d valor(es) impar(es)" %impar)
print("%d valor(es) positivo(s)" %positivo)
print("%d valor(es) negativo(s)" %negativo)