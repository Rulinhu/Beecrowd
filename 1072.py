numval = int(input())

val = []

val = [0 for i in range(numval + 1)]

l = len(val) - 1
valin = 0
valout = 0

while l >= 1:
    
    val[l] = int(input())
    if val[l] in range(10,20 + 1):
        valin += 1
    else:
        valout += 1

    l -= 1

print("%d in" %valin)
print("%d out" %valout)