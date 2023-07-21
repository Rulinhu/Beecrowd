a, b = map(int, input().split(" "))

q = a // b
r = a % b

if r < 0:
    q += 1
    r = a - b * q

print(q, r)