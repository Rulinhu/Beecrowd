num_l = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900]
rom = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

num = int(input())
a = 11

for i in num_l[::-1]:
    if num // i:
        res = num // i
        num %= i
        for j in range(res):
            print(rom[a], end='')
    a -= 1
print()