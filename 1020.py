idade = int(input())

ano = idade // 365
idade = idade - ano*365

meses = idade // 30
idade = idade - meses*30

dias = idade

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))