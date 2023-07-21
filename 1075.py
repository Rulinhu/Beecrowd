val = int(input())

for odd in range(1, 10001):
    if odd % val == 2:
        print(odd)