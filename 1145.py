x, y = map(int, input().split())
j = 1
for i in range(1, int(y/x) + 1):
    num = ""
    for l in range(x):
        num += str(j) + " "
        j += 1
    print(num[:-1])