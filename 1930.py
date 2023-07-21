a = list(map(int, input().split()))

for i in range(len(a) - 1):
    a[i] -= 1
    
print(sum(a))