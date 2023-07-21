l=[]
for i in range(100):
    l.append(float(input()))

for i in range(100):
    if l[i]<=10:
        print("A[%d] = %.1f" %(i,l[i]))