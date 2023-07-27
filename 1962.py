for i in range(int(input())):
    q = int(input())
    ano = 2015

    t_a = ano - q

    if t_a <= 0:
        print(str((t_a - 1) * -1) + ' A.C.')
    else:
        print(str(t_a) + ' D.C.')