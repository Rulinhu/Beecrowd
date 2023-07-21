pares = []
impares = []

def check_limit(numero):
    if numero % 2 == 0 or (numero % 2)*-1 == 0:
        ip = pares
    else:
        ip = impares
    
    ip.append(numero) #anexa o numero à lista

    if len(ip) == 5: #mostra a lista
            mostra_limpa(ip)
        

def mostra_limpa(ip):
    temp = 0

    for i in ip:
        if ip == impares:
            print("im", end="")
        print("par[" + str(temp) + "] = " + str(i))
        temp += 1
        
    for i in range(len(ip)): #limpa a lista
        ip.remove(ip[0])

for num in range(15):
    numero = int(input())

    check_limit(numero)

#mostra o resto dos numeros

mostra_limpa(impares)
mostra_limpa(pares)