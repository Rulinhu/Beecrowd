A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

MaiorAB = (A + B + abs(A - B)) / 2
MaiorBC = (MaiorAB + C + abs(MaiorAB - C)) / 2

MaiorBC = int(MaiorBC)

print(MaiorBC, "eh o maior")