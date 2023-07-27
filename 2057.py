a, b, c = map(int, input().split())

hora = a + b + c

if hora >= 24:
    hora -= 24
elif hora < 0:
    hora += 24

print(hora)