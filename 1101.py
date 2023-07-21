M, N = map(int, input().split())

while M > 0 and N > 0:
    
    if M > N:
        temp = M
        M = N
        N = temp

    sum = 0
    
    for i in range(M, N + 1):
        print("%d" %i, end=" ")
        sum += i
        if i == N:
            print("Sum=%d" %sum)

    M, N = map(int, input().split())
