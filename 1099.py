quant = int(input())
val = [0 for i in range(quant + 1)]
impares = [0 for i in range(quant + 1)]

for i in range(0, quant):
    impar = 0
    val[i], val[i+1] = map(int, input().split())
    
    if val[i] > val[i+1]:
        temp = val[i]
        val[i] = val[i+1]
        val[i+1] = temp

    j = val[i]

    for j in range(val[i] + 1, val[i+1]):
        if j % 2 != 0:
            impar += j
        j +=1

    impares[i] = impar

    i += 2

for i in range(0, quant):
    print(impares[i])