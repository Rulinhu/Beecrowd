f = [0 for i in range(4)]

dm = int(input())
f[1] = int(input())
f[2] = int(input())

f[3] = dm - (f[1] + f[2])

print(max(f))