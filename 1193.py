import math

r = 0

for i in range(int(input())):
    num, tip = input().split()
    
    r += 1

    print('Case ' + str(r) + ':')

    if tip == 'bin':
        numd = int(num, 2)
        print(str(numd) + ' dec')
        print(str(hex(numd)[2:]) + ' hex')
    elif tip == 'hex':
        numd = int(num, 16)
        print(str(numd) + 'dec')
        print(str(bin(numd)[2:]) + 'bin')
    else:
        num = int(num)
        print(str(hex(num)[2:]) + ' hex')
        print(str(bin(num)[2:]) + ' bin')
    print()