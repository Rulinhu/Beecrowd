val_1 = int(input())
val_2 = int(input())

soma = 0

if val_1 > val_2:
    temp = val_2
    val_2 = val_1
    val_1 = temp

for i in range(val_1, val_2):
    if i % 13 != 0:
        soma += i

print(soma)