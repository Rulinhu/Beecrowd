val1 = float(input())
val2 = float(input())
val3 = float(input())
val4 = float(input())
val5 = float(input())
val6 = float(input())

valpos = 0

if val1 > 0:
    valpos +=1
if val2 > 0:
    valpos +=1
if val3 > 0:
    valpos +=1
if val4 > 0:
    valpos +=1
if val5 > 0:
    valpos +=1
if val6 > 0:
    valpos +=1

print("%d valores positivos" %valpos)