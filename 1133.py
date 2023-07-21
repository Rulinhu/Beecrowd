val_1 = int(input())
val_2 = int(input())

if val_1 > val_2:
    temp = val_2
    val_2 = val_1
    val_1 = temp

for i in range(val_1+1, val_2):
    if i % 5 == 2 or i % 5 == 3:
        print(i)