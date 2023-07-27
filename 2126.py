q = 0
while True:
    try:
        q += 1
        a = input()
        s = input()

        print('Caso #' + str(q) + ':')

        if a in s:
            onde = int(s.rfind(a)) + 1
            print('Qtd.Subsequencias: ' + str(s.count(a)))
            print('Pos: ' + str(onde))
        else:
            print('Nao existe subsequencia')
        print()
    
    except EOFError:
        break