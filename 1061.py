dia = [0 for i in range(3)]
horario = [0 for i in range(2)]
h = [0 for i in range(3)]
m = [0 for i in range(3)]
s = [0 for i in range(3)]

for i in range(2):
    dia[i] = input()

    dia[i] = int(dia[i][4:])

    horario[i] = input()

    h[i] = int(horario[i][:-10])
    m[i] = int(horario[i][5:-5])
    s[i] = int(horario[i][10:])

h[0] += dia[0]*24
h[1] += dia[1]*24

m[0] += h[0]*60
m[1] += h[1]*60

s[0] += m[0]*60
s[1] += m[1]*60

tempo = s[1]-s[0]

s[2] = tempo % 60
m[2] = (tempo / 60) % 60
h[2] = ((tempo / 60) / 60) % 24
dia[2] = ((tempo / 60) / 60) / 24

print("%d dia(s)\n%d hora(s)\n%d minuto(s)\n%d segundo(s)" %(dia[2], h[2], m[2], s[2]))