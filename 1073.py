num = 0
resp = 0

limit = int(input())

for num in range(2, limit + 1):
    if num % 2 == 0:
        resp = num ** 2
        print("%d^2 = %d" %(num, resp))
    else:
        num +=1