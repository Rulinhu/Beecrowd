while True:
    try:
        m, n = map(int, input().split())

        resm = 1
        resn = 1

        if m == 0:
            resm = 1
        else:
            for i in range(1, m + 1):
                resm = i * resm
        if n == 0:
            resn = 1
        else:
            for i in range(1, n + 1):
                resn = i * resn

        print(resm + resn)

    except EOFError:
        break