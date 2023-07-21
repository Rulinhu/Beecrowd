q = int(input())

for i in range(q):
    n1, pi1, n2, pi2 = input().split()

    a, b = map(int, input().split())

    if (a + b) % 2 == 0:
        if pi1 == "PAR":
            print(n1)
        else:
            print(n2)
    else:
        if pi1 == "IMPAR":
            print(n1)
        else:
            print(n2)