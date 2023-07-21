q = int(input())

for i in range(q):
    a = int(input())

    num = [0 for j in range(a + 1)]

    for w in range(0, a + 1):
        if w <= 1:
            num[w] = w
        else:
            num[w] = num[w - 1] + num[w - 2]

    print("Fib(%d) = %d" %(a, num[a]))