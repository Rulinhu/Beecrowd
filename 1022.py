a = int(input())

for i in range(a):
    n1, sep, d1, sinal, n2, sep, d2 = input().split()
    
    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)

    if sinal == '+':
        n1 = (n1*d2 + n2*d1)
        d1 = (d1*d2)
    elif sinal == '-':
        n1 = (n1*d2 - n2*d1)
        d1 = (d1*d2)
    elif sinal == '*':
        n1 = (n1*n2)
        d1 = (d1*d2)
    else:
        n1 = (n1*d2)
        d1 = (n2*d1)

    print(str(n1) + '/' + str(d1) + ' = ', end='')

    for j in range(2, d1):
            if ((n1 % j) == 0) and ((d1 % j) == 0):
                n1 //= j
                d1 //= j

    print(str(n1) + '/' + str(d1))