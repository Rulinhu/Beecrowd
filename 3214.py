e, f, c = map(int, input().split())
b = 0

vaz = e + f

while vaz >= c:
    b += 1
    vaz = vaz - c + 1

print(b)