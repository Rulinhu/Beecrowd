j = int(input())
num = 1
for i in range(j):
    for l in range(2):
        if l == 0:
            print("%d %d %d" %(num, num**2, num**3))
        else:
            print("%d %d %d" %(num, (num**2) + 1, (num**3) + 1))
    num += 1