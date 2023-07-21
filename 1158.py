q = int(input())

for i in range(q):
    x, y = map(int, input().split())

    if x % 2 == 0:
            x += 1
    
    num = x

    for j in range(y - 1):
        num += x + 2
        x += 2

    print(num)