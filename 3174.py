num = int(input())
trabalho = []
q = []
geral = {
    "bonecos" : 0,
    "arquitetos" : 1,
    "musicos" : 2,
    "desenhistas" : 3,
    0 : 8,
    1 : 4,
    2 : 6,
    3 : 12
}
horas = [0, 0, 0, 0]

def separacao(trabalho, q):
    brinquedos = 0
    for i in range(num):
        horas[geral.get(trabalho[i])] += q[i]
    for i in range(4):
        brinquedos += (horas[i] // geral.get(i))
    print(brinquedos)


for i in range(num):
    elfo = input().split(" ")
    trabalho.append(elfo[1])
    q.append(int(elfo[2]))

separacao(trabalho, q)