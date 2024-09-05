num = 1
for i in range(int(input())):
    idades = list(map(int, input().split()))
    idades.pop(0)

    print('Case ' + str(num) + ': ' + str(idades[int(len(idades) / 2)]))
    num += 1