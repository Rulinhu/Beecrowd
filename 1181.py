m = [[0 for i in range(13)] for j in range(13)]
soma = 0
media = 0
lin = int(input())

sm = input()

for l in range(12):
    for c in range(12):
        m[l][c] = float(input())

for i in m[lin]: #caso for a soma
    if sm == "S":
        soma += i
    else: #caso for a media
        soma += i
        if i == m[lin][11]:
            soma = soma / 12

print(soma)