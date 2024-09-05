for i in range(int(input())):
    a, b = map(str, input().split())

    if b == a[-len(b):]:
        print('encaixa')
    else:
        print('nao encaixa')