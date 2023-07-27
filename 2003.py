while True:
    try:
        h, m = map(int, input().split(':'))

        m_fe = 8 * 60
        m += h * 60

        atraso = (m + 60) - m_fe

        if atraso < 0:
            atraso = 0

        print('Atraso maximo: ' + str(atraso))
    except EOFError:
        break