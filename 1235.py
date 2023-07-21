b = int(input())

for c in range(b):
    code = input()

    code_r = list(code)
    code_new = []

    for a in range(int(len(code_r) / 2), len(code_r)):
        code_new.append(code_r[a])

    for a in range(int(len(code_r) / 2)):
        code_new.append(code_r[a])

    code_new.reverse()

    r2 = ''.join(code_new)

    print(r2)