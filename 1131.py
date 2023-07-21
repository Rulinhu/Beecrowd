i = 0
cal = 1
inter = 0
gremio = 0
empate = 0

while cal == 1:
    gols_i, gols_g = map(float, input().split())

    if gols_i > gols_g:
        inter += 1
    elif gols_g > gols_i:
        gremio += 1
    else:
        empate += 1

    i += 1
    cal = 0
    while cal > 2 or cal < 1:
        print("Novo grenal (1-sim 2-nao)")
        cal = int(input())
    if cal == 2:
        break

print("%d grenais" %(empate + gremio + inter))
print("Inter:%d" %inter)
print("Gremio:%d" %gremio)
print("Empates:%d" %empate)

if gremio > inter:
    print("Gremio venceu mais")
elif inter > gremio:
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")


    