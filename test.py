import math

a, b, c = 4, 30, 32

pi = math.pi

s = (a+b+c)/2

vermelhas = pi * (math.sqrt((s - a)*(s - b)*(s - c) / s))**2

p = (a + b + c) / 2
triangulo = math.sqrt(p*(p - a)*(p - b)*(p - c))


raio = (a * b * c) / math.sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c))
amarelas = (pi * raio**2) - triangulo

print(amarelas)