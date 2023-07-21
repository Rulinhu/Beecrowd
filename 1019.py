temp = int(input())

hora = int((temp / 60) // 60)
temp = temp - hora*60*60

min = int(temp // 60)
temp = temp - min*60

sec = int(temp)

print('{}:{}:{}'.format(hora,min,sec))