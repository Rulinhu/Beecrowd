q = int(input())

n = input().split()

for i in range(q):
    n[i] = int(n[i])

print(n.index(min(n)) + 1)