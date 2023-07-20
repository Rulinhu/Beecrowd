#TLE - TIME LIMIT EXCEDEED ??

j = 0
while True:
    j += 1
    a, b = map(int, input().split())

    if (a or b) == 0:
        exit()

    m = [0]

    for i in range(a):
        m.append(int(input()))
    m.sort()
    print('CASE# ' + str(j) + ':')

    for i in range(b):
        c = int(input())
        if c in m:
            print(str(c) + ' found at ' + str(m.index(c)))
        else:
            print(str(c) + ' not found')