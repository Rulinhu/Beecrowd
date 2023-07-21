q = int(input())

for i in range(q):
    x = int(input())

    y = 0

    for j in range(2, x):
        if x % j == 0:
            y += j

    if y >= 1:
        print("%d nao eh primo" %x)
    else:
        print("%d eh primo" %x)