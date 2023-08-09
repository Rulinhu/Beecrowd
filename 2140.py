nota = [2, 5, 10, 20, 50, 100]

while True:
    n, m = map(int, input().split())

    if n == m == 0:
        exit()

    troco = m - n
    nota_u = []

    while (troco > 1) and (len(nota_u) < 3):
        for i in nota[::-1]:
            q = troco // i
            for j in range(q):
                troco %= i
                nota_u.append(i)
    if len(nota_u) == 2:
        print('possible')
    else:
        print('impossible')