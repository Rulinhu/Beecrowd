while True:
    try:
        dias_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        m, d = map(int, input().split())
        dias = 0

        if (m == 12) and (d > 25):
            print('Ja passou!')
        elif (m == 12) and (d == 25):
            print('E natal!')
        elif (m == 12) and (d == 24):
            print('E vespera de natal!')
        else:
            while ((d != 25) or (m != 12)):
                if d == dias_mes[m - 1]:
                    d = 0
                    m += 1
                dias += 1
                d += 1
            print('Faltam ' + str(dias) + ' dias para o natal!')
    
    except EOFError:
        break