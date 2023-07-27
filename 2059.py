p, j1, j2, r, a = map(int, input().split())

if a == r == 1:
    print('Jogador 2 ganha!')
elif a^r:
    print('Jogador 1 ganha!')
else:
    if ((j1 + j2) % 2)^p:
        print('Jogador 1 ganha!')
    else:
        print("Jogador 2 ganha!")