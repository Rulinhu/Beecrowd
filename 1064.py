val = []

val = [0 for y in range(6)]

val[0] = float(input())
val[1] = float(input())
val[2] = float(input())
val[3] = float(input())
val[4] = float(input())
val[5] = float(input())

positivos = 0
numeros = 6
i = 0
media = 0

while numeros >= 1:
    if val[i] >= 0:
        positivos +=1
        media = val[i] + media
    numeros -= 1
    i += 1

media = media / positivos

print("%d valores positivos" %positivos)
print("%0.1f" %media)