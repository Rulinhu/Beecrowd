i = 1

while i == True:
    try:
        r = int(input())

        if r >= 1:
            print("vai ter duas!")
        else:
            print("vai ter copa!")
    except:
        break