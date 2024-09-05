a = 0
while True:
    try:
        ano = int(input())

        if a == 1:
            print()

        #leap (4, !100, 400)
        bissexto = (((ano % 4) == 0) and (((ano % 400) == 0) or ((ano % 100) != 0)))

        #huluculu (15)
        huluculu = ((ano % 15) == 0)

        #bulukulu (55, leap = true)
        bulukulu = ((bissexto == True) and ((ano % 55) == 0))

        if bissexto == True:
            print('This is leap year.')
        if huluculu == True:
            print('This is huluculu festival year.')
        if bulukulu == True:
            print('This is bulukulu festival year.')
        if bissexto == huluculu == bulukulu == False:
            print('This is an ordinary year.')

        a = 1
    except EOFError:
        break