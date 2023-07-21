i = 0
media = 0
nota = [0 for i in range(2)]
cal = 1

while cal == 1:
    while i < 2:
        nota[i] = float(input())

        if nota[i] < 0 or nota[i] > 10:
            print("nota invalida")
        else:
            media += nota[i]
            i += 1

    media /= 2

    print("media = %0.2f" %media)
    media = 0
    i = 0
    cal = 0
    while cal > 2 or cal < 1:
        print("novo calculo (1-sim 2-nao)")
        cal = int(input())
    if cal == 2:
        break