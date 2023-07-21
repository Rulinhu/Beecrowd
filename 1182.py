m = [[0 for i in range(13)] for j in range(13)]
soma = 0
media = 0
col = int(input())
x = int(0)

sm = input()

for l in range(12):
    for c in range(12):
        m[l][c] = float(input())

for i in range(12):
    soma += m[i][col]
    if sm == "M" and i == 11:
            soma = soma / 12

print("%.1f" %soma)