for i in range(3):
    s = 0
    while True:
        piscada = input()
        if piscada != 'caw caw':
            piscada = piscada.replace('-','0')
            piscada = piscada.replace('*','1')
            s+=int(piscada, 2)
        else:
            print(s)
            break