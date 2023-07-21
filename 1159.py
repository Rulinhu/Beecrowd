while True:
    x = int(input())

    if x % 2 != 0:
        x += 1
    elif x == 0:
        break
    
    num = x

    for j in range(4):
        num += x + 2
        x += 2

    print(num)