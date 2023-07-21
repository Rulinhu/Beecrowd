num = list(map(int, input().split()))

if (num[0] > num[1] and num[0] < num[2]) or (num[0] < num[1] and num[0] > num[2]):
    print("huguinho")
elif (num[1] > num[0] and num[1] < num[2]) or (num[1] < num[0] and num[1] > num[2]):
    print("zezinho")
else:
    print("luisinho")