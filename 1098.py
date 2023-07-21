J = 1
I = 0
temp = 0
dec = 0
val = 0

while I <= 2:
    if(dec == 0):
        print("I=%0.0f J=%0.0f" %(I, J))
    else:
        print("I=%0.1f J=%0.1f" %(I, J))

    temp += 1

    if temp == 3:
        val += 0.2
        I += 0.2
        J = val
        temp = 0
        dec += 1

    if dec == 5:
        dec = 0
    
    J += 1