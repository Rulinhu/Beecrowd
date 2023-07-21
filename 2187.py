j = 1

def mvalor(num):
    n50 = num // 50
    num = num - n50 * 50
    n10 = num // 10
    num = num - n10 * 10
    n5 = num // 5
    num = num - n5 * 5
    n1 = num
    
    print(str(n50) + " " + str(n10) + " " + str(n5) + " " + str(n1))
    print("")

while True:
    num = int(input())

    if num == 0:
        break
    
    print("Teste " + str(j))
    j+=1

    mvalor(num)