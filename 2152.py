for i in range(int(input())):
    h, m, p = map(int, input().split())

    print('{:02d}:{:02d} - '.format(h, m), end='')

    if p == 1:
        print('A porta abriu!')
    else:
        print('A porta fechou!')