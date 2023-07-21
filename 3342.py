t = int(input())

a = 1
brancas = 0
pretas = 0

for linha in range(t):
    for coluna in range(t):
        if a % 2 == 0:
            pretas += 1
        else:
            brancas += 1
        a += 1

print("%d casas brancas e %d casas pretas" %(brancas, pretas))