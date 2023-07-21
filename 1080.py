num = [0 for i in range(101)]

maior = 0

for i in range(0, 100):
    num[i] = int(input())
    
    if num[i] > maior:
        maior = num[i]
        posicao = i + 1

print(maior)
print(posicao)