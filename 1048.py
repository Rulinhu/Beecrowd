sa = float(input())

if sa >= 0 and sa <= 400:
    per = 15

elif sa >= 400.01 and sa <= 800:
    per = 12

elif sa >= 800.01 and sa <= 1200:
    per = 10

elif sa >= 1200.01 and sa <= 2000:
    per = 7

else:
    per = 4

rea = sa * (per / 100)
ns = sa + rea

print("Novo salario: %0.2f" %ns)
print("Reajuste ganho: %0.2f" %rea)
print("Em percentual: " + str(per) + " %")