num = int(input())

for i in range(num):
    temp = input()

    if temp == "P=NP":
        print("skipped")
    else:
        a, b = map(int, temp.split("+"))
        print(a+b)