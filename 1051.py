sal = float(input())

sali = sal

if sal > 0 and sal <= 2000:
    print("Isento")

elif sali > 2000:
    if (sal - 2000) > 1000:
        temp = 1000
    else:
        temp = sal - 2000
    
    val = temp * 0.08

    if sali > 3000:
        if (sal - 3000) > 1500:
            temp = 1500
        else:
            temp = sal - 3000
        
        val = val + (temp * 0.18)
    
    if sali > 4500:
        temp = sal - 4500
        val = val + (temp * 0.28)
    
    print("R$ %0.2f" %val)