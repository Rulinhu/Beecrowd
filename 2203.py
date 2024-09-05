import math

while True:
    try:
        x1, y1, x2, y2, v, r1, r2 = map(int, input().split())

        #triangle1
        dist = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)

        dist = dist + (v * 1.5)

        if (r1 + r2) >= dist:
            print('Y')
        else:
            print('N')
    except EOFError:
        break