q = 0

while True:
    try:
        q += 1
        l_num = '0 '
        contagem = 0
        a = int(input())

        while contagem <= a:
            for i in range(contagem):
                l_num += str(contagem) + ' '
            contagem += 1

        print('Caso ' + str(q) + ': ' + str(len(l_num.split())) + ' numero', end='')

        if len(l_num.split()) > 1:
            print('s', end='')

        print('\n' + str(l_num[:-1]) + '\n')

    except EOFError:
        break