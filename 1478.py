a = int(input())

while a != 0:
    c = 0
    b = [[0 for i in range(a)] for j in range(a)]

    for i in range(a):
        for j in range(a):
            if i - j <= 0:
                b[i][j] = j - i
            else:
                b[i][j] = i - j

    for i in range(a):
        tx = ''
        for j in range(a):
            b[i][j] += 1
            tx += " %3d" %b[i][j]
        print(tx[1:])
    print("")

    a = int(input())