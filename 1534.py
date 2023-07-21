while True:
    try:
        q = int(input())

        num = 3

        for i in range(q):
            for j in range(q):
                if j + i == q - 1:
                    num = 2
                elif j == i:
                    num = 1
                else:
                    num = 3
                
                print(num,end="")
            print("")

    except EOFError:
        break