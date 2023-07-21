q = int(input())
aluno = [0 for i in range(q+1)]
nota = [0 for i in range(q+1)]

for s in range(q):
    aluno[s], nota[s] = map(float, input().split())
    aluno[s] = int(aluno[s])

aluno_maximo = aluno[nota.index(max(nota))]

if max(nota) < 8:
    print("Minimum note not reached")
else:
    print(aluno_maximo)