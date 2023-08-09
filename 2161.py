r = int(input())
re = 3
m = 1/6
if r == 0:
    m = 0
for i in range(r-1):
    m = 1/(6 + m)
re = re + m
print('{:0.10f}'.format(re))