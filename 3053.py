n = int(input())

m = input()

mov = [['A', 'B'],['B', 'C'],['C', 'A']]

for i in range(n):
    mov_feito = int(input())

    if m in mov[mov_feito-1]:
        if mov[mov_feito-1].index(m) == 0:
            m = mov[mov_feito-1][mov[mov_feito-1].index(m) + 1]
        else:
            m = mov[mov_feito-1][mov[mov_feito-1].index(m) - 1]
    
print(m)