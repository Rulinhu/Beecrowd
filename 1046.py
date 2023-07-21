i, f = map(int,input().split())

tempo = f - i

if tempo <= 0:
    tempo = tempo + 24

print("O JOGO DUROU %d HORA(S)" %tempo)