a = int(input())

for b in range(a):
    s1,s2 = input().split(" ")
    resultad = ''
    for v in range(max(len(s1), len(s2))):
        if v < len(s1):
            resultad += s1[v]
        if v < len(s2):
            resultad += s2[v]

    print(resultad)