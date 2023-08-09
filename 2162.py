a = int(input())
pv = list(map(int, input().split()))

pico = 1
if pv[0] == pv[1]:
    pico = 0
for i in range(1, a - 1):
    if not ((pv[i - 1] < pv[i] > pv[i + 1]) or (pv[i - 1] > pv[i] < pv[i + 1])):
        pico = 0
        break

print(pico)