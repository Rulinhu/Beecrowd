for i in range(int(input())):

    x, y = map(int, input().split())

    pessoitas = ['Rafael', 'Beto', 'Carlos']
    funcoes = [((3 * x)**2) + (y**2), (2*(x**2)) + ((5*y)**2), (-100*x) + (y**3)]

    print(pessoitas[funcoes.index(max(funcoes))] + ' ganhou')