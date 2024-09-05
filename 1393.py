while True:
    a = int(input())

    if a == 0:
        break

    num = [1, 2]

    for i in range(a):
        num.append(num[-1] + num[-2])

    print(num[a-1])