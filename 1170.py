for i in range(int(input())):
    comida = float(input())
    dias = 0

    while comida > 1:
        comida /= 2
        dias += 1

    print(str(dias) + ' dias')