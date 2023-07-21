p = int(input())
val = 0

for i in range(p):
    id_q, q = map(int, input().split())
    id_q = id_q % 1000

    val += (id_q+0.50) * q
    
print("%.2f" %val)