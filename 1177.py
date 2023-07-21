n = [0 for i in range(1001)]

a = int(input())
j = 0

for i in range(1000):
    print("N[%i] = %i" %(i, j))
    j += 1
    if j == a:
        j = 0