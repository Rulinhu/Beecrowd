n = int(input())
num = [0 for i in range(n)]

for i in range(0, n):
    if i <= 1:
        num[i] = i
    else:
        num[i] = num[i - 1] + num[i - 2]

    if i == n-1:
        print("%d" %num[i], end="")
    else:
        print("%d" %num[i], end=" ")
print()