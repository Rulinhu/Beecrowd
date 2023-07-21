a = int(input())

while a != 0:
    c = 0
    b = [[0 for i in range(a)] for j in range(a)]

    for m in range(a):
        for i in range(c, a - c):
            for j in range(c, a - c):
                b[i][j] = c
        c += 1

    for i in range(a):
        tx = ''
        for j in range(a):
            b[i][j] += 1
            tx += " %3d" %b[i][j]
        print(tx[1:])
    print("")

    a = int(input())