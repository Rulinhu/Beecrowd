while True:
    try:
        q = int(input())

        lesmas = map(int, input().split())

        vel_max = max(lesmas)

        if vel_max < 10:
            n = 1
        elif vel_max < 20:
            n = 2
        else:
            n = 3
        
        print(n)

    except EOFError:
        break