while True:
    try:
        a = int(input())
        b = 1
        seq = 1

        while (seq % a) != 0:
            seq = (seq * 10 + 1) % a
            b += 1

        print(b)
    except EOFError:
        break