a, b, c = map(int, input().split())

if a > b and b <= c:
	print(":)")
elif a < b and b >= c:
	print(":(")
elif a < b and b < c:
    if (b - a) > (c - b):
        print(":(")
    else:
        print(":)")
elif a > b and c < b:
    if (a - b) > (b - c):
        print(":)")
    else:
        print(":(")
else:
    if c > b:
        print(":)")
    else:
        print(":(")