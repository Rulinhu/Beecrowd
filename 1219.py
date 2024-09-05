import math
while True:
    try:
        a, b, c = map(int, input().split())

        s = (a+b+c)/2

        vermelhas = math.pi * (math.sqrt((s - a)*(s - b)*(s - c) / s))**2

        p = (a + b + c) / 2
        tria = math.sqrt(p*(p - a)*(p - b)*(p - c))
        azuis = tria - vermelhas

        raio = (a * b * c) / math.sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c))
        amarelas = (math.pi * raio**2) - tria

        print('{:.4f}'.format(amarelas), '{:.4f}'.format(azuis), '{:.4f}'.format(vermelhas))
    except EOFError:
        break