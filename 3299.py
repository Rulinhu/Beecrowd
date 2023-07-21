n = int(input())
m = n

while m != 0:
    if (m % 100) - 13 == 0:
        print("%d es de Mala Suerte" %n)
        break
    else:
        m = int(m / 10)

if m == 0:
    print("%d NO es de Mala Suerte" %n)