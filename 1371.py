while True:
    q = int(input())

    if q == 0:
        break

    a = 0

    portas = [0 for i in range(q)]

    for i in range(1, q + 1):
        for j in range(1, q + 1):
            if i % j == 0:
                portas[i - 1] += 1
    for i in portas:
        a += 1
        if i % 2 != 0:
            print(a, end=' ')
    print()

#TIME LIMIT EXCEDEED, muitos FOR