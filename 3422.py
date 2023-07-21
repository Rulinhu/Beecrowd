q = int(input())

for i in range(q):
    l = input().split(" ")
    t = int(l[0])
    s = l[1]
    extra = 0

    if t > 45:
        extra = t - 45
    
    if extra != 0:
        t = 45

        if s == "2T":
            t += 45

        print(str(t) + "+" + str(extra))
    else:
        if s == "2T":
            t += 45
        
        print(t)