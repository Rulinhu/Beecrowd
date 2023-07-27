while True:
    try:
        v = float(input())
        d = float(input())

        r = d / 2
        al = v / (3.14 * (r ** 2))
        ar = (3.14 * (r ** 2))

        print('ALTURA = {:.2f}'.format(al))
        print('AREA = {:.2f}'.format(ar))
    except EOFError:
        break