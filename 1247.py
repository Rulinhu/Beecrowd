while True:
    try:
        d, vf, vg = map(int, input().split())
        dg = 0
        df = d

        while True:
            dg = dg + vg
            df = df + vf

            if dg >= df:
                print('S')
                break
            if df > 12 and dg < df:
                print('N')
                break

            
    except EOFError:
        break

from math import sqrt
while True:
    try:
        d, vf, vg = [int(x) for x in input().split()]
        vg = (sqrt(144 + (d * d)))/vg
        vf = 12/vf
        if vg > vf:
            print('N')
        else:
            print('S')
    except EOFError:
        break

#TERMINAR