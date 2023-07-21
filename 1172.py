for i in range(10):
    a = int(input())

    x = [0 for i in range(10)]

    if a <= 0:
        a = 1

    print("X[%d] = %d" %(i, a))