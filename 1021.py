quant = float(input())

print('NOTAS:')

n100 = int(quant // 100)
quant = quant - n100*100

print('{} nota(s) de R$ 100.00'.format(n100))

n50 = int(quant // 50)
quant = quant - n50*50

print('{} nota(s) de R$ 50.00'.format(n50))

n20 = int(quant // 20)
quant = quant - n20*20

print('{} nota(s) de R$ 20.00'.format(n20))

n10 = int(quant // 10)
quant = quant - n10*10

print('{} nota(s) de R$ 10.00'.format(n10))

n5 = int(quant // 5)
quant = quant - n5*5

print('{} nota(s) de R$ 5.00'.format(n5))

n2 = int(quant // 2)
quant = quant - n2*2

print('{} nota(s) de R$ 2.00'.format(n2))

print('MOEDAS:')

m100 = int(quant // 1)
quant = quant - m100

print('{} moeda(s) de R$ 1.00'.format(m100))

m50 = int(quant // 0.50)
quant = quant - m50/2

print('{} moeda(s) de R$ 0.50'.format(m50))

m25 = int(quant // 0.25)
quant = quant - m25/4

print('{} moeda(s) de R$ 0.25'.format(m25))

m10 = int(quant // 0.10)
quant = quant - m10/10

print('{} moeda(s) de R$ 0.10'.format(m10))

m5 = int(quant // 0.05)
quant = quant - m5/20

print('{} moeda(s) de R$ 0.05'.format(m5))

quant = quant + 0.001
m1 = quant * 100

print('%d moeda(s) de R$ 0.01' %m1)