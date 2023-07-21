n = [0 for i in range(20)]

for j in reversed(range(20)):
    n[j] = int(input())

a = 0

for w in n:
    print("N[%d] = %d" %(a, w))
    a += 1