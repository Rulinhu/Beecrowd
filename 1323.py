while True:
    a = int(input())

    if a == 0:
        break
    
    total2 = 0

    for i in range(a, 0, -1):
        total2 = total2 + (i * i)

    print(total2)