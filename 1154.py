num = 0
quant = 0
n = 1

while n >= 0:
    n = int(input())
    if n >= 0:
        num += n
        quant += 1
    else:
        break

num /= quant
print("%.2f" %num)