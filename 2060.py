a = int(input())
num = list(map(int, input().split()))
d = [2, 3, 4, 5]
num_mul = [0, 0, 0, 0]

for i in num:
    for j in d:
        if i % j == 0:
            num_mul[j - 2] += 1
            
for j, i in enumerate(num_mul):
    print(str(i) + ' Multiplo(s) de ' + str(j + 2))