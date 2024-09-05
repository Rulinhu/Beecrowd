from itertools import zip_longest

while True:
    a,b = map(str, input().split())

    carry = 0
    next = 0

    if int(a) + int(b) == 0:
        break

    for c, d in zip_longest(reversed(a), reversed(b), fillvalue = 0):
        soma = int(c) + int(d) + next

        if soma >= 10:
            carry += 1
            next = 1
        else:
            next = 0
    if carry == 0:
        print('No carry operation.')
    else:
        if carry > 1:
            print(str(carry) + ' carry operations.')
        else:
            print(str(carry) + ' carry operation.')