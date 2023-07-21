quant = int(input())

val = [0 for i in range(quant + 1)]
resp = [0 for i  in range(quant + 1)]
l = quant - 1
val = []
val = [0 for i in range(3)]

while l >= 0:
   
    val[0], val[1], val[2] = map(float, input().split())
    
    resp[l] = ((val[0] * 2) + (val[1] * 3) + (val[2] * 5)) / 10

    l -= 1

l = quant - 1

while l >= 0:

    print("%0.1f" %resp[l])

    l -= 1