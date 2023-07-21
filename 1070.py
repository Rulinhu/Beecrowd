num = int(input())
final = num + 11

for temp in range(num, final + 1):
    if temp % 2 != 0:
        print(temp)