a, b, c = map(float, input().split())

delta = (b ** 2) - 4 * a * c

if delta < 0 or a == 0:
    print("Impossivel calcular")

else:
    x1 = (-b + delta ** (1/2)) / (2 * a)

    print("R1 = %0.5f" %x1)

    x2 = (-b - delta ** (1/2)) / (2 * a)

    print("R2 = %0.5f" %x2)