n = int(input())
kilo = []
preco = []

for i in range(n):
    mercado = input().split(" ")
    preco.append(float(mercado[0]))
    kilo.append(int(mercado[1]))

for j in range(n):
    final = 1000 / kilo[j]
    preco[j] = final * preco[j]
    
print("{:.2f}" .format(min(preco)))