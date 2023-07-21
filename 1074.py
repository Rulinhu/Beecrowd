numval = int(input())

val = []

val = [0 for i in range(numval + 1)]

l = len(val) - 1

posneg = []
evenodd = []

posneg = [0 for i in range(numval + 1)]
evenodd = [0 for i in range(numval + 1)]

while l >= 1:
    
    val[l] = int(input())

    if val[l] > 0:
        posneg[l] = " POSITIVE"
    else:
        posneg[l] = " NEGATIVE"

    if val[l] % 2 == 0:
        evenodd[l] = "EVEN"
    else:
        evenodd[l] = "ODD"

    l -= 1

l = len(val) - 1

while l >= 1:
    if val[l] > 0 or val[l] < 0:
        print(evenodd[l] + posneg[l])
    else:
        print("NULL")

    l -= 1