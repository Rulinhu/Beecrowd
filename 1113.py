val_1, val_2 = map(int, input().split())

while val_1 != val_2:
    if val_1 < val_2:
        print("Crescente")
    else:
        print("Decrescente")

    val_1, val_2 = map(int, input().split())