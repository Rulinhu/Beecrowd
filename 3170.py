b = int(input())
g = int(input())

if g % 2 != 0:
    g -= 1

if (g / 2) > b:
    print("Faltam %d bolinha(s)" %(g/2-b))
else:
    print("Amelia tem todas bolinhas!")