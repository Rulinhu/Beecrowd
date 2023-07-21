q = int(input())

for i in range(q):
    r = 0

    for l in range(3):
        a, b = map(int, input().split())
        r += a * b

    j = r

    r = 0
    
    for l2 in range(3):
        a, b = map(int,input().split())
        r += a * b

    m = r

    if m > j:
        print("MARIA")
    else:
        print("JOAO")