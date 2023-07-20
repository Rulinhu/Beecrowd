num = int(input())

for i in range(num):
    r, v = map(int, input().split())
    
    for j in range(min(r, v), 0, -1):
        if (r % j == 0) and (v % j == 0):
            print(j)

#incompleto