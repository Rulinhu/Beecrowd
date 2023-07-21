n = int(input())
led = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)

for i in range(n):
	num = input()
	leds = 0
	
	for j in num:
		leds += led[int(j)]
		
	print("%d leds" %int(leds))