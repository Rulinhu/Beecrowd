q_e = int(input())
faz = list(map(int, input().split()))
i = 0
faz_atq = [0] * q_e

while i >= 0 and i < q_e:
    faz[i] -= 1
    faz_atq[i] = 1

    if (faz[i] + 1) % 2 == 0:
        i -= 1
    else:
        i += 1

print(faz_atq, sum(faz))

#=============================TIME LIMIT EXCEEDED :(
