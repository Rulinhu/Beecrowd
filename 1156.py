S = 1
x = 2
for i in range(4, 40):
    S += i/x
    i += 2
    x *= 2

print("%.2f"%S)