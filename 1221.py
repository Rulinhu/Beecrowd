import math

for _ in range(int(input())):
    num = int(input())
    
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print('Not Prime')
            is_prime = False
            break
    
    if is_prime:
        print('Prime')