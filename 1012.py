A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

NUM1 = A * C / 2
NUM2 = 3.14159 * (C ** 2)
NUM3 = ((A + B) * C) / 2
NUM4 = B * B
NUM5 = A * B

print("TRIANGULO: %0.3f" %NUM1)
print("CIRCULO: %0.3f" %NUM2)
print("TRAPEZIO: %0.3f" %NUM3)
print("QUADRADO: %0.3f" %NUM4)
print("RETANGULO: %0.3f" %NUM5)