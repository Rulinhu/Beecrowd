for i in range(int(input())):
    j1 = input()
    j2 = input()

    if j1 == 'ataque':
        if j2 == j1:
            print('Aniquilacao mutua')
        else:
            print('Jogador 1 venceu')
    elif j1 == 'papel':
        if j2 != j1:
            print('Jogador 2 venceu')
        else:
            print('Ambos venceram')
    else:
        if j1 == j2:
            print('Sem ganhador')
        elif j2 == 'papel':
            print('Jogador 1 venceu')
        else:
            print('Jogador 2 venceu')