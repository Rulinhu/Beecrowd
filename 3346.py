f1, f2 = map(float, input().split())

pib = 100 + f1
pib = (pib / 100) * f2 + pib
pib = pib - 100

print("%.6f" %pib)