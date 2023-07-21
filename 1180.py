n = int(input())
num = list(map(int, input().split()))
menor = []

for i in range(n):
    menor.insert(i, num[i])

for i in range(n):
    if num[i] == min(menor):
        posicao = i

print("Menor valor: %d"%min(menor))
print("Posicao: %d"%posicao)