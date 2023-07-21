quant = int(input())

for i in range(quant):
    val_1, val_2 = map(int, input().split())

    if val_2 == 0:
        print("divisao impossivel")
    else:
        print(val_1 / val_2)