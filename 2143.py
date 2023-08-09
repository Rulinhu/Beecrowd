while True:
    p = int(input())

    if p == 0:
        exit()

    for i in range(p):
        n = int(input())
        ped = 0

        if n % 2 == 0:
            ped = n * 2 - 2
        else:
            ped = n * 2 - 1
        print(ped)
    