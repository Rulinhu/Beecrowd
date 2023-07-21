x = 1

while x != 0:
    x = int(input())
    j = 1
    num = ""
    for l in range(x):
        if l == x - 1:
            print("%d" %j, end="\n")
        else:
            print("%d" %j, end=" ")
        j += 1