while True:
    try:
        a = int(input())
        b = [[0 for i in range(a)] for j in range(a)]

        c = int(len(b) / 3)

        for i in range(a):
            b[i][i] = 2

            for j in range(a):
                if i + j == a-1:
                    b[i][j] = 3
                    
        for i in range(c, a - c):
            for j in range(c, a - c):
                b[i][j] = 1
        
        b[int(a/2)][int(a/2)] = 4

        for i in range(a):
            for j in range(a):
                print(b[i][j],end='')
            print()
        print()
    except EOFError:
        break