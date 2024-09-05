for i in range(int(input())):
    grades = list(map(int, input().split()))
    mm = 0
    grades.pop(0)

    media = sum(grades) / len(grades)

    for a in grades:
        if a > media:
            mm += 1
        
    mnm = round((mm * 100) / len(grades), 3)
    print("{0:.3f}%".format(mnm))