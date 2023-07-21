a = int(input())

while a != 0:
    c = 0
    b = [[1 for i in range(a)] for j in range(a)]

    for i in range(a):
        for j in range(a):
            valor = b[i][j]
            valor = i + j
            l = 1

            while valor > 0:
                l *= 2
                valor-= 1

            b[i][j] = l
    

    esp = len(str(b[a-1][a-1])) + 1
    for i in range(a):
        for j in range(a):
            if j >= 1:
                print('{0:{1}}'.format(b[i][j], esp), end='')
            else:
                print('{0:{1}}'.format(b[i][j], esp - 1), end='')
        print()
    print("")

    a = int(input())