pul_sap, can = map(int, input().split())

canos = list(map(int, input().split()))

cano_anterior = canos[0]
p = 0

for i in canos:
    if (pul_sap + cano_anterior >= i and cano_anterior <= i) or (cano_anterior - pul_sap <= i and cano_anterior >= i):
        cano_anterior = i
        p += 1

if p == len(canos):
    print('YOU WIN')
else:
    print('GAME OVER')