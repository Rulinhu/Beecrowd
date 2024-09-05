teste = 1
while True:
    m = int(input())
    if m == 0:
        break

    exp = list(map(str, input().split('+')))

    for i in exp:
        try:
            if '-' in i:
                exp.remove(i)
                sub = list(i.split('-'))
                exp.append(str(sub[0] - sum(sub[1:])))
        except TypeError:
            a = 0

    print(exp)

    print('Teste', teste, '\n', sum(int(x) for x in exp), '\n')
    teste += 1

#MUITO CONFUSO (subtração // base10 erro)