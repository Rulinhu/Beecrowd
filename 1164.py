q = int(input())

for i in range(q):
    x = int(input())

    y = 0

    for j in range(1, x):
        if x % j == 0:
            y += j

    if x == y:
        print("%d eh perfeito" %x)
    else:
        print("%d nao eh perfeito" %x)