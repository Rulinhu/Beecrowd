a = int(input())

for i in range(a):
    cid_a, cid_b, c_a, c_b = map(float, input().split())
    cid_a, cid_b = map(int, (cid_a, cid_b))
    ano = 0

    while (cid_a <= cid_b):
        cid_a = int(cid_a * (1 + c_a / 100))
        cid_b = int(cid_b * (1 + c_b / 100))

        ano += 1
        if ano > 100:
            print("Mais de 1 seculo.")
            break

    if ano <= 100:
        print(ano,"anos.")