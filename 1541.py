while True:

    a = input()

    if a[0] == "0":
        break
    
    a, b, c = map(int, a.split())

    x = (a * b * 100 / c)**(1/2)

    print(int(x))