while True:
    num = input()
    
    if num[:2] == '0x':
        print(int(num, 16))
    elif int(num) < 0:
        break
    else:
        print(hex(int(num))[:2] + hex(int(num))[2:].upper())