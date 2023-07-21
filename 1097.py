J = 7
I = 1
temp = 5

while I <= 9:

    print("I=%d J=%d" %(I, J))

    if J == temp:
        temp = J + 2
        I += 2
        J = J + 4
    else: 
        J -= 1