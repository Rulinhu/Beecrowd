while True:
    a, b = map(int, input().split())

    c = [0,0,0,0,0,0,0,0,0,0]
    
    if a + b == 0:
        break

    for i in range(a, b + 1):
        for j in str(i):
            c[int(j)] += 1
    
    print(' '.join(map(str, c)))

#TIME LIMIT EXCEEDED :(