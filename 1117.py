i = 0
media = 0
nota = [0 for i in range(2)]

while i < 2:
    nota[i] = float(input())

    if nota[i] < 0 or nota[i] > 10:
        print("nota invalida")
    else:
        media += nota[i]
        i += 1

media /= 2

print("media = %0.2f" %media)