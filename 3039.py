q = int(input())
boneca = 0
carrinho = 0

for i in range(q):
    a, s = input().split()

    if s == "F":
        boneca += 1
    else:
        carrinho += 1

print("%d carrinhos" %carrinho)
print("%d bonecas" %boneca)