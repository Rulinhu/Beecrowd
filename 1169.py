for i in range(int(input())):
    tab = int(input())
    a = 1

    for i in range(tab):
        a *= 2

    print(str(int(a / 12 / 1000)) + ' kg')